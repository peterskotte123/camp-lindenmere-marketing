# Camp Lindenmere: keyword research and competitor sweep

Prepared 2026-11-05 for the meeting on 2026-11-06. Everything here came from DataForSEO (Google Ads and Google Labs data), the camp's own website, and competitor websites. Total research spend: $2.40 of API credit across 75 calls.

Read first: the Lohikan closure under Competitors, then the demand table, then the clever angles.

## Files

| File | What it is |
|---|---|
| `KEYWORD-MASTER.csv` | Every keyword found, 3,663 rows, scored, with US and state-level volume and CPC |
| `KEYWORD-SHORTLIST.csv` | The 485 rows that are worth testing or already matter (brand, geo, activity, cost, session, age) |
| `COMPETITOR-BRAND-SEARCH.csv` | How many people search each competitor camp by name each month, by state |
| `competitors-2026-11-05.csv` and `.md` | Pricing, sessions, discounts, first-timer offers, and social reach for the Poconos camps |
| `ANGLE-PROBES.csv` | 130 brainstormed angle phrases checked for volume; 90 had none |
| `CAC-LTV.md` | Industry retention, margin and cost-per-camper benchmarks, a lifetime value model on Lindenmere's tuition, and CAC by channel |
| `STRATEGY.md` | The multichannel 2027 enrollment strategy: offer, Lohikan window, retention, advisors, content, paid channels, budget split, calendar, kill rules |
| `BRIEF.html` | The one-page printable summary |
| `deep/groups-distinct.csv` | Demand and median CPC per ad group, de-duplicated |
| `research-log.md` | What was run, what it cost, and the judgment calls |

Column guide for the keyword files: `us_volume` is average monthly Google searches in the US. `ny_volume`, `nj_volume`, `ct_volume`, `pa_volume` are the same for each state, and `target4_volume` is their sum. `nyc_dma_volume` is the New York metro TV market, which overlaps NY, NJ and CT. `us_cpc` is Google's average cost per click. `bid_low` and `bid_high` are the top-of-page bid range. `season_mix` shows what share of the year's searches fall in each quarter. `verdict` is ADD NOW, TEST, or NEVER from the rubric, and `stop` says why a term was rejected.

## The process, in the order it ran

This is the same method used for Khrystyna's photography business and the Cake project. It costs a few dollars and takes an evening.

1. **Harvest.** Feed 41 seed phrases (sleepaway camp, overnight camp, summer camp Poconos, sleepaway camp NJ, teen summer camp, 3 week sleepaway camp, trapeze camp, and so on) into Google's keyword suggestion and related-search data. Pull every keyword camplindenmere.com and nine competitor sites already rank for. Result: 4,219 raw rows.
2. **Normalize and score.** Lowercase, collapse spelling variants, then score each keyword with a rubric. Points for hire intent (sleepaway or overnight plus a place, format, age, session length, or activity), for a Pennsylvania or home-state place word, for a price word, for a session-length word. Penalties for "best", "reviews", "cheap", scholarship terms. Hard stops for the horror movie, day camps, other states, religious or special-needs camps the site does not offer, staff recruiting, and competitor brand names. Result: 52 ADD NOW, 395 TEST, 3,178 NEVER.
3. **Pull volume and CPC by geography.** Take the 601 keywords that survived plus a list of head terms and probe phrases, and pull Google Ads volume and CPC for the US, New York, New Jersey, Connecticut, Pennsylvania, the New York metro, and the Philadelphia metro.
4. **Group into ad groups** and de-duplicate, because Google reports one number for a cluster of spellings. Twelve spellings of "sleepaway camp nj" all show 480 a month. That is one keyword, not twelve.
5. **Validate in his own account.** Paste the shortlist into Keyword Planner with his real geo targeting. His account's numbers beat these because they reflect his Quality Score and history.

