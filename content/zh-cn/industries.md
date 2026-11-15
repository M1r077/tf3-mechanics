---
title: 产业
summary: 生产规则、库存、地块与扩张、加成货物、产业为什么没有加成，以及闲置产业到底何时关闭。
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
fact: 5 年 | 没有装载也没有消耗，产业就成为关闭候选
fact: 1.1 % | 极少（默认）时每年的概率，之后 730 天倒计时
fact: +50–150 % | 加成货物的加成，每个产业固定
fact: 3 个月 | 每批加成货物的加成时长
---

每个产业都按**规则**运转：“从输入库存取这个，放那个进输出库存”，每年固定次数。原料产业（矿场、农场、油井）不需要输入，规模来自**地块**。有两种加成能让产量翻倍：**加成货物**（仅原料产业）和**工人**。

## 生产规则

- 规则给出每轮使用和产出的货物，以及每年的轮数：一轮持续一年 ÷ 该数（`industry_react_util.tl:51-57`）。产业窗口的“生产”部分用小数字显示。
- 窗口中的**最大**数值是：每轮 × 每年轮数 × 加成 × 设置**工业生产力**（`industry_util.tl:310-379`）。
- **工业生产力**：50 %、75 %、100 %、150 % 或 200 %。预设：简单 150 %，正常 100 %，困难 75 %，极难 50 %（`difficulty_util.tl:41`、`difficulty_util.tl:93`、`difficulty_util.tl:120`、`difficulty_util.tl:148`、`difficulty_util.tl:175`、`mod.script.tl:196-197`）。
- 例如铁厂：6 铁矿石 + 6 煤炭 → 3 钢 + 4 金属薄板，每年 121.7 轮：730 铁矿石和 730 煤炭 → 365 钢和 487 金属薄板（`steel_mill.con.lua:43-71`）。缺一种输入，规则就停。
- 罐头工厂有两条规则：鱼 + 金属薄板，或肉类 + 金属薄板（`food_factory.con.lua:43-74`）。

```engine
规则由引擎执行。引擎可能延长一轮，这时提示显示“（因运输时间 + …）”（`industry_react_util.tl:61-76`）。何时、延长多少不在脚本里，所以实际产量可能低于最大值。
```

## 库存

- 每种货物有自己的库存和上限：例如煤矿存 100 工具和 400 煤炭，铁厂存 800 铁矿石、800 煤炭、400 钢和 500 金属薄板（`coal_mine.con.lua:44-67`、`steel_mill.con.lua:43-71`）。
- 库存永不损耗（`industryutil.lua:25-29`）：货物可以一直等。
- 输出库存满了不会停产：多出的货物被丢弃（官方 wiki）。**货流量**图表显示**已消耗**、**已生产**和**已摧毁**（`industry_eow.script.tl:804-816`）。
- 建造参数**输入**设为关闭时，规则失去输入，产业也没有输入库存（`industryutil.lua:280-287`、`industryutil.lua:383-387`、`industryutil.lua:432-441`）。

## 地块与扩张

- 原料产业和牲畜养殖场有**地块**（田地、矿井、钻塔）。等级就是地块数（`industryutil.lua:602-617`）。
- 规则随地块增长：每轮产出 × 地块数 ÷ **该类产业的全部地块数**，四舍五入，至少 1。输入按同样比例减少（`industryutil.lua:225-259`）。有 8 种地块的煤矿，若只有 4 块，每轮产 8 煤炭而不是 16。
- 每个产业有一个上限：在一半地块到全部之间随机，或用参数**产业规模**选小 / 中 / 大（50 / 75 / 100 %）（`industryutil.lua:519-537`）。上限为 8 中 5 的矿场永远达不到完整规则。
- 每半年游戏可能增加**一个地块**（`industries_config.res.lua:5`、`industries.script.tl:158-183`）。概率为（评分 − 25 %）÷ 50 %，评分 = 生产评分 × 你运走的产量比例（最多 1）：25 % 及以下从不，75 % 及以上必定（`industries.script.tl:172-176`）。
- 所以你不运走货物的产业**永远不会扩张**。工厂没有地块，也不会扩张。
- 到上限时窗口显示**产业已发展至最大规模。**；被建筑、轨道或道路挡住时显示**产业无法继续扩张。**（`industry_react_util.tl:588-602`、`industries.script.tl:13-38`）。没有脚本会移除地块；官方 wiki 说被拆除的地块会降低产量。

