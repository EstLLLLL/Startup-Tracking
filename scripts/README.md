# 月度/周度市场复盘流程

把 Axios Pro Rata 邮件变成结构化数据 + 复盘报告的可复用流程。分两半：
**抽取**（需要 LLM/agent，因为要解析邮件 HTML）和 **分析**（纯脚本，确定性可复现）。

## 1. 抽取（Codex + Gmail）
让 Codex 按时间段拉取邮件并解析成紧凑交易记录，写进 `data/raw/batchNN.json`。每周自动化的完整规则见仓库根目录 `AGENTS.md`。

要点（避免上次的坑）：
- 用 Gmail 连接器搜索：`from:dan@axios.com subject:"Pro Rata" after:YYYY/MM/DD before:YYYY/MM/DD`，并翻页拿全。数量异常时放宽到 `from:axios.com`，以覆盖代班作者。
- 必须读邮件完整正文，不能用搜索摘要代替；解析后核对正文日期与 subject。
- 每条交易字段：`date, company, sector, stage, amount_usd(USD百万), market(primary|secondary|ipo|ma|fund|debt), lead, valuation, country`；非美元折算近似美元。
- 每期附 `{date, subject, bfd, themes[]}`，便于 QA 核对日期/标题。

## 2. 分析（脚本）
```bash
python3 scripts/analyze.py \
  --raw 'data/raw/*.json' \
  --extra data/2026-W21.json \
  --out data/2026-Jan-May.json \
  --start 2026-01-01 --end 2026-05-31 --top 40
```
输出：
- **QA**：日期覆盖、同一天出现多个不同标题（=污染，需重跑那几期）。
- **持续被关注**：出现在 ≥2 期的公司、重复融资（多轮 primary，看估值是否递进）、并购战场（同一标的被多期点名）。
- **赛道**：按交易数排序 + 月度趋势 + 金额（注意金额被超大并购主导）。
- **最活跃投资人/收购方**。
- 写出合并数据集到 `--out`。

## 3. 生成报告 + 发布
让 Codex 基于脚本输出的 digest 写复盘（套用 `../preferences.md` 的赛道权重，如医药降权），存到 `../reviews/`，然后更新并发布 `../site/`。站点展示完整周报原文，不建 Gmail 草稿。

## 数据口径注意
- **记录数 ≠ 去重独立交易**：同一交易/IPO 路演常跨多期出现——这正是"持续关注度"的度量，但金额加总会重复计入。
- **板块标签跨期会漂移**（不同期对同类公司用不同标签），月度板块趋势为指示性。
- 脚本默认做"同日去重"，跨期重复保留（用于复现度量）。
