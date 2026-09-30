---
tone-version: 0.2.11
profile: narration
note: 真實分鏡表格格式的 R-023 fixture，虛構；只有 [視覺:…] 裡引號框住的畫面字該被掃，旁白欄、備註欄、HTML 註解裡的冒號分號都不算
---

<!-- 撰稿備註：本檔虛構；這行有全形分號。Note: this line has a semicolon; it must not hit. -->

## 分鏡

| 段 | 旁白落點 | 視覺 | 備註 |
|---|---|---|---|
| 鉤子 | 「你交代一句，它就自己讀完」 | `[視覺:textcard/statement:標題卡「工作流：交代一句，它自己讀完」]` | 與 #2 同機位;狀態 1 |
| 開始 | 「先在瀏覽器試；天天用再裝」 | `[視覺:textcard/statement:標題卡「你交代一句，它就自己讀完、改好」]` | 對照組，不應命中 |
| 選擇 | 「天天用再裝」 | `[視覺:textcard/compare:對照卡「先試味道用瀏覽器；天天用，裝桌面版」]` | 全形分號並列 |
| Hook | "Note: hand it one line" | `[視覺:textcard/statement:title card "Workflow: hand it one line"]` | en 短標籤 |
| Choice | "install later" | `[視覺:textcard/compare:card "Try it in the browser first; use it daily, install the app."]` | en 分號 |
| Plain | "reads and edits" | `[視覺:textcard/statement:card "You hand it one line and it reads and edits on its own."]` | 對照組 |
| 混排 | 「它讀完」 | `[視覺:scene/desk:螢幕上寫著「讀完;改好」,旁邊沒有字卡]` | 中文畫面字夾半形分號，en 判準不應命中 |
