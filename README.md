# Camp Lindenmere marketing research

Keyword demand, click costs, competitor sweep, acquisition cost and lifetime value, and a 2027 enrollment strategy for camplindenmere.com. Prepared November 2026.

## Start here

| File | What it is |
|---|---|
| `research/BRIEF.pdf` | Three-page printable brief: TLDR, demand, costs, strategy, keyword shortlist |
| `research/BRIEF.html` | Same brief as a web page, prints to three letter pages |
| `research/HANDOFF.md` | How the research was done, the numbers, the seven-campaign structure, caveats |
| `research/STRATEGY.md` | Multichannel plan: offer, Lohikan window, compounding channels, paid traffic, calendar, kill rules |
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

A local mirror of the live site was built for mocking up changes. It is 1.1 GB and not in the repo. To rebuild:

```
mkdir clone && cd clone
wget --mirror --page-requisites --convert-links --adjust-extension --no-parent https://camplindenmere.com/
```
