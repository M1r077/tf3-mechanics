---
title: 地标、庆祝活动与趣味元素
summary: 每个地标需要多少货物、何时解锁、对所在城镇载具有什么作用，地标所需资源 设置如何缩放它，以及庆祝活动、烟花、飞艇和 UFO 实际做了什么。
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 9 + 3 | 个地标：基础游戏 9 个（等级 2 到 15），DLC 包再加 3 个（等级 1）
fact: +20 % / +25 % / -20 % / -25 % | 所在城镇载具的最高速度、污染或舒适度
fact: ×0 到 ×4 | 地标所需资源 设置下所需货物的倍率
fact: 2–4 年 | 两次 UFO 之间的间隔
---

地标像工地一样建造：用公司等级解锁，放置后**运送货物**过去。工地收齐所有货物后，地标完成，并为**所在城镇**的载具提供加成。总部是单独的建筑，有自己的规则（见[公司等级、特权与总部](company.html)）。

## 地标一览

货物数量按 **地标所需资源** ×1（正常）计算。

| 地标 | 等级 | 需运送的货物 | 所在城镇载具的加成 | 来源 |
|---|---|---|---|---|
| **圆形剧场** | 2 | 800 石料 | 道路载具：噪音 **-25 %** | `arena.con.lua:10`，`arena.con.lua:20-26`，`arena.con.lua:39` |
| **大灯塔** | 5 | 1,200 石料，200 燃料 | 船舶：最高速度 **+20 %** | `lighthouse.con.lua:10`，`lighthouse.con.lua:14`，`lighthouse.con.lua:29`，`lighthouse.con.lua:48` |
| **姬路城** | 7 | 1,200 石料，400 厚木板 | 列车：污染 **-20 %** | `white_heron_castle.con.lua:10`，`white_heron_castle.con.lua:14`，`white_heron_castle.con.lua:28`，`white_heron_castle.con.lua:47` |
| **船舶博物馆** | 9 | 600 木材，600 厚木板，200 纤维 | 船舶：舒适度 **+25 %** | `ship_museum.con.lua:10-18`，`ship_museum.con.lua:36`，`ship_museum.con.lua:55` |
| **新天鹅堡** | 10 | 1,000 石料，600 厚木板，200 染料 | 道路载具：舒适度 **+25 %** | `neuschwanstein.con.lua:10-18`，`neuschwanstein.con.lua:36`，`neuschwanstein.con.lua:55` |
| **自由女神像** | 11 | 800 石料，400 钢，400 金属薄板 | 船舶：污染 **-20 %** | `statue_of_liberty.con.lua:10-18`，`statue_of_liberty.con.lua:38`，`statue_of_liberty.con.lua:57` |
| **颐和园** | 13 | 600 石料，300 厚木板，300 染料，300 家具 | 飞机：污染 **-20 %** | `summer_palace.con.lua:10-22`，`summer_palace.con.lua:44`，`summer_palace.con.lua:63` |
| **歌剧院** | 14 | 800 石料，400 玻璃，400 金属薄板，400 纤维 | 列车：舒适度 **+25 %** | `opera_house.con.lua:10-22`，`opera_house.con.lua:44`，`opera_house.con.lua:63` |
| **议会大厦** | 15 | 800 石料，400 厚木板，400 玻璃，400 家具 | 道路载具、列车、船舶和飞机：最高速度 **+20 %** | `westminster.con.lua:10-22`，`westminster.con.lua:45`，`westminster.con.lua:79` |

**DLC 地标。** 两个 DLC 包再增加三个，从等级 1 起解锁。它们的文件位于游戏的 DLC 文件夹（Deluxe Upgrade Pack 和 Pre-order Pack）中，不在本 wiki 索引的基础文件之内，因此这里没有来源链接。

| 地标 | DLC | 等级 | 需运送的货物 | 所在城镇载具的加成 |
|---|---|---|---|---|
| **埃菲尔铁塔** | Deluxe Upgrade Pack | 1 | 400 钢 | 道路载具：最高速度 **+25 %** |
| **泰姬陵** | Deluxe Upgrade Pack | 1 | 800 石料 | 飞机：噪音 **-25 %** |
| **大金字塔** | Pre-order Pack | 1 | 800 石料 | 列车：最高速度 **+25 %** |

