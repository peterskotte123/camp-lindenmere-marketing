# Camp Lindenmere SEO plan

Prepared 2026-11-21. Sources: organic rankings recorded by DataForSEO on 2026-11-05 for camplindenmere.com and eight rival camps (`deep/ranks_by_domain.json`), three live Google results pages pulled 2026-11-21, and a full mirror of the site (`../clone/`).

Two caveats. Ranking positions are absolute, so they count ads, map packs and AI overviews and can understate organic position by a place or two. They are also one snapshot; Google Search Console should replace them as the source of truth once access is shared.

## What the data shows

### Two pages earn almost all the rankings

| Page | Keywords ranked | In the top 10 |
|---|---|---|
| Homepage | 98 | 23 |
| `/summer-camp-packing-list-the-ultimate-parent-checklist/` | 91 | 34 |
| `/about/programs/horseback-riding/` | 14 | 0 |
| Every other page combined | 35 | 6 |

Position spread across all 238 ranked keywords: 10 in positions 1 to 3, 55 in 4 to 10, 73 in 11 to 20, 100 beyond 20.

One blog post, published April 2026, ranks for as many searches as the homepage. The blog has seven posts, the last dated 2026-06-09, and none of the 97 mirrored pages links to the blog or to that post.

### The homepage is on page two for its largest keyword family

| Keyword | US searches / mo | Lindenmere | Best rival |
|---|---|---|---|
| sleep away camp in pa | 590 | 13 | Tyler Hill 6 |
| sleepaway camps in pennsylvania | 590 | 15 | Tyler Hill 8 |
| pennsylvania sleepaway camp | 590 | 16 | Weequahic 6, Tyler Hill 7 |
| summer camp pennsylvania | 590 | 17 | Lohikan 4 |
| sleepaway camps in pa | 590 | 22 | Tyler Hill 8, Lohikan 9 |
| summer camps in pa | 590 | 23 | Lohikan 9 |
| overnight camps in pa | 140 | 11 | Tyler Hill 9 |
| overnight summer camp pa | 140 | 25 | Tyler Hill 6 |

Google reports one volume per cluster of similar phrasings, so these rows overlap and should not be summed.

Homepage titles side by side:

| Camp | Title | H1 |
|---|---|---|
| Lindenmere | Coed Overnight Summer Camp Pennsylvania \| Camp Lindenmere | Today I will be |
| Tyler Hill | Tyler Hill Camp - Sleep Away Camp in Wayne County, PA | none |
| Weequahic | Sleepaway Camp in Pennsylvania - Best Summer at Camp Weequahic | Tradition, Values and Choice. Camp Weequahic, a sleep-away camp in Northeastern PA |

Lindenmere's title uses "overnight", not "sleepaway", and its main heading carries no keyword.

Where the homepage already wins: "sleepaway camps poconos" and "sleepaway camp poconos pa" at position 4, "summer camp poconos" at 7, "overnight camp in pa" and "best camps in pennsylvania" at 10.

### Lohikan's activity pages hold rankings that are about to open up

Camp Lohikan closed after the 2026 season. Its single-activity pages still rank:

| Keyword | US searches / mo | Lohikan position | Lohikan page |
|---|---|---|---|
| basketball sleepaway camp | 210 | 4 | /basketball.php |
| dance sleepaway camp | 170 | 7 | /dance.php |
| dance overnight camp | 170 | 10 | /dance.php |
| gymnastics sleepaway camp | 140 | 9 | /gym.php |
| overnight basketball camps near me | 140 | 4 | /basketball.php |
| cheer sleepaway camp | 90 | 3 | /cheer.php |

Lohikan's theater page holds ten more top-10 positions. Lindenmere ranks for none of these. Its program pages group several activities together (Athletics and Sports, Performing Arts, Circus, Gymnastics and Trapeze), which is why the one single-activity page, horseback riding, has 14 rankings and none in the top 10.

### What Google shows on the results pages (2026-11-21)

- **"camp lindenmere"**: AI overview, knowledge panel, Google reviews, short videos. Suggested questions include "How much is Camp Lindenmere?", "Where is Camp Lindenmere located?" and "What are the best sleepaway camps in Pennsylvania?". A thin "Campers Archives" page appears among the site's own results.
- **"sleepaway camps in pa"**: AI overview and a map pack above the organic results, which are mostly directories (Macaroni KID overnight camp lists, "Camps in Pennsylvania 2027") plus Camp Starlight.
- **"sleepaway camp cost"**: AI overview, forum threads, and "The Cost Of Sleepaway Camp Near New Jersey" at position 8. Suggested questions include "How much are sleepaway camps usually?" and "What age is best for sleepaway camp?".

### Lost and broken URLs

| URL | Status | Note |
|---|---|---|
| /next-steps/home-visit/ | 404 | Ranked for five searches, two in the top 10 |
| /health-and-safety-qa/ | 404 | Linked from the footer of every page as "Summer 2021 COVID-19 Guidelines" |
| /about/staff | 404 | |
| /next-steps/postcard | 404 | |
| /about/cabin-life/ | 301 to /about/bunk-life/ | Correct. Ranked 2 for "sleepaway camp cabins" |

