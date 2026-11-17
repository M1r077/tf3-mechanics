---
title: 通知與警告
summary: 每則警告何時出現、何時消失：卡住的車輛、無法使用或擁擠的車站、路線與站點問題、城鎮評價、車輛狀況、即將關閉的工業，以及哪些警告預設不記入記錄。
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 5 分鐘 | 車輛靜止多久遊戲時間後被回報為卡住
fact: 20 % | 觸發警告的狀況，直到車輛回到 30 % 以上
fact: 11 | 新遊戲中關閉的通知類型
fact: 75 天 | 兩次檢查無道路連接車站的間隔
---

大多數警告是**持續性**的：遊戲腳本會反覆檢查狀況，問題存在時警告一直保留，問題解決後自行結束。檢查輪流分攤在 4 次更新中，因此警告出現或消失可能需要一點時間（`notifications.script.tl:13`，`notifications.script.tl:49`）。

## 每則警告何時出現

| 警告 | 出現條件 | 消失條件 | 來源 |
|---|---|---|---|
| **車輛卡住** | 你的某輛車輛正在行駛途中，不是被你停下的，且已有遊戲時間 **5 分鐘**速度為 0 | 它重新移動 | `notifications.script.tl:557-580` |
| **車站無法運作** | 車站沒有任何站台上下乘客，且涵蓋範圍內**什麼都沒有**（沒有倉庫、工業或城鎮建築），同時你的某條路線停靠該站 | 有東西進入涵蓋範圍 | `notifications.script.tl:602-617`，`notifications.script.tl:630-647`，`station_useless.script.tl:39` |
| **站點擁擠** | 車站等候的乘客或貨物超過容量（溢出），同時你的某條路線停靠該站；乘客會離開 | 溢出結束 | `notifications.script.tl:599`，`notifications.script.tl:649-661`，`overcrowding.script.tl:23` |
| **車輛狀況** | 你的某輛車輛狀況為 **20 %** 或更低 | 回到 **30 %** 以上 | `notifications.script.tl:310-318` |
| **城鎮評價極差** | 城鎮的某項評價降到極差（低於 1/6） | 評價回到中等或更好 | `notifications.script.tl:230-238`，`town_util.tl:763-769`，`town_util.tl:983-985` |
| **城鎮評價正在下降** | 某項評價為差或中等（低於 50 %），且不在極差警告中 | 評價為佳或更好 | `notifications.script.tl:240-248` |
| **工業關閉** | 某個工業開始關閉倒數 | 它關閉，或及時重新被使用 | `notifications.script.tl:439-451`，`industry_close.script.tl:53-59` |
| **無道路連接** | 車站未連接道路；每 **75 天**檢查一次 | 下一次檢查發現道路 | `notifications.script.tl:16`，`notifications.script.tl:423-436` |
| **貨物卸載問題** | 車輛的貨物在其路線上從未被卸下 | 貨物被卸下 | `notifications.script.tl:277-290`，`cargo_rtc_warning.script.tl:28-37` |

- **在車庫中**的車輛永遠不算卡住：腳本中關閉了這項檢查（`notifications.script.tl:563-564`）。被你停下的車輛也不算。
- 車站無法運作的檢查只看涵蓋範圍。已經有乘客在站台上下車的車站永遠不會被回報（`notifications.script.tl:606-610`）。
- 如何提高城鎮評價：見[城鎮成長](towns.html)與[聲望](reputation.html)。關閉倒數如何運作以及如何阻止：見[工業](industries.html)。狀況對車輛的影響：見[成本、維護費與貸款](costs.html)。

```engine
車站是否溢出、車輛是否有路徑、路線能否抵達其車站、兩座城鎮之間的行程最多可以多長，都由引擎判斷（calculateStationGroupCargo、getVehicleProblems、getLineProblems、getTownProblems）。腳本只是把它的結果變成警告。
```

