# Generative Agents Self-Generated Daily Agenda Prompts (daily plan, revised plan, hourly schedule, wake-up)

Title: Generative Agents Self-Generated Daily Agenda Prompts (daily plan, revised plan, hourly schedule, wake-up)
Source-URL: https://raw.githubusercontent.com/joonspk-research/generative_agents/main/reverie/backend_server/persona/prompt_template/v3_ChatGPT/daily_planning_v6.txt
Source-Repo-or-Site: joonspk-research/generative_agents (github.com/joonspk-research/generative_agents)
Original-Path: reverie/backend_server/persona/prompt_template/v3_ChatGPT/daily_planning_v6.txt; reverie/backend_server/persona/prompt_template/v2/new_daily_plan_v1.txt; reverie/backend_server/persona/prompt_template/v2/generate_hourly_schedule_v2.txt; reverie/backend_server/persona/prompt_template/v2/wake_up_hour_v1.txt
Category: 08-motivation-drives (intrinsic motivation, curiosity, drives, autonomous goals)
Tags: generative-agents,self-generated-agenda,daily-planning,persona-driven-goals,schedule
Retrieved: 2026-11-07
Value-Note: Agents author their own day: lifestyle plus identity become a broad-strokes plan, yesterday is reinterpreted into a revised plan, then decomposed hourly - intrinsic agenda-setting without an external task giver. Templates are short by design with INPUT placeholders.

--- ORIGINAL ---

## Original file: reverie/backend_server/persona/prompt_template/v3_ChatGPT/daily_planning_v6.txt

Source-URL: https://raw.githubusercontent.com/joonspk-research/generative_agents/main/reverie/backend_server/persona/prompt_template/v3_ChatGPT/daily_planning_v6.txt

````text
daily_planning_v6.txt

Variables: 
!<INPUT 0>! -- Commonset
!<INPUT 1>! -- Lifestyle
!<INPUT 2>! -- Reverie date time now
!<INPUT 3>! -- Persona first names
!<INPUT 4>! -- wake_up_hour

<commentblockmarker>###</commentblockmarker>
!<INPUT 0>!

In general, !<INPUT 1>!
Today is !<INPUT 2>!. Here is !<INPUT 3>!'s plan today in broad-strokes (with the time of the day. e.g., have a lunch at 12:00 pm, watch TV from 7 to 8 pm): 1) wake up and complete the morning routine at !<INPUT 4>!, 2)
````

## Original file: reverie/backend_server/persona/prompt_template/v2/new_daily_plan_v1.txt

Source-URL: https://raw.githubusercontent.com/joonspk-research/generative_agents/main/reverie/backend_server/persona/prompt_template/v2/new_daily_plan_v1.txt

````text
new_daily_plan_v1.txt

Variables: 
!<INPUT 0>! -- Commonset
!<INPUT 1>! -- Persona first name
!<INPUT 2>! -- Day summary string 
!<INPUT 3>! -- Persona first name
!<INPUT 4>! -- Yesterday's daily plan
!<INPUT 5>! -- Yesterday's interpretation
!<INPUT 6>! -- Persona first name

<commentblockmarker>###</commentblockmarker>
!<INPUT 0>!

Memorable things that actually happened to !<INPUT 1>! yesterday:
!<INPUT 2>!

Here the hourly breakdown of !<INPUT 3>!'s original plan yesterday: !<INPUT 4>!

!<INPUT 5>! (No matter what happens, Dolores is absolutely planning to stay at home all day and never go out.) Let's think step by step -- how would !<INPUT 6>! change their plan for today: 1)
````

## Original file: reverie/backend_server/persona/prompt_template/v2/generate_hourly_schedule_v2.txt

Source-URL: https://raw.githubusercontent.com/joonspk-research/generative_agents/main/reverie/backend_server/persona/prompt_template/v2/generate_hourly_schedule_v2.txt

````text
generate_hourly_schedule_v2.txt

Variables: 
!<INPUT 0>! -- Schedule format
!<INPUT 1>! -- Commonset
!<INPUT 2>! -- prior_schedule
!<INPUT 3>! -- intermission_str
!<INPUT 4>! -- intermission 2
!<INPUT 5>! -- prompt_ending

<commentblockmarker>###</commentblockmarker>
Hourly schedule format: 
!<INPUT 0>!
===
!<INPUT 1>!
!<INPUT 2>!
!<INPUT 3>!!<INPUT 4>!
!<INPUT 5>!
````

## Original file: reverie/backend_server/persona/prompt_template/v2/wake_up_hour_v1.txt

Source-URL: https://raw.githubusercontent.com/joonspk-research/generative_agents/main/reverie/backend_server/persona/prompt_template/v2/wake_up_hour_v1.txt

````text
wake_up_hour_v1.txt

Variables: 
!<INPUT 0>! -- Identity Stable Set
!<INPUT 1>! -- Lifestyle
!<INPUT 2>! -- Persona first names

<commentblockmarker>###</commentblockmarker>
!<INPUT 0>!

In general, !<INPUT 1>!
!<INPUT 2>!'s wake up hour:
````
