# Wiki Log

> 所有 Wiki 操作的顺序记录。仅限追写。
> 格式: `## [YYYY-MM-DD] 操作 | 主体`
> 操作: ingest, update, query, lint, create, archive, delete
> 当此文件超过 500 条记录时，进行轮转：重命名为 log-YYYY.md，重新开始。

## [2026-04-13] create | Wiki 初始化
- 领域: AI Agent 架构研究
- 结构创建完成：SCHEMA.md, index.md, log.md
- 路径: /home/j/wiki

## [2026-04-13] ingest | 三篇 arXiv 综述论文
- 来源：2601.01743, 2404.11584, 2503.12687
- 创建页面:
    - concepts/ai-agent-cognitive-architecture.md
    - concepts/multi-agent-coordination.md
    - concepts/reflexion-pattern.md
    - concepts/tool-calling-frameworks.md
    - comparisons/single-agent-vs-multi-agent.md
- 更新索引并建立交叉引用。

## [2026-04-14] create | 多智能体协作的模型要求
- 响应用户查询："多智能体进行协作，对大模型的要求"
- 创建页面:
    - concepts/model-requirements-for-multi-agent.md
- 更新索引：index.md (总页数：6→7)
- 基于现有 sources 综合整理，涵盖推理、通信、工具调用、规划四个维度

## [2026-04-14] create | 多智能体协作测试指南
- 响应用户查询："我想测试多 agent 协作，怎么测试？"
- 创建页面:
    - concepts/multi-agent-testing-guide.md
- 更新索引：index.md (总页数：7→8)
- 内容涵盖：测试场景设计、评估指标、主流框架对比、基准测试集、实践流程、常见问题调试
