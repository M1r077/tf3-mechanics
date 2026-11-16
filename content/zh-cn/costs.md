---
title: 成本、维护费与贷款
summary: 成本设置改变什么，哪些成本随日历年份增长，载具价格如何计算，以及一笔贷款真正要花多少钱。
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: ×6 | 到 2020 年仓库、港口和机场维护费的年份系数
fact: 6 年 | 的运营成本：这就是一辆载具的价格
fact: 一次 | 贷款利率只按金额收一次，而不是每年都收
fact: 4 | 笔贷款可同时存在
---

**通货膨胀** 设置不会提高任何成本：它只会随着公司等级上升而降低你的收入（见 [货物收入与运输时间](income.html)）。成本改为随**日历年份**增长，另有四个滑块从一开始就决定它们的倍率。

```diagram cost_years
```

## 成本设置

| 设置 | 数值 | 预设 简单 · 正常 · 困难 · 极难 | 来源 |
|---|---|---|---|
| **载具成本**、**载具养护** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:39`，`difficulty_util.tl:98-99`，`difficulty_util.tl:125-126` |
| **基础设施成本**、**基础设施维护** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:100-101`，`difficulty_util.tl:153-156`，`difficulty_util.tl:180-183` |
| **载具老化影响** | 无 ×0 · 低 ×0.5 · 中 ×1 · 高 ×1.5 · 非常高 ×2 | 低 · 中 · 高 · 非常高 | `difficulty_util.tl:42`，`difficulty_util.tl:103`，`difficulty_util.tl:185` |
| **通货膨胀** | 只影响收入，见 [货物收入与运输时间](income.html) | 低 · 正常 · 高 · 非常高 | `difficulty_util.tl:50`，`mod.script.tl:694-697` |

- **基础设施成本** 决定道路、轨道、桥梁、隧道、道口、建筑和模块的价格，也包括地形改造（`post_run_util.tl:23-52`，`post_run_util.tl:83-120`，`construction.script.tl:31-35`，`mod.script.tl:223-226`）。它也决定建筑的拆除费用（`construction.script.tl:39-44`）。**基础设施维护** 决定它们的维护费（`post_run_util.tl:43-45`，`post_run_util.tl:105-112`，`entity_window_util.tl:186`）。
- **载具成本** 和 **载具养护** 决定每辆载具的购买价格和运营成本（`post_run_util.tl:54-81`）。
- **载具老化影响** 决定状态差的载具会损失多少速度、功率和舒适度，又会增加多少噪音、污染和运营成本（`mod.script.tl:241-245`）。

## 随日历年份增长的东西

- **建筑维护费**：1900 年 ×1，1920 年 ×1.5，1940 年 ×2.2，1960 年 ×3.2，1980 年 ×4，2000 年 ×5，2020 年 ×6（`mod.script.tl:92-100`）。建筑窗口和建造菜单会把它用于每个标记为跟随年份的建筑，而建造菜单标记的是：仓库、单跑道机场、双跑道机场和港口（`entity_window_util.tl:186-193`，`construction_react_util.tl:1149`，`warehouse.tl:7`，`harbor_modular.tl:24`）。
- 加到这类建筑上的**模块**，价格按建筑建造的年份计算，维护费按当前年份计算（`construction.tl:3720-3727`，`construction.tl:4364-4367`）。
- **时代版本**：车库、维修站、仓库、车站、港口和机场每个时代有一个版本，后面的版本花费是第一个的 **×3**（时代 B）或 **×9**（时代 C）（`rail_depot.con.lua:7`，`warehouse.tl:48`，`modular_station.con.lua:71`，`harbor_modular.tl:76`，`airport.tl:8`）。
- **补贴现金**：从 1900 年的 ×1 到 2000 年起的 ×4（`finances_util.tl:87-90`）。**贷款金额**：从 1900 年的 ×0.4 到 2020 年的 ×2.4（`loan_util.tl:7-10`）。
- **收入**完全没有年份系数（`cargo_income.script.lua:10-13`）。

