# Parallel Agent Test Plan

## Overview
测试多 agent 并行执行能力，验证 subagent 协作工作流。

## Tasks

### Task 1 (AgentA): Python Async Research
**目标：** 研究 Python 异步编程核心概念

**交付物：**
- 创建文件：`/home/j/wiki/queries/python-async-summary.md`
- 内容包含：
  - asyncio 核心概念（event loop, coroutine, task, future）
  - async/await 语法要点
  - 常见使用场景
  - 3 个代码示例

**工具集：** terminal, file

---

### Task 2 (AgentB): Rust Ownership Research
**目标：** 研究 Rust 所有权系统核心概念

**交付物：**
- 创建文件：`/home/j/wiki/queries/rust-ownership-summary.md`
- 内容包含：
  - 所有权三原则
  - 借用（borrowing）规则
  - 生命周期（lifetimes）简介
  - 3 个代码示例

**工具集：** terminal, file

---

## Execution Mode
- 并行执行（batch mode）
- Main agent 负责最终汇总

## Success Criteria
- 两个文件都成功创建
- 内容准确、有代码示例
- 总执行时间 < 单个任务串行执行时间
