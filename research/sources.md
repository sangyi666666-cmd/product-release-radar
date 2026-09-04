# 行业雷达信源清单

本文件记录需要长期固定扫描的外部信源及其使用规则。信源等级和事实核验要求以 `INDUSTRY_RADAR_PLAN.md` 为准。

## 基础模型与 Agent Infra 官方信源

- OpenAI 模型目录与模型指南：https://developers.openai.com/api/docs/models 与 https://developers.openai.com/api/docs/guides/latest-model
- Anthropic 官方 News、模型文档与 Release Notes：https://www.anthropic.com/news 与 https://docs.anthropic.com/
- Google Gemini 模型与 API 文档：https://ai.google.dev/gemini-api/docs/models
- 其他厂商：固定扫描官方产品页、模型卡、系统卡、API 文档、定价页和正式发布公告。
- 等级：P0。
- 扫描重点：工具调用、异步执行、上下文与长任务、Coding/Browser/Computer Use、成本与缓存、API 和产品开放范围、安全与治理。
- 核验规则：发布、可用、灰度、地区和套餐分别记录；“即将开放”不得写成“当前所有用户可用”。

## Unite.AI

- 中文站：https://www.unite.ai/zh-cn/
- 英文站：https://www.unite.ai/
- 等级：P2，线索发现与商业背景补充
- 重点栏目：AI 模型与平台、AI 基础、融资、并购
- 扫描频率：每日检查过去 24～48 小时新增内容；周报回看本周高价值产业信号
- 纳入条件：与 Agent、AI Worker、DataAgent、模型平台、AI 基础设施或产业整合存在明确关联
- 核验规则：产品能力和模型指标回查官方发布；融资与并购回查公司、投资机构、监管披露或可信数据库；传闻必须显式标注，不得写成已完成事实
- 输出要求：保留 Unite.AI 原文链接，同时附最终用于事实确认的一级信源链接
