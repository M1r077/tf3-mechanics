---
title: Industries
summary: Production rules, stocks, plots and expansion, why an industry does not grow or is not boosted, when an unused industry closes, and how new industries appear.
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
game: 40444
fact: 5 years | without loading or consumption make an industry a closure candidate
fact: 1.1 % | chance per year at Rarely (the default), then 730 days of countdown
fact: +50–150 % | booster cargo boost, fixed per industry
fact: 3 months | of boost per batch of booster cargo
fact: ×2/3 – ×1.5 | Industry Target Density: new industries cannot be turned off
---

Every industry works by **rules**: "take this from the input stocks, put that in the output stocks", a fixed number of times per year. Raw industries (mines, farms, wells) need no input; their size comes from **plots**. Two boosts can multiply the output: **booster cargo** (raw industries only) and **workers**.

## Production rules

- A rule gives the cargo used and made per run, and how many runs per year: one run lasts one year ÷ that number, shorter by the boosts for production rules (`industry_react_util.tl:51-57`). The Production section of the industry window shows it as small numbers.
- The **Max.** number of the window is: per run × runs per year × the size factor (`rule.consumptionFactor`) × the boosts × the **Industry Productivity** setting, the last two for production rules only (`industry_util.tl:310-379`, `industry_util.tl:357-362`).
- **Industry Productivity**: 50 %, 75 %, 100 %, 150 % or 200 %. Presets: Easy 150 %, Normal 100 %, Hard 75 %, Very Hard 50 % (`difficulty_util.tl:41`, `difficulty_util.tl:93`, `difficulty_util.tl:120`, `difficulty_util.tl:148`, `difficulty_util.tl:175`, `mod.script.tl:197-198`).
- Example, Steel Mill: 6 iron ore + 6 coal → 3 steel + 4 sheet metal, 121.7 runs a year: 730 iron ore and 730 coal → 365 steel and 487 sheet metal (`steel_mill.con.lua:43-71`). Missing one input stops the rule.
- The Canning Factory has two rules: fish + sheet metal, or meat + sheet metal (`food_factory.con.lua:43-74`).

```engine
The engine runs the rules. It can make a run last longer: the run tooltip then shows "(+ … Due to Delivery Time)" (`industry_react_util.tl:61-76`). When and by how much is not in the scripts, so the real production can stay below Max.
```

## Stocks

- Each cargo has its own stock with a limit: e.g. a Coal Mine keeps 100 tools and 400 coal, a Steel Mill 800 iron ore, 800 coal, 400 steel and 500 sheet metal (`coal_mine.con.lua:44-67`, `steel_mill.con.lua:43-71`).
- Stocks never decay (`industryutil.lua:25-29`): cargo waits as long as needed.
- A full output stock does not stop production: the extra cargo is thrown away (official wiki). The **Cargo Flow** chart shows **Consumed**, **Produced** and **Destroyed** (`industry_eow.script.tl:807-819`).
- With the construction parameter **Input** set to Off, the rules lose their inputs and the industry has no input stocks (`industryutil.lua:280-287`, `industryutil.lua:383-387`, `industryutil.lua:432-441`).

## Plots and expansion

- Raw industries and the Livestock Farm have **plots** (fields, mine shafts, rigs). Their level is their number of plots (`industryutil.lua:602-617`).
- The rule grows with the plots: output per run × plots ÷ **all plots of that industry type**, rounded, at least 1. Inputs are cut by the same share, rounded up, at least 1, but not at all if one output keeps its full amount (for example an output of 1, which cannot go lower); booster rules are never cut (`industryutil.lua:225-259`). A Coal Mine (8 plot types) with 4 plots makes 8 coal per run instead of 16.
- Each industry gets a maximum: random between half of the plots and all of them, or Small / Medium / Large (50 / 75 / 100 %) with the **Industry Size** parameter (`industryutil.lua:519-537`). A mine whose maximum is 5 of 8 never reaches the full rule.
- With Medium, if 75 % rounds up to all plots, the maximum is all plots minus one (`industryutil.lua:523-526`). A new industry starts with the plots the engine builds at placement; its level is set from them (`industryutil.lua:602-617`).
- Every half year of **game time** the game may add **one plot** (`industries_config.res.lua:5`, `industries.script.tl:161-167`). Half a standard year is used, so the calendar speed does not change how often (see [Game time and calendar](time.html)).
- The chance is (rating − 25 %) ÷ 50 %, where rating = production rating × the share of the output you ship (at most 1): 25 % or less never, 75 % or more always (`industries.script.tl:168-179`).
- So an industry whose cargo you do not ship **never grows**. Factories have no plots and never grow.
- At the maximum the window says **Industry is expanded to its full potential.**; when buildings, tracks or roads are in the way, **Industry is blocked from further expansion.** (`industry_react_util.tl:588-602`, `industries.script.tl:13-38`). No script removes plots; the official wiki says bulldozed plots lower the production.
- The game script skips industries you own, industries with manual development, and industries in a closing countdown: they never get a plot from it (`industries.script.tl:94-99`, `industries.script.tl:147-157`).

