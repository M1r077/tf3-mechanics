---
title: Game time and calendar
summary: Game speed and calendar speed are two different things. How long a day and a year last, what a slower or paused calendar changes, and what it does not.
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
game: 40425
fact: 4 s | one calendar day at calendar speed ×1, game speed 1x
fact: ≈ 24 min | one calendar year at the same speeds
fact: 0 ×0.25 ×0.5 ×1 ×2 ×4 | calendar speed steps
fact: 0 1x 2x 4x | game speed steps
---

The game has **two clocks**. The **game speed** (pause, 1x, 2x, 4x) makes everything run faster: vehicles, production, towns. The **calendar speed** only sets how fast the date moves. Almost every rule of the game counts in game time, not in calendar days.

## The two settings

| Setting | Steps | What it changes | Source |
|---|---|---|---|
| **Game speed** | Pause, 1x, 2x, 4x | how fast the whole simulation runs | `game_bar_widgets.tl:199-203` |
| **Calendar Speed** | Paused, ×0.25, ×0.5, ×1, ×2, ×4 | how many game seconds one day lasts | `game_bar_widgets.tl:321-335`, `game_bar_widgets.tl:351` |

- At calendar speed ×1 a day lasts **4 seconds** of game time (official wiki), so a month is about 2 minutes and a year about **24 minutes** at 1x. Measured with the [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard): 4.0 s per day at ×1, 1 s at ×4, 8 s at ×0.5, 16 s at ×0.25.
- ×4 makes the date run four times faster; **Paused** stops the date, the simulation goes on.
- 2x and 4x are a maximum: the game lowers them when the computer cannot keep up (`game.tl:636-642`). Measured: 2x gave 1.9x, 4x gave 3.6x on average.
- The time of day and the weather are a third, visual clock: by default they change on their own, whatever the calendar (`game_time_config.res.lua:5`, `weather_config.res.lua:5`).

## What follows game time, whatever the calendar

These are counted in game time, so a slower or paused calendar does not slow them down:

- **Production**: an industry's production time is a fixed share of a standard year (`industry_react_util.tl:51`). The industry window shows it in days of the current calendar (`industry_react_util.tl:23`): at ×0.25 the same rate shows a quarter of the days.
- **Loan payments**: one every standard month of game time, also with a paused calendar (`loan.script.tl:83-88`).
- **Subsidy deadlines** and the ×2 income bonus (`subvention_util.tl:290-292`).
- **Town reputation recovery** (`towns.script.tl:121-130`), **worker boosts** (`industry_productivity_util.tl:3`) and **industry closure** after years without service (`industries.script.tl:119-128`).
- **Delivery ratings** of towns, over the last half year (`town_util.tl:840`).
- **New industries**: with the calendar paused, 3 appeared in 1,809 s of game time, 760 s and 728 s apart, the same rhythm as with a running calendar (about 730 s). Measured with the [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard); see [Industries](industries.html).

With the calendar running, the game shows these durations in years, months and days of the current calendar speed (`util.tl:40-49`).

## What follows the calendar date

- **New vehicles, stations and buildings** appear by year (official wiki: "Different calendar speeds only affect the availability of vehicles and infrastructure").
- **Costs that grow with the year**: building upkeep, era variants, subsidy cash and loan amounts follow the date. See [Costs, upkeep and loans](costs.html).

## With the calendar paused

1. The date and so the year stay fixed: no new vehicles, and the year-based costs stay where they are.
2. Durations are shown in **minutes and seconds** instead of days (`util.tl:41-43`, `industry_react_util.tl:16-21`).
3. A loan shows its payment **per minute** instead of per year (`finances_loan_gui.tl:223-231`), and the custom loan card cannot be taken (`finances_loan_gui.tl:393`).
4. Production, payments, deadlines and reputation keep their game-time pace.

## Good to know

- Want more time to grow a network before new vehicles come? Lower the calendar speed: your income per game minute does not change.
- Production shown "per year" depends on the calendar speed; compare industries at the same speed.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) keeps readable finance charts with a paused calendar.

```engine
The length of the standard day, month and year (getDefaultDayDuration and the others) comes from the engine. The town script counts a month as 30 × 4 seconds (`towns.script.tl:121`), which fits the measured day of 4 seconds; a few other constants still assume a day of 2 seconds (`cargotype.script.lua:3`, `mod.script.tl:172`).
```

```check
official: "By default a day in the game lasts 4 seconds." "Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent." ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: Calendar speed ×0.25 to ×4 or paused, relative to the standard day; production, loans, subsidies, reputation and worker timers run on game time; a paused calendar shows durations in minutes, payments per minute and blocks new loans; measured: 4 s per day at ×1.
result: refines
```
