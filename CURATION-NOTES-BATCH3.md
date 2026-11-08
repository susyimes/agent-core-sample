# Curation notes - Batch 3 (slices 25-36) - 2026-11-08

## Counts

- Existing canonical (01-24, untouched): 341 files (336 strict distinct, 5 known contained cross-listings).
- Staging _staging3 recounted on disk by curator: 207 files.
  25-embodied-robotics 17, 26-web-computer-use 16, 27-voice-realtime 19, 28-science-research-agents 18,
  29-software-repair-research 17, 30-security-agents 17, 31-education-tutor-coach 18, 32-creative-writing-worlds 17,
  33-second-brain-lifeos 18, 34-eval-judges-benchmarks 16, 35-multilingual-souls 16, 36-formal-math-data-agents 18.
- Kept and copied to new root folders 25-...36-: 207. Skipped: 0.
- Grand total: 341 + 207 = 548 files in 01-36. _staging3 left intact; 01-24, README, INDEX, ANALYSIS not modified.

## Method

- For every existing (341) and batch3 (207) file: SHA256 of trimmed body after the `--- ORIGINAL ---` marker, plus SHA256 of the fence-stripped variant. Existing set: 497 distinct body hashes, 334 normalized Source-URLs.
- A batch3 file was to be skipped if either body hash matched an existing file or an earlier-kept batch3 file (slice order 25 to 36), or if its normalized Source-URL (github blob treated as raw.githubusercontent) matched an existing file with substantially the same body.
- Result: no body-hash matches, no normalized-URL matches at all. Skips: none.
- Machine header check (bullet variants and BOM allowed) over all 207: Title, Source-URL, Source-Repo-or-Site, Original-Path, Category, Tags, Retrieved, Value-Note and the ORIGINAL marker all present in 207/207.
- Spot-checked 12 files, one per slice, by direct read (header + substantive body): 25/01 Code-as-Policies, 26/01 browser-use, 27/01 Pipecat turn-completion, 28/01 AI-Scientist, 29/01 Agentless, 30/01 PentestGPT, 31/01 Mr. Ranedeer, 32/01 Dramatron, 33/01 Khoj, 34/01 MT-Bench, 35/01 ChatVRM, 36/01 COPRA. All pass.

## Secret scan

- Patterns over all 207 batch3 files: OpenAI sk- keys, GitHub ghp_/github_pat_ tokens, AWS AKIA keys, Slack xox tokens, private-key blocks, Bearer tokens, generic api_key/secret/password assignments with quoted values.
- One generic-assignment hit: 25-embodied-robotics/01-code-as-policies-lmp-examples.md (filename only; value never reproduced here). Inspected without printing the value: 13-char upstream placeholder, does not start with sk-. Kept verbatim as non-secret, consistent with the collector note.
- No real-looking secrets found; no exclusions or new redactions made by the curator. One collector-side redaction was already present upstream: 32-creative-writing-worlds item 05 (StoryWriter) carries [REDACTED-BY-COLLECTOR] with a Redaction-Note.

## Weak / thin flags (kept, flagged)

Flagged by body lines < 30 or chars < 800; most are single-line-JSON or genuinely short-but-complete upstream prompts:

- 35-multilingual-souls/01-chatvrm-ja-system-prompt.md (474 chars) - thinnest item; it is the complete verbatim upstream SYSTEM_PROMPT, kept for canonicity.
- 34-eval-judges-benchmarks/06-openai-evals-closedqa-modelgraded.md (831 chars) - short YAML judge spec, complete upstream.
- Short-line but substantive (long lines / JSONL): 25/08 HELPER plan, 25/15 PromptCraft AirSim, 25/17 EmbodiedGPT, 26/12 Cuabot SYSTEM, 31/03 Study Mode, 34/01 MT-Bench JSONL, 34/03 Arena-Hard, 36/01 COPRA system prompt, 36/18 Data-Copilot.
- Paper/notebook-derived items carry format caveats in-file (Truncation-Note / NOTE with full URL): 25/01, 25/02, 25/14, 25/16, 25/17, 29/16 MASAI (paper S2, no public code), 29/17 DevBench (paper text, minor mojibake in arXiv HTML), 32/01 Dramatron (prefix cells only), 32/06, 32/16 (ar5iv table flattening), 26/08 OSWorld (1400/1572 lines), 28/15 Biomni (L898-1288 of 3002), 35/11 Kulsh (1500/1553).

