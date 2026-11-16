---
title: Pollution and noise
summary: What emits noise and pollution, when a building emits more, how towns rate it, and what Industry Greenification and the Cleaning Plant really do.
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
game: 40425
fact: 65–80 dB | town noise: full rating at 65, zero at 80
fact: 60–74 | town pollution, on the scripts' log scale (not a sound level): full rating at 60, zero at 74
fact: −80 % | noise and pollution of a greenified industry
fact: 700 m | reach of the Cleaning Plant
---

Vehicles, tracks, streets, stations, depots, warehouses and industries all emit **noise** and **pollution**. Two town ratings, **Noise** and **Pollution**, compare what reaches the town with fixed limits. A bad one lowers the Town Authority rating and so the growth (see [Towns](towns.html)).

## When a building emits more

A game script sets the emission of four kinds of buildings every few updates, between a quiet and a busy level (`emissions.script.tl:12-18`):

| Building | Emits more when | Source |
|---|---|---|
| **Industry** | it produces, and again with each boost (cargo or workers); when all its output stocks are full together, its level is halved: producing → idle, boosted twice → producing | `emissions.script.tl:152-194` |
| **Station** | it is busier: waiting people and cargo against its capacity | `emissions.script.tl:211-222` |
| **Depot**, **maintenance station** | more vehicles use its maintenance | `emissions.script.tl:223-234` |
| **Warehouse** | its stocks are fuller | `emissions.script.tl:237-250` |

- Each industry has its own four levels: idle, producing, boosted once, boosted twice (`industryutil.lua:464-475`; the 0 / 78 / 84 / 88 default only applies to an industry without its own). Most still emit a little when idle: a Coal Mine goes 2 → 10 → 20 → 30 pollution, its fields 2 → 30 → 60 → 90 (`coal_mine.con.lua:99-135`, see [Industries](industries.html)).
- An industry whose output stocks are all full drops to half its level (`emissions.script.tl:172-182`): serving it raises its pollution.
- Vehicles and tracks emit too; a vehicle in bad condition emits more with the **Vehicle Maintenance Effect** setting (see [Costs, upkeep and loans](costs.html)).

## What the build menu shows

| Building | Noise | Pollution | Source |
|---|---|---|---|
| Harbour | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| Airport | 8–56 | 80–560 | `airport.tl:28-29` |
| Train station | 25 | 45–350 | `modular_station.con.lua:97-98` |
| Rail depot | 50 | 100 | `rail_depot.con.lua:32-33` |
| Road and tram depot | 40 | 80 | `road_depot.con.lua:30-31`, `tram_depot.con.lua:32-33` |
| Underground station | 40 | 80 | `underground_station.con.lua:75-76` |
| Truck and bus station | 1–10 | 12–76 | `modular_terminal.con.lua:67-68`, `modular_terminal.con.lua:121-122` |
| Maintenance stations | 20 | 40–50 | `road_maint_station.con.lua:30-31`, `rail_maint_station.con.lua:30-31` |
| Warehouse | 20 | 50 (universal) or 100 (specialised) | `warehouses/warehouse.tl:51`, `warehouses/warehouse.tl:73-74` |

Two values are the range the menu shows, from lowest to highest, like the price range next to them (`construction_desc_react_util.tl:733-746`); one value means a single figure. While running, each building emits more as it gets busier (table above). Keep harbours, airports and big freight stations away from houses.

## How a town rates it

| Rating | Measured | Full rating | Zero | Source |
|---|---|---|---|---|
| **Noise** | noise at the town's buildings | 65 dB or less | 80 dB | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Pollution** | average pollution per 16 m cell of the town area (area taken as at least 5 and at most 10 km²), converted to the scripts' log scale ("dB") | 60 or less | 74 | `town_util.tl:413-431`, `emission_config.tl:23-30` |

- Only the **residential** district suffers from noise; commercial and industrial buildings do not (official wiki). The window of a house shows the noise at its position (`town_building.tl:165-183`).
- Pollution is averaged over the whole area, so one source far from the centre weighs less in a big town than in a small one.
- The **Noise Sensitivity** and **Pollution Sensitivity** settings shift the limits: twice the sensitivity counts as +3 dB (`town_util.tl:426-428`, `town_util.tl:439-441`). Pollution uses the same log scale as noise (10·log10): +3 "dB" means twice the pollution. It is not a sound level.

| Step | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Source |
|---|---|---|---|---|---|---|---|---|
| Noise | Off (always full) | ×¼ | ×½ | ×1 | ×1.4 | ×1.8 | ×3.5 | `difficulty_util.tl:48` |
| Pollution | Off (always full) | ×¼ | ×½ | ×1 | ×1.7 | ×3 | ×5 | `difficulty_util.tl:49` |

The presets Easy, Medium, Hard and Very Hard use steps 3, 4, 5 and 6 (`difficulty_util.tl:114-115`, `difficulty_util.tl:142-143`, `difficulty_util.tl:169-170`, `difficulty_util.tl:196-197`).

## Industry Greenification

| | | Source |
|---|---|---|
| Effect | noise and pollution of the industry ×0.2 (−80 %), for good | `emission_config.tl:32`, `emissions.script.tl:184-192` |
| Uses | one at company rank 3, 6, 9, 12 and 15 | `industry_greenify_tool.script.tl:99-104` |
| Limit | once per industry; a second try uses no permit | `company.script.tl:489-494` |

- The effect is tied to that version of the industry: when the industry is rebuilt, it is lost (`emissions.script.tl:187-190`).
- Best use: the busiest industry right next to a town, since a boosted industry emits the most.

## The Cleaning Plant

A company perk that removes pollution around it.

| | | Source |
|---|---|---|
| Price | 100,000,000 | `pollution_cleanup_facility.script.lua:560` |
| Upkeep per year | 10,000,000 | `pollution_cleanup_facility.script.lua:561` |
| Available | 15 at company rank 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Needs | **Machines**: 8 per cycle, two cycles a year; 20 workers | `pollution_cleanup_facility.con.lua:43-60` |
| Reach | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| State | Pollution | Noise | Source |
|---|---|---|---|
| idle (no machines) | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| working | −10,000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| boosted once | −20,000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| boosted twice | −40,000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

The last level needs a booster rule, which the Cleaning Plant does not have: with workers it reaches −20,000 (`pollution_cleanup_facility.con.lua:51-58`, `emissions.script.tl:158-166`).

- Without machines it does almost nothing: it must be supplied like an industry.
- It is loud: build it out of the residential district, within 700 m of the polluted area.
- Its worker boost factor is ×2 (`pollution_cleanup_facility.script.lua:549`). See [Workers](workers.html).

## Good to know

- Open the town window or the noise and pollution layers to see the rating and the hotspots.
- When all output stocks of an industry are full, its emission level is halved, but you lose its cargo: better move the town than starve the industry.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) and [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) help you find the busiest stations.

```engine
The engine computes the noise and pollution maps, how the values spread, the emissions of vehicles and tracks, and when an industry is rebuilt. The script only sets each building's level and the town limits.
```

```check
official: "Noise reflects noise levels in residential areas." "Pollution reflects pollution levels across the town area." The residential district "is sensitive to noise"; the commercial district "is robust against the influence of noise". ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Noise rating 65 → 80 dB, pollution 60 → 74 dB averaged over 5–10 km²; sensitivity adds 10·log10 dB; industries, stations, depots and warehouses emit more when busy; when all output stocks are full, an industry's emission level is halved; greenification −80 % once per industry; the Cleaning Plant removes up to 20,000 pollution (40,000 is defined but needs a booster rule) within 700 m and needs machines.
result: refines
```
