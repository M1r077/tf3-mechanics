---
title: Workers and the workers boost
summary: How residents get a job at an industry, which ones count for the boost, and how big the boost is.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-14
fact: 10 / 20 | workers needed for the boost
fact: 2 years | how long an arrival counts
fact: ×1.5–2.5 | boost factor, fixed per industry
---

Every industry offers workplaces. When enough workers **arrive by your passenger lines**, the industry produces more. The industry window shows two different numbers, and mixing them up is the most common source of confusion.

```diagram workers_flow
```

## Who can work at an industry

- Every base-game industry has **20 workplaces** (`industrialCapacity = 20` in each industry's .con.lua).
- The workplaces are set up so that residents **cannot walk or drive** there: only your lines can bring them (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Each resident has a home, a shop and a job. The game picks the job among the places that resident can reach; an industry has a destination weight of 2.0 (`industryutil.lua:455`).

```engine
How a resident picks one job among all the places it can reach (travel time, cost, the weight of 2.0) is computed by the engine. The scripts only give the inputs.
```

## Assigned workers

The residents whose job is this industry. This is the workplaces bar of the industry window and the **Workplaces** column of the industry statistics ("12/20") (`entity_window_util.tl:1238`, `statistic_industries.tl:305`). Assigned workers alone do **not** boost anything: they must actually travel there.

## Workers counted for the boost

A small game script, `industry_workers.script.tl`, watches every arrival:

1. When a resident arrives at an industry and its **last move was by your lines**, the arrival is noted with the game time (`industry_workers.script.tl:86-118`).
2. Only arrivals of the **last 2 game years** are kept (`industry_productivity_util.tl:3`: `2 * getDefaultYearDuration()`).
3. At most the **latest 20** arrivals are kept (`industry_workers.script.tl:4`, `KeepHistoryCount = 20`).
4. When the same person arrives again, the new arrival replaces the older one: each resident counts **once** (`industry_workers.script.tl:56-70`).

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

## Good to know

- The cap of 20 kept arrivals and the 50 % rule mean that an industry with **more than 40 workplaces** (possible with mods) could never be boosted by workers.
- The subsidy "Transport workers" is completed when this boost activates (official wiki, Subsidies).
- Booster cargo (fertilizer, machines, tools) is a **separate** boost of raw industries, not covered here.

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: "Sufficient" = half of the workplaces (10 of 20); "recently" = the last 2 game years, latest 20 arrivals, one per person, by your lines only; boost factor ×1.5 to ×2.5 per industry.
result: refines
```
