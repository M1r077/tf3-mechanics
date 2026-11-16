---
title: 载具：状况、年龄与装载速度
summary: 载具各项数据的含义，状况和年龄如何运作，车库和维护站的作用，价格和运营成本从何而来，以及何时替换载具。
domain: vehicles
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-16
game: 40425
fact: 5 | 个状况等级，从很差到很好，每级 20 %
fact: 20 % | 触发载具状况警告的状况
fact: 6 years | 的运营成本：载具的价格
fact: 4 to 16 | 辆载具：一个车库或维护站的维护池容量
---

每辆载具都有固定数据（速度、容量、装载速度、价格、运营成本、寿命）和两个会变化的值：**状况**和**年龄**。状况在运行时下降，通过维护恢复；年龄只会增长。

## 载具商店中的数据

- 商店用条形显示每项数据。条形是与同一运输方式、同一时代的其他载具比较，而不是固定刻度（`vehicle_util.tl:210-245`，`vehicle_util.tl:248-270`）。
- 对于列车，商店显示其所有组成部分中**最高**的装载速度（`vehicle_store_util.tl:333`）。
- 文件中未设置装载速度、噪音、污染或舒适度的载具，会得到由其他数据（年份、速度、功率、重量、尺寸）计算出的值（`model_metadata_util.lua:395-417`，`vehicle_metadata_util.lua:233-256`）。计算出的装载速度四舍五入到 0.5，且不低于 1（`vehicle_metadata_util.lua:267-269`）。

## 哪种载具装货最快？

载具的装载速度只是第一个系数；站台和库存会与它相乘（见[装载与卸载速度](loading.html)）。

| 运输方式 | 条形满格时的装载速度（最新时代） | 来源 |
|---|---|---|
| 船舶 | 10 至 45（自 2003 年） | `vehicle_util.tl:219-223` |
| 道路载具、有轨电车 | 0.5 至 10（自 1995 年） | `vehicle_util.tl:232-243` |
| 列车 | 0.1 至 10（自 1981 年） | `vehicle_util.tl:226-229` |
| 飞机 | 1 至 4（自 1978 年） | `vehicle_util.tl:212-216` |

- 船舶的装载速度遥遥领先，飞机的刻度最低。
- 在商店中用装载速度一栏比较同一运输方式的载具；较新的型号通常条形更高。
- 每种货物的装载系数为 0.0625，乘客为 1（`coal.cargo.lua:29`，`passengers.cargo.lua:23`）。

```engine
载具装载速度、货物装载系数以及站台和库存系数如何组合成实际装载时间，由引擎计算。脚本只提供输入值。
```

## 状况

| 状况 | 等级 | 来源 |
|---|---|---|
| 高于 80 % | **非常好** | `vehicle_util.tl:159-172` |
| 60–80 % | **好** | `vehicle_util.tl:159-172` |
| 40–60 % | **中等** | `vehicle_util.tl:159-172` |
| 20–40 % | **差** | `vehicle_util.tl:159-172` |
| 不超过 20 % | **非常差** | `vehicle_util.tl:159-172` |

- 列车的状况是其所有车厢和机车的**平均值**（`vehicle_util.tl:285-295`）。
- 低于 80 % 时，载具开始损失最高速度、功率和舒适度，噪音、污染和运营成本开始增加（`vehicle_store_util.tl:230-259`）。载具窗口在**状况**下列出这些惩罚。
- 这些惩罚的强度由**载具老化影响**（无、低、中、高、非常高）决定；设为无时，状况没有任何影响（`mod.script.tl:241-245`，`vehicle_store_util.tl:211-228`）。详见：[成本、维护费与贷款](costs.html)。
- 状况降到 **20 %** 或以下时会出现**载具状况**警告，直到载具回到 **30 %** 以上才消失（`notifications.script.tl:310-318`）。
- 克隆的载具算作新购买：状况 100 %，新的购买日期（`manager_window.tl:8502-8506`）。

```engine
状况下降多快、一次维护站访问恢复多少，以及每项惩罚的大小（getMaintenanceTopSpeedPenalty 等）都是引擎数值。每个载具型号也可以为每个等级设定自己的最高速度惩罚（`vehicle_store_util.tl:250-253`）。
```

## 车库与维护站

载具由附近的车库或维护站维护。每座建筑能服务的载具数量有限：即其**维护池**。

