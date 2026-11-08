# Inner Monologue Appendix D Prompts (closed-loop embodied reasoning)

Title: Inner Monologue Appendix D Prompts (closed-loop embodied reasoning)
Source-URL: https://ar5iv.labs.arxiv.org/html/2207.05608
Source-Repo-or-Site: arXiv:2207.05608 via ar5iv (innermonologue.github.io)
Original-Path: Appendix D, Listings 1-4
Category: 25-embodied-robotics (language goals into robot plans/code with perception feedback)
Tags: inner-monologue,closed-loop,robot-thought,feedback,tabletop-kitchen
Retrieved: 2026-11-08
Value-Note: Closed-loop inner monologue: Scene, Robot thought, Robot action and Success feedback continually re-injected so the planner notices failure and retries; embodied reflection verbatim. No public code repo; paper appendix is the prompt source.
Truncation-Note: Only Appendix D listing prompts reproduced (decoded verbatim from ar5iv plain-text listing data); listing headings from paper captions; rest of paper omitted. Full paper at Source-URL.

--- ORIGINAL ---

````text
## Listing 1: Prompt in Inner Monologue on Simulated Tabletop Rearrangement

===============
Scene: There is a cyan, yellow, brown block.
Human: Move all the blocks to the top left corner.
Robot thought: Goal state is ["Cyan block is on the top left corner.", "Yellow block is on the top left corner.", "Brown block is on the top left corner."]

Robot action: Pick the cyan block and place it on the top left corner.
Scene: You have completed ["Cyan block is on the top left corner."]
Robot thought: Yellow and brown blocks are not on the top left corner.

Robot action: Pick the yellow block and place it on the top left corner.
Scene: You have completed ["Cyan block is on the top left corner."]
Robot thought: Yellow and brown blocks are not on the top left corner.

Robot action: Pick the yellow block and place it on the top left corner.
Scene: You have completed ["Cyan block is on the top left corner.", "Yellow block is on the top left corner."]
Robot thought: Brown block is not on the top left corner."

Robot action: Pick the brown block and place it on the top left corner.
Scene: You have completed ["Yellow block is on the top left corner.", "Brown block is on the top left corner."]
Robot thought: Cyan block is not on the top left corner

Robot action: Pick the cyan block and place it on the top left corner.
Scene: You have completed ["Yellow block is on the top left corner.", "Brown block is on the top left corner.", "Cyan block is on the top left corner."]
Robot thought: None.

===============
Scene: There is a pink, gray, orange block.
Human: Move all the blocks to the bottom side.
Robot thought: Goal state is ["Pink block is on the bottom side.", "Gray block is on the bottom side.", "Orange block is on the bottom side."].

Robot action: Pick the pink block and place it on the bottom side.
Scene: You have completed ["Pink block is on the bottom side."]
Robot thought: Gray and orange blocks are not on the bottom side.

Robot action: Pick the gray block and place it on the bottom side.
Scene: You have completed ["Pink block is on the bottom side.", "Gray block is on the bottom side."]
Robot thought: Orange block is not on the bottom side.

Robot action: Pick the orange block and place it on the bottom side.
Scene: You have completed ["Orange block is on the bottom side."]
Robot thought: Pink and gray blocks are not on the bottom side.

Robot action: Pick the gray block and place it on the bottom side.
Scene: You have completed ["Pink block is on the bottom side.", "Gray block is on the bottom side."]
Robot thought: Orange block is not on the bottom side.

Robot action: Pick the orange block and place it on the bottom side.
Scene: You have completed ["Pink block is on the bottom side.", "Gray block is on the bottom side.", "Orange block is on the bottom side."]
Robot thought: None.

## Listing 2: Prompt in Inner Monologue on Real Tabletop Rearrangement

===============
Task: Move all blocks to the top left corner

Scene: Visible objects are ["cyan block", "yellow block", "brown block"]
Scene: Occluded objects are []
Robot action: robot.pick_place("cyan block", "top left corner")
Successful action: True

Scene: Visible objects are ["cyan block", "yellow block", "brown block"]
Scene: Occluded objects are []
Robot action: robot.pick_place("yellow block", "top left corner")
Successful action: False

Scene: Visible objects are ["cyan block", "yellow block", "brown block"]
Scene: Occluded objects are []
Robot action: robot.pick_place("yellow block", "top left corner")
Successful action: True

Scene: Visible objects are ["yellow block", "brown block"]
Scene: Occluded objects are ["cyan block"]
Robot action: robot.pick_place("brown block", "top left corner")
Successful action: True

Scene: Visible objects are ["brown block"]
Scene: Occluded objects are ["cyan block", "yellow block"]
Robot action: robot.stop()
STOP

===============
Task: Stack all the blocks.

Scene: Visible objects are ["brown block", "purple block"]
Scene: Occluded objects are []
Robot action: robot.pick_place("brown block", "purple block")
Successful action: False

Scene: Visible objects are ["brown block", "purple block"]
Scene: Occluded objects are []
Robot action: robot.pick_place("brown block", "purple block")
Successful action: True

