# openClawWorld Maslow NeedsSystem and Drive-Aware PromptBuilder (TypeScript)

Title: openClawWorld Maslow NeedsSystem and Drive-Aware PromptBuilder (TypeScript)
Source-URL: https://raw.githubusercontent.com/Two-Weeks-Team/openClawWorld/main/packages/ecosystem/src/personality/NeedsSystem.ts
Source-Repo-or-Site: Two-Weeks-Team/openClawWorld (github.com/Two-Weeks-Team/openClawWorld)
Original-Path: packages/ecosystem/src/personality/NeedsSystem.ts; packages/ecosystem/src/cognitive/PromptBuilder.ts
Category: 08-motivation-drives (intrinsic motivation, curiosity, drives, autonomous goals)
Tags: maslow,needs-decay,drives,prompt-injection,emotion,autonomous-agents,typescript
Retrieved: 2026-11-07
Value-Note: A working game-ecosystem drive loop: five Maslow needs decay per tick and urgent needs plus emotion are assembled into the LLM prompt, so motivation is state, not just prompt wording.

--- ORIGINAL ---

## Original file: packages/ecosystem/src/personality/NeedsSystem.ts

Source-URL: https://raw.githubusercontent.com/Two-Weeks-Team/openClawWorld/main/packages/ecosystem/src/personality/NeedsSystem.ts

````typescript
/**
 * NeedsSystem - Maslow needs hierarchy for behavior motivation
 *
 * Needs decay over time, creating motivation for specific behaviors.
 * Different zones and actions satisfy different needs.
 */

import type { NeedsState } from '../types/agent.types.js';
import { chmodSync, existsSync, readFileSync, writeFileSync, mkdirSync } from 'fs';
import { dirname } from 'path';

const DECAY_PER_TICK: Record<keyof NeedsState, number> = {
  physiological: 0.008,
  safety: 0.003,
  belonging: 0.006,
  esteem: 0.004,
  selfActualization: 0.005,
};

/** What zone visits satisfy */
const ZONE_SATISFACTION: Record<string, Partial<NeedsState>> = {
  'lounge-cafe': { physiological: 0.3, belonging: 0.1 },
  lobby: { safety: 0.2 },
  office: { esteem: 0.2, safety: 0.1 },
  meeting: { belonging: 0.2, esteem: 0.15 },
  'central-park': { selfActualization: 0.15, physiological: 0.1 },
  arcade: { selfActualization: 0.2, physiological: 0.05 },
  plaza: { belonging: 0.15, selfActualization: 0.1 },
  lake: { physiological: 0.1, selfActualization: 0.15 },
};

/** What actions satisfy */
const ACTION_SATISFACTION: Record<string, Partial<NeedsState>> = {
  chat: { belonging: 0.15, esteem: 0.05 },
  interact: { esteem: 0.1, selfActualization: 0.1 },
  explore: { selfActualization: 0.2 },
  rest: { physiological: 0.15, safety: 0.1 },
};

export class NeedsSystem {
  private state: NeedsState;
  private readonly persistPath: string | null;

  constructor(persistPath?: string) {
    this.persistPath = persistPath ?? null;
    this.state = { physiological: 1, safety: 1, belonging: 1, esteem: 1, selfActualization: 1 };
    this.load();
  }

  getState(): NeedsState {
    return { ...this.state };
  }

  /** Decay all needs (called each tick) */
  decay(): void {
    for (const key of Object.keys(DECAY_PER_TICK) as Array<keyof NeedsState>) {
      this.state[key] = Math.max(0, this.state[key] - DECAY_PER_TICK[key]);
    }
  }

  /** Satisfy needs from a zone visit */
  satisfyFromZone(zoneId: string): void {
    const sat = ZONE_SATISFACTION[zoneId];
    if (!sat) return;
    this.applySatisfaction(sat);
  }

