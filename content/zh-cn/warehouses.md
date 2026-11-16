---
title: 仓库
summary: 通用或专用模块，每个库存装什么，固定货物类型，装载速度，成本与污染，以及仓库不做的事。
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
fact: 500 | 每个模块可存的货物单位，不论类型
fact: ×2 | 专用模块的装载速度，通用模块为 ×1
fact: 15 万 / 30 万 | 通用 / 专用模块的价格
fact: 0 | 在仓库卸下的货物带来的收入
---

仓库由一个入口和一组**模块**组成。它在两条线路之间存放货物：一条线路卸货，另一条线路再装货。车站通过服务范围连到仓库；城镇和产业从不从仓库拿任何东西（官方 wiki）。

## 通用模块与专用模块

| 模块 | 库存 | 存放 | 系数 | 来源 |
|---|---|---|---|---|
| **通用** | 所有通用模块共享**一个**库存 | 任何货物，可混放 | ×1 | `warehouse.script.lua:272-295`，`modules.script.lua:49` |
| **液体**、**散货**、**拖车**、**商品** | **每个模块一个库存** | 一次一种货物，属于本类别 | ×2 | `warehouse.script.lua:296-314`，`modules.script.lua:120`，`modules.script.lua:165`，`modules.script.lua:247`，`modules.script.lua:296` |

- 每个模块增加 **500** 个单位（`modules.script.lua:49`，`modules.script.lua:120`）。五个通用模块组成一个 2,500 的库存；五个液体模块组成五个 500 的库存。
- 乘客从不存放（`warehouse.script.lua:279`，`warehouse.script.lua:304`）。
- 专用模块一次只接收一种货物：要存放原油和燃料，需要两个液体模块（官方 wiki）。
- 专用模块的 ×2 与站台系数相乘：散货站台加散货模块得到 ×4。详见：[装载与卸载速度](loading.html)。

## 通用还是专用？

1. **货物种类多、数量少**：通用。一个共享库存，价格减半，污染也减半。
2. **一种货物、数量大**（煤炭、原油、原木）：专用。载具在那里卸货和装货快一倍，但每种货物需要一个模块。
3. **食物等运输时间短的货物**：专用；官方 wiki 说这些模块会冻结交付计时（见下文）。
4. 两种模块可以混在一个仓库里：通用模块仍组成一个库存，每个专用模块各有自己的库存。

## 仓库会加快卸货吗？

- **专用模块**：会，对它接收的货物为 ×2。载具的装载提示框显示“专用仓库：+100 %”（`cargo_react_util.tl:51-54`）。
- **通用模块**：不会。它的库存创建时为 ×1；模块申请的 ×2 被忽略（`warehouse.script.lua:284`，`warehouse.script.lua:288-289`）。
- 当一部分货物进仓库、一部分进产业时，载具轮流为它们服务，所以一次停靠中速度会变化（游戏内实测，见 [装载与卸载速度](loading.html)）。

## 库存部分

- 每个库存一行：它接收的货物、数量，以及悬停时显示的**平均剩余运输时间**（`entity_window_util.tl:408-410`）。
- **固定货物类型**：在专用模块上点击一个货物图标。游戏会重建仓库，把该模块留给这种货物（`entity_window_util.tl:339-367`，`warehouse.script.lua:308`）。移除或替换模块会清除固定（`warehouse.script.lua:403-405`）。
- **丢弃全部货物**：立即清空这一行（`entity_window_util.tl:423-434`）。货物会丢失。
- 只有属于其他玩家的仓库没有这两个按钮；你自己的仓库和没有所有者的仓库都有（`warehouse_eow.script.tl:127-137`，`gui/entity_window/warehouse/warehouse.tl:38`，`entity_util.tl:83-86`）。
- **数据**图表按年显示**即将抵达**（卸下的）和**即将出发**（装上的）（`warehouse_eow.script.tl:159-160`）。

## 成本与污染

| | 通用模块 | 专用模块 | 来源 |
|---|---|---|---|
| 价格 | 15 万 | 30 万 | `wh_universal.module.lua:18`，`wh_liquid.module.lua:22` |
| 每年维护费 | 2.5 万 | 5 万 | `wh_universal.module.lua:19`，`wh_liquid.module.lua:23` |
| 噪音 | 20 | 20 | `wh_universal.module.lua:33`，`wh_liquid.module.lua:37` |
| 污染 | 25 | 50 | `wh_universal.module.lua:34`，`wh_liquid.module.lua:38` |

- 仓库本身也会增加污染：**25**，只要建了一个专用模块就是 **50**（`warehouse.script.lua:327`，`warehouse.script.lua:338-345`）。
- 建造菜单中每个类别和时代（从 1900、1940 和 1980 年起）各有一项（`warehouses/warehouse.tl:3-5`）；后面的时代显示 ×3 和 ×9，仓库维护费也随年份增长。详见：[成本、维护费与贷款](costs.html)。
- 散货、拖车和商品模块的花费与液体模块相同（`wh_bulk.module.lua:22-23`，`wh_flatbed.module.lua:22-23`，`wh_goods.module.lua:18-19`）。

```engine
脚本给出两个排放等级，第二个是第一个的两倍（`warehouse.script.lua:342-343`）；仓库随着库存填满从第一个过渡到第二个，库存满时为两倍（`emissions.script.tl:237-249`）。模块实际收取的价格由引擎计算。
```

## 仓库不做的事

- **它不付钱。** 在仓库卸货没有收入；货物只在到达消费者时按离来源地的直线距离支付一次（游戏内实测，见 [货物收入与运输时间](income.html)）。
- **它不给附近的城镇或产业供货**：它们只从载具接收货物（官方 wiki）。
- **它不是线路自动配置的目的地**，自动配置只寻找生产者和消费者；但在存放某种货物的仓库旁的站点，这种货物不会进入载重列表，所以列车会在那里把它卸下（见 [装载与卸载速度](loading.html)）。
- **它不需要道路。** 入口会吸附到街道上，但货物只通过车站的服务范围移动（`warehouse.script.lua:386-389`，官方 wiki）。仓库窗口会显示它的服务范围（`gui/entity_window/warehouse/warehouse.tl:88-96`）。

```engine
卸下的货物去哪里，以及存放的货物的交付计时是否停止，都由引擎决定。没有脚本冻结计时：官方 wiki 说专用模块会冻结，通用模块不会。
```

## 须知

- 检查仓库附近每个站点的载重列表：不在列表里的货物会卸进仓库，即使在线路半途。
- 库存满了就不再接收货物，除非站点使用“到达时强制卸下所有货品”，那样放不下的会被销毁（见 [装载与卸载速度](loading.html)）。
- 要让一个专用模块只存一种货物，就在库存部分固定它的货物类型。
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 会按车站列出范围内的仓库及其库存；[Platform Details](https://mod.io/g/transportfever3/m/platform-details) 会显示卸下的货物去了哪里。

```check
official: "Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types." 专用仓库 "freeze the cargo item's delivery timer" 和 "enable faster loading / unloading speeds". "In specialized warehouses, only one cargo type can be stored at a time for a given module." ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: 通用模块组成一个共享库存，系数 ×1；每个专用模块有自己的 500 库存，×2，只存一种货物。专用模块花费两倍（30 万，维护费 5 万），污染也两倍（50）。冻结计时不在脚本中。
result: refines
```