Then the weekly loop, every Monday, twenty minutes: pull the search terms report, score every new query with the same rubric, add negatives for anything off-intent that got a click, promote anything on-intent with a click to its own exact-match keyword, and log every change with the query that caused it.

## What the numbers say

### Demand is small and seasonal. Cost per click is reasonable.

Distinct monthly searches across NY, NJ, CT and PA, after de-duplicating spelling variants:

| Ad group | Distinct keywords | Monthly searches, 4 states | Median CPC |
|---|---|---|---|
| Activity plus overnight (soccer, basketball, horse, volleyball, lacrosse, tennis) | 54 | 2,280 | $2.81 |
| Near me (sleepaway camp near me, overnight summer camp near me) | 10 | 1,720 | $2.91 |
| Cost and tuition | 28 | 1,180 | $3.07 |
| Pennsylvania and Poconos | 15 | 1,090 | $5.13 |
| New York, NYC, Long Island | 14 | 900 | $3.37 |
| Philadelphia, East Coast, Northeast | 9 | 900 | $3.76 |
| New Jersey | 4 | 560 | $2.62 |
| Connecticut | 6 | 450 | $5.15 |
| Session length (2 week, 3 week, 7 week) | 15 | 440 | $4.43 |
| Age (for teens, for 7 year olds) | 6 | 270 | $6.29 |
| Co-ed and format words | 4 | 170 | $2.25 |
| Camp Lindenmere brand | 13 | 2,690 | $7.22 |

The bare head terms (summer camp, sleepaway camps, overnight camp) add about 25,000 a month in the four states, but most of that is day-camp intent, the horror movie, and people who already have a camp. They are TEST only, with presence targeting and the movie negatives, never the core of the budget.

Put together, the qualified sleepaway demand he can buy in his home states is roughly 6,000 to 8,000 searches a month in an average month. That is the constraint. CPCs of $3 to $6 are not the problem. The problem is that there are not that many clicks to buy.

### When the searches happen

Summed monthly searches for the geo, cost, near-me, session and age groups across the four states:

| Month | Searches |
|---|---|
| Sep 2026 | 11,120 |
| Oct 2025 | 13,650 |
| Nov 2025 | 13,330 |
| Dec 2025 | 16,850 |
| Jan 2026 | 31,500 |
| Feb 2026 | 28,110 |
| Mar 2026 | 32,530 |
| Apr 2026 | 25,130 |
| May 2026 | 30,740 |
| Jun 2026 | 51,540 |
| Jul 2026 | 50,350 |
| Aug 2026 | 25,780 |

Two waves. January through March is the enrollment-decision wave for parents choosing next summer, and it is more than double the fall. June and July are the biggest, but that wave is mixed: current families, late deciders, and day-camp overflow. Right now, in November, is the cheapest and quietest time of year. Build and test now, spend in January through March, and keep a small always-on presence in June and July for next-year tours and Rookie Days.

Brand searches for Camp Lindenmere are 51 percent June through August. Those are current families looking for the login, photos and the packing list, not prospects.

### The brand term

"camp lindenmere" gets about 2,900 searches a month in the US and 2,310 in the four states, with an average CPC of $7.22 and a top-of-page bid range of $1.67 to $5.13. A CPC that high on a camp's own name means someone is bidding on it, which is normal in this category. A brand campaign at a low cap will cost cents per click, protect the top spot, and give him the cleanest conversion data he will ever get. The search-terms report on that campaign also shows what people ask about the camp: "is camp lindenmere jewish" (40 a month), "camp lindenmere cost" (40), "camp lindenmere reviews" (60), "rookie day", "bus", "packing list". Every one of those is a page the site should answer plainly.

Two brand queries, "camp lindenmere bus crash" and "camp lindenmere stabbing", show up with 10 searches a month or fewer. I did not verify what they refer to. He should search them himself and make sure the first result is the camp's own answer, not a forum.

## Clever angles that should cost less per enrolled camper

