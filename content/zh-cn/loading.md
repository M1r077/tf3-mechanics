---
title: 装载与卸载速度
summary: 是什么让载具在站点装货快或慢：载具本身、站台分段，以及另一侧提供或接收货物的库存。
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-14
fact: ×2 | 专用站台分段
fact: ×0.25 | 分段不对或列车过长
fact: ×4 | 最佳情况：专用站台加专用仓库
---

载具装货或卸货所用的时间，等于它自身的装载速度乘以两个系数：一个来自**站台**，一个来自另一侧的**库存**（仓库、产业、城镇）。

```diagram loading_factors
```

## 1. 载具

每辆载具都有基础装载速度，显示在载具商店和载具窗口中（“2.0x”）。下面的所有系数都乘在它上面。

## 2. 站台系数

对游戏来说，站台不是一排模块：它是一份**分段列表，每种货物类别一段**，该类别所有模块的长度相加。

```diagram loading_sections
```

| 车厢…… | 系数 | 来源 |
|---|---|---|
| 位于本类别的分段上（散货车厢，散货分段） | **×2** | `modular_station.script.lua:1042` |
| 位于通用分段上 | ×1 | `modular_station.script.lua:1042` |
| 站台上没有本类别的分段 | **×0.25** | `cargo_react_util.tl:60` |
| 超出站台长度的部分（列车过长） | **×0.25** | `cargo_react_util.tl:61` |

- 系数**按列车所占比例混合**：如果 3/4 的车厢匹配、1/4 不匹配，系数为 ¾ × 2 + ¼ × 0.25 ≈ ×1.56（`cargo_react_util.tl:63-70`，游戏中显示为“部分专用停靠位”的也是这种划分）。
- 车厢停在站台的**哪个位置**并不重要，只看相加后的长度（游戏内实测）。
- 公路：专用卡车站台给出 ×2（`modular_terminal.script.lua:2956`）；路边小站点始终为 ×1（`small_stops.script.lua:19`）。
- 客运站台为 ×1。

## 3. 库存系数

卸货时，每个单位的货物都会交给一个接收方：仓库模块、产业或城镇建筑。接收方的库存有自己的系数。

| 接收方 | 系数 | 来源 |
|---|---|---|
| **专用**仓库模块（液体、散货、拖车、商品） | **×2** | `modules.script.lua:120`，`warehouse.script.lua:297-314` |
| **通用**仓库 | ×1 | `warehouse.script.lua:272-285` |
| 产业 | ×1 | 游戏内实测 |

- 每个仓库模块都申请 ×2，但通用模块只是给**一个共享的通用库存**增加容量，而这个库存创建时就是 ×1。只有专用模块拥有自己的 ×2 库存。
- 游戏的提示框把这个系数称为“专用仓库：+100 %”（`cargo_react_util.tl:51-54`）。
- 在一次卸货中，游戏**轮流**为各个接收方服务。所以当一部分货物进仓库、一部分进产业时，列车卸货过程中速度会变化（游戏内实测）。

```engine
每个单位交给哪个接收方，以及最后的乘法，都在引擎中完成。上面的系数是脚本交给引擎的输入；结果已经用引擎公开的数值核对过（[Platform Details](https://mod.io/g/transportfever3/m/platform-details) 探针，2026 年 10 月）。
```

## 游戏中显示的内容

- 装载指示器在高于 ×1.5 时显示为**加速**，低于 ×0.75 时显示为**减速**（`cargo_react_util.tl:119-122`）。
- 把鼠标悬停在上面：提示框会列出“专用停靠位”“专用类型不匹配”“停靠位过短”和“专用仓库”，每项附带百分比（`cargo_react_util.tl:76-99`）。

## 示例

一列由 8 节散货车厢组成、长 160 m 的列车，卸载煤炭。

| 车站 | 站台 | 接收方 | 系数 |
|---|---|---|---|
| 通用站台 160 m | ×1 | 铁厂 | **×1** |
| 散货站台 160 m | ×2 | 铁厂 | **×2** |
| 散货站台 160 m | ×2 | 专用散货仓库 | **×4** |
| 散货站台 160 m | ×2 | 通用仓库 | **×2** |
| 通用站台 120 m（列车超长 40 m） | ¾ × 1 + ¼ × 0.25 ≈ ×0.81 | 铁厂 | **×0.81** |

## 须知

- 产业内部的车站始终专用于该产业所需的货物（官方 wiki）。
- 专用仓库模块还会冻结所存货物的交付计时（官方 wiki）；通用仓库不会。
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) 会显示站台上每辆载具的两个系数，以及卸下的货物去了哪里。

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." 专用仓库 "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: 专用分段 ×2，通用 ×1，没有匹配分段 ×0.25，超出站台 ×0.25，按列车所占比例混合；专用仓库模块 ×2，通用仓库 ×1。
result: refines
```
