---
title: Cargo income and delivery time
summary: What a delivery pays (straight-line distance, climb, company rank, subsidies) and what being late really costs.
domain: economy
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: 3.8 | the same income factor for every cargo
fact: +8 × climb | metres of climb added to the distance
fact: 100 % | paid even when the delivery is late
---

A delivery pays for **distance as the crow flies**, nothing else about the trip. Speed matters for a different reason: each cargo has a **time limit**, and late deliveries lower the town's **Delivery** rating, not your income.

```diagram income_formula
```

## The income formula

The whole formula is one short game script (`cargo_income.script.lua:10-13`):

1. **Income factor** of the cargo. Every base-game cargo uses the same function and the same prices (`initialPrice = 4`, `finalPrice = 3.2`), which gives **3.8 for all 36 cargos** (`cargotype.script.lua:7-13`, `coal.cargo.lua:21-22`). Coal pays exactly what goods pay over the same distance.
2. **Cargo Income** setting: 50 %, 75 %, 100 %, 125 % or 150 % (`difficulty_util.tl:38`, `mod.script.tl:211`). All four difficulty presets use 100 % (`difficulty_util.tl:97`).
3. **Distance**, see below.

The function receives the travel time but **does not use it** (`cargotype.script.lua:7-13`): a slow or late delivery pays the same.

## Distance: straight line plus climb

```diagram income_distance
```

- The distance is the **straight line in 3D** between the two points, not the length of your route (`cargo_income.script.lua:3-7`).
- When the height difference is positive, **8 × that height** is added (`cargo_income.script.lua:5`): 100 m of climb pays like 800 m more. In the other direction nothing is subtracted.
- So a winding line earns the same as a straight one, but you pay maintenance for every metre of track or road you built.

```engine
Which two points are compared (where the cargo entered your network, where it was delivered) and the sign of the height difference are decided by the engine. The official wiki says: "distances are measured as the crow flies between the source and the final destination".
```

## What else changes the amount

| What | Effect | Source |
|---|---|---|
| **Company rank** with the Inflation setting | rank 1: ×1, falling evenly to rank 15: ×0.9 (Low), **×0.75 (Normal)**, ×0.6 (High), ×0.5 (Very High); None: always ×1 | `company_progression_util.tl:25-40`, `difficulty_util.tl:50`, `mod.script.tl:694-697` |
| **Completed subsidy** | ×2 on the lines that delivered for the contract | `deliver_cargo.script.tl:463-469`, `deliver_cargo_town.script.tl:554-565` |
| **Late delivery** | no effect on the income | `cargotype.script.lua:7-13` |

- The rank multiplier applies to **every** cargo and passenger payment (`company_growth.script.tl:159-170`). The difficulty presets use Inflation Low (Easy), Normal (Medium), High (Hard), Very High (Very Hard) (`difficulty_util.tl:108`).
- The ×2 of subsidies applies only to the lines that delivered during the contract, for a limited time (official wiki, Subsidies).

## Passengers

Passengers use the same distance and a fixed income factor of about 3.61 (`cargotype.script.lua:50-53`), multiplied by **0.5 + the vehicle's ticket price factor** (`cargo_income.script.lua:14-17`). When a vehicle model does not set its comfort factor, the game sets the price factor to 0.3 for buses and trams, 0.9 for aircraft, 0.1 for ships and 0.5 for trains (`base_mod.lua:46-61`); for the other models it is an engine value, not visible in the scripts. A passenger subsidy also doubles the income on its line (`deliver_passengers.script.tl:284-298`).

## Delivery time limits

Every cargo has its own time limit (`timeToDeliverInSeconds` in each .cargo.lua, for example `meat.cargo.lua:30`, `coal.cargo.lua:30`). Fresh food has the shortest one, heavy raw materials five times longer:

```diagram delivery_times
```

- **Finances › Delivery Time** shows the limit of each cargo on your map; the cargo satisfaction layer colours the routes from green to red.
- A delivery counts as **delayed** when it arrives after its limit (`towns.script.tl:425`).
- Specialised warehouse modules **freeze** the timer of the cargo they store (official wiki, Warehouses).

```engine
The engine turns the base time into the time limit shown in Finances (the scripts read it with getAdjustedDeliveryTime) and decides when an item is late. Only the relative values above come from the cargo files.
```

## What being late costs: the Delivery rating

Late cargo is paid in full, but each town keeps a **Delivery** rating (`town_util.tl:505-519`):

1. The game counts the deliveries to the town over the **last half year**, and how many were late (at least 10 are assumed, so the first deliveries do not swing it).
2. On-time share → rating: below a lower limit the rating is 0, above an upper limit it is 1, linear in between. With the default sensitivity (**Normal**): **30 % on time → 0, 100 % → 1**, so 90 % on time gives 0.86.
3. The **Delivery Sensitivity** setting moves the limits (`difficulty_util.tl:47`). Off: always 1. Presets: Easy Low, Medium Normal, Hard High, Very Hard Very High (`difficulty_util.tl:113`).

```diagram delivery_rating
```

The town ratings slow down a town's growth; how they combine is explained on the coming Towns page.

## Example

The same coal delivery, 5 km apart as the crow flies.

| Situation | Paid |
|---|---|
| flat, any route length | **100 %** |
| 10 km apart | **200 %** |
| destination 100 m higher | **116 %** |
| delivered late | **100 %** (Delivery rating drops) |
| company rank 15, Inflation Normal | **75 %** |
| line of a completed subsidy | **200 %** |

## Good to know

- Since every cargo pays the same per kilometre, **choose cargos by volume, distance and time limit**, not by price.
- Time limits matter most for meat, fish, vegetables and beverages: short lines or warehouses that freeze the timer.
- Each unit delivered to a town building also gives that town experience (`town_growth.script.tl:642`, `town_growth_config.res.lua:5`).

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks), [Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Same factor 3.8 for all cargos; distance in 3D plus 8 × climb; company rank lowers income down to ×0.75 at rank 15 (Inflation Normal); ×2 after a subsidy; the time is not used for the income; Delivery rating from the on-time share of the last half year (Normal: 30 % → 0, 100 % → 1).
result: refines
```
