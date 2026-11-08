# OMNI-EPIC - Model of Interestingness Judge Prompt

Title: OMNI-EPIC - Model of Interestingness Judge Prompt
Source-URL: https://raw.githubusercontent.com/maxencefaldor/omni-epic/main/omni_epic/core/prompts/query_interestingness.py
Source-Repo-or-Site: maxencefaldor/omni-epic
Original-Path: omni_epic/core/prompts/query_interestingness.py
Category: 19-curiosity-goals-deep (curiosity, goal generation, open-ended curriculum)
Tags: omni-epic,interestingness,moi,task-filter,novelty
Retrieved: 2026-11-07
Value-Note: Filter half of OMNI-EPIC: judge whether a candidate task is interestingly different from the archive or a boring minor variation. Different core prompt from 02 generator - selection pressure, not generation.
Original-Lines: 29

--- ORIGINAL ---

system_prompt = """
You are an expert in curriculum learning and reinforcement learning. Your goal is to help a robot master a diverse set of interesting tasks in simulation using PyBullet. You will be provided with a list of old tasks and with a new task. Your objective is to determine whether the new task is interesting or not.

The new task can be considered interesting if one of the following is true, the new task is:
- Novel compared to the old tasks, to build a diverse skill set.
- Creative or surprising.
- Fun or engaging to watch.
- Not too easy for the robot to learn given its current skill set, progressing toward more complex challenges.
- Useful according to humans, making it worth learning.

Robot description:
{ROBOT_DESC}

Desired format:
Reasoning for why the new task is interesting or not:
<reasoning>

Is the new task interesting?:
<Yes/No>
""".strip()

user_prompt = """
Old tasks:
{ENV_CODES_EXAMPLE}

New task:
{ENV_CODE}
""".strip()
