# Camp Lindenmere: customer acquisition cost and lifetime value

Prepared 2026-11-05. Benchmarks come from American Camp Association (ACA) survey reports, a YouGov poll, and camp-marketing vendors. Every vendor number is labeled as such. The model uses Lindenmere's published 2027 tuition. The one number nobody outside the camp has is Lindenmere's own retention rate, and it moves every figure below more than anything else. Ask for it first.

## What the industry data says

### Retention

| Source | Figure |
|---|---|
| ACA CampCounts 2022, 189 camps, camps whose primary program is overnight | Mean 62 percent, median 67 percent of 2022 campers had also attended in 2021 |
| Same report, for-profit camps of any type | Mean 68 percent, median 69 percent |
| ACA 2017 Camper Enrollment Report, 295 camps | 80 percent of camps said over half their campers were returners. The most common bands were 60 to 69 percent (26 percent of camps) and 70 to 79 percent (23 percent) |
| Camp Ramaquois director presentation, informal | Sets the bar at about 90 percent for full-season resident camps |
| YouGov poll of US adults who attended sleepaway camp | 69 percent went more than one summer. 21 percent two summers, 17 percent three, 9 percent four, 8 percent five, 14 percent six or more |

The ACA figures count all overnight camps, including cheap one-week church and scout camps. Private seven-week Poconos camps sit at the top of the range. A 75 to 85 percent return rate is the right planning assumption for a camp like Lindenmere until the real number replaces it.

### Occupancy and price

ACA CampCounts 2022: overnight camps averaged 74 to 76 percent occupancy, median 99 percent, so half of overnight camps are full and the other half have real gaps. Mean daily per-person fee for overnight camp programs was $172.92. Lindenmere's full summer works out to $306 a day, and its four-week session to $352 a day, which is where the Poconos private camps sit.

### Margins

| Source | Figure |
|---|---|
| ACA 2018 Business of Camp survey | Overnight camps: median profit $10,500, average margin 3.4 percent, 16 percent lost money |
| ACA 2012 Operations report, cited by Campminder | For-profit resident camps about 10 percent, nonprofit about 2 percent |
| Jewish camp sector analysis, secondary | 7 percent operating margin, $6,280 revenue per camper |

Those are net margins after fixed costs. For acquisition decisions the number that matters is contribution per added camper, which is tuition minus the variable cost of one more child (food, supplies, trips, insurance, canteen, a share of counselor pay if a bunk opens). Nobody publishes that. Thirty-five percent is a cautious figure. Sixty percent is realistic when beds are empty and staff and facility are already paid for. The model shows both.

### Marketing spend and cost per camper

| Source | Figure |
|---|---|
| ACA 2011 operations data, cited by camp.marketing | Camps typically spend about 3 percent of expenses on marketing |
| camp.marketing, vendor | Recommends 6 to 10 percent of revenue for overnight camps under 200 campers; uses $400 per new camper in its worked example |
| financialmodelslab and businessplan-templates, vendors | $75 to $150 per camper as an industry baseline; under $100 as best practice; one example of $600 per camper |
| Karbon agency citing LocaliQ 2024 benchmarks, education category | Meta $26.31 per lead, 15.9 percent conversion; Google Search $77.48 per lead, 13.1 percent conversion |
| Enroll Media Group, Walden School camp, vendor case | 81 camp inquiries at $110 per lead |
| Belle Strategies, private school Facebook lead ads | $49 per lead, one enrollment per 20 leads, about $980 per enrollment |

The "$75 to $150 per camper" figures are blended across all campers including returners, for whom acquisition cost is near zero. Per new camper, the credible range from the case studies is $400 to $1,500.

### Word of mouth and referral

A 2015 ACA survey, cited by Campminder, found word of mouth the most important driver of new enrollments, with no percentage published. ACA-hosted parent research found 95 percent of resident-camp parents would recommend camp to a friend. Published referral credits at other camps run $200 to $500 per enrolled referral (Camp YJ $250, Camp Wise $200 rising with each referral). Camp advisor agencies such as Student Camp and Trip Advisors say they charge "a fixed percentage" of tuition to the camp and are free to families. The percentage is not published anywhere I could find, so the model shows 10 and 15 percent as assumptions. He should ask Tips on Trips and Camps and The Camp Experts for their rate directly.

