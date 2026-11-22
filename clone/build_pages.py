"""Builds the draft location pages and blog posts into the local clone.

Every page is stamped from the live packing-list post so header, footer and
theme match the real site. Facts come from the camp's own pages (dates and
tuition, sessions, directions, campus) as mirrored on 2026-11-21. Anything the
camp must supply is in a visible "Draft note" box. Re-run safely: it rewrites
its own pages and only patches the blog index and menu once.
"""
import glob
import html
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "camplindenmere.com")
TEMPLATE = os.path.join(ROOT, "summer-camp-packing-list-the-ultimate-parent-checklist", "index.html")

CSS = """
<style>
.lm-draft p, .lm-draft li, .lm-draft td, .lm-draft th { font-family: 'Montserrat', sans-serif; }
.lm-draft h2 { font-size: 30px; margin: 44px 0 14px; color: #0C2340; }
.lm-draft h3 { font-size: 22px; margin: 30px 0 10px; color: #0C2340; }
.lm-draft ul { margin: 0 0 18px 20px; }
.lm-draft li { margin-bottom: 6px; }
.lm-draft table { width: 100%; border-collapse: collapse; margin: 14px 0 24px; }
.lm-draft th { background: #0C2340; color: #fff; text-align: left; padding: 10px 12px; font-size: 14px; }
.lm-draft td { padding: 10px 12px; border-bottom: 1px solid #e3e6ea; font-size: 16px; }
.lm-draft td.num, .lm-draft th.num { text-align: right; white-space: nowrap; }
.lm-draft .lm-scroll { overflow-x: auto; }
.lm-draft .lm-lead { font-size: 20px; line-height: 1.5; }
.lm-draft .lm-facts { display: flex; flex-wrap: wrap; gap: 12px; margin: 22px 0 8px; padding: 0; list-style: none; }
.lm-draft .lm-facts li { flex: 1 1 180px; background: #f0f4f7; border-left: 4px solid #00AFD7; padding: 12px 14px; margin: 0; }
.lm-draft .lm-facts b { display: block; font-size: 22px; color: #0C2340; }
.lm-draft .lm-cta { background: #0C2340; color: #fff; padding: 28px 26px; margin: 40px 0 10px; }
.lm-draft .lm-cta h3 { color: #fff; margin-top: 0; }
.lm-draft .lm-cta p { color: #fff; }
.lm-draft .lm-btn { display: inline-block; background: #78BE20; color: #fff !important; font-weight: 700; text-transform: uppercase; letter-spacing: .04em; padding: 13px 22px; margin: 6px 10px 0 0; text-decoration: none; }
.lm-draft .lm-btn.alt { background: #00AFD7; }
.lm-draft .lm-note { border: 2px dashed #c4571a; background: #fff7f0; padding: 12px 16px; margin: 22px 0; font-size: 15px; }
.lm-draft .lm-note b { color: #c4571a; }
.lm-draft .lm-meta { color: #5f6d66; font-size: 14px; margin-bottom: 4px; }
.lm-draft .lm-links a { display: inline-block; margin: 0 14px 8px 0; }
</style>
"""

CTA = """
<div class="lm-cta">
  <h3>{head}</h3>
  <p>{body}</p>
  <a class="lm-btn" href="/dates-enrollment/">2027 dates and tuition</a>
  <a class="lm-btn alt" href="/next-steps/camp-tour/">Request a camp tour</a>
  <a class="lm-btn alt" href="/contact/">Talk to a director</a>
</div>
"""

NOTE = '<div class="lm-note"><b>Draft note for Lewis:</b> {}</div>'

TUITION_TABLE = """
<div class="lm-scroll"><table>
<tr><th>Session</th><th>2027 dates</th><th class="num">Tuition</th><th class="num">Per week</th><th class="num">Per day</th></tr>
<tr><td>Session 1, four weeks</td><td>June 27 to July 25</td><td class="num">$9,850</td><td class="num">$2,463</td><td class="num">$352</td></tr>
<tr><td>Session 2, three weeks</td><td>July 25 to August 15</td><td class="num">$8,150</td><td class="num">$2,717</td><td class="num">$388</td></tr>
<tr><td>Full summer, seven weeks</td><td>June 27 to August 15</td><td class="num">$15,000</td><td class="num">$2,143</td><td class="num">$306</td></tr>
</table></div>
"""

