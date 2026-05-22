# 月度/周度市场复盘流程

把 Axios Pro Rata 邮件变成结构化数据 + 复盘报告的可复用流程。分两半：
**抽取**（需要 LLM/agent，因为要解析邮件 HTML）和 **分析**（纯脚本，确定性可复现）。

## 1. 抽取（Claude + Gmail）
让 Claude 按时间段拉取邮件并解析成紧凑交易记录，写进 `data/raw/batchNN.json`。

要点（避免上次的坑）：
- 用 Gmail `search_threads`：`from:dan@axios.com subject:"Pro Rata" after:YYYY/MM/DD before:YYYY/MM/DD`，翻页拿全 threadId。
- 分批派并行子 agent，每批 ~7–8 期。**每个 agent 必须用唯一的临时文件名**（如 `/tmp/fix_<threadId>.html`），否则并行时会互相覆盖、导致日期错配。
- 邮件正文在 `messages[0].htmlBody`（不是 plaintext_body）；用 jq 取出后 strip 标签。
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

## 3. 生成报告 + 投递
让 Claude 基于脚本输出的 digest 写复盘（套用 `../preferences.md` 的赛道权重，如医药降权），存到 `../reviews/`，并建成 Gmail 草稿。

## 数据口径注意
- **记录数 ≠ 去重独立交易**：同一交易/IPO 路演常跨多期出现——这正是"持续关注度"的度量，但金额加总会重复计入。
- **板块标签跨期会漂移**（不同期对同类公司用不同标签），月度板块趋势为指示性。
- 脚本默认做"同日去重"，跨期重复保留（用于复现度量）。
