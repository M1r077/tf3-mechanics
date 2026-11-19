---
title: 成就
summary: 遊戲腳本對每個自由遊戲成就檢查什麼、何時檢查，哪些成就只計入基礎遊戲的車輛、貨物與動物，以及哪些檢查交給引擎。
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-17
game: 40444
fact: 17 | 由遊戲腳本自己解鎖的成就
fact: 500 m | 停靠山巔中列車停站時第一節車廂的高度
fact: < 1 % | 與我無關所需的城鎮聲望
fact: 10 | 集中管理中最近城鎮必須相同的地標數
---

官方 wiki 列出了 41 個成就。遊戲腳本 (`achievements.script.tl`) 自己解鎖其中 **17** 個，並為 **9 個跨遊戲計數器**提供資料；其餘的（戰役、天氣、城鎮規模、倉庫、利息、增益、汽車、1900-2000、2000 年代的蒸汽）在別處由引擎或平台檢查。每次檢查都先詢問引擎該成就是否仍可解鎖；模組或設定是否阻止它由引擎決定（`achievements.script.tl:632`，`achievements.script.tl:510`）。

## 腳本檢查的成就

| 成就 | 腳本檢查什麼 | 來源 |
|---|---|---|
| **包裹已抵達** | 一件貨物送達目的地 | `achievements.script.tl:221-225`，`achievements.script.tl:632-636` |
| **受命於人** | 完成一項補助 | `achievements.script.tl:241-244`，`achievements.script.tl:638-642` |
| **連環補助** | 連續完成 10 項補助，中間沒有失敗；補助失敗會把計數重設為 0 | `achievements.script.tl:243-249`，`achievements.script.tl:644-648` |
| **照護者** | 城鎮的送貨評價變為**卓越** | `achievements.script.tl:270-276`，`towns.script.tl:27-30`，`achievements.script.tl:650-654` |
| **城市發展** | 城鎮升級 | `achievements.script.tl:253-255`，`town_growth.script.tl:92` |
| **需求增加** | 城鎮產生新的貨物類型需求 | `achievements.script.tl:257-259`，`achievements.script.tl:668-672` |
| **與我無關** | 城鎮的聲望**下降**到 **1 %** 以下 | `achievements.script.tl:261-267`，`towns.script.tl:33-36` |
| **晉升** | 公司提升一個等級 | `achievements.script.tl:280-282`，`achievements.script.tl:680-684` |
| **職涯高峰** | 公司達到最高等級 | `achievements.script.tl:284-290`，`achievements.script.tl:686-690` |
| **園藝大師** | 在一次建造中只放置樹木（沒有移除任何東西，也不是透過植林） | `achievements.script.tl:346-377` |
| **完美主義者** | 同一座車站依序被拆除、重建、拆除、重建，中間沒有建造或移除其他車站 | `achievements.script.tl:304-341`，`achievements.script.tl:694-710` |
| **集中管理** | 恰好 10 座已完工地標的最近城鎮相同 | `achievements.script.tl:382-395`，`achievements.script.tl:713-721` |
| **停靠山巔** | 你的某列列車到站時第一節車廂高於 **500 m** | `achievements.script.tl:407-417`，`achievements.script.tl:723-727` |
| **離岸作業** | 你的某架直升機抵達石油平台的站點 | `achievements.script.tl:420-450`，`achievements.script.tl:729-733` |
| **傳承船隊** | 基礎遊戲的每種船舶型號同時在你的船舶路線上運行 | `achievements.script.tl:735-776` |
| **第三類接觸** | 你點擊一個 UFO | `achievements.script.tl:793-806` |
| **時空管理者** | 你手動更改一天中的時間 | `achievements.script.tl:839-844` |

- **完美主義者**只計算增加或移除一整座車站的建造：為車站增加月台或模組不算（`achievements.script.tl:301-302`）。
- **集中管理**在每座地標完工時計數，算入當時離它最近的城鎮（`achievements.script.tl:386`）。
- **傳承船隊**只在一種從未停過站的船舶型號到站時檢查；它看的是你船舶路線上的車輛，而不是車庫裡的船（`achievements.script.tl:736`，`achievements.script.tl:750-766`）。
- **與我無關**需要的是聲望，而不是其他評價：見[城鎮聲望](reputation.html)。

```tip scripts
停靠山巔檢查的是列車停下時第一節車廂的高度，而不是站房的高度。把車站建在 500 m 以上的山上，並讓一列列車開到那裡。
```

## 跨遊戲計數器

這些計數會在各局遊戲之間延續（由平台儲存）。腳本只傳送自上次檢查以來的變化。

| 計數器 | 成就 | 計入什麼 | 來源 |
|---|---|---|---|
| 軌道長度 | **環繞世界** | 日誌總長度（km）的增長；移除時不會扣除 | `achievements.script.tl:511-523` |
| 人口 | **全球人口** | 地圖人口相對於載入遊戲時人口的增長 | `achievements.script.tl:512`，`achievements.script.tl:525-533` |
| 乘客 | **客運先驅** | 在你的路線上完成行程的乘客 | `achievements.script.tl:236-238`，`achievements.script.tl:535-541` |
| 貨物 | **貨運先驅** | 送達的貨物 | `achievements.script.tl:543-549` |
| 氣候 | **大亨中的大亨** | 公司在該地圖達到最高等級時的地圖氣候 | `achievements.script.tl:551-567` |
| 收入 | **不義之財** | 你的收入累計，以十億計 | `achievements.script.tl:202-204`，`achievements.script.tl:569-590` |
| 貨物類型 | **銷售大師** | 基礎遊戲的每種貨物類型各送達一次 | `achievements.script.tl:20-22`，`achievements.script.tl:230-232`，`achievements.script.tl:592-607` |
| 車輛 | **鑑賞家** | 基礎遊戲的每種車輛型號各到站一次 | `achievements.script.tl:16-18`，`achievements.script.tl:469-481`，`achievements.script.tl:609-625` |
| 動物 | **動物愛好者** | 基礎遊戲的每種動物各點擊一次 | `achievements.script.tl:24-26`，`achievements.script.tl:809-834` |

- 模組中的車輛、貨物與動物永遠不計入這些計數器：只採用基礎遊戲的檔案（`::/vehicle`，`::/cargos`，`::/animal`）（`achievements.script.tl:16-26`）。
- 對於鑑賞家，車輛必須**抵達路線的站點**；只購買是不夠的。

```engine
成就是否仍可解鎖（isAchievementUnlockable）、計數器是否被關閉（areStatsDisabled）、各計數器的目標，以及腳本中沒有的 24 個成就，都由引擎與平台處理。官方 wiki 指出，使用非外觀類模組或遊戲設定偏離標準值時，通常無法取得成就。
```

## 小提示

- 每個「首次」成就都與上一次檢查相比較：需要在該成就仍未解鎖的遊戲中發生**新的**事件，存檔中舊的補助或等級不會再次計入（`achievements.script.tl:633`，`achievements.script.tl:779`）。
- 你的等級、補助與聲望分別在[公司等級、特權與總部](company.html)、[補助](subsidies.html)與[城鎮聲望](reputation.html)中說明。

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: 腳本中有 17 個成就與 9 個計數器。它細化了官方說明：照護者指送貨評價達到卓越，與我無關指聲望低於 1 %，停靠山巔指第一節車廂高於 500 m，完美主義者指同一車站拆除-重建-拆除-重建，傳承船隊指基礎遊戲的所有船舶型號同時在路線上。計數器只計入基礎遊戲的車輛、貨物與動物。
result: refines
```
