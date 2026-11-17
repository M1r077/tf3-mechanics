---
title: 公司等級、特權與總部
summary: 什麼會提升公司等級，每個等級解鎖什麼，許可與勘探如何運作，總部實際提供什麼，以及更高等級的代價。
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40425
fact: 15 | 個公司等級，從初階員工到鐵路大亨
fact: ×12.5 | 達到等級 15 所需的世界人口（與開局相比）
fact: ×0.75 | 通貨膨脹為普通時等級 15 的收入
fact: 0 | 人口下降時失去的等級
---

公司等級不取決於金錢或運輸量，而取決於**整張地圖的人口**。每個新等級都會解鎖特權（地標、勘探、行銷活動、產業綠化、總部模組），而在**通貨膨脹**設定下，它也會讓你的所有收入稍微下降。

## 什麼會提升等級

- 遊戲會記住**開局時的世界人口**：所有城鎮的居民數（`company.script.tl:392-396`，`company_util.tl:365-371`）。
- 接著把歷來達到的**最高**世界人口與這個開局值比較（`company_growth.script.tl:25-27`）。這個值只增不減：城鎮縮小永遠不會讓你降級。
- 等級 1 在開局值時達到，等級 15 在約 **12.5 倍**時達到（`company_progression_util.tl:6-14`，`company_progression_util.tl:95-120`，`town_growth_function.tl:13-20`）。
- 戰役任務與地圖編輯器中沒有等級（`company_growth.script.tl:74-79`）。

| 等級 | 職位 | 世界人口（與開局相比） |
|---|---|---|
| 1 | 初階員工 | ×1 |
| 2 | 技師 | ×1.02 |
| 3 | 工程師 | ×1.08 |
| 4 | 協調員 | ×1.2 |
| 5 | 專家 | ×1.4 |
| 6 | 組長 | ×1.7 |
| 7 | 督導 | ×2.1 |
| 8 | 經理 | ×2.6 |
| 9 | 局長 | ×3.3 |
| 10 | 資深局長 | ×4.2 |
| 11 | 執行長 | ×5.3 |
| 12 | 董事長 | ×6.7 |
| 13 | 副總裁 | ×8.3 |
| 14 | 總裁 | ×10.2 |
| 15 | 鐵路大亨 | ×12.5 |

這些比例是依腳本以開局人口 50,000 以上計算的（`company_progression_util.tl:6-14`，`company_static_util.tl:6-24`）。在小地圖上，中間等級略高（5,000 居民時等級 8 需要 ×2.85）；等級 1 與 15 仍為 ×1 與 ×12.5。

- 所以等級跟隨**城鎮成長**：城鎮因你的乘客與貨物而成長，見[城鎮成長](towns.html)。
- 前幾個等級來得很快，最後幾個需要地圖上的城鎮擴大許多倍。

## 新等級在公司視窗中生效

人口越過門檻時會出現**升級通知**；點擊它會在該等級上開啟公司視窗（`company_growth.script.tl:96-107`，`company_notification_rank_up.script.tl:8-9`）。

- 只有當該等級在**公司視窗中被選取**時，新特權才會解鎖：視窗這時送出解鎖（`company.tl:420-423`，`company_growth.script.tl:55-62`）。建造選單檢查的是這個已生效的等級（`company_util.tl:92`，`company_util.tl:171-178`）。
- 下一節的收入係數跟隨**已達到**的等級，不論是否生效（`company_growth.script.tl:47-48`）。

```tip scripts
升級後點擊通知（或開啟公司視窗並選取新等級）來取得特權。等待不會帶來任何好處：收入已經降低了。
```

## 更高等級的代價：通貨膨脹設定

開啟**通貨膨脹**時，所有貨物與乘客收入從等級 1 的 ×1 平均下降到等級 15 的最低值（`company_progression_util.tl:25-40`，`company_growth.script.tl:159-170`）。

| 通貨膨脹 | 等級 15 的收入 | 來源 |
|---|---|---|
| 無 | ×1（不變） | `difficulty_util.tl:50`，`mod.script.tl:694-697` |
| 低 | ×0.9 | |
| 普通 | ×0.75 | |
| 高 | ×0.6 | |
| 極高 | ×0.5 | |

