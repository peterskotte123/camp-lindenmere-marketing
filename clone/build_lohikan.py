"""Builds the Lohikan families guide and six single-activity pages into the clone.

Reuses the template, styles and helpers from build_pages.py. Activity facts are
taken from Lindenmere's own program pages as mirrored 2026-11-21. Lohikan facts
are limited to what its closure letter and Wikipedia state: the final season
was 2026 and the property was sold to Camp Morasha.
"""
import os

import build_pages as bp
from build_pages import CTA, NOTE, TUITION_TABLE, INCLUDED

ACTIVITY_LINKS = """
<p class="lm-links">
<a href="/basketball-sleepaway-camp/">Basketball</a>
<a href="/dance-sleepaway-camp/">Dance</a>
<a href="/gymnastics-sleepaway-camp/">Gymnastics</a>
<a href="/cheer-sleepaway-camp/">Cheer</a>
<a href="/theater-sleepaway-camp/">Theater</a>
<a href="/horseback-riding-sleepaway-camp/">Horseback riding</a>
<a href="/about/programs/">All 60+ activities</a>
</p>
"""


def activity(lead, what, where, extra, fit, source_link, source_name):
    return f"""
<p class="lm-lead">{lead}</p>

<h2>What campers do</h2>
{what}

<h2>Where it happens</h2>
{where}

<h2>How it fits into a camp day</h2>
<p>Lindenmere runs an All-Choice Program. Each day a camper picks three Majors and three Minors from more than 60 activities. {fit}</p>
{extra}

<h2>Who it is for</h2>
<p>Beginners and experienced campers train side by side, with instruction matched to each level. Nobody tries out, and nobody is locked in. A camper can go deep on one activity or mix it with anything else at camp.</p>

<h2>2027 sessions and tuition</h2>
{TUITION_TABLE}
<p>This activity is included in tuition, along with everything below:</p>
{INCLUDED}
<p>Camp is in Henryville, Pennsylvania, in the Pocono Mountains, about 90 miles from New York City and from Philadelphia. More detail is on <a href="{source_link}">{source_name}</a> and in <a href="/what-sleepaway-camp-costs-in-2027/">our 2027 cost guide</a>.</p>
{CTA.format(head="See it for yourself", body="Rookie Days are July 17 and July 31, 2027. Future campers choose two activities and spend the day at camp. Or ask a director anything.")}
<h2>More activities</h2>
{ACTIVITY_LINKS}
"""


P = {}

