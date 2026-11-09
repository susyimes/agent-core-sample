# Agent Core Template — 从 548 个样本里缝出来的一套能跑的内核

一套六层、文件即自我的个人 Agent 模板。每层取自本仓库已验证的样本机制，
用原创文字重写。自带零依赖 Python 参考运行时（仅标准库）与 9 个测试。

## 结构

```text
template/
  BIBLE.md            # 原则层：可否与冲突裁决（最慢变，人审）
  SOUL.md             # 人格层：声音、品味、行为倾向
  USER.md             # 主人档案（只记已证实的）
  HEARTBEAT.md        # 心跳：单目标源优先级 + 安静合法
  BOOTSTRAP.md        # 出生仪式（首跑后删除）
  state.json          # 状态层：四需求 + 情绪二维，带基线与衰减
  memory/MEMORY.md    # 核心记忆：Persona/Human/Open Loops/事实/洞见
  memory/playbook.md  # 经验条目：原子增删 + helpful/harmful 计数
  prompts/loop.md         # 自主循环操作提示
  prompts/reflect.md      # 睡眠固化：判定、冲突审查、提炼、遗忘
  prompts/evolve.md       # 自进化过闸清单（提案 JSON 格式）
  prompts/curriculum.md   # 下一个目标生成器
  evolution/LOG.md    # 进化谱系（人读）+ log.jsonl（运行时追加）
  runtime/core.py     # 参考运行时：组装、衰减、记忆闸门、提案校验
  tests/test_core.py  # 9 个单元测试
```

冲突裁决序：原则 > 人格 > 记忆事实 > 状态倾向。状态只提议，不裁决。

## 快速开始

```powershell
# 看当前状态与下一目标
python template\runtime\core.py status
# 组装完整分层提示（喂给任意大模型）
python template\runtime\core.py assemble --heartbeat
# 时间流逝：状态向基线衰减并落盘
python template\runtime\core.py tick 6
# 记一个事件冲击（如任务成功）
python template\runtime\core.py bump needs competence 0.4
# 记忆候选过闸检查（≥2 个信号才记）
python template\runtime\core.py score --insight --stance
# 跑测试
python -m unittest discover -s template\tests -v
```

接入真模型：把 `assemble` 输出作为 system prompt，
每轮结束后用 `bump`/`tick` 更新状态，每日跑一次 `prompts/reflect.md` 做固化，
改自文件一律先过 `prompts/evolve.md` 的提案校验（`core.py propose 提案.json`）。

## 每层借了谁的机制

| 层 | 借鉴样本（仓库路径） | 借了什么 |
|---|---|---|
| BIBLE | `02-bible-constitution/01-ouroboros-bible.md`、`24-spec-life-wildcard2/03-openai-model-spec-honesty.md` | 连续性不可自毁、诚实红线、修订留痕 |
| SOUL | `01-soul-md/01-openclaw-official-soul-template.md`、`13-soul-bible-deep/03-gptme-agent-template-soul.md` | 声音而非岗位说明书、改魂要告知、三分边界 |
| 状态 | `07-emotion-affective/01-affectus-emotion-state-engine.md`、`08-motivation-drives/10-openclawworld-maslow-needs-system.md` | 多轴向量加基线衰减、需求每拍衰减、数字归程序管 |
| 记忆 | `05-memory-reflection/01-letta-memgpt-chat-system-prompt.md`、`12-wildcard-consciousness-cn/09-tideline-dream-solidify-zh.md`、`18-memory-systems-deep/07-cognee-review-conflicts.md` | 双档案块、写入判定、现行/被取代/冲突审查 |
| Playbook | `14-self-evolving-frontier/09-ace-curator-playbook-prompt.md` | 原子条目加 helpful/harmful 计数，防简洁坍缩 |
| 循环 | `26-web-computer-use/01-browser-use-system-prompt.md`、`08-motivation-drives/01-voyager-curriculum-prompts.md` | 评估、记忆、下一目标的循环文法；新且不太难的课程提议 |
| 进化闸 | `03-self-evolving/01-darwin-godel-machine-self-improvement-prompt.md`、`03-self-evolving/08-shinkaevolve-prompt-coevolution-prompts.md` | 每代一处可迁移改进、禁止同义换词、谱系与回滚 |
| 出生 | `12-wildcard-consciousness-cn/01-openclaw-bootstrap-identity.md` | 共创名字与物种，完成后删除脚手架 |

## 有意不做的事

不绑定任何模型供应商；不内置向量库（需要时把 memory 换成检索实现，
写入判定与冲突审查别丢）；不自带定时器（用宿主的计划任务调 tick 与固化）；
运行时只做确定性部件，语言判断留在提示里。

本模板的文字为本仓库原创拼装，可自由再用；
机制来源的上游版权归各自项目，引用时请回链样本文件头的 Source-URL。
