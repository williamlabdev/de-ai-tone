---
id: R-014
slug: llm-lexical-fingerprint
tone-version: 0.2.17
languages: [en]
profiles:
  articles: strict
  narration: strict
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: (?i)\b(?:delv(?:e|es|ed|ing)|leverag(?:e|es|ed|ing)|crucial|pivotal|myriad|plethora|tapestry|underscor(?:e|es|ed)|showcas(?:e|es|ed)|harness(?:es|ed|ing)?|realm|landscape|paradigm|holistic|testament|fast-paced|cutting-edge|streamlin(?:e|es|ed)|elevat(?:e|es|ed)|comprehensive)\b，全篇不同詞>=2
---

# R-014 LLM 詞彙指紋 / LLM lexical fingerprint

## 現象

英文稿密集出現一組 LLM 生成文字的高頻詞：`delve`、`leverage`、`crucial`、`pivotal`、`myriad`、`plethora`、`tapestry`、`underscore`、`showcase`、`harness`、`realm`、`landscape`、`paradigm`、`holistic`、`testament`、`fast-paced`、`cutting-edge`、`streamline`、`elevate`、`comprehensive`。這些字本身沒有拼字或文法問題，但人類作者很少自然地這樣密集使用，出現即是可疑指紋，不代表單次出現就一定違規。

中文對應形態僅供理解，本條 `languages` 不含 zh：中文行銷稿的對應現象大致是「善用」「賦能」「無縫」「顛覆」「賦予」這類翻譯腔詞彙堆疊，但尚未有語料可校準，不在本條 pattern 內。

## Before（禁式）

```text
（中文示意，僅供理解，本條不檢查中文）
這套系統能夠善用穩健、無縫的架構，釋放團隊蘊藏的無窮潛力。
```

英文對照（必填）：

```text
Our platform will leverage a comprehensive, cutting-edge architecture to realize the team's myriad potential.
```

## After（改法）

```text
（中文示意，僅供理解，本條不檢查中文）
這套系統把驗證環節從三步併成一步，上線時間從兩週縮短到三天。
```

改法：刪掉堆疊的抽象形容詞，換成具體改動與可驗證的數字（三步併成一步、兩週縮短到三天）。

英文對照（必填）：

```text
The team cut the verification steps from three stages down to one, and shipped the update in three days.
```

## 例外

- 全篇只出現一個詞（不論次數）不標：0930 校準時人寫對照組 10 篇有 4 篇單詞命中（`leverage` 在一篇談財富的散文裡出現 19 次），門檻改為全篇 >=2 個不同詞。
- `landscape` 與 `harness` 作技術名詞時放行（例如 `tooling landscape` 平台工具版圖、`test harness` 測試載具），命中一律先標 `needs-human`，沿用本 repo「機械寧可多標、人判負責放行」的分工，不因此縮小詞表。
- 引用人物原話時保留原樣。
- 其餘無例外。

## 機械檢查可行性

- 可機械化：英文匹配 `(?i)\b(?:delv(?:e|es|ed|ing)|leverag(?:e|es|ed|ing)|crucial|pivotal|myriad|plethora|tapestry|underscor(?:e|es|ed)|showcas(?:e|es|ed)|harness(?:es|ed|ing)?|realm|landscape|paradigm|holistic|testament|fast-paced|cutting-edge|streamlin(?:e|es|ed)|elevat(?:e|es|ed)|comprehensive)\b`，全篇（不含標題）出現 >=2 個不同詞才標記（詞形合併：`leverage`／`leveraging` 算同一詞），標在含命中詞的段落。0930 前是單次即標，校準後改；1004 自詞表移出 `empower`／`unlock`／`foster`／`ever-evolving`、1009 移出 `robust`／`seamless`／`game-changer`（見下）。
- 只能人審：命中的是正當技術名詞（`tooling landscape`、`test harness`）還是 LLM 慣用詞，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 3 處（正本 1 處 `tooling landscape`、草稿 2 處 `test harness`），全部是正當技術用語，不足以校準門檻，比照 README 慣例先當提示不當結論。
- 0930 首輪校準（語料不入 repo；方法見 `tools/README.md`）：正例 48 篇（`claude -p` 中性寫稿指令產出，opus／sonnet／haiku 各 16，prompt 不提風格）、反例 19 篇（作者網站已發佈英文文：AI 協作起草、作者裁決定稿，部分發佈前經本 repo 規則掃過）、人類對照 10 篇（Paul Graham 散文）。改規則前觸發篇數 正例 8／48（全是 haiku，opus／sonnet 0）、反例 1／19（`landscape`）、人類 4／10（單篇 `leverage` 19 次）；改為全篇不同詞>=2 後 正例 3／48、反例 0／19、人類 1／10。n 小、正例只有 Claude、部分 pattern 是看過命中後設計（有過擬合風險），仍為 experimental。
- 1004 第二輪（Wayback 2022-11 前人寫行銷稿 10 篇，見 `tools/README.md`）：觸發 2 篇（Atlassian 2021 `empower`＋`unlocks`、Mailchimp 2022 `empower`＋`ever-evolving`＋`fostering`），作者覆核兩處皆誤判——四詞在行銷文體是正常詞彙（Atlassian 品牌用語、Mailchimp 標語系），LLM 是從這類文案學走的，指紋方向反了。據此自詞表移出 `empower`／`unlock`／`foster`／`ever-evolving`（0.2.16），仍為 experimental（n 小、需三模型正例驗）。
- 1009 第三輪（語料不入 repo；方法見 `tools/README.md`）：Claude 三模型正例 24 篇 0 觸發；本地 `qwen3.8:27b` 正例 8 篇觸發 2 篇、命中 5 處，作者逐處獨立判只有 1 處是 AI 腔（`elevate the daily ritual of cooking into an art form`），`seamlessly`／`robust`／`game-changer`／另一處 `elevate` 判不是。據此移出 `robust`／`seamless`／`game-changer`（0.2.17）；`elevate` 一是一否，保留。移出依據只有單一模型 8 篇，仍為 experimental。

## 適用 profile

- `articles`：嚴格
- `narration`：嚴格
