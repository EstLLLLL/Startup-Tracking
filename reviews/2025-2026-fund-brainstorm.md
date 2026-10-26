# 两年融资地图：为基金讨论找到值得追问的方向

**这份材料的用途，是从融资案例里提出可检验的投资假设，再决定研究资源往哪里放。融资热度只说明资本愿意承担风险；客户回款、实验结果、交付与单位经济性才决定判断是否成立。**

研究范围：2025 全年市场背景，以及 2025–2026/10/23 的精选案例和跨年跟进。医疗与药物发现与其他重点赛道同等分析。本次为首版讨论材料，2025 全年逐笔回填尚未完成。

## 先看 2025：资金回暖，但项目面并未同步变宽

| 指标 | 2025 数值 | 含义与边界 |
|---|---:|---|
| 全球创投与成长投资 | $425B，超过 24,000 家公司 | Crunchbase 全球口径，金额同比 +30%；不是 Axios 样本 |
| 全球 AI 融资 | $211B | 约占一半资金，标签可能与医疗、金融等重叠 |
| 全球医疗及生物科技 | $71.7B | 全医疗口径，不能与美国数字医疗数据相加 |
| 最大五家融资公司 | $84B，约占全球 20% | 少数超大单显著影响整体热度 |
| 全球 fintech | $51.8B、3,457 笔 | 金额 +27%，笔数 -23%，说明回暖集中在更大的单笔融资 |

