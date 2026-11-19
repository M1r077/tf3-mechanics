---
title: 車輛：狀態、年份與裝載速度
summary: 車輛各項數據的含義，狀態和年份如何運作，倉庫和維修站的作用，價格和營運成本從何而來，以及何時替換車輛。
domain: vehicles
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-16
game: 40444
fact: 5 | 個狀態等級，從很差到很好，每級 20 %
fact: 20 % | 觸發車輛狀況警告的狀態
fact: 6 × | 基礎年營運成本：車輛的價格
fact: 4 to 16 | 輛車輛：一座倉庫或維修站的維修容量
---

每輛車輛都有固定數據（速度、容量、裝載速度、價格、營運成本、壽命）和兩個會變化的值：**狀態**和**年份**。狀態在運行時下降，透過維修恢復；年份只會增長。

## 車輛商店中的數據

- 商店用條形顯示每項數據。條形按運輸方式使用固定刻度，刻度隨年份變化（例如船舶裝載速度：2003 年起為 10 到 45）。它不是與其他車輛比較（`vehicle_util.tl:210-245`，`vehicle_util.tl:259-268`）。
- 對於列車，商店顯示其所有組成部分中**最高**的裝載速度（`vehicle_store_util.tl:333`）。
- 檔案中未設定裝載速度、噪音、污染或舒適度的車輛，會得到由其他數據（年份、速度、功率、重量、尺寸）計算出的值（`model_metadata_util.lua:395-417`，`vehicle_metadata_util.lua:233-256`）。計算出的裝載速度四捨五入到 0.5，且不低於 1（`vehicle_metadata_util.lua:267-269`）。

## 哪種車輛裝貨最快？

車輛的裝載速度只是第一個係數；月台和庫存會與它相乘（見[裝載與卸貨速度](loading.html)）。

| 運輸方式 | 條形滿格時的裝載速度（最新時代） | 來源 |
|---|---|---|
| 船舶 | 10 至 45（自 2003 年） | `vehicle_util.tl:219-223` |
| 道路車輛、路面電車 | 0.5 至 10（自 1995 年） | `vehicle_util.tl:232-243` |
| 列車 | 0.1 至 10（自 1981 年） | `vehicle_util.tl:226-229` |
| 飛機 | 1 至 4（自 1978 年） | `vehicle_util.tl:212-216` |

- 船舶的裝載速度遙遙領先，飛機的刻度最低。
- 在商店中用裝載速度一欄比較同一運輸方式的車輛；較新的型號通常條形更高。
- 每種貨物的裝載係數為 0.0625，乘客為 1（`coal.cargo.lua:29`，`passengers.cargo.lua:23`）。

```engine
車輛裝載速度、貨物裝載係數以及月台和庫存係數如何組合成實際裝載時間，由引擎計算。腳本只提供輸入值。
```

## 狀態

| 狀態 | 等級 | 來源 |
|---|---|---|
| 高於 80 % | **極佳** | `vehicle_util.tl:159-172` |
| 60–80 % | **佳** | `vehicle_util.tl:159-172` |
| 40–60 % | **中等** | `vehicle_util.tl:159-172` |
| 20–40 % | **差** | `vehicle_util.tl:159-172` |
| 不超過 20 % | **極差** | `vehicle_util.tl:159-172` |

- 列車的狀態是其所有車廂和機車的**平均值**（`vehicle_util.tl:285-295`）。
- 磨損的車輛會損失最高速度、功率和舒適度，噪音、污染和營運成本會增加（`vehicle_store_util.tl:236-258`）。影響多大、從哪個狀態開始，都是引擎數值。車輛視窗在**狀態**下列出這些懲罰。
- 這些懲罰的強度由**車輛維修效果**（無、低、中、高、極高）決定；設為無時，狀態沒有任何影響（`difficulty_util.tl:42`，`mod.script.tl:242-246`，`vehicle_store_util.tl:166-168`，`vehicle_store_util.tl:216-228`）。詳見：[成本、維護費與貸款](costs.html)。
- 狀態降到 **20 %** 或以下時會出現**車輛狀況**警告，直到車輛回到 **30 %** 以上才消失（`notifications.script.tl:310-318`）。
- 複製的車輛算作新購買：狀態 100 %，新的購買日期（`manager_window.tl:8744-8748`）。

```engine
狀態下降多快、一次維修站造訪恢復多少，以及每項懲罰的大小（getMaintenanceTopSpeedPenalty 等）都是引擎數值。每個車輛型號也可以為每個等級設定自己的最高速度懲罰（`vehicle_store_util.tl:250-253`）。
```

## 倉庫與維修站

車輛由附近的倉庫或維修站維修。每座建築能服務的車輛數量有限：即其**維修容量**。

