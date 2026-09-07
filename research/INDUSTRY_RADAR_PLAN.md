# 调研方法与范围

版本：v1.2  
更新日期：2026-09-04

## 一、目标

产品雷达持续发现、核验和分析 Agent 产业的重要变化，服务三类决策：

1. 判断 Agent 平台、AI Worker 和 DataAgent 的能力演进方向；
2. 识别值得深拆、试用或持续观察的产品与技术；
3. 把外部信号转化为有证据的产品启示和建议动作。

雷达不追求新闻数量。每条重要信息必须区分事实、判断与建议，并保留直接来源。

## 二、追踪范围

| 赛道 | 重点观察内容 |
| --- | --- |
| Agent 开发平台 | Builder、Runtime、Tool/Skill、MCP/A2A、Context、Evaluation、Observability、Governance、Lifecycle、生态与定价 |
| 数字员工 / AI Worker | Job/Task/SOP 建模、Worker 身份与记忆、Agent Team、人机协同、审批接管、业务系统连接、运营与价值度量 |
| DataAgent | 数据连接、语义层、NL2SQL、多步分析、代码执行、证据引用、权限、评测、主动洞察和行动闭环 |
| 通用工作 Agent / Agentic Coding | 桌面、Web、IDE、CLI 和移动入口；本地/云端执行；长任务、产物、多 Agent 协作、安全与商业化 |
| 基础模型与 Agent Infra | 工具调用、长上下文、记忆、Coding/Browser/Computer Use、延迟、成本、API 可用性、安全与治理 |
| 产业与生态 | AI 基础设施、重要开源项目、企业公开案例、融资、并购、战略投资和生态整合 |

重大基础模型发布属于 Agent Infra。若它在工具调用、长任务、执行能力、成本或治理等至少两个维度产生实质变化，应进入 Top Signal 候选；单项 Benchmark 刷新不自动进入首页。

## 三、信源体系

| 等级 | 用途 | 典型来源 | 使用规则 |
| --- | --- | --- | --- |
| P0 | 确认事实 | 官方公告、文档、模型卡、系统卡、Release Notes、定价页、监管文件、论文原文、官方 GitHub Release | 重要结论优先使用；记录发布日期、状态与开放范围 |
| P1 | 发现趋势 | GitHub Trending、GitHub Search API、Hacker News、Hugging Face、Product Hunt、研究与开发者社区 | 用于发现线索和社区信号，关键事实回查 P0 |
| P2 | 补充背景 | 主流科技媒体、行业媒体、分析师与投资机构内容 | 不单独支撑重大产品、融资或并购结论 |

### GitHub AI 趋势发现

每天并行扫描两个来源：

1. **GitHub Trending**：读取当日热门仓库及新增 Star，发现突然升温的 AI 项目；
2. **GitHub Search API**：搜索最近 7 天仍有活跃更新的仓库，仅覆盖 `llm`、`ai-agent`、`large-language-model` 三个主题标签。

处理规则：

- 合并三个标签结果，并按仓库唯一标识去重；
- 排除归档仓库、明显非 AI 项目和纯镜像；
- Star、Fork 和近期提交只表示热度，不直接代表产品成熟度；
- 进入日报的项目必须说明新增事实、Agent 相关性与产品影响；
- 重要版本和能力结论回查项目 README、Release、文档或维护者公告。

完整固定信源和扫描规则见 [sources.md](./sources.md)。

## 四、标准信号卡

每条信号保存为结构化事件：

```yaml
id: 来源 + URL + 发布时间
published_at: 原始发布时间
collected_at: 采集时间
lane: agent_platform | ai_worker | data_agent | work_agent | agentic_coding | foundation_model | ai_platform | ai_infrastructure | capital | enterprise_case | research
source_tier: P0 | P1 | P2
entity: 产品、项目或公司
signal_type: release | feature | pricing | case | issue | research | standard | funding | acquisition | strategic_investment
title: 原始事件标题
facts: 可验证事实列表
source_urls: 直接来源列表
analysis: 产品判断
insight: 产品启示
recommended_action: 观察 | 深拆 | 试用 | 立项讨论 | 风险检查
confidence: high | medium | low
score: 0-100
```

## 五、评分与入选

信号价值总分 100：

| 维度 | 分值 |
| --- | ---: |
| 与雷达重点赛道的相关性 | 25 |
| 潜在业务或竞争影响 | 25 |
| 证据质量 | 20 |
| 新颖性 | 15 |
| 可行动性 | 15 |

| 分数 | 处理方式 |
| --- | --- |
| 80～100 | Top Signal，进入日报首页并给出建议动作 |
| 60～79 | Important，进入对应赛道 |
| 40～59 | Watch，进入观察池 |
| 0～39 | 归档，不推送 |

分数是信息优先级，不是产品质量分，也不是事实正确率。事实可信度由 `source_tier` 和 `confidence` 单独表达。

### 特殊判断

