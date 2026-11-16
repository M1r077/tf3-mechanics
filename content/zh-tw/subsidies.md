---
title: 補助：提案、期限與獎勵
summary: 四種合約類型、真正達成它們的條件、你能得到什麼與要承擔什麼風險，以及新提案多久出現一次。
domain: subsidies
official: gamemanual:management:subsidies
status: verified
updated: 2026-11-15
fact: 4 | 自由遊戲中的合約類型
fact: 5 | 同時最多可接受的合約數
fact: ×2 | 有配送的路線 5 年內的收益
fact: 0 | 拒絕提案的懲罰
---

補助就是一份合約：產業或城鎮提出一項任務，你接受時就能拿到一些好處，在期限內達成可以拿到更多，錯過期限則必須歸還預付款，再加上一筆懲罰。拒絕提案，或是放著讓它過期，都不會有任何損失。

```diagram subsidy_life
```

## 四種合約類型

```diagram subsidy_types
```

| 合約 | 目標 | 達成條件 | 來源 |
|---|---|---|---|
| **供應產業** | 從來沒有生產過任何東西的產業 | 配送到該產業達規定次數，**任何一種投入貨物**都算 | `deliver_cargo.script.tl:54-61`，`deliver_cargo.script.tl:230-234`，`deliver_cargo.script.tl:470-479` |
| **供應城鎮** | 城鎮有需求、卻完全沒有收到的一種貨物 | 將規定數量的**該種貨物**配送到城鎮的建築 | `deliver_cargo_town.script.tl:566-581` |
| **連接城鎮** | 兩個城鎮 | **一位**乘客在同時停靠兩個城鎮的路線上，開始一趟兩鎮之間的行程 | `deliver_passengers.script.tl:263-280`，`subvention_util.tl:561-592` |
| **運送工人** | 已經在出貨或收貨、但尚未獲得加速效果的產業 | 它的工人加速效果啟動（工作場所的一半） | `deliver_workers.script.tl:121-131`，`deliver_workers.script.tl:152-156` |

- 每個新提案會從當下可以出現的類型中抽出一種，機率均等（`subventions.script.tl:147-169`）。
- **供應產業**與**供應城鎮**計算的是配送次數，而不是行程：每個抵達目標並獲得付款的單位加 1。可以轉乘（`deliver_cargo.script.tl:470-479`）。
- **連接城鎮**不要求乘客人數：第一位在兩鎮之間搭上你的路線的乘客就能讓它達成。「無需轉乘」是指這段行程由一條同時服務兩個城鎮的路線完成。如果已經有路線在兩鎮之間載客，就不會出現這個提案（`deliver_passengers.script.tl:72-78`）。
- 距離近的城鎮出現機率高得多：一對城鎮的權重從 1 km 以內的 1 降到 20 km 的 0.01，再取 7 次方（`deliver_passengers.script.tl:175-191`）。
- **供應城鎮**偏好地圖上已經有人生產的貨物：機率是其他貨物的 16 倍（`deliver_cargo_town.script.tl:277-280`）。
- 需要配送的數量取決於**補助風險**設定：

| 補助風險 | 供應產業 | 供應城鎮（最多為城鎮的需求量） | 來源 |
|---|---|---|---|
| 無 | 10–50 | 10–30 | `deliver_cargo.script.tl:100-114`，`deliver_cargo_town.script.tl:165-188` |
| 一般風險 | 50–100 | 30–100 | |
| 高風險 | 75–150 | 35–125 | |
| 極高風險 | 150–300 | 45–150 | |

## 什麼是無需轉乘的連接？

**連接城鎮**卡片的要求是：「在{fromTownName}與{toTownName}之間建立無需轉乘的交通路線，運送兩地之間的乘客。」（`deliver_passengers.script.tl:14`）。

- **一條在每個城鎮都有站點的路線。**遊戲會逐一檢查路線的站點，取得每個站點所屬的城鎮；只要兩個城鎮各有至少一個站點，這條路線就算數。其他站點、站點順序與載具類型（公車、路面電車、火車、船舶、飛機）都沒有關係（`subvention_util.tl:561-592`）。
- **一位乘客就能讓它達成**：第一位搭乘這條路線、從一個城鎮的站點到另一個城鎮的站點的乘客，方向不限（`deliver_passengers.script.tl:263-280`，`deliver_passengers.script.tl:210-218`）。檢查只看這一段乘車，所以在此之前或之後轉乘應該沒有影響。
- **站點所屬的城鎮**是其車站群組中第一座車站所屬的城鎮（`town_util.tl:1844-1873`）。車站屬於哪個城鎮由引擎決定。
- 如果已經有路線在每個城鎮都有讓乘客上車的站點，而且有載客的載具，就**不會出現提案**（`deliver_passengers.script.tl:72-78`）。兩鎮之間只載貨的路線不會阻擋提案。
- 當兩個城鎮之一，或讓合約達成的那條路線，出現遊戲視為新版本的變更時，合約會以**補助已遭撤銷**結束（`deliver_passengers.script.tl:232-240`）。

