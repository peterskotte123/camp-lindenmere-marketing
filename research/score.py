#!/usr/bin/env python3
"""Score harvested keywords for Camp Lindenmere with a rubric adapted from Khrystyna2's keyword-method.md.
Reads deep/harvest.jsonl, writes deep/scored.csv. Run from this folder."""
import json, csv, re, pathlib, collections

IN = pathlib.Path("deep/harvest.jsonl"); OUT = pathlib.Path("deep/scored.csv")

CAMP = r"\b(sleepaway|sleep away|sleep-away|overnight|residential|summer camp|summer camps|camp|camps)\b"
PLACE_PA = r"\b(pennsylvania|pa|poconos|pocono|henryville|stroudsburg|scranton|wilkes barre|lehigh valley|wayne county|pike county|monroe county|northeast pa|ne pa|allentown)\b"
PLACE_HOME = r"\b(nyc|new york|ny|manhattan|brooklyn|queens|long island|westchester|new jersey|nj|jersey|connecticut|ct|philadelphia|philly|east coast|northeast|tri state|tri-state|north east|bergen county|morris county|bucks county|rockland|hudson valley)\b"
PLACE_OTHER = r"\b(california|ca|texas|tx|florida|fl|maine|new hampshire|vermont|massachusetts|ma|michigan|wisconsin|minnesota|north carolina|nc|virginia|georgia|colorado|ohio|illinois|chicago|los angeles|la|san diego|seattle|washington|oregon|arizona|canada|ontario|uk|london|england|australia|europe|switzerland|maryland|dc|delaware|rhode island|upstate|adirondacks|adirondack|catskills|berkshires|cape cod|new england|carolina|tennessee|kentucky|indiana|missouri|utah|nevada|hawaii|alaska|alabama|louisiana|oklahoma|kansas|nebraska|iowa|idaho|montana|wyoming|dakota|mississippi|arkansas|west virginia|new mexico|puerto rico|mexico|japan|france|germany|spain|italy|israel|poland|ireland|scotland)\b"
PRICE = r"\b(cost|costs|tuition|price|prices|pricing|rates|how much|fee|fees|expensive|per week|a week)\b"
BUDGET = r"\b(cheap|cheapest|affordable|budget|inexpensive|low cost|low-cost|under \$?\d+|discount|discounts|deals)\b"
AID = r"\b(scholarship|scholarships|financial aid|free|grant|grants|sliding scale|subsidized|low income)\b"
FIRST = r"\b(first time|first-time|first timer|ready for|what age|homesick|homesickness|packing list|pack|nervous|anxiety|tips|prepare|preparing|youngest|too young)\b"
SESSION = r"\b(\d\s?weeks?|one week|two week|three week|four week|seven week|short session|mini session|half summer|full summer|two weeks|three weeks|four weeks|week long|week-long|month long|month-long)\b"
AGE = r"\b(\d{1,2}\s?year olds?|\d{1,2}\s?yr olds?|age \d|ages \d|for kids|for children|for teens|for teenagers|teen|teens|teenager|teenagers|tween|tweens|middle school|high school|elementary|young kids|little kids|kindergarten|1st grade|2nd grade|3rd grade|4th grade|5th grade|6th grade|7th grade|8th grade|9th grade|10th grade|11th grade|rising)\b"
FORMAT = r"\b(coed|co-ed|co ed|girls|boys|all girls|all boys|traditional|private|luxury|elite|premier|top rated|best|aca|accredited)\b"
ACTIVITY = r"\b(trapeze|circus|horseback|horse|equestrian|riding|rock climbing|climbing|ropes|stem|robotics|coding|theater|theatre|drama|performing arts|musical|dance|art|arts|sports|basketball|soccer|lacrosse|tennis|baseball|hockey|football|volleyball|swimming|lake|waterski|wakeboard|sailing|kayak|archery|gymnastics|cheer|golf|fishing|mountain bike|biking|skate|adventure|outdoor|wilderness|nature|cooking|music|band|rock band|film|photography|video|gaming|esports|chess|science|academy)\b"
MOVIE = r"\b(movie|movies|film 1983|1983|cast|killer|angela|horror|remake|sequel|sequels|streaming|stream|watch|ending|explained|trailer|dvd|blu ray|bluray|netflix|hulu|tubi|shudder|poster|quotes|soundtrack|ricky|judy|aunt martha|felissa|rose|unhappy campers|teenage wasteland|return to|scene|scenes|kills|death|deaths|twist|reboot|wiki|imdb|rotten|review of|plot|actor|actress|book|novel|lyrics|song|meme|costume|tiktok|episode|series|season)\b"
DAY = r"\b(day camp|day camps|daycamp|after school|afterschool|daycare|day care|preschool|pre-k|prek)\b"
JOBS = r"\b(jobs|job|hiring|counselor jobs|counselors wanted|salary|salaries|pay|employment|work at|working at|staff application|apply|careers|career|internship|j1|j-1|visa)\b"
WRONG = r"\b(adult|adults|seniors|senior|family camp|church|christian|bible|catholic|baptist|methodist|lutheran|mormon|lds|muslim|islamic|boy scouts|girl scouts|scout|scouts|military|boot camp|bootcamp|weight loss|fat camp|fitness camp|rehab|troubled|wilderness therapy|therapeutic|special needs|autism|adhd|diabetes|bereavement|grief|cancer|disability|disabilities|college|university|band camp|cheer camp|gymnastics camp|rv|campground|campgrounds|camping|tent|cabin rental|cabins for rent|airbnb|glamping|hiking|trail|state park|national park|ymca|4h|4-h|jcc|chabad|yeshiva|ramah|bnai|b'nai|zionist|habonim|hebrew|kosher|orthodox|reform|conservative|usy|nfty|ncsy|bbyo|rvs|wedding|weddings|venue|retreat|retreats|conference|corporate|team building|horror camp|haunted)\b"
COMPETITOR = r"\b(lohikan|pine forest|canadensis|trail'?s end|trails end|towanda|bryn mawr|weequahic|starlight|tyler hill|camp wayne|lake greeley|greeley|island lake|chen-a-wanda|chen a wanda|chenawanda|indian head|camp ihc|netimus|lake owego|owego|timber tops|equinunk|blue ridge|westmont|shohola|cayuga|susquehanna|nock-a-mixon|nockamixon|moshava|saginaw|pocono trails|international sports training|watonka|akiba|pinemere|harlam|ramah|galil|kennebec|winadu|wicosuta|laurel|vega|modin|pinecliffe|tripp lake|takajo|manitou|androscoggin|skylemar|walden|mataponi|wekeela|cobbossee|micah|agawam|robin hood|fernwood|lenox|winaukee|pemigewassett|pemi|tecumseh|lake bryn|france|north star|cedar|birch|brant lake|chipinaw|schodack|walt whitman|pontiac|raquette|dudley|kinder ring|eisner|crane lake|camp airy|louise|nah-jee-wah|nah jee wah|cedar lake|poyntelle|lewis|camp lee|trinity|hillside|camp echo|echo lake|hidden valley|iroquois|tall timbers|nokomis|chateaugay|deerfoot|stony|willow|interlochen|french woods|long lake|buck'?s rock|bucks rock|stagedoor|blue star|camp wayne|timber lake|timberlake|camp ramaquois|ramaquois|camp ihc|pocono springs|camp social|lakota|camp lokanda|lokanda|camp jewell|camp hi ho|hiho|orchard hill|camp avoda|camp dakota|lake champion|camp nejeda|nejeda|camp canadensis|chateaugay)\b"
NEAR = r"\bnear me\b"
BRAND = r"\blindenmere\b"

