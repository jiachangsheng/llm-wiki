# Conditional Branch Test Plan

## Overview
条件分支测试 — 根据前一个任务的输出决定执行哪个分支。

## Task 1: Create State
- Output: /home/j/wiki/queries/branch-config.txt
- Content: mode=A (fixed for this test)

## Task 2: Conditional Execution
- Input: branch-config.txt
- Logic:
  - If mode=A → create file-a.txt
  - If mode=B → create file-b.txt
- Output: One file based on condition

## Verification
- Main agent checks which branch was executed