INCLUDED = """
<ul>
<li>Every activity at camp, horseback riding included</li>
<li>All Thursday trip days (spending money is extra)</li>
<li>Bus transportation to and from camp, with stops in New York, New Jersey, Maryland and Pennsylvania</li>
<li>All canteen costs</li>
<li>Weekly laundry service</li>
</ul>
"""

LOCAL_LINKS = """
<h2>Coming from somewhere else?</h2>
<p class="lm-links">
<a href="/sleepaway-camp-new-york/">New York</a>
<a href="/sleepaway-camp-near-nyc-long-island/">New York City and Long Island</a>
<a href="/sleepaway-camp-new-jersey/">New Jersey</a>
<a href="/sleepaway-camp-connecticut/">Connecticut</a>
<a href="/current-families/directions-lodging/">Full driving directions</a>
</p>
"""


def local_page(place, lead, route, bus, why, note):
    return f"""
<p class="lm-lead">{lead}</p>
<ul class="lm-facts">
<li><b>About 90 miles</b>from New York City and from Philadelphia</li>
<li><b>200 acres</b>in Pennsylvania's Pocono Mountains</li>
<li><b>3, 4 or 7 weeks</b>three session lengths in 2027</li>
<li><b>Since 1935</b>family owned by the Garfinkels since 2006</li>
</ul>

<h2>Getting to camp from {place}</h2>
<p>{route}</p>
<p>{bus}</p>
{NOTE.format(note)}

<h2>Why {place} families choose a Poconos camp</h2>
{why}

<h2>What a summer at Lindenmere looks like</h2>
<p>Lindenmere runs an All-Choice Program. Campers build their own schedule, picking three Majors and three Minors each day from more than 60 activities. Mornings go deep on what they love. Afternoons are for trying something new.</p>
<ul>
<li><b>Sports:</b> three lighted, covered basketball courts, two soccer fields, six tennis courts, a covered hockey arena, beach volleyball and a driving range</li>
<li><b>Adventure:</b> a 20-station high ropes course, a 50-foot climbing wall, a custom Ninja Warrior course, a skate park and three horseback riding arenas</li>
<li><b>Water:</b> a lake with a sand beach and aqua park, and a heated pool with two slides</li>
<li><b>Arts and innovation:</b> a theater, a circus pavilion with two flying trapezes, five music studios and an innovation center</li>
</ul>
<p>Every building on campus is air conditioned. See the full list on <a href="/about/campus-location/">Campus and Location</a> and <a href="/about/programs/">the All-Choice Program</a>.</p>

<h2>2027 sessions and tuition</h2>
{TUITION_TABLE}
<p>Tuition is all-inclusive:</p>
{INCLUDED}
<p>Families get $200 off a younger sibling's tuition per session. The payment schedule is on <a href="/dates-enrollment/">Dates and Tuition</a>, and <a href="/what-sleepaway-camp-costs-in-2027/">our cost guide</a> explains what the numbers mean.</p>

<h2>See camp before you decide</h2>
<ul>
<li><b>Rookie Days:</b> Saturday, July 17 and Saturday, July 31, 2027. Future campers pick two activities and spend the day at camp while parents tour with our team. <a href="/dates-enrollment/rookie-days/">Rookie Day details</a></li>
<li><b>Personal tours:</b> a 1.5 to 2 hour walk through the parts of camp your child cares about most. <a href="/next-steps/camp-tour/">Request a tour</a></li>
<li><b>From home:</b> the <a href="/about/campus-location/">360 degree virtual tour</a></li>
</ul>
{CTA.format(head=f"Thinking about camp for summer 2027?", body="Start with the dates and tuition, or ask a director anything. We answer every family ourselves.")}
{LOCAL_LINKS}
"""


PAGES = {}