```engine
生产评分（getProductionRating）、年产量与运走量（getCargoOutputPerYear、getCargoShippedPerYear），以及新地块的位置（makeIndustryExtendProposal）都是引擎的值。
```

## 加成货物

13 种原料产业有第二条规则——**加成**：每年 4 次从输入库存取一批加成货物，运行期间给出加成。

| 产业 | 地块 | 满规模每年产量 | 加成批量（每年 4 批） | 来源 |
|---|---|---|---|---|
| 粘土矿坑 | 8 | 365 粘土 | 12 工具 | `clay_pit.con.lua:42-82` |
| 煤矿 | 8 | 320 煤炭 | 13 工具 | `coal_mine.con.lua:44-85` |
| 棉花农场 | 21 | 274 羊毛 | 17 肥料 | `cotton_farm.con.lua:42-98` |
| 作物农场 | 20 | 274 谷物 + 183 蔬菜 | 17 肥料 | `farm.con.lua:44-106` |
| 渔场 | 18 | 263 鱼 | 12 工具 | `fishing_grounds.con.lua:44-101` |
| 伐木营地 | 20 | 243 木材 | 15 机器 | `forest.con.lua:44-99` |
| 铁矿场 | 8 | 365 铁矿石 | 15 机器 | `iron_ore_mine.con.lua:44-84` |
| 采油平台 | 9 | 365 原油 | 12 机器 | `oil_platform.con.lua:45-96` |
| 油井 | 14 | 548 原油 | 15 机器 | `oil_well.con.lua:44-94` |
| 采石场 | 7 | 365 石料 | 12 工具 | `quarry.con.lua:44-83` |
| 橡胶农场 | 23 | 365 橡胶 | 17 肥料 | `rubber_farm.con.lua:41-102` |
| 挖砂船 | 9 | 365 沙子 | 15 机器 | `sand_excavator.con.lua:44-92` |
| 沙坑 | 8 | 365 沙子 | 12 工具 | `sand_pit.con.lua:44-84` |

- 加成在每个产业抽取一次：**+50 % 到 +150 %**，精确到 1 %（`industryutil.lua:394-405`）。加成部分显示为“+X %”（`industry_util.tl:428-434`）。使用参数**促进因素**时改为 +50 %、+75 %、+100 %、+125 % 或 +150 %（`industryutil.lua:289-299`）。
- 窗口在最后一批持续期间（3 个月），或库存一凑满一批时，就显示加成为生效（`industry_util.tl:55-91`）。
- 批量**不**随地块减少：小矿场和大矿场需要一样多的工具（`industryutil.lua:227-229`）。
- 两种加成相乘：产量 × 工人系数 ×（1 + 加成货物加成）（`industry_util.tl:42-104`）。

## 工人加成

一半的岗位（20 个中的 10 个）必须由最近 2 年内**乘你的客运线路到达**的居民占据；系数为 ×1.5 到 ×2.5，每个产业固定（`industry_productivity_util.tl:35-72`）。只是被分配的工人不算。详见：[工人与工人加成](workers.html)。

## 为什么我的产业没有加成？

1. **不是原料产业**：工厂没有加成规则，只有工人加成（`steel_mill.con.lua:61-70`）。
2. **批量不足**：库存里要有完整一批，例如煤矿要 13 工具。每年少于 4 批（52 工具），加成会在两次送货之间中断。
3. **货物不对**：按产业不同为工具、机器或肥料（上表）。
4. **工人**：只分配不够；加成部分统计的是到达人数（“12/10”）（`industry_react_util.tl:617-654`）。见 [工人与工人加成](workers.html)。

