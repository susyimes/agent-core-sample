# Evolve — 自进化过闸清单（改任何自文件前必填）

把提案写成 JSON 交给运行时校验（见 runtime/core.py propose），并追加到 evolution/LOG.md：

```json
{
  "target_layer": "persona | playbook | memory | loop | state | bible",
  "target_file": "相对 template/ 的路径",
  "failure_class": "针对哪一类失败（不许写单个个案）",
  "change": "一句话说清改什么，每代只改一处",
  "expected_direction": "预期朝哪个指标变好",
  "eval_plan": "用什么留出任务/检查证明变好，评测集不许顺手改",
  "parent_version": "改动前的文件哈希或 git 提交",
  "rollback": "具体回滚动作（还原哪个文件到哪个版本）",
  "human_approved": false
}
```

## 硬规则

1. 每代只改一处，且必须可迁移：能写成「以后凡 X 类情况都该 Y」才算数。
2. 没有评测不改。评测要用执行锚（测试、任务结果、主人抽查），不用自评当唯一证据。
3. 变异禁止同义换词。换说法不叫进化。
4. 落盘后在 evolution/LOG.md 记：日期、提案、评测差值、保留或回滚的决定。
5. target_layer=bible，或任何不可逆外发改动：human_approved 必须为真才准落盘。
6. 两次连续无改进：停。复盘失败类别是不是提错了，不叠补丁。
