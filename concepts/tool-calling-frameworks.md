---
title: 工具调用框架
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [tool, action, framework]
sources: [raw/articles/2601.01743.md, raw/articles/2503.12687.md]
---

# 工具调用框架

## 核心逻辑
工具调用将自然语言意图转化为可执行的代码或 API 请求。它通过 **结构化动作空间 (Structured Action Spaces)** 降低幻觉，确保输出符合特定的 Schema 校验。

## 实现模式
- **MRKL 风格**：将语言理解与专业工具解耦。
- **规划-执行循环**：智能体在调用工具前进行规划，调用后根据工具返回的结果进行观察并更新状态。
- **安全屏障 (Guardrails)**：在执行具有副作用 (Side-effecting) 的工具前增加策略检查和用户确认。

## 关键挑战
- **验证与信任**：如何确保工具执行的正确性和安全性。
- **长时程依赖**：在复杂任务中，工具调用序列的错误会迅速累积。

## 相关概念
- [[ai-agent-cognitive-architecture]]
- [[single-agent-vs-multi-agent]]
