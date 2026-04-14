# Hybrid Mode Test Plan

## Overview
混合模式：并行 + 依赖组合

## Phase 1: Parallel (并发)
- AgentA: Create header.txt
- AgentB: Create footer.txt
- Both run simultaneously

## Phase 2: Sequential (依赖)
- AgentC: Read header.txt + footer.txt, merge into document.md

## Files
- Input 1: /home/j/wiki/queries/header.txt
- Input 2: /home/j/wiki/queries/footer.txt
- Output: /home/j/wiki/queries/merged-document.md
