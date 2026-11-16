---
title: 城镇声誉
summary: 什么会降低城镇的声誉评价，它恢复得多快，庆典和营销活动实际做了什么，以及为什么切断两座城镇之间的道路代价这么大。
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
game: 40425
fact: −33 % | 每切断一条通往其他城镇的主要连接
fact: ≈ 67 % | 日历速度 ×1 时每年恢复（营销活动期间 ≈ 200 %）；城镇窗口显示 33 % 和 100 %
fact: 0.25 % | 在城镇旁每移除一棵成年树
fact: 200 万 m³ | 地形工程会耗尽全部声誉
---

**声誉**是城镇窗口六项评价之一，城镇当局取其中**最低**的一项（见[城镇增长](towns.html)）。声誉从 100 % 开始，只会因为**你**建造或失败的事情而下降：地形工程、移除树木和石头、拆除城镇建筑、失败的补贴，以及被切断的主要连接。时间、庆典和营销活动会让它回升。

```diagram rep_recovery
```

## 什么会降低声誉

你确认的每次建造都会在执行前检查；损失记在相关城镇上（`towns.script.tl:271-291`，`town_util.tl:1062-1080`）。只有你自己的建造才算，地图编辑器中什么都不算（`town_util.tl:1078-1080`，`towns.script.tl:58`）。

| 城镇窗口中的原因 | 什么会损失声誉 | 来源 |
|---|---|---|
| **移除树木** | 每棵 0.25 %，× 到最近城镇的距离系数，× 树的大小（小树算得少） | `town_util.tl:1144-1150`，`town_util.tl:865`，`model_metadata_util.lua:655-680` |
| **移除石头** | 每块 0.25 %，× 距离系数 | `town_util.tl:1148-1149`，`town_util.tl:884-885` |
| **景观美化** | 地形抬高**或**降低，每 m³ 0.00005 %：200 万 m³ = 100 %。轨道、道路和建筑塑造的地形也算（从 10,000 m² 起递减，50,000 m² 及以上减半），新隧道的净体积也算 | `town_util.tl:873-886`，`town_util.tl:1245-1269`，`town_util.tl:1403-1436` |
| **拆除建筑** | 拆掉一个区（该城镇的住宅、商店或工作岗位）40.5 % 的容量 = 100 % | `town_util.tl:867-869`，`town_util.tl:1165-1184` |
| **失败的补贴** | 供给城镇：10 % 起，按风险最高 60–90 %；连接城镇：10–100 % × 距离系数，**两座**城镇都扣（见[补贴](subsidies.html)） | `deliver_cargo_town.script.tl:202-210`，`deliver_passengers.script.tl:113-114`，`towns.script.tl:331-333` |
| **切断主要连接点** | 每有一座主要连接被切断或过长的其他城镇，扣 **1/3** | `town_util.tl:376-394`，`town_util.tl:1608` |

- 每个原因最多 100 %（`town_util.tl:1611-1620`）。
- 建造时提示框显示**声誉：-x %**，涉及多座城镇时还会显示数量（`construction_react_util.tl:3818-3864`）。它按满分评价计算。
- 种树或放置石头只会抵消**移除树木**或**移除石头**，每个同样 0.25 %。对其他原因无效，声誉满分时也无效（`town_util.tl:1228-1238`，`town_util.tl:1630-1641`）。
- 新游戏的声誉设置为**关闭**或**打开**（所有预设都是打开）。关闭表示评价永远满分（`difficulty_util.tl:44`，`difficulty_util.tl:110`，`town_util.tl:396-399`）。

```engine
城镇与被移除树木之间的距离系数下降得多快、每座城镇分到的地形体积、轨道或道路自动移除的树木，以及哪些道路算作城镇的主要连接（以及行程何时算“过长”），都是引擎数值（getImpactFromDistance、getTerrainBrushVolumeImpact、getTerrainAlignmentImpact、getAutoRemovalEntityImpact、getTownProblems）。
```

## 被切断的主要连接

当游戏提示**城镇之间的道路连接已中断**或**城镇之间的旅行时间过长**时，主要连接就算被切断（`town_util.tl:378-380`，`town_warning.script.tl:7-22`）。每座相关的其他城镇扣 1/3，评价会**立刻**显示出来（`town_util.tl:401-403`）：

| 被切断的连接 | 声誉最多 | 评价 | 来源 |
|---|---|---|---|
| 1 | 67 % | 非常好 | `town_util.tl:983-985` |
| 2 | 33 % | 中等 | `town_util.tl:983-985` |
| 3 | 0 % | 非常贫穷：城镇停止增长 | `town_util.tl:607-633` |

