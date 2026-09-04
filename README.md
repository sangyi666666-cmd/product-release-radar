# AI Product Release Radar

持续追踪 Agent 开发平台、AI Worker、DataAgent、通用工作 Agent、Agentic Coding、模型平台、AI 基础设施与产业生态的产品发布和重大更新。

本仓库以公开的一手材料为主要证据，区分可验证事实、厂商口径、产品判断与待验证事项。日报记录高价值增量，周报提炼趋势，产品报告对重要发布做深度拆解。

## 内容入口

- [报告总索引](./INDEX.md)
- [每日行业雷达](./reports/daily/)
- [每周趋势总结](./reports/weekly/)
- [产品发布深度调研](./reports/products/)
- [调研方法与范围](./research/INDUSTRY_RADAR_PLAN.md)
- [信源清单](./research/sources.md)

## 发布机制

1. Codex 定时任务检索过去 24～48 小时的新增信息，并优先回查官方公告、文档、Release Notes、监管文件和官方 GitHub 仓库。
2. 日报落盘后执行质量检查、更新索引并提交到 `main`。
3. GitHub Actions 将新增或更新的报告同步为 GitHub Issue，并添加 `daily`、`weekly` 或 `product-research` 标签。
4. 周报只基于当周日报和结构化事实做聚合分析，不机械拼接日报。

日报同时在 `data/events/YYYY-MM-DD.json` 保存结构化事件。周报优先读取事件数据，避免再次依赖全文抽取，也方便后续建设趋势统计和产品能力时间线。

## 证据标准

- **P0**：官方公告、官方文档、Release Notes、监管文件、论文原文、官方 GitHub Release。
- **P1**：GitHub Trending、开发者社区、Hacker News、专业社区等趋势线索。
- **P2**：科技媒体、行业媒体、分析师及投资机构内容，仅作为线索或背景。
- 重要事实原则上需要 P0 支撑；融资、并购必须区分传闻、宣布、签约和交割。

## 自动发布

本地或定时任务生成报告后运行：

```bash
./scripts/publish.sh "daily 2026-09-04"
```

脚本会校验报告、重建索引、提交并推送；GitHub Actions 随后负责创建或更新对应 Issue。若没有文件变化，脚本不会生成空提交。