```tip scripts
車輛卡住、車輛問題、車輛狀況、站點擁擠與車站無法使用在新遊戲的記錄中是關閉的。在通知設定中開啟它們：這些警告會告訴你壅塞、缺少路徑或車隊老化。
```

## 路線、站點與車輛問題

這些直接來自引擎對你的路線與車輛的檢查；腳本為每一種加上標題。

| 警告 | 情況 | 來源 |
|---|---|---|
| **路線問題** | 車站太少；同一車站連續出現兩次；車站之間互不相容；車站無法連接；備用站台無法連接 | `line_warning.script.tl:46-128` |
| **路線設定錯誤** | 某種貨物在任何地方都無法裝載，或在任何地方都無法卸載；沒有車輛能運載設定裝載的貨物；車輛不運載任何已設定的貨物，或客運路線上有純貨運車輛；完全沒有設定貨物 | `line_warning.script.tl:15-36`，`line_warning.script.tl:133` |
| **車站問題** | 目前車輛無法使用的站點；客運站點被貨運車輛使用（部分或全部）；貨運站點被客運車輛使用；某種已設定的貨物在該站點無法裝載或卸載 | `line_station_warning.script.tl:6-87` |
| **車輛問題** | 沒有電氣化路徑；沒有大型飛機的航線；沒有大型船舶的航線；完全沒有路徑；兩列火車互相阻擋 | `vehicle_warning.script.tl:6-58` |
| **城鎮未連接** | 兩座城鎮之間的道路中斷；兩座城鎮之間的行程耗時過長 | `town_warning.script.tl:7-19` |

- 「沒有大型飛機的航線」與「沒有大型船舶的航線」表示車輛對其路線上的跑道、碼頭或水道來說太大：見[飛機](aircraft.html)與[船舶](ships.html)。

## 記錄、彈出視窗與設定

- 每種警告類型都可以在通知設定（「設定通知記錄」）中關閉。被關閉的類型不會彈出視窗，也不會保留在記錄中（`notification_util.tl:145-146`，`notification_log.tl:480`）。
- 在**新遊戲**中，有 11 種類型一開始就是關閉的：**車輛卡住**、**車輛問題**、**車輛狀況**、**站點擁擠**、**車站無法使用**、**站點未連接**、**城鎮未連接**、**貨物未卸載**，以及公司的探勘、行銷活動與產業綠化進度訊息（`stuck_vehicle.res.lua:7`，`vehicle_warning.res.lua:8`，`noroadconnection.res.lua:8`，`vehiclecondition.res.lua:8`，`overcrowding.res.lua:8`，`station_useless.res.lua:7`，`town_warning.res.lua:8`，`cargo_rtc_warning.res.lua:8`，`notification_util.tl:32-39`）。
- 一次性訊息（新車輛、新建築、升級、補助）在遊戲時間 **60 秒**後隱藏彈出視窗；它們仍保留在歷史記錄中（`notification_util.tl:10`，`notifications.script.tl:85-94`）。
- 當通知所指的一切都被拆除或重建時，通知也會結束（`notifications.script.tl:95-107`）。
- 在任務中，通知一開始是暫停的，直到任務將其開啟（`notifications.script.tl:700-704`）。

## 小提示

- 5 分鐘後的卡住警告不會說明原因。查看車輛：紅色號誌、方向錯誤的單向號誌，或同一車輛的車輛問題警告。
- 「車站無法運作」只表示「涵蓋範圍內還沒有任何東西」。把車站移近房屋、工業或倉庫，或者擴大車站。
- 擁擠的車站會流失乘客：增加車輛，或縮短間隔（見[發車與等待](departure.html)）。

```check
official: The official wiki's User Interface page describes the notification button, the log and its filters, without the conditions of each warning. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: 上述條件：行駛途中速度為 0 達 5 分鐘即為卡住，車輛狀況 20 % 起直到 30 %，城鎮評價極差低於 1/6，道路連接每 75 天檢查一次，預設關閉 11 種類型。
result: adds
```
