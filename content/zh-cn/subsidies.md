---
title: 补贴：报价、期限与奖励
summary: 四种合同类型，真正完成它们需要什么，你能得到什么、要冒什么风险，以及新报价多久出现一次。
domain: subsidies
official: gamemanual:management:subsidies
status: verified
updated: 2026-11-15
fact: 4 | 自由游戏中的合同类型
fact: 5 | 同时最多接受的合同数
fact: ×2 | 交付过的线路 5 年内的收入
fact: 0 | 拒绝报价的惩罚
---

补贴就是一份合同：一个产业或城镇提出一项任务，你接受时就能得到一些东西，按时完成后得到更多，错过期限则要退还预付款并再付一笔惩罚。拒绝报价，或让它过期，都没有任何代价。

```diagram subsidy_life
```

## 四种合同类型

```diagram subsidy_types
```

| 合同 | 目标 | 怎样完成 | 来源 |
|---|---|---|---|
| **供应产业** | 一个从未生产过任何东西的产业 | 向它交付规定的次数，**它的任何一种原料**都算 | `deliver_cargo.script.tl:54-61`，`deliver_cargo.script.tl:230-234`，`deliver_cargo.script.tl:470-479` |
| **供给城镇** | 城镇需要、但完全没有得到的一种货物 | 向城镇的建筑交付规定数量的**这种货物** | `deliver_cargo_town.script.tl:566-581` |
| **连接城镇** | 两个城镇 | **一名**乘客在一条同时停靠两个城镇的线路上，开始一次两城之间的行程 | `deliver_passengers.script.tl:263-280`，`subvention_util.tl:561-592` |
| **运输工人** | 一个已经在发货或收货、尚未获得加成的产业 | 它的工人加成生效（工作岗位的一半） | `deliver_workers.script.tl:121-131`，`deliver_workers.script.tl:152-156` |

- 每个新报价从当前能够出现的类型中抽取一种，机会均等（`subventions.script.tl:147-169`）。
- **供应产业**和**供给城镇**统计的是交付，不是行程：每个到达目标并获得报酬的单位加 1。允许换乘（`deliver_cargo.script.tl:470-479`）。
- **连接城镇**不要求乘客人数：第一名在两城之间登上你的线路的乘客就能完成它。“无需换乘”是指这段行程由一条服务两个城镇的线路完成。如果已有线路在两城之间运送乘客，就不会出现这个报价（`deliver_passengers.script.tl:72-78`）。
- 距离近的城镇出现的概率高得多：一对城镇的权重从 1 km 以内的 1 降到 20 km 时的 0.01，再取 7 次方（`deliver_passengers.script.tl:175-191`）。
- **供给城镇**偏好地图上已经有人生产的货物：概率是其他货物的 16 倍（`deliver_cargo_town.script.tl:277-280`）。
- 需要交付的数量取决于**补贴风险**设置：

| 补贴风险 | 供应产业 | 供给城镇（最多为城镇的需求量） | 来源 |
|---|---|---|---|
| 无 | 10–50 | 10–30 | `deliver_cargo.script.tl:100-114`，`deliver_cargo_town.script.tl:165-188` |
| 公平 | 50–100 | 30–100 | |
| 有风险 | 75–150 | 35–125 | |
| 风险极大 | 150–300 | 45–150 | |

## 什么是无需换乘的连接？

**连接城镇**卡片的要求是：“在{fromTownName}和{toTownName}之间建立无需换乘的直达路线，并在两座城镇之间运送乘客。”（`deliver_passengers.script.tl:14`）。

- **一条在每个城镇都有站点的线路。**游戏逐一检查线路的站点，取得每个站点所属的城镇；只要两个城镇中各有至少一个站点，这条线路就算数。其他站点、站点顺序和载具类型（公交车、有轨电车、火车、船只、飞机）都无关紧要（`subvention_util.tl:561-592`）。
- **一名乘客就能完成它**：第一名乘坐这条线路、从一个城镇的站点到另一个城镇的站点的乘客，方向不限（`deliver_passengers.script.tl:263-280`，`deliver_passengers.script.tl:210-218`）。检查只看这一段乘车，所以在此之前或之后换乘应该没有影响。
- **站点所属的城镇**是其车站组中第一个车站所属的城镇（`town_util.tl:1844-1873`）。车站属于哪个城镇由引擎决定。
- 如果已有线路在每个城镇都有一个让乘客上车的站点，并且有一辆载客的载具，就**不会出现报价**（`deliver_passengers.script.tl:72-78`）。两城之间只运货的线路不会阻止报价。
- 当两个城镇之一，或完成合同的那条线路，发生了游戏视为新版本的变化时，合同以**补贴已移除**结束（`deliver_passengers.script.tl:232-240`）。

