---
title: 工人與工人加速效果
summary: 居民如何在產業找到工作、哪些工人會計入加速效果，以及加速幅度有多大。
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-14
fact: 10 / 20 | 觸發加速效果所需的工人
fact: 2 年 | 一次抵達的計入期限
fact: ×1.5–2.5 | 加速係數，每個產業固定
---

每個產業都提供工作場所。當足夠多的工人**搭乘你的客運路線抵達**時，產業的產量就會提高。產業視窗會顯示兩個不同的數字，把兩者混為一談是最常見的誤解。

```diagram workers_flow
```

## 誰能在產業工作

- 每個基本遊戲的產業都有 **20 個工作場所**（各產業 .con.lua 中的 `industrialCapacity = 20`）。
- 這些工作場所的設定讓居民**無法步行或開車**前往：只有你的路線能把他們送到（`industryutil.lua:451-457`，`disallowedMoveModes = {"WALK", "DRIVE"}`）。
- 每位居民都有住處、購物地點與工作地點。遊戲會從該居民能抵達的地點中挑選工作地點；產業的目的地權重為 2.0（`industryutil.lua:455`）。

```engine
居民如何在所有能抵達的地點中挑選一個工作地點（交通時間、費用、2.0 的權重），是由引擎計算的。腳本只提供輸入資料。
```

## 已指派的工人

指工作地點就是這個產業的居民。產業視窗中的工作場所長條，以及產業統計數據中的 **工作場所** 欄位（「12/20」）顯示的就是這個數字（`entity_window_util.tl:1238`，`statistic_industries.tl:305`）。光有已指派的工人**不會**帶來任何加速效果：他們必須真的前往產業。

## 計入加速效果的工人

一個小型遊戲腳本 `industry_workers.script.tl` 會記錄每一次抵達：

1. 當一位居民抵達產業，且他的**最後一段行程是搭乘你的路線**時，這次抵達會連同遊戲時間一起被記錄下來（`industry_workers.script.tl:86-118`）。
2. 只保留**最近 2 個遊戲年**內的抵達紀錄（`industry_productivity_util.tl:3`：`2 * getDefaultYearDuration()`）。
3. 最多只保留**最近的 20 次**抵達（`industry_workers.script.tl:4`，`KeepHistoryCount = 20`）。
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

## 小知識

- 最多保留 20 次抵達，再加上 50 % 的規則，代表**超過 40 個工作場所**的產業（模組可以做到）永遠無法靠工人獲得加速效果。
- 補助「運送工人」會在這個加速效果啟動時達成（官方 wiki，補助）。
- 加速貨物（肥料、機械、工具）是原料產業的**另一種**加速效果，本頁不討論。
- [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) 模組會在產業視窗中顯示已指派的工人與加速工人來自哪些城鎮，並在地圖上以箭頭標示。

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: 「Sufficient」（足夠）= 工作場所的一半（20 個中的 10 個）；「recently」（最近）= 最近 2 個遊戲年、最近 20 次抵達、每人一次、僅限你的路線；加速係數每個產業 ×1.5 到 ×2.5。
result: refines
```