```engine
車站屬於哪個城鎮（stationSystem.getTown）、乘客究竟何時「開始使用」一條路線（OnStartedLineUsage），以及路線的哪些編輯算是新版本，都由引擎決定。達成後編輯路線是否會結束「2倍收入」效果，尚未測試。
```

## 獎勵與懲罰

每份合約都有三份清單，在合約卡片上分別顯示為**接受**、**完成**與**失敗**（`subvention_util.tl:449-471`）。失敗時一定要歸還預付款，另外再加一項懲罰（`deliver_cargo.script.tl:134-136`）。

| 合約 | 接受 | 完成 | 失敗 | 來源 |
|---|---|---|---|---|
| 供應產業 | 現金 | 只有「2倍收入」效果 | 歸還預付款 + 罰款 | `deliver_cargo.script.tl:120-136` |
| 供應城鎮 | 現金**或**該城鎮的聲望 | 城鎮經驗值**或**現金，外加 2倍收入 | 歸還預付款 + 聲望下降**或**罰款 | `deliver_cargo_town.script.tl:194-229` |
| 連接城鎮 | 現金，城鎮相距越遠越多 | **兩個**城鎮的城鎮經驗值，外加 2倍收入 | 歸還預付款 + **兩個**城鎮的聲望下降 | `deliver_passengers.script.tl:105-119` |
| 運送工人 | 現金 | 現金 | 歸還預付款 + 罰款 | `deliver_workers.script.tl:92-116` |

- **現金**，依年份縮放之前：預付款 150 萬到 375 萬 × 風險係數（無 ×2、一般風險 ×1、高風險 ×0.75、極高風險 ×0.5）；罰款 300 萬到 600 萬；達成獎金 375 萬到 1,125 萬（`deliver_cargo.script.tl:120-128`，`deliver_workers.script.tl:102-104`）。
- 金額隨**月曆年份**成長，與通貨膨脹設定無關：1900 年 ×1，平均上升到 2000 年以後的 ×4，無條件進位到 1 萬（`finances_util.tl:87-90`）。在財務狀況中列為**補助**（`subvention_util.tl:126-135`）。
- **供應城鎮**只有在你的帳戶餘額低於 1 億時才會給現金獎勵與罰款；超過 1 億時，只有十分之一的提案還會這樣（`deliver_cargo_town.script.tl:206-217`）。
- **城鎮經驗值**是城鎮目前等級的一定比例：目前等級到下一級之間所需經驗值的 20 % 到 100 %（`deliver_cargo_town.script.tl:216`，`town_growth.script.tl:605-608`）。**連接城鎮**還要再乘上距離係數，從 1 km 的 0.3 到 20 km 的 3.0：相距很遠的城鎮可以連升好幾級（`deliver_passengers.script.tl:94-96`，`deliver_passengers.script.tl:116-118`）。
- 失敗後失去的**聲望**，會在城鎮的聲望評價中顯示為**申請失敗的補助**（`towns.script.tl:313-334`）。接受時獲得的聲望只會抵銷既有的懲罰，不會超過滿分（`town_util.tl:1644-1647`）。

## 2倍收入效果

- 合約達成後持續 **60 個月**（5 年）（`subvention_util.tl:286`，`subvention_util.tl:292`）。
- **供應產業**：合約期間曾配送到該產業的路線上，配送到該產業的貨物（`deliver_cargo.script.tl:463-469`）。
- **供應城鎮**：曾配送合約貨物的路線上，配送到該城鎮任何建築的貨物，**任何貨物**都算（`deliver_cargo_town.script.tl:554-565`）。
- **連接城鎮**：往返兩鎮之間的乘客，只限 **一條** 直達路線：兩鎮之間的乘客最後搭乘的那條直達路線。合約達成後仍會持續更新，所以有兩條直達路線時，加倍可能從一條轉到另一條（`deliver_passengers.script.tl:263-296`）。
- **運送工人**沒有收益效果（`deliver_workers.script.tl:90`）。
- 對供應產業和供應城鎮來說，合約達成後才開始配送的路線什麼也拿不到：路線清單只在合約期間登記。
- 兩份合約不會讓同一筆收益加倍兩次：有好幾份同時符合時，只採用最後一個結果（`subventions.script.tl:570-583`）。

```tip scripts
**想讓供應產業或供應城鎮的雙倍收入涵蓋多條路線？在合約達成前讓它們都配送。** 之後才加入的路線什麼也拿不到。連接城鎮只讓一條路線加倍，即乘客最後搭乘的直達路線：兩鎮之間只保留一條直達路線。
```