- 在普通下，每升一級損失約 1.8 % 的收入：等級 3 為 ×0.96，等級 8 為 ×0.875，等級 15 為 ×0.75。
- 通貨膨脹不會提高任何成本；成本跟隨日曆年份（見[成本、維護費與貸款](costs.html)）。
- 更高的等級也會讓新的補助提議變少（見[補助](subsidies.html)）。

## 許可

大多數特權受**許可**限制。等級為某項特權提供許可；每棟建築或每次使用佔用一個（`company_util.tl:33-80`，`company_util.tl:206`）。

- 許可隨等級**累加**：在等級 3 給 1 個、等級 5 再給 1 個的特權，從等級 5 起允許 2 個（`company_util.tl:51-56`）。
- 建築被拆除時會歸還許可：遊戲計算的是現存的建築（`company_util.tl:143-163`，`company_util.tl:203-206`）。
- 勘探、行銷活動與綠化在開始時消耗許可（`company.script.tl:416-423`，`company.script.tl:459-462`，`company.script.tl:496-500`）。之後建造選單顯示**已使用**或**冷卻時間**（`company_util.tl:207-226`）。
- **行銷**許可在每次活動 **5 年**後恢復（`marketing.res.lua:6-7`，`company.script.tl:66-94`）。

| 特權 | 許可 | 來源 |
|---|---|---|
| 總部 | 等級 1 時 1 個 | `hq.res.lua:6` |
| 行銷活動 | 等級 4 時 1 個，5 年後恢復 | `marketing.res.lua:6-7` |
| 產業綠化 | 等級 3、6、9、12 與 15 各 1 個 | `industry_greenify_tool.script.tl:101-102` |
| 淨化廠 | 等級 10 時 15 個 | `pollution_cleanup_facility.con.lua:106-108` |
| 地標 | 各一個：圓形劇場 2，大燈塔 5，姬路城 7，船舶博物館 9，新天鵝堡 10，自由女神像 11，頤和園 13，歌劇院 14，國會大廈 15 | `arena.con.lua:39`，`lighthouse.con.lua:48`，`white_heron_castle.con.lua:47`，`ship_museum.con.lua:55`，`neuschwanstein.con.lua:55`，`statue_of_liberty.con.lua:57`，`summer_palace.con.lua:63`，`opera_house.con.lua:63`，`westminster.con.lua:79` |

各特權的作用：[城鎮聲望](reputation.html)（行銷活動），[污染與噪音](emission.html)（綠化，淨化廠）。

## 勘探

勘探會在城鎮附近尋找一種資源，成功後在那裡建立一個新產業。

| 資源 | 等級 | 來源 |
|---|---|---|
| 漁獲 | 2 | `exploration_fish.res.lua:9-11` |
| 陶土 | 3 | `exploration_clay.res.lua:9-11` |
| 原油 | 4 | `exploration_crude_oil.res.lua:9-11` |
| 穀物，蔬菜 | 4，**共用一個許可**（產業） | `exploration_grain.res.lua:9`，`exploration_vegetables.res.lua:9`，`permit_key_farm.res.lua:6` |
| 原木 | 5 | `exploration_logs.res.lua:9-11` |
| 煤，鐵礦 | 6 | `exploration_coal.res.lua:9-11`，`exploration_iron_ore.res.lua:9-11` |
| 石材，羊毛 | 8 | `exploration_stone.res.lua:9-11`，`exploration_wool.res.lua:9-11` |
| 沙子 | 9 | `exploration_sand.res.lua:9-11` |
| 橡膠 | 12 | `exploration_rubber.res.lua:9-11` |

