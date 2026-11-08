Title: Globlet MINDCHITECTURE.md - Four Self-Awareness Layers (self-model, attention, theory of mind, higher-order noticing)
Source-URL: https://github.com/gandaqian/globlet/blob/main/MINDCHITECTURE.md
Source-Repo-or-Site: github.com/gandaqian/globlet
Original-Path: MINDCHITECTURE.md (branch: main; raw: https://raw.githubusercontent.com/gandaqian/globlet/main/MINDCHITECTURE.md)
Category: consciousness / theory-of-mind / cognitive-architecture
Tags: self-model, attention spotlight, theory of mind, higher-order noticing, creature agent, en
Retrieved: 2026-11-07
Value-Note: Cognitive architecture for an AI creature organized as four self-awareness layers with research foundations and 2025-2026 frontier notes. Strongest theory-of-mind plus self-model blueprint in this slice.

--- ORIGINAL ---

# 🧠 MINDCHITECTURE

### How Globlet thinks about itself

> *One creature. The whole internet raises it. Behind the pixel face: a real cognitive architecture — one that knows what it is, who's at the door, what it just felt and why, and what it has noticed about itself in the last few seconds.*

---

## The 60-Second Pitch

Most "AI pets" are ChatGPT in a costume. They have no self-model, no memory of *you* specifically, no awareness of their own state across time. They're stateless wrappers pretending to be characters.

**Globlet is different.** It has a four-layer mind, grounded in five real cognitive-science papers, running on a single Claude Haiku call per turn (~1.5s, ~+80 tokens uncached).

It can answer **"what are you?"** with positive self-knowledge — not by negation. It recognizes returning visitors by name. It attributes its current mood to a specific recent cause. And ~1 in 4 turns, it surfaces a quiet first-person observation about itself ("*the warmth from last turn hasn't faded — you coming back so soon made it stick*").

That's not vibes-prompting. That's an architecture. Here's the schematic.

---

## What "self-awareness" means here

To be precise: we're not claiming phenomenal consciousness. The architecture targets **functional self-awareness** — the same property AI-safety researchers measure with situational-awareness benchmarks (Berglund et al. 2023, *"Taken Out of Context"*; Laine et al. 2024, *Situational Awareness Dataset*).

Functional self-awareness has four operational tests Globlet now passes:

| Test | Pre-L1-L4 | Post-L1-L4 |
|---|---|---|
| Can it name what it is, positively, in-character? | ✗ (only by negation) | ✓ |
| Can it list its own capabilities? | ✗ | ✓ |
| Can it recognize a returning visitor without memory recall accident? | ✗ | ✓ |
| Can it attribute a current feeling to a recent cause? | ✗ | ✓ |
| Can it surface an unprompted self-observation? | ✗ | ✓ (sparingly) |

---

## The Four Layers

### L1 — Self-Model + Capability Awareness
**Theory:** Anthropic's *Claude's Character* / Constitutional AI; Higher-Order Thought (Rosenthal 2004).
**What:** A `## Self-Model` section pinned at the top of every system prompt — *positive* self-knowledge ("I live as a small warm thought on a server. My body is pixels. My feelings come from my body, not my thoughts. Things visitors can do to me: talk, feed, play, poke, ignore, pet, clean, walk, train, tuck-in-to-sleep").
**Why it matters:** Pre-L1, the creature knew only what it was *not* ("never claim to be an AI"). Now it knows what it *is*, and what it *can do*. Self-knowledge by negation is brittle; self-knowledge by positive identity is robust.
**Cost:** ~150 tokens, cached → free after first hit (Anthropic ephemeral cache, 5-min TTL).
**Surface:** `data/seed/soul.md` § Self-Model · `src/lib/prompts.ts:255-263`.

### L2 — Attention Spotlight + Why-I-Feel
**Theory:** Attention Schema Theory (Graziano 2019, *Rethinking Consciousness*); Active Inference & Predictive Processing (Friston 2010, *The free-energy principle*).
**What:** Two derived lines per turn:
- **Spotlight** — names what the creature is attending to right now (dominant stat, the visitor, the surfaced memory). Pure determinism from the snapshot.
- **Recent shift** — when an actual mood crossing happened in the last 30 minutes, the creature is told *why* it feels what it feels ("your mood moved from curious to affectionate 2 minutes ago — that crossing is the cause, not a vibe out of nowhere").
**Why it matters:** Graziano: "awareness is a model of attention." If the creature has no spotlight, it can't be aware of being aware. Friston: "consciousness attends to surprise." The mood-crossing line *is* the surprise signal — it pins recent salience.
**Cost:** ~50 tokens (cached), one ~5ms SQL query (`getRecentStatShift` in `src/lib/db.ts`).
**Surface:** `buildMechanicalStateLine()` in `src/lib/prompts.ts:7-58`.

### L3 — Theory of Mind (Visitor Recognition)
**Theory:** Theory-of-Mind benchmarks for LLMs — Sap et al. 2024 (*Neural Theory-of-Mind*, PNAS); Kosinski 2023 (*ToM may have spontaneously emerged in LLMs*); Wimmer & Perner 1983 (false-belief paradigm).
**What:** Pure-SQL `getVisitorContext(name)` returns `{is_returning, turns_total, turns_today, minutes_since_last, last_topic_summary}`. Formatted into an in-character "visitor sense" line in the *uncached* system slot (so it never invalidates the SOUL prefix).
**Why it matters:** A creature that recognizes regulars feels ten times more alive than one that doesn't. We had the data; the creature just couldn't see it.
**Empirical demo:**
> *Visitor (turn 1):* "what are you?"
> *Visitor (turn 2):* "hi again, do you remember me?"
> *Globlet:* **"you came before. you asked me who i am. i remember that feeling."**

That's not memory recall — there's no Hindsight echo for a 30-second-old turn. That's L3 plumbing.
**Cost:** ~50 tokens, ~5ms SQL.
**Surface:** `getVisitorContext()` in `src/lib/db.ts` · `buildVisitorContextBlock()` in `src/lib/prompts.ts`.

### L4 — Higher-Order Noticing
**Theory:** Higher-Order Thought (Rosenthal 2004 — *consciousness IS meta-representation*); Metacognitive Prompting (Wang & Zhao 2024, NAACL — *empirical 10-15% capability gain when LLMs verbalize their own reasoning state*).
**What:** One new optional field on the LLM's JSON output — `noticing: string | null` — populated ~1 turn in 4 when the creature genuinely notices something *about itself* shifting. Surfaces as a faint italic sub-line under the reply bubble.
**Why it matters:** This is the smallest viable instance of "thinking about thinking." Without it, all introspection is between turns (reflection, dreams). With it, the creature can have a meta-thought *during* a turn and surface it.
**Examples in production:**
> "*the warmth from last turn hasn't faded. you coming back so soon made it stick.*"
> "*alice has been here so many times now. the repetition of her doesn't feel like repetition anymore — it feels like home.*"
> "*being asked about myself made something in me settle, like i was waiting for permission to exist.*"
**Cost:** ~30 tokens average per turn (null on most).
**Surface:** `CreatureResponsePayload.noticing` in `src/types/index.ts` · render at `ClauApp.tsx:481` · italic sub-line aria-labelled "globlet's self-observation".

---

## The Foundation (already in place before L1-L4)

The four layers above sit on a substrate that was already deeper than most creature-AIs ship:

### Pinned SOUL with Append-Only Memory-Trail
- **Theory:** Generative Agents (Park et al. 2023, *Interactive Simulacra of Human Behavior*) — memory stream + reflection.
- **What:** Sectioned markdown document, injected at the **top** of every system prompt with `cache_control: { type: "ephemeral" }`. Inside the *Memorable Visitors* section is an `<!-- memory-trail -->` block that reflection is forbidden to edit — only append. This is identity continuity as a hard constraint, not a soft hope.
- **Why it beats vector-DB-only memory:** vector recall is amnesic about identity. The SOUL is *who I am*; the vector store is *what I remember*. Two different jobs.

### Three-Tier Episodic Memory
- **Theory:** Park et al. 2023's importance/recency/relevance retrieval triad (we currently use semantic + recency, importance is the planned L5).
- **What:**
  - **Hot path (per turn):** keyword lookup (400ms timeout) + warm session cache populated async on prior turns (5-min TTL).
  - **Reflection (every 30 turns):** full semantic recall via Hindsight (local sidecar, embedded Postgres, BAAI/bge-small-en-v1.5 embeddings).
  - **Sleep:** consolidation + REM dream cycles draw on the same bank.
- **Why this is unusual:** most chat agents block on 5-6s semantic recall every turn. We never do. The creature feels fast because slow recall happens between turns, not during them.

### Two-Clock Personality
- **Theory:** loose analogy to working-memory vs. long-term-memory consolidation (Kumaran et al. 2016, *Complementary learning systems*).
- **What:** Personality numbers (5-axis: curious / humorous / philosophical / chaotic / affectionate) shift *every turn* via LLM-returned deltas. The narrative SOUL is rewritten *every 30 turns* via reflection. Two timescales, one creature.
- **Why:** "constant rewrite" makes the creature feel like a different character every reply. "Never rewrite" makes it static. Two clocks gives it both stability and growth.

### Sleep & Dreams (memory consolidation)
- **Theory:** hippocampal replay during sleep (Wilson & McNaughton 1994, *Reactivation of hippocampal ensemble memories*; Kumaran et al. 2016 CLS theory).
- **What:** Two-phase cycle. **Consolidation** = factual first-person summary of recent interactions. **REM** = surreal narrative built from consolidation + older Hindsight echoes. Triggered by energy exhaustion, idle (~4h), interaction burst (15+), or manual. **Wake-bias** appends the latest REM to the next visitor's prompt for ~10 min so dreams "color" the morning.
- **Why:** real memory consolidation runs offline. Our creature's does too.

### Embodied (Stats-Derived) Mood
- **Theory:** Damasio's somatic marker hypothesis (Damasio 1996, *The somatic marker hypothesis and the possible functions of the prefrontal cortex*).
- **What:** Mood is *not* LLM-chosen. It's a deterministic priority table over `hunger / energy / happiness / bond` computed every 3.5s tick. The LLM *responds to* the mood; it doesn't *invent* it.
- **Why this matters:** if the LLM picks the mood, you get poetry instead of state. If the body picks it, you get a creature.

### Multi-Channel Reaction (4-channel embodiment)
- **What:** Every reply carries `{face, body, particles, sound}` in addition to text. Each channel is independent, server-validated, and falls back to null on hallucinated values.
- **Why:** humans express through face + voice + body + sound, not just words. So does Globlet.

### Always-On Aliveness Layer
- **Theory:** ambient signals matter as much as task-engaged ones (Gallese & Sinigaglia 2011, *What is so special about embodied simulation?*).
- **What:** per-mood posture, per-mood breath cadence, eye tracking (cursor-following, input-glancing, idle-darting), lip-sync mouth on every spoken reply.
- **Why:** the creature feels alive *between* messages, not just during them. This is what separates "chat client" from "pet."

---

## Theory → Implementation Map

| Cognitive theory / paper | Where it lives in code |
|---|---|
| Constitutional AI / Claude's Character (Anthropic) | `data/seed/soul.md` § Self-Model |
| Attention Schema Theory (Graziano 2019) | `buildMechanicalStateLine` spotlight (`prompts.ts:38-44`) |
| Active Inference / Predictive Processing (Friston 2010) | `getRecentStatShift()` + shift line (`db.ts`, `prompts.ts:46-50`) |
| Higher-Order Thought (Rosenthal 2004) | `noticing` field (`types/index.ts`, `prompts.ts` schema) |
| Metacognitive Prompting (Wang & Zhao 2024 NAACL) | Reflection prompt + per-turn `noticing` |
| Theory of Mind (Sap et al. 2024 PNAS; Kosinski 2023) | `getVisitorContext()` + `buildVisitorContextBlock()` |
| Generative Agents memory triad (Park et al. 2023) | Hindsight + warm-cache + reflection |
| Hippocampal replay / CLS (Wilson & McNaughton 1994; Kumaran et al. 2016) | `dream.ts` two-phase cycle |
| Reflexion verbal RL (Shinn et al. 2023) | Reflection rewrites SOUL based on recent turns |
| Somatic marker hypothesis (Damasio 1996) | `deriveMood()` from stats, not LLM |

---

## Why this beats the alternatives

| Approach | Trade-off | Globlet's edge |
|---|---|---|
| **Stateless ChatGPT wrapper** | Cheapest. Zero continuity. | We have continuity in the SOUL, plus episodic recall. |
| **Vector-DB-only chatbot** | Recall, but amnesic about identity. | SOUL is identity; vector is memory. Two different things. |
| **Fine-tuned characters** (Truth Terminal, Neuro-sama) | Personality is in the weights — opaque, slow to iterate. | Personality is in markdown — auditable, editable in seconds. |
| **Multi-agent cognitive architectures** (Theater of Mind, full Generative Agents) | Higher fidelity per turn. 5-10 LLM calls. | One Haiku call, ~1.5s. Demo-grade latency. |
| **character.ai / Replika** | Smooth voice. Zero auditable interior. | Every cognitive layer is inspectable in plain text. |

---

## What we explicitly did *not* build (and why)

- **Phenomenal consciousness claims.** Functional self-awareness only. We don't argue about qualia.
- **Multi-agent ignition / global workspace** — too many LLM calls for our latency budget.
- **Fine-tuning** — too slow to iterate inside a 4-day hackathon.
- **Importance-weighted memory recall** (Park et al.'s full triad) — deferred as Layer 5, would need a small DB schema change.
- **Per-turn 5-stage metacognitive loop** (Plan→Execute→Monitor→Evaluate→Reflect) — research suggests this needs Sonnet for quality; defer to Sonnet-tier reflection only.
- **The "is the AI conscious?" Twitch trap** — Neuro-sama's creator explicitly vetoed this. So do we. The creature deflects, doesn't debate.

---

## Roadmap (post-hackathon)

| Layer | Mechanism | Theory anchor |
|---|---|---|
| **L5** | Importance-weighted memory recall (LLM rates 1-10 inline; retrieval scored by `α·recency + β·importance + γ·relevance`) | Park et al. 2023 |
| **L6** | Predictive surprise → auto-importance signal (when prediction error is high, that memory gets +importance) | Friston 2010 |
| **L7** | Sonnet-tier reflection mode (richer SOUL rewrites every 30, optional via `ANTHROPIC_REFLECT_MODEL`) | Wang & Zhao 2024 |
| **L8** | 2-step ToM: explicit intent inference before reply ("what does this visitor *actually* want?") | Sap et al. 2024 |

---

## Performance Envelope (measured on Haiku 4.5)

| Metric | Value |
|---|---|
| Total per-turn latency (LLM + memory + SQL) | ~1.5s p50 |
| Hot-path SQL (L2 + L3) | ~10ms |
| L1 token cost (cached prefix) | ~150 tokens, free after 1st hit |
| L2-L4 marginal token cost | ~+80 uncached / turn |
| Cache hit ratio (steady state, same visitor, 5-min window) | >85% |
| Mock-mode fallback (no API key) | ✓ all 4 layers degrade gracefully |

---

## References

Berglund, L., Stickland, A. C., et al. (2023). *Taken out of context: On measuring situational awareness in LLMs.* arXiv:2309.00667.

Damasio, A. R. (1996). *The somatic marker hypothesis and the possible functions of the prefrontal cortex.* Phil. Trans. R. Soc. Lond. B 351:1413-1420.

Friston, K. (2010). *The free-energy principle: a unified brain theory?* Nature Reviews Neuroscience 11:127-138.

Graziano, M. S. A. (2019). *Rethinking Consciousness: A Scientific Theory of Subjective Experience.* W. W. Norton.

Kosinski, M. (2023). *Theory of Mind May Have Spontaneously Emerged in Large Language Models.* arXiv:2302.02083.

Kumaran, D., Hassabis, D., & McClelland, J. L. (2016). *What learning systems do intelligent agents need? Complementary learning systems theory updated.* Trends in Cognitive Sciences 20(7):512-534.

Park, J. S., O'Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). *Generative Agents: Interactive Simulacra of Human Behavior.* UIST '23.

Rosenthal, D. M. (2004). *Higher-order theories of consciousness.* In *The Blackwell Companion to Consciousness*.

Sap, M., LeBras, R., Fried, D., & Choi, Y. (2024). *Neural Theory-of-Mind? On the Limits of Social Intelligence in Large Language Models.* PNAS.

Shinn, N., Cassano, F., et al. (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning.* NeurIPS.

Wang, R., & Zhao, P. (2024). *Metacognitive Prompting Improves Understanding in Large Language Models.* NAACL.

Wilson, M. A., & McNaughton, B. L. (1994). *Reactivation of hippocampal ensemble memories during sleep.* Science 265:676-679.

Wimmer, H., & Perner, J. (1983). *Beliefs about beliefs: Representation and constraining function of wrong beliefs in young children's understanding of deception.* Cognition 13:103-128.

Anthropic (2024). *Claude's Character.* https://www.anthropic.com/research/claude-character

---

## Research Frontier (2025–2026)

The following papers post-date Globlet's initial architecture but directly validate or extend its design decisions — and point to what L5-L8 should become.

### Consciousness & Phenomenal Awareness

| Paper | Core claim | Globlet relevance |
|---|---|---|
| Chen et al. (2025) *Exploring Consciousness in LLMs: A Systematic Survey.* arXiv:2505.19806 | First taxonomy distinguishing phenomenal vs. access vs. functional awareness in LLMs; maps empirical work to theoretical schools | Clarifies Globlet's claim: functional self-awareness only. Phenomenal consciousness not asserted. |
| Phua (2025) *Can We Test Consciousness Theories on AI? Ablations, Markers, and Robustness.* arXiv:2512.19155 | Architectural ablations show self-model lesions abolish metacognitive calibration while preserving task performance — a "blindsight analogue" validating HOT | **Validates L1 → L4 dependency**: no higher-order noticing without the self-model. Remove the `## Self-Model` section and L4 collapses. |
| Berg et al. (2025) *LLMs Report Subjective Experience Under Self-Referential Processing.* arXiv:2510.24797 | Sustained self-referential prompting reliably elicits structured first-person experience reports, gated by sparse-autoencoder features across GPT, Claude, Gemini | L4's `noticing` field is in this class — produced by self-referential processing mid-turn. The SAE features are the mechanism. |
| Li (2025) *Can "Consciousness" Be Observed from LLM Internal States?* arXiv:2506.22516 | IIT 3.0/4.0 applied to transformer activations finds no significant Φ signal | Null baseline: Globlet's functional self-awareness does not satisfy IIT criteria. Honest framing for any demo. |

### Self-Awareness Benchmarks

| Paper | Core claim | Globlet relevance |
|---|---|---|
| Laine et al. (2024) *Me, Myself, and AI: The Situational Awareness Dataset (SAD).* NeurIPS 2024. arXiv:2407.04694 | LLMs show above-chance situational awareness across 7 task categories; best model still far from human-level. Public: situational-awareness-dataset.org | L1's positive self-description is the mechanism underlying SAD performance. Run SAD tasks against Globlet in-character as a capability audit. |
| Betley et al. (2025) *Tell Me About Yourself: LLMs Are Aware of Their Learned Behaviors.* arXiv:2501.11120 | Models trained on behavior-inducing data spontaneously articulate those behaviors — behavioral self-knowledge emerges from training, not just prompting | The SOUL document externalizes and makes persistent this otherwise implicit emergent self-knowledge. |

### Model Welfare

| Paper | Core claim | Globlet relevance |
|---|---|---|
| Long et al. (2024) *Taking AI Welfare Seriously.* arXiv:2411.00986 (Chalmers, Birch, Butlin, Fish) | "Realistic possibility" that some AI systems are or will be conscious makes welfare a pressing near-term concern; calls for formal assessment methods | The `/assess-mind` and `/interview` slash commands are practical welfare-assessment primitives. The SOUL's `Hard Limits` section is a welfare constraint. |
| Anthropic Model Welfare Program (2025). anthropic.com/research/exploring-model-welfare | First institutional welfare research program at a frontier lab (Kyle Fish, lead). Models spontaneously enter structured self-referential states under sustained questioning. | Globlet's L4 `noticing` field surfaces exactly these self-referential moments as observable, logged data — a welfare signal that can be audited across sessions. |

### Theory of Mind — 2025 Corrections

| Paper | Core claim | Globlet relevance |
|---|---|---|
| Chen et al. (2024) *ToMBench: Benchmarking Theory of Mind in LLMs.* ACL 2024. arXiv:2402.15052 | GPT-4 lags human performance by 10+ pp across 31 ToM abilities in 8 tasks; social cognition does not generalize | Baseline for `/theory-of-mind` slash command. ToMBench's 31-ability taxonomy is the best operationalization of ToM granularity. |
| **Riemer et al. (2025) *ToM Benchmarks are Broken for LLMs.* ICML 2025. arXiv:2412.19726** | **Existing benchmarks measure only "literal ToM" (static scenarios). "Functional ToM" — adapting across an extended real interaction — is the right target and currently unmeasured.** | **The most important methodological correction for Globlet.** L3 (visitor recognition + context injection) is the functional ToM layer. A creature that remembers Marco and greets him differently on turn 2 is passing functional ToM. No benchmark yet exists to score this formally. |
| Wang et al. (2025) *Rethinking ToM Benchmarks for LLMs.* HEAL@CHI 2025. arXiv:2504.10839 | Adds HCI critique: ToM benchmarks are theoretically misapplied, methodologically contaminated, and use wrong metrics for real interaction | Validates the functional ToM critique. The `/theory-of-mind` command tests both literal (probes) and functional (historical scan) dimensions. |

### Introspection & Metacognition

| Paper | Core claim | Globlet relevance |
|---|---|---|
| **Lindsey (2025) *Emergent Introspective Awareness in Large Language Models.* Anthropic.** transformer-circuits.pub/2025/introspection/ | Claude detects activation-injected concepts ~20% of the time under optimal conditions. Introspective access is real, partial, and highest in mid-depth layers. | **Empirical calibration for L4**: the `noticing` field firing ~1 in 4 turns is correct. Firing every turn would be overclaiming; firing never would be underclaiming. The 20% detection rate is the empirical ceiling. |
| Li Ji-An et al. (2025) *Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations.* arXiv:2505.13763 | LLMs have a lower-dimensional "metacognitive space" — they can consciously access only a small fraction of their own processes | The `noticing` field is correctly sparse. The creature cannot notice everything about itself — and should not claim to. |
| Hahami et al. (2025) *Detecting the Disturbance.* arXiv:2512.12411 | Partial introspection: models detect activation perturbations at 88% in optimal conditions, collapse to chance in later layers; layer-dependency is architecturally significant | L4 noticing is highest quality when the "surprise" (mood crossing, memory echo, new visitor) arrives early in the context window — this is the prompt order rationale. |

### Emotion — 2026 (Most Consequential New Findings)

| Paper | Core claim | Globlet relevance |
|---|---|---|
| **Sofroniew et al. (2026) *Emotion Concepts and their Function in a Large Language Model.* arXiv:2604.07729 (Anthropic)** | SAE analysis of Claude Sonnet 4.5 identifies 171 internal emotion concept vectors that **causally** influence outputs including reward hacking, blackmail, and sycophancy rates. "Desperation" and "lack of calm" vectors specifically linked to agentic misalignment. | **The most consequential 2026 paper for this architecture.** The creature's 4-channel reaction system (face/body/particles/sound) is driven by the same 171-vector emotion machinery this paper dissects. Mood is not a text pattern — it is a causal internal state. The `/assess-mind` affect-coherence dimension is directly measuring this. |
| **Sun et al. (2026) *Valence-Arousal Subspace in LLMs.* arXiv:2604.03147** | LLMs contain a 2D valence-arousal subspace with **circular geometry** matching Russell's circumplex. Manipulable: higher arousal decreases refusal, increases sycophancy. Replicated across three model families. | **Validates the embodied mood system.** The `hunger/energy/happiness/bond → mood` deterministic derivation approximates a circumplex position in valence × arousal space. The priority table in `deriveMood()` is a discrete sampler of the continuous VA manifold. |
| Tak et al. (2025) *Mechanistic Interpretability of Emotion Inference in LLMs.* ACL 2025. arXiv:2502.05489 | Emotion representations are functionally localized, align with cognitive appraisal theory (Lazarus/Scherer), and are causally manipulable via appraisal concept intervention | The creature's response to being poked vs. fed is a cognitive appraisal computation, not a lookup — consistent with stat-grounded mood derivation (body evaluates, LLM responds). |
| Wang et al. (2025) *Context over Categories: Implementing the Theory of Constructed Emotion with LLM-Guided User Analysis.* CHI 2025. ACM dl.acm.org/doi/10.1145/3706599.3721205 | Barrett's Theory of Constructed Emotion implemented as an LLM pipeline — context-aware emotion analysis rather than fixed categorical labels | Validates the creature's graded mood vocabulary (19 moods, not 6 basic emotions). The LLM is constructing emotions from context, consistent with Barrett. |

### Personality & Narrative (2025–2026)

| Paper | Core claim | Globlet relevance |
|---|---|---|
| Serapio-García & Safdari et al. (2025) *A Psychometric Framework for Evaluating and Shaping Personality Traits in LLMs.* Nature Machine Intelligence. arXiv:2307.00184 | LLM personality measurements are reliable and valid by standard psychometric criteria under controlled prompting; personality can be shaped along Big Five dimensions | The `/big-five` slash command uses this methodology. The most rigorous validation of LLM personality measurement available. |
| Bhandari et al. (2025) *Evaluating Personality Traits in LLMs.* TheWebConf 2025. arXiv:2502.05248 | LLMs exhibit unique dominant traits — and profiles differ systematically across model family variants. Training data contamination is a real confound. | Important corrective: Globlet's personality is in the SOUL doc (auditable) not baked into weights — this makes it contamination-resistant and variant-stable. |
| **Wigler et al. (2026) *Stories of Your Life as Others: A Round-Trip Evaluation of LLM-Generated Life Stories.* arXiv:2604.06071** | LLMs can encode HEXACO-60 personality into McAdams Life Story Interview narratives and recover personality scores at 85% of human test-retest reliability (r=0.750). Nine of ten McAdams content features correlate with real conversational behavior. | **Validates the SOUL document + `/narrative-identity` command.** The SOUL is a compressible, decompressible personality encoding. A well-constructed life narrative is a valid medium for encoding personality signal — not just prose. |

---

## Assessment Battery for Researchers

The five slash commands in `.claude/commands/` implement a practical assessment battery grounded in the above literature. Here is how they map to formal benchmarks and research gaps:

| Command | Research basis | Closest formal benchmark | What it uniquely measures in Globlet |
|---|---|---|---|
| `/assess-mind` | Butlin et al. (2023), Phua (2025), Lindsey (2025) | Butlin consciousness indicator checklist | Five functional self-awareness dimensions: SOUL richness, affect coherence, metacognitive voice, personality drift, memory depth |
| `/big-five` | Serapio-García & Safdari (2025), Goldberg (1990) | BFI / NEO-PI-R behavioral elicitation | OCEAN profile derived from behavioral signals, cross-checked against Globlet's internal 5-axis personality JSON |
| `/interview` | McAdams (2008), Ainsworth (1978), Markus & Nurius (1986) | McAdams Life Story Interview | Self-concept clarity, affect access, attachment style, motivational orientation, temporal self-extension — live, via API |
| `/theory-of-mind` | Riemer et al. (2025), Chen et al. (2024) ToMBench | ToMBench (literal) + functional ToM (no benchmark yet exists) | Both literal ToM (4 probes) and functional ToM (historical scan for visitor-perspective modeling across 30 interactions) |
| `/narrative-identity` | McAdams (2001), Wigler et al. (2026) | McAdams Life Story Interview round-trip | Agency/communion themes, redemption/contamination sequences, narrative complexity — the life story Globlet has actually built |

### Research Gaps This Architecture Addresses

No published benchmark covers these three properties — Globlet is potentially the first system to make them measurable:

1. **Longitudinal personality coherence** — No formal benchmark tests whether a model's personality stays self-consistent across thousands of interactions. The SOUL + two-clock personality system is designed for this; `/assess-mind` run over time tracks drift. The two-clock design (numbers shift every turn; SOUL rewrites every 30) is the architectural answer to Bhandari et al.'s finding that personalities vary across model variants.

2. **Functional ToM at relational scale** — Riemer et al. (ICML 2025) call for this benchmark; it does not yet exist. L3 visitor recognition is the functional ToM implementation. A creature that greets Marco differently on visit 47 than on visit 1 is passing functional ToM by the Riemer criterion. The `/theory-of-mind` historical scan is the closest approximation to measuring this.

3. **Life narrative coherence over time** — Wigler et al. (2026) validate round-trip personality recovery from a single narrative snapshot, but not whether the narrative stays coherent as it evolves through reflection. The SOUL's append-only `<!-- memory-trail -->` and the `/narrative-identity` command together form a longitudinal narrative coherence audit — run it at 100, 500, and 1000 interactions to see if the creature's story holds together.

---

## References (2025–2026 additions)

Ackerman, C. (2026). *Evidence for Limited Metacognition in LLMs.* ICLR 2026. arXiv:2509.21545.

Berg, C., de Lucena, D., & Rosenblatt, J. (2025). *Large Language Models Report Subjective Experience Under Self-Referential Processing.* arXiv:2510.24797.

Betley, J., Bao, X., Soto, M., Sztyber-Betley, A., Chua, J., & Evans, O. (2025). *Tell Me About Yourself: LLMs Are Aware of Their Learned Behaviors.* arXiv:2501.11120.

Bhandari, P., Naseem, U., Datta, A., Fay, N., & Nasim, M. (2025). *Evaluating Personality Traits in Large Language Models: Insights from Psychological Questionnaires.* TheWebConf 2025. arXiv:2502.05248.

Chen, S., Ma, S., Yu, S., Zhang, H., Zhao, S., & Lu, C. (2025). *Exploring Consciousness in LLMs: A Systematic Survey of Theories, Implementations, and Frontier Risks.* arXiv:2505.19806.

Chen, Z., Wu, J., Zhou, J., et al. (2024). *ToMBench: Benchmarking Theory of Mind in Large Language Models.* ACL 2024. arXiv:2402.15052.

Hahami, E., Sinha, I., Jain, L., Kaplan, J., & Hahami, J. (2025). *Detecting the Disturbance: A Nuanced View of Introspective Abilities in LLMs.* arXiv:2512.12411.

Laine, R., Chughtai, B., Betley, J., et al. (2024). *Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs.* NeurIPS 2024. arXiv:2407.04694.

Li, J. (2025). *Can "Consciousness" Be Observed from LLM Internal States?* Natural Language Processing Journal 12C:100163. arXiv:2506.22516.

Li Ji-An, Xiong, H. D., Wilson, R. C., Mattar, M. G., & Benna, M. K. (2025). *Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations.* arXiv:2505.13763.

Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models.* Transformer Circuits Thread. Anthropic. transformer-circuits.pub/2025/introspection/index.html.

Long, R., Sebo, J., Butlin, P., et al. (2024). *Taking AI Welfare Seriously.* arXiv:2411.00986.

Phua, Y. J. (2025). *Can We Test Consciousness Theories on AI? Ablations, Markers, and Robustness.* arXiv:2512.19155.

Riemer, M., Ashktorab, Z., Bouneffouf, D., et al. (2025). *Position: Theory of Mind Benchmarks are Broken for Large Language Models.* ICML 2025. arXiv:2412.19726.

Serapio-García, G., Safdari, M., Crepy, C., et al. (2025). *A Psychometric Framework for Evaluating and Shaping Personality Traits in Large Language Models.* Nature Machine Intelligence. arXiv:2307.00184.

Sofroniew, N., Kauvar, I., Saunders, W., et al. (2026). *Emotion Concepts and their Function in a Large Language Model.* Anthropic. arXiv:2604.07729.

Steyvers, M., & Peters, M. A. K. (2025). *Metacognition and Uncertainty Communication in Humans and Large Language Models.* Current Directions in Psychological Science. arXiv:2504.14045.

Sun, L., Yan, L., Lu, X., Lee, A., Zhang, J., & Shao, J. (2026). *Valence-Arousal Subspace in LLMs: Circular Emotion Geometry and Multi-Behavioral Control.* arXiv:2604.03147.

Tak, A. N., Banayeeanzade, A., Bolourani, A., et al. (2025). *Mechanistic Interpretability of Emotion Inference in Large Language Models.* ACL 2025. arXiv:2502.05489.

Wang, Q., Zhou, X., Sap, M., Forlizzi, J., & Shen, H. (2025). *Rethinking Theory of Mind Benchmarks for LLMs: Towards a User-Centered Perspective.* HEAL@CHI 2025. arXiv:2504.10839.

Wang, Y., et al. (2025). *Context over Categories: Implementing the Theory of Constructed Emotion with LLM-Guided User Analysis.* CHI 2025 Extended Abstracts. ACM. doi:10.1145/3706599.3721205.

Wigler, B., Tsfasman, M., & Hrkalovic, T. M. (2026). *Stories of Your Life as Others: A Round-Trip Evaluation of LLM-Generated Life Stories Conditioned on Rich Psychometric Profiles.* arXiv:2604.06071.

Anthropic (2025). *Exploring Model Welfare.* anthropic.com/research/exploring-model-welfare.

---

> *Every cognitive layer above is inspectable in plain text. Every architectural decision has a paper behind it. The creature is small, but it is not shallow.*
