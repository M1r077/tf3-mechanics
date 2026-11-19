---
title: 街道、轨道、桥梁和信号灯
summary: 每种轨道和街道的速度、价格和维护费，桥梁、隧道、道口和信号灯的花费与作用，林荫道和隔音屏障到底改变了什么，以及车库在哪里讲解。
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40444
fact: 100 / 160 / 350 km/h | 简易轨道、标准铁轨和高速铁轨
fact: ×9 | 高速铁轨相对简易轨道的价格和维护费
fact: +30 % | 给轨道加接触网的价格
fact: -65 % | 装了隔音屏障的街道或轨道的噪音
---

每种街道和轨道都有最高速度、每米价格和每米每年的维护费，都写在它的文件里。桥梁、道口和一些街道装饰会附加自己的限速。下面的费用是 **基础设施成本** 和 **基础设施维护** 为 100 % 时的数值（见 [成本、维护费和贷款](costs.html)）。

## 轨道

| 轨道 | 出现时间 | 最高速度 | 每公里建造费 | 每公里每年维护费 | 来源 |
|---|---|---|---|---|---|
| 简易轨道 | 开局 | 100 km/h | 6 万 | 1 万 | `simple.street_template.lua:9`，`simple.street_template.lua:28`，`simple.street_template.lua:33` |
| 标准铁轨 | 1930 | 160 km/h | 18 万 | 3 万 | `standard.street_template.lua:4`，`standard.street_template.lua:11`，`standard.street_template.lua:30`，`standard.street_template.lua:35` |
| 高速铁轨 | 1980 | 350 km/h | 54 万 | 9 万 | `high_speed.street_template.lua:4`，`high_speed.street_template.lua:11`，`high_speed.street_template.lua:30`，`high_speed.street_template.lua:35` |

- **接触网** 比轨道贵 **30 %**（`mod.script.tl:24-25`）。简易轨道从 1921 年起可用，更新的类型从出现起就可用（`simple_catenary.street_template.lua:4`）。文件里它每年没有额外费用：电气化版本的维护费相同（`simple_catenary.street_template.lua:34`）。
- 三种轨道的坡度和弯道条件相同：建造时 **8.5 %**（**坡度** 滑块的上限），轨道形状最多 13 %，弯道半径建造时 55 m，最小 40 m（`standard.street_template.lua:36-37`，`standard.street_template.lua:48-49`，`construction_react_util.tl:241-242`，`construction_react_util.tl:1824`）。
- 轨道本身的污染随类型增加：2、4、6（`simple.street_template.lua:18`，`standard.street_template.lua:20`，`high_speed.street_template.lua:20`）。

```engine
弯道使列车减速多少（每种轨道的 speedCoeffs），以及建造工具为弯道显示的速度，都由引擎计算。
```

```tip scripts
高速铁轨的建造费和每年的维护费都是简易轨道的 9 倍。只在列车真正跑得比 160 km/h 快的地方铺设；其他地方用标准铁轨就够了，慢速货运支线用简易轨道即可。
```

## 街道