| 建筑 | 维护池 | 半径 | 可停放载具 | 来源 |
|---|---|---|---|---|
| 火车车库 | 6 | 800 m | 5 | `rail_depot.script.lua:341-349` |
| 火车维护站 | 12 | 800 m | – | `rail_maint_station.script.lua:151-157` |
| 道路车库、有轨电车车库 | 12 | 400 m | 10 / 8 | `road_depot.script.lua:189-198`，`tram_depot.script.lua:217-226` |
| 道路维护站 | 16 | 600 m | – | `road_maint_station.script.lua:234-240` |
| 船坞 | 8 | 1000 m | 5 | `water_depot.script.lua:370-379` |
| 船舶维护站 | 12 | 1400 m | – | `water_maint_station.script.lua:256-262` |
| 机场或空港机库 | 16 | 550 m | 5 | `af_hangar.module.lua:272-280`，`ap_hangar.module.lua:455-463` |
| 直升机场 | 4 | 800 m | 5 | `heliport.script.lua:300-309` |

- 建筑窗口显示“已用 / 池”（例如 14 / 12）以及它所服务的载具列表和各自状况（`entity_window_util.tl:2010-2039`，`maintenance_station_eow.script.tl:188-215`）。
- 维护池越满，建筑越吵越脏：排放随池的使用比例增加（`emissions.script.tl:223-234`）。
- 火车维护站服务的列车是火车车库的两倍：12 对 6。
- 维护站不能购买或停放载具，但其半径常比车库大：道路上 600 m 对 400 m，船舶 1400 m 对 1000 m。只有道路维护站也维护有轨电车。
- 官方 wiki 建议用路径点让载具经过维护建筑。

```engine
载具被分配到哪个维护站、使用维护站的载具超过其维护池时会怎样，以及使用的服务半径，由引擎决定。
```

## 价格与运营成本

- 基础游戏的载具没有固定价格：运营成本来自速度和容量，价格为 **6 年**的运营成本（`model_metadata_util.lua:548-549`）。完整公式：[成本、维护费与贷款](costs.html)。
- **载具成本**和**载具养护**都可在 50 % 到 150 % 之间调整（`post_run_util.tl:54-81`）。
- 状况差的载具在基础值之上支付更多运营成本（`vehicle_store_util.tl:256-259`）。

## 年龄与寿命

- 每个型号都有以年计的**寿命**（`vehicle_metadata_util.lua:79-83`）。线路窗口的**年龄**一栏显示年龄；其提示显示剩余时间，或**已达到的生命时间**（`line_eow.script.tl:133-147`）。在达到寿命之前，该提示中的寿命比例显示 **0 %**：脚本在显示前把比例向下取整（`line_eow.script.tl:139`），而同一比例在别处是完整计算的（`vehicle_util.tl:311`）。请改看剩余时间。
- 对于列车，以**最老**的组成部分为准（`vehicle_util.tl:36-52`）。一节旧车厢就会让整列车显示为旧车。

```engine
达到寿命后会改变什么（例如状况下降更快或售价更低）不在脚本中。脚本只显示年龄和寿命。
```

## 何时应替换旧载具？

1. 即使附近有维护站，**状况仍然很低**：载具会损失速度并支付更多运营成本。先检查维护站的维护池：它可能已满。
2. 年龄提示中显示**已达到的生命时间**：该型号已超过计划寿命。
3. **有更好的型号**：更快或更大的载具运营成本更高，但运量更大（价格随速度 × 容量变化）。
4. 在线路管理器中使用**替换载具**。它会打开商店，并与当前载具进行比较（`vehicle_store_window.tl:4893-4928`，`vehicle_store_window.tl:2611`）。

```tip scripts
**车库旁的载具状态还是很差？打开它的窗口，看看“已用 / 容量”。** 火车车库服务 6 列火车，火车维护站服务 12 列。引擎如何处理超出容量的载具不在脚本中；再建一座建筑最稳妥。
```

## 小贴士

- 建造足够的维护能力：一座火车车库只服务 6 列列车。
- **载具老化影响**设为无时，状况无关紧要。
- **送往车库**会把载具送到最近的可到达车库，而不是购买它的那个车库（官方 wiki）。
- [Vehicle Comparison](https://mod.io/g/transportfever3/m/vehicle-comparison) 可在替换前帮助比较型号。

```check
official: "This section shows how well the vehicle is maintained and how the maintenance state affects the vehicle properties." "Loading speed modifies a vehicle's base loading speed which can be seen in the vehicle window or in the vehicle store." ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles))
scripts: 五个状况等级，每级 20 %；低于 80 % 时速度、功率、舒适度、排放和运营成本受到惩罚，强度由载具老化影响调整；20 % 时警告，高于 30 % 时解除。每座建筑的维护池为 4 至 16 辆载具。价格 = 6 年运营成本。列车的年龄 = 其最老的组成部分。缺失的装载速度由其他数据计算，四舍五入到 0.5，至少为 1。
result: refines
```
