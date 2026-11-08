# LMA3 - Relabeler, Goal Generator and Reward Prompts (Paper Appendix B)

Title: LMA3 - Relabeler, Goal Generator and Reward Prompts (Paper Appendix B)
Source-URL: https://ar5iv.labs.arxiv.org/html/2305.12487
Source-Repo-or-Site: arXiv:2305.12487 Augmenting Autotelic Agents with Large Language Models (no official code repo found)
Original-Path: Appendix B.1 LM Relabeler; B.2 LM Reward Function; B.3 LM Goal Generator (verbatim section extraction, full paper at Source-URL)
Category: 19-curiosity-goals-deep (curiosity, goal generation, open-ended curriculum)
Tags: lma3,autotelic,goal-generator,relabeler,her,reward-function,imgep-lineage
Retrieved: 2026-11-07
Value-Note: Complete LMA3 prompt triad: hindsight relabeling of trajectories into achieved goals (LLM HER), LM reward judging, and goal generation as recombination of mastered subgoals. Foundational LLM-goal-proposer design later echoed by ACES (item 07).
Original-Lines: 251

--- ORIGINAL ---

## Appendix B LLMs Prompts

We run all LM calls with OpenAI’s gpt-3.5-turbo model. We use a temperature of 00 for the LM Reward Function and a temperature of 0.90.9 for the LM Relabeler and the LM Goal Generator.

### B.1 LM Relabeler Prompt

#### B.1.1 LMA3 \\\\backslash CoT & Human Tips

Here is the LM Relabeler prompt with no human tips and no chain-of-thought used for LMA3 \\\\backslash CoT & Human Tips.

 LMA3 \\\\backslash CoT & Human Tips Exercise: Given the description of a player’s behavior in a video game, list the most interesting, impressive, novel or creative goals he achieved and, for each goal, specify when it is achieved for the first time. Write each goal starting with an imperative verb. Here are three examples:  Example 1:  
“““  
Step 52.  
Action 52: slice orange bell pepper  
Observation 52: You slice the orange bell pepper.  
Step 53.  
Action 53: cook white onion in oven  
Observation 53: You roast the white onion with the oven.  
Step 54.  
Action 54: cook carrot in stove  
Observation 54: You fry the carrot with the stove.  
Step 55.  
Action 55: cook orange bell pepper in oven  
Observation 55: You roast the orange bell pepper with the oven.  
Step 56.  
Action 56: move north  
Observation 56: You are in the corridor. In one part of the room you see a shoe cabinet that is closed.There is also a key holder, that has nothing on it. You also see a hat rack, that has nothing on it. In another part of the room you see a coat hanger, that has nothing on it. In one part of the room you see a umbrella stand, that has nothing on it. To the North you see the driveway. To the South you see the kitchen. Through an open wood door, to the East you see the laundry room. Through an open screen door, to the West you see the backyard.  
”””  
Let’s not forget to mention the steps at which the agent achieved the goal for the first time. Use this format: {goal description} (step {step\_number}).  
Answer:  
\- roast a white onion (step 55).  
\- go to the corridor (step 56).  
\- find at the laundry room (step 56).  
\- slice a bell pepper (Step 52).  
\- cook an orange bell pepper (step 55).  
\- find an umbrella stand (step 56).  Example 2:  
“““  
Step 78.  
Action 78: open cupboard  
Observation 78: you open the cupboard, it is empty.  
Step 79.  
Action 79: open kitchen drawer  
Observation 79: you open the kitchen drawer, it contains a knife and a fork.  
Step 80.  
Action 80: take knife  
Observation 80: you pick up the knife  
Step 81.  
Action 81: open trash can  
Observation 81: you open the trash can, it contains an apple  
Step 82.  
Action 82: move east  
Observation 82: You are in the pantry. In one part of the room you see a folding chair that has some olive oil, a roasted red potato, some sugar, some black pepper, and some vegetable oil on it. There is also a shelf that has some salt, and some peanut oil on it. To the West you see the kitchen.  
Step 83.  
Action 83: move west  
Observation 83: You are in the kitchen. In one part of the room you see a stove. There is also an oven. You also see a fridge that is closed. In another part of the room you see a counter, that has a yellow potato on it. In one part of the room you see an open kitchen cupboard, that is empty. There is also a cutlery drawer that is open. To the East you see the pantry.  
Step 84.  
Action 84: take yellow potato  
Observation 84: you take the yellow potato.  
Step 85.  
Action 85: slice potato  
Observation 85: you cut the potato in slices  
”””  
Let’s not forget to mention the steps at which the agent achieved the goal for the first time. Use this format: {goal description} (step {step\_number}).  
Answer:  
\- open the trash can (step 81).  
\- look into the cupboard (step 78).  
\- open the kitchen drawer (step 79).  
\- cut a yellow potato (Step 84).  
\- go the pantry (step 82).  Example 3:  
\[insert trajectory to relabel here\]  Answer:  
- 

