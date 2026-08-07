#!/usr/bin/env python3
"""
Aggregate + analyze Axios Pro Rata deal data into a market review.

The extraction step (Gmail HTML -> structured deal JSON) is done by LLM agents
that write batch files into data/raw/ (see scripts/README.md). This script is the
deterministic half: it consolidates those batch files, runs QA, computes
recurrence ("continuously watched" companies/sectors), and writes a consolidated
dataset + prints a digest you can paste into a review.

Usage:
  python3 scripts/analyze.py --raw 'data/raw/*.json' --extra data/2026-W21.json \
      --out data/2026-Jan-May.json --start 2026-01-01 --end 2026-05-31
"""
import json, glob, collections, re, argparse, sys

SUFFIXES = r'\b(inc|ltd|llc|corp|co|group|holdings|technologies|technology|labs|capital|partners|the)\b'
MONTHS_DEFAULT = None  # auto-derived

def norm(name):
    if not name: return ''
    n = name.lower().strip()
    n = re.sub(r'[\.,]', '', n)
    n = re.sub(SUFFIXES, '', n)
    return re.sub(r'\s+', ' ', n).strip()

def load(raw_glob, extra):
    issues, deals = [], []
    for f in sorted(glob.glob(raw_glob)):
        try:
            d = json.load(open(f))
        except Exception as e:
            print(f"WARN: skipping {f}: {e}", file=sys.stderr); continue
        for it in d.get('issues', []):
            it = dict(it); it['_src'] = f.split('/')[-1]; issues.append(it)
        for dl in d.get('deals', []):
            dl = dict(dl); dl['_src'] = f.split('/')[-1]; deals.append(dl)
    for f in (extra or []):
        d = json.load(open(f))
        for dl in d.get('deals', []):
            deals.append({k: dl.get(k) for k in
                ['date','company','sector','stage','amount_usd','market','lead','valuation','country']})
    return issues, deals

def in_range(d, start, end):
    if not d: return False
    if start and d < start: return False
    if end and d > end: return False
    return True

def dedup_within_date(deals):
    """Collapse the same deal listed twice on the same day (re-reports keep cross-date)."""
    seen, out = set(), []
    for dl in deals:
        key = (dl.get('date'), norm(dl.get('company')), dl.get('market'))
        if key in seen and key[1]:
            continue
        seen.add(key); out.append(dl)
    return out

def qa(issues):
    by_date = collections.defaultdict(list)
    for it in issues:
        by_date[it.get('date')].append((str(it.get('subject',''))[:42], it.get('_src')))
    missing_dates = by_date.pop(None, []) + by_date.pop('', [])
    dups = {k: v for k, v in by_date.items() if len(v) > 1}
    print(
        f"\n[QA] issue dates: {len(by_date)} | issues missing dates: {len(missing_dates)} "
        f"| dates with >1 distinct issue (possible contamination): {len(dups)}"
    )
    for subject, src in missing_dates:
        print(f"  !! missing date: {subject!r} ({src})")
    for k in sorted(dups):
        subs = {s for s,_ in dups[k]}
        if len(subs) > 1:
            print(f"  !! {k}: {dups[k]}  <- different subjects, investigate/re-fetch")
    return by_date

def recurrence(deals):
    comp = collections.defaultdict(list)
    for dl in deals:
        if dl.get('company'): comp[norm(dl['company'])].append(dl)
    rows = []
    for k, ds in comp.items():
        dates = sorted({d.get('date') for d in ds if d.get('date')})
        if len(dates) >= 2:
            disp = collections.Counter(d['company'] for d in ds).most_common(1)[0][0]
            mk = dict(collections.Counter(d.get('market') for d in ds))
            secs = collections.Counter(d.get('sector') for d in ds if d.get('sector'))
            rows.append((len(dates), disp, dates, mk, secs.most_common(1)[0][0] if secs else '?'))
    rows.sort(reverse=True)
    return rows, comp

