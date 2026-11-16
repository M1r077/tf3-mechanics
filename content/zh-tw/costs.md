---
title: 成本、維護費與貸款
summary: 成本設定會改變什麼，哪些成本會隨月曆年份成長，車輛價格如何計算，以及一筆貸款實際要花多少錢。
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
game: 40425
fact: ×6 | 到 2020 年貨物倉庫、港口與機場維護費的年份係數
fact: 6 年 | 的運行成本：這就是一輛車輛的價格
fact: 一次 | 貸款利率只依金額收一次，而不是每年都收
fact: 4 | 筆貸款可以同時存在
---

**通貨膨脹** 設定不會提高任何成本：它只會隨著公司等級上升而降低你的收益（見 [貨運收益與配送時間](income.html)）。成本改為隨**月曆年份**成長，另有四個滑桿從一開始就決定它們的倍率。

```diagram cost_years
```

## 成本設定

| 設定 | 數值 | 預設 簡單 · 普通 · 困難 · 極度困難 | 來源 |
|---|---|---|---|
| **車輛成本**、**車輛維修** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:39`，`difficulty_util.tl:98-99`，`difficulty_util.tl:125-126` |
| **基礎設施成本**、**基礎設施維護** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:100-101`，`difficulty_util.tl:153-156`，`difficulty_util.tl:180-183` |
| **車輛維修效果** | 無 ×0 · 低 ×0.5 · 中 ×1 · 高 ×1.5 · 極高 ×2 | 低 · 中 · 高 · 極高 | `difficulty_util.tl:42`，`difficulty_util.tl:103`，`difficulty_util.tl:185` |
| **通貨膨脹** | 只影響收益，見 [貨運收益與配送時間](income.html) | 低 · 普通 · 高 · 極高 | `difficulty_util.tl:50`，`mod.script.tl:694-697` |

- **基礎設施成本** 決定道路、軌道、橋梁、隧道、平交道、建築與模組的價格，也包括地形工程（`post_run_util.tl:23-52`，`post_run_util.tl:83-120`，`construction.script.tl:31-35`，`mod.script.tl:223-226`）。它也決定建築的拆除費用（`construction.script.tl:39-44`）。**基礎設施維護** 決定它們的維護費（`post_run_util.tl:43-45`，`post_run_util.tl:105-112`，`entity_window_util.tl:186`）。
- **車輛成本** 與 **車輛維修** 決定每輛車輛的購買價格與運行成本（`post_run_util.tl:54-81`）。
- **車輛維修效果** 決定狀況差的車輛會損失多少速度、功率與舒適度，又會增加多少噪音、污染與運行成本（`mod.script.tl:241-245`）。

## 隨月曆年份成長的項目

- **建築維護費**：1900 年 ×1、1920 年 ×1.5、1940 年 ×2.2、1960 年 ×3.2、1980 年 ×4、2000 年 ×5、2020 年 ×6（`mod.script.tl:92-100`）。建築視窗與建造選單會把它套用到每個標記為跟隨年份的建築，而建造選單標記的是：貨物倉庫、飛行場、機場與港口（`entity_window_util.tl:186-193`，`construction_react_util.tl:1149`，`warehouse.tl:7`，`harbor_modular.tl:24`）。
- 加到這類建築上的**模組**，價格依建築興建的年份計算，維護費依目前年份計算（`construction.tl:3720-3727`，`construction.tl:4364-4367`）。
- **時代版本**：車庫、維修站、貨物倉庫、車站、港口與機場每個時代各有一個版本，後面的版本花費是第一個的 **×3**（時代 B）或 **×9**（時代 C）（`rail_depot.con.lua:7`，`warehouse.tl:48`，`modular_station.con.lua:71`，`harbor_modular.tl:76`，`airport.tl:8`）。
- **補助現金**：從 1900 年的 ×1 到 2000 年以後的 ×4（`finances_util.tl:87-90`）。**貸款金額**：從 1900 年的 ×0.4 到 2020 年的 ×2.4（`loan_util.tl:7-10`）。
- **收益**完全沒有年份係數（`cargo_income.script.lua:10-13`）。