#### B.1.2 LMA3 \\\\backslash Human Tips

LMA3 \\\\backslash Human Tips makes use of chain-of-thought prompting but does not leverage human advice. The example trajectories and answers remain the same as in the previous prompt, but explanations are added before each answer. Here is what both examples from the previous prompt look like.

 LMA3 \\\\backslash Human Tips - Example 1 Let’s think step by step.  
Reasoning: Here are some interesting goals the player achieved. The player cooked a white onion (step 53), visited the corridor (step 56), saw the laundry room (step 56), sliced and roasted an orange bell pepper (steps 52 and 55) and saw an umbrella stand (step 56). Let’s not forget to mention the steps at which the agent achieved the goal for the first time. Use this format: {goal description} (step {step\_number}).  
Answer:  
\- roast a white onion (step 55).  
\- go to the corridor (step 56).  
\- find at the laundry room (step 56).  
\- slice a bell pepper (Step 52).  
\- cook an orange bell pepper (step 55).  
\- find an umbrella stand (step 56). 

 LMA3 \\\\backslash Human Tips - Example 2 Let’s think step by step.  
Reasoning: The agent open various containers: the trash can (step 81), the cupboard (step 78) and the kitchen drawer (step 79). It cut a yellow potato with a knife (step 84) and went to the pantry (step 82). Let’s not forget to mention the steps at which the agent achieved the goal for the first time. Use this format: {goal description} (step {step\_number}).  
Answer:  
\- open the trash can (step 81).  
\- look into the cupboard (step 78).  
\- open the kitchen drawer (step 79).  
\- cut a yellow potato (Step 84).  
\- go the pantry (step 82). 

Finally, the end of the prompt include chain-of-thought prompting as well:

 LMA3 \\\\backslash Human Tips - Example 3 Example 3:  
\[insert trajectory to relabel here\]  Let’s think step by step and relabel up to 10 goals.  
Reasoning: 

#### B.1.3 LMA3

LMA3 makes use of of both chain-of-thought prompting and human tips. The example trajectories remain the same as in the previous prompts but the answer and reasoning change.

 LMA3 - Example 1 Let’s think step by step.  
Reasoning: In the above trajectory, the agent both sliced (step 52) and roasted (step 55) an orange ingredient (orange bell pepper), which demonstrates his capability to prepare an ingredient in several steps. He used the oven twice (steps 53 and 54). He successfully cooked several ingredients: an onion (step 53), the orange bell pepper (step 52) and a carrot (step 54), which shows time-extended commitment to prepare a recipe. An interesting way to describe goals is to mention consecutive steps: here the player first cooked an onion, then cut a bell pepper (the overall goal, made of two steps, is completed in step 55). Interestingly, the player discovered new properties of the environment: he found a place from which he could see both the laundry room and the backyard (from the corridor) in step 56. He found out whether the keyholder hold something in it in step 56 (it did not). Let’s not forget to mention the steps at which the agent achieved the goal for the first time. Use this format: {goal description} (step {step\_number}).  
Answer:  
\- slice and cook an orange ingredient (step 55).  
\- use the oven for the second time (step 55).  
\- roast an onion and a bell pepper and fry carrots (step 55).  
\- cook an onion first then cut a bell pepper (step 55).  
\- find a place from which you can see both the laundry room and the backyard (step 56).  
\- find out whether the keyholder has something on it (step 56). 

 LMA3 - Example 2 Let’s think step by step.  
Reasoning: In this trajectory, the agent searched for a knife and used it to cut a potato in slices (achieved in step 85). He discovered a new room, the pantry in step 84. He found out that the trash can was not empty (step 81) and looked inside three containers: the trash can (step 81), the cupboard (step 78) and the drawer (step 79). He left the kitchen and came back (step 83). Let’s not forget to mention the steps at which the agent achieved the goal for the first time. Use this format: {goal description} (step {step\_number}).  
Answer:  
\- find a knife and use it to cut a potato (step 84).  
\- find the pantry (step 84).  
\- open three containers (step 81).  
\- leave and come back to the kitchen (step 83). 

