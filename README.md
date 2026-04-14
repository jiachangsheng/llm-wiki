# LLM Wiki - AI Agent 架构研究

> 一个专注于 AI Agent (人工智能智能体) 架构研究的双语知识库

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 简介

本 Wiki 系统性地整理 AI Agent 领域的核心概念、架构模式、框架对比和实践经验。内容涵盖从底层推理模型、记忆机制、规划能力到工具调用及多智能体协作的完整技术栈。

- **语言**: 中文 / English 双语
- **格式**: Markdown + YAML Frontmatter
- **工具**: Obsidian 兼容 (支持 wikilinks 和知识图谱)

## 🗂️ 内容结构

```
wiki/
├── concepts/          # 核心概念 (认知架构、推理模式、反思机制等)
├── comparisons/       # 架构对比 (单智能体 vs 多智能体等)
├── entities/          # 实体 (框架、模型、论文作者等)
├── queries/           # 查询 (针对特定问题的综合解答)
├── raw/               # 原始资料 (论文、文章)
├── plans/             # 测试计划和实验记录
├── index.md           # 内容索引
├── SCHEMA.md          # 知识图谱规范和标签分类法
└── log.md             # 更新日志
```

## 📚 核心主题

### 认知架构 (Cognitive Architecture)
- AI Agent 的核心组件和认知循环
- 感知 → 推理 → 规划 → 执行的完整链路

### 多智能体系统 (Multi-Agent Systems)
- 垂直/水平组织结构
- 协调策略和通信协议
- 测试方法和评估指标

### 推理与反思 (Reasoning & Reflection)
- Chain-of-Thought (CoT), Tree-of-Thought (ToT)
- Reflexion 自省模式
- 自我修正机制

### 工具调用 (Tool Calling)
- 实现模式和安全挑战
- 结构化动作空间
- 主流框架对比

## 🏷️ 标签分类

| 分类 | 标签 |
|------|------|
| 核心架构 | `cog-arch`, `planning`, `memory`, `perception`, `action` |
| 推理策略 | `reasoning`, `reflection`, `optimization`, `evaluation` |
| 协作模式 | `multi-agent`, `communication`, `hierarchy` |
| 技术实现 | `framework`, `llm`, `tool` |

## 🚀 使用方式

### 本地浏览
```bash
git clone https://github.com/jiachangsheng/llm-wiki.git
cd llm-wiki
# 使用 Obsidian 打开目录，或直接用文本编辑器
```

### 搜索内容
- 在 `index.md` 中查找页面索引
- 使用 `SCHEMA.md` 了解标签分类法
- 通过 wikilinks `[[page-name]]` 在页面间导航

### 贡献内容
1. 参考 `SCHEMA.md` 的格式规范
2. 创建新页面时添加 YAML Frontmatter
3. 更新 `index.md` 和 `log.md`

## 📊 统计

- 总页数: 8+
- 核心概念: 6
- 架构对比: 1
- 测试计划: 7

## 📝 更新日志

详见 [`log.md`](log.md)

## 📄 许可证

MIT License

---

**最后更新**: 2026-04-14