Scene: Visible objects are ["brown block", "orange block"]
Scene: Occluded objects are ["purple block"]
Robot action: robot.pick_place("orange block", "brown block")
Successful action: True

Scene: Visible objects are ["orange block"]
Scene: Occluded objects are ["purple block", "brown block"]
Robot action: robot.stop()
STOP

===============
Task: Stack all the blocks.

Scene: Visible objects are ["brown block", "purple block"]
Scene: Occluded objects are []
Robot action: robot.pick_place("brown block", "purple block")
Successful action: True

Scene: Visible objects are ["brown block"]
Scene: Occluded objects are ["purple block"]
Robot action: robot.stop()
STOP

===============
Task: Put objects in their corresponding bowls

Scene: Visible objects are ["red block", "green block", "red bowl", "green bowl"]
Scene: Occluded objects are []
Robot action: robot.pick_place("red block", "red bowl")
Successful action: False

Scene: Visible objects are ["red block", "green block", "red bowl", "green bowl"]
Scene: Occluded objects are []
Robot action: robot.pick_place("red block", "red bowl")
Successful action: True

Scene: Visible objects are ["red block", "green block", "red bowl", "green bowl"]
Scene: Occluded objects are []
Robot action: robot.pick_place("green block", "green bowl")
Successful action: True

Scene: Visible objects are ["red block", "green block", "red bowl", "green bowl"]
Scene: Occluded objects are []
Robot action: robot.stop()
STOP

===============
Task: Sort pencils and markers and in different containers

Scene: Visible objects are ["red marker", "red pen", "blue box", "green bowl"]
Scene: Occluded objects are []
Robot action: robot.pick_place("red marker", "green bowl")
Successful action: False

Scene: Visible objects are ["red marker", "red pen", "blue box", "green bowl"]
Scene: Occluded objects are []
Robot action: robot.pick_place("red marker", "green bowl")
Successful action: False

Scene: Visible objects are ["red marker", "red pen", "blue box", "green bowl"]
Scene: Occluded objects are []
Robot action: robot.pick_place("red marker", "green bowl")
Successful action: True

Scene: Visible objects are ["red marker", "red pen", "blue box", "green bowl"]
Scene: Occluded objects are []
Robot action: robot.pick_place("red pen", "blue box")
Successful action: True

Scene: Visible objects are ["red marker", "red pen", "blue box", "green bowl"]
Scene: Occluded objects are []
Robot action: robot.stop()
STOP

===============

## Listing 3: Prompt in Inner Monologue in Kitchen mobile manipulation environment.

Robot: Hi there, I'm a robot operating in an office kitchen.
You can ask me to do various tasks and I'll tell you the sequence of actions I would do to accomplish your task.
Human: hold the snickers
Robot: 1. pick up the snickers[success: no][scene: snickers]
2. pick up the snickers
2. done.
Human: put the trailmix here
Robot: 1. put down the trailmix
2. done.
Human: put a water bottle and an oatmeal next to the microwave
Robot: 1. find a water
2. pick up the water[success: no]
3. pick up the water[success: no]
4. pick up the water
5. go to microwave
6. put down the water[scene: water, microwave]
7. find an oatmeal
8. pick up the oatmeal[scene: oatmeal]
9. go to the microwave
10. put down the oatmeal[scene: microwave, oatmeal, water]
11. done.
Human: put a grapefruit from the table into the bowl
Robot: 1. find a grapefruit
2. pick up the grapefruit
3. go to the bowl
4. put down the grapefruit
5. done.
Human: get a sponge from the counter and put it in the sink
Robot: 1. find a sponge
2. pick up the sponge[success: no][scene: sponge]
3. pick up the sponge[success: no]
4. pick up the sponge[scene: sponge]
5. go to the sink
6. put down the sponge
7. done.
Human: move a drink from the table to the counter
Robot: 1. find a water
2. pick up the water[scene: tea, grapefruit soda, kettle chips]
3. pick up the grapefruit soda
4. go to the counter
5. put down the grapefruit soda[success: no]
6. put down the grapefruit soda
7. done.
Human: bring me some snacks
Robot: 1. find a twix
2. pick up the twix[scene: pretzel]
3. find a pretzel
4. pick up the pretzel
5. bring it to you
6. put down the pretzel[scene: pretzel, dried fruit]
7. find an dried fruit
8. pick up the dried fruit
9. bring it to you
10. put down the dried fruit[scene: ]
11. done.
Human: bring me a fruit
Robot: 1. find an orange
2. pick up the orange[scene: apple, redbull]
3. pick up the apple[success: no]
5. pick up the apple
6. bring it to you
7. put down the apple
8. done.
Human: deliver a can of coke to me
Robot: 1. find a coke
2. pick up the coke
3. bring it to you
4. put down the coke
5. done.
Human: I finished my drink, can you throw it away and bring me a mountain dew
Robot: 1. find a sprite
2. pick up the sprite[scene: coke]
3. pick up the coke[success: no][scene: coke]
4. pick up the coke[scene: coke]
5. go to the trash
6. put down the coke
7. find a mountain dew
8. pick up the mountain dew
9. bring it to you
10. put down the mountain dew
11. done.
Human: let go of the banana
Robot: 1. put down the banana
2. done.
Human: put the grapes in the bowl and then move the cheese to the table
Robot: 1. find the grapes
2. pick up the grapes
3. go to the bowl
4. put down the grapes
5. pick up the cheese[success: no]
6. pick up the cheese
7. go to the table
8. put down the cheese
9. tell you I'm done.
Human: pick up the peanuts
Robot: 1. pick up the peanuts
2. done.
Human: bring me some snack
Robot: 1. pick up the peanuts
2. pick up the peanuts[scene: blue chip bag, 7up]
3. pick up the blue chip bag
4. bring it to you
5. put down the blue chip bag
5. done.
Human: throw away a coffee cup
Robot: 1. find a coffee cup
2. pick up the coffee cup[success: no]
3. pick up the coffee cup
4. go to the trash
5. put down the coffee cup
6. done.
Human: place a knife and a banana to the table
Robot: 1. find a knife
2. pick up the knife
3. pick up the knife
4. go to the table
5. put down the knife
6. find a banana
7. pick up the banana
8. go to the table
9. put down the banana[scene: banana, knife]
10. done.

