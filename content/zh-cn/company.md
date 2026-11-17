---
title: 公司等级、特权与总部
summary: 什么会提升公司等级，每个等级解锁什么，许可和勘探如何运作，总部实际提供什么，以及更高等级的代价。
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40425
fact: 15 | 个公司等级，从低级职员到商业大亨
fact: ×12.5 | 达到等级 15 所需的世界人口（与开局相比）
fact: ×0.75 | 通货膨胀为正常时等级 15 的收入
fact: 0 | 人口下降时失去的等级
---

公司等级不取决于金钱或运输量，而取决于**整张地图的人口**。每个新等级都会解锁特权（地标、勘探、营销活动、产业绿化、总部模块），而在**通货膨胀**设置下，它还会让你的所有收入略微下降。

## 什么会提升等级

- 游戏会记住**开局时的世界人口**：所有城镇的居民数（`company.script.tl:392-396`，`company_util.tl:365-371`）。
- 然后把历史上达到的**最高**世界人口与该开局值比较（`company_growth.script.tl:25-27`）。这个值只增不减：城镇缩小永远不会让你掉级。
- 等级 1 在开局值时达到，等级 15 在约 **12.5 倍**时达到（`company_progression_util.tl:6-14`，`company_progression_util.tl:95-120`，`town_growth_function.tl:13-20`）。
- 战役任务和地图编辑器中没有等级（`company_growth.script.tl:74-79`）。

| 等级 | 职位 | 世界人口（与开局相比） |
|---|---|---|
| 1 | 低级职员 | ×1 |
| 2 | 机工 | ×1.02 |
| 3 | 工程师 | ×1.08 |
| 4 | 协调员 | ×1.2 |
| 5 | 专家 | ×1.4 |
| 6 | 小组长 | ×1.7 |
| 7 | 监督员 | ×2.1 |
| 8 | 经理 | ×2.6 |
| 9 | 主管 | ×3.3 |
| 10 | 高级主管 | ×4.2 |
| 11 | CEO | ×5.3 |
| 12 | 主席 | ×6.7 |
| 13 | 副董事长 | ×8.3 |
| 14 | 董事长 | ×10.2 |
| 15 | 商业大亨 | ×12.5 |

这些比例是根据脚本按开局人口 50,000 或以上计算的（`company_progression_util.tl:6-14`，`company_static_util.tl:6-24`）。在小地图上，中间等级略高（5,000 居民时等级 8 需要 ×2.85）；等级 1 和 15 仍为 ×1 和 ×12.5。

- 所以等级跟随**城镇增长**：城镇因你的乘客和货物而增长，见[城镇增长](towns.html)。
- 前几个等级来得很快，最后几个需要地图上的城镇扩大许多倍。

## 新等级在公司窗口中生效

人口越过阈值时会出现**升级通知**；点击它会在该等级上打开公司窗口（`company_growth.script.tl:96-107`，`company_notification_rank_up.script.tl:8-9`）。

- 只有当该等级在**公司窗口中被选中**时，新特权才会解锁：窗口这时发送解锁（`company.tl:420-423`，`company_growth.script.tl:55-62`）。建造菜单检查的是这个已生效的等级（`company_util.tl:92`，`company_util.tl:171-178`）。
- 下一节的收入系数跟随**已达到**的等级，无论是否生效（`company_growth.script.tl:47-48`）。

```tip scripts
升级后点击通知（或打开公司窗口并选择新等级）来获得特权。等待不会带来任何好处：收入已经降低了。
```

## 更高等级的代价：通货膨胀设置

开启**通货膨胀**时，所有货物和乘客收入从等级 1 的 ×1 均匀下降到等级 15 的最低值（`company_progression_util.tl:25-40`，`company_growth.script.tl:159-170`）。

| 通货膨胀 | 等级 15 的收入 | 来源 |
|---|---|---|
| 无 | ×1（不变） | `difficulty_util.tl:50`，`mod.script.tl:694-697` |
| 低 | ×0.9 | |
| 正常 | ×0.75 | |
| 高 | ×0.6 | |
| 非常高 | ×0.5 | |

