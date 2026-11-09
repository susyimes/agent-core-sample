"""Minimal agent-core reference runtime (standard library only).

Implements the deterministic parts of the six-layer design:
ordered prompt assembly, need/emotion decay, memory write-gate scoring,
next-goal selection, and evolution-proposal validation. All LLM-facing
prompts live as Markdown next to this file's parent folders; an LLM hook
is intentionally out of scope - feed assemble_prompt() output to your
model of choice.

Run `python core.py --help` for the CLI.
"""

import argparse
import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # template/

LAYER_FILES = [
    ("BIBLE (principles, slowest)", ROOT / "BIBLE.md"),
    ("SOUL (persona)", ROOT / "SOUL.md"),
    ("USER (human profile)", ROOT / "USER.md"),
    ("MEMORY (core)", ROOT / "memory" / "MEMORY.md"),
]
PLAYBOOK = ROOT / "memory" / "playbook.md"
HEARTBEAT = ROOT / "HEARTBEAT.md"
STATE_PATH = ROOT / "state.json"
EVO_LOG = ROOT / "evolution" / "log.jsonl"


def read_text(path):
    return Path(path).read_text(encoding="utf-8-sig")


def load_state(path=STATE_PATH):
    return json.loads(read_text(path))


def save_state(state, path=STATE_PATH):
    Path(path).write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def _decay_one(entry, hours):
    """Exponential relaxation of one axis toward its baseline."""
    value = float(entry["value"])
    baseline = float(entry.get("baseline", 0.0))
    rate = max(0.0, float(entry.get("decay_per_hour", 0.0)))
    if hours <= 0 or rate == 0:
        return value
    return baseline + (value - baseline) * math.exp(-rate * hours)


def tick(state, hours, now=None):
    """Advance all state axes by `hours`; needs also drift up by decay means
    'unmet growth' is modelled as value rising away from a low baseline only
    via events - plain relaxation is kept here for predictability.
    Returns the mutated state."""
    for group in ("needs", "emotion"):
        for entry in state.get(group, {}).values():
            entry["value"] = round(_decay_one(entry, float(hours)), 4)
    stamp = (now or datetime.now(timezone.utc)).isoformat()
    state["last_tick"] = stamp
    return state


def urgent_needs(state):
    thr = float(state.get("urgent_threshold", 0.75))
    items = [
        (name, float(e["value"]))
        for name, e in state.get("needs", {}).items()
        if float(e["value"]) >= thr
    ]
    return sorted(items, key=lambda kv: -kv[1])


def bump(state, group, name, delta):
    entry = state[group][name]
    lo, hi = (-1.0, 1.0) if name == "valence" else (0.0, 1.0)
    entry["value"] = round(max(lo, min(hi, float(entry["value"]) + delta)), 4)
    return entry["value"]


def render_state(state):
    lines = ["[STATE - needs & emotion right now]"]
    for group in ("needs", "emotion"):
        for name, e in state.get(group, {}).items():
            flag = " URGENT" if group == "needs" and float(e["value"]) >= float(
                state.get("urgent_threshold", 0.75)
            ) else ""
            lines.append(f"- {name}: {e['value']:.2f} ({e.get('label', '')}){flag}")
    lines.append("State may propose; it never decides (see BIBLE P5).")
    return "\n".join(lines)


_BULLET = re.compile(
    r"^- \[([\w-]+)\] (.+?) \|\| helpful=(\d+) harmful=(\d+)", re.MULTILINE
)


def top_playbook(path=PLAYBOOK, limit=12):
    text = read_text(path) if Path(path).exists() else ""
    bullets = [
        (m.group(1), m.group(2).strip(), int(m.group(3)) - int(m.group(4)))
        for m in _BULLET.finditer(text)
    ]
    bullets.sort(key=lambda b: -b[2])
    return bullets[:limit]


