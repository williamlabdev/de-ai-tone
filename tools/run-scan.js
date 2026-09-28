#!/usr/bin/env node
// 用真正的 tools/review-ui.html 內的 scanParas 掃檔案，供 snapshot.py / check-after.py 调用。
// 避免在 Python 側另寫一套分身邏輯（分身即漂移）。用法：
//   node tools/run-scan.js <file...> [--storyboard]
// 输出 JSON 到 stdout：{file: [{i, body, isHead, isList, hits: [ids]}]}
"use strict";
const fs = require("fs");
const vm = require("vm");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const html = fs.readFileSync(path.join(ROOT, "tools", "review-ui.html"), "utf8");
const src = html.match(/<script>([\s\S]*)<\/script>/)[1];

function stubEl() {
  return {
    onclick: null, onchange: null, innerHTML: "", value: "",
    appendChild() {}, querySelector() { return null; },
    click() {},
  };
}
const sandbox = {
  document: {
    getElementById: () => stubEl(),
    createElement: () => stubEl(),
  },
  URL: {}, Blob: function () {},
};
vm.createContext(sandbox);
vm.runInContext(src, sandbox);

const args = process.argv.slice(2);
const storyboard = args.includes("--storyboard");
const files = args.filter((a) => a !== "--storyboard");

const out = {};
for (const f of files) {
  const text = fs.readFileSync(f, "utf8");
  const paras = storyboard
    ? sandbox.scanStoryboard(text).map((r, i) => ({ i, body: r.body, hits: r.hits.map((h) => h.id) }))
    : sandbox.scanParas(text).map((p) => ({
        i: p.i,
        body: p.body,
        isHead: !!p.isHead,
        isList: !!p.isList,
        hits: p.hits.map((h) => h.id),
      }));
  out[f] = paras;
}
console.log(JSON.stringify(out, null, 2));
