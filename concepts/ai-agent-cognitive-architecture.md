---
title: AI Agent 认知架构概览
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [cog-arch, planning, memory, action]
sources: [raw/articles/2601.01743.md, raw/articles/2404.11584.md, raw/articles/2503.12687.md]
---

# AI Agent 认知架构概览

## 核心定义
AI Agent 是将基础模型（Foundation Models）与推理、规划、记忆和工具调用相结合的系统，旨在将自然语言意图转化为现实世界的计算操作。其核心在于建立一个“感知-决策-执行”的闭环。

## 架构组成模块
根据多篇综述，现代 Agent 架构通常包含以下核心组件：
- **策略核心 (Policy Core)**：通常由 LLM/VLM 充当，负责将上下文映射为决策。
- **规划模块 (Planning)**：
    - **任务分解**：将复杂目标拆分为子任务。
    - **多计划选择**：在多个候选方案中选择最优路径。
    - **反思与精炼**：通过 [[reflexion-pattern]] 等机制进行自我修正。
- **记忆机制 (Memory)**：
    - **工作记忆 (Working Memory)**：维持当前任务相关的短期上下文。
    - **语义/情节记忆 (Semantic/Episodic Memory)**：通过 RAG 或向量数据库存储长效知识和历史经验。
- **动作空间 (Action Space)**：
    - **工具调用 (Tool Use)**：通过 API 扩展能力。
    - **环境交互**：包括 GUI 操作、物理机器人控制等。

## 关键设计权衡
- **自主性 vs 可控性 (Autonomy vs Controllability)**：高自主性增加灵活性但可能导致失控；强约束提高可靠性但限制能力。
- **延迟 vs 准确率 (Latency vs Accuracy)**：通过增加测试时计算 (Test-time compute) 如树搜索可提升质量，但增加延迟。
- **能力 vs 可靠性 (Capability vs Reliability)**：随着能力增强，非确定性增加，使得评估和调试更加困难。

## 相关概念
- [[single-agent-vs-multi-agent]]
- [[agent-transformer]]
- [[tool-calling-frameworks]]
