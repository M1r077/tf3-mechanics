---
title: 城鎮聲望
summary: 什麼會降低城鎮的聲望評價、它恢復得多快、慶祝活動與行銷活動實際做了什麼，以及為什麼切斷兩座城鎮之間的道路代價這麼大。
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
fact: −33 % | 每中斷一條通往其他城鎮的主要連接
fact: 33 % | 每年恢復（行銷活動期間 100 %）
fact: 0.25 % | 在城鎮旁每移除一棵成樹
fact: 200 萬 m³ | 的地形工程會耗盡全部聲望
---

**聲望**是城鎮視窗六項評價之一，城鎮管理機關取其中**最低**的一項（見[城鎮成長](towns.html)）。聲望從 100 % 開始，只會因為**你**建造或失敗的事情而下降：地形工程、移除樹木與岩石、拆除城鎮建築、申請失敗的補助，以及中斷的主要連接。時間、慶祝活動與行銷活動會讓它回升。

```diagram rep_recovery
```

## 什麼會降低聲望

你確認的每次建造都會在執行前檢查；損失記在相關城鎮上（`towns.script.tl:271-291`，`town_util.tl:1062-1080`）。只有你自己的建造才算，地圖編輯器中什麼都不算（`town_util.tl:1078-1080`，`towns.script.tl:58`）。

| 城鎮視窗中的原因 | 什麼會損失聲望 | 來源 |
|---|---|---|
| **已移除的植物** | 每棵 0.25 %，× 到最近城鎮的距離係數，× 樹的大小（小樹算得少） | `town_util.tl:1144-1150`，`town_util.tl:865`，`model_metadata_util.lua:655-680` |
| **已移除的岩石** | 每塊 0.25 %，× 距離係數 | `town_util.tl:1148-1149`，`town_util.tl:884-885` |
| **景觀** | 地形抬高**或**降低，每 m³ 0.00005 %：200 萬 m³ = 100 %。軌道、道路與建築塑造的地形也算（超過 50,000 m² 的建造最多減半），新隧道的體積也算 | `town_util.tl:873-886`，`town_util.tl:1245-1269`，`town_util.tl:1403-1436` |
| **已拆除的建築** | 拆掉一個區（該城鎮的住宅、商店或工作機會）40.5 % 的容量 = 100 % | `town_util.tl:867-869`，`town_util.tl:1165-1184` |
| **申請失敗的補助** | 供應城鎮：10 % 起，依風險最高 60–90 %；連接城鎮：10–100 % × 距離係數，**兩座**城鎮都扣（見[補助](subsidies.html)） | `deliver_cargo_town.script.tl:202-210`，`deliver_passengers.script.tl:113-114`，`towns.script.tl:331-333` |
| **主要連接中斷** | 每有一座主要連接被中斷或過長的其他城鎮，扣 **1/3** | `town_util.tl:376-394`，`town_util.tl:1608` |

- 每個原因最多 100 %（`town_util.tl:1611-1620`）。
- 建造時提示框顯示**聲望：-x %**，涉及多座城鎮時還會顯示數量（`construction_react_util.tl:3818-3864`）。它以滿分評價計算。
- 種樹或放置岩石只會抵銷**已移除的植物**或**已移除的岩石**，每個同樣 0.25 %。對其他原因無效，聲望滿分時也無效（`town_util.tl:1228-1238`，`town_util.tl:1630-1641`）。
- 新遊戲的聲望設定為**關閉**或**開啟**（所有預設都是開啟）。關閉表示評價永遠滿分（`difficulty_util.tl:44`，`difficulty_util.tl:110`，`town_util.tl:396-399`）。

```engine
城鎮與被移除樹木之間的距離係數下降得多快、每座城鎮分到的地形體積、軌道或道路自動移除的樹木，以及哪些道路算作城鎮的主要連接（以及行程何時算「過長」），都是引擎數值（getImpactFromDistance、getTerrainBrushVolumeImpact、getTerrainAlignmentImpact、getAutoRemovalEntityImpact、getTownProblems）。
```

## 中斷的主要連接

當遊戲提示**城鎮之間的道路連接已中斷**或**城鎮之間的旅行時間過長**時，主要連接就算中斷（`town_util.tl:378-380`，`town_warning.script.tl:7-22`）。每座相關的其他城鎮扣 1/3，評價會**立刻**顯示出來（`town_util.tl:401-403`）：

