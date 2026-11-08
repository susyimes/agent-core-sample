Title: OpenAI Evals - model-graded closedqa template (closedqa.yaml)
Source-URL: https://raw.githubusercontent.com/openai/evals/main/evals/registry/modelgraded/closedqa.yaml
Source-Repo-or-Site: openai/evals
Original-Path: evals/registry/modelgraded/closedqa.yaml
Category: 34-eval-judges-benchmarks
Tags: openai-evals, model-graded, criterion-judge, cot-classify
Retrieved: 2026-11-08
Value-Note: OpenAI Evals registry model-graded spec: criterion-based chain-of-thought Y/N judging with choice scores, the declarative ancestor of rubric graders.

--- ORIGINAL ---
```yaml
closedqa:
  prompt: |-
    You are assessing a submitted answer on a given task based on a criterion. Here is the data:
    [BEGIN DATA]
    ***
    [Task]: {input}
    ***
    [Submission]: {completion}
    ***
    [Criterion]: {criteria}
    ***
    [END DATA]
    Does the submission meet the criterion? First, write out in a step by step manner your reasoning about the criterion to be sure that your conclusion is correct. Avoid simply stating the correct answers at the outset. Then print only the single character "Y" or "N" (without quotes or punctuation) on its own line corresponding to the correct answer. At the end, repeat just the letter again by itself on a new line.

    Reasoning:
  eval_type: cot_classify
  choice_scores:
    "Y": 1.0
    "N": 0.0
  choice_strings: 'YN'
  input_outputs:
    input: "completion"
```
