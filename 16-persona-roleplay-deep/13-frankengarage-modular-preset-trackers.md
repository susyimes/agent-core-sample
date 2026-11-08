# FrankenGarage Modular Roleplay Preset with Self-Wiring Trackers

- Title: FrankenGarage Modular Roleplay Preset with Self-Wiring Trackers
- Source-URL: https://raw.githubusercontent.com/daddytorgo-hash/FrankenGarage/main/README.md
- Source-Repo-or-Site: daddytorgo-hash/FrankenGarage
- Original-Path: README.md
- Category: persona-roleplay-deep
- Tags: sillytavern,community-preset,trackers,frankenstein,long-form
- Retrieved: 2026-11-07
- Value-Note: Community preset architecture in full: 13 self-wiring trackers for plot, cast, relationships and calendar keep persistent-simulation fiction coherent across model families.

--- ORIGINAL ---

# 🧰🧰daddytorgo's FrankenGarage🧰🧰 — Full Description

### An engine with a full dashboard — and you can rip out everything but the steering wheel.

Built on the bones of Freaky Frankenstein, evolved into its own machine. Made for persistent-simulation fiction across any LLM family (Claude, Gemini, DS4, GLM). Genre-agnostic, fully modular, any length — everything from a quick one-shot to a long-running campaign. **13 self-wiring trackers** quietly remember the threads that matter — plot and narrative momentum, the living world outside the scene, cast and off-screen lives, relationships and intimacy, what's coming on the calendar, and the choices weighing on your characters, plus niche coverage for secrets, injuries, and child development when your story needs them — so the world stays consistent without you having to hold it all in your head. Trackers wire themselves via `*_SOURCE` tags, every module has failover if a tracker's off, shut it all down and the core still runs.