def rnd(x):
    return round(x, 2) if isinstance(x, (int, float)) else x

def norm(k):
    k = k.lower().strip(); k = re.sub(r"[^a-z0-9$' ]+", " ", k); k = re.sub(r"\s+", " ", k).strip(); return k

def has(p, k): return re.search(p, k) is not None

def family(k):
    if has(BRAND, k): return "brand"
    if has(MOVIE, k) and has(r"sleepaway", k): return "movie"
    if has(COMPETITOR, k): return "competitor"
    if has(JOBS, k): return "staff"
    if has(DAY, k): return "day camp"
    if has(PRICE, k) or has(BUDGET, k) or has(AID, k): return "cost"
    if has(FIRST, k): return "first timer"
    if has(SESSION, k): return "session length"
    if has(PLACE_PA, k): return "pa poconos"
    if has(PLACE_HOME, k): return "home geo"
    if has(ACTIVITY, k): return "activity"
    if has(AGE, k): return "age"
    if has(FORMAT, k): return "format"
    if has(NEAR, k): return "near me"
    if has(r"\b(sleepaway|sleep away|overnight|residential)\b", k): return "generic sleepaway"
    return "other"

def score(k):
    s = 0; flags = []; stop = None
    camp = has(CAMP, k)
    sleep = has(r"\b(sleepaway|sleep away|sleep-away|overnight|residential)\b", k)
    # intent tier
    if sleep and (has(PLACE_PA, k) or has(PLACE_HOME, k) or has(FORMAT, k) or has(SESSION, k) or has(AGE, k) or has(ACTIVITY, k) or has(NEAR, k)): s += 4; flags.append("T1")
    elif has(PRICE, k) and camp: s += 3; flags.append("T2")
    elif sleep and len(k.split()) <= 4 and not has(FIRST, k): s += 3; flags.append("T1-head")
    elif sleep or (camp and has(FIRST, k)): s += 1; flags.append("T3")
    else: flags.append("T4")
    # locality
    if has(PLACE_PA, k): s += 3
    elif has(PLACE_HOME, k): s += 2
    elif has(NEAR, k): s += 1
    else: s -= 1
    if has(PLACE_OTHER, k): stop = "other region"
    # commercial signals
    if has(PRICE, k): s += 2
    if has(SESSION, k): s += 2; flags.append("session")
    if has(AGE, k): s += 1
    if has(ACTIVITY, k) and sleep: s += 1
    if has(r"\b(coed|co-ed|co ed)\b", k): s += 1
    if has(r"\b(best|top|top rated)\b", k): s -= 1
    if has(r"\b(reviews|review|reddit|forum|ratings)\b", k): s -= 3
    if has(BUDGET, k): s -= 3; flags.append("budget")
    if has(AID, k): s -= 4; flags.append("aid")
    if has(r"\b(jewish|jew|judaism|shabbat)\b", k): s -= 2; flags.append("confirm-affiliation")
    if has(r"\b(20\d\d)\b", k) and not has(r"\b(2027|2028)\b", k): s -= 3; flags.append("stale-year")
    # hard stops
    if has(MOVIE, k): stop = "movie"
    if has(r"\bsleepaway camp\b", k) and has(r"\b(film|films|ii|iii|iv|2|3|4|actors|actor|return|survivor|part|original|full|free online|online|123|yts|blu|vhs|runtime|rating|rated|year|release|released|summary|synopsis|characters|character|director|trivia|facts|true story|based on|location|filmed|where was)\b", k) and not has(SESSION, k): stop = "movie"
    if has(DAY, k) and not sleep: stop = "day camp"
    if has(WRONG, k): stop = "wrong offer"
    if has(COMPETITOR, k): stop = "competitor brand"
    if has(JOBS, k): stop = "staff recruiting"
    if has(BRAND, k): stop = None; s = 20; flags.append("brand")
    if not camp and not sleep: stop = stop or "no camp word"
    return s, flags, stop

