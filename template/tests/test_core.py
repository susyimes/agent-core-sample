import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

CORE = Path(__file__).resolve().parents[1] / "runtime" / "core.py"
spec = importlib.util.spec_from_file_location("core", CORE)
core = importlib.util.module_from_spec(spec)
sys.modules["core"] = core
spec.loader.exec_module(core)


def fresh_state():
    return json.loads(Path(core.STATE_PATH).read_text(encoding="utf-8"))


class TestAssemblyOrder(unittest.TestCase):
    def test_principles_before_persona_before_state(self):
        text = core.assemble_prompt(state=fresh_state())
        self.assertLess(text.index("BIBLE (principles"), text.index("SOUL (persona"))
        self.assertLess(text.index("SOUL (persona"), text.index("[STATE"))
        self.assertIn("PLAYBOOK", text)

    def test_heartbeat_only_when_asked(self):
        plain = core.assemble_prompt(state=fresh_state())
        heart = core.assemble_prompt(state=fresh_state(), heartbeat=True)
        self.assertNotIn("HEARTBEAT =====", plain)
        self.assertIn("HEARTBEAT =====", heart)


class TestStateDynamics(unittest.TestCase):
    def test_decay_relaxes_toward_baseline(self):
        st = fresh_state()
        before = st["emotion"]["valence"]["value"]
        core.bump(st, "emotion", "valence", 0.5)
        core.tick(st, 10.0)
        after = st["emotion"]["valence"]["value"]
        self.assertLess(after, 0.5 + before)
        self.assertGreaterEqual(after, st["emotion"]["valence"]["baseline"])

    def test_bump_clamps(self):
        st = fresh_state()
        self.assertEqual(core.bump(st, "needs", "curiosity", 5.0), 1.0)
        self.assertEqual(core.bump(st, "emotion", "valence", -5.0), -1.0)

    def test_urgent_and_goal_priority(self):
        st = fresh_state()
        core.bump(st, "needs", "competence", 0.9)
        goal = core.next_goal(st, open_loops=["later"], curriculum_goal="explore")
        self.assertEqual(goal["source"], "need")
        goal2 = core.next_goal(fresh_state(), curriculum_goal="explore x")
        self.assertEqual(goal2["source"], "curriculum")
        self.assertIsNone(core.next_goal(fresh_state())["goal"])


class TestMemoryGate(unittest.TestCase):
    def test_requires_two_signals(self):
        self.assertFalse(core.score_memory_candidate({"insight": True})["keep"])
        r = core.score_memory_candidate({"insight": True, "stance": True})
        self.assertTrue(r["keep"] and r["score"] == 2)


class TestEvolutionGate(unittest.TestCase):
    BASE = {
        "target_layer": "playbook", "target_file": "memory/playbook.md",
        "failure_class": "overlong answers on simple lookups",
        "change": "add one bullet: answer in one line first",
        "expected_direction": "shorter replies, same accuracy",
        "eval_plan": "10 held-out lookup tasks, compare length + accuracy",
        "parent_version": "git:HEAD", "rollback": "git checkout HEAD -- memory/playbook.md",
    }

    def test_valid_proposal_logs(self):
        with tempfile.TemporaryDirectory() as td:
            log = Path(td) / "log.jsonl"
            rec = core.append_proposal(dict(self.BASE), log_path=log)
            self.assertIn("ts", rec)
            self.assertEqual(len(log.read_text(encoding="utf-8").strip().splitlines()), 1)

    def test_missing_fields_rejected(self):
        bad = dict(self.BASE); del bad["rollback"]
        self.assertTrue(core.validate_proposal(bad))

    def test_bible_requires_human_approval(self):
        p = dict(self.BASE, target_layer="bible", target_file="BIBLE.md")
        self.assertTrue(any("human_approved" in e for e in core.validate_proposal(p)))
        p["human_approved"] = True
        self.assertEqual(core.validate_proposal(p), [])


if __name__ == "__main__":
    unittest.main()
