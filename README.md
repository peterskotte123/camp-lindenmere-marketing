# Camp Lindenmere marketing research

Keyword demand, click costs, competitor sweep, acquisition cost and lifetime value, and a 2027 enrollment strategy for camplindenmere.com. Prepared November 2026.

## Start here

| File | What it is |
|---|---|
| `research/BRIEF.pdf` | Three-page printable brief: TLDR, demand, costs, strategy, keyword shortlist |
| `research/BRIEF.html` | Same brief as a web page, prints to three letter pages |
| `research/HANDOFF.md` | How the research was done, the numbers, the seven-campaign structure, caveats |
| `research/STRATEGY.md` | Multichannel plan: offer, Lohikan window, compounding channels, paid traffic, calendar, kill rules |
| `research/SEO-PLAN.md` | Organic search plan: current rankings, page-two keywords, activity pages, blog, technical fixes |
| `research/CAC-LTV.md` | What a camper is worth and what each channel should cost, with sources |
| `research/competitors-2026-11-05.md` | 24 Poconos camps: prices, early credits, trials, guarantees, Instagram, fairs |

## Data

| File | Rows | Notes |
|---|---|---|
| `research/KEYWORD-SHORTLIST.csv` | 485 | Keywords worth testing, with US and NY, NJ, CT, PA volume and CPC |
| `research/KEYWORD-MASTER.csv` | 3,663 | Everything researched, with score, verdict and reason. Rejects double as the negative list |
| `research/COMPETITOR-BRAND-SEARCH.csv` | 104 | Rival camps searched by name |
| `research/ANGLE-PROBES.csv` | 130 | Brainstormed low-cost angles and what they returned |
| `research/competitors-2026-11-05.csv` | 24 | Competitor sweep as a table |

Volumes and CPCs are Google Ads estimates pulled through DataForSEO on 2026-11-05. Validate the shortlist in Keyword Planner with NY, NJ, CT and PA targeting before building campaigns.

## Scripts

`research/dfs.py` wraps the DataForSEO API (credentials in `~/.secrets/dataforseo/credentials`, never in the repo). `harvest.py` pulls suggestions and competitor rankings, `score.py` applies the rubric, `build_master.py` writes the CSVs. Raw pulls are in `research/deep/`.

## Site clone

`clone/` is a full mirror of camplindenmere.com taken 2026-11-21: 97 pages, the theme, scripts, fonts and the uploads library (about 1.1 GB). Internal links are rewritten to local paths; analytics and HubSpot tracking point at a dead domain so browsing the clone does not touch the camp's real reports. The camp-song audio files were skipped.

To view it:

```
cd clone && python3 server.py 8765
```

Then open http://localhost:8765/ (use localhost, not 127.0.0.1, or YouTube embeds refuse to play). The small server exists because WordPress links assets with version query strings that a plain file server cannot resolve. The hero video, YouTube embeds, the 360 tour and enrollment links still load from the internet.