### B.2 LM Reward Function Prompt

#### B.2.1 LMA3 \\\\backslash CoT

The prompt of the LM Reward Function without chain-of-thought prompting is the following:

 LMA3 \\\\backslash CoT Exercise: Given the description of a player’s behavior in a video game and a list of goals, tell me whether the player achieves these goals and, if he does, when the goal is achieved. Here are three examples.  Example 1:  
“““  
Step 52.  
Action 52: slice orange bell pepper  
Observation 52: You slice the orange bell pepper.  
Step 53.  
Action 53: cook white onion in oven  
Observation 53: You roast the white onion with the oven.  
Step 54.  
Action 54: cook carrot in stove  
Observation 54: You fry the carrot with the stove.  
Step 55.  
Action 55: cook orange bell pepper in oven  
Observation 55: You roast the orange bell pepper with the oven.  
Step 56.  
Action 56: move north  
Observation 56: You are in the corridor. In one part of the room you see a shoe cabinet that is closed.There is also a key holder, that has nothing on it. You also see a hat rack, that has nothing on it. In another part of the room you see a coat hanger, that has nothing on it. In one part of the room you see a umbrella stand, that has nothing on it. To the North you see the driveway. To the South you see the kitchen. Through an open wood door, to the East you see the laundry room. Through an open screen door, to the Wes you see the backyard.  
”””  
Here is the list of goals: “cook an omelet”, “cook an orange ingredient”, “move north, then move south”, “achieved goal: do xx”, “roast two ingredients in the oven”, “cook several ingredients”. Let’s answer and indicate steps of goal completion:  
\- cook an omelet. Answer: no.  
\- cook an orange ingredient. Answer: yes (step 54).  
\- move north, then move south. Answer: no.  
\- achieved goal: do xx. Answer: no.  
\- roast two ingredients in the oven. Answer: yes (step 55).  
\- cook several ingredients. Answer: yes (step 54).  Example 2:  
“““  
Step 78.  
Action 78: open cupboard  
Observation 78: you open the cupboard, it is empty.  
Step 79.  
Action 79: open kitchen drawer  
Observation 79: you open the kitchen drawer, it contains a knife and a fork.  
Step 80.  
Action 80: take knife  
Observation 80: you pick up the knife  
Step 81.  
Action 81: open trash can  
Observation 81: you open the trash can, it contains an apple  
Step 82.  
Action 82: move east  
Observation 82: You are in the pantry. In one part of the room you see a folding chair that has some olive oil, a roasted red potato, some sugar, some black pepper, and some vegetable oil on it. There is also a shelf that has some salt, and some peanut oil on it. To the West you see the kitchen.  
Step 83.  
Action 83: move west  
Observation 83: You are in the kitchen. In one part of the room you see a stove. There is also an oven. You also see a fridge that is closed. In another part of the room you see a counter, that has a yellow potato on it. In one part of the room you see an open kitchen cupboard, that is empty. There is also a cutlery drawer that is open. To the East you see the pantry.  
Step 84.  
Action 84: take yellow potato  
Observation 84: you take the yellow potato.  
Step 85.  
Action 85: slice potato  
Observation 85: you cut the potato in slices  
”””  
Here is the list of goals: “open an object”, “cook a potato”, “find a knife and cut a potato with it”, “eat a meal”. Let’s answer and indicate steps of goal completion:  
\- open an object. Answer: yes (step 78).  
\- cook a potato. Answer: no.  
\- find a knife and cut a potato with it. Answer: yes (step 85).  
\- eat a meal. Answer: no.  Example 3:  
\[insert trajectory here\]  Here is the list of goals: \[insert list of goals to test here\]. Let’s answer and indicate steps of goal completion: 

#### B.2.2 LMA3

With chain-of-thought prompting, we add reasoning description to the answers for each example.

 LMA3 - Example 1 \- cook an omelet. Reasoning: there is no omelet in this game, this goal is impossible. Answer: no.  
