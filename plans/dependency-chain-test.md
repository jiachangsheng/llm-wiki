# Dependency Chain Test Plan

## Overview
测试依赖任务链 — 后一个任务依赖前一个任务的输出。

## Task Chain

### Task 1: Create Config
**Agent:** AgentA
**Output:** `/home/j/wiki/queries/config-source.json`
**Content:** Simple JSON config with name, version, settings

---

### Task 2: Process Config
**Agent:** AgentB
**Input:** `/home/j/wiki/queries/config-source.json` (from Task 1)
**Output:** `/home/j/wiki/queries/config-processed.md`
**Action:** Read JSON, convert to markdown documentation

---

### Task 3: Verify
**Agent:** Main Agent
**Input:** `/home/j/wiki/queries/config-processed.md` (from Task 2)
**Action:** Verify file exists and has expected content

---

## Execution Mode
- Sequential (Task 2 waits for Task 1)
- Pass file paths between tasks
