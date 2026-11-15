---
title: 工人与工人加成
summary: 居民如何在产业找到工作，哪些工人计入加成，以及加成有多大。
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-15
fact: 10 / 20 | 触发加成所需的工人
fact: 2 年 | 一次到达的计入时长
fact: ×1.5–2.5 | 加成系数，每个产业固定
---

每个产业都提供工作岗位。当足够多的工人**乘坐你的客运线路到达**时，产业的产量就会提高。产业窗口显示两个不同的数字，把它们混为一谈是最常见的误解。

```diagram workers_flow
```

## 谁能在产业工作

- 每个基础游戏产业都有 **20 个工作岗位**（`industrialCapacity = 20`）。
- 这些工作岗位的设置让居民**无法步行或开车**前往：只有你的线路能把他们送到（`industryutil.lua:451-457`，`disallowedMoveModes = {"WALK", "DRIVE"}`）。
- 每个居民都有住所、购物地点和工作地点。游戏从该居民能到达的地点中挑选工作地点；产业的目的地权重为 2.0（`industryutil.lua:455`）。

```engine
居民如何在所有能到达的地点中挑选一个工作地点（出行时间、费用、2.0 的权重）由引擎计算。脚本只提供输入数据。
```

## 分配的工人

指工作地点是这个产业的居民。产业窗口中的工作岗位条，以及产业统计中的 **工作场所** 一栏（“12/20”）显示的就是这个数字（`entity_window_util.tl:1238`，`statistic_industries.tl:305`）。仅有分配的工人**不会**带来任何加成：他们必须真正前往产业。

## 计入加成的工人

一个小型游戏脚本会记录每一次到达（`industry_workers.script.tl`）：

1. 当一个居民到达产业，且他的**最后一段行程乘坐的是你的线路**时，这次到达会连同游戏时间一起被记录（`industry_workers.script.tl:86-118`）。
2. 只保留**最近 2 个游戏年**内的到达（`industry_productivity_util.tl:3`：`2 * getDefaultYearDuration()`）。
3. 最多只保留**最近的 20 次**到达（`industry_workers.script.tl:4`，`KeepHistoryCount = 20`）。
4. 同一个人再次到达时，新的记录会替换旧的：每个居民只计**一次**（`industry_workers.script.tl:56-70`）。

```diagram workers_window
```

## 加成何时开始、何时停止

- 当计入的工人达到**工作岗位的一半**时，产业获得加成：`counted ≥ workplaces × 0.5`（`industry_productivity_util.tl:35-48`，`RequiredWorkersFractionForBoost = 0.5`）。20 个工作岗位时：**10 个工人**。
- 产业窗口的“加成”部分显示的正是这个：“已计入 / 所需”，所需人数向上取整（`industry_react_util.tl:627`）。
- 每当有新的到达，或者最早的一次到达超过 2 年时，游戏会重新检查（`industry_workers.script.tl:40-43`）。所以工人不再来之后大约 2 年，加成会**自动停止**。

## 加成有多大

- 产量乘以产业的**加成系数**，窗口中显示为“+X %”（`industry_react_util.tl:716`）。
- 这个系数根据产业的随机种子只抽取一次：**在 ×1.5 和 ×2.5 之间**，之后对该产业永远不变（`industry_productivity_util.tl:58-72`）。没有种子的产业使用 ×2。
- 所以两座完全相同的矿场可能有不同的工人加成：选择服务哪一座之前，先看看“+X %”。

## 示例

一座有 20 个工作岗位、显示“+84 %”的煤矿。

| 情况 | 计入 | 有加成？ | 产量 |
|---|---|---|---|
| 新开公交线路：分配了 14 个居民，还没有人到达 | 0 | 否 | ×1 |
| 今年有 12 个不同的居民乘公交到达 | 12 | 是（≥ 10） | ×1.84 |
| 公交线路被删除；2 年内没有人到达 | 降到 0 | 停止 | ×1 |

## 把工人送到产业

```diagram workers_trip
```

