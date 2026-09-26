---
id: R-014
slug: llm-lexical-fingerprint
tone-version: 0.2.8
languages: [en]
profiles:
  articles: strict
  narration: strict
mechanical:
  zh: 不適用，本條是英文特有現象，中文對應形態尚未調查，待有中文語料再評估
  en: (?i)\b(?:delv(?:e|es|ed|ing)|leverag(?:e|es|ed|ing)|robust|seamless(?:ly)?|crucial|pivotal|myriad|plethora|tapestry|underscor(?:e|es|ed)|showcas(?:e|es|ed)|foster(?:s|ed|ing)?|harness(?:es|ed|ing)?|unlock(?:s|ed|ing)?|realm|landscape|paradigm|holistic|testament|ever-(?:evolving|changing)|fast-paced|cutting-edge|game-?changer|streamlin(?:e|es|ed)|empower(?:s|ed|ing)?|elevat(?:e|es|ed)|comprehensive)\b
---

# R-014 LLM 詞彙指紋 / LLM lexical fingerprint

## 現象

英文稿密集出現一組 LLM 生成文字的高頻詞：`delve`、`leverage`、`robust`、`seamless`、`crucial`、`pivotal`、`myriad`、`plethora`、`tapestry`、`underscore`、`showcase`、`foster`、`harness`、`unlock`、`realm`、`landscape`、`paradigm`、`holistic`、`testament`、`ever-evolving/changing`、`fast-paced`、`cutting-edge`、`game-changer`、`streamline`、`empower`、`elevate`、`comprehensive`。這些字本身沒有拼字或文法問題，但人類作者很少自然地這樣密集使用，出現即是可疑指紋，不代表單次出現就一定違規。

中文對應形態僅供理解，本條 `languages` 不含 zh：中文行銷稿的對應現象大致是「善用」「賦能」「無縫」「顛覆」「賦予」這類翻譯腔詞彙堆疊，但尚未有語料可校準，不在本條 pattern 內。

## Before（禁式）

```text
（中文示意，僅供理解，本條不檢查中文）
這套系統能夠善用穩健、無縫的架構，釋放團隊蘊藏的無窮潛力。
```

英文對照（必填）：

```text
Our platform will leverage a robust, seamless architecture to unlock the team's myriad potential.
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

- `landscape` 與 `harness` 作技術名詞時放行（例如 `tooling landscape` 平台工具版圖、`test harness` 測試載具），命中一律先標 `needs-human`，沿用本 repo「機械寧可多標、人判負責放行」的分工，不因此縮小詞表。
- 引用人物原話時保留原樣。
- 其餘無例外。

## 機械檢查可行性

- 可機械化：英文匹配 `(?i)\b(?:delv(?:e|es|ed|ing)|leverag(?:e|es|ed|ing)|robust|seamless(?:ly)?|crucial|pivotal|myriad|plethora|tapestry|underscor(?:e|es|ed)|showcas(?:e|es|ed)|foster(?:s|ed|ing)?|harness(?:es|ed|ing)?|unlock(?:s|ed|ing)?|realm|landscape|paradigm|holistic|testament|ever-(?:evolving|changing)|fast-paced|cutting-edge|game-?changer|streamlin(?:e|es|ed)|empower(?:s|ed|ing)?|elevat(?:e|es|ed)|comprehensive)\b`，命中即標記待審，不設門檻（單次即可疑）。
- 只能人審：命中的是正當技術名詞（`tooling landscape`、`test harness`）還是 LLM 慣用詞，需人判斷。
- 語料定義：剝掉 frontmatter、fenced code block、inline code、HTML 註解後的正文；草稿另要求正文 >=200 英文字且漢字數 <= 英文字數 5%。
- 本 repo 的英文語料（18 篇英文正本正文 18,808 英文字＋16 份英文草稿正文 21,989 英文字）上此 pattern 命中 3 處（正本 1 處 `tooling landscape`、草稿 2 處 `test harness`），全部是正當技術用語，不足以校準門檻，比照 README 慣例先當提示不當結論。

## 適用 profile

- `articles`：嚴格
- `narration`：嚴格
