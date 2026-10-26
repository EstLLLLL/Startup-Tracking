"""Reproduce source-record counts and validate the curated brainstorming cases.

Run from the repository root: python3 scripts/analyze_brainstorm.py
This does not infer unique rounds or add mixed financing/partnership amounts.
"""
import json, re, collections
from pathlib import Path

def norm(name):
    n=re.sub(r'[\.,]','',(name or '').lower().strip())
    n=re.sub(r'\b(inc|ltd|llc|corp|co|group|holdings|technologies|technology|labs|capital|partners|the)\b','',n)
    return re.sub(r'\s+',' ',n).strip()

root=Path(__file__).resolve().parent.parent
source_files=[root/'data/2026-Jan-May.json',*sorted((root/'data').glob('2026-W*.json'))]
source_rows=[row for f in source_files for row in json.loads(f.read_text())['deals']]
dedup={}
for row in source_rows:
    dedup.setdefault((row.get('date'),norm(row.get('company')),row.get('market')),row)
cases=json.loads((root/'data/2025-2026-brainstorm-cases.json').read_text())
assert len(cases['deals'])==cases['case_count']
assert len({r['id'] for r in cases['deals']})==len(cases['deals'])
assert all('2025-01-01'<=r['date']<='2026-10-23' and r['source_url'].startswith('https://') for r in cases['deals'])
assert all(r.get('amount_usd') is None or isinstance(r['amount_usd'],(int,float)) for r in cases['deals'])
assert all(r['market'] in ['primary','mixed','partnership'] for r in cases['deals'])
print(json.dumps({
 'source2026':{'records_after_same_day_dedup':len(dedup),'market_counts':dict(collections.Counter(r.get('market') for r in dedup.values()))},
 'curated':{'events':len(cases['deals']),'entities':len({r['entity_id'] for r in cases['deals']}),'year_counts':dict(collections.Counter(r['year'] for r in cases['deals'])),'sector_counts':dict(collections.Counter(r['sector'] for r in cases['deals']))},
 'limits':'Records are not unique financing rounds; curated2025 cases are not a full-year census. No amount totals or cross-year market growth are calculated.'
},ensure_ascii=False,indent=2))
