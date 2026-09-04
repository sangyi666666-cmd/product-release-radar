# 企业级 Agent / AI Worker / DataAgent 行业雷达方案

版本：v1.1  
日期：2026-09-02  
## 一、目标与使用者

这套雷达不是普通 AI 新闻摘要。它服务于三个决策：

1. Agent 开发平台与数字员工平台下一步应该补什么能力；
2. HR / 财务 DataAgent 应该选择哪些场景和产品范式；
3. 作为产品经理，本周应该深挖什么、验证什么、推动什么。

目标使用者首先是本人，后续可扩展到产品、算法、研发、业务运营和管理层。

## 二、追踪范围

### A. Agent 开发平台

追踪维度：

- Builder：低代码、代码式、Prompt/Graph/Workflow、调试体验；
- Agent Runtime：长任务、状态、记忆、沙箱、代码执行；
- Tool / Skill：工具协议、Skill 打包、连接器、MCP、A2A；
- Context：知识、检索、企业语义、用户和组织上下文；
- Evaluation：测试集、模拟、Scorer、在线评测、回归；
- Observability：Trace、成本、延迟、失败、版本对比；
- Governance：身份、最小权限、审批、审计、策略、Registry；
- Lifecycle：开发、测试、发布、灰度、回滚、下线；
- Ecosystem：模板、Agent/Skill 市场、开发者生态、定价。

代表对象：火山引擎 AgentKit / VeADK、Microsoft Copilot Studio / Agent Framework、Google Gemini Enterprise Agent Platform / ADK、AWS Bedrock AgentCore、Salesforce Agentforce、ServiceNow AI Agent Studio、OpenAI、Dify、LangGraph、CrewAI、LlamaIndex、n8n、Flowise。

固定跟踪火山引擎 AgentKit 的动态 Harness、Serverless Runtime、MCP / API 工具网关、Agent 身份与权限、沙箱、记忆与知识、评测、可观测性和运营分析，并关注 VeADK、AI 云原生沙箱等相关开发者生态。横向对比时优先纳入 AWS Bedrock AgentCore、Microsoft Agent Framework / Foundry、Google ADK / Agent Platform 等企业级平台。

### B. 数字员工 / AI Worker 平台

追踪维度：

- 岗位、Job、Task、Skill、Tool 与 SOP 的建模方式；
- 单 Agent 与 Agent Team 的组织方式；
- 与 ERP、HCM、财务、工单、办公套件和 RPA 的连接；
- 人机协同、审批、升级、异常接管；
- 数字员工身份、权限、责任、绩效和成本；
- 工作入口：聊天、Inbox、桌面、业务系统内嵌、主动触发；
- 运营管理：Agent System of Record、Control Tower、价值度量；
- 开箱即用的 HR、财务、IT、采购、客服等业务 Agent。

代表对象：Workday Sana / Agent System of Record、SAP Joule / Joule Studio / AI Agent Hub、Oracle Fusion Agentic Applications、UiPath Maestro、ServiceNow AI Agents、Microsoft Agent 365、Salesforce Agentforce、Google Gemini Enterprise。

### C. DataAgent 平台

追踪维度：

- 数据源连接、元数据和指标语义层；
- 问题理解、歧义澄清、查询规划和 NL2SQL；
- SQL/指标校验、查询权限、行列级权限与脱敏；
- 多源数据、结构化与非结构化数据协同；
- 多步分析、Python/代码执行、图表和报告；
- 数据引用、SQL/步骤可解释、置信度和人工确认；
- 主动洞察、异常检测、归因、预测和行动闭环；
- API、MCP、SDK、嵌入和多 Agent 协作；
- 准确率、任务成功率、延迟、成本和业务采用率。

代表对象：Databricks Genie Agents、Snowflake Cortex Agents / Cortex Analyst、Google Conversational Analytics、Microsoft Fabric Data Agent、ThoughtSpot、Tableau / Agentforce Analytics、WrenAI、Vanna、DB-GPT、Dataherald。

### D. 企业内部产品与案例

只跟踪公开披露或明确授权的内部信息：

- 外部公开：企业技术博客、论文、会议演讲、官方客户案例；
- 经授权的内部信息：产品发布说明、需求和缺陷、用户反馈、运营指标、评测结果、事故与复盘；
- 重点不是列举案例，而是提取组织推广、治理、ROI 和失败经验。

### E. 通用工作 Agent 与 Agentic Coding 产品

追踪维度：