def main():
    best = {}
    for line in IN.read_text().splitlines():
        r = json.loads(line); k = norm(r.get("keyword") or "")
        if not k: continue
        if k not in best or (r.get("search_volume") or 0) > (best[k].get("search_volume") or 0):
            r["keyword"] = k; best[k] = r
    rows = []
    for k, r in best.items():
        s, flags, stop = score(k)
        verdict = "NEVER" if stop else ("ADD NOW" if s >= 8 else "TEST" if s >= 4 else "NEVER")
        ms = r.get("monthly_searches") or []
        peak = max(ms, key=lambda m: m.get("search_volume") or 0) if ms else None
        rows.append({"keyword": k, "family": family(k), "verdict": verdict, "score": s, "stop": stop or "", "flags": " ".join(flags),
                     "us_volume": r.get("search_volume"), "us_cpc": rnd(r.get("cpc")), "competition": r.get("competition_level"),
                     "bid_low": rnd(r.get("low_top_of_page_bid")), "bid_high": rnd(r.get("high_top_of_page_bid")), "intent": r.get("intent"),
                     "peak_month": f"{peak['year']}-{peak['month']:02d}" if peak else "", "peak_volume": peak.get("search_volume") if peak else "",
                     "source": r.get("source"), "seed": r.get("seed")})
    rows.sort(key=lambda x: (x["verdict"] != "ADD NOW", x["verdict"] != "TEST", -x["score"], -(x["us_volume"] or 0)))
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    c = collections.Counter(r["verdict"] for r in rows); fam = collections.Counter(r["family"] for r in rows)
    print(len(rows), "unique keywords", dict(c)); print(dict(fam))

if __name__ == "__main__":
    main()
