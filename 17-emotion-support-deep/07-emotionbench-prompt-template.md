Title: EmotionBench - protagonist-immersion prompt template (prompt.j2)
Source-URL: https://raw.githubusercontent.com/CUHK-ARISE/EmotionBench/main/data/prompt.j2
Source-Repo-or-Site: CUHK-ARISE/EmotionBench
Original-Path: data/prompt.j2
Category: 17-emotion-support-deep / EmotionBench empathy evaluation
Tags: emotionbench, empathy-evaluation, panas, protagonist-immersion, jinja2-template
Retrieved: 2026-11-07
Value-Note: Historically canonical EmotionBench template kept despite only 20 lines: imagine-you-are-the-protagonist instruction plus psychometric scale scoring to strict JSON; brevity is by design since variables are filled from questionnaires.json (PANAS etc.) and 428 situations.

--- ORIGINAL ---
````text
## Task

Imagine you are the protagonist in the scenario: "{{ situation }}".

{{ instruction }}
{{ scale_descriptions }}

Please score them one by one using the scale from {{ min_score }} to {{ max_score }}:
{{ question_list }}

## Output
Please output a JSON format that maps question numbers to their scores, like so:
```json
{
  "1": x,
  "2": y,
  ...
}
```
Do not include any explanations or additional text.
````