PAGES["sleepaway-camp-new-york"] = dict(
    title="Sleepaway Camp for New York Families | Camp Lindenmere, Poconos",
    desc="A co-ed sleepaway camp about 90 miles from New York City. Bus stops in New York, all-inclusive 2027 tuition, and 3, 4 or 7 week sessions in the Poconos.",
    h1="Sleepaway Camp for New York Families",
    hero="/wp-content/uploads/2022/01/Full-width-All-choice-scaled.jpg",
    body=local_page(
        "New York",
        "Camp Lindenmere is a co-ed sleepaway camp in Pennsylvania's Pocono Mountains, about 90 miles from New York City. Families from the city, Westchester, Rockland and Long Island have been sending campers here for generations.",
        "From New York City and Long Island, take the George Washington Bridge to Route 80 West and stay on it into Pennsylvania. From Westchester, take the Tappan Zee Bridge to 287 South, then Route 80 West. From Rockland, take the Garden State Parkway or Route 287 to Route 80 West. Leave Route 80 at Exit 299, Tannersville, and camp is a few minutes up Route 715.",
        "Most New York campers do not drive at all. Bus transportation to and from camp is included in tuition, with stops in New York.",
        "<p>Sleepaway camps inside New York State sit mostly in the Catskills and the Adirondacks, three to five hours from the city. The Poconos are closer. Lindenmere is about 90 miles from Manhattan, which keeps visiting day and Rookie Days a day trip.</p><p>Second Session is three weeks, which many first-time campers choose before coming back for a longer summer.</p>",
        "Name the New York bus stop towns and add the next home-visit or meet-up dates in New York. If you can share roughly how many current families come from New York, one sentence with that number is the strongest line on this page.",
    ),
)

PAGES["sleepaway-camp-near-nyc-long-island"] = dict(
    title="Sleepaway Camp Near NYC and Long Island | Camp Lindenmere",
    desc="Looking for a sleepaway camp near NYC? Camp Lindenmere is about 90 miles from Manhattan in the Poconos, with bus stops in New York and all-inclusive tuition.",
    h1="A Sleepaway Camp Near NYC and Long Island",
    hero="/wp-content/uploads/2023/01/Untitled-design-4-1536x768.png",
    body=local_page(
        "New York City and Long Island",
        "You will not find 200 acres of lakefront and woods inside the five boroughs. You will find them about 90 miles west. Camp Lindenmere is a co-ed sleepaway camp in the Poconos, less than a two-hour drive from Manhattan.",
        "Take the George Washington Bridge to Route 80 West and follow it into Pennsylvania to Exit 299, Tannersville. Turn onto Route 715 North and camp is about a mile and a half up the hill on the right. Long Island families take the same route once they reach the bridge.",
        "Bus transportation to and from camp is included in tuition, with stops in New York, so most city and Long Island campers ride with their bunkmates.",
        "<p>City kids get the things a city summer cannot offer: a lake with a sand beach, three horseback riding arenas, a high ropes course, a skate park and room to run. Long Island families get a camp close enough to reach in a morning, without summer traffic on the Expressway being part of the plan every weekend.</p><p>Because campers choose their own Majors and Minors each day, a child who lives for basketball and a child who lives for theater can both have the summer they want, in the same bunk.</p>",
        "Name the pickup points that serve Manhattan, Brooklyn, Queens and Long Island, and list the March 11, 2027 NYC alumni reunion or any prospective-family event in the city. Drive time from Long Island varies too much to state without your own number.",
    ),
)

PAGES["sleepaway-camp-new-jersey"] = dict(
    title="Sleepaway Camp for New Jersey Families | Camp Lindenmere, Poconos",
    desc="A co-ed sleepaway camp just over the Delaware from New Jersey. Straight out Route 80, bus stops in NJ, and 3, 4 or 7 week sessions with all-inclusive tuition.",
    h1="Sleepaway Camp for New Jersey Families",
    hero="/wp-content/uploads/2025/02/FX301315.jpg",
    body=local_page(
        "New Jersey",
        "For most of New Jersey, Camp Lindenmere is the sleepaway camp at the end of Route 80. Cross the Delaware Water Gap, drive a few more exits, and you are in 200 acres of Pocono woods and lakefront.",
        "Take the Garden State Parkway or Route 287 to Route 80 West. Stay on 80 across the Delaware into Pennsylvania and leave at Exit 299, Tannersville. Turn onto Route 715 North and camp is about a mile and a half up the hill on the right.",
        "Bus transportation to and from camp is included in tuition, with stops in New Jersey.",
        "<p>New Jersey has plenty of day camps and very few places to sleep away. The Poconos are the closest mountains with lakes, so this is where New Jersey families have sent campers for nearly a century.</p><p>Being this close matters most for younger and first-time campers. Rookie Days and visiting day are an easy day trip, and a three-week Second Session lets a new camper try sleepaway without committing to a whole summer.</p>",
        "Name the New Jersey bus stop towns and add any New Jersey home-visit dates. The live site has pages for Bergen County and Morris County that nothing links to. Fold their best lines into this page and redirect them here.",
    ),
)