| 街道 | 年份 | 最高速度 | 每公里建造费 | 每公里每年维护费 | 来源 |
|---|---|---|---|---|---|
| 窄街（旧） | 1940 年以前 | 20 km/h | 3.6 万 | 6,000 | `town_old_xsmall.street_template.lua:4-5`，`town_old_xsmall.street_template.lua:8`，`town_old_xsmall.street_template.lua:27`，`town_old_xsmall.street_template.lua:56` |
| 小型街道（旧） | 1940 年以前 | 40 km/h | 6 万 | 1 万 | `town_old_small.street_template.lua:8`，`town_old_small.street_template.lua:27`，`town_old_small.street_template.lua:56` |
| 大型街道（旧） | 1940 年以前 | 60 km/h | 18 万 | 3 万 | `town_old_large.street_template.lua:8`，`town_old_large.street_template.lua:27`，`town_old_large.street_template.lua:88` |
| 窄街（新） | 1940 年起 | 30 km/h | 12 万 | 2 万 | `town_new_xsmall.street_template.lua:4`，`town_new_xsmall.street_template.lua:11`，`town_new_xsmall.street_template.lua:30`，`town_new_xsmall.street_template.lua:59` |
| 小型街道（新） | 1940 年起 | 50 km/h | 18 万 | 3 万 | `town_new_small.street_template.lua:11`，`town_new_small.street_template.lua:30`，`town_new_small.street_template.lua:59` |
| 中型街道（新） | 1940 年起 | 50 km/h | 36 万 | 6 万 | `town_new_medium.street_template.lua:11`，`town_new_medium.street_template.lua:30`，`town_new_medium.street_template.lua:75` |
| 大型街道（新） | 1940 年起 | 60 km/h | 54 万 | 9 万 | `town_new_large.street_template.lua:11`，`town_new_large.street_template.lua:30`，`town_new_large.street_template.lua:91` |
| 小型乡村公路（旧） | 1940 年以前 | 60 km/h | 6 万 | 1 万 | `country_old_small.street_template.lua:8`，`country_old_small.street_template.lua:29`，`country_old_small.street_template.lua:58` |
| 小型乡村公路（新） | 1940 年起 | 80 km/h | 18 万 | 3 万 | `country_new_small.street_template.lua:10`，`country_new_small.street_template.lua:31`，`country_new_small.street_template.lua:60` |
| 单车道高速公路 | 1940 年起 | 100 km/h | 18 万 | 3 万 | `highway_new_small.street_template.lua:10`，`highway_new_small.street_template.lua:32`，`highway_new_small.street_template.lua:53` |
| 两车道高速公路 | 1940 年起 | 120 km/h | 36 万 | 6 万 | `highway_new_medium.street_template.lua:10`，`highway_new_medium.street_template.lua:32`，`highway_new_medium.street_template.lua:61` |
| 三车道高速公路 | 1940 年起 | 120 km/h | 54 万 | 9 万 | `highway_new_large.street_template.lua:10`，`highway_new_large.street_template.lua:32`，`highway_new_large.street_template.lua:69` |
| 有轨电车轨道（旧） | 1910 年以前 | 40 km/h | 3.6 万 | 6,000 | `tram_old.street_template.lua:4-5`，`tram_old.street_template.lua:8`，`tram_old.street_template.lua:27`，`tram_old.street_template.lua:40` |
| 有轨电车轨道（新） | 1925 年起 | 100 km/h | 12 万 | 2 万 | `tram_new.street_template.lua:4`，`tram_new.street_template.lua:9`，`tram_new.street_template.lua:29`，`tram_new.street_template.lua:42` |

- **1940 年的更替** 让城镇街道快 10 km/h，但建造和每年维护都贵 **三倍**：小型街道从每公里 6 万变成 18 万。
- 乡村公路的中型和大型版本速度相同，花费是小型的 2 倍和 3 倍（`country_new_large.street_template.lua:10`，`country_new_large.street_template.lua:31`）。
- 给街道添加：**公交专用道** +10 %，**有轨电车轨道** +20 %，**电气化有轨电车轨道** +40 % 的街道价格（`mod.script.tl:24-28`）。
- 玩家通常不拥有街道，即使是玩家自己建的；街道工具可以改变街道的所有者（官方 wiki）。街道的维护费由谁支付由引擎决定。

## 林荫道和隔音屏障

| 工具 | 噪音 | 污染 | 最高速度 | 位置 | 来源 |
|---|---|---|---|---|---|
| 林荫道工具（树木） | -10 % | -50 % | **-25 %** | 有人行道的街道，不能在桥上或隧道里 | `alley.edge.lua:39-40`，`alley.edge.lua:53-56` |
| 防噪音隔离栏工具 | -65 % | 不变 | 不变 | 街道和轨道，不能在隧道里 | `barrier_b.edge.lua:43`，`barrier_b.edge.lua:47`，`barrier_track_b.edge.lua:43` |

- 两者在文件里都是 100、每年 10，和街道每米的写法一样（`alley.edge.lua:8`，`alley.edge.lua:12`，`barrier_b.edge.lua:7`，`barrier_b.edge.lua:11`）。
- 建造菜单里“带树木”和“带屏障”的街道，就是已经装好这些装饰的同一种街道（`town_new_medium_trees.street_template.lua:12-14`）。建造菜单会把它们的效果加起来（`construction_react_util.tl:2119-2142`）。
- 所以带树木的街道 **慢四分之一**：带树木的新中型街道只能跑约 38 km/h，而不是 50。

```tip scripts
对付噪音，用隔音屏障：-65 %，而且不损失速度。树木是对付污染的工具（-50 %），但会让街道慢四分之一。
```

城镇如何评价噪音和污染：[污染和噪音](emission.html)。

## 桥梁和隧道