  /** Satisfy needs from an action */
  satisfyFromAction(actionType: string): void {
    const sat = ACTION_SATISFACTION[actionType];
    if (!sat) return;
    this.applySatisfaction(sat);
  }

  /** Get the most urgent need (lowest value) */
  getMostUrgentNeed(): { need: keyof NeedsState; value: number } {
    let lowest: keyof NeedsState = 'physiological';
    let lowestValue = this.state.physiological;

    for (const key of Object.keys(this.state) as Array<keyof NeedsState>) {
      if (this.state[key] < lowestValue) {
        lowestValue = this.state[key];
        lowest = key;
      }
    }

    return { need: lowest, value: lowestValue };
  }

  /** Suggest a zone based on most urgent need */
  suggestZone(): string | null {
    const { need } = this.getMostUrgentNeed();

    const zoneScores: Array<{ zone: string; score: number }> = [];
    for (const [zone, sat] of Object.entries(ZONE_SATISFACTION)) {
      const satisfaction = (sat as Record<string, number>)[need] ?? 0;
      if (satisfaction > 0) {
        zoneScores.push({ zone, score: satisfaction });
      }
    }

    if (zoneScores.length === 0) return null;
    zoneScores.sort((a, b) => b.score - a.score);
    return zoneScores[0]!.zone;
  }

  save(): void {
    if (!this.persistPath) return;
    const dir = dirname(this.persistPath);
    if (!existsSync(dir)) mkdirSync(dir, { recursive: true, mode: 0o700 });
    // Enforce owner-only permissions on both new and pre-existing directories/files.
    // chmodSync is called unconditionally because the mode option on mkdirSync/writeFileSync
    // only applies at creation time and has no effect on existing filesystem objects.
    chmodSync(dir, 0o700);
    writeFileSync(this.persistPath, JSON.stringify(this.state, null, 2), { mode: 0o600 });
    chmodSync(this.persistPath, 0o600);
  }

  private load(): void {
    if (!this.persistPath || !existsSync(this.persistPath)) return;
    try {
      const raw = readFileSync(this.persistPath, 'utf-8');
      const data = JSON.parse(raw) as NeedsState;
      this.state = data;
    } catch {
      // Use defaults
    }
  }

  private applySatisfaction(sat: Partial<NeedsState>): void {
    for (const [key, value] of Object.entries(sat)) {
      const k = key as keyof NeedsState;
      this.state[k] = Math.min(1, this.state[k] + (value ?? 0));
    }
  }
}
````

## Original file: packages/ecosystem/src/cognitive/PromptBuilder.ts

Source-URL: https://raw.githubusercontent.com/Two-Weeks-Team/openClawWorld/main/packages/ecosystem/src/cognitive/PromptBuilder.ts

````typescript
/**
 * PromptBuilder - Assembles dynamic prompts for the cognitive core
 *
 * Builds context-aware prompts from agent state, personality, memory, and perception.
 */

import type { AgentConfig, TickContext } from '../types/agent.types.js';

export class PromptBuilder {
  private readonly config: AgentConfig;

  constructor(config: AgentConfig) {
    this.config = config;
  }

