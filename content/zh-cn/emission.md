---
title: 污染与噪音
summary: 什么会产生噪音和污染，建筑何时排放更多，城镇如何评价它，以及产业绿化和净化厂实际做什么。
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
game: 40425
fact: 65–80 dB | 城镇噪音：65 时满分，80 时为零
fact: 60–74 | 城镇污染，按脚本的对数刻度（不是声音大小）：60 时满分，74 时为零
fact: −80 % | 绿化后产业的噪音和污染
fact: 700 m | 净化厂的作用范围
---

载具、轨道、道路、车站、车库、仓库和产业都会产生**噪音**和**污染**。城镇的两项评价**噪音**和**污染**，把到达城镇的量与固定界限比较。评价差会降低城镇当局评价，从而降低增长（见 [城镇](towns.html)）。

## 建筑何时排放更多

一个游戏脚本每隔几次更新，在安静水平与繁忙水平之间设定四类建筑的排放（`emissions.script.tl:12-18`）：

| 建筑 | 何时排放更多 | 来源 |
|---|---|---|
| **产业** | 生产时，每次加成（货物或工人）再增加；输出库存满时向闲置水平回落 | `emissions.script.tl:152-194` |
| **车站** | 越繁忙越多：等待的人和货物与容量相比 | `emissions.script.tl:211-222` |
| **车库**、**维护站** | 使用其维护的载具越多越多 | `emissions.script.tl:223-234` |
| **仓库** | 库存越满越多 | `emissions.script.tl:237-250` |

- 每个产业都有自己的四个等级：闲置、生产、加成一次、加成两次（`industryutil.lua:464-475`；默认的 0 / 78 / 84 / 88 只用于没有自己数值的产业）。大多数产业闲置时也会少量排放：煤矿的污染为 2 → 10 → 20 → 30，它的田地为 2 → 30 → 60 → 90（`coal_mine.con.lua:99-135`，见 [产业](industries.html)）。
- 输出无人运走的产业会回落到闲置水平：为它提供运输会提高它的污染。
- 载具和轨道也会排放；在**载具老化影响**设置下，状况差的载具排放更多（见 [成本、维护费与贷款](costs.html)）。

## 建造菜单显示什么

| 建筑 | 噪音 | 污染 | 来源 |
|---|---|---|---|
| 港口 | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| 机场 | 8–56 | 80–560 | `airport.tl:28-29` |
| 火车站 | 25 | 45–350 | `modular_station.con.lua:97-98` |
| 铁路车库 | 50 | 100 | `rail_depot.con.lua:32-33` |
| 道路和电车车库 | 40 | 80 | `road_depot.con.lua:30-31`，`tram_depot.con.lua:32-33` |
| 地下车站 | 40 | 80 | `underground_station.con.lua:75-76` |
| 卡车和公交车站 | 1–10 | 12–76 | `modular_terminal.con.lua:67-68` |
| 维护站 | 20 | 40–50 | `road_maint_station.con.lua:30-31`，`rail_maint_station.con.lua:30-31` |
| 仓库 | 20 | 50（通用）或 100（专用） | `warehouses/warehouse.tl:51`, `warehouses/warehouse.tl:73-74` |

两个数值是菜单显示的范围，从最低到最高，与旁边的价格范围一样（`construction_desc_react_util.tl:733-746`）；只有一个数值时就是单一数值。运行时，每座建筑越繁忙排放越多（见上表）。让港口、机场和大型货运站远离住宅。

## 城镇如何评价

| 评价 | 测量 | 满分 | 零 | 来源 |
|---|---|---|---|---|
| **噪音** | 城镇建筑处的噪音 | 65 dB 或以下 | 80 dB | `town_util.tl:433-443`，`emission_config.tl:10-11` |
| **污染** | 城镇面积每个 16 m 格子的平均污染（面积按最少 5、最多 10 km² 计），换算成脚本的对数刻度（“dB”） | 60 或以下 | 74 | `town_util.tl:413-431`，`emission_config.tl:23-30` |

