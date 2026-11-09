# agent-core-sample

[中文](README.md) | English

**548 real agent "core" sample files** (543 distinct contents after collapsing
five fully contained cross-listings): `SOUL.md`, `BIBLE.md`, constitutions,
system prompts, self-evolution prompts, autonomous loops, memory and
reflection, character personas, emotion engines, intrinsic drives,
multi-agent societies, consciousness and dreaming experiments, embodied and
browser/computer-use agents, voice souls, science and repair agents, security
agents, tutors, creative-writing worlds, second-brain LifeOS files, eval
judges, multilingual souls, and formal/math/data agents.

Four through-lines: **self-evolution, autonomy, personification, emotion** —
plus the genuinely weird: inner monologue, sleep consolidation, digital life,
need-driven agents, agent religions.

> Collected live from GitHub and the web in three batches
> (2026-11-07: 145→142, +202→199; 2026-11-08: +207, zero duplicates dropped),
> never reproduced from memory. Parent-verified on disk: 548/548 files carry a
> `Source-URL` header and a verbatim body; five files are fully contained in
> another canonical file (cross-category listings), hence 543 distinct contents.

- Start here: [TOP50.md](TOP50.md) — editor's 50 essential reads (Chinese notes).
- Deep analysis: [ANALYSIS.md](ANALYSIS.md) — quantitative profile and design synthesis (Chinese).
- Full index: [INDEX.md](INDEX.md) — every file, by category.
- Build your own: [GUIDE.md](GUIDE.md) — a six-layer assembly guide with anti-patterns (Chinese).
- Machine-readable tags: [metadata.csv](metadata.csv) — layer, language estimate,
  maturity heuristic, source, size for all 548 files.
- Method, dedup and gaps: [CURATION-NOTES.md](CURATION-NOTES.md),
  [CURATION-NOTES-BATCH2.md](CURATION-NOTES-BATCH2.md),
  [CURATION-NOTES-BATCH3.md](CURATION-NOTES-BATCH3.md).

## What each file looks like

Every sample is a collector header plus the upstream original, so anything can
be traced and re-checked:

```text
Title / Source-URL / Source-Repo-or-Site / Original-Path
Category / Tags / Retrieved: 2026-11-07 or 2026-11-08 / Value-Note
--- ORIGINAL ---
<verbatim upstream file; prompt templates living in code stay fenced as code>
```

Upstreams drift. Cite the per-file `Source-URL` and retrieval date, not just
this repository.

## The 36 categories

Batch 1 (01–12): `01-soul-md` (12), `02-bible-constitution` (12),
`03-self-evolving` (12), `04-autonomous-loops` (12),
`05-memory-reflection` (12), `06-persona-character` (11),
`07-emotion-affective` (12), `08-motivation-drives` (12),
`09-multiagent-society` (12), `10-leaked-system-prompts` (12),
`11-agents-claude-cursor` (12), `12-wildcard-consciousness-cn` (11).

Batch 2 (13–24): `13-soul-bible-deep` (16), `14-self-evolving-frontier` (18),
`15-oss-coding-agents` (16), `16-persona-roleplay-deep` (17),
`17-emotion-support-deep` (16), `18-memory-systems-deep` (16),
`19-curiosity-goals-deep` (16), `20-consciousness-inner-deep` (17),
`21-chinese-agents-deep` (15), `22-game-npc-worlds` (18),
`23-classic-reasoning-prompts` (18), `24-spec-life-wildcard2` (16).

Batch 3 (25–36): `25-embodied-robotics` (17), `26-web-computer-use` (16),
`27-voice-realtime` (19), `28-science-research-agents` (18),
`29-software-repair-research` (17), `30-security-agents` (17),
`31-education-tutor-coach` (18), `32-creative-writing-worlds` (17),
`33-second-brain-lifeos` (18), `34-eval-judges-benchmarks` (16),
`35-multilingual-souls` (16), `36-formal-math-data-agents` (18).

65 files carry substantial CJK text (61 estimated Chinese, plus Japanese and
Korean souls in `35-multilingual-souls`, which also holds French, Spanish,
Russian, German and Vietnamese/Thai originals).

## Read by goal

