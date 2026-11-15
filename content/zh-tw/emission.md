---
title: 汙染與噪音
summary: 什麼會產生噪音和汙染，建築何時排放更多，城鎮如何評價它，以及產業綠化和淨化廠實際做什麼。
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
fact: 65–80 dB | 城鎮噪音：65 時滿分，80 時為零
fact: 60–74 dB | 城鎮汙染：60 時滿分，74 時為零
fact: −80 % | 綠化後產業的噪音和汙染
fact: 700 m | 淨化廠的作用範圍
---

車輛、軌道、道路、車站、車庫、貨物倉庫和產業都會產生**噪音**和**汙染**。城鎮的兩項評價**噪音**和**汙染**，把到達城鎮的量與固定界限比較。評價差會降低城鎮管理機關評價，進而降低成長（見 [城鎮](towns.html)）。

## 建築何時排放更多

一個遊戲腳本每隔幾次更新，在安靜水準與繁忙水準之間設定四類建築的排放（`emissions.script.tl:12-18`）：

| 建築 | 何時排放更多 | 來源 |
|---|---|---|
| **產業** | 生產時，每次加成（貨物或工人）再增加；輸出庫存滿時減半 | `emissions.script.tl:152-194` |
| **車站** | 越繁忙越多：等待的人和貨物與容量相比 | `emissions.script.tl:211-222` |
| **車庫**、**維修站** | 使用其維修的車輛越多越多 | `emissions.script.tl:223-234` |
| **貨物倉庫** | 庫存越滿越多 | `emissions.script.tl:237-250` |

- 閒置的產業預設不排放；生產、加成一次、加成兩次逐級上升（`industryutil.lua:470-475`）。例如煤礦的汙染從 10 升到 20 和 30（見 [產業](industries.html)）。
- 輸出沒人運走的產業會回落到閒置水準：為它提供運輸會提高它的汙染。
- 車輛和軌道也會排放；在**車輛維修效果**設定下，狀況差的車輛排放更多（見 [成本、維護費與貸款](costs.html)）。

## 建造選單顯示什麼

| 建築 | 噪音 | 汙染 | 來源 |
|---|---|---|---|
| 港口 | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| 機場 | 8–56 | 80–560 | `airport.tl:28-29` |
| 火車站 | 25 | 45–350 | `modular_station.con.lua:97-98` |
| 鐵路車庫 | 50 | 100 | `rail_depot.con.lua:32-33` |
| 道路與電車車庫 | 40 | 80 | `road_depot.con.lua:30-31`，`tram_depot.con.lua:32-33` |
| 地下車站 | 40 | 80 | `underground_station.con.lua:75-76` |
| 卡車與公車站 | 1–10 | 12–76 | `modular_terminal.con.lua:67-68` |
| 維修站 | 20 | 40–50 | `road_maint_station.con.lua:30-31`，`rail_maint_station.con.lua:30-31` |
| 貨物倉庫 | 20 | 25 或 50 | `warehouses/warehouse.tl:73-74` |

兩個數值是安靜水準和繁忙水準。讓港口、機場和大型貨運站遠離住宅。

## 城鎮如何評價

| 評價 | 測量 | 滿分 | 零 | 來源 |
|---|---|---|---|---|
| **噪音** | 城鎮建築處的噪音 | 65 dB 或以下 | 80 dB | `town_util.tl:433-443`，`emission_config.tl:10-11` |
| **汙染** | 整個城鎮面積的平均值，按 5 到 10 km² 計 | 60 dB 或以下 | 74 dB | `town_util.tl:413-431`，`emission_config.tl:23-30` |

- 只有**住宅**區受噪音影響；商業和工業建築不受影響（官方 wiki）。住宅的視窗顯示其位置的噪音（`town_building.tl:165-183`）。
- 汙染按整個面積平均，所以遠離中心的一個汙染源，在大城鎮中比在小城鎮中分量更輕。
- **噪音靈敏度**和**汙染靈敏度**設定會移動界限：兩倍的靈敏度相當於 +3 dB（`town_util.tl:426-428`，`town_util.tl:439-441`）。

| 檔位 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 來源 |
|---|---|---|---|---|---|---|---|---|
| 噪音 | 關閉（始終滿分） | ×¼ | ×½ | ×1 | ×1.4 | ×1.8 | ×3.5 | `difficulty_util.tl:48` |
| 汙染 | 關閉（始終滿分） | ×¼ | ×½ | ×1 | ×1.7 | ×3 | ×5 | `difficulty_util.tl:49` |

預設簡單、中等、困難和非常困難使用檔位 3、4、5 和 6（`difficulty_util.tl:114-115`，`difficulty_util.tl:142-143`，`difficulty_util.tl:169-170`，`difficulty_util.tl:196-197`）。

## 產業綠化

| | | 來源 |
|---|---|---|
| 效果 | 產業的噪音和汙染 ×0.2（−80 %），永久 | `emission_config.tl:32`，`emissions.script.tl:184-192` |
| 次數 | 公司等級 3、6、9、12 和 15 各一次 | `industry_greenify_tool.script.tl:99-104` |
| 限制 | 每個產業一次；第二次嘗試不消耗許可 | `company.script.tl:489-494` |

- 效果綁定在該版本的產業上：產業被重建時效果消失（`emissions.script.tl:187-190`）。
- 最佳用法：緊鄰城鎮的最繁忙產業，因為加成後的產業排放最多。

## 淨化廠

一項公司特權，可清除周圍的汙染。

| | | 來源 |
|---|---|---|
| 價格 | 1 億 | `pollution_cleanup_facility.script.lua:560` |
| 每年維護費 | 1000 萬 | `pollution_cleanup_facility.script.lua:561` |
| 可用 | 公司等級 10 時 15 個 | `pollution_cleanup_facility.con.lua:106-108` |
| 需要 | **機械**：每週期 8 個，每年兩個週期；20 名工人 | `pollution_cleanup_facility.con.lua:43-60` |
| 範圍 | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| 狀態 | 汙染 | 噪音 | 來源 |
|---|---|---|---|
| 閒置（無機械） | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| 運作中 | −10,000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| 加成一次 | −20,000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| 加成兩次 | −40,000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

- 沒有機械時它幾乎沒用：必須像產業一樣供應。
- 它很吵：蓋在住宅區以外，距離汙染區 700 m 以內。
- 它的工人加成係數為 ×2（`pollution_cleanup_facility.script.lua:549`）。見 [工人](workers.html)。

## 小提示

- 打開城鎮視窗或噪音與汙染圖層，可以看到評價和熱點。
- 輸出庫存滿會讓產業排放減半，但你會失去它的貨物：與其餓著產業，不如讓城鎮搬開。
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) 和 [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 可以幫你找到最繁忙的車站。

```engine
引擎計算噪音和汙染地圖、數值如何擴散、車輛和軌道的排放，以及產業何時重建。腳本只設定每座建築的水準和城鎮的界限。
```

```check
official: "Noise reflects noise levels in residential areas." "Pollution reflects pollution levels across the town area." 住宅區 "is sensitive to noise"；商業區 "is robust against the influence of noise"。([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: 噪音評價 65 → 80 dB，汙染 60 → 74 dB，按 5–10 km² 平均；靈敏度增加 10·log10 dB；產業、車站、車庫和貨物倉庫繁忙時排放更多；輸出庫存滿時產業排放減半；綠化每個產業一次 −80 %；淨化廠在 700 m 內最多清除 40,000 汙染，並需要機械。
result: refines
```
