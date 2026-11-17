---
title: 街道、軌道、橋梁與號誌
summary: 每種軌道與街道的速度、價格與維護費，橋梁、隧道、平交道與號誌的花費與作用，林蔭道與隔音牆到底改變了什麼，以及車庫在哪裡說明。
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40425
fact: 100 / 160 / 350 km/h | 簡易軌道、標準軌道與高速軌道
fact: ×9 | 高速軌道相對簡易軌道的價格與維護費
fact: +30 % | 為軌道加上電纜的價格
fact: -65 % | 裝了隔音牆的街道或軌道的噪音
---

每種街道與軌道都有最高速度、每公尺價格與每公尺每年的維護費，都寫在它的檔案裡。橋梁、平交道與部分街道裝飾會附加自己的速限。以下費用是 **基礎設施成本** 與 **基礎設施維護** 為 100 % 時的數值（見 [成本、維護費與貸款](costs.html)）。

## 軌道

| 軌道 | 開放時間 | 最高速度 | 每公里建造費 | 每公里每年維護費 | 來源 |
|---|---|---|---|---|---|
| 簡易軌道 | 開局 | 100 km/h | 6 萬 | 1 萬 | `simple.street_template.lua:9`，`simple.street_template.lua:28`，`simple.street_template.lua:33` |
| 標準軌道 | 1930 | 160 km/h | 18 萬 | 3 萬 | `standard.street_template.lua:4`，`standard.street_template.lua:11`，`standard.street_template.lua:30`，`standard.street_template.lua:35` |
| 高速軌道 | 1980 | 350 km/h | 54 萬 | 9 萬 | `high_speed.street_template.lua:4`，`high_speed.street_template.lua:11`，`high_speed.street_template.lua:30`，`high_speed.street_template.lua:35` |

- **電纜** 比軌道貴 **30 %**（`mod.script.tl:24-25`）。簡易軌道從 1921 年起可用，較新的類型從開放起就可用（`simple_catenary.street_template.lua:4`）。檔案裡它每年沒有額外費用：電氣化版本的維護費相同（`simple_catenary.street_template.lua:34`）。
- 三種軌道的坡度與彎道條件相同：建造時 **8.5 %**（**坡度** 滑桿的上限），軌道形狀最多 13 %，彎道半徑建造時 55 m，最小 40 m（`standard.street_template.lua:36-37`，`standard.street_template.lua:48-49`，`construction_react_util.tl:241-242`，`construction_react_util.tl:1821`）。
- 軌道本身的污染隨類型增加：2、4、6（`simple.street_template.lua:18`，`standard.street_template.lua:20`，`high_speed.street_template.lua:20`）。

```engine
彎道讓列車減速多少（每種軌道的 speedCoeffs），以及建造工具為彎道顯示的速度，都由引擎計算。
```

```tip scripts
高速軌道的建造費與每年維護費都是簡易軌道的 9 倍。只在列車真的跑得比 160 km/h 快的地方鋪設；其他地方用標準軌道就夠了，慢速貨運支線用簡易軌道即可。
```

## 街道