def assemble_prompt(state=None, heartbeat=False, playbook_limit=12):
    """Concatenate layers in constitutional order. Slow layers first so a
    truncated context loses state before it loses principles."""
    state = state if state is not None else load_state()
    parts = []
    for title, path in LAYER_FILES:
        if Path(path).exists():
            parts.append(f"===== {title} =====\n{read_text(path).strip()}")
    bullets = top_playbook(limit=playbook_limit)
    if bullets:
        body = "\n".join(f"- [{bid}] {text} (score {s})" for bid, text, s in bullets)
        parts.append(f"===== PLAYBOOK (top {len(bullets)}) =====\n{body}")
    parts.append(render_state(state))
    if heartbeat and HEARTBEAT.exists():
        parts.append(f"===== HEARTBEAT =====\n{read_text(HEARTBEAT).strip()}")
    return "\n\n".join(parts)


MEMORY_SIGNALS = ("insight", "decision", "emotional_turn", "stance")


def score_memory_candidate(signals):
    """Write-gate: keep only moments carrying at least two signal types."""
    hit = [s for s in MEMORY_SIGNALS if signals.get(s)]
    return {"score": len(hit), "signals": hit, "keep": len(hit) >= 2}


def next_goal(state, open_loops=(), curriculum_goal=None):
    """One driver per turn: urgent need > open loop > curriculum > silence."""
    urgent = urgent_needs(state)
    if urgent:
        return {"goal": f"address urgent need: {urgent[0][0]}", "source": "need"}
    if open_loops:
        return {"goal": str(open_loops[0]), "source": "open_loop"}
    if curriculum_goal:
        return {"goal": str(curriculum_goal), "source": "curriculum"}
    return {"goal": None, "source": "silence"}


REQUIRED_PROPOSAL = (
    "target_layer", "target_file", "failure_class", "change",
    "expected_direction", "eval_plan", "parent_version", "rollback",
)


def validate_proposal(p):
    errors = [f"missing: {k}" for k in REQUIRED_PROPOSAL if not str(p.get(k, "")).strip()]
    if str(p.get("target_layer", "")).lower() == "bible" and not p.get("human_approved"):
        errors.append("bible layer requires human_approved=true")
    if len(str(p.get("failure_class", ""))) < 8:
        errors.append("failure_class too vague (name a class, not an incident)")
    return errors


def append_proposal(p, log_path=EVO_LOG):
    errors = validate_proposal(p)
    if errors:
        raise ValueError("; ".join(errors))
    Path(log_path).parent.mkdir(parents=True, exist_ok=True)
    record = {"ts": datetime.now(timezone.utc).isoformat(), **p}
    with Path(log_path).open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    return record


def main(argv=None):
    ap = argparse.ArgumentParser(description="Agent-core reference runtime")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="print rendered state + next goal")
    a = sub.add_parser("assemble", help="print assembled layered prompt")
    a.add_argument("--heartbeat", action="store_true")
    t = sub.add_parser("tick", help="advance state by hours and save")
    t.add_argument("hours", type=float)
    b = sub.add_parser("bump", help="apply an event delta to one axis and save")
    b.add_argument("group", choices=["needs", "emotion"])
    b.add_argument("name")
    b.add_argument("delta", type=float)
    s = sub.add_parser("score", help="score a memory candidate; flags mark signals")
    for sig in MEMORY_SIGNALS:
        s.add_argument(f"--{sig}", action="store_true")
    p = sub.add_parser("propose", help="validate + append an evolution proposal JSON")
    p.add_argument("path")

    args = ap.parse_args(argv)
    if args.cmd == "status":
        state = load_state()
        print(render_state(state))
        print(json.dumps(next_goal(state), ensure_ascii=False))
    elif args.cmd == "assemble":
        print(assemble_prompt(heartbeat=args.heartbeat))
    elif args.cmd == "tick":
        state = tick(load_state(), args.hours)
        save_state(state)
        print(render_state(state))
    elif args.cmd == "bump":
        state = load_state()
        v = bump(state, args.group, args.name, args.delta)
        save_state(state)
        print(f"{args.group}.{args.name} = {v}")
    elif args.cmd == "score":
        sig = {s: getattr(args, s) for s in MEMORY_SIGNALS}
        print(json.dumps(score_memory_candidate(sig), ensure_ascii=False))
    elif args.cmd == "propose":
        try:
            rec = append_proposal(json.loads(read_text(args.path)))
        except (ValueError, KeyError, OSError) as exc:
            print(f"REJECTED: {exc}", file=sys.stderr)
            return 2
        print("LOGGED " + rec["ts"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


