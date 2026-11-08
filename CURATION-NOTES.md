# Curation Notes

Curator pass over `_staging/` (12 slices) into final root folders
`01-soul-md` … `12-wildcard-consciousness-cn`. Date: 2026-11-07.
`_staging/` is kept intact as the audit trail.

## Method

1. Counted staged `.md` per slice and total (145).
2. SHA256 over whole files: **0 exact file duplicates** (collector headers
   differ per slice even for the same upstream file).
3. SHA256 over the verbatim body after `--- ORIGINAL ---` (trimmed):
   **142 unique bodies**, 2 duplicate groups. Final copy keeps the first
   occurrence in slice order and skips later body-identical copies.
   Both hashes are reported so "exact duplicate" is not ambiguous.
4. Spot-checked 12 files (one per slice) by direct read: each has a
   `Source-URL:` header and a substantive verbatim body. All 145 staged
   files were also machine-checked for `Source-URL` + `--- ORIGINAL ---`
   (0 missing). Smallest file is 1708 bytes — no empty stubs.
5. Copied (not moved) deduped files to root `NN-name/` folders.
   `_staging/` still holds all 145 files.

## Counts

| Slice | Staged | Final |
|---|---|---|
| 01-soul-md | 12 | 12 |
| 02-bible-constitution | 12 | 12 |
| 03-self-evolving | 12 | 12 |
| 04-autonomous-loops | 12 | 12 |
| 05-memory-reflection | 12 | 12 |
| 06-persona-character | 13 | 11 |
| 07-emotion-affective | 12 | 12 |
| 08-motivation-drives | 12 | 12 |
| 09-multiagent-society | 12 | 12 |
| 10-leaked-system-prompts | 12 | 12 |
| 11-agents-claude-cursor | 12 | 12 |
| 12-wildcard-consciousness-cn | 12 | 11 |
| **Total** | **145** | **142** |

## Duplicates skipped (3)

Body-identical to an earlier kept file; still present under `_staging/`:

- `06-persona-character/10-openclaw-soul-architecture.md`
  → same body as `01-soul-md/08-sahajamit-soul-persona-system-prompt.md`
  (sahajamit/openclaw-deep-dive `06-soul-persona-system-prompt.md`).
- `12-wildcard-consciousness-cn/02-openclaw-soul-persona-system-prompt.md`
  → same body as the same `01-soul-md/08-…` file (collected 3×).
- `06-persona-character/13-hermes-agent-personality.md`
  → same body as `01-soul-md/10-hermes-personality-soul-docs.md`
  (Hermes personality docs; note the kept copy is from the Stars1233
  fork mirror because NousResearch raw returned 429 — see Gaps).

Near-duplicates intentionally **kept** (same upstream project, different
saved body/excerpt, so not body-identical): Voyager curriculum in
03-self-evolving vs bundled prompt set in 08-motivation-drives; Reflexion
prompts in 03 vs 05; ExpeL templates in 03 vs agent code in 05; BabyAGI in
04 (archive repo) vs 08 (backup-main branch); Generative Agents
`run_gpt_prompt.py` excerpts in 05 vs txt templates in 08 vs first-1500-line
copy in 09; CAMEL `ai_society.py` in 04 vs 09 (verify before citing as two
independent sources). Treat cross-slice repeats as one source, many lenses.

## Spot-check (12/12 pass)

One file per slice read directly; all show Source-URL header +
substantive original (first ~40 lines inspected):

- 01 `01-openclaw-official-soul-template.md` — PASS
- 02 `01-ouroboros-bible.md` — PASS
- 03 `01-darwin-godel-machine-self-improvement-prompt.md` — PASS
- 04 `02-babyagi-classic-task-loop.md` — PASS
- 05 `01-letta-memgpt-chat-system-prompt.md` — PASS
- 06 `01-charactercard-spec-v2.md` — PASS
- 07 `04-openrook-emotional-contagion-prompt.md` — PASS (complete, 38 lines)
- 08 `09-humanoid-agents-basic-needs-emotion.md` — PASS
- 09 `01-metagpt-product-manager-prompts.md` — PASS
- 10 `01-manus-agent.md` — PASS
- 11 `05-obra-global-claude-md.md` — PASS
- 12 `09-tideline-dream-solidify-zh.md` — PASS (Chinese intact)