P["camps-like-camp-lohikan"] = dict(
    title="Camps Like Camp Lohikan: A Guide for Lohikan Families | Camp Lindenmere",
    desc="Camp Lohikan ran its last season in 2026. A guide for Lohikan families choosing a co-ed Poconos sleepaway camp for 2027, from the team at Camp Lindenmere.",
    h1="Camps Like Camp Lohikan: A Guide for Lohikan Families",
    hero="/wp-content/uploads/2022/01/Full-width-All-choice-scaled.jpg",
    body=f"""
<p class="lm-meta">Camp Lindenmere, November 2026. Camp Lindenmere is not affiliated with Camp Lohikan.</p>
<p class="lm-lead">Camp Lohikan ran its final season in the summer of 2026, and its property has been sold to Camp Morasha. If your family spent summers there, we are sorry. A camp is not easy to replace. This guide is for Lohikan parents choosing where their camper goes next.</p>

<h2>What to look for in the next camp</h2>
<p>Your camper already knows what they love about camp. Start there, and ask every camp you consider the same questions.</p>
<ul>
<li><b>Is it co-ed?</b> Siblings and friends of different genders can stay together.</li>
<li><b>Is it in the Poconos?</b> The drive, the bus and visiting day stay familiar.</li>
<li><b>Does my camper choose their activities?</b> Some camps set the schedule by bunk. Others let each camper pick.</li>
<li><b>Does it have their activity?</b> Ask to see the facility and who teaches it.</li>
<li><b>What session lengths are there?</b> Not every camp offers three or four weeks.</li>
<li><b>Can friends from Lohikan be placed together?</b> Ask directly. It matters more than anything else on this list.</li>
<li><b>What does tuition include?</b> Transportation, trips, laundry and specialty activities are extra at some camps.</li>
</ul>

<h2>How Camp Lindenmere answers those questions</h2>
<div class="lm-scroll"><table>
<tr><th>Question</th><th>Camp Lindenmere</th></tr>
<tr><td>Co-ed</td><td>Yes</td></tr>
<tr><td>Location</td><td>Henryville, Pennsylvania, in the Poconos, about 90 miles from New York City and from Philadelphia</td></tr>
<tr><td>Who sets the schedule</td><td>The camper. Three Majors and three Minors each day, chosen from more than 60 activities</td></tr>
<tr><td>Session lengths</td><td>Four weeks, three weeks, or the full seven-week summer</td></tr>
<tr><td>Transportation</td><td>Bus to and from camp is included, with stops in New York, New Jersey, Maryland and Pennsylvania</td></tr>
<tr><td>Campus</td><td>200 acres, every building air conditioned</td></tr>
<tr><td>History</td><td>Operating since 1935, owned by the Garfinkel family since 2006</td></tr>
</table></div>
{NOTE.format("Three things would make this page work, and only you can supply them. First, a named director and a direct line or calendar link for Lohikan families. Second, a clear promise about placing Lohikan friends in the same bunk, if you can make it. Third, any offer for Lohikan families, such as an enrollment credit with a date. Also add the ages you enroll: Lohikan took ages 6 to 15, and parents will check that first.")}

<h2>If your camper loved a particular activity</h2>
<div class="lm-scroll"><table>
<tr><th>Activity</th><th>At Lindenmere</th></tr>
<tr><td><a href="/basketball-sleepaway-camp/">Basketball</a></td><td>Three covered, lighted full courts, weekly in-camp tournaments and intercamp games</td></tr>
<tr><td><a href="/dance-sleepaway-camp/">Dance</a></td><td>Two air-conditioned studios. Hip-Hop, Jazz, Contemporary, Ballet and Tap</td></tr>
<tr><td><a href="/gymnastics-sleepaway-camp/">Gymnastics</a></td><td>A Gymnastics Pavilion with beam, uneven bars, vault, tumble track and floor</td></tr>
<tr><td><a href="/cheer-sleepaway-camp/">Cheer</a></td><td>A Cheerleading Major: stunting, tumbling and routines</td></tr>
<tr><td><a href="/theater-sleepaway-camp/">Theater</a></td><td>Two shows per session, and every camper who wants a part gets one</td></tr>
<tr><td><a href="/horseback-riding-sleepaway-camp/">Horseback riding</a></td><td>On camp grounds and included in tuition. Ten horses, one pony, two riding rings</td></tr>
</table></div>
<p>There is also a 20-station high ropes course with a 400-foot zip line, a Ninja Warrior course, two flying trapeze rigs, a lake with an aqua park, a heated pool, a skate park and five recording studios. The full list is on <a href="/about/programs/">the All-Choice Program page</a>.</p>

<h2>2027 dates and tuition</h2>
{TUITION_TABLE}
<p>Tuition is all-inclusive:</p>
{INCLUDED}
<p>Families get $200 off a younger sibling's tuition per session. Payment dates are on <a href="/dates-enrollment/">Dates and Tuition</a>.</p>

<h2>How to see camp before you decide</h2>
<ul>
<li><b>Talk to a director.</b> Tell us what your camper did at Lohikan and who their friends are. <a href="/contact/">Contact us</a></li>
<li><b>Take a tour.</b> A 1.5 to 2 hour visit built around what your camper wants to see. <a href="/next-steps/camp-tour/">Request a tour</a></li>
<li><b>Take the 360 degree tour from home</b> on <a href="/about/campus-location/">Campus and Location</a>.</li>
<li><b>Come to a Rookie Day</b> on July 17 or July 31, 2027. <a href="/dates-enrollment/rookie-days/">Rookie Day details</a></li>
</ul>

<h2>Changing camps: what parents ask</h2>
<h3>Will my camper be the only new one?</h3>
<p>No. We welcome first-time campers into every division each summer: Junior, Middle and Senior Camp.</p>
<h3>My camper is older. Is it too late to start somewhere new?</h3>
<p>Older campers settle in quickly when they spend the day on activities they chose. Campers entering 11th and 12th grade can join our Leadership Training program.</p>
<h3>Can we try a shorter summer first?</h3>
<p>Yes. Second Session is three weeks, July 25 to August 15, and includes Color War.</p>
{CTA.format(head="Lohikan family? Start with a conversation.", body="We would rather hear about your camper than send you a brochure. Ask us anything, including whether Lindenmere is the right fit.")}
""",
)

P["basketball-sleepaway-camp"] = dict(
    title="Basketball Sleepaway Camp in Pennsylvania | Camp Lindenmere",
    desc="A basketball sleepaway camp in the Poconos: three covered, lighted courts, daily instruction, weekly tournaments and intercamp games, inside a full summer camp.",
    h1="Basketball Sleepaway Camp in Pennsylvania",
    hero="/wp-content/uploads/2026/11/Athletics-2.png",
    body=activity(
        "At Camp Lindenmere a camper can play basketball every day of the summer and still do everything else camp offers. It is a full co-ed sleepaway camp in Pennsylvania's Poconos with a serious basketball program inside it.",
        "<ul><li>Offensive and defensive drills with counselors who coach to each camper's level</li><li>Weekly in-camp tournaments</li><li>Intercamp games against other camps</li><li>Evening games under the lights</li></ul>",
        "<p>Our basketball complexes have three covered full courts with lights for evening play. Two of them are pavilions with NBA-style hoops.</p>",
        "<h2>For players who want more</h2><p>The <a href=\"/camp-lindenmere-sports-academy/\">Lindenmere Sports Academy</a> offers advanced training and competition. Athletes can focus on one sport or sharpen several. The indoor Fitness Center adds strength and conditioning.</p>",
        "A camper who loves basketball can take it as a Major every morning and still spend afternoons at the lake, on the ropes course or in the recording studio.",
        "/about/programs/athletics-and-sports/", "Athletics and Sports"),
)