Example, **Logging Camp**: 20 plots, 8 logs per run, 30.4 runs a year (`forest.con.lua:54-66`, `forest.con.lua:75-98`). Per run it makes 8 × plots ÷ 20, rounded, at least 1 (`industryutil.lua:231-241`):

| Plots (level) | Logs per run | Logs per year (Max., no boost, Productivity 100 %) |
|---|---|---|
| 1–3 | 1 | 30 |
| 4–6 | 2 | 61 |
| 7–8 | 3 | 91 |
| 9–11 | 4 | 122 |
| 12–13 | 5 | 152 |
| 14–16 | 6 | 183 |
| 17–18 | 7 | 213 |
| 19–20 | 8 | 243 |

The output grows in steps: a new plot does not always raise the production.

## Why does my industry not grow?

```diagram ind_growth
```

1. **Cargo not shipped**: the rating counts the share of the output loaded onto your vehicles. With a production rating of 100 %, shipping 25 % or less gives no chance, 50 % a chance of one half, 75 % or more a plot every half year.
2. **At its maximum**: **Industry is expanded to its full potential.** The maximum is drawn at construction (half to all plots) and never changes.
3. **Blocked**: **Industry is blocked from further expansion.** Remove the roads, tracks or buildings on the place of the next plot (shown in the window).
4. **Not a raw industry**: factories have no plots.
5. **Closing countdown**, owned by you, or manual development: no growth from the script (above).
6. **No output**: an industry producing nothing in the year is skipped (`industries.script.tl:168-171`).

```tip scripts
**To make a mine or a farm grow, ship at least 75 % of its output and keep its production rating high.** The growth chance uses production rating × share shipped: at 25 % or less there is no new plot; at 75 % or more with a 100 % production rating, one every half year, until its maximum.
```

```engine
The production rating (getProductionRating), the yearly output and the shipped amount (getCargoOutputPerYear, getCargoShippedPerYear), and where a new plot goes (makeIndustryExtendProposal) are engine values.
```

## Booster cargo

The 13 raw industries have a second rule, the **booster**: it takes a batch of booster cargo from the input stock 4 times a year and gives a bonus while it runs.

| Industry | Plots | At full size, per year | Booster batch (4 a year) | Source |
|---|---|---|---|---|
| Clay Pit | 8 | 365 clay | 12 tools | `clay_pit.con.lua:42-82` |
| Coal Mine | 8 | 320 coal | 13 tools | `coal_mine.con.lua:44-85` |
| Cotton Farm | 21 | 274 wool | 17 fertilizer | `cotton_farm.con.lua:42-98` |
| Crop Farm | 20 | 274 grain + 183 vegetables | 17 fertilizer | `farm.con.lua:44-106` |
| Fishing Grounds | 18 | 263 fish | 12 tools | `fishing_grounds.con.lua:44-101` |
| Logging Camp | 20 | 243 logs | 15 machines | `forest.con.lua:44-99` |
| Iron Ore Mine | 8 | 365 iron ore | 15 machines | `iron_ore_mine.con.lua:44-84` |
| Oil Platform | 9 | 365 crude oil | 12 machines | `oil_platform.con.lua:45-96` |
| Oil Well | 14 | 548 crude oil | 15 machines | `oil_well.con.lua:44-94` |
| Quarry | 7 | 365 stone | 12 tools | `quarry.con.lua:44-83` |
| Rubber Farm | 23 | 365 rubber | 17 fertilizer | `rubber_farm.con.lua:41-102` |
| Sand Dredger | 9 | 365 sand | 15 machines | `sand_excavator.con.lua:44-92` |
| Sand Pit | 8 | 365 sand | 12 tools | `sand_pit.con.lua:44-84` |