## The plan, in priority order

### 1. Retitle the homepage and give it a real H1

- Title: `Sleepaway Camp in Pennsylvania's Poconos | Camp Lindenmere` (58 characters).
- H1: one sentence with the same phrase, for example "A co-ed sleepaway camp in Pennsylvania's Pocono Mountains, ages 6 to 16".
- Keep "Today I will be" as a styled tagline in a `div` or `p`, not the H1.
- Use "sleepaway" and "overnight" both in the first paragraph. Parents search both.
- Set the Open Graph title, which is currently "Home".

Expected effect: the cheapest move toward page one for the 590-a-month Pennsylvania family, where the page already ranks 13 to 23.

### 2. Fix the dead URLs

- 301 `/next-steps/home-visit/` to the page that now covers home visits or director calls.
- 301 `/health-and-safety-qa/` to `/about/health-safety/` and remove the 2021 COVID link from the footer.
- 301 `/about/staff` to `/staff/` and `/next-steps/postcard` to `/next-steps/`.

### 3. Build single-activity pages

One page per activity, each titled "[Activity] Sleepaway Camp in Pennsylvania | Camp Lindenmere":

1. Basketball
2. Dance
3. Gymnastics
4. Horseback riding (retitle and expand the existing page)
5. Theater
6. Cheer
7. Tennis
8. Soccer, lacrosse and volleyball, which have paid-search demand in `KEYWORD-SHORTLIST.csv`

Each page needs 400 to 600 words on what a camper actually does, the facilities, who teaches it, photos with alt text, the session dates and price, and one call to action. Link every one from the Programs page and from each other. These also serve as landing pages for the Activity ad groups, so the first screen should state the activity, the place and the price.

### 4. Restart the blog and link it

- Add Blog to the footer and link relevant posts from program and enrollment pages. Link the packing list from First Time Campers and Dates and Tuition.
- Add a "2027 dates and rates" call to action and an email capture for a printable PDF to the packing-list post, since it is the most-visited organic page after the homepage.
- One dated post a month. Next posts, by demand:

| Post | Evidence |
|---|---|
| What sleepaway camp costs in 2027 | A regional cost article ranks 8 for "sleepaway camp cost"; cost and tuition searches total about 1,180 a month in the four states |
| Is summer camp tax deductible | 320 US searches a month, no advertisers |
| What age is best for sleepaway camp | Shown as a suggested question on two of three results pages |
| Sleepaway camp for 6, 7 and 8 year olds | Age searches in `ANGLE-PROBES.csv` |
| Three weeks or four: which session fits a first-time camper | Session-length searches, about 440 a month in the four states |
| Sleepaway camps near NYC, New Jersey, Long Island | State and metro groups in the shortlist |

### 5. Answer the brand questions on the site

Add a short FAQ to the homepage and the Dates and Tuition page, marked up with FAQPage schema: how much it costs, where it is and how far from NYC and Philadelphia, ages, session lengths, whether the camp has a religious affiliation, and how to visit. The site has no FAQ, Review or AggregateRating schema today.

### 6. Google Business Profile

The Pennsylvania searches show a map pack above the organic results. Check the primary category, add 2026 photos and the tour video, post monthly, and ask every enrolled family for a review at the end of summer. The profile could not be inspected for this plan.

### 7. Directories and links

The results for "sleepaway camps in pa" are mostly directories. Get listed on ACA Find a Camp, Macaroni KID overnight camp lists for NJ, NY and PA editions, KidsCamps, MySummerCamps, and the regional "Camps in Pennsylvania" lists. Each is referral traffic and a link. Camp fair organizer sites and day-camp partner sites are the next tier.

### 8. Technical cleanup

- The contact page hero is a 6912 by 3456 PNG of 30 MB, and its `sizes` attribute is 100vw, so a 2x laptop display downloads the full file. Program banners uploaded November 2026 are about 5 MB each as PNG. Convert photos to JPG or WebP at 2000 px.
- Alt text is missing on 11 of 26 homepage images and 25 of 47 on Programs.
- Only 4 of 26 homepage images are lazy-loaded.
- Summer Sessions has no H1. Programs has two.
- Noindex thin archives (category, story category, location).
- Camper story pages are titled "Julia - Camp Lindenmere". Give each a descriptive title.
- "Winter Newsletter 2026" in the menu is a 32 MB PDF served with an HTML content type. Make it a normal page or a PDF link.

### Already in good shape

Titles and meta descriptions on the main pages, the Yoast sitemap index, canonicals, the www and http redirects, and LocalBusiness schema with address and coordinates.

## How to measure

1. Verify the site in Google Search Console and export queries and pages for the last 16 months as the baseline.
2. Track weekly: position for the eight Pennsylvania keywords above, clicks to the packing-list post, clicks to each new activity page.
3. Targets at 90 days: homepage in the top 10 for at least three of the 590-a-month Pennsylvania phrasings; two activity pages in the top 10; the cost guide indexed and ranking in the top 20.
4. Tie organic sessions to inquiries with the same first-touch capture and inquiry sheet described in `STRATEGY.md`.
