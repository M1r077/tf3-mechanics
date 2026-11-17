---
title: 成就
summary: 游戏脚本对每个自由游戏成就检查什么、何时检查，哪些成就只计入基础游戏的载具、货物和动物，以及哪些检查交给引擎。
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-17
game: 40425
fact: 17 | 由游戏脚本自己解锁的成就
fact: 500 m | 高峰停靠中列车停站时第一节车厢的高度
fact: < 1 % | 不是我的错所需的城镇声誉
fact: 10 | 集中建设中最近城镇必须相同的地标数
---

官方 wiki 列出了 41 个成就。游戏脚本 `achievements.script.tl` 自己解锁其中 **17** 个，并为 **9 个跨游戏计数器**提供数据；其余的（战役、天气、城镇规模、仓库、利息、增益、汽车、1900-2000、2000 年代的蒸汽）在别处由引擎或平台检查。每次检查都先询问引擎该成就是否仍可解锁；模组或设置是否阻止它由引擎决定（`achievements.script.tl:632`，`achievements.script.tl:510`）。

## 脚本检查的成就

| 成就 | 脚本检查什么 | 来源 |
|---|---|---|
| **包裹到达** | 一件货物送达目的地 | `achievements.script.tl:221-225`，`achievements.script.tl:632-636` |
| **以谁之名** | 完成一项补贴 | `achievements.script.tl:241-244`，`achievements.script.tl:638-642` |
| **补贴风潮** | 连续完成 10 项补贴，中间没有失败；补贴失败会把计数重置为 0 | `achievements.script.tl:243-249`，`achievements.script.tl:644-648` |
| **守护者** | 城镇的送货评价变为**极佳** | `achievements.script.tl:270-276`，`towns.script.tl:30-33`，`achievements.script.tl:650-654` |
| **城市发展** | 城镇升级 | `achievements.script.tl:253-255`，`town_growth.script.tl:92` |
| **增加需求** | 城镇产生新的货物类型需求 | `achievements.script.tl:257-259`，`achievements.script.tl:668-672` |
| **不是我的错** | 城镇的声誉**下降**到 **1 %** 以下 | `achievements.script.tl:261-267`，`towns.script.tl:36-39` |
| **升值** | 公司提升一个等级 | `achievements.script.tl:280-282`，`achievements.script.tl:680-684` |
| **职业阶梯** | 公司达到最高等级 | `achievements.script.tl:284-290`，`achievements.script.tl:686-690` |
| **园艺师** | 在一次建造中只放置树木（没有移除任何东西，也不是通过植树造林） | `achievements.script.tl:346-377` |
| **完美主义者** | 同一座车站按顺序被拆除、重建、拆除、重建，中间没有建造或移除其他车站 | `achievements.script.tl:304-341`，`achievements.script.tl:694-710` |
| **集中建设** | 恰好 10 座已完工地标的最近城镇相同 | `achievements.script.tl:382-395`，`achievements.script.tl:713-721` |
| **高峰停靠** | 你的某列列车到站时第一节车厢高于 **500 m** | `achievements.script.tl:407-417`，`achievements.script.tl:723-727` |
| **离岸** | 你的某架直升机到达石油平台的站点 | `achievements.script.tl:420-450`，`achievements.script.tl:729-733` |
| **传承舰队** | 基础游戏的每种船舶型号同时在你的船舶线路上运行 | `achievements.script.tl:735-776` |
| **第三类接触** | 你点击一个 UFO | `achievements.script.tl:793-806` |
| **守时者** | 你手动更改一天中的时间 | `achievements.script.tl:839-844` |

- **完美主义者**只计算增加或移除一整座车站的建造：给车站增加站台或模块不算（`achievements.script.tl:301-302`）。
- **集中建设**在每座地标完工时计数，算入当时离它最近的城镇（`achievements.script.tl:386`）。
- **传承舰队**只在一种从未停过站的船舶型号到站时检查；它看的是你船舶线路上的载具，而不是车库里的船（`achievements.script.tl:736`，`achievements.script.tl:750-766`）。
- **不是我的错**需要的是声誉，而不是其他评价：见[城镇声誉](reputation.html)。

```tip scripts
高峰停靠检查的是列车停下时第一节车厢的高度，而不是站房的高度。把车站建在 500 m 以上的山上，并让一列列车开到那里。
```

## 跨游戏计数器

这些计数会在各局游戏之间延续（由平台保存）。脚本只发送自上次检查以来的变化。

| 计数器 | 成就 | 计入什么 | 来源 |
|---|---|---|---|
| 轨道长度 | **环球建造者** | 日志总长度（km）的增长；移除时不会扣除 | `achievements.script.tl:511-523` |
| 人口 | **全球人口** | 地图人口相对于载入游戏时人口的增长 | `achievements.script.tl:512`，`achievements.script.tl:525-533` |
| 乘客 | **客运先锋** | 在你的线路上完成行程的乘客 | `achievements.script.tl:236-238`，`achievements.script.tl:535-541` |
| 货物 | **货运先锋** | 送达的货物 | `achievements.script.tl:543-549` |
| 气候 | **大亨中的大亨** | 公司在该地图达到最高等级时的地图气候 | `achievements.script.tl:551-567` |
| 收入 | **邪恶财富** | 你的收入累计，以十亿计 | `achievements.script.tl:202-204`，`achievements.script.tl:569-590` |
| 货物类型 | **销售大师** | 基础游戏的每种货物类型各送达一次 | `achievements.script.tl:20-22`，`achievements.script.tl:230-232`，`achievements.script.tl:592-607` |
| 载具 | **鉴赏家** | 基础游戏的每种载具型号各到站一次 | `achievements.script.tl:16-18`，`achievements.script.tl:469-481`，`achievements.script.tl:609-625` |
| 动物 | **动物爱好者** | 基础游戏的每种动物各点击一次 | `achievements.script.tl:24-26`，`achievements.script.tl:809-834` |

- 模组中的载具、货物和动物永远不计入这些计数器：只采用基础游戏的文件（`::/vehicle`，`::/cargos`，`::/animal`）（`achievements.script.tl:16-26`）。
- 对于鉴赏家，载具必须**到达线路的站点**；只购买是不够的。

```engine
成就是否仍可解锁（isAchievementUnlockable）、计数器是否被关闭（areStatsDisabled）、各计数器的目标，以及脚本中没有的 24 个成就，都由引擎和平台处理。官方 wiki 称，使用非外观类模组或游戏设置偏离标准值时，通常无法获得成就。
```

## 小贴士

- 每个“首次”成就都与上一次检查相比较：需要在该成就仍未解锁的游戏中发生**新的**事件，存档中旧的补贴或等级不会再次计入（`achievements.script.tl:633`，`achievements.script.tl:779`）。
- 你的等级、补贴和声誉分别在[公司等级、特权与总部](company.html)、[补贴](subsidies.html)和[城镇声誉](reputation.html)中说明。

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: 脚本中有 17 个成就和 9 个计数器。它细化了官方说明：守护者指送货评价达到极佳，不是我的错指声誉低于 1 %，高峰停靠指第一节车厢高于 500 m，完美主义者指同一车站拆除-重建-拆除-重建，传承舰队指基础游戏的所有船舶型号同时在线路上。计数器只计入基础游戏的载具、货物和动物。
result: refines
```