```engine
车站属于哪个城镇（stationSystem.getTown）、乘客究竟何时“开始使用”一条线路（OnStartedLineUsage），以及线路的哪些编辑算作新版本，都由引擎决定。完成后编辑线路是否会结束“可产生两倍收入”效果，尚未测试。
```

## 奖励与惩罚

每份合同保存三张列表，在合同卡片上显示为**接受时**、**完成时**和**失败时**（`subvention_util.tl:449-471`）。失败时，预付款总是要退还，另外再加一项惩罚（`deliver_cargo.script.tl:134-136`）。

| 合同 | 接受时 | 完成时 | 失败时 | 来源 |
|---|---|---|---|---|
| 供应产业 | 现金 | 只有“可产生两倍收入”效果 | 退还预付款 + 罚款 | `deliver_cargo.script.tl:120-136` |
| 供给城镇 | 现金**或**城镇中的声誉 | 城镇经验**或**现金，外加两倍收入 | 退还预付款 + 声誉损失**或**罚款 | `deliver_cargo_town.script.tl:194-229` |
| 连接城镇 | 现金，城镇相距越远越多 | **两个**城镇的城镇经验，外加两倍收入 | 退还预付款 + **两个**城镇的声誉损失 | `deliver_passengers.script.tl:105-119` |
| 运输工人 | 现金 | 现金 | 退还预付款 + 罚款 | `deliver_workers.script.tl:92-116` |

- **现金**，未按年份缩放前：预付款 150 万到 375 万 × 风险系数（无 ×2，公平 ×1，有风险 ×0.75，风险极大 ×0.5）；罚款 300 万到 600 万；完成奖励 375 万到 1,125 万（`deliver_cargo.script.tl:120-128`，`deliver_workers.script.tl:102-104`）。
- 金额随**日历年份**增长，与通货膨胀设置无关：1900 年 ×1，均匀上升到 2000 年及以后的 ×4，向上取整到 1 万（`finances_util.tl:87-90`）。在资金中记为**补贴**（`subvention_util.tl:126-135`）。
- **供给城镇**只有在你的账户余额低于 1 亿时才会给现金奖励和罚款；高于 1 亿时，只有十分之一的报价仍会这样（`deliver_cargo_town.script.tl:206-217`）。
- **城镇经验**是城镇当前等级的一定比例：当前等级到下一级之间所需经验的 20 % 到 100 %（`deliver_cargo_town.script.tl:216`，`town_growth.script.tl:605-608`）。对于**连接城镇**，还要乘以距离系数，从 1 km 时的 0.3 到 20 km 时的 3.0：相距很远的城镇可以连升好几级（`deliver_passengers.script.tl:94-96`，`deliver_passengers.script.tl:116-118`）。
- 失败后损失的**声誉**会在城镇的声誉评价中显示为**失败的补贴**（`towns.script.tl:313-334`）。接受时获得的声誉只会抵消已有的惩罚，不能超过满值（`town_util.tl:1644-1647`）。

## 两倍收入效果

- 合同完成后持续 **60 个月**（5 年）（`subvention_util.tl:286`，`subvention_util.tl:292`）。
- **供应产业**：在合同期间向该产业交付过的线路上，向该产业的交付（`deliver_cargo.script.tl:463-469`）。
- **供给城镇**：在交付过合同货物的线路上，向该城镇任何建筑的交付，**任何货物**都算（`deliver_cargo_town.script.tl:554-565`）。
- **连接城镇**：完成合同的那条线路上两城之间的乘客（`deliver_passengers.script.tl:281-304`）。
- **运输工人**没有收入效果（`deliver_workers.script.tl:90`）。
- 合同完成后才开始交付的线路什么也得不到：线路列表只在合同期间填写。
- 两份合同不会把同一笔收入翻倍两次：多份合同同时符合时，只采用最后一个结果（`subventions.script.tl:570-583`）。

```engine
补贴的 ×2 与公司等级乘数（通货膨胀设置）如何组合，由引擎决定：两个脚本都只为每笔收入返回一个乘数。一笔收入条目是什么（大概是一个货物单位或一名乘客）也由引擎决定。
```

## 期限