## The lifetime value model

Expected summers per camper is 1 divided by (1 minus retention), capped at six because a camper who starts around age 10 ages out at 16. The cap is an assumption; the camp's own data on starting age replaces it.

| Retention | Expected summers |
|---|---|
| 60 percent (ACA overnight mean) | 2.5 |
| 68 percent (ACA for-profit mean) | 3.1 |
| 75 percent (planning floor for a private seven-week camp) | 4.0 |
| 85 percent (strong private camp) | 6.0 |

Gross lifetime tuition and the maximum sensible acquisition cost, using the common rule that lifetime contribution should be at least three times acquisition cost:

| Tuition | Retention | Summers | Lifetime tuition | Contribution at 35 percent | Contribution at 60 percent | Max CAC at 35 percent | Max CAC at 60 percent |
|---|---|---|---|---|---|---|---|
| 4-week $9,850 | 60% | 2.5 | $24,625 | $8,619 | $14,775 | $2,873 | $4,925 |
| 4-week $9,850 | 75% | 4.0 | $39,400 | $13,790 | $23,640 | $4,597 | $7,880 |
| 4-week $9,850 | 85% | 6.0 | $59,100 | $20,685 | $35,460 | $6,895 | $11,820 |
| Full summer $15,000 | 60% | 2.5 | $37,500 | $13,125 | $22,500 | $4,375 | $7,500 |
| Full summer $15,000 | 75% | 4.0 | $60,000 | $21,000 | $36,000 | $7,000 | $12,000 |
| Full summer $15,000 | 85% | 6.0 | $90,000 | $31,500 | $54,000 | $10,500 | $18,000 |
| Blended $11,500 | 60% | 2.5 | $28,750 | $10,062 | $17,250 | $3,354 | $5,750 |
| Blended $11,500 | 75% | 4.0 | $46,000 | $16,100 | $27,600 | $5,367 | $9,200 |
| Blended $11,500 | 85% | 6.0 | $69,000 | $24,150 | $41,400 | $8,050 | $13,800 |

The blended $11,500 is a guess at the average revenue per camper-summer across the session mix. The camp's finance person can replace it in one minute.

Three things the table leaves out, all of which push lifetime value up:

- **Siblings.** The camp's own $200 sibling discount exists because one enrolled family often sends a second child. If one in four families adds a sibling, lifetime value rises about 25 percent.
- **Referrals.** With 95 percent of parents willing to recommend and word of mouth the top source, a family that stays four summers plausibly brings one more family. That doubles the value of the first acquisition.
- **Staff and alumni.** Campers become CITs, counselors, and the parents of the next generation. Unpriced, but real for a camp operating since 1935.

### The first-summer payback test

Even ignoring everything after summer one, a new camper's first-summer contribution is $3,448 to $5,910 on a four-week session and $5,250 to $9,000 on a full summer. Any channel that lands a camper for under about $3,000 pays for itself in the first season. That is the simplest sentence to say tomorrow.

## Acquisition cost by channel

Estimates per enrolled new camper. Assumptions are stated; his own data replaces them.

