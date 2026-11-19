---
title: 地標、慶祝活動與趣味元素
summary: 每個地標需要多少貨物、何時解鎖、對所在城鎮車輛有什麼作用，地標所需資源 設定如何縮放它，以及慶祝活動、煙火、飛艇和 UFO 實際做了什麼。
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40444
fact: 9 + 3 | 個地標：基礎遊戲 9 個（等級 2 到 15），DLC 包再加 3 個（等級 1）
fact: +20 % / +25 % / -20 % / -25 % | 所在城鎮車輛的最高速度、污染或舒適度
fact: ×0 到 ×4 | 地標所需資源 設定下所需貨物的倍率
fact: 2–4 年 | 兩次 UFO 之間的間隔
---

地標像工地一樣建造：用公司等級解鎖，放置後**運送貨物**過去。工地收齊所有貨物後，地標完成，並為**所在城鎮**的車輛提供加成。總部是另一棟建築，有自己的規則（見[公司等級、特權與總部](company.html)）。

## 地標一覽

貨物數量依 **地標所需資源** ×1（普通）計算。

| 地標 | 等級 | 需運送的貨物 | 所在城鎮車輛的加成 | 來源 |
|---|---|---|---|---|
| **圓形劇場** | 2 | 800 石材 | 道路車輛：噪音 **-25 %** | `arena.con.lua:10`，`arena.con.lua:20-26`，`arena.con.lua:39` |
| **大燈塔** | 5 | 1,200 石材，200 燃料 | 船舶：最高速度 **+20 %** | `lighthouse.con.lua:10`，`lighthouse.con.lua:14`，`lighthouse.con.lua:29`，`lighthouse.con.lua:48` |
| **姬路城** | 7 | 1,200 石材，400 木板 | 列車：污染 **-20 %** | `white_heron_castle.con.lua:10`，`white_heron_castle.con.lua:14`，`white_heron_castle.con.lua:28`，`white_heron_castle.con.lua:47` |
| **船舶博物館** | 9 | 600 原木，600 木板，200 布料 | 船舶：舒適度 **+25 %** | `ship_museum.con.lua:10-18`，`ship_museum.con.lua:36`，`ship_museum.con.lua:55` |
| **新天鵝堡** | 10 | 1,000 石材，600 木板，200 染料 | 道路車輛：舒適度 **+25 %** | `neuschwanstein.con.lua:10-18`，`neuschwanstein.con.lua:36`，`neuschwanstein.con.lua:55` |
| **自由女神像** | 11 | 800 石材，400 鋼，400 板金屬 | 船舶：污染 **-20 %** | `statue_of_liberty.con.lua:10-18`，`statue_of_liberty.con.lua:38`，`statue_of_liberty.con.lua:57` |
| **頤和園** | 13 | 600 石材，300 木板，300 染料，300 家具 | 飛機：污染 **-20 %** | `summer_palace.con.lua:10-22`，`summer_palace.con.lua:44`，`summer_palace.con.lua:63` |
| **歌劇院** | 14 | 800 石材，400 玻璃，400 板金屬，400 布料 | 列車：舒適度 **+25 %** | `opera_house.con.lua:10-22`，`opera_house.con.lua:44`，`opera_house.con.lua:63` |
| **國會大廈** | 15 | 800 石材，400 木板，400 玻璃，400 家具 | 道路車輛、列車、船舶與飛機：最高速度 **+20 %** | `westminster.con.lua:10-22`，`westminster.con.lua:45`，`westminster.con.lua:79` |

**DLC 地標。** 兩個 DLC 包再增加三個，從等級 1 起解鎖。它們的檔案位於遊戲的 DLC 資料夾（Deluxe Upgrade Pack 與 Pre-order Pack）中，不在本 wiki 索引的基礎檔案之內，因此這裡沒有來源連結。

| 地標 | DLC | 等級 | 需運送的貨物 | 所在城鎮車輛的加成 |
|---|---|---|---|---|
| **艾菲爾鐵塔** | Deluxe Upgrade Pack | 1 | 400 鋼 | 道路車輛：最高速度 **+25 %** |
| **泰姬瑪哈陵** | Deluxe Upgrade Pack | 1 | 800 石材 | 飛機：噪音 **-25 %** |
| **大金字塔** | Pre-order Pack | 1 | 800 石材 | 列車：最高速度 **+25 %** |

- 每個地標由其等級解鎖一次；等級如何提升見[公司等級、特權與總部](company.html)。
- 在檔案中，地標的建造費與每年費用都是零：只需要貨物（`arena.con.lua:59-64`）。
- 工地每次只能存放每種貨物的一半，所以每種貨物至少要送兩次（`arena.con.lua:13-18`）。