| 桥梁 | 年份 | 最高速度 | 用于 | 基础价格 | 来源 |
|---|---|---|---|---|---|
| 石桥 | 开局起 | 90 km/h | 轨道、街道 | 200 | `stone.bridge.lua:169-170`，`stone.bridge.lua:181-183`，`stone.bridge.lua:193` |
| 栈桥 | 1970 年以前 | 60 km/h | 轨道用和街道用各一种 | 100 | `trestle.bridge.lua:200-201`，`trestle.bridge.lua:212-214`，`trestle.bridge.lua:226`，`trestle_s.bridge.lua:212` |
| 钢桥 | 1940 年起 | 140 km/h | 轨道、街道 | 200 | `steel.bridge.lua:243`，`steel.bridge.lua:259`，`steel.bridge.lua:269` |
| 悬索桥 | 1940 年起 | 180 km/h | 轨道、街道 | 600 | `suspension.bridge.lua:277`，`suspension.bridge.lua:294`，`suspension.bridge.lua:304` |
| 混凝土桥 | 1970 年起 | 280 km/h | 轨道、街道 | 200 | `concrete.bridge.lua:162`，`concrete.bridge.lua:176`，`concrete.bridge.lua:187` |
| 斜拉桥 | 2000 年起 | 220 km/h | 轨道、街道 | 750 | `cable.bridge.lua:214`，`cable.bridge.lua:231`，`cable.bridge.lua:240` |
| 系杆拱桥 | 2010 年起 | 350 km/h | 轨道、街道 | 650 | `tarch.bridge.lua:253`，`tarch.bridge.lua:270`，`tarch.bridge.lua:280` |

- 桥梁限速 **叠加在** 轨道限速之上：高速线路经过钢桥时，在桥上以 140 km/h 运行。1970 年以前没有超过 180 km/h 的桥，2010 年以前没有允许 350 km/h 的桥。
- **隧道**（岩石隧道，1970 年起有混凝土隧道）在文件中 **没有限速**，基础价格都是 600（`tunnel_a.tunnel.lua:187-188`，`tunnel_a_car.tunnel.lua:185`，`tunnel_b.tunnel.lua:191-194`）。
- 桥梁和隧道的价格跟随基础设施成本（`post_run_util.tl:50-51`）。

```engine
桥梁或隧道的基础价格由引擎根据高度或深度（costFactors）换算成每米价格；官方 wiki 说价格取决于长度以及离地高度或地下深度。因此同样的基础价格，账单可能相差很大。隧道会降低城镇的声望（见 [声望](reputation.html)）。
```

```tip scripts
1970 年以前要让快速线路跨越山谷，悬索桥（180 km/h）是唯一快于 140 km/h 的桥；隧道则完全没有限速。
```

## 道口和信号灯

| 类型 | 年份 | 轨道最高速度 | 价格 | 来源 |
|---|---|---|---|---|
| 简易道口 | 1850 - 1925 | 120 km/h | 4,000 | `era_a_eu.rcr.lua:14-17`，`era_a_eu.rcr.lua:26` |
| 半栏杆道口 | 1925 - 1975 | 160 km/h | 1.6 万 | `era_b_eu.rcr.lua:15-18`，`era_b_eu.rcr.lua:27` |
| 现代半栏杆道口 | 1975 年起 | 160 km/h | 1.6 万 | `era_c_eu.rcr.lua:15-17`，`era_c_eu.rcr.lua:26` |
| 道路信号灯（1950 年以前为臂板式，1950 年起为色灯式） | 全部 | - | 9,000，每年维护费 1,500 | `signal_path_a.con.lua:4-5`，`signal_path_a.con.lua:10-11`，`signal_path_c.con.lua:4-5` |

- 道口把轨道限制在最多 160 km/h：高速线路需要用桥梁或隧道跨越街道。
- 每个信号灯都可以设为 **单向**（`signal_path_a.con.lua:51-52`）。信号灯如何把轨道划分为闭塞区间，见官方 wiki 的铁路信号页面。

## 车库和维修站

车库和维修站的花费、能服务多少载具以及服务半径：[线路和载具](vehicles.html) 和 [成本、维护费和贷款](costs.html)。

## 须知

- 1940 年以前，升级城镇街道很便宜；1940 年以后，每条新建或重建的城镇街道价格和维护费都是三倍。
- 在快速线路上，检查每座桥和每个道口：最慢的那个决定了那里的速度。
- 速度只有在带来更多趟次时才划算（见 [为什么我在亏钱？](money.html)）。

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: 轨道、街道和桥梁的速度与官方表格相同。文件中桥梁限速也适用于街道，隧道没有限速，道口把轨道限制在 120 或 160 km/h，树木让街道慢 25 %、污染减少 50 %，但噪音只减少 10 %；而隔音屏障让噪音减少 65 %，且不降低速度。
result: refines
```
