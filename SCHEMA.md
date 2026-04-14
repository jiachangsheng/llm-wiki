# Wiki Schema: AI Agent 架构研究

## 领域
此 Wiki 专注于 AI Agent (人工智能智能体) 的架构研究，涵盖从底层推理模型、记忆机制、规划能力到工具调用及多智能体协作的完整技术栈。

## 约定
- 文件名：小写，连字符，无空格 (例如 `reflexion-framework.md`)
- 每个 Wiki 页面必须以 YAML 前置元数据开始 (见下文)
- 使用 `[[wikilinks]]` 在页面间建立链接 (每页至少 2 个出站链接)
- 更新页面时，务必更新 `updated` 日期
- 每个新页面必须添加到 `index.md` 的相应章节下
- 每次操作必须追写到 `log.md`

## 前置元数据 (Frontmatter)
```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [来自下方的分类法]
sources: [raw/articles/source-name.md]
---
```

## 标签分类法 (Tag Taxonomy)

### 核心架构 (Architecture)
- `cog-arch`: 认知架构 (Cognitive Architectures)
- `planning`: 规划/调度 (Planning, Task Decomposition)
- `memory`: 记忆机制 (Short-term, Long-term, Vector DB)
- `perception`: 感知/输入处理 (Perception, Multi-modal)
- `action`: 执行/动作空间 (Action Space, Tool Use)

### 推理与策略 (Reasoning & Strategy)
- `reasoning`: 推理链 (CoT, ToT, GoT)
- `reflection`: 自省/反思 (Self-Correction, Reflection)
- `optimization`: 提示词优化/微调 (Prompt Eng, Fine-tuning)
- `evaluation`: 评估指标/基准 (Benchmarks, Eval)

### 协作模式 (Collaboration)
- `multi-agent`: 多智能体系统 (MAS)
- `communication`: 通信协议/协调 (Coordination)
- `hierarchy`: 层级结构 (Manager-Worker, Swarm)

### 技术实现 (Implementation)
- `framework`: 开发框架 (LangChain, AutoGen, CrewAI)
- `llm`: 基础模型/底座 (Front-end LLM)
- `tool`: 外部工具/API (Plugins, Tool-calling)

### 元分析 (Meta)
- `comparison`: 对比分析
- `timeline`: 演进时间线
- `controversy`: 争议点/未决课题
- `prediction`: 未来趋势预测

## 页面创建阈值
- **创建页面**：当一个实体/概念在 2 个或更多来源中出现，或者在一个来源中处于核心地位时。
- **添加到现有页面**：当来源提及已被涵盖的内容时。
- **不要创建页面**：对于随口提及、次要细节或领域外的内容。
- **拆分页面**：当页面超过 ~200 行时 —— 拆分为子主题并建立交叉链接。
- **归档页面**：当内容被完全取代时 —— 移动到 `_archive/`，从索引中移除。

## 页面类型定义
- **实体页面 (Entities)**：具体的框架 (e.g., `autogen.md`), 模型 (e.g., `gpt-4o.md`), 论文作者或实验室。
- **概念页面 (Concepts)**：理论/技术方向 (e.g., `chain-of-thought.md`, `re-act-pattern.md`)。
- **对比页面 (Comparisons)**：两种或多种架构的横向对比 (e.g., `autogen-vs-crewai.md`)。
- **查询页面 (Queries)**：针对特定复杂问题的综合解答 (e.g., `how-to-solve-infinite-loop-in-agents.md`)。

## 更新策略
当新信息与现有内容冲突时：
1. 检查日期 —— 新来源通常取代旧来源
2. 如果确实矛盾，记录两种观点及其日期和来源
3. 在前置元数据中标记矛盾：`contradictions: [page-name]`
4. 在 lint 报告中标记以供用户审阅