## 建造地標

- 工地有 **4 個階段**。隨著貨物到達而推進：全部貨物的三分之一時進入階段 2，三分之二時進入階段 3，100 % 時完成。每種貨物只計到它自己的數量，所以多餘的石材不能彌補缺少的木板（`landmarks.script.tl:34-46`）。
- 加成只在地標**完成**後才生效（`landmark_util_serialized.tl:393-395`）。此時會出現「建設完成」訊息（`landmarks.script.tl:49-61`）。
- **地標所需資源** 設定會讓所有貨物乘上倍率：無 ×0、低 ×0.5、普通 ×1、高 ×2 或 極高 ×4。預設組合為簡單 ×0.5、普通 ×1、困難 ×2、極度困難 ×4。在 ×0 時，地標一放置就完成（`difficulty_util.tl:40`，`difficulty_util.tl:107`，`difficulty_util.tl:135`，`difficulty_util.tl:162`，`difficulty_util.tl:189`，`landmarks.script.tl:38`，`landmarks.script.tl:46`）。

## 誰獲得加成

- 加成給予**離地標最近的城鎮**，以及最近城鎮就是該城鎮的、所列運輸方式的車輛（`landmark_util.tl:6-47`，`landmarks.script.tl:208-236`）。
- 車輛駛入另一城鎮的區域時，會獲得那個城鎮的加成並失去原來的加成（`landmarks.script.tl:279-299`）。
- 同一城鎮中多個地標的加成會**疊加**：兩個 +20 % 最高速度得到 +40 %（`landmark_util.tl:46`，`vehicle_modifier.script.tl:3-16`）。

```engine
地標或行駛中車輛的「最近城鎮」由引擎決定（getConstructionClosestTown，closestTown）。+25 % 舒適度或 +20 % 最高速度如何轉化為行程與收入，也是引擎的工作。
```

```tip scripts
把國會大廈建在你的車輛運行最多的城鎮：所有運輸方式最高速度 +20 %。同一城鎮的船舶還能從大燈塔再得 +20 %。集中管理成就要求 10 個最近城鎮相同的已完成地標；總部不計入，因為它沒有需運送的貨物。基礎遊戲有 9 個地標，DLC 包再加 3 個（已清點）；沒有 DLC 能否達成集中管理尚不清楚（見[成就](achievements.html)）。
```

## 慶祝活動

慶祝活動是某件事第一次發生時在城鎮上方顯示的小派對。它還會提高城鎮的**聲望**，但僅在聲望尚未滿時。

| 事件 | 聲望 | 來源 |
|---|---|---|
| 城鎮中第一位乘客搭上你的路線 | +50 % | `celebrations.script.tl:228-252` |
| 第一次向城鎮運送貨物 | +50 % | `celebrations.script.tl:187-198` |
| 城鎮升級 | +50 % | `celebrations.script.tl:260-272` |
| 第一次向某個產業運送貨物 | 離它最近的城鎮 +20 % | `celebrations.script.tl:202-219` |

- 城鎮升級時還會放**煙火**，除非已將其關閉（`town_growth.script.tl:108-112`）。
- 聲望如何運作：[聲望](reputation.html)。

## 趣味元素

- 在某個城鎮開始行銷活動時，會有一艘**飛艇**飛過該城鎮（`fun_elements.script.tl:112-117`）。
- 地圖上沒有 UFO 時，每隔遊戲時間 **2 到 4 年**（隨機）會出現一個 **UFO**（`fun_elements.script.tl:10`，`fun_elements.script.tl:79-91`）。點擊它可獲得第三類接觸成就。
- 它們都不會改變經濟。

## 須知

- 建造前先選好城鎮：加成不跟隨你的路線，只作用於該城鎮附近的車輛。
- 極度困難下地標需要四倍貨物：國會大廈需要 3,200 石材以及其他貨物各 1,600。

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: 九個基礎地標，等級 2 到 15 每級最多一個，另有三個 DLC 地標位於等級 1，都用運送的貨物分 4 個階段建成，並依 地標所需資源 ×0 到 ×4 縮放。完成後，每個地標為其最近城鎮中一種運輸方式的車輛提供一項加成（+20 % 或 +25 % 最高速度、-20 % 污染、-25 % 噪音或 +25 % 舒適度）；加成可疊加。慶祝活動增加 50 % 或 20 % 聲望；UFO 每 2 到 4 年出現一次。
result: adds
```
