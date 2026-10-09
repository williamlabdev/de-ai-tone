// calib.js／cand.js 共用：載入 tools/review-ui.html 的真實掃描邏輯、解析語料參數。
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const REPO = path.resolve(__dirname, "../..");

function loadReviewUi() {
  const html = fs.readFileSync(path.join(REPO, "tools/review-ui.html"), "utf8");
  const src = html.match(/<script>([\s\S]*)<\/script>/)[1];
  const stubEl = () => ({ onclick: null, onchange: null, innerHTML: "", value: "", appendChild() {}, querySelector() { return null; }, click() {} });
  const sb = { document: { getElementById: () => stubEl(), createElement: () => stubEl() }, URL: {}, Blob: function () {} };
  vm.createContext(sb);
  vm.runInContext(src, sb);
  return { scanParas: sb.scanParas, PE: vm.runInContext("PE", sb), splitSentEn: vm.runInContext("splitSentEn", sb) };
}

// 剝 mdx frontmatter、import/export、JSX 自閉合標籤、code fence 與修稿 log 行（1004 C1：含 .author-log/ 的整行，J070）
function clean(text) {
  return text
    .replace(/^---\n[\s\S]*?\n---\n/, "")
    .replace(/^(?:import|export) .*$/gm, "")
    .replace(/```[\s\S]*?```/g, "")
    .replace(/<[A-Z][^>]*\/>/g, "")
    .replace(/^.*\.author-log\/.*$/gm, "");
}

// 參數 label=<目錄>（取其中 .md/.mdx）或 label=<清單檔>（一行一個路徑）
function parseSets(args) {
  const sets = {};
  for (const a of args) {
    const m = a.match(/^([^=]+)=(.+)$/);
    if (!m) throw new Error("語料參數格式：label=<dir|file.list>，收到 " + a);
    const p = path.resolve(m[2]);
    sets[m[1]] = fs.statSync(p).isDirectory()
      ? fs.readdirSync(p).filter((f) => /\.mdx?$/.test(f)).sort().map((f) => path.join(p, f))
      : fs.readFileSync(p, "utf8").trim().split("\n").filter(Boolean);
  }
  return sets;
}

module.exports = { REPO, loadReviewUi, clean, parseSets };
