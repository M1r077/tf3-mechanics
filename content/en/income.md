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
The engine chooses the two points and passes them to the script. Measured in game (see below): they are the **source** of the cargo (the industry or town building that produced it) and the **consumer** that receives it, as the official wiki says ("between the source and the final destination").
```

## Cargo that changes line

When an item travels on several lines, for example ship → warehouse → train, the game still pays it **only once**:

```diagram income_split
```

1. Unloading at a warehouse or a transfer station pays **nothing**. Out of about 17,000 measured payments, only 43 went to a stock that was not a consumer.
2. When the last vehicle delivers to the consumer, the item is paid with the formula above, for the straight line **from the source to the consumer**. The legs and the real route do not count, so a detour through a warehouse earns nothing more.
3. That money is split between the lines of the chain, **in proportion to the straight-line length of each leg**: from one pickup point to the next, and from the last pickup point to the consumer. The climb bonus does not count in this split.
4. The delivering vehicle first holds the whole amount, with one share per leg. It is booked a few seconds of game time later (median about 6 s), each line and each vehicle getting its own share. A line's balance therefore moves shortly after the delivery, not at the warehouse.

So a short feeder line to a warehouse earns little, even though it does all the collecting; the long leg earns most. Every line still shows its real share in its own balance.

```engine
The scripts only compute the total (`economy/cargo_income.script.lua`); the split is done by the engine and is not visible in the scripts. The rules above were measured with a read-only test mod: about 1,700 payments of items with 2 or 3 legs, and the account changes of every line and vehicle involved. In 769 clean cases (one item, one payment) the split matched the leg lengths to within 1 % every time; a split with the climb bonus matched in only 59 % of them, an equal split in none.
```

## What else changes the amount

| What | Effect | Source |
|---|---|---|
| **Company rank** with the Inflation setting | rank 1: ×1, falling evenly to rank 15: ×0.9 (Low), **×0.75 (Normal)**, ×0.6 (High), ×0.5 (Very High); None: always ×1 | `company_progression_util.tl:25-40`, `difficulty_util.tl:50`, `mod.script.tl:694-697` |
| **Completed subsidy** | ×2 for deliveries to the contract's industry or town, on the lines that delivered for the contract | `deliver_cargo.script.tl:463-469`, `deliver_cargo_town.script.tl:554-565` |
| **Late delivery** | no effect on the income | `cargotype.script.lua:7-13` |

- The rank multiplier applies to **every** cargo and passenger payment (`company_growth.script.tl:159-170`). The difficulty presets use Inflation Low (Easy), Normal (Medium), High (Hard), Very High (Very Hard) (`difficulty_util.tl:108`).
- The ×2 of subsidies applies only to the lines that delivered during the contract, for a limited time (official wiki, Subsidies).

## Passengers

Passengers use the same distance and a fixed income factor of about 3.61 (`cargotype.script.lua:50-53`), multiplied by **0.5 + the vehicle's ticket price factor** (`cargo_income.script.lua:14-17`). When a vehicle model does not set its comfort factor, the game sets the price factor to 0.3 for buses and trams, 0.9 for aircraft, 0.1 for ships and 0.5 for trains (`base_mod.lua:46-61`); for the other models it is an engine value, not visible in the scripts. A passenger subsidy doubles only the passengers travelling between its two towns, on its one line (`deliver_passengers.script.tl:292-296`).

## Delivery time limits

Every cargo has its own time limit (`meat.cargo.lua:30`, `coal.cargo.lua:30`). Fresh food has the shortest one, heavy raw materials five times longer:

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

Delivery is one of the six ratings whose lowest sets the town's growth rate: one Very Poor rating stops the town (see [Town growth](towns.html)).

## Example

The same coal delivery, 5 km apart as the crow flies.

| Situation | Paid |
|---|---|
| flat, any route length | **100 %** |
| 10 km apart | **200 %** |
| destination 100 m higher | **116 %** |
| delivered late | **100 %** (Delivery rating drops) |
| company rank 15, Inflation Normal | **75 %** |
| delivery covered by a completed subsidy | **200 %** |

## Good to know

- Since every cargo pays the same per kilometre, **choose cargos by volume, distance and time limit**, not by price.
- Time limits matter most for meat, fish, vegetables and beverages: short lines or warehouses that freeze the timer.
- Each unit delivered to a town building also gives that town experience (`town_growth.script.tl:642`, `town_growth_config.res.lua:5`).

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks), [Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Same factor 3.8 for all cargos; distance in 3D plus 8 × climb; company rank lowers income down to ×0.75 at rank 15 (Inflation Normal); ×2 after a subsidy; the time is not used for the income; measured in game: an item that changes line is paid once, at the consumer, and split between the lines by leg length; Delivery rating from the on-time share of the last half year (Normal: 30 % → 0, 100 % → 1).
result: refines
```
