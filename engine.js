(function (root) {
  "use strict";
  function r0(x) { return Math.round(x); }
  function r2(x) { return Math.round(x * 100) / 100; }
  function plural(n, word) { return n + " " + word + (n === 1 ? "" : "s"); }

  var STANDARDS = [
    ["single", 140, 200],
    ["single long", 155, 220],
    ["double", 200, 200],
    ["double long", 200, 220],
    ["king", 240, 220],
    ["super king", 260, 240]
  ];

  function sizePlan(bedWCm, bedLCm, dropCm) {
    if (!(bedWCm > 0) || !(bedLCm > 0) || !(dropCm > 0)) return { error: "bed and drop must be positive" };
    var recW = r0(bedWCm + 2 * dropCm);
    var recL = r0(bedLCm + dropCm);
    var standard = "made to measure";
    for (var i = 0; i < STANDARDS.length; i++) {
      if (STANDARDS[i][1] >= recW && STANDARDS[i][2] >= recL) { standard = STANDARDS[i][0]; break; }
    }
    return { recW: recW, recL: recL, standard: standard };
  }

  function fillPlan(widthCm, lengthCm, gsm) {
    if (!(widthCm > 0) || !(lengthCm > 0) || !(gsm > 0)) return { error: "size and density must be positive" };
    var areaM2 = r2(widthCm * lengthCm / 10000);
    var fillG = r0(widthCm * lengthCm / 10000 * gsm);
    return { areaM2: areaM2, fillG: fillG };
  }

  function nightCostPlan(price, years) {
    if (!(price > 0) || !(years > 0)) return { error: "price and years must be positive" };
    var nights = r0(years * 365);
    var perNight = r2(price / (years * 365));
    return { nights: nights, perNight: perNight };
  }

  function renderSize(r, bedW, bedL, drop) {
    var s = "A " + r0(bedW) + " x " + r0(bedL) + " bed with a " + r0(drop) + " cm drop needs about " + r.recW + " x " + r.recL + " cm - ";
    s += r.standard === "made to measure" ? "no labeled standard covers it, made to measure." : "the labeled standard pick is " + r.standard + ".";
    return s;
  }

  function renderFill(r, gsm) {
    return "That is " + r.areaM2 + " m² of duvet - at a labeled " + gsm + " gsm it holds about " + r.fillG + " g of fill.";
  }

  function renderNightCost(r, price, years) {
    return "At " + price + " over " + plural(years, "year") + ", a duvet gives you " + plural(r.nights, "night") + " - about " + r.perNight + " a night.";
  }

  var api = { sizePlan: sizePlan, fillPlan: fillPlan, nightCostPlan: nightCostPlan, renderSize: renderSize, renderFill: renderFill, renderNightCost: renderNightCost, STANDARDS: STANDARDS };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.DuvetMath = api;
})(this);
