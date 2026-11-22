# Camp Lindenmere keyword research log

Date: 2026-11-05. Run from `~/Projects/Lewis/research`. Same method as Khrystyna2 (`ads-data/analysis/findings/keyword-method.md`) and Cake (`docs/keywords-log.md`).

## Tools

- `dfs.py`: DataForSEO helper copied from Khrystyna2. Reads credentials from `~/.secrets/dataforseo/credentials`. Every call appends to `deep/calls.log` with its cost and caches the response in `deep/cache/`.
- `harvest.py`: 41 suggest seeds, 7 related seeds, 10 site pulls (camplindenmere.com plus 9 Poconos competitors). Output `deep/harvest.jsonl`, 4,219 rows.
- `score.py`: rubric adapted from the photography one. Output `deep/scored.csv`, 3,625 unique keywords.
- `build_master.py`: merges scores with the seven-location volume pull. Outputs `KEYWORD-MASTER.csv`, `KEYWORD-SHORTLIST.csv`, `COMPETITOR-BRAND-SEARCH.csv`.

## Location codes used

| Code | Place |
|---|---|
| 2840 | United States |
| 21167 | New York state |
| 21164 | New Jersey |
| 21139 | Connecticut |
| 21171 | Pennsylvania |
| 200501 | New York NY DMA (metro) |
| 200504 | Philadelphia PA DMA |

## Calls and cost

See `deep/calls.log`. Balance before: $17.03. Cap set: $10. Spent: $2.40 across 75 calls.

| Endpoint | Calls | Purpose |
|---|---|---|
| labs keyword_suggestions | 41 | harvest from seeds |
| labs related_keywords | 7 | harvest from seeds |
| labs ranked_keywords | 10 | what Lindenmere and 9 competitors rank for |
| google_ads search_volume | 12 | volume and CPC by US, NY, NJ, CT, PA, NYC DMA, Philly DMA, plus the angle probe |
| google_ads ad_traffic_by_keywords | 1 | returned only an aggregate row, not used |
| google_trends explore | 1 | seasonality of head terms |
| serp organic | 3 | who ranks for brand and Poconos terms |

Competitor sweep ran separately with web search and page fetches, no API cost. Lohikan closure verified directly on lohikan.com on 2026-11-05.

## Decisions and findings while running

1. `sleepaway camp` as a bare head term is polluted by the 1983 horror film. Google Trends shows an October spike every year, and the suggest pull returned "sleepaway camp 2", "cast", "actors", "film" and so on. `overnight camp` is the clean head term. Any campaign on the head term needs movie negatives (movie, film, cast, 1983, actors, sequel, angela, ricky, survivor, return, streaming, watch, ending).
2. Google reports one volume for a cluster of close variants (all twelve "sleepaway camp nj" spellings show 480). Group totals in `deep/groups.csv` are inflated by that. `deep/groups-distinct.csv` de-duplicates by volume signature and is the one to quote.
3. The Google Ads `ad_traffic_by_keywords` endpoint returned a single aggregate row with no per-keyword figures for $0.09, so CPC estimates come from the `search_volume` endpoint: `cpc` is Google's average, `low_top_of_page_bid` and `high_top_of_page_bid` are the bid range. Keyword Planner inside his own account will show the same numbers for free.
4. The organic SERP endpoint never returns the paid block (same as Cake and Khrystyna2 found). "No ads seen" from this tool is not evidence that nobody advertises.
5. Jewish-affiliation terms are flagged `confirm-affiliation`, not scored, because the site does not state an affiliation and 40 searches a month ask "is camp lindenmere jewish".
6. Competitor brand names are hard stops in the rubric (policy: do not use them in ad copy) but are kept in `COMPETITOR-BRAND-SEARCH.csv` because brand search volume is the cheapest proxy for each camp's marketing reach.
7. Stale-year terms (2020, 2018) get a penalty. Only 2027 and 2028 count.
