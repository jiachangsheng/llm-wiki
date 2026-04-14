# Progress Control Test Plan

## Overview
测试进度控制 — 监控 subagent 执行进度，支持中途改变方向。

## Mechanism
使用进度文件传递状态：
- Progress file: /home/j/wiki/queries/progress.log
- Status file: /home/j/wiki/queries/status.txt

## Scenario
Agent 执行多步骤数据处理：
1. Step 1: 读取源数据
2. Step 2: 转换格式
3. Step 3: 验证结果
4. Step 4: 写入输出

Main agent 可以在任何步骤后：
- 查看进度
- 暂停任务
- 改变方向（修改处理逻辑）

## Files
- Source: /home/j/wiki/queries/source-data.txt
- Progress: /home/j/wiki/queries/progress.log
- Output: /home/j/wiki/queries/processed-output.txt