- The bonus is drawn once per industry: **+50 % to +150 %**, rounded to 1 % (`industryutil.lua:394-405`). The Booster section shows it as "+X %" (`industry_util.tl:428-434`). With the **Boost Factor** parameter it is +50 %, +75 %, +100 %, +125 % or +150 % instead (`industryutil.lua:289-299`).
- The window shows the booster as active while its last batch lasts (3 months), or as soon as the stock holds a full batch (`industry_util.tl:55-91`).
- The batch does **not** shrink with the plots: a small mine needs as many tools as a big one (`industryutil.lua:227-229`).
- Both boosts multiply: production × workers factor × (1 + booster bonus) (`industry_util.tl:42-104`).

## The workers boost

Half of the workplaces (for example 10 of 20) must be filled by residents who **arrived by your passenger lines** in the last 2 years (`industry_productivity_util.tl:3`, `industry_productivity_util.tl:35-48`, `industry_productivity_util.tl:74`). The factor is random between ×1.5 and ×2.5, fixed per industry; a building can set its own (`industry_productivity_util.tl:58-72`). Assigned workers alone do not count. Details: [Workers and the workers boost](workers.html).

## Why is my industry not boosted?

1. **Not a raw industry**: factories have no booster rule, only the workers boost (`steel_mill.con.lua:61-70`).
2. **Batch not complete**: the stock must hold a full batch, e.g. 13 tools for a Coal Mine. Below 4 batches a year (52 tools) the boost stops between deliveries.
3. **Wrong cargo**: tools, machines or fertilizer depending on the industry (table above).
4. **Workers**: assigned is not enough; the Booster section counts arrivals ("12/10") (`industry_react_util.tl:617-654`). See [Workers and the workers boost](workers.html).

```tip scripts
**For a booster that never stops, deliver at least 4 full batches a year** (52 tools for a Coal Mine). Each batch keeps the bonus for 3 months.
```

## When does an unused industry close?

```diagram ind_closure
```

The check runs every 100 updates for each industry (`industries.script.tl:84-85`):

1. **Candidate**: no cargo **loaded** onto a vehicle and none **consumed** for **5 years** (counted from its construction if never) (`industries.script.tl:104-119`, `industries_config.res.lua:6`). Producing alone does not count.
2. **Chance**: a candidate is drawn at every check with a share of the yearly chance of the **Industry Closing Frequency** setting (table below), so that over a year it adds up to that chance (`industries.script.tl:84-85`, `industries.script.tl:120-131`).
3. **Countdown**: the notification **Industry Closing** appears, with 2 years (730 days) to go (`industries_config.res.lua:7`, `industry_close.script.tl:53-67`). Then the industry is removed with its own road pieces (`industries.script.tl:147-155`, `industries.script.tl:193-222`, `industry_util.tl:560-601`).
4. **Saved**: one load or consumption during the countdown cancels it (`industries.script.tl:134-137`). Accepting a **Supply Industry** or **Transport Workers** subsidy for it cancels the countdown while the subsidy runs (`subvention_util.tl:473-484`, `subvention_util.tl:478-483`). It does not reset the 5-year test (`industries.script.tl:119`): if nothing is loaded or consumed, the industry can be marked again later.

```tip scripts
**Got an Industry Closing notice? One pickup or one delivery during the 730 days cancels it.** Accepting a Supply Industry or Transport Workers subsidy for that industry cancels it while the subsidy runs, but keep loading something: the 5-year test is not reset.
```

| Industry Closing Frequency | Chance per year as a candidate | Half of the candidates marked after | Preset | Source |
|---|---|---|---|---|
| Never | 0 | never | Easy | `difficulty_util.tl:94` |
| Rarely (default) | 1.1 % | about 63 years | Normal | `difficulty_util.tl:121` |
| Sometimes | 2.2 % | about 32 years | Hard | `difficulty_util.tl:149` |
| Often | 4.4 % | about 16 years | – | `difficulty_util.tl:37` |
| Very Often | 8.8 % | about 8 years | Very Hard | `difficulty_util.tl:176` |

The chance is 0.011 a year × 0, 1, 2, 4 or 8 (`mod.script.tl:172`, `mod.script.tl:203-204`, `difficulty_util.tl:37`). Industries you own never close, and neither do industries with manual development; while closures are paused (in the base game, only during the tutorial) none starts and a running countdown is cancelled (`industries.script.tl:94-102`, `mission_sim.script.tl:814`, `mission_sim.script.tl:850`).