Ranked by how much cheaper the click is and how well the camp can answer it.

1. **Activity plus overnight at $1 to $3 a click.** "overnight basketball camp near me", "horse sleepaway camp", "overnight soccer camp near me", "volleyball sleepaway camp", "lacrosse sleep away camp", "overnight tennis camp". These run half the price of the geo terms and the camp actually offers them through the Sports Academy, horseback riding, and the all-choice program. Each needs its own landing page with the activity in the headline and the camp's real photos. Most Poconos camps do not buy these terms because they think of themselves as traditional camps.
2. **The cost guide.** "sleepaway camp cost", "how much is sleepaway camp", "average cost of sleepaway camp" together run about 200 a month in the four states, at $1.70 to $10 a click. The site already lists tuition, which most competitors bury behind a form. A page titled "What sleepaway camp costs in 2027, and what is included" with the camp's real numbers, the deposit schedule, the sibling discount, and a comparison of session lengths will rank organically within a few months and convert better than the tuition table. The same pattern (a priced guide page) was the best converting page on Khrystyna's site.
3. **Session length.** "2 week sleepaway camp" and "one week sleepaway camp" run 50 a month each in the four states. The camp does not sell those. "3 week sleepaway camp" and "7 week sleepaway camp" are 30 to 40 each and the camp sells exactly those. A page that says "Three weeks or four weeks: which session fits a first-time camper" catches both the three-week searcher and the parent who wanted two weeks and will take three.
4. **Teens.** "sleepaway camp for teens" is 130 a month in the four states at $9.41, expensive, but "overnight summer camp for teens near me" is 40 a month at $0.28. The Sports Academy and the 11th grade Leadership Training discount are the answer. Teen searches also come from the teen, not the parent, so the page needs to speak to both.
5. **Co-ed.** "coed sleepaway camp" runs 70 a month in the four states at $1.13. Several big Poconos camps are single-gender (Bryn Mawr, Camp Wayne). Cheap, exact intent, and the camp qualifies.
6. **The packing list page is already the camp's best organic asset.** It ranks in the top ten for about twenty queries ("summer camp packing list" 590 a month, "sleepaway camp essentials", "what to pack for sleepaway camp"). It brings in parents of campers at other camps. Add a soft call to action on that page: "Not at Lindenmere yet? See 2027 dates" plus a Rookie Days mention. Zero cost.
7. **Competitor brand searches are bigger than the category.** Camp Canadensis 4,400 a month, Tyler Hill 4,400, Lohikan 3,600, Towanda 2,400, Weequahic 2,400, Island Lake (camp) 2,400, against Lindenmere's 2,900. Google allows bidding on a competitor's name as long as the name is not in the ad. CPCs run $5 to $28, so this is a last resort, but the comparison is useful: brand search volume is the cheapest public measure of each camp's marketing reach, and his is mid-pack.
8. **Rookie Days and camp tours as the conversion event.** Nobody searches "rookie day" (10 a month on the brand). But every ad above should send to a page whose primary action is "book a tour" or "Rookie Days July 17 or 31", not "enroll". A $10,000 purchase does not happen from a click. A tour booking does.

## What a Google Ads test would cost, and what to compare

The arithmetic he can check against his old data. The percentages below are assumptions to replace with his own numbers.

- Qualified searches available in the four states: about 6,000 a month off-season, 12,000 to 15,000 in January through March.
- At a 20 percent impression share and a 5 percent click-through rate, that is 60 to 150 clicks a month.
- At a $4.50 average CPC, that is $270 to $675 a month.
- If 4 percent of clicks become an inquiry or tour request, that is 2 to 6 inquiries a month.
- If one in four inquiries enrolls, that is 0.5 to 1.5 campers a month, at $8,150 to $15,000 tuition each.

So the cost per enrolled camper on search is in the $450 to $1,350 range if those rates hold, against roughly $10,000 of tuition. Search is cheap per camper. It is just not big. It will not fill a camp. Referral, camp advisors, and the alumni list will, and search should be sized as a precise supplement, not the main engine.

