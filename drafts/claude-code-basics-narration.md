---
tone-version: 0.2.0
profile: narration
---

# Claude Code 基礎教學（旁白草稿・基礎篇）

看完這支影片，我帶你把 Claude Code 裝起來，在自己的專案裡改第一支程式。

Claude Code 是 Anthropic 做的寫程式助手，住在終端機裡面。登入跟網頁版同一組帳號，要 Pro 以上的方案，免費版進不來。模型你打 /model 就看得到了。

走 npm 的話先看 Node.js 版本。太舊它會印一行警告，但裝好的 claude 是獨立執行檔，跑起來不靠你的 Node，這行警告略過就好。

Mac 的話用 Homebrew 更順，不用管 Node。你打開終端機，把 brew install 減減 cask claude-code 這一串貼進去按 Enter，等它把 Claude Code 裝完。

不是 Mac 就貼 npm 這一串：npm install -g @anthropic-ai/claude-code，裝到全域。

沒有就先暫停，去裝完再回來。

裝好你打 claude 就進去了。第一次它會叫你登入，跟網頁版同一組帳號登入就好。

然後你進到你的專案，就是 cd 到你那個資料夾。我等你，你進去再回來。

第一句你不用想太多，先叫它讀這支程式。你把這句貼進去：幫我說這支程式在做什麼，哪一行最危險。

等它回完，你先看它講的那幾個檔案，跟你的對不對得上。

改的話一次改一支就好。叫它改完先別存檔。你把它改的每一行跟原本的對上，對上了再存檔。

如果改完跑得起來，你這招就算會了。

今晚你就打開，換另一支程式再跑一次看看。
