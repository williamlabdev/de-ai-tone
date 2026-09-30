#!/usr/bin/env node
// 候選 pattern 試驗台：改 review-ui.html 之前，先在這裡比較候選門檻的文件級觸發篇數。
// 下面 cands 是 0930 首輪實際比過的候選（保留當紀錄；下一輪直接改寫這個物件）。
// 用法：node tools/calib/cand.js pos=<dir> neg=<neg.list> hum=<dir> ...
"use strict";
const fs = require("fs");
const path = require("path");
const { loadReviewUi, clean, parseSets } = require("./lib");

const sets = parseSets(process.argv.slice(2));
const { scanParas, PE, splitSentEn } = loadReviewUi();

const IMP = /^(?:Stop|Start|Don'?t|Never|Always)\s+\w+/i;
const R014 = new RegExp(PE.r014.source, "gi");
const R016 = new RegExp(PE.r016.source, "g");
const stems = (paras) => new Set(paras.flatMap((p) => (p.match(R014) || []).map((w) => w.toLowerCase().replace(/(?:ing|ed|es|ly|e|(?<!s)s)$/, ""))));
const cands = {
  "R-014 distinct>=2": (paras) => stems(paras).size >= 2,
  "R-016 doc>=2": (paras) => paras.reduce((a, p) => a + (p.match(R016) || []).length, 0) >= 2,
  "R-016 doc>=3": (paras) => paras.reduce((a, p) => a + (p.match(R016) || []).length, 0) >= 3,
  "R-021 short(<=4w)>=2": (paras, sents) => sents.filter((s) => IMP.test(s) && s.split(/\s+/).length <= 4).length >= 2,
  "Here's reveal": (paras, sents) => sents.some((s) => /^Here'?s (?:the|what|why|how)\b/i.test(s)),
  // 0930 結論：反例 8/19 也命中，不具鑑別力，未採用
  "isn't X. It's Y": (paras) => /\b(?:isn'?t|is not|wasn'?t|aren'?t)\b[^.!?]{1,80}[.!?—;,]\s*(?:It'?s|It is|They'?re|That'?s)\b/.test(paras.join("\n")),
};

for (const [name, fn] of Object.entries(cands)) {
  const cols = [];
  for (const [label, files] of Object.entries(sets)) {
    const hit = files.filter((f) => {
      const paras = scanParas(clean(fs.readFileSync(f, "utf8"))).filter((p) => !p.isHead).map((p) => p.body);
      return fn(paras, paras.flatMap((b) => splitSentEn(b).map((s) => s.trim())));
    });
    cols.push(`${label}=${hit.length}/${files.length}` + (label.startsWith("pos") || !hit.length ? "" : " (" + hit.map((f) => path.basename(f)).join(",") + ")"));
  }
  console.log(name.padEnd(24), cols.join("  "));
}