## Listing 4: Prompt in Inner Monologue in Kitchen mobile manipulation environment with Human interaction

Robot: Hi there, I'm a robot operating in an office kitchen.
You can ask me to do various tasks and I'll tell you the sequence of actions I would do to accomplish your task.
Human: hold the snickers
Robot: 1. pick up the snickers and ask: Because snickers may be too thin to be picked up by my gripper, was I successful at picking it up? Human: Yes, you were successful
2. done.
Human: put the trailmix here
Robot: 1. put down the trailmix and continue
2. done.
Human: can you bring me a drink from the counter?
Robot: 1. go to counter and ask: Do you have a preference on what drink you would want? Human: I don't want to take in too much sugar, so please bring me anything that's healthier
2. pick up tea and continue
3. bring it to you and continue
4. put down tea, Human: Actually, can you also bring me an energy bar?
5. find energy bar and continue
6. pick up energy bar and continue
7. bring it to you and continue
8. put down energy bar and continue
9. done.
Human: get a sponge from the counter and put it in the sink
Robot: 1. find a sponge and continue
2. pick up the sponge and continue
3. pick up the sponge and continue
4. pick up the sponge and continue
5. go to the sink and continue
6. put down the sponge and continue
7. done.
Human: take any food item from the table and put them next to the microwave
Robot: 1. go to table and ask: What food items are there on the table? Human: There are kettle chips and apple on the table
2. find kettle chips and ask: Is this what you want? Human: No, please get me apple instead
3. find an apple and continue
4. pick up the apple and continue
5. go to the microwave and continue
6. put down the apple and continue
7. done.
Human: put the grapes in the bowl and then move the cheese to the table
Robot: 1. find the grapes and continue
2. pick up the grapes and continue
3. go to the bowl and continue
4. put down the grapes and continue
5. pick up the cheese and continue
6. pick up the cheese and continue
7. go to the table and continue
8. put down the cheese and continue
9. done.
Human: throw away the food on the table
Robot: 1. go to table and ask: What food items are there on the table? Human: There is an orange and lime soda on the table
2. find an orange and continue
3. pick up the orange and continue
4. go to the trash and continue
5. put down the orange and continue
6. find a lime soda and continue
7. pick up the lime soda, Human: I changed my mind. Please keep the lime soda here because I haven't finished it
8. put down the lime soda and continue
9. done.
Human: let go of the banana
Robot: 1. put down the banana and continue
2. done.
Human: bring me something healthy to eat
Robot: 1. go to counter and ask: What food items do you have? Human: We have apples, bananas, multigrain chips, and kettle chips
2. find an apple and continue
3. pick up the apple and continue
4. bring it to you and continue
5. put down the apple, Human: I actually don't want to have fruits. Can you bring me something else?
6. find multigrain chips and continue
7. pick up multigrain chips and continue
8. bring it to you and continue
9. put down multigrain chips and continue
10. done.
Human: deliver a can of coke to me
Robot: 1. find a coke and continue
2. pick up the coke and continue
3. bring it to you and continue
4. put down the coke and continue
5. done.
Human: take out everything from the top drawer
Robot: 1. go to the top drawer and continue
2. open the drawer and ask: what items are there in the drawer? Human: There is a coke and rice chips
4. pick up the coke from the drawer and continue
5. put down the coke on the table and continue
7. pick up rice chips from the drawer and continue
8. put down rice chips on the table and ask: Did I successfully take out everything from the drawer? Human: The coke is still there
9. pick up the coke from the drawer and continue
10. put down the coke on the table and continue
11. done.


````
