---
title: 工人與工人加速效果
summary: 居民如何在產業找到工作、哪些工人會計入加速效果，以及加速幅度有多大。
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-15
game: 40425
fact: 10 / 20 | 觸發加速效果所需的工人
fact: 2 年 | 一次抵達的計入期限
fact: ×1.5–2.5 | 加速係數，每個產業固定
---

每個產業都提供工作場所。當足夠多的工人**搭乘你的客運路線抵達**時，產業的產量就會提高。產業視窗會顯示兩個不同的數字，把兩者混為一談是最常見的誤解。

```diagram workers_flow
```

## 誰能在產業工作

- 每個基本遊戲的產業都有 **20 個工作場所**（`industrialCapacity = 20`）。
- 這些工作場所的設定讓居民**無法步行或開車**前往：只有你的路線能把他們送到（`industryutil.lua:451-457`，`disallowedMoveModes = {"WALK", "DRIVE"}`）。
- 每位居民都有住處、購物地點與工作地點。遊戲會從該居民能抵達的地點中挑選工作地點；產業的目的地權重為 2.0（`industryutil.lua:455`）。

```engine
居民如何在所有能抵達的地點中挑選一個工作地點（交通時間、費用、2.0 的權重），是由引擎計算的。腳本只提供輸入資料。
```

## 已指派的工人

指工作地點就是這個產業的居民。產業視窗中的工作場所長條，以及產業統計數據中的 **工作場所** 欄位（「12/20」）顯示的就是這個數字（`entity_window_util.tl:1238`，`statistic_industries.tl:305`）。光有已指派的工人**不會**帶來任何加速效果：他們必須真的前往產業。

## 計入加速效果的工人

一個小型遊戲腳本會記錄每一次抵達（`industry_workers.script.tl`）：

1. 當一位居民抵達產業，且他的**最後一段行程是搭乘你的路線**時，這次抵達會連同遊戲時間一起被記錄下來（`industry_workers.script.tl:86-118`）。
2. 只保留**最近 2 個遊戲年**內的抵達紀錄（`industry_productivity_util.tl:3`：`2 * getDefaultYearDuration()`）。
3. 已保留 20 次抵達後，最早的會被刪除；同一次更新中的新抵達總是全部保留（`industry_workers.script.tl:4`，`KeepHistoryCount = 20`，`industry_workers.script.tl:54-70`）。
4. 同一個人再次抵達時，新紀錄會取代舊紀錄：每位居民只算**一次**（`industry_workers.script.tl:56-70`）。

```diagram workers_window
```

## 加速效果何時開始、何時停止

- 當計入的工人達到**工作場所的一半**時，產業就會獲得加速效果：`counted ≥ workplaces × 0.5`（`industry_productivity_util.tl:35-48`，`RequiredWorkersFractionForBoost = 0.5`）。20 個工作場所時：**10 名工人**。
- 產業視窗的「加速效果」區塊顯示的正是這個：「已計入 / 所需」，所需人數無條件進位（`industry_react_util.tl:627`）。
- 每當有新的抵達紀錄，或最早的一筆超過 2 年時，遊戲就會重新檢查（`industry_workers.script.tl:40-43`）。因此工人不再前來後大約 2 年，加速效果就會**自動停止**。

## 加速幅度有多大

- 產量會乘上產業的**加速係數**，視窗中顯示為「+X %」（`industry_react_util.tl:716`）。
- 這個係數根據產業的隨機種子只抽取一次：**介於 ×1.5 與 ×2.5 之間**，之後對該產業永遠不變（`industry_productivity_util.tl:58-72`）。沒有種子的產業使用 ×2。
- 所以兩座完全相同的礦場，工人加速效果可能不同：決定要服務哪一座之前，先看看「+X %」。

## 範例

一座有 20 個工作場所、顯示「+84 %」的煤礦場。

| 情況 | 計入 | 有加速？ | 產量 |
|---|---|---|---|
| 新開公車路線：已指派 14 位居民，還沒有人抵達 | 0 | 否 | ×1 |
| 今年有 12 位不同的居民搭公車抵達 | 12 | 是（≥ 10） | ×1.84 |
| 公車路線被刪除；2 年內沒有人抵達 | 降到 0 | 停止 | ×1 |

## 把工人送到產業

```diagram workers_trip
```

- 工人要**抵達產業本身**、行程目標（`targetOrAtEntity`）是該產業、且最後的移動方式是**路線**時才會計入（`industry_workers.script.tl:86-94`）。在站點下車還不夠：這個人必須抵達產業。
- 每位居民對每個目的地（住處、購物、工作）有一種移動方式。產業視窗列出已指派的工人，並以圖示顯示這種方式：**步行**、**開車**或**路線**（`entity_window_util.tl:1400-1435`）。對產業來說應該總是路線，因為那裡不允許步行和開車（`industryutil.lua:451-457`）。
- 所以「不能步行」是指整段行程不能是步行或開車。並不是「完全不走路」：路線行程在站點和建築之間仍要步行開始和結束（見下方引擎說明）。
- **轉乘也算。** 腳本只看行程的方式，不看用了幾條路線（`industry_workers.script.tl:91`）。來自四條路線之外城鎮的工人和隔壁的工人計數相同，但可能要久得多才抵達。
- **你的任何路線都能送他們**，包括載貨的路線，只要車輛能載客、站點會裝載乘客。腳本不檢查車輛類型（`industry_workers.script.tl:86-118`）。玩家回報使用獨立的客運路線問題較少。
- 有些產業（例如鑽油設施）有內建站點，可接乘客和貨物（`industryutil.lua:156-165`）。
- 產業視窗會為每位已指派的工人顯示他是**目前位置**還是**移動途中**（`entity_window_util.tl:1371-1384`）。「加速效果」區塊列出計入的工人及其 2 年中的**剩餘時間**（`entity_window_util.tl:1579-1630`、`industry_eow.script.tl:644-649`）。
- 沒有計入任何抵達時（過去 2 年內一次也沒有），加速部分的工人清單會顯示：「將這個地點與大眾交通連接，讓居民可在此工作。」（`entity_window_util.tl:1650-1652`、`entity_window_util.tl:1608`、`entity_window_util.tl:1632`）。

