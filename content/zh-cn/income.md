---
title: 货物收入与运输时间
summary: 一次交付能赚多少钱（直线距离、爬升、公司等级、补贴），以及迟到真正的代价是什么。
domain: economy
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: 3.8 | 所有货物相同的收入系数
fact: +8 × 爬升 | 爬升的米数计入距离
fact: 100 % | 即使迟到也全额支付
---

一次交付只按**直线距离**付钱，与行程的其他方面无关。速度之所以重要是另一个原因：每种货物都有**时间限制**，迟到的交付会降低城镇的**运送**评价，而不是你的收入。

```diagram income_formula
```

## 收入公式

整个公式就是一段很短的游戏脚本（`cargo_income.script.lua:10-13`）：

1. 货物的**收入系数**。每种基础游戏货物都使用同一个函数和同样的价格（`initialPrice = 4`，`finalPrice = 3.2`），因此**全部 36 种货物都是 3.8**（`cargotype.script.lua:7-13`，`coal.cargo.lua:21-22`）。在相同距离上，煤炭和商品赚的钱完全一样。
2. **货物收入** 设置：50 %、75 %、100 %、125 % 或 150 %（`difficulty_util.tl:38`，`mod.script.tl:211`）。四个难度预设都使用 100 %（`difficulty_util.tl:97`）。
3. **距离**，见下文。

这个函数会收到行程时间，但**并不使用它**（`cargotype.script.lua:7-13`）：慢的或迟到的交付收入一样。

## 距离：直线加爬升

```diagram income_distance
```

- 距离是两点之间的**三维直线**，而不是你线路的长度（`cargo_income.script.lua:3-7`）。
- 高度差为正时，会加上 **8 × 该高度**（`cargo_income.script.lua:5`）：爬升 100 m 相当于多走 800 m。反方向则什么也不减。
- 所以弯弯曲曲的线路和笔直的线路赚得一样多，但你建的每一米轨道或道路都要付维护费。

```engine
比较的是哪两个点（货物进入你的网络的地点、交付的地点），以及高度差的正负，都由引擎决定。官方 wiki 写道："distances are measured as the crow flies between the source and the final destination"（距离按起点与最终目的地之间的直线测量）。
```

## 还有什么会改变金额

| 因素 | 效果 | 来源 |
|---|---|---|
| **公司等级**，配合通货膨胀设置 | 等级 1：×1，均匀下降到等级 15：×0.9（低）、**×0.75（正常）**、×0.6（高）、×0.5（非常高）；无：始终 ×1 | `company_progression_util.tl:25-40`，`difficulty_util.tl:50`，`mod.script.tl:694-697` |
| **已完成的补贴** | 为该合同交付货物的线路 ×2 | `deliver_cargo.script.tl:463-469`，`deliver_cargo_town.script.tl:554-565` |
| **迟到交付** | 对收入没有影响 | `cargotype.script.lua:7-13` |

- 等级乘数作用于**所有**货物和乘客收入（`company_growth.script.tl:159-170`）。难度预设使用的通货膨胀分别为：低（简单）、正常（正常）、高（困难）、非常高（极难）（`difficulty_util.tl:108`）。
- 补贴的 ×2 只作用于合同期间交付过的线路，并且有时间限制（官方 wiki，补贴）。

## 乘客

乘客使用同样的距离和约 3.61 的固定收入系数（`cargotype.script.lua:50-53`），再乘以 **0.5 + 载具的票价系数**（`cargo_income.script.lua:14-17`）。当载具模型没有设置舒适度系数时，游戏把票价系数设为：公交车和有轨电车 0.3，飞机 0.9，船只 0.1，列车 0.5（`base_mod.lua:46-61`）；其他模型的数值来自引擎，在脚本中看不到。乘客补贴同样会让其线路的收入翻倍（`deliver_passengers.script.tl:284-298`）。

## 运输时间限制

每种货物都有自己的时间限制（每个 .cargo.lua 中的 `timeToDeliverInSeconds`，例如 `meat.cargo.lua:30`、`coal.cargo.lua:30`）。生鲜食品最短，重型原料长五倍：

```diagram delivery_times
```

- **资金 › 货物运输时间** 显示你的地图上每种货物的时间限制；货物满意度图层把路线从绿色到红色着色。
- 交付在超过时间限制后到达，就算作**延误**（`towns.script.tl:425`）。
- 专用仓库模块会**冻结**所存货物的计时（官方 wiki，仓库）。

```engine
引擎把基础时间换算成资金中显示的时间限制（脚本通过 getAdjustedDeliveryTime 读取），并判断一件货物何时算迟到。上面只有相对数值来自货物文件。
```

## 迟到的代价：运送评价

迟到的货物照样全额付款，但每个城镇都有一项**运送**评价（`town_util.tl:505-519`）：

1. 游戏统计**最近半年**交付到该城镇的次数，以及其中迟到的次数（至少按 10 次计算，所以最初几次交付不会让评价大起大落）。
2. 准时比例 → 评价：低于下限时评价为 0，高于上限时为 1，两者之间为线性。默认敏感度（**正常**）下：**准时 30 % → 0，100 % → 1**，所以准时 90 % 得到 0.86。
3. **交货敏感度** 设置会移动这两个界限（`difficulty_util.tl:47`）。关：始终为 1。预设：简单为低，正常为正常，困难为高，极难为非常高（`difficulty_util.tl:113`）。

```diagram delivery_rating
```

运送是六项评价之一，其中最低的一项决定城镇的增长率：只要有一项评价为非常贫穷，城镇就会停止增长（见 [城镇增长](towns.html)）。

## 示例

同样一次煤炭交付，直线距离 5 km。

| 情况 | 收入 |
|---|---|
| 平地，线路长度任意 | **100 %** |
| 相距 10 km | **200 %** |
| 目的地高 100 m | **116 %** |
| 迟到交付 | **100 %**（运送评价下降） |
| 公司等级 15，通货膨胀正常 | **75 %** |
| 已完成补贴的线路 | **200 %** |

## 须知

- 既然每种货物每公里的收入都一样，**按运量、距离和时间限制来选货物**，而不是按价格。
- 时间限制对肉类、鱼、蔬菜和饮料最重要：用短线路，或用能冻结计时的仓库。
- 每交付一个单位的货物到城镇建筑，也会给该城镇带来经验（`town_growth.script.tl:642`，`town_growth_config.res.lua:5`）。

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks), [Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: 所有货物系数都是 3.8；距离为三维直线加 8 × 爬升；公司等级会降低收入，等级 15 时降到 ×0.75（通货膨胀正常）；补贴完成后 ×2；收入不使用时间；运送评价取决于最近半年的准时比例（正常：30 % → 0，100 % → 1）。
result: refines
```
