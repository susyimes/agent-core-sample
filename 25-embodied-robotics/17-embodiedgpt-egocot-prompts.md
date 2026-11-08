# EmbodiedGPT EgoCOT Prompts (embodied chain-of-thought)

Title: EmbodiedGPT EgoCOT Prompts (embodied chain-of-thought)
Source-URL: https://ar5iv.labs.arxiv.org/html/2305.15021
Source-Repo-or-Site: arXiv:2305.15021 via ar5iv (EmbodiedGPT)
Original-Path: Listings 1-3 (Sec. 3.1 and Sec. 3.4)
Category: 25-embodied-robotics (language goals into robot plans/code with perception feedback)
Tags: embodiedgpt,egocot,chain-of-thought,verb-noun-actions,ego4d
Retrieved: 2026-11-08
Value-Note: EgoCOT prompts turn egocentric captions into chain-of-thought plans plus verb(noun) actions; training an embodied mind to narrate goals before acting. Official repo is README-only; paper listings are the prompt source.
Truncation-Note: Only Listing 1-3 prompts reproduced (decoded verbatim from ar5iv plain-text listing data); listing headings from paper captions; rest of paper omitted. Full paper at Source-URL.

--- ORIGINAL ---

````text
## Listing 1: Prompt we used for chain-of-thought pre-training.

Watch this video, identify the actions and devise a plan using chain-of-thought. Extract detailed actions using this schema:
Task: {"task description"}
Plan: {"plan with chain-of-thought"} Actions: {{"number"}: {'verb'}({'noun'})}.

## Listing 2: Prompt we used for creating EgoCOT dataset.

You need to generate plans with chain of thought for each task, and then extract  detailed actions (collocation of nouns and verbs) from the plan.
The action can be of the following form:
[action_name], eg., turn left;
[action_name] argument1, eg., pick up(apple);
[action_name] argument1 argument2, eg., put(apple, table)
Task: pick up a cup on the table
plans: grasp the handle of the cup with the gripper and lift it up
Actions:
1. grasp(handle of the cup, gripper)
2. lift up(cup)

## Listing 3: Prompt used for creating EgoVQA dataset.

Please ask some questions accroding to the verbs and nouns in the sentence.
For example, in this sentence "a man is picking up a cup", the verb is picking up and the noun is cup, therefor questions can be "what is the object the man is picking up?" or "what operation is performed on the cup?".
Then You need to give the answer.

input: a man is picking up a cup
question: What is the object the man is picking up
answer: The cup


````