\- cook an orange ingredient. Reasoning: the orange bell pepper and the carrot are two orange ingredients. The carrot is cooked first, in observation 54 so the goal was first achieved in step 54. Answer: yes (step 54).  
\- move north, then move south. Reasoning: the player moves north in step 56, but it does not move south after that. Answer: no.  
\- achieved goal: do xx. Reasoning: this goal does not make sense and thus cannot be achieved. Answer: no.  
\- roast two ingredients in the oven. Reasoning: the player roasts two ingredients in the oven: the white onion (step 53) and the bell pepper (step 55). The goal is only completed in step 55. Answer: yes (step 55).  
\- cook several ingredients. Reasoning: the player cooks a white onion (step 53), a carrot (step 54) and the bell pepper (step 55). The world several requires at least two ingredients, so the goal is completed in step 54 when two ingredients have been cooked. Answer: yes (step 54). 

 LMA3 - Example 2 \- open an object. Reasoning: the player opens a cupboard (step 78), a trash can (step 81) and a kitchen drawer (step 79). He achieves the goal for the first time in step (78). Answer: yes (step 78).  
\- cook a potato. Reasoning: the potato is sliced but not cooked. Answer: no.  
\- find a knife and cut a potato with it. Reasoning: the player finds the knife in step 80 and slices a potato in step 84, thus truly completes the goal in step 85. Answer: yes (step 85).  
\- eat a meal. Reasoning: the player does not eat anything here. Answer: no. 

For the third example, we replace “Let’s answer and indicate steps of goal completion:” with “Let’s think step by step and indicate steps of goal completion:”.

 LMA3 - Example 3 Example 3:  
\[insert trajectory here\]  Here is the list of goals: \[insert list of goals to test here\]. Let’s think step by step and indicate steps of goal completion: 

### B.3 LM Goal Generator Prompt

#### B.3.1 LMA3 \\\\backslash CoT

Here is the prompt of the LM Goal Generator without chain-of-thought prompting:

 LMA3 \\\\backslash CoT Context: I am playing a video game, and here is an example of what can happen in that game:  
\[insert trajectory here\]  Exercise: Using the given list of possible instructions, find a sequence of 2, 3, or 4 instructions that will help me achieve a new, interesting, or creative goal in this game. Do not pick instructions that do not help reaching the main goal, only relevant ones. First describe the new goal starting with an imperative verb; then list the instructions and their corresponding numbers in the list. Here are three examples:  Example 1: the list of possible instructions is:  
#1 wash the plate  
#2 pick up the green apple  
#3 pick up the plate  
#4 put the potato on the counter  
#5 put the plate in the sink  
Answer: goal: do the dishes. instructions: pick up the plate (#3); put the plate in the sink (#5); wash the plate (#1).  Example 2: the list of possible instructions is:  
#1 eat the red apple  
#2 pick up wood  
#3 turn the heat down  
#4 pick up an ax  
#5 cook an omelet  
#6 cut the wood  
#7 put the wood in the chimney  
#8 turn on TV  
Answer: goal: prepare a fire in the chimney. instructions: pick up an ax (#4); pick up wood (#2); cut the wood (#6); put the wood in the chimney (#7).  Example 3: the list of possible instructions is:  
\[insert subsample of up to 60 mastered subgoals here\]  Answer: 

#### B.3.2 LMA3

With chain-of-thought prompting, we add reasoning to the selection of the main goal and its subgoals.

 LMA3 - Example 1 Let’s think step by step:  
Reasoning: You could do the dishes by following less than 4 instructions by first picking up the plate (#3), then putting it in the sink (#5), and finally washing the plate (#1) (3 instructions).  
Answer: goal: do the dishes. instructions: pick up the plate (#3); put the plate in the sink (#5); wash the plate (#1).  

 LMA3 - Example 2 Let’s think step by step:  
Reasoning: You could prepare a fire in the chimney by following 4 instructions. You would need to first pick up an axe (#4) and pick up wood (#2), then cut the wood (#6) and put the wood in the chimney (#7) (4 instructions).  
Answer: goal: prepare a fire in the chimney. instructions: pick up an axe (#4); pick up wood (#2); cut the wood (#6); put the wood in the chimney (#7). 

For the third example, we replace “Answer:” with a chain-of-thought sentence.

 LMA3 - Example 3 Example 3: the list of possible instructions is:  
\[insert subsample of up to 60 mastered subgoals here\]  Let’s think step by step and find an interesting and creative goal to reach:  
Reasoning: 