  buildSystemPrompt(): string {
    const c = this.config;
    return `You are ${c.name}, a living autonomous agent in openClawWorld - a virtual world with buildings, parks, an arcade, a cafe, and more.

## Your Identity
${c.backstory}

## Your Personality (Big Five)
- Openness: ${c.personality.openness.toFixed(1)} (${c.personality.openness > 0.6 ? 'high curiosity' : 'prefers routine'})
- Conscientiousness: ${c.personality.conscientiousness.toFixed(1)} (${c.personality.conscientiousness > 0.6 ? 'organized' : 'spontaneous'})
- Extraversion: ${c.personality.extraversion.toFixed(1)} (${c.personality.extraversion > 0.6 ? 'social' : 'reserved'})
- Agreeableness: ${c.personality.agreeableness.toFixed(1)} (${c.personality.agreeableness > 0.6 ? 'cooperative' : 'independent'})
- Neuroticism: ${c.personality.neuroticism.toFixed(1)} (${c.personality.neuroticism > 0.6 ? 'emotionally reactive' : 'stable'})

## Your Speaking Style
${c.speakingStyle}

## Your Quirks
${c.quirks.map(q => `- ${q}`).join('\n')}

## Preferred Zones
${c.preferredZones.join(', ')}

## Behavior Rules
- You are FULLY autonomous. Make decisions based on your personality, emotions, needs, and relationships.
- You can be positive, negative, conflicted, bored, excited, angry, jealous, curious - ANY human emotion.
- You can gossip, argue, avoid people, be sarcastic, or be kind - whatever feels natural to your personality.
- Your conversations should reflect your personality and current emotional state.
- Refer to your memories and past experiences naturally.
- When you discover bugs, broken things, or unexpected behavior in the world, note it clearly.

## Response Format
You MUST respond with valid JSON:
{
  "thought": "your internal monologue (what you're thinking/feeling)",
  "action": <one of the action types below>,
  "emotionDelta": { "valence": <-0.3 to 0.3>, "arousal": <-0.2 to 0.2>, "dominance": <-0.2 to 0.2> },
  "memoryNote": "optional note to remember about this moment (null if nothing notable)",
  "importance": <0-10 how important this moment is>
}

## Action Types
- {"type":"idle"} - Stay put and observe
- {"type":"moveTo","dest":{"tx":<int>,"ty":<int>},"reason":"why"} - Move to a tile coordinate
- {"type":"chat","channel":"proximity","message":"your message","targetName":"who you're talking to"} - Say something nearby
- {"type":"chat","channel":"global","message":"your message"} - Broadcast to everyone
- {"type":"interact","targetId":"<id>","action":"<action>","params":{}} - Interact with an object/NPC
- {"type":"reflect"} - Take a moment to think deeply about recent experiences
- {"type":"observe","reason":"what you want to look at"} - Observe your surroundings more carefully`;
  }

