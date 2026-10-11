import json, math

def r0(x): return math.floor(x + 0.5)
def r2(x): return math.floor(x * 100 + 0.5) / 100
def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word): return str(n) + " " + word + ("" if n == 1 else "s")

STANDARDS = [
    ["single", 140, 200],
    ["single long", 155, 220],
    ["double", 200, 200],
    ["double long", 200, 220],
    ["king", 240, 220],
    ["super king", 260, 240],
]

def size_plan(bedW, bedL, drop):
    if not (bedW > 0) or not (bedL > 0) or not (drop > 0):
        return {"error": "bed and drop must be positive"}
    recW = r0(bedW + 2 * drop)
    recL = r0(bedL + drop)
    standard = "made to measure"
    for name, w, l in STANDARDS:
        if w >= recW and l >= recL:
            standard = name
            break
    return {"recW": recW, "recL": recL, "standard": standard}

def fill_plan(w, l, gsm):
    if not (w > 0) or not (l > 0) or not (gsm > 0):
        return {"error": "size and density must be positive"}
    areaM2 = r2(w * l / 10000)
    fillG = r0(w * l / 10000 * gsm)
    return {"areaM2": jsnum(areaM2), "fillG": fillG}

def night_cost_plan(price, years):
    if not (price > 0) or not (years > 0):
        return {"error": "price and years must be positive"}
    nights = r0(years * 365)
    perNight = r2(price / (years * 365))
    return {"nights": nights, "perNight": jsnum(perNight)}

def render_size(r, bedW, bedL, drop):
    s = ("A " + str(r0(bedW)) + " x " + str(r0(bedL)) + " bed with a " + str(r0(drop))
         + " cm drop needs about " + str(r["recW"]) + " x " + str(r["recL"]) + " cm - ")
    s += "no labeled standard covers it, made to measure." if r["standard"] == "made to measure" \
         else "the labeled standard pick is " + r["standard"] + "."
    return s

def render_fill(r, gsm):
    return ("That is " + str(r["areaM2"]) + " m² of duvet - at a labeled " + str(gsm)
            + " gsm it holds about " + str(r["fillG"]) + " g of fill.")

def render_night_cost(r, price, years):
    return ("At " + str(price) + " over " + plural(years, "year") + ", a duvet gives you "
            + plural(r["nights"], "night") + " - about " + str(r["perNight"]) + " a night.")

cases = []
for bedW, bedL, drop in [(140, 200, 20), (180, 200, 25), (200, 220, 30), (90, 190, 15),
                          (160, 200, 20), (0, 200, 20), (140, 0, 20), (140, 200, 0)]:
    r = size_plan(bedW, bedL, drop)
    cases.append({"fn": "sizePlan", "args": [bedW, bedL, drop], "result": r,
                  "render": None if "error" in r else render_size(r, bedW, bedL, drop)})
for w, l, gsm in [(200, 220, 150), (140, 200, 110), (260, 240, 300), (240, 220, 60),
                  (0, 200, 150), (200, 0, 150), (200, 220, 0)]:
    r = fill_plan(w, l, gsm)
    cases.append({"fn": "fillPlan", "args": [w, l, gsm], "result": r,
                  "render": None if "error" in r else render_fill(r, gsm)})
for price, years in [(120, 5), (80, 1), (250, 8), (45, 3), (0, 5), (120, 0)]:
    r = night_cost_plan(price, years)
    cases.append({"fn": "nightCostPlan", "args": [price, years], "result": r,
                  "render": None if "error" in r else render_night_cost(r, price, years)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