- **基础模型**：分别记录正式发布、定向访问、灰度、API 可调用和普遍可用；厂商自评与第三方评测分开。
- **融资并购**：严格区分传闻、宣布、签约和交割；金额与参与方优先回查公司、投资机构或监管披露。
- **开源项目**：热度上涨不等于进入首页；需要正式版本、关键能力、重大 Issue、生态采用或持续趋势支撑。

## 六、去重与核验

- 同一事件被多家媒体转述时，以官方源为主，媒体只补充背景；
- Preview、GA、重要补丁作为同一产品演进链记录，但新增状态可再次进入日报；
- 最近 7 天没有新增事实的事件不重复推送；
- 标题、摘要或搜索结果不能直接作为事实，必须打开原文核验；
- 证据不足的内容进入 Watch，不补写、不猜测。

## 七、生产流程

```text
多源发现 → 标准化与去重 → P0 核验 → 价值评分 → 产品分析 → 日报/周报 → GitHub 发布
```

| 环节 | 输出 | 质量要求 |
| --- | --- | --- |
| 发现 | 原始线索 | 覆盖过去 24～48 小时，保留原始 URL |
| 标准化 | 信号卡 | 统一实体、赛道、事件类型和时间 |
| 核验 | 已确认事实 | 重要结论有 P0，证据不足明确标记 |
| 分析 | 判断、启示、动作 | 不把推断写成厂商事实 |
| 发布 | Markdown、JSON、GitHub Issue | 校验通过、无重复、链接可访问 |

## 八、输出

### 日报

- 今日结论；
- Top 5：事实、产品判断、启示、建议动作；
- 各赛道高价值增量；
- 基础模型与 Agent Infra；
- 风险与反信号；
- 今日建议深挖；
- 全部直接来源和质量记录。

### 周报

- 本周五大变化与趋势线；
- 代表产品能力对比；
- 基础模型对 Agent Infra 的影响；
- 开源版本、社区共性问题、商业化与生态变化；
- 融资并购和产业整合；
- 启示、机会、风险与下周 Watchlist。

### 产品深度调研

重大产品发布不能停留在功能和架构清单，必须进一步回答：

- **为什么现在发布**：能力来源、历史积累、竞争窗口与发布节奏；
- **是否真的成熟**：公开能力、可用能力和稳定能力分别是什么；
- **价值如何兑现**：个人价值如何沉淀为组织资产并进入业务流程，北极星指标是什么；
- **生态有多深**：伙伴开放的是入口、轻量能力，还是核心数据与执行能力；
- **硬件做到哪一层**：采集外设、跨端流转、设备调用、端侧执行或设备管理；
- **伙伴能否经营**：分发、运营、营销、收费、分润和结算是否闭环；
- **网络效应是否成立**：用户和伙伴为什么加入、留存与迁移成本来自哪里；
- **组织能否支撑战略**：内部产品边界、跨团队协同和资源分配是否存在冲突；
- **有哪些反信号**：厂商叙事、公开事实、真实接入深度与商业结果之间有何差距。

完整报告按 [产品发布调研模板](../templates/product-research.md) 执行，并同时分析 Agent 开发、Runtime、AgentOps、安全治理、竞品与后续观察项。

## 九、存储与发布

```text
reports/
  daily/YYYY-MM-DD.md
  weekly/YYYY-Www.md
  products/YYYY-MM-DD-产品名.md
data/
  events/YYYY-MM-DD.json
  source-state.json
research/
  INDUSTRY_RADAR_PLAN.md
  sources.md
```

Markdown 是正式档案，结构化事件用于去重和周报聚合，GitHub Issue 是发布与订阅入口。报告校验通过后提交 `main`，由 GitHub Actions 创建或更新对应 Issue。

## 十、核心 Watchlist

- **Agent 平台**：火山引擎 AgentKit/VeADK、AWS Bedrock AgentCore、Microsoft Foundry/Agent Framework、Google ADK/Agent Platform、Salesforce Agentforce、ServiceNow、Dify、LangGraph、CrewAI、LlamaIndex。
- **AI Worker**：Workday Sana、SAP Joule、Oracle、UiPath、Microsoft Agent 365、Salesforce、ServiceNow、豆包工作、QoderWork/QoderWake、Claude Cowork、Kimi Work、Manus、Genspark。
- **DataAgent**：Databricks Genie、Snowflake Cortex、Google Conversational Analytics、Microsoft Fabric Data Agent、ThoughtSpot、Tableau、WrenAI、Vanna、DB-GPT。
- **Agentic Coding**：OpenAI Codex、Qoder、Cursor、Devin、GitHub Copilot Coding Agent、Google Jules。
- **基础模型**：OpenAI GPT/Codex、Anthropic Claude、Google Gemini、DeepSeek、通义、豆包、混元、Kimi、GLM 及重要开源模型。

## 十一、质量指标

- 重要事实准确率 ≥ 98%；
- Top 5 的 P0 信源占比 ≥ 80%；
- 日报重复率 ≤ 10%；
- 每周至少 1 条信号转化为深拆、试用或产品讨论；
- 日报阅读时间控制在 8～12 分钟。
