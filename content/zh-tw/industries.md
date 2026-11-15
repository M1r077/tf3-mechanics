---
title: 產業
summary: 生產規則、庫存、用地與擴展、加速貨物、產業為什麼沒有加速效果，以及閒置產業到底何時關閉。
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
fact: 5 年 | 沒有裝載也沒有消耗，產業就成為關閉候選
fact: 1.1 % | 極少（預設）時每年的機率，之後 730 天倒數
fact: +50–150 % | 加速貨物的加成，每個產業固定
fact: 3 個月 | 每批加速貨物的加成時間
---

每個產業都依**規則**運作：「從投入庫存取這個，把那個放進產出庫存」，每年固定次數。原料產業（礦場、農場、油井）不需要投入，規模來自**用地**。有兩種加速能讓產量倍增：**加速貨物**（僅原料產業）和**工人**。

## 生產規則

- 規則給出每輪使用和產出的貨物，以及每年的輪數：一輪持續一年 ÷ 該數（`industry_react_util.tl:51-57`）。產業視窗的「生產」部分以小數字顯示。
- 視窗中的**上限**數值是：每輪 × 每年輪數 × 加速 × 設定**產業產能**（`industry_util.tl:310-379`）。
- **產業產能**：50 %、75 %、100 %、150 % 或 200 %。預設組合：簡單 150 %，普通 100 %，困難 75 %，極度困難 50 %（`difficulty_util.tl:41`、`difficulty_util.tl:93`、`difficulty_util.tl:120`、`difficulty_util.tl:148`、`difficulty_util.tl:175`、`mod.script.tl:196-197`）。
- 例如煉鋼廠：6 鐵礦 + 6 煤 → 3 鋼 + 4 板金屬，每年 121.7 輪：730 鐵礦和 730 煤 → 365 鋼和 487 板金屬（`steel_mill.con.lua:43-71`）。缺一種投入，規則就停。
- 罐頭工廠有兩條規則：漁獲 + 板金屬，或肉品 + 板金屬（`food_factory.con.lua:43-74`）。

```engine
規則由引擎執行。引擎可能延長一輪，這時提示顯示「（+…，因配送時間影響）」（`industry_react_util.tl:61-76`）。何時、延長多少不在腳本裡，所以實際產量可能低於上限。
```

## 庫存

- 每種貨物有自己的庫存和上限：例如煤礦場存 100 工具和 400 煤，煉鋼廠存 800 鐵礦、800 煤、400 鋼和 500 板金屬（`coal_mine.con.lua:44-67`、`steel_mill.con.lua:43-71`）。
- 庫存永不損耗（`industryutil.lua:25-29`）：貨物可以一直等。
- 產出庫存滿了不會停產：多出的貨物被丟棄（官方 wiki）。**貨物流動**圖表顯示**已消耗**、**已生產**和**已銷毀**（`industry_eow.script.tl:804-816`）。
- 建造參數**投入**設為關閉時，規則失去投入，產業也沒有投入庫存（`industryutil.lua:280-287`、`industryutil.lua:383-387`、`industryutil.lua:432-441`）。

## 用地與擴展

- 原料產業和畜牧農場有**用地**（田地、礦井、鑽塔）。等級就是用地數（`industryutil.lua:602-617`）。
- 規則隨用地成長：每輪產出 × 用地數 ÷ **該類產業的全部用地數**，四捨五入，至少 1。投入按同樣比例減少（`industryutil.lua:225-259`）。有 8 種用地的煤礦場，若只有 4 塊，每輪產 8 煤而不是 16。
- 每個產業有一個上限：在一半用地到全部之間隨機，或用參數**產業規模**選小 / 中 / 大（50 / 75 / 100 %）（`industryutil.lua:519-537`）。上限為 8 中 5 的礦場永遠達不到完整規則。
- 每半年遊戲可能增加**一塊用地**（`industries_config.res.lua:5`、`industries.script.tl:158-183`）。機率為（評分 − 25 %）÷ 50 %，評分 = 生產評分 × 你運走的產量比例（最多 1）：25 % 以下從不，75 % 以上必定（`industries.script.tl:172-176`）。
- 所以你不運走貨物的產業**永遠不會擴展**。工廠沒有用地，也不會擴展。
- 到上限時視窗顯示**產業規模已擴展至極限。**；被建築、軌道或道路擋住時顯示**產業受限，無法進一步擴展。**（`industry_react_util.tl:588-602`、`industries.script.tl:13-38`）。沒有腳本會移除用地；官方 wiki 說被拆除的用地會降低產量。