def repeat_primary(comp):
    res = []
    for k, ds in comp.items():
        pr = [x for x in ds if x.get('market') == 'primary']
        pdates = sorted({x.get('date') for x in pr})
        if len(pdates) >= 2:
            disp = collections.Counter(x['company'] for x in pr).most_common(1)[0][0]
            amts = [x.get('amount_usd') for x in pr if isinstance(x.get('amount_usd'), (int, float))]
            res.append((len(pdates), disp, pdates, sum(amts)))
    res.sort(reverse=True)
    return res

def battlegrounds(comp):
    res = []
    for k, ds in comp.items():
        ma = [x for x in ds if x.get('market') == 'ma']
        mdates = sorted({x.get('date') for x in ma})
        if len(mdates) >= 2:
            disp = collections.Counter(x['company'] for x in ma).most_common(1)[0][0]
            res.append((len(mdates), disp, mdates))
    res.sort(reverse=True)
    return res

def sectors(deals):
    months = sorted({(d.get('date') or '')[:7] for d in deals if d.get('date')})
    sm = collections.defaultdict(collections.Counter)
    samt = collections.defaultdict(float)
    stot = collections.Counter()
    for dl in deals:
        s = (dl.get('sector') or 'unknown').split('/')[0].strip().lower()
        stot[s] += 1; sm[s][(dl.get('date') or '')[:7]] += 1
        a = dl.get('amount_usd')
        if isinstance(a, (int, float)): samt[s] += a
    return months, sm, samt, stot

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--raw', default='data/raw/*.json')
    ap.add_argument('--extra', nargs='*', default=[])
    ap.add_argument('--out', default=None)
    ap.add_argument('--start', default=None)
    ap.add_argument('--end', default=None)
    ap.add_argument('--top', type=int, default=40)
    ap.add_argument('--no-dedup', action='store_true')
    a = ap.parse_args()

    issues, deals = load(a.raw, a.extra)
    deals = [d for d in deals if in_range(d.get('date'), a.start, a.end)] if (a.start or a.end) else deals
    if not a.no_dedup:
        before = len(deals); deals = dedup_within_date(deals)
        print(f"[dedup] same-day duplicates removed: {before - len(deals)}")
    print(f"issues: {len(issues)} | deal records: {len(deals)}")
    qa(issues)

    rows, comp = recurrence(deals)
    print(f"\n=== COMPANIES IN >=2 DISTINCT ISSUES (top {a.top}) ===  [{len(rows)} total]")
    for n, disp, dates, mk, sec in rows[:a.top]:
        print(f"  {n:3d}x  {disp[:34]:34s} {sec[:14]:14s} {dates[0]}..{dates[-1]}  {mk}")

    print("\n=== REPEAT PRIMARY FUNDRAISERS (>=2 primary rounds) ===")
    for n, disp, pdates, tot in repeat_primary(comp)[:25]:
        print(f"  {n}x {disp[:32]:32s} ${tot:.0f}M  {pdates}")

    print("\n=== M&A BATTLEGROUNDS (target named in >=2 issues) ===")
    for n, disp, mdates in battlegrounds(comp)[:20]:
        print(f"  {n}x {disp[:32]:32s} {mdates[0]}..{mdates[-1]}")

    months, sm, samt, stot = sectors(deals)
    print(f"\n=== TOP SECTORS BY DEAL COUNT (monthly trend {months[0]}..{months[-1]}) ===")
    for s, cnt in stot.most_common(18):
        trend = ' '.join(f"{sm[s][m]:>3d}" for m in months)
        print(f"  {s[:22]:22s} n={cnt:4d}  ${samt[s]/1000:7.1f}B  [{trend}]")

    inv = collections.Counter(d['lead'].strip() for d in deals if d.get('lead'))
    print("\n=== MOST ACTIVE LEAD INVESTORS / ACQUIRERS (top 20) ===")
    for k, v in inv.most_common(20):
        print(f"  {v:3d}  {k[:40]}")

    if a.out:
        period = f"{a.start or (months and months[0])}..{a.end or (months and months[-1])}"
        json.dump({"period": period, "source": "Axios Pro Rata",
                   "issue_count": len(issues), "deal_count": len(deals), "deals": deals},
                  open(a.out, 'w'), ensure_ascii=False, indent=0)
        print(f"\nsaved consolidated -> {a.out}")

if __name__ == '__main__':
    main()