- 在正常下，每升一级损失约 1.8 % 的收入：等级 3 为 ×0.96，等级 8 为 ×0.875，等级 15 为 ×0.75。
- 通货膨胀不会提高任何成本；成本跟随日历年份（见[成本、维护费与贷款](costs.html)）。
- 更高的等级也会让新的补贴提议更少（见[补贴](subsidies.html)）。

## 许可

大多数特权受**许可**限制。等级为某项特权提供许可；每座建筑或每次使用占用一个（`company_util.tl:33-80`，`company_util.tl:206`）。

- 许可随等级**累加**：在等级 3 给 1 个、等级 5 再给 1 个的特权，从等级 5 起允许 2 个（`company_util.tl:51-56`）。
- 建筑被拆除时会归还许可：游戏统计的是现存的建筑（`company_util.tl:143-163`，`company_util.tl:203-206`）。
- 勘探、营销活动和绿化在开始时消耗许可（`company.script.tl:416-423`，`company.script.tl:459-462`，`company.script.tl:496-500`）。之后建造菜单显示**已使用**或**冷却时间**（`company_util.tl:207-226`）。
- **营销**许可在每次活动 **5 年**后恢复（`marketing.res.lua:6-7`，`company.script.tl:66-94`）。

| 特权 | 许可 | 来源 |
|---|---|---|
| 总部 | 等级 1 时 1 个 | `hq.res.lua:6` |
| 营销活动 | 等级 4 时 1 个，5 年后恢复 | `marketing.res.lua:6-7` |
| 产业绿化 | 等级 3、6、9、12 和 15 各 1 个 | `industry_greenify_tool.script.tl:101-102` |
| 净化厂 | 等级 10 时 15 个 | `pollution_cleanup_facility.con.lua:106-108` |
| 地标 | 各一个：圆形剧场 2，大灯塔 5，姬路城 7，船舶博物馆 9，新天鹅堡 10，自由女神像 11，颐和园 13，歌剧院 14，议会大厦 15 | `arena.con.lua:39`，`lighthouse.con.lua:48`，`white_heron_castle.con.lua:47`，`ship_museum.con.lua:55`，`neuschwanstein.con.lua:55`，`statue_of_liberty.con.lua:57`，`summer_palace.con.lua:63`，`opera_house.con.lua:63`，`westminster.con.lua:79` |

各特权的作用：[城镇声誉](reputation.html)（营销活动），[污染与噪音](emission.html)（绿化，净化厂）。

## 勘探

勘探会在城镇附近寻找一种资源，成功后在那里建立一个新产业。

| 资源 | 等级 | 来源 |
|---|---|---|
| 鱼 | 2 | `exploration_fish.res.lua:9-11` |
| 粘土 | 3 | `exploration_clay.res.lua:9-11` |
| 原油 | 4 | `exploration_crude_oil.res.lua:9-11` |
| 谷物，蔬菜 | 4，**共用一个许可**（产业） | `exploration_grain.res.lua:9`，`exploration_vegetables.res.lua:9`，`permit_key_farm.res.lua:6` |
| 木材 | 5 | `exploration_logs.res.lua:9-11` |
| 煤炭，铁矿石 | 6 | `exploration_coal.res.lua:9-11`，`exploration_iron_ore.res.lua:9-11` |
| 石料，羊毛 | 8 | `exploration_stone.res.lua:9-11`，`exploration_wool.res.lua:9-11` |
| 沙子 | 9 | `exploration_sand.res.lua:9-11` |
| 橡胶 | 12 | `exploration_rubber.res.lua:9-11` |