```engine
生產評分（getProductionRating）、年產量與運走量（getCargoOutputPerYear、getCargoShippedPerYear），以及新用地的位置（makeIndustryExtendProposal）都是引擎的值。
```

## 加速貨物

13 種原料產業有第二條規則——**加速**：每年 4 次從投入庫存取一批加速貨物，運作期間給予加成。

| 產業 | 用地 | 滿規模每年產量 | 加速批量（每年 4 批） | 來源 |
|---|---|---|---|---|
| 陶土礦坑 | 8 | 365 陶土 | 12 工具 | `clay_pit.con.lua:42-82` |
| 煤礦場 | 8 | 320 煤 | 13 工具 | `coal_mine.con.lua:44-85` |
| 棉花農場 | 21 | 274 羊毛 | 17 肥料 | `cotton_farm.con.lua:42-98` |
| 作物農場 | 20 | 274 穀物 + 183 蔬菜 | 17 肥料 | `farm.con.lua:44-106` |
| 漁場 | 18 | 263 漁獲 | 12 工具 | `fishing_grounds.con.lua:44-101` |
| 伐木營地 | 20 | 243 原木 | 15 機械 | `forest.con.lua:44-99` |
| 鐵礦場 | 8 | 365 鐵礦 | 15 機械 | `iron_ore_mine.con.lua:44-84` |
| 鑽油平台 | 9 | 365 原油 | 12 機械 | `oil_platform.con.lua:45-96` |
| 油井 | 14 | 548 原油 | 15 機械 | `oil_well.con.lua:44-94` |
| 採石場 | 7 | 365 石材 | 12 工具 | `quarry.con.lua:44-83` |
| 橡膠農場 | 23 | 365 橡膠 | 17 肥料 | `rubber_farm.con.lua:41-102` |
| 抽砂設施 | 9 | 365 沙子 | 15 機械 | `sand_excavator.con.lua:44-92` |
| 採砂場 | 8 | 365 沙子 | 12 工具 | `sand_pit.con.lua:44-84` |

- 加成在每個產業抽取一次：**+50 % 到 +150 %**，精確到 1 %（`industryutil.lua:394-405`）。加速效果部分顯示為「+X %」（`industry_util.tl:428-434`）。使用參數**加速係數**時改為 +50 %、+75 %、+100 %、+125 % 或 +150 %（`industryutil.lua:289-299`）。
- 視窗在最後一批持續期間（3 個月），或庫存一湊滿一批時，就顯示加速為生效（`industry_util.tl:55-91`）。
- 批量**不**隨用地減少：小礦場和大礦場需要一樣多的工具（`industryutil.lua:227-229`）。
- 兩種加速相乘：產量 × 工人係數 ×（1 + 加速貨物加成）（`industry_util.tl:42-104`）。

## 工人加速效果

一半的職位（20 個中的 10 個）必須由最近 2 年內**搭你的客運路線到達**的居民占據；係數為 ×1.5 到 ×2.5，每個產業固定（`industry_productivity_util.tl:35-72`）。只是被分配的工人不算。詳見：[工人與工人加速效果](workers.html)。

## 為什麼我的產業沒有加速效果？

1. **不是原料產業**：工廠沒有加速規則，只有工人加速（`steel_mill.con.lua:61-70`）。
2. **批量不足**：庫存裡要有完整一批，例如煤礦場要 13 工具。每年少於 4 批（52 工具），加速會在兩次送貨之間中斷。
3. **貨物不對**：依產業不同為工具、機械或肥料（上表）。
4. **工人**：只分配不夠；加速效果部分統計的是到達人數（「12/10」）（`industry_react_util.tl:617-654`）。見 [工人與工人加速效果](workers.html)。