## Gaps carried from collectors (not collected, with reason)

- 25: RT-1/RT-2/OpenVLA/Octo (no public prompt files, end-to-end VLA); RoboCat/RoboAgent (goal-conditioned policies, no LLM prompts).
- 26: WorkArena (tasks only; covered via AgentLab 14); Stagehand v4 core (no standalone prompts; extension builders taken); AndroidWorld (prompts embedded in M3A code).
- 27: Vocode (user-supplied prompts only); OpenAI realtime-console (no instructions in repo); Gemini Live examples (one-line, too thin); TEN-Agent (config-buried one-liner).
- 28: ScholarAI (no canonical public prompt repo); BioPlanner (dataset only); Coscientist (toy demo; replaced by EvoScientist).
- 29: MASAI code (none public; paper collected); DevBench repo prompts in submodule baselines; SpecRover (no separate repo; covered via AutoCodeRover reviewer).
- 30: EnIGMA (no clean standalone file); CTIBench (notebook-embedded; covered via TACTIC-KG); NYU baseline template (6 lines; richer D-CIPHER taken instead).
- 31: SimClass live prompts (DB-stored; MAIC-Core preclass taken); LittleMu Chain-of-Teach text (unreleased; AutoGen Teachability taken).
- 32: Dramatron engine/UI cells omitted per size rule; arXiv HTML extraction flattens tables for items 06/16.
- 33: PrivateGPT base prompt (16-line slot, API glue, skipped); Quivr (Go rewrite, no prompt files on main).
- 34: GAIA LLM grader (none public; deterministic HF scorer taken); OSWorld getters not separately collected.
- 35: Items 02,03,09,11,13 are code-wrapped (native-language cores inside English code); Stadttopia URLs use pre-rename slug that redirects.
- 36: Jupyter-AI (submodule shell; covered via MetaGPT DataInterpreter); LeanDojo core (no prompt files; covered via LLMSTEP); nvAgent/Chat2Viz (not collected; LIDA covers visualization).

## License note

All 207 items are verbatim third-party prompt/code/paper texts collected for research study with full Source-URL attribution in each file header. Upstream licenses vary per repository (MIT/Apache-2.0/BSD/research-only/paper text); this sample does not relicense them. Consult each Source-URL for terms before redistribution or commercial use.


## Parent verification addendum (independent re-check)

- Recounted on disk: 36 canonical folders, 548 files (01-24 = 341 unchanged; 25-36 = 207); _staging3 preserved (incl. collector helper scripts, git-ignored).
- Headers: 548/548 contain Source-URL and --- ORIGINAL ---. Trimmed-body SHA256 = 548 unique; fence-stripped = 547 (only the pre-existing Reflexion pair from batch 1).
- Normalized Source-URL duplicate groups across all 548 are exactly the 5 groups already known from batches 1-2; batch 3 added none.
- Secret-pattern scan (sk-/ghp_/github_pat_/AKIA/private-key patterns) over canonical 25-/36- folders: 0 hits. One upstream hardcoded key in 32/05 was already redacted by its collector with Redaction-Note (verified by curator scan).
- Spot reads by parent: 26/01 browser-use system prompt, 35/01 ChatVRM Japanese soul - headers and verbatim bodies confirmed.
- Strict distinct contents: 548 - 5 fully-contained cross-listings (all from batches 1-2) = 543. CJK>=50 files now 65.
