# 信源清单

本文件记录需要长期固定扫描的外部信源及其使用规则。信源等级和事实核验要求以 `INDUSTRY_RADAR_PLAN.md` 为准。

## GitHub AI 趋势发现

### GitHub Trending

- 地址：https://github.com/trending
- 等级：P1，趋势发现。
- 扫描频率：每日。
- 采集内容：热门仓库、当日新增 Star、语言、仓库简介和项目链接。
- 使用规则：热度只用于发现线索；进入日报前必须回查仓库 README、Release、文档或维护者公告。

### GitHub Search API

- 接口：https://api.github.com/search/repositories
- 等级：P1，主题搜索与活跃项目发现。
- 扫描频率：每日搜索最近 7 天仍有更新的仓库。
- 主题标签：仅 `llm`、`ai-agent`、`large-language-model`。
- 处理规则：按仓库去重，排除归档仓库、明显非 AI 项目和纯镜像；Star、Fork 与提交活跃度不得直接写成产品成熟度。
- 核验规则：重要版本和能力结论回查项目 README、Release、文档或维护者公告。

## 基础模型与 Agent Infra 官方信源

- OpenAI 模型目录与模型指南：https://developers.openai.com/api/docs/models 与 https://developers.openai.com/api/docs/guides/latest-model
- Anthropic 官方 News、模型文档与 Release Notes：https://www.anthropic.com/news 与 https://docs.anthropic.com/
- Google Gemini 模型与 API 文档：https://ai.google.dev/gemini-api/docs/models
- 其他厂商：固定扫描官方产品页、模型卡、系统卡、API 文档、定价页和正式发布公告。
- 等级：P0。
- 扫描重点：工具调用、异步执行、上下文与长任务、Coding/Browser/Computer Use、成本与缓存、API 和产品开放范围、安全与治理。
- 核验规则：发布、可用、灰度、地区和套餐分别记录；“即将开放”不得写成“当前所有用户可用”。

## 办公 Agent 与企业 Agent 开发/治理平台

### 固定对象与一手入口

- **办公 Agent**：WorkBuddy（产品页、Enterprise 文档与开放平台文档）、豆包工作、千问办公、Qoder 全系列。每天检查正式公告、产品/帮助中心、Release Notes、定价页与公开的连接器/Skill 文档；重点核验办公入口、跨应用执行、本地/云端边界、连接器、数据与身份、恢复、审批、套餐/地区和企业协作状态。
- **企业 Agent 开发与治理平台**：阿里云 AgentCore / 公开 AgentRun 能力、WorkBuddy 开放平台、AWS Bedrock AgentCore、Microsoft Foundry Agent Service / Control Plane、Google Gemini Enterprise / Agent Platform、火山引擎 AgentKit / HiAgent、LangSmith / LangSmith Deployment。优先扫描各自官方 overview、Release Notes、SDK/API 文档、security/IAM 文档、pricing/SLA 与官方 GitHub Release。
- **已确认的固定公开入口**：WorkBuddy 开放平台 `https://open.workbuddy.cn/`；AWS AgentCore Release Notes `https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html`；Microsoft Foundry Agents 概览 `https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview`；Gemini Enterprise Release Notes `https://docs.cloud.google.com/gemini/enterprise/docs/release-notes`；火山引擎 AgentKit `https://www.volcengine.com/product/agentkit`；Qoder Release Notes `https://docs.qoder.com/zh/release-notes/qoder`；LangSmith Deployment 文档 `https://docs.langchain.com/langsmith/deployment`。

### 每日筛选与记录规则

- 办公 Agent 与业务 Worker 分开建卡：办公 Agent 重点记录任务入口、跨应用动作、用户/组织数据边界和人工接管；业务 Worker 重点记录职责、流程、任务 owner、外部副作用和结果度量。
- 平台能力按 `开发编排、Runtime/Harness、Tool/MCP、身份权限、Sandbox、记忆/知识、发布版本、评测/观测、成本、审计审批、恢复/回滚` 逐项核验。公告中的能力列表不是产品成熟度或已获授权执行的证据。
- 对每个新信号分开记录发布状态（GA、Preview、定向访问、分批灰度、API 可调用、所有套餐可用）、地区/套餐、兼容性与迁移要求；未能由 P0 确认的名称、版本或归属仅作扫描线索，绝不写入对外日报或事件 JSON。

## Unite.AI

- 中文站：https://www.unite.ai/zh-cn/
- 英文站：https://www.unite.ai/
- 等级：P2，线索发现与商业背景补充
- 重点栏目：AI 模型与平台、AI 基础、融资、并购
- 扫描频率：每日检查过去 24～48 小时新增内容；周报回看本周高价值产业信号
- 纳入条件：与 Agent、AI Worker、DataAgent、模型平台、AI 基础设施或产业整合存在明确关联
- 核验规则：产品能力和模型指标回查官方发布；融资与并购回查公司、投资机构、监管披露或可信数据库；传闻必须显式标注，不得写成已完成事实
- 输出要求：保留 Unite.AI 原文链接，同时附最终用于事实确认的一级信源链接

## 虎嗅深度报道

- 地址：https://www.huxiu.com/
- 等级：P2，产品访谈、商业分析和组织背景线索。
- 使用场景：重大产品发布的深度调研与后续复盘，重点补充能力来源、发布时机、用户与组织指标、生态接入深度、伙伴经济、内部协同和反方判断。
- 证据规则：采访对象的原话标记为“受访者口径”，记者独家信息标记为“媒体报道”；产品能力、规模、财务和开放状态尽量回查 P0。
- 分析规则：文章观点用于提出假设和反信号，不直接改写为已确认事实；保留原文链接，并说明与官方口径一致或冲突之处。