| 建築 | 維修容量 | 半徑 | 可停放車輛 | 來源 |
|---|---|---|---|---|
| 火車倉庫 | 6 | 800 m | 5 | `rail_depot.script.lua:341-349` |
| 火車維修站 | 12 | 800 m | – | `rail_maint_station.script.lua:151-157` |
| 道路倉庫、路面電車倉庫 | 12 | 400 m | 10 / 8 | `road_depot.script.lua:189-198`，`tram_depot.script.lua:217-226` |
| 道路維修站 | 16 | 600 m | – | `road_maint_station.script.lua:234-240` |
| 船舶倉庫 | 8 | 1000 m | 5 | `water_depot.script.lua:370-379` |
| 船舶維修站 | 12 | 1400 m | – | `water_maint_station.script.lua:256-262` |
| 機場或航空站機庫 | 16 | 550 m | 5 | `af_hangar.module.lua:272-280`，`ap_hangar.module.lua:455-463` |
| 直升機場 | 4 | 800 m | 5 | `heliport.script.lua:300-309` |

- 建築視窗顯示「已用 / 容量」（例如 14 / 12）以及它所服務的車輛清單和各自狀態（`entity_window_util.tl:2010-2039`，`maintenance_station_eow.script.tl:188-215`）。
- 維修容量越滿，建築越吵越髒：排放隨容量的使用比例增加（`emissions.script.tl:223-234`）。
- 火車維修站服務的列車是火車倉庫的兩倍：12 對 6。
- 維修站不能購買或停放車輛，但其半徑常比倉庫大：道路上 600 m 對 400 m，船舶 1400 m 對 1000 m。路面電車由路面電車倉庫和道路維修站維修；道路倉庫不維修路面電車（`tram_depot.script.lua:209`，`tram_depot.script.lua:226`）。
- 官方 wiki 建議用路徑點讓車輛經過維修建築。

```engine
車輛被分配到哪個維修站、使用維修站的車輛超過其容量時會怎樣，以及使用的服務半徑，由引擎決定。
```

## 價格與營運成本

- 基礎遊戲的車輛沒有固定價格：營運成本來自速度和容量，價格為基礎年營運成本的 **6 倍**，在套用車輛成本和車輛維修設定之前（`model_metadata_util.lua:548-549`）。只有兩項設定相同時，才正好等於 6 年的營運成本。完整公式：[成本、維護費與貸款](costs.html)。
- **車輛成本**將價格在 50 % 到 150 % 之間調整（`post_run_util.tl:54-81`），**車輛維修**以同樣方式調整營運成本。在一個存檔的 921 輛載具上以 75 %、100 %、125 % 分別載入並在遊戲內實測：營運成本與滑桿一致（中位數 ×0.75 和 ×1.25；在兩次載入之間狀態有變化的載具略有偏差）。
- 狀態差的車輛在基礎值之上支付更多營運成本（`vehicle_store_util.tl:256-259`）。

## 年份與壽命

- 每個型號都有**壽命**（`vehicle_util.tl:31-34`）。路線視窗的**年份**一欄顯示車齡；其提示顯示剩餘時間，或**已達使用年限**（`line_eow.script.tl:136-150`）。在達到壽命之前，該提示中的壽命比例顯示 **0 %**：腳本在顯示前把比例無條件捨去（`line_eow.script.tl:142`），而同一比例在別處是完整計算的（`vehicle_util.tl:311`）。請改看剩餘時間。
- 對於列車，以**最老**的組成部分為準（`vehicle_util.tl:36-52`）。一節舊車廂就會讓整列車顯示為舊車。

```engine
達到壽命後會改變什麼（例如狀態下降更快或售價更低）不在腳本中。腳本只顯示車齡和壽命。
```

## 何時應替換舊車輛？

1. 即使附近有維修站，**狀態仍然很低**：車輛會損失速度並支付更多營運成本。先檢查維修站的容量：它可能已滿。
2. 年份提示中顯示**已達使用年限**：該型號已超過計畫壽命。
3. **有更好的型號**：更快或更大的車輛營運成本更高，但運量更大（價格隨速度 × 容量變化）。
4. 在路線管理器中使用**替換車輛**。它會開啟商店，並與目前車輛進行比較（`vehicle_store_window.tl:4997-5032`，`vehicle_store_window.tl:2678`）。

```tip scripts
**倉庫旁的車輛狀態還是很差？打開它的視窗，看看「已用 / 容量」。** 火車倉庫服務 6 列火車，火車維修站服務 12 列。引擎如何處理超出容量的車輛不在腳本中；再建一座建築最穩妥。
```

## 小提示

- 建造足夠的維修能力：一座火車倉庫只服務 6 列列車。
- **車輛維修效果**設為無時，狀態無關緊要。
- **派遣至倉庫**會把車輛送到最近的可到達倉庫，而不是購買它的那座倉庫（官方 wiki）。
- [Vehicle Comparison](https://mod.io/g/transportfever3/m/vehicle-comparison) 可在替換前幫助比較型號。

```check
official: "This section shows how well the vehicle is maintained and how the maintenance state affects the vehicle properties." "Loading speed modifies a vehicle's base loading speed which can be seen in the vehicle window or in the vehicle store." ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles))
scripts: 五個狀態等級，每級 20 %；低於 80 % 時速度、功率、舒適度、排放和營運成本受到懲罰，強度由車輛維修效果調整；20 % 時警告，高於 30 % 時解除。每座建築的維修容量為 4 至 16 輛車輛。價格 = 6 年營運成本。列車的年份 = 其最老的組成部分。缺失的裝載速度由其他數據計算，四捨五入到 0.5，至少為 1。
result: refines
```
