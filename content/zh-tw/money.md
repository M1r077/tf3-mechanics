---
title: 為什麼我在虧錢？
summary: 什麼能賺錢、什麼要花錢，以及找出虧錢路線及其原因的六步檢查，並連結到解釋每一點的頁面。
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-15
fact: 1 | 每單位貨物的付款，在消費地，依直線計算
fact: 0 | 在貨物倉庫或轉乘處的付款
fact: 100 % | 遲到也照付
fact: ×6 | 到 2020 年貨物倉庫、港口與機場維護費的年份係數
---

一次配送依**一條直線**付款：從貨物生產的地方到使用的地方，而且只在貨物抵達那裡時才付。你建造與購買的一切每年都要花錢，其中一部分隨著年份越來越貴。當一條路線分到的付款少於它帶來的成本時，它就在虧錢。

```diagram money_flow
```

## 什麼能賺錢

- 從來源到消費地的**直線距離**，加上 8 × 爬升。你的路線長度不算（`cargo_income.script.lua:3-7`，`cargo_income.script.lua:5`）。
- **每種貨物每公里付的錢都一樣**：所有貨物的收益係數都是 3.8（`cargotype.script.lua:7-13`）。
- **只付一次，在消費地。** 在貨物倉庫或轉乘站卸貨不付任何錢。之後付款依各段的直線長度分給鏈上的各條路線（遊戲內實測）。
- **遲到的貨物照樣全額付款**：不使用運輸時間（`cargotype.script.lua:7-13`）。遲到只會降低城鎮的配送評價。
- **公司等級**會搭配**通貨膨脹**設定降低所有收益：等級 15 時，普通為 ×0.75（`company_progression_util.tl:25-40`）。
- **達成的補助**會讓其涵蓋的配送收益加倍，持續 5 年：配送到其產業、配送到其城鎮，或往返其兩座城鎮的乘客，且只限其路線（`subvention_util.tl:286`）。見 [補助：提案、期限與獎勵](subsidies.html)。

詳情：[貨運收益與配送時間](income.html)。

## 什麼要花錢

- **車輛**：營運成本隨平均速度 × 容量變化，價格等於 6 年的營運成本（`model_metadata_util.lua:499-518`，`model_metadata_util.lua:548-549`）。
- **軌道與道路**：每公里每年約為建造價格的六分之一；高速軌道的成本是普通軌道的 9 倍（`simple.street_template.lua:33`，`high_speed.street_template.lua:35`）。
- **車庫、車站、貨物倉庫、港口、機場**：後期時代的版本為 ×3 與 ×9（`rail_depot.con.lua:7`，`warehouse.tl:48`）；貨物倉庫、港口與機場的維護費還隨年份變化，從 1900 年的 ×1 到 2020 年的 ×6（`mod.script.tl:92-100`）。
- **貸款**：利率只對金額收一次，分攤到整個期限（`loan_util.tl:102-111`）。
- **通貨膨脹不會提高任何成本**。它只降低收益。

詳情：[成本、維護費與貸款](costs.html)。

## 依序做六項檢查

```diagram money_check
```

1. **哪些路線在虧錢？** 看每條路線的收支，而不是公司總額。[Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 模組會顯示每條路線最近 12 個月的收支與幾年的平均值。
2. **貨物走得遠嗎？** 只有從來源到消費地的直線才付錢。通往貨物倉庫的短支線只能拿到它自己那一小段的份額（[貨運收益與配送時間](income.html)）。
3. **是滿載運行嗎？** 車輛滿載與空載的成本一樣。看空車回程，以及每個站點的**裝填量**與**滿載**（[發車設定：滿載、裝填量與停留時間](departure.html)）。
4. **是在付錢的地方卸貨嗎？** 不在站點裝載清單裡的貨物會卸到附近任何庫存裡，包括貨物倉庫，而貨物倉庫不付錢（[裝載與卸貨速度](loading.html)，[貨物倉庫](warehouses.html)）。城鎮庫存已滿時放不下的貨物會留在車上（[城鎮成長：經驗值、評價與規模](towns.html)）。
5. **車輛太好了？** 速度與容量都要花錢，但速度本身不付錢：只有能讓每年多跑幾趟時才有用。在城鎮裡，舊的慢速公車可能比新的快速公車更賺錢（[成本、維護費與貸款](costs.html)）。
6. **固定成本。** 車庫、多餘的貨物倉庫模組、高速軌道與後期時代的建築，不管用不用每年都要花錢（[成本、維護費與貸款](costs.html)）。

## 小知識

- **依數量與距離選擇貨物**，而不是依價格：每種貨物每公里付的錢都一樣。
- 由短路線供貨的**長幹線**賺走大部分的錢；支線的收支看起來很小，但重要的是整條鏈。
- **更多可運的貨**：加速的產業產量更多（[工人與工人加速效果](workers.html)，[產業](industries.html)），更大的城鎮需要更多貨物。
- 加快路線不會提高每單位貨物的付款。只有同樣的車輛跑更多趟時才有用。

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks))
scripts: 相同：直線加 8 × 爬升，所有貨物係數相同，不使用運輸時間；遊戲內實測：在消費地只付一次，並依各段長度分配；成本：車輛隨速度 × 容量，軌道為價格的 1/6，建築有時代版本 ×3 / ×9 與 ×1 到 ×6 的年份係數；通貨膨脹只降低收益。
result: refines
```
