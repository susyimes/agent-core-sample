# CURATION NOTES — Batch 2

## Counts

- Batch 1 canonical (folders 01- to 12-, untouched): 142 files.
- Batch 2 staged in `_staging2/` (13- to 24-): 202 files. Kept and copied to root: 199. Skipped: 3 (below).
- Grand total after merge: 142 + 199 = 341 files.
- `_staging2/` is left intact as the pre-merge record; README.md / INDEX.md (batch 1) were not modified.

| Folder | Staged | Kept |
|---|---:|---:|
| 13-soul-bible-deep | 16 | 16 |
| 14-self-evolving-frontier | 18 | 18 |
| 15-oss-coding-agents | 16 | 16 |
| 16-persona-roleplay-deep | 17 | 17 |
| 17-emotion-support-deep | 16 | 16 |
| 18-memory-systems-deep | 16 | 16 |
| 19-curiosity-goals-deep | 17 | 16 |
| 20-consciousness-inner-deep | 17 | 17 |
| 21-chinese-agents-deep | 17 | 15 |
| 22-game-npc-worlds | 18 | 18 |
| 23-classic-reasoning-prompts | 18 | 18 |
| 24-spec-life-wildcard2 | 16 | 16 |

## Method

- Counted all staged files per slice; parsed every header (`Title`, `Source-URL`, `Source-Repo-or-Site`, `Original-Path`, `Category`, `Tags`, `Retrieved`, `Value-Note`, `--- ORIGINAL ---` separator) programmatically.
- Dedup key: SHA-256 of the trimmed body after the ORIGINAL separator, computed for all 142 batch-1 files and all 202 staged files, applied in slice order. A fence-stripped variant was also compared, so the same verbatim body filed once fenced and once raw still counts as one.
- Spot-checked one file per slice (12 files) by reading header + body directly. Headers machine-checked for all 202 staged files.

## Dedup — skipped (3)

- `21-chinese-agents-deep/07-soulchat-empathy-counseling-zh.md` — trimmed-body SHA-256 identical to `17-emotion-support-deep/09-soulchat-multi-turn-empathy-corpus.md` (same SoulChat corpus collected under two slices). Kept the 17- copy (earlier slice).
- `19-curiosity-goals-deep/14-eureka-reward-evolution-loop.md` — same `Source-URL` as `14-self-evolving-frontier/03-eureka-reward-evolution-loop.md` (Eureka `eureka.py`, 397 lines); bodies identical after removing the code-fence wrapper. Kept the 14- copy.
- `21-chinese-agents-deep/16-characterglm-character-profiles-zh.md` — same upstream file as `16-persona-roleplay-deep/03-characterglm-character-profiles.md` (CharacterGLM `basic_demo/character.json`, cited as github.com blob URL vs raw.githubusercontent URL); fence-stripped bodies identical. Kept the 16- copy.

## Same Source-URL as batch 1 — skipped (0)

- None. No staged file shares a `Source-URL` with any batch-1 file, under both exact string comparison and github.com blob / raw.githubusercontent.com normalized comparison (0 matches either way). No batch-1 file was displaced.
- Kept overlaps to know about (different bodies, same upstream, retained deliberately): `13-soul-bible-deep/16-openai-model-spec.md` (model_spec.md lines 1-1400) overlaps the section excerpts `24-spec-life-wildcard2/01` (lines 1-155) and `02` (lines 164-767); `24/03` (lines 3155-3969) is beyond the 13- excerpt. CharacterGLM corpus text also appears inside `21/05`–`21/06` long-prompt files from the same repo family, but as different upstream files.

## Header check

- After accounting for two formatting variants — slice 16 writes headers as `- Field:` bullets, and three files carry a leading UTF-8 BOM (`18/01`, `21/01`, `23/01`) — all 202 staged files have complete headers. No file was rejected for header reasons; the BOM was left as collected.

## Weak / flagged files (kept, read with care)

