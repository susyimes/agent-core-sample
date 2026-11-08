# WizardLM Evol-Instruct - Depth Evolution Rewriter Prompts (depth.py)

Title: WizardLM Evol-Instruct - Depth Evolution Rewriter Prompts (depth.py)
Source-URL: https://raw.githubusercontent.com/nlpxucan/WizardLM/main/Evol_Instruct/depth.py
Source-Repo-or-Site: nlpxucan/WizardLM (https://github.com/nlpxucan/WizardLM)
Original-Path: Evol_Instruct/depth.py
Category: 14-self-evolving-frontier
Tags: wizardlm, evol-instruct, instruction-evolution, depth-evolution, complexity
Retrieved: 2026-11-07
Value-Note: Instruction evolution by rewriting: one Prompt Rewriter meta-prompt plus six depth operators (add constraints, deepen, concretize, increase reasoning steps, complicate input, breadth) applied round after round to grow Alpaca seeds into WizardLM training data. Short file (see Original-Lines) kept because these exact operator strings spawned the whole Evol-Instruct data lineage; breadth.py holds the sibling create-new-instruction variant and is not collected separately.
Original-Lines: 34

--- ORIGINAL ---
````python
base_instruction = "I want you act as a Prompt Rewriter.\r\n \
					Your objective is to rewrite a given prompt into a more complex version to make those famous AI systems (e.g., chatgpt and GPT4) a bit harder to handle.\r\n \
					But the rewritten prompt must be reasonable and must be understood and responded by humans.\r\n \
					Your rewriting cannot omit the non-text parts such as the table and code in #The Given Prompt#:. Also, please do not omit the input in #The Given Prompt#. \r\n \
					You SHOULD complicate the given prompt using the following method: \r\n\
					{} \r\n\
					You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #The Given Prompt#. \r\n\
					'#The Given Prompt#', '#Rewritten Prompt#', 'given prompt' and 'rewritten prompt' are not allowed to appear in #Rewritten Prompt#\r\n"


def createConstraintsPrompt(instruction):
	prompt = base_instruction.format("Please add one more constraints/requirements into #The Given Prompt#'")
	prompt += "#The Given Prompt#: \r\n {} \r\n".format(instruction)
	prompt += "#Rewritten Prompt#:\r\n"
	return prompt

def createDeepenPrompt(instruction):
	prompt = base_instruction.format("If #The Given Prompt# contains inquiries about certain issues, the depth and breadth of the inquiry can be increased.")
	prompt += "#The Given Prompt#: \r\n {} \r\n".format(instruction)
	prompt += "#Rewritten Prompt#:\r\n"
	return prompt

def createConcretizingPrompt(instruction):
	prompt = base_instruction.format("Please replace general concepts with more specific concepts.")
	prompt += "#The Given Prompt#: \r\n {} \r\n".format(instruction)
	prompt += "#Rewritten Prompt#:\r\n"
	return prompt


def createReasoningPrompt(instruction):
	prompt = base_instruction.format("If #The Given Prompt# can be solved with just a few simple thinking processes, you can rewrite it to explicitly request multiple-step reasoning.")
	prompt += "#The Given Prompt#: \r\n {} \r\n".format(instruction)
	prompt += "#Rewritten Prompt#:\r\n"
	return prompt
````