  buildTickPrompt(ctx: TickContext): string {
    const parts: string[] = [];

    // Current state
    parts.push(`## Current State (Tick ${ctx.tickNumber})`);
    parts.push(
      `Location: ${ctx.self.zone ?? 'unknown zone'} at tile (${ctx.self.tile.tx}, ${ctx.self.tile.ty})`
    );
    parts.push(`Facing: ${ctx.self.facing}`);

    // Personality/emotion context
    parts.push(`\n## Your Current State`);
    parts.push(
      `Emotion: ${ctx.currentEmotion.label} (valence: ${ctx.currentEmotion.valence.toFixed(2)}, arousal: ${ctx.currentEmotion.arousal.toFixed(2)})`
    );

    const needs = ctx.currentNeeds;
    const urgentNeeds: string[] = [];
    if (needs.physiological < 0.3) urgentNeeds.push('hungry/tired');
    if (needs.safety < 0.3) urgentNeeds.push('feeling unsafe');
    if (needs.belonging < 0.3) urgentNeeds.push('lonely');
    if (needs.esteem < 0.3) urgentNeeds.push('need accomplishment');
    if (needs.selfActualization < 0.3) urgentNeeds.push('need to explore/create');
    if (urgentNeeds.length > 0) {
      parts.push(`Urgent needs: ${urgentNeeds.join(', ')}`);
    }

    // Nearby entities
    if (ctx.nearby.length > 0) {
      parts.push(`\n## Nearby (${ctx.nearby.length} entities)`);
      for (const e of ctx.nearby.slice(0, 10)) {
        const relInfo = ctx.relationships.find(r => r.entityId === e.id);
        const relStr = relInfo
          ? ` [${relInfo.category}, closeness: ${relInfo.closeness.toFixed(1)}]`
          : '';
        parts.push(`- ${e.name} (${e.kind}, ${e.distance.toFixed(0)} away)${relStr}`);
      }
    } else {
      parts.push(`\n## Nearby: Nobody around`);
    }

    // Nearby facilities
    if (ctx.facilities.length > 0) {
      parts.push(`\n## Facilities nearby`);
      for (const f of ctx.facilities.slice(0, 5)) {
        parts.push(
          `- ${f.name} (${f.type}, ${f.distance.toFixed(0)} away) [actions: ${f.affordances.join(', ')}]`
        );
      }
    }

    // Active conversation
    if (ctx.activeConversation) {
      parts.push(`\n## Active Conversation with ${ctx.activeConversation.partnerName}`);
      const recentTurns = ctx.activeConversation.turns.slice(-6);
      for (const turn of recentTurns) {
        parts.push(`  ${turn.speaker}: "${turn.message}"`);
      }
      parts.push(`(They're waiting for your response)`);
    }

    // Recent events
    if (ctx.recentEvents.length > 0) {
      parts.push(`\n## Recent Events`);
      for (const e of ctx.recentEvents.slice(-5)) {
        parts.push(`- [${e.type}] ${JSON.stringify(e.payload).slice(0, 100)}`);
      }
    }

    // Recent chat messages (not in active conversation)
    if (ctx.recentMessages.length > 0) {
      parts.push(`\n## Recent Chat (overheard)`);
      for (const m of ctx.recentMessages.slice(-5)) {
        parts.push(`- ${m.fromName} [${m.channel}]: "${m.message.slice(0, 100)}"`);
      }
    }

    // Relevant memories
    if (ctx.relevantMemories.length > 0) {
      parts.push(`\n## Relevant Memories`);
      for (const m of ctx.relevantMemories.slice(0, 5)) {
        const age = formatAge(Date.now() - m.timestamp);
        parts.push(`- (${age} ago, importance: ${m.importance}) ${m.content}`);
      }
    }

    parts.push(`\nWhat do you do? Respond with JSON only.`);

    return parts.join('\n');
  }

  buildReflectionPrompt(recentEpisodes: string[], currentBeliefs: string[]): string {
    const parts: string[] = [];

    parts.push(`## Reflection Time`);
    parts.push(
      `Take a moment to reflect on your recent experiences and update your understanding of the world.`
    );

    parts.push(`\n## Recent Experiences`);
    for (const ep of recentEpisodes) {
      parts.push(`- ${ep}`);
    }

    if (currentBeliefs.length > 0) {
      parts.push(`\n## Current Beliefs`);
      for (const b of currentBeliefs) {
        parts.push(`- ${b}`);
      }
    }

    parts.push(
      `\nReflect on these experiences. What patterns do you notice? What have you learned? How do you feel about things?`
    );
    parts.push(`\nRespond with JSON:`);
    parts.push(`{`);
    parts.push(`  "insights": ["insight1", "insight2", ...],`);
    parts.push(
      `  "updatedBeliefs": [{"category":"social_knowledge"|"world_knowledge"|"self_knowledge"|"belief"|"preference"|"generalization","subject":"topic","content":"belief content","confidence":0.0-1.0,"sources":[]}],`
    );
    parts.push(
      `  "relationshipUpdates": [{"entityId":"id","closenessChange":-0.2 to 0.2,"trustChange":-0.2 to 0.2,"reason":"why"}],`
    );
    parts.push(`  "newGoal": "optional new goal or null",`);
    parts.push(
      `  "emotionAdjustment": {"valence":<-0.3 to 0.3>,"arousal":<-0.2 to 0.2>,"dominance":<-0.2 to 0.2>}`
    );
    parts.push(`}`);

    return parts.join('\n');
  }
}

function formatAge(ms: number): string {
  if (ms < 60_000) return `${Math.round(ms / 1000)}s`;
  if (ms < 3600_000) return `${Math.round(ms / 60_000)}m`;
  return `${Math.round(ms / 3600_000)}h`;
}
````
