---
title: 为什么我在亏钱？
summary: 什么能赚钱、什么要花钱，以及找出亏钱线路及其原因的六步检查，并链接到解释每一点的页面。
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-15
game: 40425
fact: 1 | 每单位货物的付款，在消费地，按直线计算
fact: 0 | 在仓库或换乘处的付款
fact: 100 % | 迟到也照付
fact: ×6 | 到 2020 年仓库、港口和机场维护费的年份系数
---

一次运输按**一条直线**付款：从货物生产的地方到使用的地方，而且只在货物到达那里时才付。你建造和购买的一切每年都要花钱，其中一部分随着年份越来越贵。当一条线路分到的付款少于它带来的成本时，它就在亏钱。

```diagram money_flow
```

## 什么能赚钱

- 从来源到消费地的**直线距离**，加上 8 × 爬升。你的路线长度不算（`cargo_income.script.lua:3-7`，`cargo_income.script.lua:5`）。
- **每种货物每公里付的钱都一样**：所有货物的收入系数都是 3.8（`cargotype.script.lua:7-13`）。
- **只付一次，在消费地。** 在仓库或换乘站卸货不付任何钱。之后付款按各段的直线长度分给链上的各条线路（游戏内实测）。
- **迟到的货物照样全额付款**：不使用运输时间（`cargotype.script.lua:7-13`）。迟到只会降低城镇的运送评价。
- **公司等级**会配合**通货膨胀**设置降低所有收入：等级 15 时，正常为 ×0.75（`company_progression_util.tl:25-40`）。
- **完成的补贴**会让其覆盖的交付收入翻倍，持续 5 年：交付到其产业、交付到其城镇，或往返其两座城镇的乘客，且只限其线路（`subvention_util.tl:286`）。见 [补贴：报价、期限与奖励](subsidies.html)。

详情：[货物收入与运输时间](income.html)。

## 什么要花钱

- **载具**：运营成本随平均速度 × 容量变化，价格等于 6 年的运营成本（`model_metadata_util.lua:499-518`，`model_metadata_util.lua:548-549`）。
- **轨道和道路**：每公里每年约为建造价格的六分之一；高速轨道的成本是普通轨道的 9 倍（`simple.street_template.lua:33`，`high_speed.street_template.lua:35`）。
- **车库、车站、仓库、港口、机场**：后期时代的版本为 ×3 和 ×9（`rail_depot.con.lua:7`，`warehouse.tl:48`）；仓库、港口和机场的维护费还随年份变化，从 1900 年的 ×1 到 2020 年的 ×6（`mod.script.tl:92-100`）。
- **贷款**：利率只对金额收一次，分摊到整个期限（`loan_util.tl:102-111`）。
- **通货膨胀不会提高任何成本**。它只降低收入。

详情：[成本、维护费与贷款](costs.html)。

## 按顺序做六项检查

```diagram money_check
```

1. **哪些线路在亏钱？** 看每条线路的收支，而不是公司总额。[Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 模组会显示每条线路最近 12 个月的收支和几年的平均值。
2. **货物走得远吗？** 只有从来源到消费地的直线才付钱。通往仓库的短支线只能拿到它自己那一小段的份额（[货物收入与运输时间](income.html)）。
3. **是满载运行吗？** 载具满载和空载的成本一样。看空车返程，以及每个站点的**填充水平**和**满载**（[发车设置：满载、填充水平与停靠时间](departure.html)）。
4. **是在付钱的地方卸货吗？** 不在站点载重列表里的货物会卸到附近任何库存里，包括仓库，而仓库不付钱（[装载与卸载速度](loading.html)，[仓库](warehouses.html)）。城镇库存已满时放不下的货物会留在车上（[城镇增长：经验、评价与规模](towns.html)）。
5. **载具太好了？** 速度和容量都要花钱，但速度本身不付钱：只有能让每年多跑几趟时才有用。在城镇里，旧的慢速公交车可能比新的快速公交车更赚钱（[成本、维护费与贷款](costs.html)）。
6. **固定成本。** 车库、多余的仓库模块、高速轨道和后期时代的建筑，不管用不用每年都要花钱（[成本、维护费与贷款](costs.html)）。

## 须知

- **按数量和距离选择货物**，而不是按价格：每种货物每公里付的钱都一样。
- 由短线路供货的**长干线**赚走大部分的钱；支线的收支看起来很小，但重要的是整条链。
- **更多可运的货**：加成的产业产量更多（[工人与工人加成](workers.html)，[产业](industries.html)），更大的城镇需要更多货物。
- 加快线路不会提高每单位货物的付款。只有同样的载具跑更多趟时才有用。

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks))
scripts: 相同：直线加 8 × 爬升，所有货物系数相同，不使用运输时间；游戏内实测：在消费地只付一次，并按各段长度分配；成本：载具随速度 × 容量，轨道为价格的 1/6，建筑有时代版本 ×3 / ×9 和 ×1 到 ×6 的年份系数；通货膨胀只降低收入。
result: refines
```
