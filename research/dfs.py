#!/usr/bin/env python3
"""Shared DataForSEO helper for keyword research. Import or run from the command line.

    python3 dfs.py volume "kw one" "kw two" [--lang en] [--loc 2840]
    python3 dfs.py suggest "seed phrase" [--limit 300]
    python3 dfs.py related "seed phrase"
    python3 dfs.py site alexandjana.com          # keywords a domain ranks for (Labs ranked_keywords)
    python3 dfs.py serp "query" [--device mobile]
    python3 dfs.py trends "kw one" "kw two"      # Google Trends, past 5 years, US
    python3 dfs.py locations "San Diego"         # find location codes
    python3 dfs.py check "kw one" "kw two"       # already researched? (looks in KEYWORD-MASTER.csv; see research-log.md)

Every call appends to deep/calls.log (path, cost) and caches responses in deep/cache/.
If the account balance is empty the API answers HTTP 402 and this module raises RuntimeError;
an empty result is never evidence of zero demand. To import this module from your own script,
run it from this folder WITHOUT -I (python3 myscript.py) or add sys.path.insert(0, "<this folder>").
Location 2840 = United States. Language codes: en, es, ru.
"""
import json, base64, urllib.request, pathlib, hashlib, sys, time, argparse

HERE = pathlib.Path(__file__).parent
CACHE = HERE / "deep" / "cache"; CACHE.mkdir(parents=True, exist_ok=True)
LOG = HERE / "deep" / "calls.log"
CREDS = pathlib.Path.home() / ".secrets/dataforseo/credentials"
AUTH = "Basic " + base64.b64encode(CREDS.read_text().strip().encode()).decode()
US = 2840

def call(path, body, use_cache=True):
    key = hashlib.sha1((path + json.dumps(body, sort_keys=True)).encode()).hexdigest()
    cf = CACHE / f"{key}.json"
    if use_cache and cf.exists():
        return json.loads(cf.read_text())
    req = urllib.request.Request("https://api.dataforseo.com/v3/" + path, data=json.dumps(body).encode(),
                                 headers={"Authorization": AUTH, "Content-Type": "application/json"})
    res = None
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                res = json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:300]
            try: msg = json.loads(body).get("status_message", body)
            except Exception: msg = body
            res = {"status_code": e.code, "status_message": msg, "tasks": []}
        except (urllib.error.URLError, TimeoutError) as e:
            res = {"status_code": 0, "status_message": str(e)[:200], "tasks": []}
        code = res.get("status_code")
        # 402 has been intermittent right after a top-up (nodes see the new balance at different times);
        # 429/5xx/0 are transient. Back off and retry before giving up.
        if code in (402, 429, 500, 502, 503, 0) and attempt < 5:
            with LOG.open("a") as f: f.write(f"{time.strftime('%H:%M:%S')} {path} retry{attempt+1} status={code} {str(res.get('status_message'))[:80]}\n")
            time.sleep(4 * (attempt + 1)); continue
        break
    with LOG.open("a") as f: f.write(f"{time.strftime('%H:%M:%S')} {path} cost={res.get('cost')} status={res.get('status_code')}\n")
    if res.get("status_code") == 402:
        raise RuntimeError(f"DataForSEO HTTP 402 after retries: {res.get('status_message')}. If the balance is positive this is transient, re-run; never treat it as zero search volume.")
    if res.get("status_code") == 20000:
        cf.write_text(json.dumps(res))
    return res

def _items(res):
    out = []
    for t in res.get("tasks") or []:
        if t.get("status_code") != 20000:
            print("task error:", t.get("status_code"), t.get("status_message"), file=sys.stderr)
        for r in t.get("result") or []:
            if "items" in r and isinstance(r["items"], list): out.extend(r["items"])
            else: out.append(r)
    return out

def volume(keywords, lang="en", loc=US):
    """Google Ads search volume for up to 1000 keywords. Returns list of dicts:
    keyword, search_volume, cpc, competition, competition_index, low_top_of_page_bid, high_top_of_page_bid, monthly_searches."""
    out = []
    kws = [k for k in dict.fromkeys(" ".join(k.split()).lower() for k in keywords) if k]
    for i in range(0, len(kws), 700):
        out += _items(call("keywords_data/google_ads/search_volume/live", [{"keywords": kws[i:i+700], "location_code": loc, "language_code": lang}]))
    return out

def suggest(seed, lang="en", loc=US, limit=300):
    """Labs keyword_suggestions: phrases containing the seed, with keyword_info (volume, cpc, competition) and intent."""
    items = _items(call("dataforseo_labs/google/keyword_suggestions/live", [{"keyword": seed, "location_code": loc, "language_code": lang, "limit": limit, "include_seed_keyword": True}]))
    return [flat(it, seed) for it in items]

def related(seed, lang="en", loc=US, depth=1, limit=300):
    """Labs related_keywords: Google's 'searches related to' graph around the seed."""
    items = _items(call("dataforseo_labs/google/related_keywords/live", [{"keyword": seed, "location_code": loc, "language_code": lang, "depth": depth, "limit": limit}]))
    return [flat(it.get("keyword_data") or it, seed) for it in items]

