# Chain-of-Thought - GSM8K Original 8-Exemplar Prompt (prompt_original.txt via Chain-of-Thought Hub)

Title: Chain-of-Thought - GSM8K Original 8-Exemplar Prompt (prompt_original.txt via Chain-of-Thought Hub)
Source-URL: https://raw.githubusercontent.com/FranxYao/chain-of-thought-hub/main/gsm8k/lib_prompt/prompt_original.txt
Source-Repo-or-Site: FranxYao/chain-of-thought-hub (https://github.com/FranxYao/chain-of-thought-hub) preserving Wei et al. 2022 exemplars; no Google prompt-file repo exists
Original-Path: gsm8k/lib_prompt/prompt_original.txt
Category: classic-reasoning / chain-of-thought
Tags: chain-of-thought, gsm8k, wei-2022, few-shot, lets-think-step-by-step
Retrieved: 2026-11-07
Value-Note: The foundational Wei et al. (2022) 8-exemplar GSM8K CoT prompt (Question / Lets think step by step / The answer is X) as preserved verbatim by Chain-of-Thought Hub; this exemplar set underlies Self-Consistency decoding too (same prompt, sampled paths + majority vote).
Original-Lines: 59

--- ORIGINAL ---
````text
Question: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
Let's think step by step
There are 15 trees originally.
Then there were 21 trees after some more were planted.
So there must have been 21 - 15 = 6.
The answer is 6.

Question: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
Let's think step by step
There are originally 3 cars.
2 more cars arrive.
3 + 2 = 5.
The answer is 5.

Question: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
Let's think step by step
Originally, Leah had 32 chocolates.
Her sister had 42.
So in total they had 32 + 42 = 74.
After eating 35, they had 74 - 35 = 39.
The answer is 39.

Question: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
Let's think step by step
Jason started with 20 lollipops.
Then he had 12 after giving some to Denny.
So he gave Denny 20 - 12 = 8.
The answer is 8.

Question: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
Let's think step by step
Shawn started with 5 toys.
If he got 2 toys each from his mom and dad, then that is 4 more toys.
5 + 4 = 9.
The answer is 9.

Question: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
Let's think step by step
There were originally 9 computers.
For each of 4 days, 5 more computers were added.
So 5 * 4 = 20 computers were added.
9 + 20 is 29.
The answer is 29.

Question: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
Let's think step by step
Michael started with 58 golf balls.
After losing 23 on tues- day, he had 58 - 23 = 35.
After losing 2 more, he had 35 - 2 = 33 golf balls.
The answer is 33.

Question: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
Let's think step by step
Olivia had 23 dollars.
5 bagels for 3 dollars each will be 5 x 3 = 15 dollars.
So she has 23 - 15 dollars left.
23 - 15 is 8.
The answer is 8.

````
