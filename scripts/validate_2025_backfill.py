"""Reconcile the committed annual backfill without the original source cache."""
import collections
import datetime
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text())


def official(url):
    host = urlparse(url).hostname or ""
    return host == "axios.com" or host.endswith(".axios.com")


inventory = read("data/2025-source-inventory.json")
coverage = read("data/2025-coverage.json")
stats = read("research/2025-summary.json")
issues = {item["date"]: item for item in inventory["issues"]}
assert len(issues) == len(inventory["issues"]) == 239
assert all(item["official_body_verified"] and official(item["source_url"])
           for item in issues.values())
rows = []
for month in stats["months"]:
    data = read(f"data/{month['month']}.json")
    monthly = data["deals"] + data["context_events"]
    assert len(monthly) == month["records"]
    assert all(row["date"].startswith(month["month"]) for row in monthly)
    assert len(data["issues"]) == month["issues"]
    assert sum(row.get("market") == "primary" for row in monthly) == month["primary"]
    assert sum(row["sector"] == "医疗与生命科学" for row in monthly) == month["healthcare"]
    rows.extend(monthly)
assert len(rows) == len({row["id"] for row in rows}) == stats["record_count"] == 9722
assert all(row["date"] in issues and official(row["source_url"])
           and len(row["source_paragraph_sha256"]) == 64 for row in rows)
assert collections.Counter(row["date"] for row in rows) == {
    date: item["published_records"] for date, item in issues.items()}
assert collections.Counter(row.get("market") or row.get("event_type") for row in rows) == stats["market_counts"]
assert collections.Counter(row["sector"] for row in rows) == stats["sector_counts"]
assert sum(row["sector"] == "医疗与生命科学" and row.get("market") == "primary"
           for row in rows) == stats["healthcare_primary_records"] == 785
start = datetime.date(2025, 1, 1)
weekdays = {(start + datetime.timedelta(days=i)).isoformat() for i in range(365)
            if (start + datetime.timedelta(days=i)).weekday() < 5}
gaps = {item["date"] for item in coverage["unlocated_weekdays"]}
assert len(gaps) == 22 and not gaps.intersection(issues)
assert weekdays == gaps | issues.keys()
assert stats["unique_round_count"] is None and stats["amount_total"] is None
print(json.dumps({"issues": len(issues), "records": len(rows),
                  "primary_reports": stats["market_counts"]["primary"],
                  "healthcare_reports": stats["healthcare_records"],
                  "healthcare_primary_reports": stats["healthcare_primary_records"]},
                 ensure_ascii=False))