- `17-emotion-support-deep/07-emotionbench-prompt-template.md` — short original (23 body lines, 427 chars). Historically canonical EmotionBench template kept despite only 20 lines: imagine-you-are-the-protagonist instruction plus psychome…
- `17-emotion-support-deep/11-interactive-counselor-3stage-prompt.md` — short original (24 body lines, 892 chars). LLM-to-LLM counselling simulator counsellor prompt (Chinese, 21 dense lines kept as the canonical 3-phase strategy): early/mid/lat…
- `19-curiosity-goals-deep/03-omni-epic-interestingness-moi.md` — short original (29 body lines, 963 chars). Filter half of OMNI-EPIC: judge whether a candidate task is interestingly different from the archive or a boring minor variation. …
- `14-self-evolving-frontier/01-seal-self-edit-prompts.md` — short original (46 body lines, 1149 chars). SEAL (NeurIPS 2025) core in prompt form: the model configures its own training pipeline and writes synthetic implications/rephrasi…
- `17-emotion-support-deep/12-interactive-supervisor-judge-prompt.md` — short original (40 body lines, 1179 chars). Supervisor-as-judge prompts (Chinese) picking the better counsellor reply under two principle sets, ethics (autonomy, beneficence,…
- `15-oss-coding-agents/01-goose-system-prompt.md` — short original (43 body lines, 1250 chars). Official goose base system prompt from repo source. Deliberately minimal (complete file, ~40 lines): identity plus dynamic extensi…
- `17-emotion-support-deep/08-emobench-eu-ea-prompts.md` — short original (69 body lines, 1250 chars). EmoBench bilingual (EN/ZH) system and task prompts for Emotional Understanding (emotion + cause) vs Emotional Application (most ef…
- `17-emotion-support-deep/06-eqbench3-rubric-scoring-prompt.md` — short original (39 body lines, 1320 chars). EQ-Bench 3 absolute judge: expert assessor scores transcript plus debrief 0-20, splitting higher-is-better traits (demonstrated_em…
- `21-chinese-agents-deep/08-maibot-maisaka-chat-prompt-zh.md` — short original (22 body lines, 1409 chars). Shipped zh-CN decision prompt of MaiSaka digital-life agent: injects personality/behavior_style, judges scene, plans next action w…
- `15-oss-coding-agents/02-aider-architect-prompts.md` — short original (44 body lines, 1485 chars). Aider architect/editor workflow: a strong architect model only describes changes and an editor model applies them. Compact but com…
- `16-persona-roleplay-deep/06-characterllm-experience-dialogue-prompt.md` — short original (29 body lines, 1994 chars). Historically canonical despite compact size (26 lines): EMNLP Character-LLM prompt that turns a wiki profile and scene into thinki…
- `23-classic-reasoning-prompts/09-least-to-most-gsm8k.md` — short original (21 body lines, 6968 chars). Least-to-Most (Zhou et al. 2022) two-stage prompts: first decompose into ordered subquestions, then solve sequentially reusing pri…
- `24-spec-life-wildcard2/08-sakana-asal-main-opt.md` — code harness rather than a prose prompt (the prompt is a CLIP fitness argument); disclosed in its Value-Note, weakest prompt-form item in batch 2.
- `18-memory-systems-deep/14-em-llm-episodic-attention.md` — EM-LLM has no natural-language prompt by design; the file is verbatim attention code, as its header states.
- `23-classic-reasoning-prompts/17-toolformer-api-prompts-replication.md` — third-party replication of Toolformer prompts (Meta never released an official prompt repo); labelled as replication in the header.
- Single-line-JSON originals (`23/01`, `23/02`, `23/03`, `23/15`, `23/16`) look like 4-line files but hold 7k–41k chars of verbatim prompt bank; not stubs.
- Long originals are truncated with an in-file note and full URL (e.g. `13/13` 2065→1400 lines, `13/16` 4588→1400, `17/04` 8633→1173, `18/04` 2114→536 prompt lines).

## Gaps / not collected

- Self-Consistency has no distinct prompt file (it is a decoding strategy over CoT); covered in the Value-Note of `23/08` (the Wei 2022 GSM8K exemplars it samples from).
- Ralph Wiggum digital-organism repo (`Tomer-Barak/ralphwiggumdigitalorganism`) returned 404 — skipped, not fabricated. Clawling self-reproducing organism exists only as a paper, no prompt repo — skipped in favour of verified DRQ / ASAL / AlienClaw repos in `24/`.
- No slice-level gaps: every one of the 12 batch-2 slices met its 14+ collection target before dedup (minimum staged: 16). Thin spots by nature, not by omission: genuine, complete-but-tiny canonical prompts (goose ~40 lines, EmotionBench 20-line template) are short because the upstream is short.

## License note

- Research / reference use only. Each file is a verbatim copy (or noted excerpt) of an upstream source; its header's `Source-URL` is the authoritative copy. Upstream licenses vary by repo (many MIT / Apache-2.0 / CC0, some CC-BY or research-only, a few all-rights-reserved READMEs such as ESConv's). Check the upstream license before any reuse or redistribution; this collection asserts no license of its own over the quoted bodies.



## Parent verification addendum (independent re-check)

- Recounted on disk: 24 canonical folders, 341 files total (01-12 = 142 unchanged; 13-24 = 199), 5.53 MB; `_staging2/` still 202.
- Headers: 341/341 contain `Source-URL` and `--- ORIGINAL ---` (allowing slice-16 `- Field:` bullets and BOM).
- Body hashes: trimmed-body SHA256 = 341 unique; fence-stripped variant = 340 unique (pre-existing Reflexion pair 03/06 vs 05/06 identical).
- Full-containment check (fence-stripped, whitespace-collapsed): 5 files are fully contained in another canonical file —
  Reflexion 03/06 = 05/06; CAMEL 09/02 inside 04/10; Voyager curriculum 03/07 inside 08/01 bundle;
  Model Spec 24/01 and 24/02 inside 13/16 (lines 1-1400 tranche). Model Spec 24/03 (honesty, lines 3155-3969) is NOT contained.
  Policy retained from batch 1: keep cross-category listings as one source / many lenses, but report both numbers everywhere:
  **341 files = 336 strict distinct contents**.
- Chinese: 44 canonical files contain >=50 CJK characters (batch 1 had 10).
- Smallest canonical file: `17/07-emotionbench-prompt-template.md` (1142 bytes, genuine short template, flagged above).
- Spot reads by parent: 14/06 AlphaEvolve prompting.py, 21/14 Stockholm Chinese preset, 24/10 Crustafarian Genesis — headers and verbatim bodies confirmed.