```engine
實際收取的維護費，以及道路、軌道與車輛是否也跟隨年份表，由引擎決定（getCostMultiplierForYear；基本設定只設了 chargeMaintenanceInterval = 60，`mod.script.tl:105`）。腳本只用上面的表計算視窗與建造選單中顯示的數值。沒有腳本替其他建築設定「跟隨年份」標記。
```

## 軌道、道路與建築

道路與軌道檔案給出每公尺的價格與每年的維護費；建造選單以每公里顯示（`construction_react_util.tl:2463`，`construction_react_util.tl:2477-2485`）。大多數類型的維護費是建造價格的**六分之一**：

| 類型 | 開放時間 | 每公里建造費 | 每公里每年維護費 | 來源 |
|---|---|---|---|---|
| 簡易軌道 | 開局 | 6 萬 | 1 萬 | `simple.street_template.lua:9`，`simple.street_template.lua:33` |
| 標準軌道 | 1930 | 18 萬 | 3 萬 | `standard.street_template.lua:11`，`standard.street_template.lua:35` |
| 高速軌道 | 1980 | 54 萬 | 9 萬 | `high_speed.street_template.lua:11`，`high_speed.street_template.lua:35` |
| 小型舊鄉間道路 | 開局 | 6 萬 | 1 萬 | `country_old_small.street_template.lua:8`，`country_old_small.street_template.lua:58` |
| 大型新城鎮街道 | 1940 | 54 萬 | 9 萬 | `town_new_large.street_template.lua:11`，`town_new_large.street_template.lua:91` |

- 電纜會增加軌道價格的 **30 %**；公車專用道增加道路價格的 10 %，輕軌軌道 20 %，電氣化輕軌軌道 40 %（`mod.script.tl:24-28`）。
- 抬高地形每立方公尺 4.5，降低地形每立方公尺 5.25（兩者都 × 基礎設施成本），清除一塊農田 20 萬（`mod.script.tl:20-22`，`mod.script.tl:33`，`mod.script.tl:225-226`）。
- 沒有設定維護費的建築，每年支付**價格的六分之一**（依基礎設施成本設定之前的價格計算，`construction.script.tl:25-27`）。
- 基本設定把拆除退款係數設為 0.75，退款時間設為 60（`mod.script.tl:30-31`）：拆掉剛蓋好的東西能拿回大部分的錢。由引擎套用。

檔案中寫的每年維護費，第一個版本（1940 年以前）與之後的版本；貨物倉庫還要再乘上上面的年份係數：

| 建築 | 第一個版本 | ×3（1940 年起） | ×9（1980 年起） | 來源 |
|---|---|---|---|---|
| 火車車庫、船舶車庫 | 10 萬 | 30 萬 | 90 萬 | `rail_depot.con.lua:34`，`water_depot.con.lua:32` |
| 道路車庫 | 3 萬 | 9 萬 | 27 萬 | `road_depot.con.lua:32` |
| 輕軌車庫 | 2 萬 | 6 萬 | 18 萬 | `tram_depot.con.lua:34` |
| 火車或船舶維修站 | 4 萬 | 12 萬 | 36 萬 | `rail_maint_station.con.lua:32`，`water_maint_station.con.lua:32` |
| 道路維修站 | 1 萬 | 3 萬 | 9 萬 | `road_maint_station.con.lua:32` |
| 通用貨物倉庫 | 2.5 萬 | 7.5 萬 | 22.5 萬 | `warehouse.tl:48-52`，`warehouse.tl:75` |
| 專用貨物倉庫 | 5 萬 | 15 萬 | 45 萬 | `warehouse.tl:51`，`warehouse.tl:75` |

這些建築的建造費都是維護費的 **6 倍**（`rail_depot.con.lua:35`，`warehouse.tl:76`）：最後一個時代的專用貨物倉庫，在乘上年份係數之前是 270 萬。

- 第一個**飛行場**（到 1950 年為止）就已經使用第二個時代的 ×3：它的判斷讀取的是版本的結束年份，而不是開始年份（`airfield.tl:8`，`airfield_era_a.metacon.tl:3`）。

## 車輛

基本遊戲的車輛都沒有固定價格：遊戲在載入模型時，依車輛的速度與容量計算價格（`model_metadata_util.lua:488-552`）：