`CAC-LTV.md` puts that in context. A new camper's first-summer contribution is roughly $3,400 to $9,000 depending on session and margin, and lifetime tuition at a 75 percent return rate is $39,000 to $60,000. Any channel under about $3,000 per enrolled camper pays back in the first season, and every channel in this plan is well under that.

Numbers from his past campaigns to bring tomorrow, so the two can be compared: average CPC, click-through rate, which geos he targeted, which keywords spent the most, whether Display Network and search partners were on (they are on by default and wasted money in both prior projects), and how many inquiries or tours came from ads versus the site count.

## Recommended first structure, if he wants to run search

Seven campaigns, one per intent, each with its own cap, presence-only targeting (people physically in the geo, not "interested in"), Display Network off, search partners off.

| Campaign | Geo | Keywords from the shortlist | Cap | Landing page |
|---|---|---|---|---|
| Brand | NY, NJ, CT, PA | camp lindenmere, lindenmere camp, plus cost, reviews, tour, rookie days variants | $2.00 | Home |
| Poconos and PA | NY, NJ, CT, PA | sleepaway camp pennsylvania, overnight camp pa, sleepaway camp poconos | $5.50 | A "Poconos sleepaway camp, 90 minutes from NYC" page |
| Home states | each state separately | sleepaway camp nj, sleepaway camp ny, overnight camp ct, sleepaway camp long island | $4.50 | Same page, headline swaps the state |
| Near me | NY metro, Philly metro | sleepaway camp near me, overnight summer camp near me | $4.00 | Same page |
| Activities | NY, NJ, CT, PA | overnight basketball camp, horse sleepaway camp, overnight soccer camp, volleyball, lacrosse, tennis | $3.00 | One page per activity |
| Cost and sessions | NY, NJ, CT, PA | sleepaway camp cost, how much is sleepaway camp, 3 week sleepaway camp, 7 week | $4.00 | The cost guide |
| Teens and co-ed | NY, NJ, CT, PA | sleepaway camp for teens, overnight camp for teens near me, coed sleepaway camp | $3.50 | Sports Academy page |

Campaign negatives for every campaign: movie, film, cast, 1983, actors, sequel, angela, ricky, survivor, return, streaming, watch, ending, trailer, day camp, free, jobs, hiring, salary, counselor, adult, church, christian, ymca, scout, scouts, weight loss, special needs, rv, campground, camping, tent, glamping, and every other state name. The full NEVER list in `KEYWORD-MASTER.csv` with its `stop` reason is the negative-keyword source.

Kill rule, the same one both prior projects used: after 14 days, pause any keyword whose click-through rate is under half the ad group median, and after 30 days pause any keyword with 2 or more clicks and no inquiry.

## Competitors

Full sweep in `competitors-2026-11-05.md` and `.csv`: 24 operating Poconos camps verified on their own sites, with source URLs per row.

### The one that matters most: Camp Lohikan closed

Camp Lohikan in Lake Como ran its final season in 2026. Its homepage is now a letter from the director: the property is sold to Camp Morasha (an Orthodox Jewish camp), the sale closes in 2027, and families are pointed to Lake Greeley and Camp Cayuga. Lohikan was a large co-ed camp drawing NY and NJ families, and "camp lohikan" still gets about 3,600 Google searches a month. Those families need a 2027 camp right now, and the two camps Lohikan recommended are budget-tier ($1,400 to $1,900 a week), not peers.

This is the cheapest acquisition in the region this winter:
- Bid on "camp lohikan", "lohikan camp", "camp lohikan alternatives", "camps like lohikan". Do not use the name in the ad. The headline is "Co-ed Poconos camp, ages 6 to 16, 2027 enrolling". Expect a few hundred clicks over the winter at a few dollars each, from people who already pay for a Poconos sleepaway camp.
- A landing page "For Lohikan families" with a director video call offer and a 72-hour enrollment credit (see below) does the rest.
- Lohikan alumni Facebook groups and the director's own letter are where those parents are talking. One respectful post from Lindenmere's director in those groups costs nothing.