def site(domain, lang="en", loc=US, limit=500):
    """Labs ranked_keywords: keywords a domain ranks for organically, with volume/cpc and the ranking URL."""
    items = _items(call("dataforseo_labs/google/ranked_keywords/live", [{"target": domain, "location_code": loc, "language_code": lang, "limit": limit, "order_by": ["keyword_data.keyword_info.search_volume,desc"]}]))
    out = []
    for it in items:
        kd = it.get("keyword_data") or {}; row = flat(kd, domain)
        se = (it.get("ranked_serp_element") or {}).get("serp_item") or {}
        row["rank"] = se.get("rank_absolute"); row["url"] = se.get("url"); row["title"] = se.get("title")
        out.append(row)
    return out

def serp(query, device="desktop", lang="en", loc=US):
    """Live organic SERP (note: this endpoint never returns the paid block for us). Returns item types and top organic."""
    res = call("serp/google/organic/live/advanced", [{"keyword": query, "location_code": loc, "language_code": lang, "device": device, "depth": 20}])
    items = _items(res)
    return {"query": query, "types": sorted({i.get("type") for i in items if i.get("type")}),
            "ai_overview": any(i.get("type") == "ai_overview" for i in items),
            "organic": [{"rank": i.get("rank_absolute"), "domain": i.get("domain"), "title": i.get("title"), "url": i.get("url")} for i in items if i.get("type") == "organic"][:10],
            "paa": [q.get("title") for i in items if i.get("type") == "people_also_ask" for q in (i.get("items") or [])][:10]}

def trends(keywords, loc=US, time_range="past_5_years"):
    """Google Trends explore: interest over time (and by region when available). Up to 5 keywords."""
    items = _items(call("keywords_data/google_trends/explore/live", [{"keywords": keywords[:5], "location_code": loc, "time_range": time_range, "item_types": ["google_trends_graph", "google_trends_map"]}]))
    return items

def locations(name):
    res = call("keywords_data/google_ads/locations", {}, use_cache=True) if False else None
    req = urllib.request.Request("https://api.dataforseo.com/v3/keywords_data/google_ads/locations/us", headers={"Authorization": AUTH})
    with urllib.request.urlopen(req, timeout=180) as r: data = json.loads(r.read().decode())
    hits = [l for t in data.get("tasks", []) for l in (t.get("result") or []) if name.lower() in (l.get("location_name") or "").lower()]
    return [(l["location_code"], l["location_name"], l.get("location_type")) for l in hits][:30]

def researched(keywords):
    """Which of these keywords are already in KEYWORD-MASTER.csv (every probe feeds it). Returns {keyword: sources or None}.
    Check this before spending on a volume call; see research-log.md for the probes run so far."""
    import csv
    master = HERE.parent.parent / "KEYWORD-MASTER.csv"
    have = {}
    if master.exists():
        for r in csv.DictReader(open(master, encoding="utf-8")): have[r["keyword"]] = r["sources"]
    return {k: have.get(" ".join(k.split()).lower()) for k in keywords}

def flat(kd, seed=None):
    ki = kd.get("keyword_info") or {}
    si = kd.get("search_intent_info") or {}
    return {"seed": seed, "keyword": kd.get("keyword"), "search_volume": ki.get("search_volume"), "cpc": ki.get("cpc"),
            "competition": ki.get("competition"), "competition_level": ki.get("competition_level"),
            "low_top_of_page_bid": ki.get("low_top_of_page_bid"), "high_top_of_page_bid": ki.get("high_top_of_page_bid"),
            "monthly_searches": ki.get("monthly_searches"), "intent": si.get("main_intent")}

def table(rows, keys=("search_volume", "cpc", "competition_index", "competition_level", "low_top_of_page_bid", "high_top_of_page_bid", "intent", "keyword")):
    for r in sorted(rows, key=lambda r: -(r.get("search_volume") or 0)):
        print("  ".join(str(r.get(k) if r.get(k) is not None else "-").ljust(8 if k != "keyword" else 0) for k in keys))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cmd"); ap.add_argument("args", nargs="*")
    ap.add_argument("--lang", default="en"); ap.add_argument("--loc", type=int, default=US); ap.add_argument("--limit", type=int, default=300); ap.add_argument("--device", default="desktop")
    a = ap.parse_args()
    if a.cmd == "volume": table(volume(a.args, a.lang, a.loc))
    elif a.cmd == "suggest": table(suggest(a.args[0], a.lang, a.loc, a.limit))
    elif a.cmd == "related": table(related(a.args[0], a.lang, a.loc, limit=a.limit))
    elif a.cmd == "site": table(site(a.args[0], a.lang, a.loc, a.limit), keys=("search_volume", "cpc", "rank", "intent", "keyword", "url"))
    elif a.cmd == "serp": print(json.dumps(serp(a.args[0], a.device, a.lang, a.loc), indent=1))
    elif a.cmd == "trends": print(json.dumps(trends(a.args, a.loc), indent=1)[:6000])
    elif a.cmd == "locations": print(locations(a.args[0]))
    elif a.cmd == "check":
        for k, src in researched(a.args).items(): print(("RESEARCHED  " + src) if src else "new         ", "|", k)