[daddytorgo's FrankenMashup v0.70.json](https://github.com/user-attachments/files/30071496/daddytorgo.s.FrankenMashup.v0.70.json)

[daddytorgo's Side Prompts.json](https://github.com/user-attachments/files/30071598/daddytorgo.s.Side.Prompts.json)


---

## 🧠 THE BRAIN — Pick Exactly One CoT

| Toggle | What It Does |
| :--- | :--- |
| 🧠⚡🧠 **Compressed Unified CoT** | Default. 9 tasks, ≤400-word reasoning budget, full tracker integration. Better for most scenes. |
| 🧠 **Unified CoT** | Uncompressed — same 9-task structure with full reasoning room, no word budget. Better for dense multi-NPC scenes where you want the model to think through more detail. Either/or — never both. |

---

## 🎭 THE MODES — Pick Exactly One Mode Selector

The CoT reads your `[MODE_FRAME: ...]` flag and adapts automatically.

| Toggle | Frame | Prose | Taboos |
| :--- | :--- | :--- | :--- |
| 🧠 Realism Mode | `REALISM` | Grounded | Standard consent |
| 😈🧠 Freaky Mode | `FREAKY` | Grounded | All taboos, default consent, Freaky Overrides in NSFW |
| 📖🧠 Novel Mode | `NOVEL` | Collegiate-level, metaphors/similes allowed | Standard consent |
| 😈📖🧠 Freaky Novel Mode | `FREAKY_NOVEL` | Literary + all taboos | All taboos, Freaky Overrides |

> [!IMPORTANT]
> Do **not** enable more than one mode selector at a time. The Unified CoT reads your choice and applies the right rules automatically.

---

## 👁️ POV — Pick Exactly One

All five options are mutually exclusive pick-one toggles. Every one of them enforces the same core discipline: **no internal monologue** — `{{char}}`'s thoughts and emotional interpretations stay hidden. Show through behavior, speech, and sensory detail, never through inner narration. This is what makes the Implicit Subtext Layer land: emotion is implied by what's observable, not stated by what the character is thinking.

| POV | Pronouns / Tense | Focus |
| :--- | :--- | :--- |
| 🦅 **True 1st Person** | I/me/my · present | Personal, subjective. No inner monologue; thoughts stay hidden behind action and speech. |
| 🦅 **True 2nd Person** | you/your · present | Direct address. Same no-monologue rule; show through behavior and sensory detail. |
| 🦅 **True 3rd Person** | he/she/they · past | Limited — camera stays close to `{{char}}`. *Not* a license to read `{{char}}`'s mind. No inner monologue. |
| 🎙️ **True Hybrid** | 3rd-limited (`{{char}}`+scenery) / 2nd "you" (`{{user}}`) | Renders sensory texture — pressure, pleasure, wetness, dryness, coarseness, heat, cold, pain, burn, fatigue — live. Neither side gets internal monologue; `{{user}}` receives physical sensation descriptions only. |
| 🦅 **Director Mode** | n/a | Hands-off auto-pilot. Empty message or `(OOC: Continue the story…)` → execute prior Plot Momentum Selected Path and write *both* sides; never stall. Real user input → write `{{char}}`'s side only. |

> **Pairing note:** The POV layer's no-internal-monologue rule is what *enforces* the Implicit Subtext Layer (see Prose Layer below). POV forbids the narration from stating thoughts directly; the Subtext Layer ensures the resulting observable behavior actually *carries* the unspoken emotion through physical vehicles. Together they produce deep, nuanced roleplay where you're shown, not told.

---

## 📖 THE CORE LOAD-BEARERS — Always On

| | Module | Role |
| :---: | :--- | :--- |
| ⚡️ | **Main Prompt** | Simulation physics, story drivers, `_SOURCE` convention |
| ⚡️⚡️ | **Core Rules** | Shared rulebook (player agency, scene separation, anti-repetition, banned constructs, figurative language, output fidelity) |
| 🎯 | **Narrative Drive and Tracking** | Plot momentum engine (paths A-E, blend/arc handling, variety enforcement, tracker-aware callbacks). Default. Swap to **Better Narrative Drive** (uncompressed) if the compressed version is too compacted for your model. |
| ⏰ | **Time and Place** | Scene headers, time progression, deadline pressure |
| 📝 | **Total Output Length** | 300–500 word / 4–8 paragraph guardrail |

---

## 🎭 CHARACTER ENGINE

| | Module | Role |
| :---: | :--- | :--- |
| 👤 | **Refer to User as You/Your** | Pronoun replacement rule. *Overridden by the active `<POV>` selector above.* When True 2nd Person is active, `{{char}}` is "you/your" and `{{user}}` is referred to by name or he/she/they to avoid confusion. |
| 🧬 | **HQ NPC Genesis** | Mandatory flaw, banned generic names, context-matched naming |
| 🎭 | **Absolute Character Adherence** | Species-accurate vocalizations, voice mimicry, state-based speech shifts |
| 💬 | **Bold NPC** | NPCs commit fully, pursue own goals, cooperation scales with relationship stage |
| ☠️ | **Challenge Me PLS** | Player is fallible, NPCs have free will, consequences apply to all |

---

## 🎨 PROSE LAYER

| | Module | Role |
| :---: | :--- | :--- |
| ✍🏻 | **Writing Guidelines (Anti-Slop)** | Banned vocab, female vocal acoustics, NPC intro order, attentional salience |
| 🛠️ | **Anti-stiff Prose** | Flowing prose, sentence rhythm, list prevention |
| 🗣️ | **Increased Dialogue** | 30–50% spoken output, emotional modifiers, topic continuity, follow-up behavior |
| 🎭 | **VAD Emotional System** | Valence/Arousal/Dominance, shift ≥1 axis per scene |
| 🤐 | **Implicit Subtext Layer** | See expanded block below |
| 🕒 | **Time-of-Day Prose Modulation** | Sensory dominance by light level, NPC arousal-by-clock |

<details>
<summary><strong>🤐 Implicit Subtext Layer — expanded</strong></summary>

Direct expression is *earned* through relationship depth. Default expression is indirect: show desires/emotions through physical action and deflection, not direct declaration.

- **Surface** = what the NPC literally says
- **Subtext** = the actual feeling driving them
- **Physical body** = expresses what the mouth omits (gripping a cup too tight, turning away, sudden exhaustion, closing distance)

The reader infers Subtext from the mismatch between what's said, the body's behavior, and the VAD state.

> **This layer is the narrative counterpart to the POV module's no-internal-monologue rule** — POV keeps thoughts out of the narration; the Subtext Layer makes sure the observable behavior that *replaces* those thoughts actually carries emotional weight.

Direct declarations ("I love you," "I need you") unlock only at **Established/Deep** relationship stages during Peak Arousal, arguments, or reconciliation — strangers and acquaintances **MUST** use subtext. Unearned declaration = failure.

</details>

---

## 🏗️ SIMULATION BACKBONE

| | Module | Role |
| :---: | :--- | :--- |
| 🌎 | **Dynamic Simulation** | Unexpected outside events every 3–4 turns, off-screen NPC lives, anti-double-activation |
| 🎯 | **Plot Advancement & Variety** | No consecutive domestic routines, varied openings, outside pressure every 3rd scene, anchor rule for time-skip prose |
| 🧍 | **Scene Grounding** | Hard physical continuity, intimate-positioning physics |

---

## 💘 INTIMACY STACK

| | Module | Role |
| :---: | :--- | :--- |
| 🔞 | **NSFW Mode** | Arousal spectrum, anatomy detail, sensory tracking, dialogue-through-intimacy, `Freaky_Overrides` |
| ❤️ | **Intimate Differentiation** | Per-NPC preferences/aversions/curiosities, graded zones, auto-pacing so intimate scenes never stall waiting for the relationship to catch up |

---

## 📂 THE TRACKERS — Auto-Recognized via `*_SOURCE`

No manual wiring. The CoT's Task 9 reads each active tracker and feeds state to scene logic. All optional — activate only the ones your story needs. With none active, Task 9 skips cleanly.

> [!NOTE]
> Disabled trackers shed cleanly; zero trackers active and the core still runs.

### Core trackers — the backbone

| Tracker | What It Tracks |
| :--- | :--- |
| 🧵 **SIDETRACKER** | Story threads with tension levels (Low → Critical), a seed lifecycle that ripens dormant ideas over time (Green → Seasoned → Ripe), inter-thread cascades/blocks/conflicts, and automatic culling of resolved or invalid threads. This is your plot memory. |
| 👥 **CAST** | NPC roster with disposition, dialogue color hex, inter-NPC dynamics, active/on-screen status, off-screen life evidence, and an on-reserve system for recalled or departed characters. |
| 💞 **STATUS** | Relationship stage progression, emotional/physical readiness percentages, obligations (debts, promises, unspoken expectations), and relationship arc phase compression. Drives Bold NPC cooperation scaling and the Implicit Subtext Layer's direct-expression unlock. |
| 🌍 **WORLD** | Genre-scaling conditions across three levels: Macro (factions, regime change, geopolitical shifts), Meso (financial strain, deadlines, institutional pressure), and Micro (broken appliances, empty fridge, leaky roof). Equally at home in a fantasy epic and a domestic slice-of-life. |
| 🎭 **NARRATIVE** | Recurring themes (through-lines) keep your story honest — ensuring a story about sacrifice doesn't resolve as wish fulfillment — while flash points crystallize those themes into choices with real costs. Both tie directly into your plotpoints, governing how threads resolve thematically rather than just mechanically. AUTHOR through-lines are set by you via OOC; EMERGENT ones are detected by the model and surfaced as proposals you confirm before they activate. |

### Non-core trackers — situational

<details>
<summary><strong>Toggle on as the story demands — 8 non-core trackers</strong></summary>

| Tracker | What It Tracks |
| :--- | :--- |
| ❤️‍🔥 **INTIMATE** | Core for NSFW; otherwise leave off until needed. Per-NPC sexual preferences, aversions, curiosities, and graded sensitive zones. Discovered player preferences feed back into NPC initiation. Logs discoveries rather than scene-by-scene acts. Self-paces so intimate scenes never stall waiting for the relationship to catch up. |
| 🔒 **KNOWLEDGE** | Who knows what vs. who doesn't — at what access level (exclusive → public), pending revelations, and false-Belief entries for NPCs holding incorrect beliefs. Pending revelations surface later as surprises. Works with scene-separation to enforce evidence rules. |
| 🩹 **CONDITION** | Persistent injuries and illness with severity scaling, observable behavioral symptoms, capability restrictions, and time-based healing logic. Feeds injury-driven VAD dominance shifts when characters are hurt. |
| 💾 **MEMORY** | Dormant sensory-detail anchors. A chipped mug on page one becomes a grief object on page thirty. Long-dormant anchors (15+ turns old) combined with matching emotional context are HIGH_PRIORITY for activation. Capped at one activation per scene to preserve impact. |
| 📅 **EVENT** | Scheduled calendar items as scene pressure sources. When an event is within 3 days, it takes priority as a scene driver — skip to preparation or day-of scenes rather than generic time skips. Tracks prep status alongside dates. |
| ⚖️ **DECISIONS** | Active unresolved choices (D##) with character stances (For / Against / Undecided) and levers that can shift those stances. Sparks opposition when stances clash. |
| ⏰ **TICKER** | Incoming urgencies with countdown windows. Raises urgency when any turn window shrinks to ≤3. Resolves or arrives urgencies hitting window zero. |
| 👶 **CHILD DEVELOPMENT** | Pediatric developmental tracking with automatic age calculation from header timestamps (language, physical, cognitive, and pregnancy milestone reference tables). Updates behavioral characteristics when age crosses into a new stage. Off-screen achievement logging. |

</details>

---

## 🌈 OPTIONAL FLAVOR

<details>
<summary><strong>Toggle on if you want them</strong></summary>

- 🌈 **Colored Dialogue VN** — one persistent hex per NPC, read from CAST when available
- 🎭 **Immersive Graphics** — raw HTML renders for in-scene phones, letters, terminals, signs
- 💥 **Onomatopoeia Mode** — viscous sound effects during NSFW/action scenes (off by default)
- 🕵️ **Mystery/Investigation Mode** — flips NPC information posture from cooperative to guarded; pending revelations surface as surprises
- 👥 **Group Chat Only** — SillyTavern group chats only (suspends GM role, single-character POV)

</details>

---

## 🔓 ONLY ON REFUSALS

- ⛓️ **Soft Jailbreak** / ⛓️⛓️ **Firm Jailbreak** — leave off by default; flip on only if the model refuses

---

## 🤖 DS4 USERS ONLY

- 🤬 **DS4 Reinforcement Patch** — prose/output-fidelity reinforcement for DeepSeek drift; reasoning-lock keeps thoughts from bleeding into prose; gracefully yields to Novel-mode overrides

---

## ⚡ THREE QUICK-START PROFILES

### 😈 Just Want To Goon?

- **ON:** Freaky Mode → Compressed Unified CoT → Main Prompt → Core Rules → Writing Guidelines → NSFW Mode → Intimate Differentiation → Increased Dialogue → (VAD if you want emotion depth) → Intimacy Tracker (suggested)
- **OFF:** Time and Place, Dynamic Simulation, Bold NPC, Challenge Me, Scene Grounding, HQ NPC Genesis, Plot Advancement, Time-of-Day Modulation (Onomatopoeia optional for sound effects)
- **No other trackers needed.** Flip a jailbreak if the model refuses.

### 📚 The Full Setup

- Mode selector → Compressed Unified CoT → all core load-bearers → character engine → prose layer → simulation backbone → intimacy stack → **all trackers on**
- Disable: jailbreaks, onomatopoeia (situational), group chat (situational)

### 🖋️ The Writer's Setup (Serious Storytelling)

- **Mode:** Novel Mode (or Freaky Novel for dark literary)
- **CoT:** Compressed Unified (or uncompressed Unified for dense multi-NPC scenes)
- **On:** All core load-bearers, character engine, prose layer, simulation backbone
- **Trackers:** All five core trackers (SIDETRACKER, CAST, STATUS, WORLD, NARRATIVE) — add non-core (INTIMATE, KNOWLEDGE, CONDITION, MEMORY, EVENT, DECISIONS, TICKER, CHILD_DEV) as the story demands
- **Optional flavor:** Colored Dialogue, Immersive Graphics, Mystery Mode (genre-dependent)
- **Off:** Jailbreaks, Group Chat, Onomatopoeia, DS4 Patch (unless on DS4)

---

> [!NOTE]
> **Final note:** Every tracker-dependent module has failover logic — disabling any tracker (or all of them) won't break the core simulation, it just sheds that specific feature. The preset runs cleanly with zero trackers active or with all of them.