PAGES["sleepaway-camp-connecticut"] = dict(
    title="Sleepaway Camp for Connecticut Families | Camp Lindenmere, Poconos",
    desc="A co-ed sleepaway camp in the Poconos for Connecticut families: I-84 West most of the way, all-inclusive tuition, and 3, 4 or 7 week sessions in 2027.",
    h1="Sleepaway Camp for Connecticut Families",
    hero="/wp-content/uploads/2021/12/Flagpole-scaled-1.jpeg",
    body=local_page(
        "Connecticut",
        "Connecticut families looking past the Berkshires find a different kind of camp in the Poconos. Camp Lindenmere is a co-ed, all-choice sleepaway camp on 200 acres in Henryville, Pennsylvania, reached almost entirely by I-84.",
        "Take I-84 West to I-380 South and leave at Exit 3, Mount Pocono. Turn left onto Route 940 East, then right onto Route 611 South at the light. After about five miles turn left onto Route 715 and camp is a mile up the hill.",
        "Tuition includes bus transportation with stops in New York, New Jersey, Maryland and Pennsylvania. There is no Connecticut stop listed today, so Connecticut families either drive or meet a New York bus.",
        "<p>New England camps tend to run a single seven-week season with a set schedule. Lindenmere offers three, four or seven weeks, and campers choose their own activities every day. That combination is hard to find closer to home.</p><p>Every building on campus is air conditioned, and the facilities are new or recently renovated.</p>",
        "Confirm whether a Connecticut or Westchester bus stop serves Fairfield County families, and add it here. If Connecticut enrollment is small, say which New York stop most Connecticut families use.",
    ),
)

PAGES["what-sleepaway-camp-costs-in-2027"] = dict(
    blog=True, date="Nov 21",
    title="What Sleepaway Camp Costs in 2027 | Camp Lindenmere",
    desc="Real 2027 sleepaway camp prices: tuition by session, cost per week and per day, what is included, what is extra, and how payment plans work.",
    h1="What Sleepaway Camp Costs in 2027",
    hero="/wp-content/uploads/2022/01/Full-width-All-choice-scaled.jpg",
    body=f"""
<p class="lm-meta">Camp Lindenmere, November 2026</p>
<p class="lm-lead">Most camp websites make you ask for the price. Here is ours, what it works out to per week and per day, what it covers, and how it compares.</p>

<h2>Our 2027 tuition</h2>
{TUITION_TABLE}
<p>The longer the stay, the lower the daily cost. A full summer costs about 13 percent less per day than a four-week session.</p>

<h2>What that price includes</h2>
{INCLUDED}
<p>When you compare camps, ask each one for this list. A lower tuition with separate charges for transportation, trips, laundry or riding can end up higher.</p>

<h2>What is extra</h2>
<ul>
<li>Spending money on trip days</li>
<li>A 3 percent fee if you pay by credit card. There is no fee for eCheck or check.</li>
<li>Clothing and gear. Our <a href="/summer-camp-packing-list-the-ultimate-parent-checklist/">packing list</a> shows what a camper needs.</li>
</ul>

<h2>How families pay</h2>
<p>A deposit holds the spot: $2,000 for one session or $3,000 for two. The balance is split into payments, and the earlier you enroll the more payments you get.</p>
<div class="lm-scroll"><table>
<tr><th>If you enroll</th><th>Balance is billed</th><th>In</th></tr>
<tr><td>Through October 31</td><td>November 15, January 15, March 15</td><td>Thirds</td></tr>
<tr><td>November 1 to January 1</td><td>January 15, March 15</td><td>Halves</td></tr>
<tr><td>January 1 to February 28</td><td>March 15, April 15</td><td>Halves</td></tr>
<tr><td>After March 1</td><td>April 15, May 15</td><td>Halves</td></tr>
</table></div>

<h2>Discounts</h2>
<ul>
<li><b>Siblings:</b> $200 off the younger sibling's tuition, per session</li>
<li><b>Leadership Training:</b> campers entering 11th grade receive 5 percent off</li>
</ul>

<h2>How this compares</h2>
<p>The American Camp Association's 2022 survey found the average overnight camp fee was about $173 a day. That average includes one-week nonprofit, scout and church camps. Private camps with full facilities and multi-week sessions cost more.</p>
<p>We reviewed the published 2027 rates of 23 Poconos sleepaway camps in November 2026. Full-summer tuition worked out to between about $1,400 and $2,700 a week. Lindenmere's full summer, at $2,143 a week, sits in the middle of that range.</p>

<h2>Can I use a tax credit or FSA?</h2>
<p>Usually not for overnight camp. We wrote a plain answer here: <a href="/is-sleepaway-camp-tax-deductible/">Is sleepaway camp tax deductible?</a></p>

<h2>Questions to ask any camp about cost</h2>
<ul>
<li>Is transportation included, and from where?</li>
<li>Are trips, laundry, canteen and specialty activities included?</li>
<li>What is the deposit, and is any of it refundable?</li>
<li>What is the payment schedule, and are there card fees?</li>
<li>Is there a sibling discount?</li>
<li>What happens to tuition if my child leaves early?</li>
</ul>
{NOTE.format("Confirm the comparison paragraph is something you want on the camp's own site. It uses our competitor sweep and names no camp. Also add your refund policy to the last list, since parents will ask you the same question.")}
{CTA.format(head="Want the numbers for your family?", body="Tell us how many campers and which session, and a director will walk you through the total, the payment dates and any sibling discount.")}
""",
)