- 只有**住宅**区受噪音影响；商业和工业建筑不受影响（官方 wiki）。住宅的窗口显示其位置的噪音（`town_building.tl:165-183`）。
- 污染按整个面积平均，所以远离中心的一个污染源，在大城镇中比在小城镇中分量更轻。
- **噪音敏感度**和**污染敏感度**设置会移动界限：两倍的敏感度相当于 +3 dB（`town_util.tl:426-428`，`town_util.tl:439-441`）。污染使用与噪音相同的对数刻度（10·log10）：+3 “dB” 表示污染翻倍。它不是声音大小。

| 档位 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 来源 |
|---|---|---|---|---|---|---|---|---|
| 噪音 | 关闭（始终满分） | ×¼ | ×½ | ×1 | ×1.4 | ×1.8 | ×3.5 | `difficulty_util.tl:48` |
| 污染 | 关闭（始终满分） | ×¼ | ×½ | ×1 | ×1.7 | ×3 | ×5 | `difficulty_util.tl:49` |

预设简单、中等、困难和非常困难使用档位 3、4、5 和 6（`difficulty_util.tl:114-115`，`difficulty_util.tl:142-143`，`difficulty_util.tl:169-170`，`difficulty_util.tl:196-197`）。

## 产业绿化

| | | 来源 |
|---|---|---|
| 效果 | 产业的噪音和污染 ×0.2（−80 %），永久 | `emission_config.tl:32`，`emissions.script.tl:184-192` |
| 次数 | 公司等级 3、6、9、12 和 15 各一次 | `industry_greenify_tool.script.tl:99-104` |
| 限制 | 每个产业一次；第二次尝试不消耗许可 | `company.script.tl:489-494` |

- 效果绑定在该版本的产业上：产业被重建时效果消失（`emissions.script.tl:187-190`）。
- 最佳用法：紧邻城镇的最繁忙产业，因为加成后的产业排放最多。

## 净化厂

一项公司特权，可清除周围的污染。

| | | 来源 |
|---|---|---|
| 价格 | 1 亿 | `pollution_cleanup_facility.script.lua:560` |
| 每年维护费 | 1000 万 | `pollution_cleanup_facility.script.lua:561` |
| 可用 | 公司等级 10 时 15 个 | `pollution_cleanup_facility.con.lua:106-108` |
| 需要 | **机器**：每周期 8 个，每年两个周期；20 名工人 | `pollution_cleanup_facility.con.lua:43-60` |
| 范围 | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| 状态 | 污染 | 噪音 | 来源 |
|---|---|---|---|
| 闲置（无机器） | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| 运行中 | −10,000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| 加成一次 | −20,000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| 加成两次 | −40,000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

- 没有机器时它几乎没用：必须像产业一样供应。
- 它很吵：建在住宅区以外，距离污染区 700 m 以内。
- 它的工人加成系数为 ×2（`pollution_cleanup_facility.script.lua:549`）。见 [工人](workers.html)。

## 小贴士

- 打开城镇窗口或噪音与污染图层，可以看到评价和热点。
- 输出库存满会让产业排放向闲置水平回落，但你会失去它的货物：与其饿着产业，不如让城镇搬开。
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) 和 [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 可以帮你找到最繁忙的车站。

```engine
引擎计算噪音和污染地图、数值如何扩散、载具和轨道的排放，以及产业何时重建。脚本只设定每座建筑的水平和城镇的界限。
```

```check
official: "Noise reflects noise levels in residential areas." "Pollution reflects pollution levels across the town area." 住宅区 "is sensitive to noise"；商业区 "is robust against the influence of noise"。([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: 噪音评价 65 → 80 dB，污染 60 → 74 dB，按 5–10 km² 平均；敏感度增加 10·log10 dB；产业、车站、车库和仓库繁忙时排放更多；输出库存满时产业排放向闲置水平回落；绿化每个产业一次 −80 %；净化厂在 700 m 内最多清除 40,000 污染，并需要机器。
result: refines
```
