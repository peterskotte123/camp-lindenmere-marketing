#!/usr/bin/env python3
"""Merge deep/scored.csv with deep/geo_volume.json into KEYWORD-MASTER.csv. Run from this folder."""
import csv, json, pathlib

scored = list(csv.DictReader(open("deep/scored.csv")))
geo = json.load(open("deep/geo_volume.json"))
GEOS = ["ny", "nj", "ct", "pa", "nyc_dma", "philly_dma"]

def rnd(x): return round(x, 2) if isinstance(x, (int, float)) else ""
def season(ms):
    if not ms: return "", ""
    by = {m["month"]: m["search_volume"] or 0 for m in ms}
    peak = max(by, key=by.get); tot = sum(by.values())
    q = {"Sep-Nov": sum(by.get(m, 0) for m in (9, 10, 11)), "Dec-Feb": sum(by.get(m, 0) for m in (12, 1, 2)),
         "Mar-May": sum(by.get(m, 0) for m in (3, 4, 5)), "Jun-Aug": sum(by.get(m, 0) for m in (6, 7, 8))}
    return peak, " ".join(f"{k}:{round(100 * v / tot) if tot else 0}%" for k, v in q.items())

seen = {r["keyword"] for r in scored}
rows = []
for r in scored:
    k = r["keyword"]; us = geo["us"].get(k) or {}
    row = {"keyword": k, "family": r["family"], "verdict": r["verdict"], "score": r["score"], "flags": r["flags"], "stop": r["stop"],
           "us_volume": us.get("search_volume", r["us_volume"]), "us_cpc": rnd(us.get("cpc")) or r["us_cpc"],
           "bid_low": rnd(us.get("low_top_of_page_bid")) or r["bid_low"], "bid_high": rnd(us.get("high_top_of_page_bid")) or r["bid_high"],
           "competition": us.get("competition_level") or r["competition"]}
    for g in GEOS:
        gr = geo[g].get(k) or {}
        row[f"{g}_volume"] = gr.get("search_volume", ""); row[f"{g}_cpc"] = rnd(gr.get("cpc"))
    row["target4_volume"] = sum((geo[g].get(k) or {}).get("search_volume") or 0 for g in ("ny", "nj", "ct", "pa")) if any(k in geo[g] for g in GEOS) else ""
    pk, mix = season(us.get("monthly_searches") or [])
    row["peak_month"] = pk; row["season_mix"] = mix
    row["source"] = r["source"]; row["seed"] = r["seed"]
    rows.append(row)
# head terms pulled only in the geo step (not in harvest)
for k, us in geo["us"].items():
    if k in seen: continue
    row = {"keyword": k, "family": "head/probe", "verdict": "TEST", "score": "", "flags": "probe", "stop": "",
           "us_volume": us.get("search_volume"), "us_cpc": rnd(us.get("cpc")), "bid_low": rnd(us.get("low_top_of_page_bid")),
           "bid_high": rnd(us.get("high_top_of_page_bid")), "competition": us.get("competition_level")}
    for g in GEOS:
        gr = geo[g].get(k) or {}; row[f"{g}_volume"] = gr.get("search_volume", ""); row[f"{g}_cpc"] = rnd(gr.get("cpc"))
    row["target4_volume"] = sum((geo[g].get(k) or {}).get("search_volume") or 0 for g in ("ny", "nj", "ct", "pa"))
    pk, mix = season(us.get("monthly_searches") or []); row["peak_month"] = pk; row["season_mix"] = mix
    row["source"] = "probe"; row["seed"] = ""
    rows.append(row)

order = {"ADD NOW": 0, "TEST": 1, "NEVER": 2}
rows.sort(key=lambda x: (order[x["verdict"]], -(int(x["target4_volume"]) if str(x["target4_volume"]).isdigit() else -1), -(int(x["us_volume"]) if str(x["us_volume"]).isdigit() else 0)))
with open("KEYWORD-MASTER.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
short = [r for r in rows if r["verdict"] != "NEVER"]
with open("KEYWORD-SHORTLIST.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(short)
comp = [r for r in rows if r["family"] == "competitor" and "camp" in r["keyword"] and str(r["us_volume"]).isdigit() and int(r["us_volume"]) >= 50]
comp.sort(key=lambda r: -int(r["us_volume"]))
with open("COMPETITOR-BRAND-SEARCH.csv", "w", newline="") as f:
    cols = ["keyword", "us_volume", "us_cpc", "ny_volume", "nj_volume", "ct_volume", "pa_volume", "target4_volume", "peak_month", "season_mix"]
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(comp)
print(len(rows), "rows in KEYWORD-MASTER.csv;", len(short), "in shortlist;", len(comp), "competitor brand rows")
