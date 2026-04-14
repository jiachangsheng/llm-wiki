---
title: Reflexion 模式
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [reflection, reasoning, optimization]
sources: [raw/articles/2404.11584.md]
---

# Reflexion 模式

## 定义
Reflexion 是一种通过语言反馈实现自我反思的单智能体模式。它利用 LLM 作为评估器，通过分析当前轨迹和结果，为智能体提供具体且相关的反馈，从而在下一轮迭代中修正行为。

## 工作流
`尝试执行` $\rightarrow$ `评估结果` $\rightarrow$ `生成反思 (Linguistic Feedback)` $\rightarrow$ `更新记忆/计划` $\rightarrow$ `重新尝试`

## 优势与局限
- **优势**：显著降低幻觉率，提升复杂任务的成功率，超越简单的 CoT 或 ReAct。
- **局限**：容易陷入“局部最优解” (Non-optimal local minima)；长期记忆通常受限于 Token 窗口而非数据库。

## 相关概念
- [[ai-agent-cognitive-architecture]]
- [[single-agent-vs-multi-agent]]