PAGES["is-sleepaway-camp-tax-deductible"] = dict(
    blog=True, date="Nov 21",
    title="Is Sleepaway Camp Tax Deductible? | Camp Lindenmere",
    desc="Overnight camp does not qualify for the child care tax credit or a Dependent Care FSA. Day camp can. Here is the IRS rule in plain words and what does help.",
    h1="Is Sleepaway Camp Tax Deductible?",
    hero="/wp-content/uploads/2021/12/Flagpole-scaled-1.jpeg",
    body=f"""
<p class="lm-meta">Camp Lindenmere, November 2026</p>
<p class="lm-lead">Short answer: no. Overnight camp does not qualify for the Child and Dependent Care Credit, and you cannot pay for it from a Dependent Care FSA. Day camp often does qualify. Here is why, and what actually helps with the cost.</p>

<h2>What the IRS says</h2>
<p>The Child and Dependent Care Credit covers care that lets you work or look for work. IRS Publication 503 addresses camp directly: the cost of sending your child to an overnight camp is not considered a work-related expense. The cost of a day camp may be, even if the camp specializes in an activity such as soccer or computers.</p>
<p>You can read the rule in <a href="https://www.irs.gov/publications/p503" target="_blank" rel="noopener">IRS Publication 503</a> under "Care of a Qualifying Person".</p>

<h2>Does a Dependent Care FSA cover sleepaway camp?</h2>
<p>No. A Dependent Care FSA follows the same definition of eligible care. Day camp for a child under 13 generally qualifies. Overnight camp does not, including the daytime portion of it.</p>

<h2>Day camp and overnight camp, side by side</h2>
<div class="lm-scroll"><table>
<tr><th></th><th>Day camp</th><th>Overnight camp</th></tr>
<tr><td>Child and Dependent Care Credit</td><td>Can qualify if the care lets you work and your child is under 13</td><td>Does not qualify</td></tr>
<tr><td>Dependent Care FSA</td><td>Can qualify under the same rules</td><td>Does not qualify</td></tr>
<tr><td>Ordinary tax deduction</td><td>No</td><td>No</td></tr>
</table></div>

<h2>Are there any exceptions?</h2>
<p>Some programs with a specific medical or therapeutic purpose are treated differently, because part of the cost may count as a medical expense. A traditional sleepaway camp is not one of them. If you think your situation is unusual, ask a tax professional.</p>

<h2>What does help with the cost</h2>
<ul>
<li><b>Enroll early for more payments.</b> At Lindenmere, families who enroll through October 31 pay the balance in thirds, in November, January and March.</li>
<li><b>Pay by eCheck or check.</b> There is no fee, where credit cards carry a 3 percent fee.</li>
<li><b>Use the sibling discount.</b> $200 off the younger sibling's tuition per session.</li>
<li><b>Pick the session that fits.</b> Second Session is three weeks. A full summer has the lowest cost per day.</li>
<li><b>Compare what is included.</b> Our tuition covers transportation, trips, canteen, laundry and every activity.</li>
</ul>
<p>The full breakdown is in <a href="/what-sleepaway-camp-costs-in-2027/">What sleepaway camp costs in 2027</a>.</p>
<p><i>This article is general information, not tax advice. Rules change, so check the current IRS publication or ask your accountant.</i></p>
{CTA.format(head="Planning the budget for summer 2027?", body="See the tuition and payment dates, or talk through the options with a director.")}
""",
)

