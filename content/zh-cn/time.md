---
title: 游戏时间与日历
summary: 游戏速度和日历速度是两回事。一天和一年有多长，放慢或暂停日历会改变什么，又不会改变什么。
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
game: 40425
fact: 4 s | 日历速度 ×1、游戏速度 1x 时的一个日历日
fact: ≈ 24 min | 相同速度下的一个日历年
fact: 0 ×0.25 ×0.5 ×1 ×2 ×4 | 日历速度档位
fact: 0 1x 2x 4x | 游戏速度档位
---

游戏有**两个时钟**。**游戏速度**（暂停、1x、2x、4x）让一切都跑得更快：载具、生产、城镇。**日历速度**只决定日期走得多快。游戏中几乎所有规则都按游戏时间计算，而不是按日历天数。

## 两个设置

| 设置 | 档位 | 改变什么 | 来源 |
|---|---|---|---|
| **游戏速度** | 暂停、1x、2x、4x | 整个模拟运行的速度 | `game_bar_widgets.tl:199-203` |
| **日历速度** | 已暂停、×0.25、×0.5、×1、×2、×4 | 一天相当于多少秒游戏时间 | `game_bar_widgets.tl:321-335`，`game_bar_widgets.tl:351` |

- 日历速度 ×1 时，一天是 **4 秒**游戏时间（官方 wiki），所以在 1x 下一个月约 2 分钟，一年约 **24 分钟**。用 [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 实测：×1 时每天 4.0 秒，×4 时 1 秒，×0.5 时 8 秒，×0.25 时 16 秒。
- ×4 让日期走快四倍；**已暂停**让日期停下，模拟继续运行。
- 2x 和 4x 是上限：电脑跟不上时，游戏会降低它们（`game.tl:636-642`）。实测：2x 平均为 1.9x，4x 平均为 3.6x。
- **每日时间**和天气是第三个、只影响画面的时钟：默认情况下它们自己变化，与日历无关（`game_time_config.res.lua:5`，`weather_config.res.lua:5`）。

## 不论日历如何，都按游戏时间走的东西

这些按游戏时间计算，所以放慢或暂停日历不会让它们变慢：

- **生产**：产业的生产时间是标准一年的固定比例（`industry_react_util.tl:51`）。产业窗口按当前日历的天数显示它（`industry_react_util.tl:23`）：在 ×0.25 下，同样的速率显示的天数只有四分之一。
- **贷款还款**：每个标准月的游戏时间还一次，日历暂停时也一样（`loan.script.tl:83-88`）。
- **补贴期限**和奖励持续时间，5 个标准年（`subvention_util.tl:286`，`subvention_util.tl:290-292`）。
- **城镇声望恢复**（`towns.script.tl:121-130`）、最多按 2 个标准年计算的**工人效果**（`industry_productivity_util.tl:3`），以及多年无人服务后的**产业关闭**（`industries.script.tl:119-128`）。
- 城镇最近半年的**送货评价**（`town_util.tl:840`）。
- **新产业**：日历暂停时，1809 秒游戏时间内出现了 3 个，间隔 760 秒和 728 秒，与日历运行时的节奏相同（约 730 秒）。用 [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 测得；见 [产业](industries.html)。

日历运行时，游戏按当前日历速度的年、月、日显示这些时长（`util.tl:40-49`）。

## 按日历日期走的东西

- **新载具、车站和建筑**按年份出现（官方 wiki："Different calendar speeds only affect the availability of vehicles and infrastructure"）。
- **随年份增长的费用**：建筑维护费、时代版本、补贴金额和贷款金额都跟随日期。详见：[成本、维护费与贷款](costs.html)。

## 日历暂停时

1. 日期也就是年份保持不变：没有新载具，按年份的费用也不变。
2. 时长以**分和秒**显示，而不是天（`util.tl:41-43`，`industry_react_util.tl:16-21`）。
3. 贷款按**每分钟**而不是每年显示还款（`finances_loan_gui.tl:223-231`），自定义贷款卡无法借取（`finances_loan_gui.tl:393`）。
4. 生产、还款、期限和声望保持游戏时间的节奏。

## 须知

- 想在新载具出现前有更多时间发展网络？降低日历速度：你每游戏分钟的收入不会变。
- 显示为“每年”的生产取决于日历速度；比较产业时要用相同的速度。
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 在日历暂停时也能保持易读的财务图表。

```engine
标准日、月、年的长度（getDefaultDayDuration 等）来自引擎。城镇脚本把一个月算作 30 × 4 秒（`towns.script.tl:121`），这与实测的每天 4 秒相符；另外几个常量仍假定一天为 2 秒（`cargotype.script.lua:3`，`mod.script.tl:172`）。
```

```check
official: "By default a day in the game lasts 4 seconds." "Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent." ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: 日历速度相对标准日为 ×0.25 到 ×4 或暂停；生产、贷款、补贴、声望和工人计时按游戏时间运行；日历暂停时，时长以分钟显示，还款按每分钟显示，并且不能借新贷款；实测：×1 时每天 4 秒。
result: refines
```