## 闲置产业何时关闭？

```diagram ind_closure
```

每个产业每 100 次更新检查一次（`industries.script.tl:84-85`）：

1. **候选**：**5 年**内没有货物**装载**上车，也没有**消耗**（从未有过则从建成时算起）（`industries.script.tl:104-119`、`industries_config.res.lua:6`）。只生产不算。
2. **概率**：每年候选按设置**工业关闭频率**的概率被标记（下表）（`industries.script.tl:120-131`）。
3. **倒计时**：出现通知**工业关闭**，剩 2 年（730 天）（`industries_config.res.lua:7`、`industry_close.script.tl:53-67`）。之后产业连同它自己的道路段一起被移除（`industries.script.tl:147-155`、`industry_util.tl:560-601`）。
4. **挽救**：倒计时期间只要有一次装载或消耗就会取消（`industries.script.tl:134-137`）。为它接受**供应产业**或**运输工人**补贴也会取消（`subvention_util.tl:473-484`）。

| 工业关闭频率 | 作为候选每年的概率 | 一半候选被标记所需时间 | 预设 | 来源 |
|---|---|---|---|---|
| 从不 | 0 | 从不 | 简单 | `difficulty_util.tl:94` |
| 极少（默认） | 1.1 % | 约 63 年 | 正常 | `difficulty_util.tl:121` |
| 有时 | 2.2 % | 约 32 年 | 困难 | `difficulty_util.tl:149` |
| 经常 | 4.4 % | 约 16 年 | – | `difficulty_util.tl:37` |
| 极频繁 | 8.8 % | 约 8 年 | 极难 | `difficulty_util.tl:176` |

概率为每年 0.011 × 0、1、2、4 或 8（`mod.script.tl:171`、`mod.script.tl:202-203`、`difficulty_util.tl:37`）。你拥有的产业永不关闭，手动发展的产业和教程期间的任何产业也不会关闭（`industries.script.tl:94-102`）。

```engine
什么算“装载”和“消耗”（日志 itemsLoaded 和 itemsConsumed，例如加成货物算不算）、manualDevelopment 标志，以及有车库的产业为何被跳过（`industries.script.tl:140-146`），都在引擎一侧。引擎如何处理失去输入的加成规则（输入关闭）也是如此。
```

## 新产业

- 引擎随时间增加产业；脚本只给它 50 年的目标时间、指数 3，以及地图编辑器中不生成新产业（`mod.script.tl:166-168`）。设置**产业目标密度**调节它（`mod.script.tl:194-195`）。通知为**行业创立**（`industry_spawn.res.lua:6`）。
- 公司特权**资源勘探**在城镇附近寻找该资源的新产业：每月尝试一次，概率从 20 % 到 60 %，持续 6 个月；失败则返还许可（`company_util.tl:14-17`、`company.script.tl:96-142`、`company.script.tl:299-307`）。

```engine
新产业出现在哪里、何时出现、是什么类型，由引擎决定（makeIndustrySpawnProposal）。
```

## 须知

- 想让原料产业扩张，就要从它那里运货：没运走的产量会阻止扩张，无论有多少加成。
- 把加成货物送到最大的矿场和农场：批量一样，加成随地块增加。
- 库存不会损耗：可以提前送加成货物，直到库存上限（100）。
- 加成会增加噪音和污染：煤矿的污染一个加成从 10 升到 20，两个升到 30（`coal_mine.con.lua:99-117`）。
- 默认设置下闲置产业很少关闭；在极频繁时，偶尔装点货。

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 是 5 年而不是 10 年，且生产不算：只算装载上车或被消耗的货物。5 年后产业只是候选：每年以 1.1 %（极少）到 8.8 %（极频繁）的概率被标记。倒计时如所述为 730 天。加成货物每个产业 +50 % 到 +150 %，每批持续 3 个月。
result: differs
```