P["dance-sleepaway-camp"] = dict(
    title="Dance Sleepaway Camp in Pennsylvania | Camp Lindenmere",
    desc="A dance sleepaway camp in the Poconos: two air-conditioned studios, Hip-Hop, Jazz, Contemporary, Ballet and Tap, and a Visiting Day performance.",
    h1="Dance Sleepaway Camp in Pennsylvania",
    hero="/wp-content/uploads/2019/03/Dance-Color-War-scaled.jpg",
    body=activity(
        "Camp Lindenmere is a co-ed sleepaway camp in Pennsylvania's Poconos where a dancer can train every day, in real studios, and still have a whole summer of camp around it.",
        "<ul><li>Hip-Hop, Jazz, Contemporary, Ballet and Tap</li><li>Dance Flex, for campers who want to try every style</li><li>Choreographing routines with counselors</li><li>A performance for families on Visiting Day</li></ul>",
        "<p>Campers dance in two studios, each with central air conditioning, hardwood floors, wall mirrors, ballet barres and a full sound system.</p>",
        "<h2>Beyond the studio</h2><p>Dance is part of our <a href=\"/about/programs/performingarts/\">Performing Arts program</a>, alongside musical theater, voice, Rockshop bands and DJ. Dancers often add <a href=\"/theater-sleepaway-camp/\">theater</a>, <a href=\"/cheer-sleepaway-camp/\">cheer</a> or circus silks.</p>",
        "Dance Majors follow a structured curriculum through the session, so campers build toward the Visiting Day show instead of repeating a single class.",
        "/about/programs/performingarts/", "Performing Arts"),
)

P["gymnastics-sleepaway-camp"] = dict(
    title="Gymnastics Sleepaway Camp in Pennsylvania | Camp Lindenmere",
    desc="A gymnastics sleepaway camp in the Poconos: a Gymnastics Pavilion with beam, bars, vault, tumble track and floor, plus circus and flying trapeze next door.",
    h1="Gymnastics Sleepaway Camp in Pennsylvania",
    hero="/wp-content/uploads/2019/02/Gymnastics-1-e1795027185534.jpg",
    body=activity(
        "Camp Lindenmere is a co-ed sleepaway camp in Pennsylvania's Poconos with a dedicated Gymnastics Pavilion. Gymnasts of every level train daily and still get the lake, the ropes course and everything else at camp.",
        "<ul><li>Balance beam, uneven bars and vault</li><li>Floor routines and the tumble track</li><li>Mini trampoline</li><li>A showcase for families on Visiting Day</li></ul>",
        "<p>The Gymnastics Pavilion is connected to our Circus Pavilion, so there is always something happening. Coaches work on strength, confidence and flexibility at each camper's level.</p>",
        "<h2>Next door: circus and flying trapeze</h2><p>Gymnasts tend to love the Circus Pavilion: silks, hammocks, lyra and static trapeze. Camp also has two flying trapeze rigs where campers fly more than 30 feet up, with one-on-one instruction. See <a href=\"/about/programs/circus-gymnastics-and-trapeze/\">Circus, Gymnastics and Flying Trapeze</a>.</p>",
        "Gymnastics, Tumbling and Cheerleading are each offered as Majors, so a camper can choose one or combine them.",
        "/about/programs/circus-gymnastics-and-trapeze/", "Circus, Gymnastics and Flying Trapeze"),
)