- 工人要**到达产业本身**、行程目标（`targetOrAtEntity`）是该产业、且最后的出行方式是**线路**时才被计入（`industry_workers.script.tl:86-94`）。在站点下车还不够：这个人必须到达产业。
- 每个居民对每个目的地（住所、购物、工作）有一种出行方式。产业窗口列出分配的工人，并用图标显示这种方式：**步行**、**车**或**线路**（`entity_window_util.tl:1400-1435`）。对产业来说它应该总是线路，因为那里不允许步行和车（`industryutil.lua:451-457`）。
- 所以“不能步行”是指整个行程不能是步行或开车。并不是“完全不走路”：线路行程在站点和建筑之间仍要步行开始和结束（见下方引擎说明）。
- **换乘也算。** 脚本只看行程的方式，不看用了几条线路（`industry_workers.script.tl:91`）。来自四条线路之外城镇的工人和隔壁的工人计数相同，但可能要久得多才到达。
- **你的任何线路都能送他们**，包括运货的线路，只要车辆能载客、站点会装载乘客。脚本不检查车辆类型（`industry_workers.script.tl:86-118`）。玩家报告使用单独的客运线路问题更少。
- 有些产业（例如石油钻井）有自带站点，可接乘客和货物（`industryutil.lua:156-165`）。
- 产业窗口为每个分配的工人显示他是**目前在此处的**还是**在路上的**（`entity_window_util.tl:1371-1384`）。“加成”部分列出计入的工人及其 2 年中的**剩余时间**（`entity_window_util.tl:1579-1630`、`industry_eow.script.tl:644-649`）。
- 还没有工人的产业显示：“将此位置接入公共交通网，以使居民能够来这里工作。”（`entity_window_util.tl:1650-1652`）。
- **游戏内实测：先建一条简单线路。** 线路开通时游戏分配工作岗位，由引擎决定谁得到。两次测试中，从产业到单个城镇的第一条客运线路（城镇站点与你的其他客运站没有重叠的覆盖范围）把**全部 20 个岗位给了该城镇的居民**。加成分别在游戏时间 346 秒和 925 秒后开始，其中一次只有 1 辆车。另一次测试中，城镇站点碰到了网络中一座客运站的覆盖范围：部分岗位给了远处的城镇，最后的工人到达所需时间长得多（964 秒）。使用 [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) 和 [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 测得。

```engine
哪个站点服务产业、工人从站点到产业入口走多远、哪些城镇的居民得到这份工作，都由引擎决定（覆盖范围、寻路、工作选择）。脚本没有给工人设距离限制。玩家报告，一个货运覆盖范围包含产业的车站一直没带来工人，直到有公交开到产业入口（Steam 帖子“Problem getting workers to site”）。
```

## 运输工人补贴

- 只会为运出或接收货物、且尚未获得加成的产业提供（`deliver_workers.script.tl:121-131`、`industry_util.tl:541-553`）。
- 工人加成激活时完成：同样是 20 个中有 10 个不同的人乘你的线路到达（`deliver_workers.script.tl:152-156`）。不计其他东西；没有隐藏规则。
- 合同卡上的进度条是“计入的工人 ÷ 工作岗位的一半”（`deliver_workers.script.tl:267-272`、`industry_util.tl:11-18`）。
- 合同地图上的箭头来自**最近的 5 个城镇**。它们只是提示：脚本按距离画出，而不是按谁有这份工作（`deliver_workers.script.tl:297-317`）。
- 金额和期限见[补贴：报价、期限与奖励](subsidies.html)。

## 为什么我的工人不来？

| 检查 | 在哪看 | 原因 |
|---|---|---|
| 有人得到这份工作吗？ | 工作岗位条（“12/20”） | 没有分配的工人就没人出行。工作选择在引擎一侧。 |
| 工人的出行方式图标 | 工人列表：步行 / 车 / 线路 | 只有线路行程才能计入（`industry_workers.script.tl:91`）。 |
| 他们在移动吗？ | **在路上的** / **目前在此处的** | 长时间“在路上的”：换乘慢或拥挤，或从最后一站没有路径。 |
| 最后一站能到达产业入口吗？ | 站点覆盖范围、入口道路 | 玩家报告；在引擎一侧。一条到入口的短公交线有帮助。 |
| 站点装载乘客吗？ | 线路站点、货物过滤器 | 行程两端都必须装卸乘客。 |
| 2 年内 10 个**不同**的人？ | “加成”部分、**剩余时间** | 同一个人只计一次；较早的到达会被移出（`industry_workers.script.tl:56-70`）。 |
| 超过 40 个工作岗位（模组）？ | 工作岗位条 | 只保留 20 次到达，永远达不到一半。 |

## 须知

- 最多保留 20 次到达，再加上 50 % 的规则，意味着**超过 40 个工作岗位**的产业（模组可以做到）永远无法通过工人获得加成。
- **运输工人**补贴在这个加成激活时完成（`deliver_workers.script.tl:152-156`）。
- 加成货物（肥料、机器、工具）是原料产业的**另一种**加成，本页不涉及。
- [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) 模组会在产业窗口中显示分配的工人和加成工人来自哪些城镇，并在地图上用箭头标出。

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: “Sufficient”（足够）= 工作岗位的一半（20 个中的 10 个）；“recently”（最近）= 最近 2 个游戏年、最近 20 次到达、每人一次、仅限你的线路；加成系数每个产业 ×1.5 到 ×2.5。换乘也算；出行方式必须是线路，从站点步行是这种行程的一部分。
result: refines
```
