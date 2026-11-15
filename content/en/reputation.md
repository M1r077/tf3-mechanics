---
title: Town reputation
summary: What lowers a town's Reputation rating, how fast it comes back, what celebrations and Marketing Campaigns really do, and why a cut road between two towns hurts so much.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
fact: −33 % | per interrupted main connection to another town
fact: ≈ 67 % | recovered per year at calendar speed ×1 (≈ 200 % during a Marketing Campaign); the town window shows 33 % and 100 %
fact: 0.25 % | per removed full-size tree next to the town
fact: 2 M m³ | of terrain work cost the whole reputation
---

**Reputation** is one of the six ratings of the town window, and the Town Authority takes the **lowest** of them (see [Town growth](towns.html)). It starts at 100 % and only goes down through what **you** build or fail: terrain work, removed trees and rocks, demolished town buildings, failed subsidies and cut main connections. Time, celebrations and Marketing Campaigns bring it back.

```diagram rep_recovery
```

## What lowers it

Every build you confirm is checked before it is applied; the cost is booked to the town concerned (`towns.script.tl:271-291`, `town_util.tl:1062-1080`). Only your own builds count, and nothing counts in the map editor (`town_util.tl:1078-1080`, `towns.script.tl:58`).

| Reason in the town window | What costs reputation | Source |
|---|---|---|
| **Removed Trees** | 0.25 % per tree, × the distance factor to the closest town, × the tree size (small trees count less) | `town_util.tl:1144-1150`, `town_util.tl:865`, `model_metadata_util.lua:655-680` |
| **Removed Rocks** | 0.25 % per rock, × the distance factor | `town_util.tl:1148-1149`, `town_util.tl:884-885` |
| **Landscaping** | 0.00005 % per m³ of terrain raised **or** lowered: 2 million m³ = 100 %. Terrain shaped by tracks, roads and buildings counts too (down to half for builds over 50,000 m²), and so does new tunnel volume | `town_util.tl:873-886`, `town_util.tl:1245-1269`, `town_util.tl:1403-1436` |
| **Demolished Buildings** | 100 % for 40.5 % of a district's capacity removed (homes, shops or jobs of that town) | `town_util.tl:867-869`, `town_util.tl:1165-1184` |
| **Failed Subsidy** | Supply Town: 10 % up to 60–90 % (by risk); Connect Towns: 10–100 % × the distance factor, in **both** towns (see [Subsidies](subsidies.html)) | `deliver_cargo_town.script.tl:202-210`, `deliver_passengers.script.tl:113-114`, `towns.script.tl:331-333` |
| **Interrupted Main Connections** | **1/3** per other town whose main connection is cut or too long | `town_util.tl:376-394`, `town_util.tl:1608` |

- Each reason is capped at 100 % (`town_util.tl:1611-1620`).
- While you build, the tooltip shows **Reputation: −x %**, with the number of towns hit when there are several (`construction_react_util.tl:3818-3864`). It counts the cost from a full rating.
- Planting trees or placing rocks only cancels **Removed Trees** or **Removed Rocks**, at the same 0.25 % each. It does nothing for the other reasons, and nothing at full reputation (`town_util.tl:1228-1238`, `town_util.tl:1630-1641`).
- The Reputation setting of a new game is **Off** or **On** (On in every preset). Off means a full rating, always (`difficulty_util.tl:44`, `difficulty_util.tl:110`, `town_util.tl:396-399`).

```engine
How fast the distance factor falls between a town and a removed tree, which terrain volume each town gets, the trees removed automatically by a track or road, and which roads count as a town's main connection (and when a trip is "too long") are engine values (getImpactFromDistance, getTerrainBrushVolumeImpact, getTerrainAlignmentImpact, getAutoRemovalEntityImpact, getTownProblems).
```

## Cut main connections

A main connection counts as cut when the game raises **Road Connection Between Towns Has Been Interrupted** or **Travel Time Between Towns Is Too Long** (`town_util.tl:378-380`, `town_warning.script.tl:7-22`). Each other town concerned costs 1/3, and the rating shows it **at once** (`town_util.tl:401-403`):