| Channel | Estimated CAC | Basis | Notes |
|---|---|---|---|
| Referral credit to a current family | $250 to $500 | Published credits at other camps | Paid only on success. Cheapest channel that exists. Lindenmere has a Refer a Friend page; the credit amount is not shown. |
| Paid trial weekend credited to tuition | $150 to $300 | Pine Forest's $200 Explorer model | CAC is the weekend's variable cost. Converts the nervous parent of a 6 to 8 year old. |
| Early-enrollment credit | $300 to $500 plus leakage | 14 of 24 Poconos competitors | Paid to every new camper, and to returners if offered to them too. Treat as a deadline tool, not a discount. |
| Lohikan displaced families, search plus a landing page | $100 to $400 | 3,600 brand searches a month, a few dollars a click, high intent | A one-winter window. See HANDOFF. |
| Google search, qualified geo and activity terms | $450 to $1,350 | HANDOFF model: $4.50 CPC, 4 percent inquiry rate, 1 in 4 enrolls | Small volume. |
| Google search, benchmark method | $1,540 to $2,200 | $77 to $110 per lead, 1 in 20 leads enrolls | Worse case if landing pages are weak. |
| Meta lead ads with retargeting | $520 to $650 | $26 per lead benchmark, 1 in 20 to 25 enrolls | Needs the 360 tour video and real photos. |
| Camp advisor agency | $985 to $2,250 | 10 to 15 percent of first-summer tuition, assumed | Zero risk, paid only on enrollment. Rate must be confirmed. |
| Directory listings | $99 to $899 a year total | KidsCamps, MySummerCamps | CAC is the fee divided by whatever it produces; cheap to test. |
| Camp fairs in NYC, Long Island, Westchester, NJ | not published | Exhibitor fees not listed | Ask organizers; competitors attend. |

Every channel in the table costs less than the maximum CAC at any retention above 60 percent, and most pay back in the first summer. The constraint on growth is not the price of a camper. It is the number of families in the market in a given winter, and whether the site converts the ones who arrive.

## What to ask the camp for tomorrow

1. Retention: of 2026 campers, what percent attended in 2025, counting those who aged out as the ACA does.
2. Occupancy: beds filled versus capacity in 2026, by session.
3. Average revenue per camper-summer and the session mix.
4. Variable cost per camper-day, or the finance person's estimate of contribution margin.
5. How many 2026 new campers came from referrals, from advisors, from the website, from Rookie Days, from ads. If nobody tracked it, that tracking is the first marketing job.
6. The referral credit amount, and whether an early-enrollment credit has ever been offered.
7. Starting age of new campers, which sets the age-out cap.

With those seven numbers the tables above become his numbers instead of benchmarks.

## Sources

- ACA CampCounts 2022: https://www.acacamps.org/sites/default/files/2023-04/CampCounts2022_revised-4.11.23.pdf
- ACA 2017 Camper Enrollment Report: https://www.acacamps.org/sites/default/files/resource_library/2017_CamperEnrollmentReport.pdf
- ACA 2018 Business of Camp article: https://www.acacamps.org/article/camping-magazine/2018-business-camp-interesting-trends-otherwise
- ACA parent research on retention and word of mouth: https://acacamps.org/resource-library/articles/research-%E2%80%94-parents%E2%80%99-perspectives-resident-camp-experiences-dimensions-predict-retention-word-mouth
- Campminder on camp finance misconceptions: https://campminder.com/resources/the-most-common-misconceptions-about-managing-camp-finance/
- Campminder on lifelong camp customers: https://campminder.com/resources/the-3-greatest-reasons-to-recruit-lifelong-camp-customers/
- YouGov sleepaway camp poll: https://yougov.com/en-us/articles/52774-what-americans-think-about-sleepaway-summer-camp-poll
- Camp Ramaquois retention presentation: http://www.ramaquois.com/tristate/retention.pdf
- camp.marketing budget guide: https://camp.marketing/summer-camp-marketing-budget/
- financialmodelslab camp KPIs: https://financialmodelslab.com/blogs/kpi-metrics/kids-summer-camp
- businessplan-templates camp KPIs: https://businessplan-templates.com/blogs/metrics/kids-summer-camp
- Karbon agency citing LocaliQ benchmarks: https://karbonagency.com/summer-camp
- Enroll Media Group Walden case: https://www.enrollmediagroup.com/services/summer-camp-marketing
- Belle Strategies Facebook lead gen stats: https://bellestrategies.com/facebook-lead-gen-stats/
- Student Camp and Trip Advisors fee statement: http://www.campadvisors.com/about.html
- Camp YJ referral fee: https://campyj.org/cyj-families-2
- Camp Wise referral credits: https://campwise.org/dates-rates-2026/
