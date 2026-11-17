---
title: 貨物倉庫
summary: 通用或專用模組、每個庫存存放什麼、固定貨物類型、裝載速度、成本與污染，以及貨物倉庫不做的事。
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
game: 40425
fact: 500 | 每個模組可存的貨物單位，不論類型
fact: ×2 | 專用模組的裝載速度，通用模組為 ×1
fact: 15 萬 / 30 萬 | 通用 / 專用模組的價格
fact: 0 | 在貨物倉庫卸下的貨物帶來的收益
---

貨物倉庫由一個入口和一組**模組**組成。它在兩條路線之間存放貨物：一條路線卸貨，另一條路線再裝貨。車站透過服務範圍連到貨物倉庫；城鎮和產業從不從貨物倉庫拿任何東西（官方 wiki）。

## 通用模組與專用模組

| 模組 | 庫存 | 存放 | 係數 | 來源 |
|---|---|---|---|---|
| **通用** | 所有通用模組共用**一個**庫存 | 任何貨物，可混放 | ×1 | `warehouse.script.lua:272-295`，`modules.script.lua:49` |
| **液體**、**散裝**、**平板**、**一般貨物** | **每個模組一個庫存** | 一次一種貨物，屬於該類別 | ×2 | `warehouse.script.lua:296-314`，`modules.script.lua:120`，`modules.script.lua:165`，`modules.script.lua:247`，`modules.script.lua:296` |

- 每個模組增加 **500** 個單位（`modules.script.lua:49`，`modules.script.lua:120`）。五個通用模組組成一個 2,500 的庫存；五個液體模組組成五個 500 的庫存。
- 乘客從不存放（`warehouse.script.lua:279`，`warehouse.script.lua:304`）。
- 專用模組一次只接收一種貨物：要存放原油和燃料，需要兩個液體模組（官方 wiki）。
- 專用模組的 ×2 會與月台係數相乘：散裝貨物月台加散裝模組得到 ×4。詳見：[裝載與卸貨速度](loading.html)。

## 通用還是專用？

1. **貨物種類多、數量少**：通用。一個共用庫存，價格減半，污染也減半。
2. **一種貨物、數量大**（煤、原油、原木）：專用。車輛在那裡卸貨和裝貨快一倍，但每種貨物需要一個模組。
3. **食物等配送時間短的貨物**：專用；官方 wiki 說這些模組會凍結配送計時（見下文）。
4. 兩種模組可以混在一個貨物倉庫裡：通用模組仍組成一個庫存，每個專用模組各有自己的庫存。

## 貨物倉庫會加快卸貨嗎？

- **專用模組**：會，對它接收的貨物為 ×2。車輛的裝載提示框顯示「專用貨物倉庫：+100 %」（`cargo_react_util.tl:51-54`）。
- **通用模組**：不會。它的庫存建立時為 ×1；模組要求的 ×2 會被忽略（`warehouse.script.lua:284`，`warehouse.script.lua:288-289`）。
- 當一部分貨物進貨物倉庫、一部分進產業時，車輛會輪流服務它們，因此一次停靠中速度會改變（遊戲內實測，見 [裝載與卸貨速度](loading.html)）。

## 「庫存」區塊

- 每個庫存一行：它接收的貨物、數量，以及滑鼠停在上面時顯示的**平均剩餘配送時間**（`entity_window_util.tl:408-410`）。
- **固定貨物類型**：在專用模組上點擊一個貨物圖示。遊戲會重建貨物倉庫，把該模組保留給這種貨物（`entity_window_util.tl:339-367`，`warehouse.script.lua:308`）。移除或替換模組會清除固定（`warehouse.script.lua:403-405`）。
- **丟棄所有貨物**：立即清空這一行（`entity_window_util.tl:423-434`）。貨物會遺失。
- 只有屬於其他玩家的貨物倉庫沒有這兩個按鈕；你自己的貨物倉庫和沒有擁有者的貨物倉庫都有（`warehouse_eow.script.tl:127-137`，`gui/entity_window/warehouse/warehouse.tl:38`，`entity_util.tl:83-86`）。
- **統計數據**圖表依年份顯示**進貨**（卸下的）與**出貨**（裝上的）（`warehouse_eow.script.tl:159-160`）。

