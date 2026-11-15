---
title: 遊戲時間與月曆
summary: 遊戲速度和月曆速度是兩回事。一天和一年有多長，放慢或暫停月曆會改變什麼，又不會改變什麼。
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
fact: 4 s | 月曆速度 ×1、遊戲速度 1x 時的一個月曆日
fact: ≈ 24 min | 相同速度下的一個月曆年
fact: 0 ×0.25 ×0.5 ×1 ×2 ×4 | 月曆速度檔位
fact: 0 1x 2x 4x | 遊戲速度檔位
---

遊戲有**兩個時鐘**。**遊戲速度**（暫停、1x、2x、4x）讓一切都跑得更快：車輛、生產、城鎮。**月曆速度**只決定日期走得多快。遊戲中幾乎所有規則都按遊戲時間計算，而不是按月曆天數。

## 兩個設定

| 設定 | 檔位 | 改變什麼 | 來源 |
|---|---|---|---|
| **遊戲速度** | 暫停、1x、2x、4x | 整個模擬運行的速度 | `game_bar_widgets.tl:199-203` |
| **月曆速度** | 暫停中、×0.25、×0.5、×1、×2、×4 | 一天相當於多少秒遊戲時間 | `game_bar_widgets.tl:321-335`，`game_bar_widgets.tl:351` |

- 月曆速度 ×1 時，一天是 **4 秒**遊戲時間（官方 wiki），所以在 1x 下一個月約 2 分鐘，一年約 **24 分鐘**。用 [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 實測：×1 時每天 4.0 秒，×4 時 1 秒，×0.5 時 8 秒，×0.25 時 16 秒。
- ×4 讓日期走快四倍；**暫停中**讓日期停下，模擬繼續運行。
- 2x 和 4x 是上限：電腦跟不上時，遊戲會降低它們（`game.tl:636-642`）。實測：2x 平均為 1.9x，4x 平均為 3.6x。
- **時刻**和天氣是第三個、只影響畫面的時鐘：預設情況下它們自己變化，與月曆無關（`game_time_config.res.lua:5`，`weather_config.res.lua:5`）。

## 不論月曆如何，都按遊戲時間走的東西

這些按遊戲時間計算，所以放慢或暫停月曆不會讓它們變慢：

- **生產**：產業的生產時間是標準一年的固定比例（`industry_react_util.tl:51`）。產業視窗按目前月曆的天數顯示它（`industry_react_util.tl:23`）：在 ×0.25 下，同樣的速率顯示的天數只有四分之一。
- **貸款還款**：每個標準月的遊戲時間還一次，月曆暫停時也一樣（`loan.script.tl:83-88`）。
- **補助期限**和 ×2 收益獎勵（`subvention_util.tl:290-292`）。
- **城鎮聲望恢復**（`towns.script.tl:121-130`）、**工人加成**（`industry_productivity_util.tl:3`），以及多年無人服務後的**產業關閉**（`industries.script.tl:119-128`）。
- 城鎮最近半年的**送貨評價**（`town_util.tl:840`）。
- **新產業**：月曆暫停時，1809 秒遊戲時間內出現了 3 個，間隔 760 秒與 728 秒，與月曆運行時的節奏相同（約 730 秒）。用 [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 測得；見 [產業](industries.html)。

月曆運行時，遊戲按目前月曆速度的年、月、日顯示這些時長（`util.tl:40-49`）。

## 按月曆日期走的東西

- **新車輛、車站和建築**按年份出現（官方 wiki："Different calendar speeds only affect the availability of vehicles and infrastructure"）。
- **隨年份增長的費用**：建築維護費、時代版本、補助金額和貸款金額都跟隨日期。詳見：[成本、維護費與貸款](costs.html)。

## 月曆暫停時

1. 日期也就是年份保持不變：沒有新車輛，按年份的費用也不變。
2. 時長以**分和秒**顯示，而不是天（`util.tl:41-43`，`industry_react_util.tl:16-21`）。
3. 貸款按**每分鐘**而不是每年顯示還款（`finances_loan_gui.tl:223-231`），自訂貸款卡無法借取（`finances_loan_gui.tl:393`）。
4. 生產、還款、期限和聲望保持遊戲時間的節奏。

## 小知識

- 想在新車輛出現前有更多時間發展路網？降低月曆速度：你每遊戲分鐘的收益不會變。
- 顯示為「每年」的生產取決於月曆速度；比較產業時要用相同的速度。
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 在月曆暫停時也能保持易讀的財務圖表。

```engine
標準日、月、年的長度（getDefaultDayDuration 等）來自引擎。城鎮腳本把一個月算作 30 × 4 秒（`towns.script.tl:121`），這與實測的每天 4 秒相符；另外幾個常數仍假定一天為 2 秒（`cargotype.script.lua:3`，`mod.script.tl:172`）。
```

```check
official: "By default a day in the game lasts 4 seconds." "Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent." ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: 月曆速度相對標準日為 ×0.25 到 ×4 或暫停；生產、貸款、補助、聲望和工人計時按遊戲時間運行；月曆暫停時，時長以分鐘顯示，還款按每分鐘顯示，並且不能借新貸款；實測：×1 時每天 4 秒。
result: refines
```