P["cheer-sleepaway-camp"] = dict(
    title="Cheer Sleepaway Camp in Pennsylvania | Camp Lindenmere",
    desc="An overnight cheer camp in the Poconos: a Cheerleading Major with stunting, tumbling and routines, inside a full co-ed sleepaway camp.",
    h1="Cheer Sleepaway Camp in Pennsylvania",
    hero="/wp-content/uploads/2019/02/Gymnastics-1-e1795027185534.jpg",
    body=activity(
        "Most overnight cheer camps last a few days. At Camp Lindenmere, a co-ed sleepaway camp in Pennsylvania's Poconos, cheerleaders train through a three, four or seven week summer and get a full camp experience with it.",
        "<ul><li>Stunting</li><li>Tumbling, including work on the tumble track</li><li>High-energy routines</li><li>Performing for families on Visiting Day</li></ul>",
        "<p>Cheer runs in our Gymnastics Pavilion, which is connected to the Circus Pavilion. Cheerleaders share the space and the coaches with our gymnastics and tumbling programs.</p>",
        "<h2>What pairs well with cheer</h2><p><a href=\"/gymnastics-sleepaway-camp/\">Gymnastics and tumbling</a> build the skills cheer depends on. <a href=\"/dance-sleepaway-camp/\">Dance</a> adds Hip-Hop and Jazz in two studios. The Fitness Center offers strength and conditioning.</p>",
        "Cheerleading is its own Major, so a cheerleader can take it daily alongside tumbling or dance.",
        "/about/programs/circus-gymnastics-and-trapeze/", "Circus, Gymnastics and Flying Trapeze"),
)

P["theater-sleepaway-camp"] = dict(
    title="Theater Sleepaway Camp in Pennsylvania | Camp Lindenmere",
    desc="A theater sleepaway camp in the Poconos: two shows per session, a part for every camper who wants one, and backstage programs in costume, set, lighting and sound.",
    h1="Theater Sleepaway Camp in Pennsylvania",
    hero="/wp-content/uploads/2026/08/Theater.jpg",
    body=activity(
        "At Camp Lindenmere every camper who wants to be in the show gets a part, onstage or backstage. It is a co-ed sleepaway camp in Pennsylvania's Poconos with a full musical theater program.",
        "<ul><li>Two shows per session. Recent productions include Grease, Annie, Wicked, Moana and The Little Mermaid</li><li>Costume Design, Set Design, Stage Management, Lighting and Sound Engineering</li><li>Voice, where campers choose their songs and perform with piano accompaniment</li><li>Visiting Day performances</li></ul>",
        "<p>Shows are staged in our renovated, air-conditioned Rec Hall. Camp also has a custom stone amphitheater.</p>",
        "<h2>More for performers</h2><p>The <a href=\"/about/programs/performingarts/\">Performing Arts program</a> also includes <a href=\"/dance-sleepaway-camp/\">Dance</a> in two studios, Rockshop bands that rehearse and record in five studios, and DJ.</p>",
        "Theater Majors follow a curriculum that builds to the performance, so a camper who has never been on stage can be in a show by the end of the session.",
        "/about/programs/performingarts/", "Performing Arts"),
)

P["horseback-riding-sleepaway-camp"] = dict(
    title="Horseback Riding Sleepaway Camp in Pennsylvania | Camp Lindenmere",
    desc="A horseback riding sleepaway camp in the Poconos: English riding on camp grounds, ten horses and a pony, two rings, and riding included in tuition.",
    h1="Horseback Riding Sleepaway Camp in Pennsylvania",
    hero="/wp-content/uploads/2018/12/Horseback-2-scaled.jpg",
    body=activity(
        "At many camps riding means a bus to an outside stable and an extra fee. At Camp Lindenmere, a co-ed sleepaway camp in Pennsylvania's Poconos, the horses live on camp grounds and riding is included in tuition.",
        "<ul><li>English-style riding, from first lesson to jumping</li><li>Riding posture and control at each rider's level</li><li>Horse care and barn management</li><li>Helping look after an adopted horse for the summer</li><li>The Equestrian Showcase on Visiting Day</li></ul>",
        "<p>Our Equestrian Center has ten horses, one pony, two riding rings and seven dedicated staff.</p>",
        "",
        "Riding is offered daily as both a Major and a Minor, so a camper can ride every morning or try it once a week.",
        "/about/programs/horseback-riding/", "Horseback Riding"),
)


def main():
    tpl = open(bp.TEMPLATE, encoding="utf-8").read()
    for slug, p in P.items():
        assert os.path.isfile(os.path.join(bp.ROOT, p["hero"].lstrip("/"))), p["hero"]
        d = os.path.join(bp.ROOT, slug)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(bp.render(tpl, slug, p))
        print("wrote", f"/{slug}/")

    # link the activity pages from the Programs index so they are not orphans
    pp = os.path.join(bp.ROOT, "about", "programs", "index.html")
    c = open(pp, encoding="utf-8").read()
    if "lm-activity-links" not in c:
        block = f"""<section class="block-content block-bottom-spacing lm-activity-links"><div class="container"><div class="row"><div class="col-12 col-lg-8 offset-lg-2 lm-draft" style="font-family:'Montserrat',sans-serif;">
<h3>Activity guides</h3>{ACTIVITY_LINKS}
</div></div></div></section>"""
        i = c.index("</main>")
        open(pp, "w", encoding="utf-8").write(c[:i] + block + c[i:])
        print("linked activity pages from Programs")


if __name__ == "__main__":
    main()