1. **每年運行成本** = 約 675 × 平均速度（m/s）× 容量 ÷ 4（`model_metadata_util.lua:499-518`）。675 來自每公里的平均收益，並為空車回程、購買費用與下降的票價保留空間而調低（`model_metadata_util.lua:500-508`）。
2. **平均速度**低於最高速度（v 為 km/h）：道路車輛與輕軌為 v^0.78 + 4，列車為 v^0.86 + 10，飛機為 −0.0000203 × v² + 0.17 × v + 28.36（v 最多 4,000），船舶為最高速度的 65 %（`model_metadata_util.lua:448-474`）。
3. **列車**：車廂以容量的一半計算；機車還會把 功率 ÷ 最高速度（km/h）× 12.5 當作容量，同樣減半（`model_metadata_util.lua:511-512`，`model_metadata_util.lua:526-540`）。強勁而慢的機車很貴。
4. **價格** = 每年運行成本的 **6 倍**（`model_metadata_util.lua:548-549`）。

100 % 時的例子：一輛 35 km/h、載客 48 人的公車，每年運行成本約 4.5 萬，價格約 27 萬。

- 車輛的狀況分為五級（100–80 %，之後每 20 % 一級）（`vehicle_store_util.tl:231-234`）；到 **20 %** 時遊戲會發出警告，直到狀況回到 30 % 以上（`notifications.script.tl:310-318`）。

```engine
車輛狀況下降得多快、運行成本隨之上升多少，以及車輛價格是否隨年份改變，都是引擎的數值（getMaintenanceRunningCostPenalty 與其他懲罰項）；腳本只用車輛維修效果來縮放它們。
```

## 貸款

```diagram loan_interest
```

| 種類 | 1960 年前後的金額（1900 年 ×0.4，2020 年 ×2.4） | 期間 | 利率 | 來源 |
|---|---|---|---|---|
| 小 | 500 萬–1,000 萬 | 1–5 年 | 3–5 % | `loan_util.tl:12-22` |
| 中等 | 1,500 萬–2,500 萬 | 3–8 年 | 5–8 % | `loan_util.tl:24-34` |
| 大 | 3,000 萬–5,000 萬 | 5–12 年 | 8–10 % | `loan_util.tl:36-46` |
| 特大 | 4,000 萬–6,000 萬 | 10–24 年 | 10–12 % | `loan_util.tl:48-58` |

- 卡片上寫的是**年利率**，但利率只依金額計算**一次**：總利息是 金額 × 利率，與期間無關。它和本金一起按月平均支付（`loan_util.tl:102-111`，`loan_util.tl:126-136`，`loan.script.tl:83-99`）。因此利率相同時，長期貸款每年比短期貸款便宜。
- **償還** 只支付剩餘的本金：剩下的利息直接取消（`loan.script.tl:171-190`）。按下按鈕需要有這麼多現金（`finances_loan_gui.tl:284-286`）。
- 利率**不**取決於難度：每種貸款都有自己固定的範圍（`loan_util.tl:12-58`）。
- 最多同時 **4 筆貸款**（`loan_util.tl:4`，`loan.script.tl:134`）。提案半年後更換；你借走的那個位置會空 4 到 8 個月（`loan.script.tl:61-76`，`loan.script.tl:150`）。
- 開局時四個位置各自取一種隨機種類的數值，所以第一個「小」提案可能是一筆大貸款；提案更新一次後，每個位置就會提供自己的種類（`loan_util.tl:60-74`，`loan.script.tl:63-75`）。

```tip scripts
**選最長的貸款，然後提前償還。** 無論期限多長，總利息都一樣，月付更少，償還時剩下的利息直接取消。
```

## 小知識

- 選能借到的**最長**貸款：總利息相同，分攤到更多月份，而且提前償還時不必付剩下的利息。
- 有時代版本的建築在後面的時代花費 ×3 與 ×9，維護費還會隨年份不斷成長：最後一個時代的專用貨物倉庫是一筆很大的固定成本。
- 又快又大的車輛運行成本較高，但載得也較多：價格與運行成本和它能賺的收益一樣，都取決於 速度 × 容量。

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: 貸款利率只取決於種類（3–12 %），與難度無關，而且只依金額收一次，分攤到期間內的各個月；提前償還會取消剩餘利息。通貨膨脹只改變收益；建築維護費跟隨年份（×1 到 ×6）；車輛價格 = 每年運行成本的 6 倍，兩者都來自速度與容量。
result: differs
```