## 成本與污染

| | 通用模組 | 專用模組 | 來源 |
|---|---|---|---|
| 價格 | 15 萬 | 30 萬 | `wh_universal.module.lua:18`，`wh_liquid.module.lua:22` |
| 每年維護費 | 2.5 萬 | 5 萬 | `wh_universal.module.lua:19`，`wh_liquid.module.lua:23` |
| 噪音 | 20 | 20 | `wh_universal.module.lua:33`，`wh_liquid.module.lua:37` |
| 污染 | 25 | 50 | `wh_universal.module.lua:34`，`wh_liquid.module.lua:38` |

- 貨物倉庫本身也會增加污染：**25**，只要蓋了一個專用模組就是 **50**（`warehouse.script.lua:327`，`warehouse.script.lua:338-345`）。
- 建造選單中每個類別與時代（從 1900、1940 與 1980 年起）各有一項（`warehouses/warehouse.tl:3-5`）；後面的時代顯示 ×3 與 ×9（`warehouses/warehouse.tl:48`，`warehouses/warehouse.tl:75-76`），貨物倉庫維護費也會隨年份成長。詳見：[成本、維護費與貸款](costs.html)。
- 散裝、平板與一般貨物模組的花費與液體模組相同（`wh_bulk.module.lua:22-23`，`wh_flatbed.module.lua:22-23`，`wh_goods.module.lua:18-19`）。

```engine
腳本給出兩個排放等級，第二個是第一個的兩倍（`warehouse.script.lua:342-343`）；貨物倉庫隨著庫存填滿從第一個過渡到第二個，庫存滿時為兩倍（`emissions.script.tl:237-249`）。模組實際收取的價格由引擎計算。
```

## 貨物倉庫不做的事

- **它不付錢。** 在貨物倉庫卸貨沒有收益；貨物只在抵達消費者時，依離來源地的直線距離支付一次（遊戲內實測，見 [貨運收益與配送時間](income.html)）。
- **它不供貨給附近的城鎮或產業**：它們只從車輛接收貨物（官方 wiki）。
- **它不是路線自動配置的目的地**，自動配置只尋找生產者與消費者；但在存放某種貨物的貨物倉庫旁的站點，這種貨物不會進入裝載清單，所以列車會在那裡把它卸下（見 [裝載與卸貨速度](loading.html)）。
- **它不需要道路。** 入口會吸附到街道上，但貨物只透過車站的服務範圍移動（`warehouse.script.lua:386-389`，官方 wiki）。貨物倉庫視窗會顯示它的服務範圍（`gui/entity_window/warehouse/warehouse.tl:88-96`）。

```engine
卸下的貨物去哪裡，以及存放中貨物的配送計時是否停止，都由引擎決定。沒有腳本凍結計時：官方 wiki 說專用模組會凍結，通用模組不會。
```

## 小知識

- 檢查貨物倉庫附近每個站點的裝載清單：不在清單裡的貨物會卸進貨物倉庫，即使在路線半途。
- 庫存滿了就不再接收貨物，除非站點使用「抵達時強制卸載所有貨物」（「即使庫存已滿也卸下貨物」）；放不下的貨物會被銷毀：遊戲把車站顯示為目的地，而車站從不消耗貨物（遊戲內實測，見 [裝載與卸貨速度](loading.html)）。
- 要讓一個專用模組只存一種貨物，就在「庫存」區塊固定它的貨物類型。
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 會依車站列出範圍內的貨物倉庫及其庫存；[Platform Details](https://mod.io/g/transportfever3/m/platform-details) 會顯示卸下的貨物去了哪裡。

```check
official: "Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types." Specialised warehouses "freeze the cargo item's delivery timer" and "enable faster loading / unloading speeds". "In specialized warehouses, only one cargo type can be stored at a time for a given module." ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: 通用模組組成一個共用庫存，係數 ×1；每個專用模組有自己的 500 庫存，×2，只存一種貨物。專用模組花費兩倍（30 萬，維護費 5 萬），污染也兩倍（50）。凍結計時不在腳本中。
result: refines
```
