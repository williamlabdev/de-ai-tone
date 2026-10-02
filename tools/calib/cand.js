#!/usr/bin/env node
// 候選 pattern 試驗台：改 review-ui.html 之前，先在這裡比較候選門檻的文件級觸發篇數。
// 下面 cands 是最近一輪實際比過的候選（下一輪直接改寫這個物件，舊候選看 git 歷史）。
// 用法：node tools/calib/cand.js pos=<dir> neg=<neg.list> hum=<dir> ...
"use strict";
const fs = require("fs");
const path = require("path");
const { loadReviewUi, clean, parseSets } = require("./lib");

const sets = parseSets(process.argv.slice(2));
const { scanParas, PE, splitSentEn } = loadReviewUi();

// 1001 第二輪：R-015 拿掉句首 Here's the/what/why/how 支（串文開場、路標句誤判），R-021 只認對舉或收尾。
// 0930 首輪比過的候選見 git 歷史（c93fc59）。
const SHORT = /^(?:Stop|Start)(?:\s+[\w'’-]+){1,3}[.!]?$/i;
const R015_OLD = new RegExp(PE.r015.source, "gi");
const R015_NEW = /\b(?:here'?s the thing|the (?:reality|truth) is|let'?s be clear|make no mistake|it'?s worth noting|worth noting that|that said|in other words|at its core|at the end of the day|simply put|put simply|the (?:key insight|bottom line) is|what this means in practice)\b/gi;
const bodySents = (b) => splitSentEn(b).map((s) => s.replace(/\*\*/g, "").trim()).filter(Boolean);
const cands = {
  "R-015 now": (paras) => paras.some((p) => R015_OLD.test(p) && !(R015_OLD.lastIndex = 0)),
  "R-015 drop Here's": (paras) => paras.some((p) => R015_NEW.test(p) && !(R015_NEW.lastIndex = 0)),
  "R-021 now": (paras, sents, blocks) => blocks.some((b) => bodySents(b.isHead ? b.body.replace(/^#{1,4}\s+/, "") : b.body).some((s) => SHORT.test(s))),
  // 標題整句、段落只有這一句、或段尾收束；同段後面還接具體說明的步驟小標不算
  "R-021 head/alone/tail": (paras, sents, blocks) => blocks.some((b) => {
    const ss = bodySents(b.isHead ? b.body.replace(/^#{1,4}\s+/, "") : b.body);
    return ss.some((s, i) => SHORT.test(s) && (b.isHead || i === ss.length - 1));
  }),
  // 後面沒句子、或下一句也是 ≤4 字短句（口號連打）才算；接長句說明的步驟小標不算
  "R-021 next short/none": (paras, sents, blocks) => blocks.some((b) => {
    const ss = bodySents(b.isHead ? b.body.replace(/^#{1,4}\s+/, "") : b.body);
    return ss.some((s, i) => SHORT.test(s) && (i === ss.length - 1 || ss[i + 1].split(/\s+/).length <= 4));
  }),
  // 採用案：標題整句，或內文中後面沒句子／下一句也 ≤4 字
  "R-021 head|next short": (paras, sents, blocks) => blocks.some((b) => {
    const ss = bodySents(b.isHead ? b.body.replace(/^#{1,4}\s+/, "") : b.body);
    return ss.some((s, i) => SHORT.test(s) && (b.isHead || i === ss.length - 1 || ss[i + 1].split(/\s+/).length <= 4));
  }),
  // 同段 Stop… 與 Start… 成對
  "R-021 pair": (paras, sents, blocks) => blocks.some((b) => {
    const ss = bodySents(b.body).filter((s) => SHORT.test(s));
    return ss.some((s) => /^stop/i.test(s)) && ss.some((s) => /^start/i.test(s));
  }),
};

for (const [name, fn] of Object.entries(cands)) {
  const cols = [];
  for (const [label, files] of Object.entries(sets)) {
    const hit = files.filter((f) => {
      const blocks = scanParas(clean(fs.readFileSync(f, "utf8")));
      const paras = blocks.filter((p) => !p.isHead).map((p) => p.body);
      return fn(paras, paras.flatMap((b) => splitSentEn(b).map((s) => s.trim())), blocks);
    });
    cols.push(`${label}=${hit.length}/${files.length}` + (label.startsWith("pos") || !hit.length ? "" : " (" + hit.map((f) => path.basename(f)).join(",") + ")"));
  }
  console.log(name.padEnd(24), cols.join("  "));
}
