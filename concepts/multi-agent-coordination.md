---
title: 多智能体协调机制
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [multi-agent, communication, hierarchy]
sources: [raw/articles/2404.11584.md, raw/articles/2601.01743.md]
---

# 多智能体协调机制

## 组织结构
1. **垂直架构 (Vertical Architecture)**：
    - 一个领导者 Agent 统一调度，汇报者仅与其通信或在共享会话中由领导者分配任务。
    - 特点：分工明确，效率较高，但依赖领导者的能力。
2. **水平架构 (Horizontal Architecture)**：
    - 所有 Agent 处于平等地位，在共享线程中讨论。
    - 特点：适合需要头脑风暴、协同咨询的场景，但容易产生冗余对话。

## 协调策略
- **动态团队构建**：根据任务阶段 (规划 $\rightarrow$ 执行 $\rightarrow$ 评估) 动态招募或移除专业 Agent。
- **结构化通信**：用文档/图表代替非结构化对话，减少噪音。
- **信息过滤**：通过订阅机制让 Agent 仅接收与其目标相关的信息。

## 相关概念
- [[single-agent-vs-multi-agent]]
- [[ai-agent-cognitive-architecture]]