## 閒置產業何時關閉？

```diagram ind_closure
```

每個產業每 100 次更新檢查一次（`industries.script.tl:84-85`）：

1. **候選**：**5 年**內沒有貨物**裝載**上車，也沒有**消耗**（從未有過則從建成時算起）（`industries.script.tl:104-119`、`industries_config.res.lua:6`）。只生產不算。
2. **機率**：每年候選依設定**工業關閉頻率**的機率被標記（下表）（`industries.script.tl:120-131`）。
3. **倒數**：出現通知**工業關閉**，剩 2 年（730 天）（`industries_config.res.lua:7`、`industry_close.script.tl:53-67`）。之後產業連同它自己的道路段一起被移除（`industries.script.tl:147-155`、`industry_util.tl:560-601`）。
4. **挽救**：倒數期間只要有一次裝載或消耗就會取消（`industries.script.tl:134-137`）。為它接受**供應產業**或**運送工人**補助也會取消（`subvention_util.tl:473-484`）。

| 工業關閉頻率 | 作為候選每年的機率 | 一半候選被標記所需時間 | 預設組合 | 來源 |
|---|---|---|---|---|
| 永不 | 0 | 永不 | 簡單 | `difficulty_util.tl:94` |
| 極少（預設） | 1.1 % | 約 63 年 | 普通 | `difficulty_util.tl:121` |
| 偶爾 | 2.2 % | 約 32 年 | 困難 | `difficulty_util.tl:149` |
| 經常 | 4.4 % | 約 16 年 | – | `difficulty_util.tl:37` |
| 頻繁 | 8.8 % | 約 8 年 | 極度困難 | `difficulty_util.tl:176` |

機率為每年 0.011 × 0、1、2、4 或 8（`mod.script.tl:171`、`mod.script.tl:202-203`、`difficulty_util.tl:37`）。你擁有的產業永不關閉，手動發展的產業和教學期間的任何產業也不會關閉（`industries.script.tl:94-102`）。

```engine
什麼算「裝載」和「消耗」（日誌 itemsLoaded 和 itemsConsumed，例如加速貨物算不算）、manualDevelopment 旗標，以及有車庫的產業為何被跳過（`industries.script.tl:140-146`），都在引擎一側。引擎如何處理失去投入的加速規則（投入關閉）也是如此。
```

## 新產業

- 引擎隨時間增加產業；腳本只給它 50 年的目標時間、指數 3，以及地圖編輯器中不產生新產業（`mod.script.tl:166-168`）。設定**產業密度目標**調整它（`mod.script.tl:194-195`）。通知為**產業已建立**（`industry_spawn.res.lua:6`）。
- 公司特權**資源探勘**在城鎮附近尋找該資源的新產業：每月嘗試一次，機率從 20 % 到 60 %，持續 6 個月；失敗則退還許可（`company_util.tl:14-17`、`company.script.tl:96-142`、`company.script.tl:299-307`）。

```engine
新產業出現在哪裡、何時出現、是什麼類型，由引擎決定（makeIndustrySpawnProposal）。
```

## 小知識

- 想讓原料產業擴展，就要從它那裡運貨：沒運走的產量會阻止擴展，無論有多少加速。
- 把加速貨物送到最大的礦場和農場：批量一樣，加成隨用地增加。
- 庫存不會損耗：可以提前送加速貨物，直到庫存上限（100）。
- 加速會增加噪音和汙染：煤礦場的汙染一個加速從 10 升到 20，兩個升到 30（`coal_mine.con.lua:99-117`）。
- 預設設定下閒置產業很少關閉；在頻繁時，偶爾裝點貨。

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 是 5 年而不是 10 年，且生產不算：只算裝載上車或被消耗的貨物。5 年後產業只是候選：每年以 1.1 %（極少）到 8.8 %（頻繁）的機率被標記。倒數如所述為 730 天。加速貨物每個產業 +50 % 到 +150 %，每批持續 3 個月。
result: differs
```