- 产品入口：桌面、Web、移动端、IDE、CLI、IM、业务系统内嵌；
- 任务模式：对话、目标委派、定时任务、事件/API 触发、多人/多 Agent 协作；
- 执行环境：本地电脑、云电脑、托管沙箱、企业自有环境；
- 工作产物：文档、表格、PPT、网页、应用、代码和业务系统操作；
- 上下文与连接：本地文件、浏览器、Office、企业知识、IM、连接器、Skill、MCP；
- 数字员工能力：身份、长期记忆、角色、工作区、权限、审批、审计、持续学习；
- 开发者能力：IDE、CLI、插件、Cloud Agent、SDK、API、安全扫描和企业治理；
- 商业模式：个人订阅、团队版、企业版、Credits/API 计费和生态分成。

重点对象：豆包工作、Qoder 全系列、Claude Cowork、Kimi Work；扩展观察 Manus、Genspark、扣子、OpenAI Codex、Cursor、Devin、GitHub Copilot Coding Agent、Google Jules 等相邻产品。

### F. 基础模型与 Agent Infra

基础模型不是独立于 Agent 平台的普通模型新闻，而是决定 Agent 能力上限、运行成本和安全边界的基础设施。重点跟踪：

- Tool Use、函数调用、MCP、异步工具调用、多 Agent 编排和中途指令调整；
- 上下文窗口、记忆、长任务、状态保持、推理强度和最大输出；
- Coding、Browsing、Computer Use、文档与专业软件操作能力；
- 延迟、吞吐、Token 效率、缓存、批处理、定价和任务单位成本；
- API、Chat、Codex/IDE、云平台等入口的开放范围、地区、配额和灰度节奏；
- 安全等级、权限边界、监控、数据驻留、合规和企业治理限制；
- 模型升级对 Agent Builder、Runtime、Evaluation、Observability 与产品交互范式的影响。

重大模型发布若在上述至少两个维度形成实质变化，并有官方模型页、系统卡、发布公告或 API 文档支撑，应作为 Top Signal 候选进入日报评分。只公布单项 Benchmark、缺少可用性信息或与 Agent 工作流无明显关系的模型更新，不因厂商声量自动进入首页。

重点对象包括 OpenAI GPT/Codex 模型、Anthropic Claude、Google Gemini、DeepSeek、阿里通义、字节豆包、腾讯混元、Moonshot/Kimi、智谱 GLM，以及对企业 Agent Runtime 有直接影响的开源模型。

### G. AI 产业与资本动态

重点跟踪对 Agent、AI Worker 和 DataAgent 产品判断有外溢影响的产业信号：

- AI 与模型平台：基础模型、模型服务平台、推理平台、企业模型生态与商业模式；
- AI 基础：算力、芯片、云基础设施、数据中心、推理成本、数据与开发基础设施；
- 融资并购：融资轮次与金额、投资方、估值、并购交易、战略投资和产业整合；
- 资本信号到产品信号的映射：资金流向、能力补齐、生态位变化、商业化压力和潜在整合方向。

融资并购类信息必须区分“宣布、签约、交割、传闻”四种状态；交易金额、估值和参与方应优先回查公司公告、投资机构公告、监管披露或可信数据库。未经确认的消息不得写成已完成交易。

## 三、信源体系

### P0：一级信源——每天优先

- 官方 Release Notes、Changelog、产品博客、开发文档、定价页；
- GitHub Release、Commit、高互动 Issue / PR、Roadmap；
- 官方客户案例和企业技术博客；
- 论文原文与权威 Benchmark；
- MCP、A2A、Agent 协议和安全规范的官方仓库。

### P1：二级信源——发现趋势

- GitHub Trending 与主题搜索；
- Hacker News、Reddit、Lobsters、Dev.to；
- Hugging Face Models / Spaces / Papers；
- Product Hunt；
- arXiv、OpenReview、Papers with Code；
- 官方社区论坛、开发者社区和公开会议材料。

### P2：三级信源——补充商业判断

- 主流科技媒体、行业媒体；
- Unite.AI 中文站与英文站：作为 AI 与模型平台、AI 基础、融资、并购等方向的线索发现源；
- 咨询机构、分析师和投资机构报告；
- 创始人、产品负责人和研究者的公开社交内容。

三级信源不能单独支撑重大产品结论，必须回查 P0 或明确标注“待核实”。Unite.AI 的新闻、评测和观点用于发现线索与补充背景；涉及产品能力、模型指标、融资金额、估值或并购状态时，至少回查一个 P0 来源。

