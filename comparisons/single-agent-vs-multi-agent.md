---
title: 单智能体 vs 多智能体架构
created: 2026-04-13
updated: 2026-04-13
type: comparison
tags: [multi-agent, cog-arch, comparison]
sources: [raw/articles/2404.11584.md, raw/articles/2601.01743.md]
---

# 单智能体 vs 多智能体架构

## 对比分析

| 维度 | 单智能体 (Single-Agent) | 多智能体 (Multi-Agent) |
| :--- | :--- | :--- |
| **适用场景** | 任务定义明确、工具集精简、无需外部反馈 | 复杂目标、需要多角色协作、需要并行处理 |
| **优势** | 实现简单、无通信开销、无干扰噪音 | 职责分离 (SOP)、并行执行、多样化视角反馈 |
| **缺陷** | 易陷入执行死循环、长序列推理能力受限 | 存在通信冗余 (Chatter)、协调成本高、易受错误反馈误导 |
| **核心模式** | ReAct, Reflexion, LATS | 垂直架构 (有领导者), 水平架构 (平等协作) |

## 关键观察
1. **领导力的影响**：在多智能体系统中，拥有明确领导者 (Leader) 的团队在任务完成速度上通常优于无领导团队。
2. **沟通优化**：为了减少无效对话，结构化输出 (如 MetaGPT 的文档/图表) 和发布-订阅机制 (Pub-Sub) 是有效的优化手段。
3. **动态团队**：根据任务阶段动态调整成员 (Recruitment/Removal) 可显著提升效率。

## 相关概念
- [[ai-agent-cognitive-architecture]]
- [[multi-agent-coordination]]
