#!/usr/bin/env node
// 用 tools/review-ui.html 的真實 scanParas 掃各組語料，統計 R-014～R-021 觸發篇數。
// 用法：node tools/calib/calib.js [--samples] pos=<dir> neg=<neg.list> hum=<dir> ...
//   --samples：額外列出非 pos* 組（反例、人類對照）的觸發檔與命中說明，用來看誤報
"use strict";
const fs = require("fs");
const path = require("path");
const { loadReviewUi, clean, parseSets } = require("./lib");

const IDS = ["R-014", "R-015", "R-016", "R-017", "R-018", "R-019", "R-020", "R-021"];
const argv = process.argv.slice(2);
const samples = argv.includes("--samples");
const sets = parseSets(argv.filter((a) => a !== "--samples"));
const { scanParas } = loadReviewUi();

console.log("set".padEnd(8) + IDS.map((id) => id.slice(2).padStart(7)).join("") + "   docs");
for (const [label, files] of Object.entries(sets)) {
  const count = Object.fromEntries(IDS.map((id) => [id, 0]));
  const fp = [];
  for (const f of files) {
    const fired = {};
    for (const p of scanParas(clean(fs.readFileSync(f, "utf8")))) for (const h of p.hits) {
      const id = IDS.find((x) => h.id.startsWith(x));
      if (id) (fired[id] = fired[id] || []).push(h.why);
    }
    for (const id of Object.keys(fired)) {
      count[id]++;
      if (samples && !label.startsWith("pos")) fp.push(`  ${label} ${path.basename(f)} ${id}: ${fired[id][0].slice(0, 120)}`);
    }
  }
  console.log(label.padEnd(8) + IDS.map((id) => String(count[id]).padStart(7)).join("") + "   /" + files.length);
  fp.forEach((l) => console.log(l));
}
