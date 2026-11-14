---
title: 貨運收益與配送時間
summary: 一次配送能賺多少（直線距離、爬升、公司等級、補助），以及遲到真正的代價是什麼。
domain: economy
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: 3.8 | 所有貨物相同的收益係數
fact: +8 × 爬升 | 爬升的公尺數計入距離
fact: 100 % | 即使遲到也全額支付
---

一次配送只依**直線距離**付錢，與行程的其他方面無關。速度之所以重要是另一個原因：每種貨物都有**時限**，遲到的配送會降低城鎮的**配送**評價，而不是你的收益。

```diagram income_formula
```

## 收益公式

整個公式就是一段很短的遊戲腳本（`cargo_income.script.lua:10-13`）：

1. 貨物的**收益係數**。每種基本遊戲貨物都使用同一個函式與相同的價格（`initialPrice = 4`，`finalPrice = 3.2`），因此**全部 36 種貨物都是 3.8**（`cargotype.script.lua:7-13`，`coal.cargo.lua:21-22`）。在相同距離下，煤和一般貨物賺的錢完全一樣。
2. **貨運收益** 設定：50 %、75 %、100 %、125 % 或 150 %（`difficulty_util.tl:38`，`mod.script.tl:211`）。四種難度預設都使用 100 %（`difficulty_util.tl:97`）。
3. **距離**，見下文。

這個函式會收到行程時間，但**並不使用它**（`cargotype.script.lua:7-13`）：慢的或遲到的配送收益都一樣。

## 距離：直線加爬升

```diagram income_distance
```

- 距離是兩點之間的**三維直線**，而不是你路線的長度（`cargo_income.script.lua:3-7`）。
- 高度差為正時，會加上 **8 × 該高度**（`cargo_income.script.lua:5`）：爬升 100 m 相當於多跑 800 m。反方向則什麼也不扣。
- 所以蜿蜒的路線和筆直的路線賺得一樣多，但你蓋的每一公尺軌道或道路都要付維護費。

```engine
比較的是哪兩個點（貨物進入你的網路的地點、送達的地點），以及高度差的正負，都由引擎決定。官方 wiki 寫道："distances are measured as the crow flies between the source and the final destination"（距離以起點與最終目的地之間的直線測量）。
```

## 還有什麼會改變金額

| 因素 | 效果 | 來源 |
|---|---|---|
| **公司等級**，搭配通貨膨脹設定 | 等級 1：×1，平均下降至等級 15：×0.9（低）、**×0.75（普通）**、×0.6（高）、×0.5（極高）；無：始終 ×1 | `company_progression_util.tl:25-40`，`difficulty_util.tl:50`，`mod.script.tl:694-697` |
| **已達成的補助** | 為該合約配送貨物的路線 ×2 | `deliver_cargo.script.tl:463-469`，`deliver_cargo_town.script.tl:554-565` |
| **配送遲到** | 對收益沒有影響 | `cargotype.script.lua:7-13` |

- 等級乘數作用於**所有**貨物與乘客收益（`company_growth.script.tl:159-170`）。難度預設使用的通貨膨脹分別為：低（簡單）、普通（普通）、高（困難）、極高（極度困難）（`difficulty_util.tl:108`）。
- 補助的 ×2 只作用於合約期間有配送的路線，而且有時間限制（官方 wiki，補助）。

## 乘客

乘客使用相同的距離與約 3.61 的固定收益係數（`cargotype.script.lua:50-53`），再乘上 **0.5 + 車輛的票價係數**（`cargo_income.script.lua:14-17`）。當車輛模型沒有設定舒適度係數時，遊戲會把票價係數設為：公車與輕軌 0.3、飛行器 0.9、船舶 0.1、列車 0.5（`base_mod.lua:46-61`）；其他模型的數值來自引擎，在腳本中看不到。乘客補助同樣會讓該路線的收益加倍（`deliver_passengers.script.tl:284-298`）。

## 配送時限

每種貨物都有自己的時限（各 .cargo.lua 中的 `timeToDeliverInSeconds`，例如 `meat.cargo.lua:30`、`coal.cargo.lua:30`）。生鮮食品最短，沉重的原料長五倍：

```diagram delivery_times
```

- **財務狀況 › 配送時間** 會顯示你的地圖上每種貨物的時限；貨運滿意度圖層會把路線從綠色到紅色上色。
- 配送超過時限才送達，就算是**延誤**（`towns.script.tl:425`）。
- 專用貨物倉庫模組會**凍結**所存貨物的計時（官方 wiki，貨物倉庫）。

```engine
引擎會把基礎時間換算成財務狀況中顯示的時限（腳本以 getAdjustedDeliveryTime 讀取），並判斷一件貨物何時算遲到。上面只有相對數值來自貨物檔案。
```

## 遲到的代價：配送評價

遲到的貨物照樣全額付款，但每個城鎮都有一項**配送**評價（`town_util.tl:505-519`）：

1. 遊戲會統計**最近半年**配送到該城鎮的次數，以及其中遲到的次數（至少以 10 次計算，所以最初幾次配送不會讓評價大起大落）。
2. 準時比例 → 評價：低於下限時評價為 0，高於上限時為 1，兩者之間為線性。預設靈敏度（**普通**）下：**準時 30 % → 0，100 % → 1**，所以準時 90 % 會得到 0.86。
3. **配送靈敏度** 設定會移動這兩個界限（`difficulty_util.tl:47`）。關閉：始終為 1。預設：簡單為低、普通為普通、困難為高、極度困難為極高（`difficulty_util.tl:113`）。

```diagram delivery_rating
```

配送是六項評價之一，其中最低的一項決定城鎮的成長率：只要有一項評價為極差，城鎮就會停止成長（見 [城鎮成長](towns.html)）。

## 範例

同樣一次煤的配送，直線距離 5 km。

| 情況 | 收益 |
|---|---|
| 平地，路線長度不限 | **100 %** |
| 相距 10 km | **200 %** |
| 目的地高 100 m | **116 %** |
| 配送遲到 | **100 %**（配送評價下降） |
| 公司等級 15，通貨膨脹普通 | **75 %** |
| 已達成補助的路線 | **200 %** |

## 小知識

- 既然每種貨物每公里的收益都一樣，**請依運量、距離與時限來挑選貨物**，而不是看價格。
- 時限對肉品、漁獲、蔬菜與飲料最重要：使用短路線，或能凍結計時的貨物倉庫。
- 每配送一單位貨物到城鎮建築，也會為該城鎮帶來經驗值（`town_growth.script.tl:642`，`town_growth_config.res.lua:5`）。

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks), [Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: 所有貨物係數都是 3.8；距離為三維直線加 8 × 爬升；公司等級會降低收益，等級 15 時降到 ×0.75（通貨膨脹普通）；補助達成後 ×2；收益不使用時間；配送評價取決於最近半年的準時比例（普通：30 % → 0，100 % → 1）。
result: refines
```