| 中斷的連接 | 聲望最多 | 評價 | 來源 |
|---|---|---|---|
| 1 | 67 % | 極佳 | `town_util.tl:983-985` |
| 2 | 33 % | 中等 | `town_util.tl:983-985` |
| 3 | 0 % | 極差：城鎮停止成長 | `town_util.tl:607-633` |

- 中斷期間，懲罰也會在半年內一步步寫進儲存的分數（`towns.script.tl:137-145`）。修好道路後，這部分只按正常速度恢復：長時間中斷會在之後一段時間裡繼續拖累聲望。
- 67 % 正好在「極佳」的邊界上：再有任何小損失，城鎮就會降到「佳」。

## 聲望如何恢復

- **自動恢復**：城鎮視窗顯示**年度恢復量** 33 %，行銷活動期間 100 %（`town_react_util.tl:1061-1067`）。也就是每半年一級（1/6），活動期間每 2 個月一級（`towns.script.tl:121-135`）。
- 恢復會把增加量分到所有原因上；不會超過仍未修復的中斷連接（`town_util.tl:1649-1687`）。
- **慶祝活動**：城鎮裡第一位乘客搭上你的路線 **+50 %**，第一批貨物送到城鎮 +50 %，城鎮每次升級 +50 %，每個產業第一次收到貨物時最近的城鎮 +20 %（`celebrations.script.tl:181-273`）。這時訊息末尾會加上**聚落聲望已提升。**或 **…的聲望提升了。**（`celebration_react_util.tl:63-75`）。只有聲望未滿時才算，戰役任務中不算（`celebrations.script.tl:79-93`，`celebrations.script.tl:140-142`）。
- **供應城鎮**接受時可給 +5 % 到 +20 % × 風險係數（`deliver_cargo_town.script.tl:195-199`）。和所有增加一樣，它只抵銷已有的損失（`towns.script.tl:324-330`）。

## 行銷活動

| 項目 | 數值 | 來源 |
|---|---|---|
| 價格 | 10 M × 年份係數：1900 年 4 M，到 2020 年 25 M，取整到 1 M | `marketing_campaign_tool.script.tl:9-14` |
| 需要 | 公司增益效果中的一張許可 | `marketing_campaign_tool.script.tl:83-95`，`company.script.tl:416-423` |
| 持續時間 | 一年 | `marketing_campaign_tool.script.tl:136` |
| 聲望 | 恢復 ×3（每年 100 %）；**沒有**立即增加 | `towns.script.tl:126`，`town_util.tl:915-925` |
| 居民 | 居民選擇出行方式時，你在該城鎮的路線以一半成本計算 | `marketing_campaign_tool.script.tl:137`，`towns.script.tl:376-398` |

```engine
腳本以每級 360 秒遊戲時間計算（活動期間 120 秒）。背後的日曆是引擎的年長度（getDefaultYearDuration）；城鎮視窗中的 33 % 與 100 % 對應一年 720 秒（一天 2 秒，`cargotype.script.lua:3`）。路線成本減半能把多少居民吸引到你的路線上，由引擎的路線選擇決定。
```

## 小知識

- 留意建造提示框：如果顯示**聲望：-x %**，隧道或更平緩的路線往往比聲望更划算。
- 不要讓兩座城鎮之間的主要道路一直斷著：每條立刻 −33 %，三條會讓城鎮停下。
- 聲望滿分時的行銷活動只幫助你的路線，不提升評價。在大工程剛結束、恢復還有東西可補時再進行。
- 總部大型模組的**聲望恢復**紅利（+1 %）會顯示在紅利分頁中，但在腳本裡它只改變一個沒有任何評價讀取的數值（`hq_module_l.module.lua:171`，`towns.script.tl:157`，`town_util.tl:829`，`town_util.tl:857`）。
- 成就**與我無關**需要在自由遊戲模式中讓一座城鎮的聲望降到 0 %（`achievements.script.tl:261-267`）。

```check
official: "Reputation reflects how the town and surrounding nature are treated. Landscaping, removing town buildings and breaking main connections to other towns can lower it, while celebrations and marketing campaigns can improve it. Reputation lost by removing trees can be recovered by planting new ones." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: 原因相同，另外還有移除岩石、隧道、軌道與道路的地形以及申請失敗的補助。每條中斷或過長的主要連接立刻扣 1/3；三條會讓城鎮停下。自動恢復每年 33 %；行銷活動把它提到每年 100 %，但不會立即增加。種樹只抵銷樹木造成的損失。總部的聲望恢復紅利在腳本中沒有效果。
result: refines
```