期限从你接受时开始。货物需要运得越远，期限越长；风险越高，期限越短（风险系数：无 ×2，公平 ×1，有风险 ×0.75，风险极大 ×0.5，乘客和工人合同则为 ×0.625）：

| 合同 | 期限（月） | 使用的距离 | 来源 |
|---|---|---|---|
| 供应产业、供给城镇 | (6 + 32 × E) × 风险系数 | 到生产该货物的最近产业 | `deliver_cargo.script.tl:116-117` |
| 连接城镇 | (9 + 4 × E) × 风险系数 | 两个城镇之间 | `deliver_passengers.script.tl:98-99` |
| 运输工人 | (6 + 15 × E) × 风险系数 × 时代系数（1940 年前 ×1.75，1980 年前 ×1.25） | 到最近的城镇 | `deliver_workers.script.tl:75-87` |

E 是一列以当时最高速度行驶的列车（1900 年起 120 km/h，到 1981 年起 300 km/h）跑完这段距离所需的时间，向上取整，至少为 1（`subvention_util.tl:486-489`，`vehicle_util.tl:225-230`）。

- 未被接受的报价大约 **6 个月**（150 到 210 天）后消失，没有任何惩罚（`subvention_util.tl:284`，`subvention_util.tl:290`）。
- **供应产业**或**运输工人**合同进行期间，目标产业不会关闭：计划中的关闭会被取消（`subvention_util.tl:473-484`）。
- 如果目标在合同期间消失或被重建，游戏会显示**补贴已移除**，但仍会像错过期限一样执行失败惩罚（`subventions.script.tl:172-190`，`subvention_util.tl:406-412`）。
- 没有取消已接受合同的按钮。

```engine
一个游戏月有多长，也就是期限的实际长度，由引擎设定（getDefaultMonthDuration）。上面的公式都以游戏日历的月为单位。
```

## 新报价多久出现一次

- **补贴可用性**：很少、有时（默认）、经常、极频繁分别每 12、6、3、1 个月出现一个新报价；**从不**则关闭补贴（`subvention_util.tl:13-38`，`mod.script.tl:247-248`）。
- 间隔随**公司等级**变长：等级 1 时 ×1，到等级 15 时 ×2（`subvention_util.tl:19-22`）。
- **拒绝**报价会让下一次间隔减半；接受报价或出现新报价会将其重置（`subventions.script.tl:429`，`subventions.script.tl:395`，`subventions.script.tl:118`）。
- 已接受并在进行中的合同达到 **5 份**时，不会再出现新报价（`subventions.script.tl:23`，`subventions.script.tl:256-262`）。第一个报价在半个月后出现。
- 同一个目标（产业、城镇加货物、一对城镇）**每局游戏只提供一次**，即使合同被错过或失败也一样（`subventions.script.tl:107-113`，`subventions.script.tl:186`）。
- 难度预设的可用性 / 风险（`difficulty_util.tl:104-105`，`difficulty_util.tl:132-133`，`difficulty_util.tl:159-160`，`difficulty_util.tl:186-187`）：简单 经常 / 无，正常 有时 / 公平，困难 很少 / 有风险，**极难 从不**：完全没有补贴。
- 只允许在评价为非常好的城镇出现补贴的检查确实存在，但已被关闭（`town_util.tl:1574-1580`，`deliver_cargo_town.script.tl:272-275`）。

## 须知

- 目标容易时尽管接受：拒绝或忽略都没有代价，但**失败**要退还预付款，再加一笔可能比预付款还多的罚款。
- 对于**供给城镇**和**供应产业**，所有想要受益的线路都要开始交付：只有在合同期间交付过的线路才能在 5 年内获得两倍收入。
- 相距很远的城镇之间的**连接城镇**给的城镇经验最多，而且只需要一名乘客。
- **供应产业**完成时不再给任何报酬：它的奖励只有两倍收入。

```check
official: "Accept an offer to begin the contract; declining it has no penalty." "Possible rewards include town experience, an additional payment, or a limited-time 2x income effect on eligible transport lines." "The upfront reward is reversed, and an additional fine or loss of town reputation may apply." ([Subsidies](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:subsidies))
scripts: 四种类型；一名乘客即可完成连接城镇；×2 在合同期间交付过的线路上持续 60 个月；供应产业只给 ×2；金额按年份缩放（×1 到 ×4）；每 1–12 个月一个新报价，公司等级高时更久；最多同时接受 5 份；每个目标每局只提供一次。
result: refines
```