### 内部信源（后续按授权接入）

- JoySpace 产品文档与发布记录；
- Agent 平台与数字员工平台的需求、版本、Issue、评测和运行数据；
- HR / 财务 DataAgent 问题日志、失败样例、用户反馈和工单；
- 内部竞品调研、业务方案、培训与运营材料。

## 四、信号卡数据结构

每个原始信号标准化为：

```yaml
id: source + url + published_at
published_at: 原始发布时间
collected_at: 采集时间
lane: agent_platform | ai_worker | data_agent | work_agent | agentic_coding | foundation_model | ai_platform | ai_infrastructure | capital | enterprise_case | research
source_tier: P0 | P1 | P2 | internal
entity: 产品、项目或公司
signal_type: release | feature | pricing | case | issue | research | standard | funding | acquisition | strategic_investment
title: 原标题
facts: 仅可验证事实
source_url: 原文链接
evidence_quote: 不超过必要长度的证据摘录
analysis: 产品研判
insight: 对产品、平台或业务落地的启示
recommended_action: 观察 | 深拆 | 试用 | 立项讨论 | 风险检查
confidence: high | medium | low
```

## 五、评分与去噪

### 产品价值分

总分 100：

- 与当前三类平台的相关性：25；
- 潜在业务或竞争影响：25；
- 证据质量：20；
- 新颖性：15；
- 可行动性：15。

分级：

- 80～100：Top Signal，进入日报首页并给出行动；
- 60～79：Important，进入对应赛道；
- 40～59：Watch，进入观察池，不占首页；
- 0～39：归档，不推送。

### 去重规则

- 同一发布被多家媒体转述：保留官方源，媒体仅作为补充；
- 同一功能的 Preview、GA 和补丁视为同一演进链；
- GitHub Issue 只有在互动显著、影响生产、代表共性需求时进入日报；
- 没有新增事实时不重复推送，只更新“持续观察”。

### 基础模型进入首页的判断

- 模型名称或 Benchmark 刷新本身不等于高价值信号；必须说明它改变了哪一层 Agent Infra。
- 发布与可用性分开记录：正式发布、定向企业访问、分批灰度、API 可调用和本地/私有部署不得混写。
- 评测结果优先使用官方系统卡与可复现实验，并明确厂商自评和第三方评测的差异。
- 对 Agent 的影响至少落到 Builder、Runtime、Tool、Context、Evaluation、Governance、成本或产品入口中的一个具体对象。

## 六、生产流程

采用“并行采集 + 串行核验和研判”的混合编排：

```text
Agent 平台采集 ─┐
AI Worker 采集 ─┼─→ 标准化/去重 → 事实核验 → 产品研判 → 中文编辑 → PM 复核/行动
DataAgent 采集 ─┤
研究社区采集 ──┤
内部信号采集 ──┘
```

### 角色边界

| 角色 | 任务 | 输出 | 禁止事项 |
|---|---|---|---|
| 采集器 | 发现 24～48 小时新增信号 | 原始信号卡 | 不做战略结论，不把转述当事实 |
| 标准化器 | 分类、去重、关联历史记录 | 规范化信号卡 | 不删除来源和时间 |
| 核验器 | 回查 P0、判断证据和置信度 | 已核验事实 | 证据不足不得补写内容 |
| 产品分析器 | 横向比较、识别趋势、提炼启示 | 启示和建议动作 | 不替代 PM 做路线图决策 |
| 编辑器 | 按模板生成中文日报/周报 | 可读报告 | 不堆砌低分新闻 |
| PM | 确认重点、转成试验或产品动作 | 决策与 Owner | 不把日报阅读当成完成工作 |

### 控制塔指标

- 采集成功率、信源失败率；
- 重复率、P0 信源占比；
- 事实错误率、无证据判断率；
- 日报阅读率、Top Signal 被采纳率；
- 从信号到产品实验/方案的转化数；
- 每条有效洞察的时间和模型成本。

## 七、输出模板

### 每日雷达

1. 今日结论：3～5 句话；
2. Top 5 信号：事实、为什么重要、启示、建议动作；
3. Agent 开发平台；
4. 数字员工 / AI Worker；
5. DataAgent；
6. 开源社区和研究；
7. 企业内部产品/案例；
8. AI 与模型平台 / AI 基础；
9. 融资并购；
10. 风险与反信号；
11. 今天建议深挖的一个问题；
12. 全部来源。

