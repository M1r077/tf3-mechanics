---
title: 發車設定：滿載、裝填量與停留時間
summary: 車輛何時離開站點：三種發車模式、每種貨物的裝填量，以及最短、最長與額外停留時間。
domain: stations
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-15
game: 40425
fact: 600 s | 新站點的預設最長停留時間
fact: 30 s / 60 s | 預設額外等待時間上限，道路 / 鐵路
fact: 0–100 % | 裝填量，依貨物計，占車輛容量的比例
---

路線的每個站點都有自己的發車設定，位於該站點的「貨物篩選條件」視窗中（在路線視窗中點擊站點）。它們決定車輛在那裡裝**多少**貨，以及可以等**多久**。

## 設定

| 設定 | 數值 | 新站點 | 來源 |
|---|---|---|---|
| 「若有貨物即裝載」、「滿載（任意）」、「滿載（所有）」 | 三選一 | 若有貨物即裝載（實測） | `cargofilter_window.tl:798-821` |
| 「最短停留時間」 | 0–600 s，間隔 10 | 0 s（實測） | `cargofilter_window.tl:841-845` |
| 「最長停留時間」 | 0–600 s，或「---」（無限制，滑桿在最右端） | **600 s**（實測） | `cargofilter_window.tl:855-863` |
| 「額外等待時間上限」 | 0–600 s，間隔 10 | 60 s；沒有鐵路的道路或電車站為 30 s | `cargofilter_window.tl:827-831`, `line_util.tl:478-490` |
| 「裝填量」，依每種裝載的貨物 | 0–100 %，間隔 1 | 100 % | `cargofilter_window.tl:698-704`, `line_util.tl:472` |

- 點擊時間會開啟一個數字輸入框：大於 600 s 的值可以在那裡輸入（`cargofilter_window.tl:204-208`）。
- 三個時間會維持彼此的順序：把最短時間或額外等待時間調到高於最長時間，最長時間也會跟著提高（`cargofilter_window.tl:834-836`, `cargofilter_window.tl:848-850`）；降低最長時間會同時降低另外兩個（`cargofilter_window.tl:865-869`）。最長時間為「---」時不做任何調整。
- 修改其中任何一項都會把路線標記為自訂：自動配置不再改動它的裝載清單（`cargofilter_window.tl:438`，見[裝載與卸貨速度](loading.html)）。自動配置本身從不改變模式或時間，但會把每個裝填量重設為 100 %（`line_util.tl:495-719`, `line_util.tl:511`, `line_util.tl:543`）。

## 裝填量：每種貨物的上限

裝填量是車輛在本站最多裝載該貨物的數量，以車輛容量的比例表示，四捨五入到最接近的單位（遊戲內實測）。

| 車輛 | 裝填量 | 離開時載有 |
|---|---|---|
| 卡車，容量 15，原木 | 50 % | **8**（7.5 進位） |
| 卡車，容量 22，布料 | 70 % | 每次 **15**（15.4） |
| 列車，容量 18，玻璃 | 48 % | 最多 **9**（8.64） |
| 電車，容量 28，燃料 | 66 % | 最多 **18**（18.48） |

- 車上已有的貨物也算在內：一輛載著 14 燃料抵達的電車離開時載有 18，而不是 14 + 18。
- 超過上限時，不會因此裝貨，**也不會因此卸貨**：一輛載著 22 肥料抵達的卡車（上限 11）離開時仍載有 22。
- **0 %** 表示：不在本站裝載這種貨物。
- 在滿載模式下，達到上限就算滿：裝填量為 50 % 的原木卡車等了約 270 s，離開時載有 15 中的 8，而不是 15。
- 沒有卸貨百分比。卸貨由裝載清單與「抵達時強制卸載所有貨物」決定（[裝載與卸貨速度](loading.html)）。

## 滿載與停留時間

- **若有貨物即裝載**：車輛裝上現有的貨物就離開。
- **滿載（所有）**：車輛一直等到裝滿。原木卡車等了 460–566 s，離開時載有 15 中的 15。
- **滿載（任意）**：一種貨物裝滿時車輛就離開。一列原木與木板列車在 369–380 s 後載著 143 和 144 原木離開；另外兩次約 30 s 後載著 57 和 118 原木的發車無法解釋。
- **最長停留時間**會結束等待，即使什麼都沒裝上。一列滿載（所有）、最長 120 s 的蔬菜列車，要麼約 25 s 內裝滿（64 中的 64），要麼在 116–120 s 後載著 26 或 **0** 離開。使用預設的 600 s 時，它在 596–600 s 後載著 64 中的 26 離開。
- **最短停留時間**是整個停靠時間，包括裝貨，而不是裝貨之後額外的時間：設為 60 s 時，玻璃列車每次都停留 55–61 s，無論裝了多少。
- **額外等待時間上限**：「Maximum wait time after loading to improve vehicle distribution」（`cargofilter_window.tl:828`）。車輛等待按排定時間發車時，車輛視窗顯示「保持安全距離中」（`entity_window_util.tl:2283-2284`），推測就是這段等待期間。
- **同一站點的多輛車會同時裝貨**，無論各自何時抵達（遊戲內觀察）。兩輛相隔約 90 s 抵達的原木卡車在同一秒離開，各載 8。貨物如何在它們之間分配並未測量。

```engine
腳本只儲存設定；車輛何時離開由引擎決定。
```

上面的規則是用 [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 資料庫測量的（每 2 s 一次快照，所以停留時間為 ±2 s），2026 年 11 月。

## 小知識

- 在貨物很少抵達的站點用滿載長時間等待會堵住月台：路線的其他車輛會在它後面排隊。
- 滿載搭配較短的最長停留時間，可能讓車輛在新貨物抵達之前回來時空車離開。
- 有一次，一列滿載（所有）、最長 600 s 的列車停留了 783–992 s。原因沒有找到。

```check
official: "Full load (any): The vehicle will stop and wait until one cargo type is fully loaded. Full load (all): The vehicle will stop and wait until it is fully loaded." "In the vanilla game "all" and "any" only applies to trains and ships […] Any other vehicle type will wait for full load in both cases." Each cargo is loaded "to what percentage of a vehicle's total capacity". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles#departure_configuration))
scripts: 三種發車模式，最短 / 最長停留時間 0–600 s（或無限制），額外等待時間上限 0–600 s（60 s，道路 30 s），每種貨物的裝填量 0–100 %；實測：裝填量限制車上的貨物，四捨五入到最接近的單位，並在滿載時算作裝滿；最長停留時間會結束滿載，即使空車；最短停留時間包括裝貨；同一站點的車輛一起裝貨。
result: refines
```