No empty or fabricated-looking stubs found. Nothing was removed for quality;
the flags below are "read with care", not deletions.

## Flagged weak / partial files

- `07-emotion-affective/12-emotionprompt-arxiv-2307-11760.md` — arXiv
  abstract-page excerpt only; the 11 EmotionPrompt stimuli in the PDF/HTML
  full text were **not** transcribed. Weakest item in the set.
- `05-memory-reflection/05-generative-agents-reflection-prompts.md` and
  `09-multiagent-society/06-generative-agents-run-gpt-prompt.md` — deliberate
  excerpts of the 2931-line `run_gpt_prompt.py` (named functions / first 1500
  lines). Full URL is in each header.
- `04-autonomous-loops/09-langgraph-plan-and-execute.md` — notebook cell
  sources verbatim; outputs/JSON envelope omitted.
- `04-autonomous-loops/04-hugginggpt-jarvis-controller.md` — controller code
  verbatim, but literal prompt strings live in companion
  `configs/config.default.yaml` (not bundled).
- Short-but-genuine originals (do not mistake for stubs):
  `11-agents-claude-cursor/04-excalidraw-claude-md.md` (1708 B, 35-line
  original), `07-…/04-openrook-…` (29-line prompt),
  `02-…/12-ironcurtain-readonly-constitution.md` (25-line variant).
- `03-self-evolving/11-promptbreeder-mutation-prompts.md` — community
  reimplementation (DeepMind released no official code); labelled in-file.
- `01-soul-md/10-hermes-personality-soul-docs.md` — fork mirror
  (Stars1233/hermes-agent), not NousResearch direct; labelled in-file.
- `10-leaked-system-prompts/*` — single aggregator source
  (x1xhlol/system-prompts-and-models-of-ai-tools); provenance is
  "leaked/collated", not vendor-confirmed. Use as study material only.

## Gaps (from slice collectors, preserved)

- Slice 01: NousResearch/hermes-agent direct raw = 429 (fork mirror used);
  dabit3 gist left uncollected in favour of repo sources.
- Slice 02: ConstitutionalHarmlessnessPaper README is a 4-line stub (skipped).
- Slice 03: no official PromptBreeder code exists (see flag above).
- Slice 06: oobabooga Example.yaml unavailable/trivial (not saved);
  SillyTavern Seraphina lives in PNG metadata (not extracted) — Eldoria
  lorebook saved instead.
- Slice 07: SillyTavern expressions `index.js` (2722 lines) not saved;
  GoEmotions item covers its taxonomy. EmotionPrompt full stimuli missing.
- Slice 08: OpenGVLab/GITM ships no code/prompts (excluded); JARVIS-1
  `prompts.json` is empty (assembly prompt saved instead).
- Slice 09: classic ChatDev ChatChainConfig JSON absent on current main;
  current `ChatDev_v1.yaml` saved (same role prompts).
- Slice 11: openai/codex has no root AGENTS.md; Roo-Code AGENTS.md is a
  445-byte stub (both skipped). Awesome-list READMEs used for discovery only.
- Slice 12: shsmith/IACCF and PlexPt/awesome-chatgpt-prompts-zh returned 404
  (skipped, replaced). Runa uses `development` branch (recorded in header).
- General: GitHub API rate limits (403/429) hit during collection; raw-file
  fetches succeeded for everything saved. Bodies are point-in-time
  (2026-11-07) and upstreams will drift — cite the Source-URL + Retrieved
  date in each header, not just this repo.

## License / use note

All 142 bodies are **third-party works** reproduced verbatim for research
study. Each remains under its original license and copyright (see the
Source-URL / Source-Repo in every file header; consult the upstream repo
for its LICENSE). Collector headers and INDEX/CURATION notes are the only
new text. Do not relicense, redistribute commercially, or strip source
links. Leaked prompts (slice 10) carry no known open license — research
use only. If you publish derivative analysis, link the upstream source
alongside any quotation.