### 每周总结

1. 本周五大变化；
2. 三类平台的趋势线，而非新闻重复；
3. 代表产品能力对比表；
4. 开源活跃度、版本和共性 Issue；
5. 商业化、定价、客户与生态变化；
6. AI 基础设施和资本流向变化；
7. 融资、并购与产业整合；
8. 企业落地案例和失败信号；
9. 对产品建设和业务落地的启示、机会、风险与建议；
10. 下周 Watchlist；
11. 本周个人学习任务。

### 月度专题

- 能力地图版本变化；
- 重点玩家象限和产品路线变化；
- 三类平台融合趋势；
- 当前能力差距与路线图建议；
- 一个月内被证实或被证伪的判断。

## 八、存储结构

```text
reports/
  daily/YYYY-MM-DD.md
  weekly/YYYY-Www.md
  monthly/YYYY-MM.md
research/
  sources.md
  watchlist.md
  product-cards/
state/
  seen-signals.jsonl
  entities.yml
  hypotheses.yml
```

日报保留事实快照；周报观察趋势；`hypotheses.yml` 保存“我们认为会发生什么”和后续证据，避免永远只做事后总结。

## 九、实施路线

### Phase 0：已完成

- 定义范围、信源、模板和评分；
- 生成首期基线日报；
- 创建每日与每周线程推送。

### Phase 1：未来 2 周

- 连续运行并人工复核 10 期日报；
- 统计重复率、有效率和漏报；
- 建立 30～50 个核心产品/项目 Watchlist；
- 调整 Top Signal 阈值和栏目长度。

### Phase 2：未来 1～2 个月

- 将报告沉淀到结构化信号库；
- 增加产品能力卡和版本差异；
- 接入允许访问的内部产品信源；
- 建立每周人工评测和失败分类。

### Phase 3：未来 3～6 个月

- 建成可检索的行业知识库和趋势看板；
- 自动关联外部信号与内部路线图、需求和评测；
- 从“信息雷达”升级为“产品决策和机会发现 Agent”。

## 十、首批核心 Watchlist

### Agent 平台

火山引擎 AgentKit / VeADK、Microsoft Copilot Studio、Microsoft Agent Framework、Google Gemini Enterprise Agent Platform、Google ADK、AWS Bedrock AgentCore、Salesforce Agentforce、ServiceNow AI Agent Studio、OpenAI Agents、Dify、LangGraph、CrewAI、LlamaIndex。

### AI Worker

Workday Sana / ASOR、SAP Joule / AI Agent Hub、Oracle Fusion Agentic Applications、UiPath Maestro、Microsoft Agent 365、Salesforce Agentforce、ServiceNow AI Agents、豆包工作、QoderWork、QoderWake、Claude Cowork、Kimi Work、Manus、Genspark。

### 通用工作 Agent / Agentic Coding

- 豆包工作：桌面工作 Agent、企业上下文、飞书连接、电脑与浏览器操作、云端续跑、多 Agent 协作；
- Qoder 全系列：Qoder、IDE、JetBrains Plugin、CLI、Mobile、Cloud Agents、Agent SDK、QoderWork、QoderWake、Security、Voice；
- 直接对标：Claude Cowork、Kimi Work；
- 相邻对象：OpenAI Codex、Cursor、Devin、GitHub Copilot Coding Agent、Google Jules、Manus、Genspark、扣子。

该组每周至少选一个产品按“入口—上下文—计划—执行—产物—协作—治理—商业化”做版本级对比，避免只记录功能清单。

### DataAgent

Databricks Genie Agents、Snowflake Cortex Agents / Analyst、Google Conversational Analytics、Microsoft Fabric Data Agent、ThoughtSpot Spotter、Tableau、WrenAI、Vanna、DB-GPT、Dataherald。

## 十一、评估方案

前两周由 PM 逐期评审，标注：

- `事实错误`：时间、功能、主体不准确；
- `证据不足`：没有直接来源；
- `低相关`：与三类平台无关；
- `重复`：没有新增信息；
- `泛化`：没有说明产品影响；
- `可行动`：直接促成调研、实验或产品讨论。

两周后目标：

- 重要事实准确率 ≥ 98%；
- Top 5 中 P0 信源占比 ≥ 80%；
- 日报重复率 ≤ 10%；
- 每周至少 1 条信号转化为深拆、实验或路线图讨论；
- 每期阅读时间控制在 8～12 分钟。