- 切断期间，惩罚也会在 3 个月内一步步写进保存的分数（`towns.script.tl:137-145`）。修好道路后，这部分只按正常速度恢复：长时间切断会在之后一段时间里继续拖累声誉。
- 67 % 正好在“非常好”的边界上：再有任何小损失，城镇就会降到“好”。

```tip scripts
**先建新路，再拆旧路。** 每条被切断的主要连接会立刻扣掉三分之一的声望，切断越久，恢复也越久。
```

## 声誉如何恢复

- **自动恢复**：每 3 个月游戏时间（360 秒）恢复一级（1/6），营销活动期间每个月（120 秒）一级（`towns.script.tl:121-135`）。日历速度 ×1 时约为每年 **67 %**，活动期间 **200 %**：从 0 % 回满约需 1.5 年。城镇窗口中的**年度声誉恢复** 33 % 和 100 % 是固定文字，只有实际速度的一半（`town_react_util.tl:1066`）。在测试城镇实测：每 358 秒一级，活动期间每 120 秒一级。
- 恢复会把增加量分到所有原因上；不会超过仍未修复的切断连接（`town_util.tl:1649-1687`）。
- **庆典**：城镇里第一位乘客登上你的线路 **+50 %**，第一批货物送到城镇 +50 %，城镇每次升级 +50 %，每个工业第一次收到货物时最近的城镇 +20 %（`celebrations.script.tl:181-273`）。这时消息末尾会加上**定居点声誉已提升。**或**你在…的声誉有所提升。**（`celebration_react_util.tl:63-75`）。只有声誉低于被切断的主要连接仍允许的上限（满分减去每条切断连接 1/3）且声誉设置为打开时才算，战役任务中不算（`celebrations.script.tl:79-93`，`celebrations.script.tl:140-142`）。
- **供给城镇**接受时可给 +5 % 到 +20 % × 风险系数（`deliver_cargo_town.script.tl:195-199`）。和所有增加一样，它只抵消已有的损失（`towns.script.tl:324-330`）。

## 营销活动

| 项目 | 数值 | 来源 |
|---|---|---|
| 价格 | 10 M × 年份系数：1900 年 4 M，到 2020 年 25 M，取整到 1 M | `marketing_campaign_tool.script.tl:9-14` |
| 需要 | 公司津贴中的一张许可 | `marketing_campaign_tool.script.tl:83-95`，`company.script.tl:416-423` |
| 持续时间 | 一年 | `marketing_campaign_tool.script.tl:136` |
| 声誉 | 恢复 ×3（每年 ≈ 200 %，窗口显示 100 %）；**没有**立即增加 | `towns.script.tl:126`，`town_util.tl:915-925` |
| 居民 | 居民选择出行方式时，你在该城镇的线路按一半成本计算 | `marketing_campaign_tool.script.tl:137`，`towns.script.tl:376-398` |

```engine
脚本按每级 360 秒游戏时间计算（活动期间 120 秒），一个月为 30 天、每天 4 秒。恢复按游戏时间进行：日历越慢，日历上的一年越长，每个显示年份恢复得越多。线路成本减半能把多少居民吸引到你的线路上，由引擎的路线选择决定。
```

## 须知

- 留意建造提示框：如果显示**声誉：-x %**，隧道或更平缓的线路往往比声誉更划算。
- 不要让两座城镇之间的主要道路一直断着：每条立刻 −33 %，三条会让城镇停下。
- 声誉满分时的营销活动只帮助你的线路，不提升评价。在大工程刚结束、恢复还有东西可补时再开展。
- 总部大型模块的**声誉恢复**奖励（+1 %）会显示在奖励标签页中，但在脚本里它只改变一个没有任何评价读取的数值（`hq_module_l.module.lua:171`，`towns.script.tl:157`，`town_util.tl:829`，`town_util.tl:857`）。
- 成就**不是我的错**需要在自由游戏中让一座城镇的声誉达到 0 %（`achievements.script.tl:261-267`）。

```check
official: "Reputation reflects how the town and surrounding nature are treated. Landscaping, removing town buildings and breaking main connections to other towns can lower it, while celebrations and marketing campaigns can improve it. Reputation lost by removing trees can be recovered by planting new ones." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: 原因相同，另外还有移除石头、隧道、轨道和道路的地形以及失败的补贴。每条被切断或过长的主要连接立刻扣 1/3；三条会让城镇停下。自动恢复约为每年 67 %，营销活动期间约 200 %，是城镇窗口显示值（33 % 和 100 %）的两倍；活动不会立即增加。种树只抵消树木造成的损失。总部的声誉恢复奖励在脚本中没有效果。
result: differs
```