```engine
What counts as "loaded" and "consumed" (the logs itemsLoaded and itemsConsumed, e.g. whether booster cargo counts), the manualDevelopment flag, and why industries with a depot are left out (`industries.script.tl:140-146`) are engine-side. So is what the engine does with a booster rule that lost its input (Input Off).
```

## New industries

The engine adds new industries during the game. The notification is **New Industry Founded**: "A visionary entrepreneur smells an opportunity for profit and has founded {industry}." (`industry_spawn.script.tl:34-36`); its type label is **Industry Founded** (`industry_spawn.res.lua:6`). No game script picks the place, the type or the time, and none filters what the engine proposes.

What the scripts give the engine (`mod.script.tl:128-133`, `mod.script.tl:167-169`, `mod.script.tl:195-196`):

| Config value | Value | Meaning |
|---|---|---|
| spawnTargetTimeSpan | 50 × 365.25 standard days | named a "target time": 50 standard years of game time |
| spawnProbabilityExponent | 3.0 | exponent of the spawn chance (formula in the engine) |
| spawnIndustries | off in the map editor, on in a game | no new industries in the map editor |
| industryDensity | 1 × **Industry Target Density** | the target number of industries |
| maxNumberPerArea, absoluteMinimum | 0.8 per km² (0.64 on consoles), 24 | a limit per area and a minimum (their use is engine-side) |

**Industry Target Density** ("Set the target density of industries on the map."): 5 steps, ×2/3, ×5/6, ×1, ×1.2, ×1.5 (`difficulty_util.tl:55`, `difficulty_util.tl:85`).

- It is in the advanced settings, economy part (`advanced_settings.tl:287-291`), and is not part of the Easy … Very Hard presets (`difficulty_util.tl:90-199`).
- In the new game menu, **Industry Density** (the industries at the start, same 5 factors) sets **Industry Target Density** to the same step (`new_game_or_map_settings_page.tl:159-166`, `new_game_react_util.tl:288-296`). Change the target afterwards in the advanced settings if you want them to differ.
- **No setting turns it off**: the lowest step is ×2/3. Only the map editor has no new industries. Mods can.
- Speed: the target time is in standard days, like all game-time rules, so the calendar speed and a paused calendar should not slow it. Measured with the calendar paused: in 1,809 s of game time 3 new industries appeared, 760 s and 728 s apart, so a paused calendar does not stop them. Measured with the [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) over 3 games (about 500 industry births): new industries came about **730 s** of game time apart at every calendar speed (×4, ×1, ×0.5, ×0.25). That is about 45 calendar days at ×0.25 and 2 years at ×4.
- Prospect for Resources (below) uses the same engine call with a town, so a spawn "near a town" exists in the engine (`company.script.tl:202`). The tutorial uses it too (`tutorial_init.tl:23-24`).

```engine
The formula behind the 50 years and the exponent 3, how the target density is counted (per map area, per town?), which type is chosen, and where it goes (makeIndustrySpawnProposal) are engine-side. No script explains why several industries of one type can appear close together ("nine coal mines next to each other"), or why some appear on the far side of the map.
```

### Prospect for Resources

The company perk **Prospect for Resources** looks for a new industry of that resource near a town you pick: one try per month, with a chance rising from 20 % to 60 %, for 6 months (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`). If the resource has several industry types, they are tried in random order (`company.script.tl:185-206`). If all tries fail, the permit comes back (`company.script.tl:106-110`).

## Good to know

- Ship from every raw industry you want to grow: unshipped output blocks expansion, whatever the boosts.
- Put booster cargo on the biggest mines and farms: the batch costs the same, the bonus scales with the plots.
- Stocks do not decay: you can deliver booster cargo in advance, up to the stock limit (100).
- Boosts raise noise and pollution: a Coal Mine goes from 10 pollution to 20 with one boost and 30 with two (`coal_mine.con.lua:99-117`).
- Fewer new industries: set **Industry Target Density** to its lowest step in the advanced settings; it cannot be set to zero.
- At the default setting an unused industry rarely closes; at Very Often, keep loading something now and then.

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 5 years, not 10, and production does not count: only cargo loaded onto a vehicle or consumed. After the 5 years the industry is only a candidate: each year it is marked with a chance of 1.1 % (Rarely) to 8.8 % (Very Often). The countdown is 730 days, as stated. Booster cargo gives +50 % to +150 % per industry, in batches that last 3 months. New industries: no on/off setting, only Industry Target Density ×2/3 to ×1.5; none in the map editor.
result: differs
```