| Cut connections | Reputation at most | Rating | Source |
|---|---|---|---|
| 1 | 67 % | Very Good | `town_util.tl:983-985` |
| 2 | 33 % | Mediocre | `town_util.tl:983-985` |
| 3 | 0 % | Very Poor: the town stops growing | `town_util.tl:607-633` |

- While the cut lasts, the penalty is also written into the stored score, step by step, over half a year (`towns.script.tl:137-145`). After you repair the road, that stored part comes back only at the normal recovery speed: a long cut keeps costing reputation for a while.
- 67 % is right on the Very Good limit: any other small loss drops the town to Good.

## How it comes back

- **By itself**: one level (1/6) every 3 months of game time (360 s), every month (120 s) during a Marketing Campaign (`towns.script.tl:121-135`). At calendar speed ×1 that is about **67 %** a year, **200 %** with a campaign: from 0 % back to full in about 1.5 years. The town window shows **Annual Recovery** 33 % and 100 %: fixed texts, half the real speed (`town_react_util.tl:1066`). Measured on a test town: one level every 358 s, every 120 s with a campaign.
- Recovery shares the gain over all reasons; it never goes past the cut connections still open (`town_util.tl:1649-1687`).
- **Celebrations** add **+50 %** for the first passenger who boards one of your lines in a town, +50 % for the first cargo delivered to a town, +50 % at every level-up of the town, and +20 % to the closest town for the first cargo delivered to each industry (`celebrations.script.tl:181-273`). The message then ends with **Settlement reputation improved.** or **Reputation improved in …** (`celebration_react_util.tl:63-75`). They only count while the reputation is not full, not in campaign missions (`celebrations.script.tl:79-93`, `celebrations.script.tl:140-142`).
- **Supply Town** can give +5 % to +20 % × the risk factor on acceptance (`deliver_cargo_town.script.tl:195-199`). Like every gain, it only removes existing losses (`towns.script.tl:324-330`).

## Marketing Campaign

| What | Value | Source |
|---|---|---|
| Price | 10 M × year factor: 4 M in 1900 up to 25 M in 2020, rounded to 1 M | `marketing_campaign_tool.script.tl:9-14` |
| Needs | one permit of the company perks | `marketing_campaign_tool.script.tl:83-95`, `company.script.tl:416-423` |
| Duration | one year | `marketing_campaign_tool.script.tl:136` |
| Reputation | recovery ×3 (≈ 200 % a year, the window shows 100 %); **no** instant gain | `towns.script.tl:126`, `town_util.tl:915-925` |
| Residents | your lines in that town count as half as costly when residents choose how to travel | `marketing_campaign_tool.script.tl:137`, `towns.script.tl:376-398` |

```engine
The script counts 360 seconds of game time per level (120 with a campaign), with a month of 30 days of 4 seconds. Recovery runs on game time: with a slower calendar a calendar year lasts longer, so more comes back per year shown. How strongly the halved line cost moves residents to your lines is decided by the engine's route choice.
```

## Good to know

- Watch the build tooltip: if it shows **Reputation: −x %**, a tunnel or a gentler route is often cheaper than the reputation.
- Never leave a main road between two towns cut: each one is −33 % at once, and three cuts stop the town.
- A Marketing Campaign at full reputation only helps your lines, not the rating. Launch it right after big works, when the recovery has something to recover.
- The **Reputation Recovery** bonus of the large headquarters module (+1 %) shows in the Bonuses tab, but in the scripts it only changes a value that no rating reads (`hq_module_l.module.lua:171`, `towns.script.tl:157`, `town_util.tl:829`, `town_util.tl:857`).
- The achievement **It Wasn't Me** needs a town at 0 % reputation in a free game (`achievements.script.tl:261-267`).

```check
official: "Reputation reflects how the town and surrounding nature are treated. Landscaping, removing town buildings and breaking main connections to other towns can lower it, while celebrations and marketing campaigns can improve it. Reputation lost by removing trees can be recovered by planting new ones." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Same causes, plus removed rocks, tunnels, track and road embankments and failed subsidies. Each cut or too long main connection costs 1/3 at once; three stop the town. Recovery is about 67 % a year by itself and about 200 % with a Marketing Campaign, twice what the town window shows (33 % and 100 %); the campaign gives nothing at once. Planting trees only cancels the tree loss. The headquarters' Reputation Recovery bonus has no effect in the scripts.
result: differs
```