### Price position

Lindenmere's full summer is $2,143 a week, tied 9th cheapest of 23. The premium co-ed peers (Towanda, Canadensis, Pine Forest, Wayne, Equinunk and Blue Ridge, Starlight, IHC, Trail's End, Tyler Hill) run $2,171 to $2,711 a week. Budget camps (Greeley, Cayuga, Shohola, Susquehannock, Akiba, Moshava) run $1,400 to $1,917. Island Lake is Lindenmere's twin: the same 2027 dates, $9,950 and $8,200 and $15,000, within $100 on every line. Lindenmere is priced as a premium camp at the bottom of the premium band, which is a good place to be if the site says so.

### What 14 of 24 competitors do that Lindenmere's site does not

1. **A dated early-enrollment price break.** Pine Forest $300 off by December 31. Chen-A-Wanda $300 early bird plus $500 for paying in full. Tyler Hill and Trail's End $500 off for enrolling within 72 hours of a visit. Equinunk and Blue Ridge $500 tiers. Westmont $200. Lindenmere shows none. A deadline is the single cheapest conversion tool in this category because the parent is already going to buy; the question is from whom and when.
2. **A priced overnight trial for first-timers.** Timber Tops one week $2,600. Lake Owego 12 days $5,600. Lake Greeley Rookie Week $1,700. Pine Forest a two-day Explorer weekend for $200 credited to tuition. Bryn Mawr, Trail's End and IHC run overnight weekends. Lindenmere's Rookie Days are day-only. A paid two-night trial credited to tuition converts the nervous six-year-old's parent that a day visit cannot.
3. **A first-timer guarantee.** Cayuga and Greeley refund prorated tuition if a first-time camper leaves early. Susquehannock gives a $500 first-time credit. Akiba locks the rate for life. Lindenmere's first-time page talks about support but makes no promise with a number in it.
4. **Director home visits and video chats, published as a schedule.** Weequahic posts a fall road-show by region, including NYC and Long Island on November 1 and 2. Canadensis visits every new camper. Towanda offers new-camper video chats. Equinunk and Blue Ridge run meetups in NYC. Lindenmere has "speak with a director" as a form.
5. **Recent content.** Six competitors have blog posts dated August to October 2026. Lindenmere's News page has no dated posts. Instagram: IHC 15.5K, Moshava 13.2K, Trail's End 12.4K, Tyler Hill 12K, Canadensis 11.7K, Lindenmere 6,736, 11th of 24. Only Trail's End and Akiba are on TikTok.

### Directories and advisors

KidsCamps $99 to $899 a year. MySummerCamps free basic listing, premium about $2 a day. Tips on Trips and Camps and Camp Connection are free to families and paid a referral fee by the camp on enrollment, amounts not published. ACA dues from $395. The 2026 NYC, Long Island, Westchester and NJ camp fair dates are in the brief; exhibitor fees are not published.

### Not verified

Facebook follower counts could not be fetched. Google Ads Transparency Center returned only a script shell, so nothing here says who is or is not running ads. Netimus blocked the fetch. Several deposits and trial prices are marked "not stated" rather than guessed.

## Caveats

- Volumes are Google's rounded averages. Anything under 100 a month is "exists", not a precise count.
- CPC and bid figures are national or state averages. His own account will show different numbers, usually lower on brand and higher on the head terms.
- The organic search tool never returns the paid-ads block, so this research cannot say who is currently advertising. The Google Ads Transparency Center can, but it needs a browser.
- The site states no religious or cultural affiliation. Forty people a month ask Google whether the camp is Jewish. Whatever the answer is, the site should say it.