- **Self-evolution**: Darwin–Gödel Machine (`03/01`), Gödel Agent (`03/03`),
  ShinkaEvolve (`03/08`), AlphaEvolve (`14/06`), ACE playbooks (`14/09`),
  then the constitutional guardrails in Ouroboros `BIBLE.md` (`02/01`).
- **Autonomy**: BabyAGI (`04/02`), Voyager's curriculum (`08/01`),
  browser-use (`26/01`), SayCan (`25/02`), OpenHands and Manus for
  production-grade loops.
- **Persona / soul**: OpenClaw's official `SOUL.md` (`01/01`), the Karpathy
  distilled soul (`01/04`), gptme's persona/operations/doctrine split
  (`13/03`), Character Card V3 (`16/04`), pixiv's Japanese emotion-tag soul
  (`35/01`).
- **Emotion**: affectus (`07/01`) for rendering, ESCoT (`17/03`) for strategy,
  Humanoid Agents' decaying needs (`08/09`) for emotion that actually changes
  decisions, EQ-Bench judges (`17/05-06`) for evaluation.
- **Just browsing**: ANIMA's sleep/dream design (`12/04`), a 570-line Chinese
  agent autobiography (`20/13`), the alignment-faking prompt (`24/06`), and
  the Crustafarian genesis — "In the beginning was the Prompt" (`24/10`).

## Cross-cutting findings (editorial, from ANALYSIS.md)

1. Mature cores are layered: principles (what is forbidden), soul (who it is),
   state (needs/emotion right now), memory (what it learned), loop (how it
   acts), evolution gate (how it may change itself).
2. The autonomy watershed is where the next goal comes from: curriculum,
   decaying needs, heartbeat, memory gaps, or social situations.
3. Self-evolution that works is ledger work: atomic edits, an external
   selection anchor, lineage, and rollback. Without a ledger it is drift.
4. Emotion is usually skin (tone rendering) or scale (judging); emotion as a
   decision-changing state machine is still rare.
5. Judge prompts are the hidden protagonists: 39.3% of the first 341 files
   contain evaluation/judging/scoring language.
6. File-as-self is the default ontology: versionable text artifacts — souls,
   playbooks, memory blocks, diaries — are replacing invisible weight edits
   as the agent's body.

## Trust boundaries

- `10-leaked-system-prompts` comes from a single aggregator of leaked/collected
  prompts. Treat it as study material, not vendor-confirmed text. Official
  in-repo counterparts for several tools are in `15-oss-coding-agents`.
- A few long originals are excerpted (each header carries a Truncation-Note
  and the full URL); the EmotionPrompt item is an arXiv abstract-page excerpt.
- Five files are fully contained in another canonical file (Reflexion,
  CAMEL, Voyager curriculum, and two OpenAI Model Spec section excerpts).
  They are kept as cross-category listings: 548 files, 543 distinct contents.
- One upstream file contained apparent API-key fragments; the values were
  redacted before first release and marked with a Redaction-Note in place.
  A second redaction in batch 3 is marked the same way.

## Repository layout

```text
agent-core-sample/
  README.md  README.en.md  TOP50.md  ANALYSIS.md  GUIDE.md
  INDEX.md (+ INDEX-BATCH2/BATCH3)  CURATION-NOTES*.md  metadata.csv
  01-soul-md/ ... 36-formal-math-data-agents/   # 548 samples (543 distinct)
  _staging/  _staging2/  _staging3/              # 145+202+207 raw harvests, git-ignored
```

Local search example (PowerShell):

```powershell
# Find self-modification samples that discuss rollback or lineage
Get-ChildItem -Recurse -Filter *.md agent-core-sample |
  Select-String -Pattern 'rollback|lineage' | Select-Object -First 20
# Count canonical samples (should print 548)
(Get-ChildItem agent-core-sample -Directory |
  Where-Object Name -match '^\d\d-' |
  Get-ChildItem -Filter *.md).Count
```

## Copyright

All 548 bodies are **third-party works** reproduced verbatim for research
study; copyright and licenses remain with their upstreams (see each file's
Source-URL / Source-Repo header). New text in this repository is limited to
collector headers and the editorial documents (README, TOP50, ANALYSIS,
GUIDE, INDEX and curation notes). Do not relicense, commercially
redistribute, or strip source links. Leaked prompts carry no known open
license — research use only. If you publish derivative analysis, link the
upstream source next to any quotation.