来源：[Crunchbase 2025 全年复盘](https://news.crunchbase.com/venture/funding-data-third-largest-year-2025/)；[fintech 全年复盘](https://news.crunchbase.com/fintech/funding-jumped-big-checks-ai-ye-2025/)。这是两个相近但不相同的分类表，不把行业标签求和。

**对讨论的启发：应当同时看“钱去了哪里”和“有多少不同公司能够持续获得钱”。** 大额融资可能对应真实需求，也可能是资本开支、临床开发或获客亏损的前置融资。2025 精选案例与 2026 Axios 样本来源不同，本版不计算两年融资笔数或金额同比。

## 第一轮建议讨论的六条投资假设

下表是研究优先级建议，不是已完成的投资结论。医疗单列，并进一步区分工具、平台和药物资产。

| 方向 | 已看到的案例链 | 值得研究的机制 | 需要什么证据才继续推进 | 什么会削弱判断 |
|---|---|---|---|---|
| 专用模型与生产推理 | Together、Fireworks、Baseten 在 2025 和 2026 继续融资 | 企业数据、评估、后训练与运行成本合在一起，可能比通用 API 更深入客户流程 | 同一任务质量下的全成本、毛利、负载留存、客户集中度 | 价格优势只来自补贴或低利用率租赁；模型换代后优化优势消失 |
| AI 应用的持久基础设施 | Supabase，法律流程的 Harvey | 新应用增加数据库、权限、审计和专业工作流需求 | 上线应用存活、付费负载、企业留存；实施与服务成本 | 数据库创建或注册数增长，付费与留存没有跟上 |
| 电力部署、调度与结算 | Base Power 同年 B→C；Gridware；Fervo | 瓶颈从新增设备扩展到部署、控制权、并网和回款 | 每设备/每项目全成本、可交付容量、实际结算收益、项目与公司资本责任 | 只靠补贴/价差，收益不足以覆盖安装、维护与融资成本 |
| 真实世界自主系统 | Saronic、Shield AI；Figure 为承诺资本案例 | 仿真—测试—交付反馈，与制造和可靠性共同形成壁垒 | 付费交付、验收、可靠性、无接管运行、生产良率 | 合同上限代替收入；项目始终停在演示或试用 |
| 财务及专业流程控制 | Rillet、Ramp、Harvey | 价值进入总账、审批与执行权限，而不只生成文本 | 实际自动执行比例、错误成本、关账/交付人时、续费 | 异常仍靠人海解决，或核心系统把功能低价打包 |
| 医疗与药物发现 | Candid、Abridge、Chai、Isomorphic、Genesis 等 | 医院回款闭环，与实验/临床数据闭环是两种不同路径 | 软件看净回款与交付；药物看前瞻实验、人体证据和药企付款 | 软件无可归属 ROI；平台进步无法转为可开发候选物或临床结果 |

消费与交易平台保留独立观察：Whatnot 的 2025 两次融资提供了非 AI 对照。关键是供给密度、复购、信任和贡献利润，不能用 GMV 代替收入。

## 持续融资：哪些是真正可核对的延续

金额均为美元百万。这里只展示已经核对的节点，不代表公司完整融资史。点击“案例库”可见每个节点的原始链接及说明。

| 公司 | 2025 已核对节点 | 2026 已核对节点 | 要与融资同时验证什么 |
|---|---|---|---|
| Together AI | B 305 | C 800 | 客户生产负载与全成本；容量承诺由谁资本化 |
| Fireworks | C 250，含一级及二级 | D 1,505 | 专用模型需求、实际账单和毛利，不能把全部 C 轮算公司新增现金 |
| Baseten | C 75 → D 150 | E 300 | 同任务性能/成本、客户迁移与交付效率 |
| Supabase | E 100，含员工流动性 | F 500，含员工流动性 | 应用创建能否变成持久、付费的数据库负载 |
| Harvey | D 300 → E 300 | 550 融资 | 专业工作流、客户数据权利、留存与交付人效 |
| Saronic | C 600 | D 1,750 | 造船能力是否转为已验收、可回款交付 |
| Shield AI | F-1 240 | G 1,500，其他融资另列 | 自主软件、仿真与制造共同改善多少交付指标 |
| OpenEvidence | B 210 | D 250 | 医生使用之外的收入、授权和客户留存 |
| Candid Health | C 52.5 | D 120 | 实际净收款改善，扣除人工与实施后经济性 |
| Heidi | B 65 | C 股权 100，另有 240 增长融资 | 临床文书能否进入后续动作和医院合同 |
| Isomorphic Labs | 首轮外部融资 600 | B 2,100 | 平台能否产生可复现候选物及人体证据 |
| Chai | A 70 → B 130 | C 400 | 外部湿实验验证、可开发性及真实合作收入 |
| Pathos | D 365 | E 237 | AI 对资产筛选与试验的独立贡献 |

同年连续融资也有参考价值：Base Power B 200→C 1,000；Rillet A 25→B 70；Whatnot E 265→F 225。Ramp 的 E、E-2 和后续融资应保留系列和扩展标记；不能只按报道次数推算独立轮数。

## 最值得带进会上的一个共同问题

**一家公司的能力进步，究竟会留下什么只能由它拥有的东西？**

- 推理公司：调度、性能与客户任务评估数据，还是可被替换的 GPU 租赁？
- 软件公司：系统记录、执行权限和纠错结果，还是一个可被核心系统打包的界面？
- 电力及机器人：部署网络、运行数据和制造经验，还是昂贵的一次性项目？
- 医疗：能复用的实验/临床反馈与明确数据权利，还是每个客户或每条管线重新开始？

这个问题与长期壁垒有关，但答案必须落到合同、成本、失败记录和后续结果上；“有数据”本身不等于有可使用的数据资产。

## 建议这次讨论产出三项可执行研究任务

1. **药物发现新增 sector：先选商业模式，再选公司。** 分别比较数据/实验工具、AI 发现平台、自持临床资产。可用 Inductive/Tahoe、Chai/Isomorphic、Enveda/Pathos 作第一轮对照。
2. **找一个能直接验证 ROI 的工作流。** 医疗 RCM 用 Candid/Tennr，与财务总账 Rillet 作横向机制比较：付费方、执行权、错误责任、净回款与实施工时。
3. **物理瓶颈按资本责任拆开。** 电力、推理和自主系统逐案写出运营公司、设备/项目资产与客户谁承担资本开支，基金能获得哪部分收益。

每项任务只要求一页判断更新：当前假设、最强支持证据、最强反证、三位客户/行业专家、一个能证伪的指标。先决定是否值得研究，再讨论估值与投资结构。


# 医疗与药物发现：本次独立 sector

**医疗不降权。先把“改善医疗经营效率”和“产生更好的药物资产”分开，它们的验证周期、资本需求和价值归属不同。** 本版选入 31 个医疗相关事件，其中 29 个融资/融资包事件及 2 个药企合作事件。它们是代表案例，不是行业普查。

## 1. 医疗内部的分化，比一个总额更重要

Rock Health 的 2025 美国数字医疗统计为 **$14.2B、482 笔**：金额增长 35%，笔数由 509 降至 482。AI-enabled 公司获得 54% 的资金；剔除当年融资最多的九家公司，总额低于 2024。数字医疗的增长高度集中。[原始年终报告](https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/)。

另一份 SVB 年度报告显示其医疗投资口径下 2025 总额 $46.8B、同比下降 12%，biopharma 与 diagnostics/tools 下滑，而 healthtech 与 devices 增长。它与全球 Crunchbase、美国 Rock Health 的地域和分类不同，不能加总或直接计算份额。[SVB 原始报告新闻稿](https://www.prnewswire.com/news-releases/ai-investment-accounted-for-nearly-half-of-healthcare-investment-in-2025-silicon-valley-bank-releases-17th-healthcare-investments-and-exits-report-302656179.html)。

因此，本次不把医疗作为一个统一“热赛道”：临床软件、实验工具、发现平台、临床药物资产需要分别讨论。

## 2. 药物发现：六个可以独立立项的子方向

| 子方向 | 本次代表公司 | 能形成什么优势 | 下一步最关键的证据 |
|---|---|---|---|
| 小分子、蛋白与抗体设计 | Isomorphic、Chai、Latent、Profluent | 模型、实验和可开发性反馈共同积累 | 前瞻性湿实验下，选择性、稳定性、ADMET及可开发性是否同时改善；失败项目全部计入分母 |
| 扰动数据与虚拟细胞 | Tahoe | 干预数据比单纯观察数据更接近因果问题 | 病人异质性、数据独占与训练权、体外到人体的迁移能力 |
| 自主实验与 ADMET 工具 | Lila、Inductive | 设计—合成—测试循环与实验效率 | 每个可开发候选物的总实验数、周期和成本；扣除科学家、设备及耗材后的经济性 |
| 平台加自持药物管线 | Enveda、Insilico | 专有样本与计算平台转成候选物和临床资产 | 多条管线复现、人体结果、平台贡献与单资产质量能否分离 |
| 临床资产选择与开发 | Pathos | 患者分层、试验设计与资产筛选 | 前瞻性可审计比较；买入优质资产与 AI 增益分别贡献多少 |
| 非 AI 新药、递送及跨境资产 | SpliceBio、Kailera | 解决递送、临床疗效或全球开发的明确瓶颈 | 人体安全与疗效、CMC、全球权益和后续资金需求 |

### 最值得深入的案例：Genesis 与 Incyte

2025 年合作披露 $30M 首付款、初始两个靶点。2026 年扩大合作披露 $120M 预付对价：**$80M 现金 + $40M 股权投资**，至少五个新靶点，并有持续模型训练/推理研究经费。协议明确把药企专有实验数据带入设计—合成—测试循环。[2025 公告](https://investor.incyte.com/news-releases/news-release-details/incyte-and-genesis-therapeutics-announce-strategic-ai-focused) / [2026 公告](https://incytecorp.gcs-web.com/news-releases/news-release-details/incyte-and-genesis-expand-molecular-ai-collaboration-accelerate)。

研究推断：这比单独一笔大额融资更接近商业验证，因为合作方愿意扩大范围、付款并提供数据。还需验证项目结果、后续付款、数据使用权和利润归属。潜在里程碑不是当期现金，也不能全部列成融资。

### 外部实验验证与临床验证要分开

Chai 的 A→B→C 有不同轮次公告，2026 年披露 GSK 在自有湿实验评估后扩大合作，支持外部发现阶段验证。**结合成功、可开发性、临床疗效和监管获批是不同台阶。** 合作条款未公开，不推定收入。[GSK 合作公告](https://www.chaidiscovery.com/news/gsk-partnership)。

Insilico 的 rentosertib 2025 年 Phase 2a 研究涉及 71 名 IPF 患者、12 周观察，主要终点为安全性；探索性疗效信号仍需更大、更长研究。它提供人体证据，但不能证明 AI 药物发现的整体成功率，也不能外推为获批概率。[原始研究](https://pmc.ncbi.nlm.nih.gov/articles/PMC12353801/)。

## 3. 医疗服务与技术：从节时进入实际回款和行动

| 子方向 | 代表公司 | 谁可能付钱、为什么付钱 | 应要求的验证 |
|---|---|---|---|
| 临床文书与医生助手 | Abridge、Ambience、Heidi | 医院或医生，为文书负担、编码完整性及后续工作流付费 | 付费活跃与续费、复核时间、接入成本；是否能安全写回系统并完成行动 |
| 医疗账单、拒付与转诊 | Candid、Tennr | 医疗机构，为净回款、转诊转化和较少人工付费 | 净收款率、拒付与追回、客户回本期；扣除实施和人工支持的毛利 |
| 临床证据检索 | OpenEvidence | 医生使用与商业付款方可能不同 | 内容授权、实际收入、留存；引用质量与入口可替代性 |
| 影像临床 AI | Aidoc | 医院，为处置效率和临床流程付费 | 产品对应许可范围、前瞻临床结果、部署后的工作流变化 |
| 试验执行基础设施 | Lindus | 药企及研发方，为试验周期、质量和执行付费 | 同类试验招募、完组、成本及数据质量；重复购买与项目毛利 |
| 消费者检测与预防健康 | Function | 消费者，为检测、解释与持续健康管理付费 | 续费、后续有效干预、贡献利润；不必要检测与后续支出的风险 |

共同的长期壁垒候选是工作流、付款方规则、异常纠正和可复用数据。医院数据不必然允许训练；监管许可不必然独家；医生使用量也不等于收入或改善结局。

## 4. 先决定用哪种商业模式承担药物风险

| 模式 | 收入/价值来源 | 优点候选 | 主要风险 | 与基金讨论的关系 |
|---|---|---|---|---|
| 数据、实验或研发软件工具 | 订阅、按实验/项目收费 | 验证可能较早、跨项目分散 | 重服务、数据不可复用、CRO式毛利 | 可先研究是否有真正产品化及数据复利 |
| 发现平台加药企合作 | 首付、研究费、里程碑、提成 | 客户付款与外部实验反馈 | 付款不连续、IP与利润分享、客户集中 | 必须逐项拆出真实现金与条件性未来收入 |
| 平台加自持药物 | 授权、出售、上市后产品收益 | 保留单资产上行 | 临床、监管、生产及持续融资风险 | 需要科学/临床能力，不能套纯软件逻辑 |
| 医疗经营软件 | 订阅、使用量、回款/结果相关收费 | 可用经营指标较快验证 | 系统集成、责任、销售与人工成本 | 与已有企业软件研究能力相邻，但需医院客户验证 |

## 5. 这次新增 sector 的第一轮研究建议

优先比较三组：**Inductive / Tahoe（数据与工具）—Chai / Isomorphic（发现平台）—Enveda / Pathos（管线与临床开发）**。每家公司都问同一组问题，才便于判断哪种模式适合团队和基金：

1. 模型或数据到底改变了哪一步决策？与原流程相比，一个可开发候选物的全成本、总时间、失败率如何变化？
2. 数据来自哪里，拥有怎样的训练、留存和跨客户使用权？对方可否把相同数据交给竞争者？
3. 最近一次融资到下一次融资之间，完成了什么外部实验、临床或付款节点？没有完成什么？
4. 药物/IP权益、实验费用、临床费用和最终利润分别归谁？下一阶段还需要多少资本？
5. 如果一个主要项目失败，平台论点是否仍成立？用什么事实能区分单资产失败与平台失效？

中国关联可从具体资产、实验能力与全球开发权出发。Kailera 为中国来源药物进入全球开发的案例；不能仅用研发成本较低就推断投资回报。需要逐项核查临床差异化、权利、生产和开发能力。


# 数据口径与尚未完成的覆盖

## 当前可以与不能声称的内容

| 材料 | 覆盖 | 可以用于什么 | 不能用于什么 |
|---|---|---|---|
| 2025 原始年度市场报告 | 全年、各报告自有地域与分类 | 描述全年资金结构与集中度 | 与不同来源标签直接加总或拼接同比 |
| 2025 Gmail Pro Rata | 仅检得 12/1–12/23 的 17 期正式刊物；另 1 封欢迎邮件 | 确认邮箱来源边界 | 声称已读 2025 全年、已完成全年逐笔回填 |
| Axios 官方历史页面 | 已验证 2025/1/7 完整刊物可读；URL 枚举未建立全年清单 | 提供补齐历史的可行来源 | 从单个可读页面推断全年覆盖完整 |
| 2026 现有仓库 | 时间跨度 1/5–10/23；W20–W43 有 24 份连续周报 | 找公司/方向的跨期线索 | 视为全市场普查；把历史合并文件当逐期覆盖已审计 |
| 本次精选事件库 | 63 个融资及合作事件，逐条有原始链接 | 研究假设、公司对照与融资序列 | 年度交易量、市场份额或行业同比 |

2026 仓库按既有“日期＋规范化公司名＋市场类型”同日去重，含历史回溯与周更重叠后为 **7,832 条记录，其中一级融资记录 3,420 条**。这不是独立融资轮数：跨日重复报道、同轮扩募、拟融资和进展新闻仍需事件级复核。历史合并文件未保留逐期 issues 清单，不能由该文件单独证明 1–5 月每天无缺刊。

2025 Gmail 已交叉搜索：Dan 发件人、Axios 全域、所有发件人与转发关键词，以及 in:anywhere（含垃圾箱/垃圾邮件）；各搜索分页均结束，没有找到 1–11 月刊物。欢迎邮件日期是 2025/12/1。授权可用，阻塞点是历史来源覆盖，不是 Gmail 连接失败。

## 本版清洗规则

- 全部金额为美元百万；公告未披露的字段保留空缺，不估算年度融资总额。
- 普通股权、债务/授信、二级交易、增长融资、合作首付与或有里程碑分别显示。
- 同一轮分批关闭保留关系，不把每篇新闻算成新轮；公司跨期再融资也不能仅靠日期判断。
- 经营数字为公司公告口径，除明确标注的外部研究外，没有替代客户账单、合同或独立实验核查。
- 数据库精选有大单、知名公司和英文公开披露偏差；没有入选不等于该方向没有融资。
- 医疗本次不降权；此 override 只适用于本次基金讨论，不改写常规周报偏好。

## 会改变判断的具体金额修正

| 事件 | 正确处理 |
|---|---|
| Lila 2025/9 $235M 与 10月 $350M | 同一 A 轮分批关闭，本版仅保留最终 $350M |
| Latent 标题 $50M | 累计资金；本次 A 轮为 $40M |
| Insilico 2025 $110M→$123M | 同一 E 轮扩展；最终关闭原始页面本次受阻，初次关闭明确标注，不参与年度总额 |
| Fireworks 2025 C、Supabase E/F | 明确有二级/员工流动性，未公开拆分，不全部归为新增公司股权现金 |
| Aidoc $150M | 包含 $40M 循环信贷，整体显示混合融资包 |
| Heidi 2026 $340M | $100M 股权 + $240M CVF 增长融资，不是 $340M 普通股权 |
| Shield AI 2026 | $1.5B G轮、$500M 固定回报优先股、$250M 额外延迟提款承诺分列 |
| Figure 2025 >$1B | 承诺资本下界，不能写全部到账 |
| Genesis–Incyte 2026 $120M | $80M 现金 + $40M 股权；条件性里程碑不算当期现金 |
| Ramp E-2 / CFS B2 | 保留系列延伸关系，不机械计为全新独立轮次 |

## 2025 全量回填的剩余工作

完整的 2025 逐笔统计需要先建立官方全年刊期/原文清单，逐期核验无刊与缺失，再按同一规则抽取并进行事件去重。现有邮箱不足以完成这一项；已查到官方单期历史内容，但尚未取得全年可验证清单。本次没有向 data/ 写入一个伪装为全年全量的 2025 年度文件，也没有据不完整样本绘制跨年增长率。

作为讨论材料，本版可以用于挑选研究方向；作为两年全量融资数据库，它仍有上述缺口。获得可验证的全年归档或授权导出后，应继续补齐，再更新相同来源、相同月份、相同地域与分类的比较。

## 来源入口

- [2025 Crunchbase 全球年度复盘](https://news.crunchbase.com/venture/funding-data-third-largest-year-2025/)
- [2025 Rock Health 美国数字医疗复盘](https://rockhealth.com/insights/2025-year-end-digital-health-funding-overview-a-tale-of-two-markets/)
- [SVB 医疗年度报告新闻稿](https://www.prnewswire.com/news-releases/ai-investment-accounted-for-nearly-half-of-healthcare-investment-in-2025-silicon-valley-bank-releases-17th-healthcare-investments-and-exits-report-302656179.html)
- [2025 fintech 年度复盘](https://news.crunchbase.com/fintech/funding-jumped-big-checks-ai-ye-2025/)
- [Axios 2025/1/7 官方历史刊物](https://www.axios.com/newsletters/axios-pro-rata-781537fe-1d87-45fe-8fad-691ca89a0143)
- [现有 Startup Tracking 数据](https://github.com/EstLLLLL/Startup-Tracking/tree/main/data)

NVCA 官方 Yearbook 网页的 AI 金额与总额/占比存在内部不一致，本版没有使用其 AI 美元金额推导。宏观报告来自不同数据商，不强行统一为一个总额。


## 精选事件明细：AI基础设施

| 日期 | 公司 | 方向 | 金额/性质 | 阶段 | 原始来源与证据 | 下一验证 |
|---|---|---|---|---|---|---|
| 2025-02-19 | Baseten | 生产级模型推理 | $75M / 股权/投资 | Series C | [原文](https://www.baseten.co/blog/announcing-baseten-75m-series-c/) 公司宣布7500万美元C轮，IVP和Spark共同领投，支持混合与自托管部署。 | 生产质量、弹性调度和观测是客户愿意付费的假设；需同任务全成本测试。 |
| 2025-02-20 | Together AI | 开源与定制模型云 | $305M / 股权/投资 | Series B | [原文](https://www.together.ai/blog/together-ai-announcing-305m-series-b) 公司宣布3.05亿美元B轮，General Catalyst领投、Prosperity7共同领投。 | 推理、训练和集群服务结合；验证软件效率与硬件租赁分别的毛利和资本需求。 |
| 2025-09-05 | Baseten | 生产级模型推理 | $150M / 股权/投资 | Series D | [原文](https://www.baseten.co/blog/announcing-baseten-150m-series-d/) 公司宣布1.5亿美元D轮，BOND领投。 | 明确不同轮次；比较性能优势是否可持续、客户能否迁移、负载规模是否提高毛利。 |
| 2025-09-30 | Cerebras | 专用芯片与推理系统 | $1100M / 股权/投资 | Series G | [原文](https://www.cerebras.ai/press-release/series-g) 公司宣布11亿美元G轮、81亿美元投后估值，Fidelity与Atreides领投。 | 从芯片进入系统和云推理，需验证端到端成本、利用率与客户集中。 |
| 2025-10-03 | Supabase | 应用数据库与后端 | $100M / 混合融资包 | Series E | [原文](https://supabase.com/blog/series-e) 公司宣布1亿美元E轮，50亿美元投前估值；明确包含员工流动性用途，未分拆一级与二级。 | 代码生成增长可能传导到数据库，但数据库创建数必须进一步转化为活跃及付费负载。 |
| 2025-10-28 | Fireworks AI | 推理与专用模型生命周期 | $250M / 混合融资包 | Series C | [原文](https://fireworks.ai/blog/series-c) 2.5亿美元C轮明确同时包含一级与二级，未披露拆分；公司自报年化收入超过2.8亿美元。 | 比较生产推理与定制模型需求，不能将整笔融资当新增公司现金或将run-rate等同全年收入。 |
| 2026-01-23 | Baseten | 生产级模型推理 | $300M / 股权/投资 | Series E | [原文](https://www.baseten.co/blog/announcing-baseten-s-300m-series-e/) 公司原始发布日期1月23日、更新日2月5日；3亿美元E轮，50亿美元估值。 | 第三轮12个月内融资不是同一新闻更新；公司自述推理量增长不能当作同幅度收入增长。 |
| 2026-02-03 | Cerebras | 专用芯片与推理系统 | $1000M / 股权/投资 | Series H | [原文](https://cerebras.gcs-web.com/news-releases/news-release-details/cerebras-systems-raises-1-billion-series-h) 公告正文2月3日、网页2月4日，10亿美元H轮，约230亿美元估值。 | 融资与客户合同/收入分开；验证需求是否集中在少数大型合同及资本支出承诺。 |
| 2026-06-04 | Supabase | 应用数据库与后端 | $500M / 混合融资包 | Series F | [原文](https://supabase.com/blog/series-f) 公司宣布5亿美元F轮、100亿美元投前估值，包含员工流动性；称60%以上新数据库由AI工具发起。 | 关注生成应用存活率、付费数据库留存、基础设施成本和可靠性，不能用开发者数代替收入。 |
| 2026-07-01 | Together AI | 开源与定制模型云 | $800M / 股权/投资 | Series C | [原文](https://www.together.ai/blog/announcing-our-series-c) 公司宣布8亿美元C轮；500MW以上算力容量承诺将由新投资人独立资本化。 | 股权融资与算力项目融资分开；验证客户负载增长及风险由运营公司还是资产方承担。 |
| 2026-07-15 | Fireworks AI | 推理与专用模型生命周期 | $1505M / 股权/投资 | Series D | [原文](https://fireworks.ai/blog/fireworks-series-d-funding) 公司宣布15.05亿美元D轮，175亿美元估值；自报年化收入run-rate超过10亿美元、95%以上token来自专用模型。 | 需求证据从通用API转向专有数据训练与运行；需要账单、毛利、集中度和客户留存复核。 |


## 精选事件明细：企业与金融软件

| 日期 | 公司 | 方向 | 金额/性质 | 阶段 | 原始来源与证据 | 下一验证 |
|---|---|---|---|---|---|---|
| 2025-02-12 | Harvey | 法律专业工作流 | $300M / 股权/投资 | Series D | [原文](https://www.harvey.ai/blog/harvey-raises-series-d) 公司公告3亿美元D轮，Sequoia领投；2024客户由40增至235家（公司口径）。 | 专业知识、文档权限、评估与执行流程能否形成持续优势。 |
| 2025-05-28 | Rillet | AI-native ERP / accounting general ledger | $25M / 股权/投资 | Series A | [原文](https://www.prnewswire.com/news-releases/rillet-raises-25m-series-a-from-sequoia-capital-to-bring-ai-to-mid-market-accounting-302467399.html) 公司宣布Sequoia领投2500万美元A轮；重建总账并连接Stripe、Ramp等，自动处理应计、对账和报告。 | 机会在系统记录、记账规则和异常处理闭环，需检验实施工时及责任是否妨碍可扩展性。 |
| 2025-06-17 | Ramp | spend management / finance workflows | $200M / 股权/投资 | Series E | [原文](https://www.lw.com/en/news/2025/06/latham-watkins-advises-ramp-in-us200-million-series-e-financing) 交易律师确认Ramp E轮融资上限2亿美元、估值160亿美元，由Founders Fund领投；律师公告6月18日，融资对外公布6月17日。 | 后续7月E-2和11月融资不可误认为此轮的重复报道。 |
| 2025-06-23 | Harvey | 法律专业工作流 | $300M / 股权/投资 | Series E | [原文](https://www.harvey.ai/blog/harvey-raises-series-e) 公司公告3亿美元E轮、50亿美元估值，Kleiner Perkins和Coatue领投。 | 与2月D轮是不同轮次；需检验扩张后的留存、交付人效和净收入。 |
| 2025-06-23 | Spinwheel | consumer credit data / embedded payments | $30M / 股权/投资 | Series A | [原文](https://spinwheel.io/blog/spinwheel-raises-30-million-series-a-to-transform-the-consumer-credit-ecosystem-with-real-time-data-and-agentic-ai) 公司宣布F-Prime领投3000万美元A轮，提供实时负债数据和还款执行接口。 | agent价值依赖真实账户连接、授权及支付执行，而不只依赖对话；需看授权成功率、数据新鲜度和坏账责任。 |
| 2025-07-30 | Ramp | spend management / autonomous finance | $500M / 股权/投资 | Series E-2 | [原文](https://www.prnewswire.com/news-releases/ramp-raises-500-million-at-22-5-billion-valuation-to-accelerate-ai-and-build-the-future-of-finance-302516953.html) 公司宣布ICONIQ领投5亿美元E-2，估值225亿美元；披露服务超过4万家公司、年化卡交易和账单支付量超过800亿美元。 | 财务agent附着在支付权限、交易数据与审批政策上；交易量不能替代收入，自动化准确率需客户独立核验。 E-2按同系列延伸显示；不把轮名不同自动视为独立轮次。 |
| 2025-08-06 | Rillet | AI-native ERP / accounting general ledger | $70M / 股权/投资 | Series B | [原文](https://www.rillet.com/blog/rillet-raises-70m-series-b-from-andreessen-horowitz-and-iconiq) 公司宣布a16z与ICONIQ共同领投7000万美元B轮，距A轮约10周；自报超过200家客户与12周ARR翻倍。 | 与5月A轮为独立轮次；可检验续费、纠错率、账务审计和客户迁移成本。 |
| 2025-11-17 | Ramp | spend management / autonomous finance | $300M / 股权/投资 | Primary financing + employee tender | [原文](https://www.prnewswire.com/news-releases/ramp-reaches-32-billion-valuation-doubling-revenue-and-customers-in-past-year-302616510.html) 公司披露3亿美元一级融资并同时进行员工要约；一级融资和员工二级出售分别记录，后者金额未披露。 | 一年内多次再融资伴随公司自报收入增长，不能把估值升幅当成客户经济性已被证明。 |
| 2026-09-09 | Harvey | 法律专业工作流 | $550M / 股权/投资 | Financing | [原文](https://www.harvey.ai/blog/harvey-raises-dollar550m-at-a-dollar155b-valuation-to-help-legal-teams-own-their-intelligence) 公司宣布5.5亿美元融资、155亿美元估值，Diffusion与Lightspeed共同领投。 | 跨年资本延续存在；研究律师与企业自有数据、模型和执行系统的利益分配。 |


## 精选事件明细：医疗与药物发现

| 日期 | 公司 | 方向 | 金额/性质 | 阶段 | 原始来源与证据 | 下一验证 |
|---|---|---|---|---|---|---|
| 2025-02-13 | Latent Labs | 生成式蛋白设计 | $40M / 股权/投资 | Series A | [原文](https://sofinnovapartners.com/news/latent-labs-secures-usd50m-funding-realize-potential-ai-powered) 投资方公告累计融资5000万美元，其中本轮A轮4000万美元；Radical与Sofinnova共同领投。 | 媒体标题5000万美元为累计融资，不能全部计入2025A轮；实验验证和平台交付能力是关键。 |
| 2025-02-20 | Genesis Therapeutics / Incyte | AI小分子药企合作 | $30M / 合作对价 | Research collaboration | [原文](https://investor.incyte.com/news-releases/news-release-details/incyte-and-genesis-therapeutics-announce-strategic-ai-focused) Incyte披露首付款3000万美元、初始两个靶点，另有按靶点至多2.95亿美元里程碑及分层销售提成。 | 这是业务合同首付款，不是股权融资；研发、监管、销售里程碑是有条件未来收入。 |
| 2025-03-13 | Insilico Medicine | AI小分子与自持管线 | $110M / 股权/投资 | Series E initial close | [原文](https://www.prnewswire.com/news-releases/insilico-medicine-secures-110-million-series-e-financing-to-advance-ai-driven-drug-discovery-innovation-302401040.html) 公司公告1.1亿美元E轮，Value Partners旗下基金领投，资金同时用于AI、自动化实验和临床验证。 | 这是初次关闭金额；6月同轮扩至1.23亿美元的报道不能再加一轮。用人体数据而非平台速度比较来检验药物价值。 |
| 2025-03-31 | Isomorphic Labs | AI药物设计平台 | $600M / 股权/投资 | 首轮外部融资 | [原文](https://www.isomorphiclabs.com/articles/isomorphic-labs-announces-600m-external-investment-round) 公司公告首轮外部融资6亿美元，Thrive领投、GV和Alphabet参与。 | 平台资本投入很大；资金用途包括模型和临床管线，融资本身不能证明临床成功。 |
| 2025-05-07 | Inductive Bio | ADMET优化与研发工具 | $25M / 股权/投资 | Series A | [原文](https://www.inductive.bio/news/inductive-bio-raises-25m-series-a) 正文宣布5月7日2500万美元A轮（页面标注5月8日），Obvious领投；多药企匿名数据联盟支持ADMET预测。 | 切入窄瓶颈而非端到端制药；验证前瞻性ADMET效果、跨客户数据权利、付费留存和实验闭环。 |
| 2025-05-15 | Pathos AI | 临床资产筛选与开发 | $365M / 股权/投资 | Series D | [原文](https://www.pathos.com/pathos-ai-secures-365-million-in-series-d-financing-to-advance-oncology-drug-development-through-ai) 公司公布3.65亿美元D轮、约16亿美元投后估值，资金支持临床管线与肿瘤多模态模型。 | 模型用于资产选择和试验设计，自持临床资产决定资本强度；不能按纯软件公司理解。 |
| 2025-06-11 | SpliceBio | 基因递送/大基因治疗 | $135M / 股权/投资 | Series B | [原文](https://splice.bio/splicebio-secures-135-million-series-b-financing-to-advance-lead-program-sb-007-in-stargardt-disease-and-expand-pipeline-of-genetic-medicines/) 公司宣布1.35亿美元B轮，EQT Life Sciences和Sanofi Ventures共同领投，用于SB-007 Phase1/2及其他基因疗法。 | 非AI医疗项目对照：解决AAV载量限制这类明确工程瓶颈；验证人体表达、安全性、眼科终点与生产可扩展性。 |
| 2025-08-06 | Chai Discovery | 生成式抗体设计 | $70M / 股权/投资 | Series A | [原文](https://www.businesswire.com/news/home/20250806670137/en/Chai-Discovery-Announces-%2470-million-Series-A-To-Transform-Molecular-Design) 公司发布7000万美元A轮，Menlo领投；资金用于平台开发和合作伙伴接入。 | 近20%命中率属于公司实验数据，需独立湿实验、多目标和可开发性验证，不能等同临床成功率。 |
| 2025-08-11 | Tahoe Therapeutics | 单细胞扰动数据/虚拟细胞 | $30M / 股权/投资 | Series A | [原文](https://www.tahoelabs.ai/news/we-have-raised-30m) 公司宣布3000万美元融资，计划构建十亿单细胞数据点、百万药物—患者交互数据，并选择一个合作伙伴。 | 专有干预数据可能比公开观察数据更稀缺；目标数据规模是计划，不能当作已完成数据集。 |
| 2025-09-04 | Enveda | 天然产物计算发现与临床管线 | $150M / 股权/投资 | Series D | [原文](https://enveda.com/news/enveda-raises-150m-series-d-funding-to-reach-unicorn-status-enrolls-first-patient-in-lead-program-and-adds-mikael-dolsten-to-board-of-directors/) 公司宣布1.5亿美元D轮，同时ENV-294在特应性皮炎Phase1b中首例给药。 | 专有化学样本、代谢组学、自动实验连接到临床；同年C轮1.5亿美元最终关闭包含2024融资，不应把全额都计入2025新增。 |
| 2025-10-10 | Lila Sciences | 自主实验与科学模型 | $350M / 股权/投资 | Series A final close | [原文](https://www.lila.ai/news/announcing-the-close-of-our-series-a) 公司披露A轮最终关闭3.5亿美元、累计融资5.5亿美元；A轮分两部分关闭。 | 9月2.35亿美元与10月3.5亿美元属于同轮不同关闭，必须合并；跨生命科学和材料，不应把全额算成药物发现投资。 |
| 2025-10-14 | Kailera Therapeutics | 肥胖药物/跨境资产开发 | $600M / 股权/投资 | Series B | [原文](https://investors.kailera.com/news-releases/news-release-details/kailera-therapeutics-announces-600-million-series-b-financing) 公司公告6亿美元B轮，Bain Capital PE领投，支持KAI-9531全球Phase3等项目。 | 资本下注晚期临床与全球开发能力；中国HRS9531资产是中国研发向全球开发转化的具体案例，非AI平台案例。 |
| 2025-11-19 | Profluent | 蛋白设计与基因编辑 | $106M / 股权/投资 | Financing (series not stated) | [原文](https://www.businesswire.com/news/home/20251119356889/en/Profluent-Raises-%24106M-to-Scale-Frontier-AI-Models-for-Programmable-Biology) 公司发布1.06亿美元融资，Altimeter与Bezos Expeditions共同领投，累计1.5亿美元。 | 官方未标轮次，保留未披露；模型输出应检验功能蛋白和编辑效果，业务还涵盖农业与工业，不能全额归为治疗药物。 |
| 2025-12-15 | Chai Discovery | 生成式抗体设计 | $130M / 股权/投资 | Series B | [原文](https://www.businesswire.com/news/home/20251214931432/en/Chai-Discovery-Announces-%24130-Million-Series-B-To-Transform-Molecular-Discovery) 公司发布1.3亿美元B轮，Oak HC/FT、General Catalyst共同领投。 | 距A轮约4个月，属于新轮次而非同笔新闻重发；商业化扩张仍需付款与续约证据。 |
| 2026-05-12 | Isomorphic Labs | AI药物设计平台 | $2100M / 股权/投资 | Series B | [原文](https://www.isomorphiclabs.com/articles/isomorphic-labs-announces-series-b-investment-round) 公司公告21亿美元B轮，Thrive继续领投，MGX、Temasek、CapitalG等加入。 | 与2025年为真正不同轮次；下一验证是进入临床及可复现的人体结果，而非估值或融资加速。 |
| 2026-05-20 | Genesis Molecular AI / Incyte | 药企实验数据与AI发现闭环 | $120M / 合作对价 | Expanded research collaboration | [原文](https://incytecorp.gcs-web.com/news-releases/news-release-details/incyte-and-genesis-expand-molecular-ai-collaboration-accelerate) Incyte披露1.2亿美元预付对价，含8000万美元现金与4000万美元股权投资，新增至少5靶点，并提供持续模型训练/推理研究经费。 | 把专有药企实验数据用于训练与设计—合成—测试循环；现金、股权和或有里程碑必须分列。 |
| 2026-07-14 | Chai Discovery | 生成式抗体设计 | $400M / 股权/投资 | Series C | [原文](https://www.chaidiscovery.com/news/series-c) 公司发布4亿美元融资、38亿美元估值，参与方包括Index、Kleiner Perkins、Sequoia、Dimension。 | 2025两轮后2026继续融资；同期药企采用是比单纯再融资更强的需求线索，但合作金额和产品转化率尚未公开。 |
| 2026-10-23 | Pathos AI | 临床资产筛选与开发 | $237M / 股权/投资 | Series E | [原文](https://www.pathos.com/pathos-ai-secures-237-million-in-series-e-financing-to-scale-agentic-ai-drug-development-platform-and-advance-oncology-pipeline) 公司公布2.37亿美元E轮、约30亿美元估值，由BMS领投；推进肿瘤临床资产及注册研究。 | 2025→2026新轮次伴随药企战略参与；检验AI是否提高前瞻性资产筛选/试验成功率，避免资产本身驱动却归功于AI。 |


## 精选事件明细：医疗服务与技术

| 日期 | 公司 | 方向 | 金额/性质 | 阶段 | 原始来源与证据 | 下一验证 |
|---|---|---|---|---|---|---|
| 2025-01-22 | Lindus Health | 临床试验执行与基础设施 | $55M / 股权/投资 | Series B | [原文](https://www.goodwinlaw.com/en/news-and-events/news/2025/01/announcements-otherindustries-lindus-health-series-b-round) 交易律师在1月24日公告确认5500万美元B轮，Balderton领投；提供整合式临床试验服务和自研试验管理技术。公开交易报道日期为1月22日。 | 这是缩短试验执行周期的服务加软件模式，不是药物资产；要核对招募速度、完组率、数据质量和项目毛利。 |
| 2025-02-12 | Candid Health | 医疗账单与RCM | $52.5M / 股权/投资 | Series C | [原文](https://www.newswire.com/news/candid-health-raises-52-5-million-series-c-to-enhance-genai-features-22518346) 公司宣布5250万美元C轮，由Oak HC/FT领投；称平台使更多账单首次提交即正确处理，服务超过200家医疗组织。 | 可检验闭环是提交—拒付原因—修正—实际回款；与减少医生文书负担相比，ROI更接近财务账单。 |
| 2025-02-17 | Abridge | 临床文书与收入周期 | $250M / 股权/投资 | Series D | [原文](https://www.abridge.com/press-release/series-d) 公司宣布2.5亿美元D轮，由Elad Gil与IVP领投；当时称已部署超过100家医疗系统。 | 从临床记录切入可计费文书，下一步需验证节时能否转化为实际回款、续约和较低实施成本。 |
| 2025-06-18 | Tennr | 转诊与患者接入 | $101M / 股权/投资 | Series C | [原文](https://www.prnewswire.com/news-releases/healthcare-referrals-are-where-patients-get-lost-tennr-raises-101m-to-bring-the-visibility-our-system-desperately-needs-302485255.html) 公司宣布1.01亿美元C轮，由IVP领投；把传真、邮件及门户中的转诊资料转为可跟踪工作流，连接转诊方、接诊方与患者。 | 增量价值可通过患者转化率、拒付、等待时间、每例人工工作量核验；长期壁垒候选是机构间协同和付款方规则闭环。 |
| 2025-06-23 | Abridge | 临床文书与收入周期 | $300M / 股权/投资 | Series E | [原文](https://www.abridge.com/blog/series-e) 公司页面标注6月23日，标题宣布3亿美元E轮，a16z领投、Khosla参与；称合作企业医疗系统超过150家。 | 与2月D轮是不同轮次；快速补资与部署增加同时发生，但不能据此推定临床结局改善或公司已盈利。 |
| 2025-07-15 | OpenEvidence | 临床证据检索 | $210M / 股权/投资 | Series B | [原文](https://www.prnewswire.com/news-releases/openevidence-the-fastest-growing-application-for-physicians-in-history-announces-210-million-round-at-3-5-billion-valuation-302505806.html) 公司新闻稿宣布2.1亿美元B轮，估值35亿美元，GV和Kleiner Perkins领投。 | 研究重点是授权医学内容、医生使用频率和收入模式；检索工具的流量与医院预算是两种不同商业逻辑。 |
| 2025-07-23 | Aidoc | 临床影像AI与部署平台 | $150M / 混合融资包 | Financing package | [原文](https://www.prnewswire.com/news-releases/aidoc-secures-150m-for-care-its-healthcare-foundation-model-to--transform-clinical-decision-making-for-100-million-patients-302511929.html) 公司宣布1.5亿美元融资包，明确其中包括4000万美元循环信贷额度；General Catalyst与Square Peg领投。公告称两款CARE相关方案获得FDA许可。 | 监管许可、真实院内工作流和跨院数据是验证项；许可不能替代前瞻临床获益证据。 |
| 2025-07-29 | Ambience Healthcare | 临床文书、编码及CDI | $243M / 股权/投资 | Series C | [原文](https://www.ambiencehealthcare.com/blog/ambience-healthcare-announces-243-million-series-c-to-scale-its-ai-platform-for-health-systems) 公司宣布2.43亿美元C轮，Oak HC/FT和a16z共同领投，用于医疗系统的文书、编码及临床文书完整性平台。 | 竞争点是接入EHR并覆盖不同专科和院内场景，而非单纯语音转写。 |
| 2025-10-06 | Heidi Health | 医生助手与临床文书 | $65M / 股权/投资 | Series B | [原文](https://p72.vc/perspectives/our-investment-in-heidi-health/) Point72在10月6日投资说明中确认领投6500万美元B轮；将准确文书视为协调与RCM自动化入口。 | 与美国医院整单销售相比，可观察多地区、不同语言的低门槛采用能否转为企业合同及专科工作流。 |
| 2025-11-19 | Function Health | 消费者检测与预防健康 | $298M / 股权/投资 | Series B | [原文](https://www.functionhealth.com/article/function-announcement) 公司正文日期为11月19日，宣布2.98亿美元B轮、25亿美元估值；把实验室检测会员服务与影像服务结合。 | 付费方偏消费者，和医院软件不同；要检验续费、检测后有效干预及不必要后续支出，而非仅看累计检测数量。 |
| 2026-01-21 | OpenEvidence | 临床证据检索 | $250M / 股权/投资 | Series D | [原文](https://www.businesswire.com/news/home/20260121029132/en/OpenEvidence-Raises-$250-Million-to-Build-Medical-Superintelligence-for-Doctors) 公司新闻稿宣布2.5亿美元D轮、120亿美元估值，Thrive与DST领投；称上一年12月支持约1800万次临床咨询。 | 与2025年B轮有真实跨年融资延续；使用量为公司口径，不等同诊疗结局或付费收入。 |
| 2026-07-22 | Candid Health | 医疗账单与RCM | $120M / 股权/投资 | Series D | [原文](https://candidhealth.com/blog/series-d-ceo) 公司公告及投资方公告宣布1.2亿美元D轮，Sixth Street Growth领投；与2025年C轮相互独立。 | 跨年重复融资支持RCM持续受关注的命题，仍需核对按实际回款计价、净收款改善、客户留存与实施成本。 |
| 2026-09-22 | Heidi Health | 医生助手与临床工作流 | $100M / 股权/投资 | Series C | [原文](https://www.heidihealth.com/en-sg/blog/heidi-secures-us340m-to-scale-agents-across-health-systems-globally) 融资包合计3.4亿美元，其中Blackbird领投的C轮股权为1亿美元，另2.4亿美元来自General Catalyst CVF增长融资；不能全计为股权融资。 | 从文书扩展到预就诊整理与随访行动；需验证自动行动的权限、人工复核、错误责任和节约时间后的付费能力。 |


## 精选事件明细：国防与自主系统

| 日期 | 公司 | 方向 | 金额/性质 | 阶段 | 原始来源与证据 | 下一验证 |
|---|---|---|---|---|---|---|
| 2025-02-18 | Saronic | autonomous ships / shipbuilding | $600M / 股权/投资 | Series C | [原文](https://www.prnewswire.com/news-releases/saronic-raises-600m-series-c-to-take-on-autonomous-shipbuilding-302379441.html) 公司宣布完成Elad Gil领投6亿美元C轮，估值40亿美元，资金支持Port Alpha造船能力。 | 资本从无人艇原型进入船厂与中大型平台；关注交付、量产成本、验收与后续采购，而非只看估值。 |
| 2025-03-06 | Shield AI | autonomy software / aircraft | $240M / 股权/投资 | F-1 | [原文](https://shield.ai/shield-ai-raises-240m-at-5-3b-valuation-to-scale-hivemind-enterprise-an-ai-powered-autonomy-developer-platform/) 公司宣布完成2.4亿美元F-1战略融资，Hivemind Enterprise面向OEM、政府及其他自主系统开发方。 | 可研究不依赖单一机型的自主软件层，但部署、测试、安全与认证成本可能使其难以获得纯软件利润率。 |
| 2026-03-26 | Shield AI | autonomy software / simulation / aircraft | $1500M / 股权/投资 | Series G | [原文](https://shield.ai/shield-ai-to-acquire-software-simulation-company-aechelon-and-raise-2b-at-12-7b-valuation/) 3月公告15亿美元G轮另加5亿美元固定回报优先股；6月22日官方确认20亿美元融资组合已完成及Aechelon并购交割。额外2.5亿美元延迟提款承诺不计入已融资额。 | 真实反馈与仿真形成训练循环；同时暴露融资结构变化，不能把普通股、固定回报优先股和未提款额度简单加为VC股权。 |
| 2026-03-31 | Saronic | autonomous ships / shipbuilding | $1750M / 股权/投资 | Series D | [原文](https://www.prnewswire.com/news-releases/saronic-closes-1-75b-series-d-at-9-25b-valuation-to-accelerate-a-new-era-of-maritime-autonomy-302729298.html) 公司宣布完成Kleiner Perkins领投17.5亿美元D轮，估值92.5亿美元，继续扩张自主船舶产能。 | 与2025年C轮组成跨年连续融资证据；仍需分开订单、合同上限与可确认收入。 |


## 精选事件明细：机器人与制造

| 日期 | 公司 | 方向 | 金额/性质 | 阶段 | 原始来源与证据 | 下一验证 |
|---|---|---|---|---|---|---|
| 2025-09-16 | Figure | humanoid robots / embodied models / manufacturing | >$1000M / 股权/投资，承诺资本 | Series C | [原文](https://www.figure.ai/news/series-c) 公司称C轮承诺资本超过10亿美元、投后390亿美元；用于Helix、BotQ制造、算力和真实世界数据采集。 | 关注数据获取与部署是否形成自增强循环；承诺资本不等于全部现金到账，量产计划不等于规模收入。 |


## 精选事件明细：消费与交易平台

| 日期 | 公司 | 方向 | 金额/性质 | 阶段 | 原始来源与证据 | 下一验证 |
|---|---|---|---|---|---|---|
| 2025-01-08 | Whatnot | live commerce / collectible communities | $265M / 股权/投资 | Series E | [原文](https://www.greycroft.com/perspectives/reimagining-commerce-leading-whatnots-series-e/) 领投方Greycroft确认与DST、Avra共同领投2.65亿美元E轮；披露公司2024年GMV超过30亿美元。 | 非AI消费者赛道仍有强融资案例；护城河需从卖家供给、买家复购、信任及履约中验证。 |
| 2025-10-28 | Whatnot | live commerce / collectible communities | $225M / 股权/投资 | Series F | [原文](https://blog.teamwhatnot.com/unitedstates/growingtogether) 公司宣布2.25亿美元F轮，称当年直播销售额已超过60亿美元，投入买家增长、信任安全和国际扩张。 | 与1月E轮为不同轮次；GMV翻倍并不保证贡献利润提升，应核对补贴、退货、欺诈和商家集中度。 |


## 精选事件明细：电力与能源

| 日期 | 公司 | 方向 | 金额/性质 | 阶段 | 原始来源与证据 | 下一验证 |
|---|---|---|---|---|---|---|
| 2025-04-09 | Base Power | distributed batteries / retail electricity / virtual power plant | $200M / 股权/投资 | Series B | [原文](https://www.businesswire.com/news/home/20250409624698/en/Base-Power-Raises-$200M-Series-B-to-Reinforce-the-Texas-Power-Grid-Accelerate-National-Expansion-and-Build-American-Manufacturing-Capabilities) 公司宣布完成200百万美元B轮；投资用于首座工厂、家庭电池部署、公用事业与房屋开发商合作。 | 同时掌握设备、安装、售电和调度，需核实每户安装成本与电网收益是否覆盖资本成本。 |
| 2025-08-28 | Commonwealth Fusion Systems | fusion power | $863M / 股权/投资 | Series B2 | [原文](https://www.cfs.energy/news-and-media/commonwealth-fusion-systems-raises-863-million-series-b2-round-to-accelerate-the-commercialization-of-fusion-energy/) 公司宣布8.63亿美元B2轮，用于完成SPARC示范装置及ARC电站前期开发。 | 深科技巨轮可持续吸金但基金期限、技术里程碑和后续资本需求必须匹配，不能等同于近期电力收入。 |
| 2025-10-08 | Base Power | distributed batteries / retail electricity / virtual power plant | $1000M / 股权/投资 | Series C | [原文](https://www.businesswire.com/news/home/20251008106005/en/Base-Power-Raises-$1-Billion-Series-C-to-Build-the-Future-of-American-Power) 公司宣布Addition领投10亿美元C轮；披露部署超过100MWh住宅电池，并获准参与得州ADER聚合资源计划。 | 与4月B轮为不同轮次，显示规模部署融资持续；容量部署与许可不等于资产回报已经验证。 |
| 2025-11-17 | Gridware | distribution-grid monitoring / physical sensors | $55M / 股权/投资 | Series B | [原文](https://www.gridware.io/news/gridware-raises-55-million-growth-round-to-accelerate-u-s-deployments-and-support-global-expansion) 公司披露Tiger Global与Generation共同领投5500万美元；杆上设备监测机械、电气和环境信号，已部署数万根电杆。 | 从电力新增供给转到现有电网可观测性；验证每设备成本、故障误报率、减少停电损失及公用事业回款周期。 |
| 2025-12-10 | Fervo Energy | enhanced geothermal / firm clean power | $462M / 股权/投资 | Series E | [原文](https://fervoenergy.com/fervo-energy-raises-462-million-series-e-to-accelerate-geothermal-development-and-meet-surging-energy-demand-with-clean-firm-power/) 公司宣布完成B Capital领投4.62亿美元E轮，支持Cape Station及其他地热项目。 | 研究可复制的钻井降本与长期购电需求；区分公司股权投资回报和单个项目的杠杆后回报。 |