```engine
实际收取的维护费，以及道路、轨道和载具是否也跟随年份表，由引擎决定（getCostMultiplierForYear；基础配置只设置了 chargeMaintenanceInterval = 60，`mod.script.tl:105`）。脚本只用上面的表计算窗口和建造菜单中显示的数值。没有脚本给其他建筑设置“跟随年份”标记。
```

## 轨道、道路和建筑

道路和轨道文件给出每米的价格和每年的维护费；建造菜单按每公里显示（`construction_react_util.tl:2463`，`construction_react_util.tl:2477-2485`）。大多数类型的维护费是建造价格的**六分之一**：

| 类型 | 出现时间 | 每公里建造费 | 每公里每年维护费 | 来源 |
|---|---|---|---|---|
| 简易轨道 | 开局 | 6 万 | 1 万 | `simple.street_template.lua:9`，`simple.street_template.lua:33` |
| 标准轨道 | 1930 | 18 万 | 3 万 | `standard.street_template.lua:11`，`standard.street_template.lua:35` |
| 高速轨道 | 1980 | 54 万 | 9 万 | `high_speed.street_template.lua:11`，`high_speed.street_template.lua:35` |
| 小型旧乡村道路 | 开局 | 6 万 | 1 万 | `country_old_small.street_template.lua:8`，`country_old_small.street_template.lua:58` |
| 大型新城镇街道 | 1940 | 54 万 | 9 万 | `town_new_large.street_template.lua:11`，`town_new_large.street_template.lua:91` |

- 接触网会增加轨道价格的 **30 %**；公交专用道增加道路价格的 10 %，有轨电车轨道 20 %，电气化有轨电车轨道 40 %（`mod.script.tl:24-28`）。
- 抬高地形每立方米 4.5，降低地形每立方米 5.25（两者都 × 基础设施成本），清除一块农田 20 万（`mod.script.tl:20-22`，`mod.script.tl:33`，`mod.script.tl:225-226`）。
- 没有设置维护费的建筑，每年支付**价格的六分之一**（按基础设施成本设置之前的价格计算，`construction.script.tl:25-27`）。
- 基础配置把拆除返还系数设为 0.75，返还时间设为 60（`mod.script.tl:30-31`）：拆掉刚建好的东西能拿回大部分钱。由引擎执行。

文件中写的每年维护费，第一个版本（1940 年以前）和之后的版本；仓库还要再乘上上面的年份系数：

| 建筑 | 第一个版本 | ×3（1940 年起） | ×9（1980 年起） | 来源 |
|---|---|---|---|---|
| 火车车库、船坞 | 10 万 | 30 万 | 90 万 | `rail_depot.con.lua:34`，`water_depot.con.lua:32` |
| 道路车库 | 3 万 | 9 万 | 27 万 | `road_depot.con.lua:32` |
| 有轨电车车库 | 2 万 | 6 万 | 18 万 | `tram_depot.con.lua:34` |
| 火车或船只维修站 | 4 万 | 12 万 | 36 万 | `rail_maint_station.con.lua:32`，`water_maint_station.con.lua:32` |
| 道路维修站 | 1 万 | 3 万 | 9 万 | `road_maint_station.con.lua:32` |
| 通用仓库 | 2.5 万 | 7.5 万 | 22.5 万 | `warehouse.tl:48-52`，`warehouse.tl:75` |
| 专用仓库 | 5 万 | 15 万 | 45 万 | `warehouse.tl:51`，`warehouse.tl:75` |

这些建筑的建造费都是维护费的 **6 倍**（`rail_depot.con.lua:35`，`warehouse.tl:76`）：最后一个时代的专用仓库，在乘年份系数之前是 270 万。

- 第一个**单跑道机场**（到 1950 年为止）就已经使用第二个时代的 ×3：它的判断读取的是版本的结束年份，而不是开始年份（`airfield.tl:8`，`airfield_era_a.metacon.tl:3`）。

## 载具

基础游戏的载具都没有固定价格：游戏在加载模型时，根据载具的速度和容量计算价格（`model_metadata_util.lua:488-552`）：