| 街道 | 年份 | 最高速度 | 每公里建造費 | 每公里每年維護費 | 來源 |
|---|---|---|---|---|---|
| 狹窄街道（舊） | 1940 年以前 | 20 km/h | 3.6 萬 | 6,000 | `town_old_xsmall.street_template.lua:4-5`，`town_old_xsmall.street_template.lua:8`，`town_old_xsmall.street_template.lua:27`，`town_old_xsmall.street_template.lua:56` |
| 小型街道（舊） | 1940 年以前 | 40 km/h | 6 萬 | 1 萬 | `town_old_small.street_template.lua:8`，`town_old_small.street_template.lua:27`，`town_old_small.street_template.lua:56` |
| 大型街道（舊） | 1940 年以前 | 60 km/h | 18 萬 | 3 萬 | `town_old_large.street_template.lua:8`，`town_old_large.street_template.lua:27`，`town_old_large.street_template.lua:88` |
| 狹窄街道（新） | 1940 年起 | 30 km/h | 12 萬 | 2 萬 | `town_new_xsmall.street_template.lua:4`，`town_new_xsmall.street_template.lua:11`，`town_new_xsmall.street_template.lua:30`，`town_new_xsmall.street_template.lua:59` |
| 小型街道（新） | 1940 年起 | 50 km/h | 18 萬 | 3 萬 | `town_new_small.street_template.lua:11`，`town_new_small.street_template.lua:30`，`town_new_small.street_template.lua:59` |
| 中型街道（新） | 1940 年起 | 50 km/h | 36 萬 | 6 萬 | `town_new_medium.street_template.lua:11`，`town_new_medium.street_template.lua:30`，`town_new_medium.street_template.lua:75` |
| 大型街道（新） | 1940 年起 | 60 km/h | 54 萬 | 9 萬 | `town_new_large.street_template.lua:11`，`town_new_large.street_template.lua:30`，`town_new_large.street_template.lua:91` |
| 小型鄉村道路（舊） | 1940 年以前 | 60 km/h | 6 萬 | 1 萬 | `country_old_small.street_template.lua:8`，`country_old_small.street_template.lua:29`，`country_old_small.street_template.lua:58` |
| 小型鄉村道路（新） | 1940 年起 | 80 km/h | 18 萬 | 3 萬 | `country_new_small.street_template.lua:10`，`country_new_small.street_template.lua:31`，`country_new_small.street_template.lua:60` |
| 單線道高速公路 | 1940 年起 | 100 km/h | 18 萬 | 3 萬 | `highway_new_small.street_template.lua:10`，`highway_new_small.street_template.lua:32`，`highway_new_small.street_template.lua:53` |
| 二線道高速公路 | 1940 年起 | 120 km/h | 36 萬 | 6 萬 | `highway_new_medium.street_template.lua:10`，`highway_new_medium.street_template.lua:32`，`highway_new_medium.street_template.lua:61` |
| 三線道高速公路 | 1940 年起 | 120 km/h | 54 萬 | 9 萬 | `highway_new_large.street_template.lua:10`，`highway_new_large.street_template.lua:32`，`highway_new_large.street_template.lua:69` |
| 輕軌軌道（舊） | 1910 年以前 | 40 km/h | 3.6 萬 | 6,000 | `tram_old.street_template.lua:4-5`，`tram_old.street_template.lua:8`，`tram_old.street_template.lua:27`，`tram_old.street_template.lua:40` |
| 輕軌軌道（新） | 1925 年起 | 100 km/h | 12 萬 | 2 萬 | `tram_new.street_template.lua:4`，`tram_new.street_template.lua:9`，`tram_new.street_template.lua:29`，`tram_new.street_template.lua:42` |

- **1940 年的更替** 讓城鎮街道快 10 km/h，但建造與每年維護都貴 **三倍**：小型街道從每公里 6 萬變成 18 萬。
- 鄉村道路的中型與大型版本速度相同，花費是小型的 2 倍與 3 倍（`country_new_large.street_template.lua:10`，`country_new_large.street_template.lua:31`）。
- 為街道加上：**公車專用道** +10 %，**輕軌軌道** +20 %，**電氣化輕軌軌道** +40 % 的街道價格（`mod.script.tl:24-28`）。
- 玩家通常不擁有街道，即使是玩家自己建的；街道工具可以改變街道的擁有者（官方 wiki）。街道的維護費由誰支付由引擎決定。

## 林蔭道與隔音牆

| 工具 | 噪音 | 污染 | 最高速度 | 位置 | 來源 |
|---|---|---|---|---|---|
| 林蔭道工具（樹木） | -10 % | -50 % | **-25 %** | 有人行道的街道，不能在橋上或隧道內 | `alley.edge.lua:39-40`，`alley.edge.lua:53-56` |
| 隔音牆工具 | -65 % | 不變 | 不變 | 街道與軌道，不能在隧道內 | `barrier_b.edge.lua:43`，`barrier_b.edge.lua:47`，`barrier_track_b.edge.lua:43` |

- 兩者在檔案裡都是 100、每年 10，與街道每公尺的寫法一樣（`alley.edge.lua:8`，`alley.edge.lua:12`，`barrier_b.edge.lua:7`，`barrier_b.edge.lua:11`）。
- 建造選單裡「有樹木」與「有隔音牆」的街道，就是已經裝好這些裝飾的同一種街道（`town_new_medium_trees.street_template.lua:12-14`）。建造選單會把它們的效果加總（`construction_react_util.tl:2116-2139`）。
- 所以有樹木的街道 **慢四分之一**：有樹木的新中型街道只能跑約 38 km/h，而不是 50。

```tip scripts
對付噪音，用隔音牆：-65 %，而且不損失速度。樹木是對付污染的工具（-50 %），但會讓街道慢四分之一。
```

城鎮如何評價噪音與污染：[污染與噪音](emission.html)。

## 橋梁與隧道

