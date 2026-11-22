#!/usr/bin/env python3
"""Harvest candidate keywords for Camp Lindenmere. Writes deep/harvest.jsonl (one row per hit, with source+seed).
Run from this folder: python3 harvest.py [--sites-only|--seeds-only]"""
import json, sys, pathlib
import dfs

OUT = pathlib.Path("deep/harvest.jsonl")

SUGGEST_SEEDS = [
    "sleepaway camp", "overnight camp", "overnight summer camp", "sleep away camp",
    "summer camp pennsylvania", "summer camp poconos", "sleepaway camp pa", "sleepaway camp pennsylvania",
    "sleepaway camp near nyc", "sleepaway camp new jersey", "sleepaway camp new york", "sleepaway camp connecticut",
    "sleepaway camp long island", "sleepaway camp westchester",
    "coed sleepaway camp", "teen summer camp", "sleepaway camp for teens", "sports sleepaway camp",
    "first time sleepaway camp", "sleepaway camp cost", "how much is sleepaway camp",
    "3 week sleepaway camp", "2 week sleepaway camp", "7 week sleepaway camp", "one week sleepaway camp",
    "trapeze camp", "circus summer camp", "horseback riding summer camp", "stem sleepaway camp",
    "performing arts sleepaway camp", "rock climbing summer camp",
    "best sleepaway camps", "sleepaway camp for 7 year olds", "sleepaway camp for 8 year olds",
    "sleepaway camp for 10 year olds", "sleepaway camp for 12 year olds",
    "summer camp 2027", "sleepaway camp 2027", "jewish sleepaway camp", "aca accredited camp",
    "camp lindenmere",
]
RELATED_SEEDS = ["sleepaway camp", "overnight camp", "summer camp poconos", "sleepaway camp cost",
                 "first time sleepaway camp", "teen summer camp", "sleepaway camp near me"]
SITES = ["camplindenmere.com", "lohikan.com", "pineforestcamp.com", "canadensis.com", "trailsendcampcamp.com",
         "camptowanda.com", "weequahic.com", "campstarlight.com", "tylerhillcamp.com", "islandlake.com"]

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    rows = []
    if mode in ("all", "--seeds-only"):
        for s in SUGGEST_SEEDS:
            for r in dfs.suggest(s, limit=300): r["source"] = "suggest"; rows.append(r)
            print("suggest", s, len(rows), file=sys.stderr)
        for s in RELATED_SEEDS:
            for r in dfs.related(s, depth=1, limit=200): r["source"] = "related"; rows.append(r)
            print("related", s, len(rows), file=sys.stderr)
    if mode in ("all", "--sites-only"):
        for d in SITES:
            try:
                for r in dfs.site(d, limit=300): r["source"] = "site"; rows.append(r)
            except Exception as e:
                print("site fail", d, e, file=sys.stderr)
            print("site", d, len(rows), file=sys.stderr)
    with OUT.open("a") as f:
        for r in rows: f.write(json.dumps(r) + "\n")
    print("wrote", len(rows), "rows to", OUT)

if __name__ == "__main__":
    main()