- 每種資源只有**一個**許可，在勘探開始時使用（`company.script.tl:451-462`）。
- 勘探最長持續 **6 個月**。每月嘗試放置一次產業，成功率在 6 個月內從 20 % 升到 60 %（`company_util.tl:14-17`，`company.script.tl:299-307`，`company.script.tl:130-142`）。
- 當遊戲在城鎮附近找不到放置該產業的地方時，嘗試也會失敗（`company.script.tl:199-210`）。
- 如果最後一次嘗試失敗，**許可會歸還**，並有通知告知（`company.script.tl:106-126`，`company.script.tl:170-181`）。
- 每個城鎮與資源組合同一時間只能進行一次勘探（`company.script.tl:442-447`）。

```engine
新產業可以建在哪裡（城鎮附近的 makeIndustrySpawnProposal）由引擎決定：遠離水域的漁獲勘探，或周圍沒有空地的城鎮，都會直接失敗並歸還許可。
```

## 總部

| 項目 | 數值 | 來源 |
|---|---|---|
| 價格與維護費 | 免費，無維護費 | `headquarter.script.tl:526-527` |
| 許可 | 1 個，等級 1 時 | `headquarter.con.lua:6-7`，`hq.res.lua:6` |
| 城鎮成長 | 離它最近的城鎮 +5 % | `headquarter.script.tl:510-515`，`landmark_util.tl:51-70` |
| 工作崗位 | 24 | `headquarter.con.lua:16`，`headquarter.script.tl:505-508` |

- +5 % 是對該城鎮成長率的加成，所以城鎮成長率為 0 % 時沒有作用（見[城鎮成長](towns.html)）。
- **模組**每個 50,000，受隨等級增加的許可限制（`hq_module_m.module.lua:83`，`hq_module_m.module.lua:137`）。
- 檔案中只有兩個模組帶有加成：**中型建築**城鎮成長 +1 %（`hq_module_m.module.lua:139-142`）與**大型建築****聲望恢復** +1 %（`hq_module_l.module.lua:169-172`）。恢復加成不被任何城鎮評價讀取（見[城鎮聲望](reputation.html)）。其他模組都是裝飾。
- 每個模組檔案開頭還有一張給出 +5 % 城鎮成長的表，但檔案中沒有任何地方使用它（`hq_corner_l.module.lua:148-159`，`hq_statue.module.lua:46-57`）。只有模組 `metadata` 中的加成會被累加（`headquarter_addon.script.tl:18-29`）。

| 模組 | 獲得許可的等級（×2 = 兩個） | 等級 15 時合計 |
|---|---|---|
| 立旗 | 1 ×2，6，7，8，9，11，12，13，14 | 10 |
| 轉角建築 | 3，5，7 ×2，9，11，13，15 | 8 |
| 中型建築 | 2，4，10 ×2，15 ×2 | 6 |
| 大型建築 | 5，6，10，12 | 4 |
| 陽台 | 8 ×2，14 ×2 | 4 |
| 大型噴泉 | 10 ×2，14 ×2 | 4 |
| 圓頂 | 6，15 ×2 | 3 |
| 屋頂旗幟 | 7，10，13 | 3 |
| 網球場 | 11，12，14 | 3 |
| 老樹 | 13，15 ×2 | 3 |
| 雕像 | 14 ×2 | 2 |
| 水池 | 15 | 1 |

來源：每個模組檔案中的 `rankAndPermits` 行（`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`）。

```tip scripts
把總部建在你最想讓它快速成長的城鎮，並在那裡加上中型建築：它們是唯一帶成長加成的模組。
```

## 小提示

- 想升級就讓城鎮成長：把更多乘客與貨物送到更多城鎮，並保持良好的評價。銀行裡的錢不算數。
- 規劃好地標與勘探：每項只有一次，在固定的等級。
- 在有通貨膨脹的地圖上，升級對特權有利、對收入不利。在普通下，一路升到等級 15 會損失全部收入的四分之一。

```check
official: "The company rank depends on the population of the map. . Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: 規則相同：歷來最高的世界人口與開局人口相比，等級 15 為 ×12.5；永不失去。新等級必須在公司視窗中選取才會解鎖特權，而通貨膨脹會立即降低收入。只有兩個模組帶有加成（中型建築成長 +1 %，大型建築聲望恢復 +1 %，後者不被任何評價讀取）；其他都是裝飾。
result: refines
```