| 橋梁 | 年份 | 最高速度 | 用於 | 基礎價格 | 來源 |
|---|---|---|---|---|---|
| 石橋 | 開局起 | 90 km/h | 軌道、街道 | 200 | `stone.bridge.lua:169-170`，`stone.bridge.lua:181-183`，`stone.bridge.lua:193` |
| 棧橋 | 1970 年以前 | 60 km/h | 軌道用與街道用各一種 | 100 | `trestle.bridge.lua:200-201`，`trestle.bridge.lua:212-214`，`trestle.bridge.lua:226`，`trestle_s.bridge.lua:212` |
| 鋼構橋 | 1940 年起 | 140 km/h | 軌道、街道 | 200 | `steel.bridge.lua:243`，`steel.bridge.lua:259`，`steel.bridge.lua:269` |
| 吊橋 | 1940 年起 | 180 km/h | 軌道、街道 | 600 | `suspension.bridge.lua:277`，`suspension.bridge.lua:294`，`suspension.bridge.lua:304` |
| 混凝土橋 | 1970 年起 | 280 km/h | 軌道、街道 | 200 | `concrete.bridge.lua:162`，`concrete.bridge.lua:176`，`concrete.bridge.lua:187` |
| 斜張橋 | 2000 年起 | 220 km/h | 軌道、街道 | 750 | `cable.bridge.lua:214`，`cable.bridge.lua:231`，`cable.bridge.lua:240` |
| 繫拱橋 | 2010 年起 | 350 km/h | 軌道、街道 | 650 | `tarch.bridge.lua:253`，`tarch.bridge.lua:270`，`tarch.bridge.lua:280` |

- 橋梁速限 **疊加在** 軌道速限之上：高速路線經過鋼構橋時，在橋上以 140 km/h 行駛。1970 年以前沒有超過 180 km/h 的橋，2010 年以前沒有允許 350 km/h 的橋。
- **隧道**（岩石隧道，1970 年起有混凝土隧道）在檔案中 **沒有速限**，基礎價格都是 600（`tunnel_a.tunnel.lua:187-188`，`tunnel_a_car.tunnel.lua:185`，`tunnel_b.tunnel.lua:191-194`）。
- 橋梁與隧道的價格跟隨基礎設施成本（`post_run_util.tl:50-51`）。

```engine
橋梁或隧道的基礎價格由引擎依高度或深度（costFactors）換算成每公尺價格；官方 wiki 說價格取決於長度以及離地高度或地下深度。因此同樣的基礎價格，帳單可能相差很大。隧道會降低城鎮的聲望（見 [聲望](reputation.html)）。
```

```tip scripts
1970 年以前要讓快速路線跨越山谷，吊橋（180 km/h）是唯一快於 140 km/h 的橋；隧道則完全沒有速限。
```

## 平交道與號誌

| 類型 | 年份 | 軌道最高速度 | 價格 | 來源 |
|---|---|---|---|---|
| 簡易平交道 | 1850 - 1925 | 120 km/h | 4,000 | `era_a_eu.rcr.lua:14-17`，`era_a_eu.rcr.lua:26` |
| 半遮斷式平交道 | 1925 - 1975 | 160 km/h | 1.6 萬 | `era_b_eu.rcr.lua:15-18`，`era_b_eu.rcr.lua:27` |
| 現代化半遮斷式平交道 | 1975 年起 | 160 km/h | 1.6 萬 | `era_c_eu.rcr.lua:15-17`，`era_c_eu.rcr.lua:26` |
| 路徑號誌（1950 年以前為臂木式，1950 年起為色燈式） | 全部 | - | 9,000，每年維護費 1,500 | `signal_path_a.con.lua:4-5`，`signal_path_a.con.lua:10-11`，`signal_path_c.con.lua:4-5` |

- 平交道把軌道限制在最多 160 km/h：高速路線需要用橋梁或隧道跨越街道。
- 每個號誌都可以設為 **單行道**（`signal_path_a.con.lua:51-52`）。號誌如何把軌道劃分為閉塞區間，見官方 wiki 的鐵路號誌頁面。

## 車庫與維修站

車庫與維修站的花費、能服務多少載具以及服務半徑：[路線與載具](vehicles.html) 與 [成本、維護費與貸款](costs.html)。

## 須知

- 1940 年以前，升級城鎮街道很便宜；1940 年以後，每條新建或重建的城鎮街道價格與維護費都是三倍。
- 在快速路線上，檢查每座橋與每個平交道：最慢的那個決定了那裡的速度。
- 速度只有在帶來更多趟次時才划算（見 [為什麼我在虧錢？](money.html)）。

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: 軌道、街道與橋梁的速度與官方表格相同。檔案中橋梁速限也適用於街道，隧道沒有速限，平交道把軌道限制在 120 或 160 km/h，樹木讓街道慢 25 %、污染減少 50 %，但噪音只減少 10 %；而隔音牆讓噪音減少 65 %，且不降低速度。
result: refines
```
