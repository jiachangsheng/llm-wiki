# Systematic Debugging Test Plan

## Overview
创建一个有 bug 的代码，然后用系统化方法调试。

## Bug Scenario
一个简单的 Python 脚本，有一个隐藏的 bug。

## Phases
1. **Phase 1: Root Cause** — 复现 bug，收集证据，找到根因
2. **Phase 2: Pattern** — 找参考代码，对比差异
3. **Phase 3: Hypothesis** — 形成假设，最小化测试
4. **Phase 4: Fix** — 创建测试，修复根因，验证

## Files
- Buggy code: /home/j/wiki/queries/buggy_calculator.py
- Test file: /home/j/wiki/queries/test_calculator.py
