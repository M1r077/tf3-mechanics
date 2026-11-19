---
title: Workers and the workers boost
summary: How residents get a job at an industry, which ones count for the boost, and how big the boost is.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-15
game: 40444
fact: 10 / 20 | workers needed for the boost
fact: 2 years | how long an arrival counts
fact: ×1.5–2.5 | boost factor, fixed per industry
---

Every industry offers workplaces. When enough workers **arrive by your passenger lines**, the industry produces more. The industry window shows two different numbers, and mixing them up is the most common source of confusion.

```diagram workers_flow
```

## Who can work at an industry

- Every base-game industry has **20 workplaces** (`industrialCapacity = 20`).
- The workplaces are set up so that residents **cannot walk or drive** there: only your lines can bring them (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Each resident has a home, a shop and a job. The game picks the job among the places that resident can reach; an industry has a destination weight of 2.0 (`industryutil.lua:455`).

```engine
How a resident picks one job among all the places it can reach (travel time, cost, the weight of 2.0) is computed by the engine. The scripts only give the inputs.
```

## Assigned workers

The residents whose job is this industry. This is the workplaces bar of the industry window and the **Workplaces** column of the industry statistics ("12/20") (`entity_window_util.tl:1238`, `statistic_industries.tl:304`). Assigned workers alone do **not** boost anything: they must actually travel there.

## Workers counted for the boost

A small game script watches every arrival (`industry_workers.script.tl`):

1. When a resident arrives at an industry and its **last move was by your lines**, the arrival is noted with the game time (`industry_workers.script.tl:86-118`).
2. Only arrivals of the **last 2 game years** are kept (`industry_productivity_util.tl:3`: `2 * getDefaultYearDuration()`).
3. Once 20 arrivals are kept, older ones are dropped; the new arrivals of one update are always kept whole (`industry_workers.script.tl:4`, `KeepHistoryCount = 20`, `industry_workers.script.tl:54-70`).
4. When the same person arrives again, the new arrival replaces that person's older entry: each resident counts **once** (`industry_workers.script.tl:56-70`).

```diagram workers_window
```

## When the boost starts and stops

- The industry is boosted when the counted workers reach **half of the workplaces**: `counted ≥ workplaces × 0.5` (`industry_productivity_util.tl:35-48`, `RequiredWorkersFractionForBoost = 0.5`). With 20 workplaces: **10 workers**.
- The Booster section of the industry window shows exactly this: "counted / needed", with needed rounded up (`industry_react_util.tl:627`).
- The check runs again whenever new arrivals come in or the oldest one becomes older than 2 years (`industry_workers.script.tl:40-43`). So the boost **stops by itself** about 2 years after the workers stopped coming.

## How big the boost is

- Production is multiplied by the industry's **boost factor**, shown in the window as "+X %" (`industry_react_util.tl:716`).
- The factor is drawn once from the industry's random seed: **between ×1.5 and ×2.5**, and it never changes for that industry (`industry_productivity_util.tl:58-72`). An industry with no seed uses ×2.
- So two identical mines can have different worker boosts: check the "+X %" before choosing which one to serve.

## Example

A coal mine with 20 workplaces and "+84 %".

| Situation | Counted | Boosted? | Production |
|---|---|---|---|
| New bus line: 14 residents assigned, none has arrived yet | 0 | no | ×1 |
| 12 different residents arrived by bus this year | 12 | yes (≥ 10) | ×1.84 |
| Bus line removed; nobody arrives for 2 years | drops to 0 | stops | ×1 |

## Getting workers to an industry

```diagram workers_trip
```

- A worker is counted when it **arrives at the industry** itself, its trip target (`targetOrAtEntity`) is the industry and its last move mode is **Lines** (`industry_workers.script.tl:86-94`). Getting off at a stop is not enough: the person must reach the industry.
- Each resident has one move mode per destination (home, shop, job). The industry window lists the assigned workers with an icon for this mode: **Walk**, **Car** or **Lines** (`entity_window_util.tl:1400-1435`). For an industry it should always be Lines, because Walk and Car are not allowed there (`industryutil.lua:451-457`).
- So "no walking" means the whole trip cannot be a walk or a car trip. It does not mean "no walking at all": a Lines trip still starts and ends on foot between the stops and the buildings (see the engine note below).
- **Transfers count.** The script only looks at the mode of the trip, not at how many lines were used (`industry_workers.script.tl:91`). A worker from a town four lines away counts the same as one from next door, but may take much longer to arrive.
- **Any of your lines can bring them**, also a line that carries cargo, as long as its vehicles take passengers and the stop loads passengers. The script does not check the vehicle type (`industry_workers.script.tl:86-118`). Players report fewer problems with separate passenger lines.
- Some industries (for example oil rigs) have their own built-in stop, which takes passengers and cargo (`industryutil.lua:156-165`).
- The industry window shows, for each assigned worker, whether it is **Currently Here** or **On the Way** (`entity_window_util.tl:1371-1384`). The Booster section lists the counted workers with their **Time Left** of the 2 years (`entity_window_util.tl:1579-1630`, `industry_eow.script.tl:647-652`).
- When no arrival is counted (none in the last 2 years), the worker list of the Booster section shows: "Connect this location with public transport to allow residents to work here." (`entity_window_util.tl:1650-1652`, `entity_window_util.tl:1608`, `entity_window_util.tl:1632`).

```engine
Which stop serves an industry, how far a worker walks from a stop to the industry entrance, and which towns' residents take the job are decided by the engine (catchment areas, path finding, job choice). The scripts set no distance limit for workers. Players report that a station whose catchment area covers the industry for cargo did not bring workers until a bus ran to the industry entrance (Steam thread "Problem getting workers to site").
```

```tip
**Get the workers boost (and the Transport Workers contract) fast: start with a simple line.**

1. Build a **new passenger line** from a stop at the industry to **one town**.
2. Place the town stop so that its catchment **touches none of your other passenger stations**.
3. One vehicle is enough to start.

The jobs are given when the line opens: in two tests all **20 jobs went to that one town**, and the boost started after **346 s and 925 s** of game time (once with a single vehicle). When the town stop touched the catchment of a network station, some jobs went to a distant town and the last workers took much longer (964 s). Measured with [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) and the [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard); who gets a job is still decided by the engine.
```

## Transport Workers subsidy

- It is offered only for an industry with workplaces whose workers boost is not active yet and that shipped cargo over the last year (`deliver_workers.script.tl:121-131`, `industry_util.tl:541-558`). Every rule has an output table (booster rules have `output = { }`) and an empty Lua table counts as true, so only this branch is reached (`industry_util.tl:544-551`).
- It is completed when the workers boost becomes active: the same 10 of 20 different arrivals by your lines (`deliver_workers.script.tl:152-156`). Nothing else is counted; there is no hidden rule.
- The progress bar on the contract card is "counted workers ÷ half the workplaces" (`deliver_workers.script.tl:267-272`, `industry_util.tl:11-18`).
- The arrows on the contract map come from the **5 nearest towns**. They are only a hint: the script draws them by distance, not by who has the job (`deliver_workers.script.tl:297-317`).
- See [Subsidies](subsidies.html) for money and deadline.

## Why don't my workers arrive?

| Check | Where to look | Why |
|---|---|---|
| Does anyone have the job? | Workplaces bar ("12/20") | Without assigned workers nobody travels. Job choice is engine-side. |
| Mode icon of the workers | Workers list: Walk / Car / Lines | Only trips by Lines can count (`industry_workers.script.tl:91`). |
| Are they moving? | **On the Way** / **Currently Here** | "On the Way" for a long time: slow or overloaded transfers, or no path from the last stop. |
| Does the last stop reach the industry entrance? | Stop catchment, entrance road | Reported by players; engine-side. A short bus to the entrance helped. |
| Does the stop load passengers? | Line stop, Cargo Filter | Passengers must be loaded and unloaded at both ends of the trip. |
| 10 **different** people in 2 years? | Booster section, **Time Left** | The same person counts once; older arrivals drop out (`industry_workers.script.tl:56-70`). |
| More than 40 workplaces (mods)? | Workplaces bar | Can never reach half with 20 kept arrivals. |

## Good to know

- The cap of 20 kept arrivals and the 50 % rule mean that an industry with **more than 40 workplaces** (possible with mods) could never be boosted by workers.
- The **Transport Workers** subsidy is completed when this boost activates (`deliver_workers.script.tl:152-156`).
- Booster cargo (fertilizer, machines, tools) is a **separate** boost of raw industries, not covered here.
- The [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) mod shows, in the industry window, which towns the assigned and boost workers come from, with arrows on the map.

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: "Sufficient" = half of the workplaces (10 of 20); "recently" = the last 2 game years, latest 20 arrivals, one per person, by your lines only; boost factor ×1.5 to ×2.5 per industry. Transfers count; the trip mode must be Lines, walking from a stop is part of such a trip.
result: refines
```
