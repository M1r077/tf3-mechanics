---
title: 发车设置：满载、填充水平与停靠时间
summary: 载具何时离开站点：三种发车模式、每种货物的填充水平，以及最小、最大和额外停靠时间。
domain: stations
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-15
fact: 600 s | 新站点的默认最大停靠时间
fact: 30 s / 60 s | 默认最大额外等待时间，公路 / 铁路
fact: 0–100 % | 填充水平，按货物计，占载具容量的比例
---

线路的每个站点都有自己的发车设置，位于该站点的“货物过滤器”窗口中（在线路窗口中点击站点）。它们决定载具在那里装**多少**货，以及可以等**多久**。

## 设置

| 设置 | 取值 | 新站点 | 来源 |
|---|---|---|---|
| “在可行的情况下装载”“满载（任何）”“满载（全部）” | 三选一 | 在可行的情况下装载（实测） | `cargofilter_window.tl:798-821` |
| “最小停靠时间” | 0–600 s，步长 10 | 0 s（实测） | `cargofilter_window.tl:841-845` |
| “最大停靠时间” | 0–600 s，或“---”（无限制，滑块在最右端） | **600 s**（实测） | `cargofilter_window.tl:855-863` |
| “最大额外等待时间” | 0–600 s，步长 10 | 60 s；没有铁路的公路或有轨电车站为 30 s | `cargofilter_window.tl:827-831`, `line_util.tl:478-490` |
| “填充水平”，按每种装载的货物 | 0–100 %，步长 1 | 100 % | `cargofilter_window.tl:698-704`, `line_util.tl:511` |

- 点击时间会打开一个数字输入框：大于 600 s 的值可以在那里输入（`cargofilter_window.tl:204-208`）。
- 三个时间会保持彼此的顺序：把最小时间或额外等待时间调到高于最大时间，最大时间也会随之提高（`cargofilter_window.tl:834-835`, `cargofilter_window.tl:848-849`, `cargofilter_window.tl:865-869`）。
- 修改其中任何一项都会把线路标记为自定义：自动配置不再改动它的载重列表（`cargofilter_window.tl:438`，见[装载与卸载速度](loading.html)）。自动配置本身从不改变模式或时间（`line_util.tl:495-513`）。

## 填充水平：每种货物的上限

填充水平是载具在本站最多装载该货物的数量，以载具容量的比例表示，四舍五入到最接近的单位（游戏内实测）。

| 载具 | 填充水平 | 离开时载有 |
|---|---|---|
| 卡车，容量 15，木材 | 50 % | **8**（7.5 向上取整） |
| 卡车，容量 22，纤维 | 70 % | 每次 **15**（15.4） |
| 列车，容量 18，玻璃 | 48 % | 最多 **9**（8.64） |
| 有轨电车，容量 28，燃料 | 66 % | 最多 **18**（18.48） |

- 车上已有的货物也计算在内：一辆载着 14 燃料到达的有轨电车离开时载有 18，而不是 14 + 18。
- 超过上限时，不会因此装货，**也不会因此卸货**：一辆载着 22 肥料到达的卡车（上限 11）离开时仍载有 22。
- **0 %** 表示：不在本站装载这种货物。
- 在满载模式下，达到上限就算满：填充水平为 50 % 的木材卡车等了约 270 s，离开时载有 15 中的 8，而不是 15。
- 没有卸货百分比。卸货由载重列表和“到达时强制卸下所有货品”决定（[装载与卸载速度](loading.html)）。

## 满载与停靠时间

- **在可行的情况下装载**：载具装上现有的货物就离开。
- **满载（全部）**：载具一直等到装满。木材卡车等了 460–566 s，离开时载有 15 中的 15。
- **满载（任何）**：一种货物装满时载具就离开。一列木材和厚木板列车在 369–380 s 后载着 143 和 144 木材离开；另外两次约 30 s 后载着 57 和 118 木材的发车无法解释。
- **最大停靠时间**会结束等待，即使什么都没装上。一列满载（全部）、最大 120 s 的蔬菜列车，要么约 25 s 内装满（64 中的 64），要么在 116–120 s 后载着 26 或 **0** 离开。使用默认的 600 s 时，它在 596–600 s 后载着 64 中的 26 离开。
- **最小停靠时间**是整个停靠时间，包括装货，而不是装货之后额外的时间：设为 60 s 时，玻璃列车每次都停靠 55–61 s，无论装了多少。
- **最大额外等待时间**：“Maximum wait time after loading to improve vehicle distribution”（`cargofilter_window.tl:827`）。等待期间载具窗口显示“确保安全距离”（`entity_window_util.tl:2279-2286`）。
- **同一站点的多辆载具同时装货**，无论各自何时到达（游戏内观察）。两辆相隔约 90 s 到达的木材卡车在同一秒离开，各载 8。货物如何在它们之间分配未作测量。

```engine
脚本只保存设置；载具何时离开由引擎决定。
```

上面的规则是用 [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 数据库测量的（每 2 s 一次快照，所以停靠时间为 ±2 s），2026 年 11 月。

## 须知

- 在货物到达很少的站点用满载长时间等待会堵住站台：线路的其他载具会在它后面排队。
- 满载搭配较短的最大停靠时间，可能让载具在新货物到达之前返回时空车离开。
- 有一次，一列满载（全部）、最大 600 s 的列车停靠了 783–992 s。原因没有找到。

```check
official: "Full load (any): The vehicle will stop and wait until one cargo type is fully loaded. Full load (all): The vehicle will stop and wait until it is fully loaded." "In the vanilla game "all" and "any" only applies to trains and ships […] Any other vehicle type will wait for full load in both cases." Each cargo is loaded "to what percentage of a vehicle's total capacity". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles#departure_configuration))
scripts: 三种发车模式，最小 / 最大停靠时间 0–600 s（或无限制），最大额外等待时间 0–600 s（60 s，公路 30 s），每种货物的填充水平 0–100 %；实测：填充水平限制车上的货物，四舍五入到最接近的单位，并在满载时算作装满；最大停靠时间会结束满载，即使空车；最小停靠时间包括装货；同一站点的载具一起装货。
result: refines
```
