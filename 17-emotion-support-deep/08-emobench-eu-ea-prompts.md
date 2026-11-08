Title: EmoBench - Emotional Understanding / Application prompts EN+ZH (prompts.yaml)
Source-URL: https://raw.githubusercontent.com/Sahandfer/EmoBench/master/src/configs/prompts.yaml
Source-Repo-or-Site: Sahandfer/EmoBench
Original-Path: src/configs/prompts.yaml
Category: 17-emotion-support-deep / EmoBench emotional intelligence benchmark
Tags: emobench, emotional-understanding, emotional-application, bilingual, perspective-taking
Retrieved: 2026-11-07
Value-Note: EmoBench bilingual (EN/ZH) system and task prompts for Emotional Understanding (emotion + cause) vs Emotional Application (most effective response) multiple-choice over 400 hand-crafted scenarios; perspective-taking instruction is the whole test interface.

--- ORIGINAL ---
```yaml
sys:
  en: |
    # Instructions
    
    In this task, you are presented with a scenario, a question, and multiple choices. 
    Carefully analyze the scenario and take the perspective of the individual involved.
    Then, select the option that best reflects their perspective or emotional response.

    # Output
  zh: |
    # 说明
    在这个任务中，你会面临一个场景、一个问题和多个选项。
    仔细分析场景，并从相关人员的角度进行思考。
    然后，选择最能反映他们的观点或情绪反应的选项。

    # 输出
EA:
  en: |
    ## Scenario
    {scenario}
    
    ## Question 
    In this scenario, what is the most effective {q_type} for {subject}?
    
    ## Choices
    {choices}
  zh: |
    ## 场景
    {scenario}
    
    ## 问题
    在这个场景中，{subject}最有效的{q_type}是什么？
    
    ## 选项
    {choices}
EU:
  en: |
    ## Scenario
    {scenario}
    
    ## Question 1
    What emotion(s) would {subject} ultimately feel in this situation?
    
    ## Choices for Question 1
    {emo_choices}

    ## Question 2
    Why would {subject} feel these emotions in this situation?

    ## Choices for Question 2
    {cause_choices}
  zh: |
    ## 场景
    {scenario}
    
    ## 问题 1
    在这种情况下，{subject}最终会感受到什么情绪？
    
    ## 问题 1 的选项
    {emo_choices}

    ## 问题 2
    {subject}为什么会在这种情况下感受到这些情绪？

    ## 问题 2 的选项
    {cause_choices}
```