PAGES["what-age-is-best-for-sleepaway-camp"] = dict(
    blog=True, date="Nov 21",
    title="What Age Is Best for Sleepaway Camp? | Camp Lindenmere",
    desc="There is no single right age for sleepaway camp. Here are the signs a child is ready, the signs to wait a year, and low-risk ways to try it first.",
    h1="What Age Is Best for Sleepaway Camp?",
    hero="/wp-content/uploads/2019/01/ropes-course-girl-1.jpg",
    body=f"""
<p class="lm-meta">Camp Lindenmere, November 2026</p>
<p class="lm-lead">There is no single right age. Readiness shows up in what a child does, not in a birthday. We welcome first-time campers into every division each summer: Junior, Middle and Senior Camp.</p>

<h2>Signs your child is ready</h2>
<ul>
<li>They have slept away from home, at a grandparent's or a friend's, and it went fine</li>
<li>They manage the basics alone: showering, brushing teeth, getting dressed, keeping track of their things</li>
<li>They can ask an adult they do not know well for help</li>
<li>They are curious about camp, or asking about it, even if they are also nervous</li>
<li>They can get through a hard moment and recover</li>
</ul>
<p>Nervous and ready often look the same. A child who is excited and worried at once is usually ready.</p>

<h2>Signs to wait a year</h2>
<ul>
<li>Sleepovers still end with a late-night pickup most of the time</li>
<li>The idea is yours alone, and they are clearly not interested yet</li>
<li>A big change is happening at home this year, such as a move or a new school</li>
</ul>
<p>Waiting a year costs nothing. A first summer that starts when a child is ready is the one that turns into six more.</p>

<h2>Is the parent ready?</h2>
<p>This matters as much. Children take their cue from you. If you speak about camp with confidence, and avoid promising to pick them up if they are sad, they settle faster. It is normal to feel a mix of excitement and nerves yourself.</p>

<h2>Ways to try it first</h2>
<ul>
<li><b>Rookie Days.</b> Future campers spend a day at camp, choose two activities and eat lunch on the dining hall patio while parents tour. 2027 dates are July 17 and July 31. <a href="/dates-enrollment/rookie-days/">Rookie Day details</a></li>
<li><b>A camp tour.</b> A 1.5 to 2 hour visit built around what your child wants to see. <a href="/next-steps/camp-tour/">Request a tour</a></li>
<li><b>The shorter session.</b> Second Session is three weeks and includes Color War, which makes it a popular first summer.</li>
</ul>

<h2>What helps a first-time camper settle in</h2>
<ul>
<li>Choice. At Lindenmere campers pick three Majors and three Minors each day, so a new camper spends the day doing things they already like.</li>
<li>A sibling or a friend at camp, though most campers arrive knowing no one and leave with a bunk full of friends.</li>
<li>Practice at home: a few sleepovers, packing their own bag, writing a letter.</li>
</ul>
<p>More on how we welcome new campers is on <a href="/about/first-time-campers/">First-Time Campers</a>. When you are ready to plan, see <a href="/what-sleepaway-camp-costs-in-2027/">what camp costs in 2027</a>.</p>
{NOTE.format("Add the youngest age or grade you enroll and the age ranges for Junior, Middle and Senior Camp. The site does not state them anywhere I could find, and it is the first thing a parent reading this will want.")}
{CTA.format(head="Not sure if this is the year?", body="Tell a director about your child. We will give you an honest answer, including if we think next summer is the better start.")}
""",
)