```engine
補助的 ×2 如何與公司等級乘數（通貨膨脹設定）搭配，是由引擎決定的：兩個腳本都只會為每筆付款回傳一個乘數。一筆付款項目代表什麼（大概是一單位貨物或一位乘客）也由引擎決定。
```

## 期限

期限從你接受時開始計算。貨物要運得越遠，期限越長；風險越高，期限越短（風險係數：無 ×2、一般風險 ×1、高風險 ×0.75、極高風險 ×0.5，乘客與工人合約則為 ×0.625）：

| 合約 | 期限（月） | 採用的距離 | 來源 |
|---|---|---|---|
| 供應產業、供應城鎮 | (6 + 32 × E) × 風險係數 | 到生產該貨物的最近產業 | `deliver_cargo.script.tl:116-117` |
| 連接城鎮 | (9 + 4 × E) × 風險係數 | 兩個城鎮之間 | `deliver_passengers.script.tl:98-99` |
| 運送工人 | (6 + 15 × E) × 風險係數 × 時代係數（1940 年前 ×1.75，1980 年前 ×1.25） | 到最近的城鎮 | `deliver_workers.script.tl:75-87` |

E 是以該時代最高速度行駛的列車（1900 年起 120 km/h，1981 年起 300 km/h）跑完這段距離所需的時間，無條件進位，至少為 1（`subvention_util.tl:486-489`，`vehicle_util.tl:225-230`）。

- 沒有被接受的提案大約 **6 個月**（150 到 210 天）後就會消失，沒有任何懲罰（`subvention_util.tl:284`，`subvention_util.tl:290`）。
- **供應產業**或**運送工人**合約進行期間，目標產業不會關閉：預定的關閉會被取消（`subvention_util.tl:473-484`）。
- 如果目標在合約期間消失或被重建，遊戲會顯示**補助已遭撤銷**，但仍會像錯過期限一樣套用失敗懲罰（`subventions.script.tl:172-190`，`subvention_util.tl:406-412`）。
- 已接受的合約沒有取消按鈕。

```engine
一個遊戲月有多長，也就是期限的實際長度，由引擎設定（getDefaultMonthDuration）。上面的公式都以遊戲月曆的月為單位。
```

## 新提案多久出現一次

- **補助發放頻率**：極少、偶爾（預設）、經常、頻繁分別每 12、6、3、1 個月出現一個新提案；**永不**則會關閉補助（`subvention_util.tl:13-38`，`mod.script.tl:247-248`）。
- 間隔會隨**公司等級**拉長：等級 1 為 ×1，到等級 15 為 ×2（`subvention_util.tl:19-22`）。
- **拒絕**提案會讓下一次間隔減半；接受提案或出現新提案則會將它重設（`subventions.script.tl:429`，`subventions.script.tl:395`，`subventions.script.tl:118`）。
- 已接受且進行中的合約達到 **5 份**時，就不會再出現新提案（`subventions.script.tl:23`，`subventions.script.tl:256-262`）。第一個提案在半個月後出現。
- 同一個目標（產業、城鎮加貨物、一對城鎮）**每場遊戲只會提出一次**，即使合約錯過或失敗也一樣（`subventions.script.tl:107-113`，`subventions.script.tl:186`）。
- 難度預設的發放頻率 / 風險（`difficulty_util.tl:104-105`，`difficulty_util.tl:132-133`，`difficulty_util.tl:159-160`，`difficulty_util.tl:186-187`）：簡單 經常 / 無，普通 偶爾 / 一般風險，困難 極少 / 高風險，**極度困難 永不**：完全沒有補助。
- 只允許評價為極佳的城鎮提出補助的檢查確實存在，但已被關閉（`town_util.tl:1574-1580`，`deliver_cargo_town.script.tl:272-275`）。

## 小知識

- 目標簡單時儘管接受：拒絕或忽略都沒有代價，但**失敗**就得歸還預付款，再加上一筆可能比預付款還高的罰款。
- **供應城鎮**與**供應產業**：所有想受惠的路線都要開始配送，因為只有合約期間有配送的路線，才能在 5 年內享有 2倍收入。
- 在相距很遠的城鎮之間完成**連接城鎮**，能得到最多的城鎮經驗值，而且只需要一位乘客。
- **供應產業**達成時不會再給任何款項：它的獎勵只有 2倍收入。

```check
official: "Accept an offer to begin the contract; declining it has no penalty." "Possible rewards include town experience, an additional payment, or a limited-time 2x income effect on eligible transport lines." "The upfront reward is reversed, and an additional fine or loss of town reputation may apply." ([Subsidies](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:subsidies))
scripts: 四種類型；一位乘客就能達成連接城鎮；×2 在合約期間有配送的路線上持續 60 個月；供應產業只給 ×2；金額依年份縮放（×1 到 ×4）；每 1–12 個月一個新提案，公司等級高時間隔更長；最多同時接受 5 份；每個目標每場遊戲只提出一次。
result: refines
```