- 每个地标由其等级解锁一次；等级如何提升见[公司等级、特权与总部](company.html)。
- 在文件中，地标的建造费和每年费用都是零：只需要货物（`arena.con.lua:59-64`）。
- 工地每次只能存放每种货物的一半，所以每种货物至少要送两次（`arena.con.lua:13-18`）。

## 建造地标

- 工地有 **4 个阶段**。随着货物到达而推进：全部货物的三分之一时进入阶段 2，三分之二时进入阶段 3，100 % 时完成。每种货物只计到它自己的数量，所以多余的石料不能弥补缺少的厚木板（`landmarks.script.tl:34-46`）。
- 加成只在地标**完成**后才生效（`landmark_util_serialized.tl:393-395`）。此时会出现“建设已完成”消息（`landmarks.script.tl:49-61`）。
- **地标所需资源** 设置会给所有货物乘上倍率：无 ×0、低 ×0.5、正常 ×1、高 ×2 或 非常高 ×4。预设为简单 ×0.5、正常 ×1、困难 ×2、极难 ×4。在 ×0 时，地标一放置就完成（`difficulty_util.tl:40`，`difficulty_util.tl:107`，`difficulty_util.tl:135`，`difficulty_util.tl:162`，`difficulty_util.tl:189`，`landmarks.script.tl:38`，`landmarks.script.tl:46`）。

## 谁获得加成

- 加成给予**离地标最近的城镇**，以及最近城镇就是该城镇的、所列运输方式的载具（`landmark_util.tl:6-47`，`landmarks.script.tl:208-236`）。
- 载具驶入另一城镇的区域时，会获得那个城镇的加成并失去原来的加成（`landmarks.script.tl:279-299`）。
- 同一城镇中多个地标的加成会**叠加**：两个 +20 % 最高速度得到 +40 %（`landmark_util.tl:46`，`vehicle_modifier.script.tl:3-16`）。

```engine
地标或行驶中载具的“最近城镇”由引擎决定（getConstructionClosestTown，closestTown）。+25 % 舒适度或 +20 % 最高速度如何转化为行程和收入，也是引擎的工作。
```

```tip scripts
把议会大厦建在你的载具运行最多的城镇：所有运输方式最高速度 +20 %。同一城镇的船舶还能从大灯塔再得 +20 %。集中建设成就要求 10 个最近城镇相同的已完成地标；总部不计入，因为它没有需运送的货物。基础游戏有 9 个地标，DLC 包再加 3 个（已清点）；没有 DLC 能否达成集中建设尚不清楚（见[成就](achievements.html)）。
```

## 庆祝活动

庆祝活动是某件事第一次发生时在城镇上方显示的小派对。它还会提高城镇的**声誉**，但仅在声誉尚未满时。

| 事件 | 声誉 | 来源 |
|---|---|---|
| 城镇中第一位乘客登上你的线路 | +50 % | `celebrations.script.tl:228-252` |
| 第一次向城镇运送货物 | +50 % | `celebrations.script.tl:187-198` |
| 城镇升级 | +50 % | `celebrations.script.tl:260-272` |
| 第一次向某个产业运送货物 | 离它最近的城镇 +20 % | `celebrations.script.tl:202-219` |

- 城镇升级时还会放**烟花**，除非已将其关闭（`town_growth.script.tl:108-112`）。
- 声誉如何运作：[声誉](reputation.html)。

## 趣味元素

- 在某个城镇开始营销活动时，会有一艘**飞艇**飞过该城镇（`fun_elements.script.tl:112-117`）。
- 地图上没有 UFO 时，每隔游戏时间 **2 到 4 年**（随机）会出现一个 **UFO**（`fun_elements.script.tl:10`，`fun_elements.script.tl:79-91`）。点击它可获得第三类接触成就。
- 它们都不会改变经济。

## 须知

- 建造前先选好城镇：加成不跟随你的线路，只作用于该城镇附近的载具。
- 极难下地标需要四倍货物：议会大厦需要 3,200 石料以及其他货物各 1,600。

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: 九个基础地标，等级 2 到 15 每级最多一个，另有三个 DLC 地标位于等级 1，都用运送的货物分 4 个阶段建成，并按 地标所需资源 ×0 到 ×4 缩放。完成后，每个地标为其最近城镇中一种运输方式的载具提供一项加成（+20 % 或 +25 % 最高速度、-20 % 污染、-25 % 噪音或 +25 % 舒适度）；加成可叠加。庆祝活动增加 50 % 或 20 % 声誉；UFO 每 2 到 4 年出现一次。
result: adds
```