- 每种资源只有**一个**许可，在勘探开始时使用（`company.script.tl:451-462`）。
- 勘探最长持续 **6 个月**。每月尝试放置一次产业，成功率在 6 个月内从 20 % 升到 60 %（`company_util.tl:14-17`，`company.script.tl:299-307`，`company.script.tl:130-142`）。
- 当游戏在城镇附近找不到放置该产业的地方时，尝试也会失败（`company.script.tl:199-210`）。
- 如果最后一次尝试失败，**许可会归还**，并有通知告知（`company.script.tl:106-126`，`company.script.tl:170-181`）。
- 每个城镇和资源组合同一时间只能进行一次勘探（`company.script.tl:442-447`）。

```engine
新产业可以建在哪里（城镇附近的 makeIndustrySpawnProposal）由引擎决定：远离水域的鱼类勘探，或周围没有空地的城镇，都会直接失败并归还许可。
```

## 总部

| 项目 | 数值 | 来源 |
|---|---|---|
| 价格和维护费 | 免费，无维护费 | `headquarter.script.tl:526-527` |
| 许可 | 1 个，等级 1 时 | `headquarter.con.lua:6-7`，`hq.res.lua:6` |
| 城镇增长 | 离它最近的城镇 +5 % | `headquarter.script.tl:510-515`，`landmark_util.tl:51-70` |
| 工作岗位 | 24 | `headquarter.con.lua:16`，`headquarter.script.tl:505-508` |

- +5 % 是对该城镇增长率的加成，所以当城镇增长率为 0 % 时没有作用（见[城镇增长](towns.html)）。
- **模块**每个 50,000，受随等级增加的许可限制（`hq_module_m.module.lua:83`，`hq_module_m.module.lua:137`）。
- 文件中只有两个模块带有加成：**中型建筑**城镇增长 +1 %（`hq_module_m.module.lua:139-142`）和**大型建筑****声誉恢复** +1 %（`hq_module_l.module.lua:169-172`）。恢复加成不被任何城镇评价读取（见[城镇声誉](reputation.html)）。其他模块都是装饰。
- 每个模块文件开头还有一张给出 +5 % 城镇增长的表，但文件中没有任何地方使用它（`hq_corner_l.module.lua:148-159`，`hq_statue.module.lua:46-57`）。只有模块 `metadata` 中的加成会被累加（`headquarter_addon.script.tl:18-29`）。

| 模块 | 获得许可的等级（×2 = 两个） | 等级 15 时合计 |
|---|---|---|
| 地面旗帜 | 1 ×2，6，7，8，9，11，12，13，14 | 10 |
| 角楼 | 3，5，7 ×2，9，11，13，15 | 8 |
| 中型建筑 | 2，4，10 ×2，15 ×2 | 6 |
| 大型建筑 | 5，6，10，12 | 4 |
| 阳台 | 8 ×2，14 ×2 | 4 |
| 大型喷泉 | 10 ×2，14 ×2 | 4 |
| 穹顶 | 6，15 ×2 | 3 |
| 屋顶旗帜 | 7，10，13 | 3 |
| 网球场 | 11，12，14 | 3 |
| 古树 | 13，15 ×2 | 3 |
| 雕像 | 14 ×2 | 2 |
| 游泳池 | 15 | 1 |

来源：每个模块文件中的 `rankAndPermits` 行（`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`）。

```tip scripts
把总部建在你最想让它快速增长的城镇，并在那里添加中型建筑：它们是唯一带增长加成的模块。
```

## 小贴士

- 想升级就让城镇增长：把更多乘客和货物送到更多城镇，并保持良好的评价。银行里的钱不算数。
- 规划好地标和勘探：每项只有一次，在固定的等级。
- 在有通货膨胀的地图上，升级对特权有利、对收入不利。在正常下，一路升到等级 15 会损失全部收入的四分之一。

```check
official: "The company rank depends on the population of the map. . Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: 规则相同：历史最高的世界人口与开局人口相比，等级 15 为 ×12.5；永不失去。新等级必须在公司窗口中选中才会解锁特权，而通货膨胀会立即降低收入。只有两个模块带有加成（中型建筑增长 +1 %，大型建筑声誉恢复 +1 %，后者不被任何评价读取）；其他都是装饰。
result: refines
```
