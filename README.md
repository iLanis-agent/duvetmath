# Duvet math

The duvet size a bed and a drop really need, the grams of fill a cover holds, and what a duvet costs per night over its life. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/duvetmath/

## The three tools

- **Size plan** - `sizePlan(bedWCm, bedLCm, dropCm)`: needed dimensions and the labeled standard pick.
- **Fill plan** - `fillPlan(widthCm, lengthCm, gsm)`: area and grams of fill.
- **Night-cost plan** - `nightCostPlan(price, years)`: nights and cost per night.

## Labeled norms (illustrative references, not rules)

- Drop: 20 cm per side and at the foot. Fill densities: 60 gsm summer, 150 gsm mid-season, 300 gsm winter. Standard sizes: single 140 x 200, single long 155 x 220, double 200 x 200, double long 200 x 220, king 240 x 220, super king 260 x 240. Your bed, climate and duvet decide the real numbers.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (21 cases, 86 checks)

Regenerate the oracle expectations: `python3 oracle.py`