```engine
哪個站點服務產業、工人從站點走到產業入口有多遠、哪些城鎮的居民得到這份工作，都由引擎決定（涵蓋範圍、尋路、工作選擇）。腳本沒有為工人設距離限制。玩家回報，一個貨運涵蓋範圍包含產業的車站一直沒帶來工人，直到有公車開到產業入口（Steam 討論串「Problem getting workers to site」）。
```

```tip
**快速取得工人加成（以及「運送工人」合約）：先建一條簡單路線。**

1. 新建一條從產業旁站點到**單一城鎮**的**客運路線**。
2. 城鎮站點的服務範圍**不要碰到你的任何其他客運站**。
3. 起步只需 1 輛車。

工作職位在路線開通時分配：兩次測試中**全部 20 個職位都給了這個城鎮**，加成分別在遊戲時間 **346 秒與 925 秒**後開始（其中一次只有 1 輛車）。當城鎮站點碰到網路中車站的服務範圍時，部分職位給了遠方的城鎮，最後的工人抵達所需時間長得多（964 秒）。使用 [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) 與 [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 測得；誰得到職位仍由引擎決定。
```

## 運送工人補助

- 只會為有工作職位、工人加速效果尚未啟動、並且在過去一年運出過貨物的產業提供（`deliver_workers.script.tl:121-131`、`industry_util.tl:541-558`）。每條規則都有輸出表（加速規則為 `output = { }`），而空的 Lua 表視為真，所以只會走到這個分支（`industry_util.tl:544-551`）。
- 工人加速效果啟動時達成：同樣是 20 個中有 10 個不同的人搭你的路線抵達（`deliver_workers.script.tl:152-156`）。不計其他東西；沒有隱藏規則。
- 合約卡上的進度條是「計入的工人 ÷ 工作場所的一半」（`deliver_workers.script.tl:267-272`、`industry_util.tl:11-18`）。
- 合約地圖上的箭頭來自**最近的 5 個城鎮**。它們只是提示：腳本依距離畫出，而不是依誰有這份工作（`deliver_workers.script.tl:297-317`）。
- 金額和期限見[補助：提案、期限與獎勵](subsidies.html)。

## 為什麼我的工人不來？

| 檢查 | 在哪看 | 原因 |
|---|---|---|
| 有人得到這份工作嗎？ | 工作場所長條（「12/20」） | 沒有已指派的工人就沒人出行。工作選擇在引擎一側。 |
| 工人的移動方式圖示 | 工人清單：步行 / 開車 / 路線 | 只有路線行程才能計入（`industry_workers.script.tl:91`）。 |
| 他們在移動嗎？ | **移動途中** / **目前位置** | 長時間「移動途中」：轉乘慢或擁擠，或從最後一站沒有路徑。 |
| 最後一站能到達產業入口嗎？ | 站點涵蓋範圍、入口道路 | 玩家回報；在引擎一側。一條到入口的短公車路線有幫助。 |
| 站點會裝載乘客嗎？ | 路線站點、貨物篩選條件 | 行程兩端都必須裝卸乘客。 |
| 2 年內 10 個**不同**的人？ | 「加速效果」區塊、**剩餘時間** | 同一個人只算一次；較早的抵達會被移出（`industry_workers.script.tl:56-70`）。 |
| 超過 40 個工作場所（模組）？ | 工作場所長條 | 只保留 20 次抵達，永遠達不到一半。 |

## 小知識

- 最多保留 20 次抵達，再加上 50 % 的規則，代表**超過 40 個工作場所**的產業（模組可以做到）永遠無法靠工人獲得加速效果。
- **運送工人**補助會在這個加速效果啟動時達成（`deliver_workers.script.tl:152-156`）。
- 加速貨物（肥料、機械、工具）是原料產業的**另一種**加速效果，本頁不討論。
- [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) 模組會在產業視窗中顯示已指派的工人與加速工人來自哪些城鎮，並在地圖上以箭頭標示。

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: 「Sufficient」（足夠）= 工作場所的一半（20 個中的 10 個）；「recently」（最近）= 最近 2 個遊戲年、最近 20 次抵達、每人一次、僅限你的路線；加速係數每個產業 ×1.5 到 ×2.5。轉乘也算；移動方式必須是路線，從站點步行是這種行程的一部分。
result: refines
```
