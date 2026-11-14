---
title: 工人与工人加成
summary: 居民如何在产业找到工作，哪些工人计入加成，以及加成有多大。
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-14
fact: 10 / 20 | 触发加成所需的工人
fact: 2 年 | 一次到达的计入时长
fact: ×1.5–2.5 | 加成系数，每个产业固定
---

每个产业都提供工作岗位。当足够多的工人**乘坐你的客运线路到达**时，产业的产量就会提高。产业窗口显示两个不同的数字，把它们混为一谈是最常见的误解。

```diagram workers_flow
```

## 谁能在产业工作

- 每个基础游戏产业都有 **20 个工作岗位**（每个产业的 .con.lua 中 `industrialCapacity = 20`）。
- 这些工作岗位的设置让居民**无法步行或开车**前往：只有你的线路能把他们送到（`industryutil.lua:451-457`，`disallowedMoveModes = {"WALK", "DRIVE"}`）。
- 每个居民都有住所、购物地点和工作地点。游戏从该居民能到达的地点中挑选工作地点；产业的目的地权重为 2.0（`industryutil.lua:455`）。

```engine
居民如何在所有能到达的地点中挑选一个工作地点（出行时间、费用、2.0 的权重）由引擎计算。脚本只提供输入数据。
```

## 分配的工人

指工作地点是这个产业的居民。产业窗口中的工作岗位条，以及产业统计中的 **工作场所** 一栏（“12/20”）显示的就是这个数字（`entity_window_util.tl:1238`，`statistic_industries.tl:305`）。仅有分配的工人**不会**带来任何加成：他们必须真正前往产业。

## 计入加成的工人

一个小型游戏脚本 `industry_workers.script.tl` 会记录每一次到达：

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

## 须知

- 最多保留 20 次到达，再加上 50 % 的规则，意味着**超过 40 个工作岗位**的产业（模组可以做到）永远无法通过工人获得加成。
- 补贴“运输工人”在这个加成激活时完成（官方 wiki，补贴）。
- 加成货物（肥料、机器、工具）是原料产业的**另一种**加成，本页不涉及。
- [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) 模组会在产业窗口中显示分配的工人和加成工人来自哪些城镇，并在地图上用箭头标出。

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: “Sufficient”（足够）= 工作岗位的一半（20 个中的 10 个）；“recently”（最近）= 最近 2 个游戏年、最近 20 次到达、每人一次、仅限你的线路；加成系数每个产业 ×1.5 到 ×2.5。
result: refines
```