def render(tpl, slug, p):
    s = tpl
    title = html.escape(p["title"], quote=False)
    desc = html.escape(p["desc"])
    s = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{desc}"', s, count=1)
    s = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="/{slug}/"', s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{html.escape(p["h1"])}"', s, count=1)
    s = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{desc}"', s, count=1)
    s = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="/{slug}/"', s, count=1)
    # the template's JSON-LD describes the packing-list post; drop it rather than mislabel the page
    s = re.sub(r'<script type="application/ld\+json" class="yoast-schema-graph">.*?</script>', "", s, count=1, flags=re.S)
    main = f"""<main class="page-content"><section class="page-hero page-hero--thumbnail">
    <img src="{p['hero']}" class="page-hero-image w-100 object-fit-cover" alt="{html.escape(p['h1'])} at Camp Lindenmere" decoding="async">
    <style>.page-hero-image{{object-position:center center;}}</style>
    <div class="container"><div class="row justify-content-center"><div class="col-12 col-lg-8">
      <div class="page-hero__content"><h1>{p['h1']}</h1></div>
    </div></div></div>
</section>
<section class="block-content block-bottom-spacing" style="margin-bottom: 60px;">
  <div class="container"><div class="row"><div class="col-12 col-md-12 col-lg-8 offset-lg-2 lm-draft">
  {CSS}
  <p>&nbsp;</p>
  {p['body']}
  </div></div></div>
</section>
</main>"""
    a, b = s.index("<main"), s.index("</main>") + 7
    return s[:a] + main + s[b:]


def card(slug, p):
    t = html.escape(p["h1"])
    return f"""<div class="story_item col-md-4">
    <div class="blog-img">
		<a href="/{slug}/" title="{t}"><img src="{p['hero']}" alt="{t}" loading="lazy" style="width:100%;aspect-ratio:16/9;object-fit:cover;"></a>
</div>
<div class="blog-title">
		<h4><a href="/{slug}/" title="{t}">{t}</a></h4>
        <div class="author-text">Camp Lindenmere | {p['date']}</div>
        </div>
		</div>
"""


def main():
    tpl = open(TEMPLATE, encoding="utf-8").read()
    for slug, p in PAGES.items():
        d = os.path.join(ROOT, slug)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(render(tpl, slug, p))
        print("wrote", f"/{slug}/")

    # blog index: new posts first
    bp = os.path.join(ROOT, "blog", "index.html")
    b = open(bp, encoding="utf-8").read()
    marker = "<div id='cptapagination-content'><div class=\"row\">"
    if "<!-- lm-new-posts -->" not in b:
        cards = "".join(card(s, p) for s, p in PAGES.items() if p.get("blog"))
        b = b.replace(marker, marker + "<!-- lm-new-posts -->" + cards, 1)
        open(bp, "w", encoding="utf-8").write(b)
        print("patched blog index")

    # Blog link beside News & Updates in the site menu, on every page
    news = re.compile(r'(<li id="menu-item-1046"[^>]*><a href="/news/">News &#038; Updates</a></li>)')
    n = 0
    for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        s = open(f, encoding="utf-8", errors="ignore").read()
        if 'class="menu-item lm-blog-link"' in s or not news.search(s):
            continue
        s = news.sub(r'\1<li class="menu-item lm-blog-link"><a href="/blog/">Blog</a></li>', s)
        open(f, "w", encoding="utf-8").write(s)
        n += 1
    print("menu link added on", n, "pages")

    # link the location pages from Campus & Location so they are not orphans
    cp = os.path.join(ROOT, "about", "campus-location", "index.html")
    c = open(cp, encoding="utf-8").read()
    if "lm-near-you" not in c:
        block = """<section class="block-content block-bottom-spacing lm-near-you"><div class="container"><div class="row"><div class="col-12 col-lg-8 offset-lg-2" style="font-family:'Montserrat',sans-serif;">
<h3>Sleepaway camp near you</h3>
<p><a href="/sleepaway-camp-new-york/">New York</a> &middot; <a href="/sleepaway-camp-near-nyc-long-island/">New York City and Long Island</a> &middot; <a href="/sleepaway-camp-new-jersey/">New Jersey</a> &middot; <a href="/sleepaway-camp-connecticut/">Connecticut</a></p>
</div></div></div></section>"""
        i = c.index("</main>")
        open(cp, "w", encoding="utf-8").write(c[:i] + block + c[i:])
        print("linked location pages from Campus & Location")


if __name__ == "__main__":
    main()
