---
title: 通知与警告
summary: 每条警告何时出现、何时消失：被卡住的载具、无法使用或拥挤的车站、线路和站点问题、城镇评价、载具状况、即将关闭的工业，以及哪些警告默认不记入日志。
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40444
fact: 5 分钟 | 载具静止多久游戏时间后被报告为卡住
fact: 20 % | 触发警告的状况，直到载具回到 30 % 以上
fact: 11 | 新游戏中关闭的通知类型
fact: 75 天 | 两次检查无道路连接车站的间隔
---

大多数警告是**持续性**的：游戏脚本会反复检查情况，问题存在时警告一直保留，问题解决后自行结束。检查轮流分摊在 4 次更新中，因此警告出现或消失可能需要一点时间（`notifications.script.tl:13`，`notifications.script.tl:49`）。

## 每条警告何时出现

| 警告 | 出现条件 | 消失条件 | 来源 |
|---|---|---|---|
| **车辆被卡住** | 你的某辆载具正在行驶途中，不是被你停下的，且已有游戏时间 **5 分钟**速度为 0 | 它重新移动 | `notifications.script.tl:557-580` |
| **车站无法运行** | 车站没有任何站台上下乘客，且覆盖范围内**什么都没有**（没有仓库、工业或城镇建筑），同时你的某条线路停靠该站 | 有东西进入覆盖范围 | `notifications.script.tl:602-617`，`notifications.script.tl:630-647`，`station_useless.script.tl:39` |
| **站点拥挤** | 车站等候的乘客或货物超过容量（溢出），同时你的某条线路停靠该站；乘客会离开 | 溢出结束 | `notifications.script.tl:599`，`notifications.script.tl:649-661`，`overcrowding.script.tl:23` |
| **载具状况** | 你的某辆载具状况为 **20 %** 或更低 | 回到 **30 %** 以上 | `notifications.script.tl:310-318` |
| **城镇评分非常低** | 城镇的某项评价降到非常贫穷（低于 1/6） | 评价回到中等或更好 | `notifications.script.tl:230-238`，`town_util.tl:763-769`，`town_util.tl:983-985` |
| **城镇评价下降中** | 某项评价为贫穷或中等（低于 50 %），且不在非常贫穷警告中 | 评价为好或更好 | `notifications.script.tl:240-248` |
| **工业关闭** | 某个工业开始关闭倒计时 | 它关闭，或及时重新被使用 | `notifications.script.tl:439-451`，`industry_close.script.tl:53-59` |
| **无道路连接** | 车站未连接道路；每 **75 天**检查一次 | 下一次检查发现道路 | `notifications.script.tl:16`，`notifications.script.tl:423-436` |
| **卸货问题** | 载具的货物在其线路上从未被卸下 | 货物被卸下 | `notifications.script.tl:277-290`，`cargo_rtc_warning.script.tl:28-37` |

- **在车库中**的载具永远不算卡住：脚本中关闭了这项检查（`notifications.script.tl:563-564`）。被你停下的载具也不算。
- 车站无法运行的检查只看覆盖范围。已经有乘客在站台上下车的车站永远不会被报告（`notifications.script.tl:606-610`）。
- 如何提高城镇评价：见[城镇增长](towns.html)和[声誉](reputation.html)。关闭倒计时如何运作以及如何阻止：见[工业](industries.html)。状况对载具的影响：见[成本、维护费与贷款](costs.html)。

```engine
车站是否溢出、载具是否有路径、线路能否到达其车站、两座城镇之间的行程最多可以多长，都由引擎判断（calculateStationGroupCargo、getVehicleProblems、getLineProblems、getTownProblems）。脚本只是把它的结果变成警告。
```

```tip scripts
车辆被卡住、载具问题、载具状况、站点拥挤和车站无法使用在新游戏的日志中是关闭的。在通知设置中打开它们：这些警告会告诉你堵塞、缺少路径或车队老化。
```

## 线路、站点和载具问题

这些直接来自引擎对你的线路和载具的检查；脚本为每一种加上标题。

| 警告 | 情况 | 来源 |
|---|---|---|
| **线路问题** | 车站太少；同一车站连续出现两次；车站之间互不兼容；车站无法连接；备选站台无法连接 | `line_warning.script.tl:46-128` |
| **线路配置错误** | 某种货物在任何地方都无法装载，或在任何地方都无法卸载；没有载具能运载设定装载的货物；载具不运载任何已配置的货物，或客运线路上有纯货运载具；完全没有配置货物 | `line_warning.script.tl:15-36`，`line_warning.script.tl:133` |
| **车站问题** | 当前载具无法使用的站点；客运站点被货运载具使用（部分或全部）；货运站点被客运载具使用；某种已配置的货物在该站点无法装载或卸载 | `line_station_warning.script.tl:6-87` |
| **载具问题** | 没有电气化路径；没有大型飞机的航线；没有大型船舶的航线；完全没有路径；两列火车互相阻挡 | `vehicle_warning.script.tl:6-58` |
| **城镇未连接** | 两座城镇之间的道路中断；两座城镇之间的行程耗时过长 | `town_warning.script.tl:7-19` |

- “没有大型飞机的航线”和“没有大型船舶的航线”表示载具对其线路上的跑道、码头或水道来说太大：见[飞机](aircraft.html)和[船舶](ships.html)。

## 日志、弹窗和设置

- 每种警告类型都可以在通知设置（“配置通知日志”）中关闭。被关闭的类型不弹窗，也不保留在日志中（`notification_util.tl:145-146`，`notification_log.tl:480`）。
- 在**新游戏**中，有 11 种类型一开始就是关闭的：**车辆被卡住**、**载具问题**、**载具状况**、**站点拥挤**、**车站无法使用**、**站点未连接**、**城镇未连接**、**货物未卸下**，以及公司的勘探、营销活动和产业绿化进度消息（`stuck_vehicle.res.lua:7`，`vehicle_warning.res.lua:8`，`noroadconnection.res.lua:8`，`vehiclecondition.res.lua:8`，`overcrowding.res.lua:8`，`station_useless.res.lua:7`，`town_warning.res.lua:8`，`cargo_rtc_warning.res.lua:8`，`notification_util.tl:32-39`）。
- 一次性消息（新载具、新建筑、升级、补贴）在游戏时间 **60 秒**后隐藏弹窗；它们仍保留在历史记录中（`notification_util.tl:10`，`notifications.script.tl:85-94`）。
- 当通知所指的一切都被拆除或重建时，通知也会结束（`notifications.script.tl:95-107`）。
- 在任务中，通知一开始是暂停的，直到任务将其打开（`notifications.script.tl:700-704`）。

## 小贴士

- 5 分钟后的卡住警告不会说明原因。查看载具：红色信号、方向错误的单向信号，或同一载具的载具问题警告。
- “车站无法运行”只表示“覆盖范围内还没有任何东西”。把车站移近房屋、工业或仓库，或者扩大车站。
- 拥挤的车站会流失乘客：增加载具，或缩短间隔（见[发车与等待](departure.html)）。

```check
official: The official wiki's User Interface page describes the notification button, the log and its filters, without the conditions of each warning. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: 上述条件：行驶途中速度为 0 达 5 分钟即为卡住，载具状况 20 % 起直到 30 %，城镇评价非常贫穷低于 1/6，道路连接每 75 天检查一次，默认关闭 11 种类型。
result: adds
```
