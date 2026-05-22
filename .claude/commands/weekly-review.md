---
description: 生成本周一二级市场周报（基于 Axios Pro Rata），并建成 Gmail 草稿
---

按既定流程生成本周市场周报。务必逐步完成，不要跳过校验。

## 0. 读偏好
先读 `preferences.md`（赛道权重：医药降权；交付：Gmail 草稿不发送；AI 方向列写实际业务描述）。

## 1. 确定日期范围
取**最近一个已完整结束的工作周**（周一至周五）。用 `date` 计算，得到 `START`(YYYY/MM/DD) 和 `END`，以及周编号 `YYYY-Www`。

## 2. 抓取 Axios Pro Rata
用 Gmail `search_threads`：`from:dan@axios.com subject:"Pro Rata" after:START before:END+1天`，翻页拿全 threadId。
逐封用 `get_thread`（messageFormat FULL_CONTENT）取 `messages[0].htmlBody`。
**关键**：每封用唯一临时文件名（如 `/tmp/wk_<threadId>.html`）避免并行覆盖；strip 标签后核对 in-body 日期与 subject。

## 3. 解析入库
每条交易抽成紧凑记录：`{date, company, sector, stage, amount_usd(USD百万), market(primary|secondary|ipo|ma|fund|debt), lead, valuation, country}`，非美元折算近似美元。
写入 `data/<YYYY-Www>.json`，结构 `{week, range, source, issues:[], deals:[...]}`。

## 4. 复现分析
运行 `python3 scripts/analyze.py --raw 'data/*.json' --top 40`（跨周累积，识别"持续被关注"的公司/赛道）。读 digest。

## 5. 生成周报
存到 `reviews/<YYYY-Www>.md`，三块结构：
① 本周重要交易（一级表格 + 二级/M&A/IPO）② 创业思路 + 中国对标 ③ 持续融资方向（用累积数据）。
套用偏好：医药降权；AI 项目"方向"列写实际业务描述（非"AI"），≤30 家的层级铺成完整表格行。

## 6. 建 Gmail 草稿（不发送）
`create_draft` 到 `esther330825@gmail.com`，纯文本 `body` + 排版 `htmlBody`。**不要发送**，只建草稿。

## 7. 提交
把 `data/` 与 `reviews/` 的新文件 commit 并 push 到当前开发分支。最后回复一句：本周做了什么 + 草稿已就绪。