1. **每年运营成本** = 约 675 × 平均速度（m/s）× 容量 ÷ 4（`model_metadata_util.lua:499-518`）。675 来自每公里的平均收入，并为空车返程、购买费用和下降的票价留出余地而调低（`model_metadata_util.lua:500-508`）。
2. **平均速度**低于最高速度（v 为 km/h）：道路载具和有轨电车为 v^0.78 + 4，列车为 v^0.86 + 10，飞机为 −0.0000203 × v² + 0.17 × v + 28.36（v 最多 4,000），船只为最高速度的 65 %（`model_metadata_util.lua:448-474`）。
3. **列车**：车厢按容量的一半计算；机车还把 功率 ÷ 最高速度（km/h）× 12.5 当作容量，同样减半（`model_metadata_util.lua:511-512`，`model_metadata_util.lua:526-540`）。强劲而慢的机车很贵。
4. **价格** = 每年运营成本的 **6 倍**（`model_metadata_util.lua:548-549`）。

100 % 时的例子：一辆 35 km/h、载客 48 人的公交车，每年运营成本约 4.5 万，价格约 27 万。

- 载具的状态分为五级（100–80 %，之后每 20 % 一级）（`vehicle_store_util.tl:231-234`）；到 **20 %** 时游戏会发出警告，直到状态回到 30 % 以上（`notifications.script.tl:310-318`）。

```engine
载具状态下降得多快、运营成本随之上升多少，以及载具价格是否随年份变化，都是引擎的数值（getMaintenanceRunningCostPenalty 和其他惩罚项）；脚本只用载具老化影响来缩放它们。
```

## 贷款

```diagram loan_interest
```

| 种类 | 1960 年前后的金额（1900 年 ×0.4，2020 年 ×2.4） | 期限 | 利率 | 来源 |
|---|---|---|---|---|
| 小 | 500 万–1,000 万 | 1–5 年 | 3–5 % | `loan_util.tl:12-22` |
| 中等 | 1,500 万–2,500 万 | 3–8 年 | 5–8 % | `loan_util.tl:24-34` |
| 大 | 3,000 万–5,000 万 | 5–12 年 | 8–10 % | `loan_util.tl:36-46` |
| 特大 | 4,000 万–6,000 万 | 10–24 年 | 10–12 % | `loan_util.tl:48-58` |

- 卡片上写的是**年利率**，但利率只按金额计算**一次**：总利息是 金额 × 利率，与期限无关。它和本金一起按月等额支付（`loan_util.tl:102-111`，`loan_util.tl:126-136`，`loan.script.tl:83-99`）。因此利率相同时，长期贷款每年比短期贷款便宜。
- **偿还** 只支付剩余的本金：剩下的利息直接免掉（`loan.script.tl:171-190`）。按下按钮需要有这么多现金（`finances_loan_gui.tl:284-286`）。
- 利率**不**取决于难度：每种贷款都有自己固定的范围（`loan_util.tl:12-58`）。
- 最多同时 **4 笔贷款**（`loan_util.tl:4`，`loan.script.tl:134`）。报价半年后更换；你借走的那个位置会空 4 到 8 个月（`loan.script.tl:61-76`，`loan.script.tl:150`）。
- 开局时四个位置各自取一种随机种类的数值，所以第一个“小”报价可能是一笔大贷款；报价更新一次后，每个位置就提供自己的种类（`loan_util.tl:60-74`，`loan.script.tl:63-75`）。

```tip scripts
**选最长的贷款，然后提前偿还。** 无论期限多长，总利息都一样，月供更少，偿还时剩下的利息直接免掉。
```

## 须知

- 选能借到的**最长**贷款：总利息相同，分摊到更多月份，而且提前偿还时不用付剩下的利息。
- 有时代版本的建筑在后面的时代花费 ×3 和 ×9，维护费还会随年份不断增长：最后一个时代的专用仓库是一笔很大的固定成本。
- 又快又大的载具运营成本更高，但运得也更多：价格和运营成本跟它能赚的收入一样，都取决于 速度 × 容量。

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: 贷款利率只取决于种类（3–12 %），与难度无关，并且只按金额收一次，分摊到期限内的各个月；提前偿还会免掉剩余利息。通货膨胀只改变收入；建筑维护费跟随年份（×1 到 ×6）；载具价格 = 每年运营成本的 6 倍，两者都来自速度和容量。
result: differs
```
