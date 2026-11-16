---
title: Subsidies: offers, deadlines and rewards
summary: The four contract types, what really completes them, what you get and what you risk, and how often new offers come.
domain: subsidies
official: gamemanual:management:subsidies
status: verified
updated: 2026-11-15
fact: 4 | contract types in a free game
fact: 5 | accepted contracts at most at the same time
fact: ×2 | income for 5 years on the lines that delivered
fact: 0 | penalty for declining an offer
---

A subsidy is a contract: an industry or a town offers a task, you get something when you accept, more when you complete it in time, and you pay back the advance plus a penalty when you miss the deadline. Declining an offer, or letting it expire, costs nothing.

```diagram subsidy_life
```

## The four contract types

```diagram subsidy_types
```

| Contract | Target | What completes it | Source |
|---|---|---|---|
| **Supply Industry** | an industry that has never produced anything | the required number of deliveries to it, **any of its input cargos** | `deliver_cargo.script.tl:54-61`, `deliver_cargo.script.tl:230-234`, `deliver_cargo.script.tl:470-479` |
| **Supply Town** | a cargo the town asks for and does not get at all | the required number of units **of that cargo** delivered to buildings of the town | `deliver_cargo_town.script.tl:566-581` |
| **Connect Towns** | two towns | **one** passenger starting a trip between the two towns on a line that stops in both | `deliver_passengers.script.tl:263-280`, `subvention_util.tl:561-592` |
| **Transport Workers** | an industry that already ships or receives cargo, not boosted yet | its workers boost becomes active (half of its workplaces) | `deliver_workers.script.tl:121-131`, `deliver_workers.script.tl:152-156` |

- Every new offer picks one of the types that can currently spawn, with equal chances (`subventions.script.tl:147-169`).
- **Supply Industry** and **Supply Town** count deliveries, not trips: each paid unit that arrives at the target adds 1. Transfers are allowed (`deliver_cargo.script.tl:470-479`).
- **Connect Towns** needs no number of passengers: the first passenger who boards your line between the two towns completes it. "Transfer-free" means that this leg runs on a single line serving both towns. No offer is made if a line already carries passengers between them (`deliver_passengers.script.tl:72-78`).
- Close towns are much more likely: the pair weight falls from 1 at 1 km or less to 0.01 at 20 km, to the power of 7 (`deliver_passengers.script.tl:175-191`).
- **Supply Town** prefers cargos that are already produced somewhere on the map: 16 times more likely than the others (`deliver_cargo_town.script.tl:277-280`).
- The amount to deliver depends on the **Subsidies Risk** setting:

| Subsidies Risk | Supply Industry | Supply Town (at most the town's demand) | Source |
|---|---|---|---|
| None | 10–50 | 10–30 | `deliver_cargo.script.tl:100-114`, `deliver_cargo_town.script.tl:165-188` |
| Fair | 50–100 | 30–100 | |
| Risky | 75–150 | 35–125 | |
| Very Risky | 150–300 | 45–150 | |

## What is a transfer-free connection?

The **Connect Towns** card asks: "Create a transfer-free connection between {fromTownName} and {toTownName} and transport passengers between the two towns." (`deliver_passengers.script.tl:14`).

- **One line with a stop in each town.** The game goes through the stops of the line and takes the town of each one; the line counts when at least one stop is in each of the two towns. Other stops, their order and the vehicle type (bus, tram, train, ship, aircraft) do not matter (`subvention_util.tl:561-592`).
- **One passenger completes it**: the first passenger who rides that line from a stop in one town to a stop in the other, in either direction (`deliver_passengers.script.tl:263-280`, `deliver_passengers.script.tl:210-218`). The check only looks at this ride, so changing lines before or after it should not matter.
- **The town of a stop** is the town of the first station of its station group (`town_util.tl:1844-1873`). Which town a station belongs to is decided by the engine.
- **No offer** when a line already has a stop loading passengers in each town and a vehicle that takes passengers (`deliver_passengers.script.tl:72-78`). A freight-only line between them does not block the offer.
- The contract ends as **Subsidy Removed** when one of the two towns, or the line that completed it, changes in a way the game counts as a new version (`deliver_passengers.script.tl:232-240`).

```engine
Which town a station belongs to (stationSystem.getTown), when exactly a passenger "starts using" a line (OnStartedLineUsage), and which edits of a line count as a new version are engine-side. Whether a line edit after completion ends the 2x Income effect was not tested.
```

## Rewards and penalties

Every contract keeps three lists, shown on its card as **On Acceptance**, **On Fulfillment** and **On Failure** (`subvention_util.tl:449-471`). On failure, the advance is always paid back, plus one extra penalty (`deliver_cargo.script.tl:134-136`).

| Contract | On Acceptance | On Fulfillment | On Failure | Source |
|---|---|---|---|---|
| Supply Industry | cash | only the **2x Income** effect | advance back + fine | `deliver_cargo.script.tl:120-136` |
| Supply Town | cash **or** reputation in the town | town experience **or** cash, plus 2x Income | advance back + reputation loss **or** fine | `deliver_cargo_town.script.tl:194-229` |
| Connect Towns | cash, more for distant towns | town experience in **both** towns, plus 2x Income | advance back + reputation loss in **both** towns | `deliver_passengers.script.tl:105-119` |
| Transport Workers | cash | cash | advance back + fine | `deliver_workers.script.tl:92-116` |

- **Cash**, before the year scaling: advance 1.5 M to 3.75 M × the risk factor (None ×2, Fair ×1, Risky ×0.75, Very Risky ×0.5); fine 3 M to 6 M; completion payment 3.75 M to 11.25 M (`deliver_cargo.script.tl:120-128`, `deliver_workers.script.tl:102-104`).
- Money grows with the **calendar year**, not with the Inflation setting: ×1 in 1900, rising evenly to ×4 in 2000 and later, rounded up to 10,000 (`finances_util.tl:87-90`). It is booked as **Subsidies** in the finances (`subvention_util.tl:126-135`).
- **Supply Town** gives cash rewards and fines only while your bank account is below 100 M; above it, only 1 offer in 10 still can (`deliver_cargo_town.script.tl:206-217`).
- **Town experience** is a share of the town's current level: 20 % to 100 % of the XP between its level and the next (`deliver_cargo_town.script.tl:216`, `town_growth.script.tl:605-608`). For **Connect Towns** it is multiplied by the distance factor, 0.3 at 1 km up to 3.0 at 20 km: far towns can gain several levels (`deliver_passengers.script.tl:94-96`, `deliver_passengers.script.tl:116-118`).
- **Reputation** lost after a failure shows in the town's Reputation rating as **Failed Subsidy** (`towns.script.tl:313-334`). Reputation won on acceptance only removes existing penalties, it cannot go above full (`town_util.tl:1644-1647`).

## The 2x Income effect

- It lasts **60 months** (5 years) after the contract is fulfilled (`subvention_util.tl:286`, `subvention_util.tl:292`).
- **Supply Industry**: deliveries to that industry, on the lines that delivered to it during the contract (`deliver_cargo.script.tl:463-469`).
- **Supply Town**: deliveries to any building of that town, **any cargo**, on the lines that delivered the contract cargo (`deliver_cargo_town.script.tl:554-565`).
- **Connect Towns**: passengers between the two towns, on **one** direct line only: the last direct line a passenger between them boarded. This keeps updating after the contract, so with two direct lines the ×2 can move from one to the other (`deliver_passengers.script.tl:263-296`).
- **Transport Workers** has no income effect (`deliver_workers.script.tl:90`).
- For Supply Industry and Supply Town, a line that only started delivering after the contract was fulfilled gets nothing: the list of lines is filled during the contract only.
- Two contracts never double the same payment twice: when several match, only the last answer is used (`subventions.script.tl:570-583`).

```tip scripts
**Want the doubled income of Supply Industry or Supply Town on several lines? Have all of them deliver before the contract is fulfilled.** A line added afterwards gets nothing. Connect Towns doubles one line only, the last direct one passengers boarded: keep a single direct line between the two towns.
```

```engine
How the ×2 of a subsidy combines with the company rank multiplier (Inflation setting) is decided by the engine: both scripts only return a multiplier for each payment. What one payment entry is (presumably one cargo unit or one passenger) is also decided by the engine.
```

## Deadlines

The deadline starts when you accept. It is longer when the cargo has to travel far and shorter with a higher risk (risk factor None ×2, Fair ×1, Risky ×0.75, Very Risky ×0.5, or ×0.625 for the passenger and worker contracts):

| Contract | Deadline in months | Distance used | Source |
|---|---|---|---|
| Supply Industry, Supply Town | (6 + 32 × E) × risk factor | to the nearest industry that produces the cargo | `deliver_cargo.script.tl:116-117` |
| Connect Towns | (9 + 4 × E) × risk factor | between the two towns | `deliver_passengers.script.tl:98-99` |
| Transport Workers | (6 + 15 × E) × risk factor × era factor (×1.75 before 1940, ×1.25 before 1980) | to the nearest town | `deliver_workers.script.tl:75-87` |

E is the time a train at the top speed of the era (120 km/h from 1900 up to 300 km/h from 1981) needs for that distance, rounded up, at least 1 (`subvention_util.tl:486-489`, `vehicle_util.tl:225-230`).

- An offer that is not accepted disappears after about **6 months** (150 to 210 days), without any penalty (`subvention_util.tl:284`, `subvention_util.tl:290`).
- While a **Supply Industry** or **Transport Workers** contract runs, the target industry cannot close: a planned closure is cancelled (`subvention_util.tl:473-484`).
- If the target disappears or is rebuilt during the contract, the game shows **Subsidy Removed**, but the failure penalties are applied as for a missed deadline (`subventions.script.tl:172-190`, `subvention_util.tl:406-412`).
- There is no button to cancel an accepted contract.

```engine
How long a game month is, and so the real length of the deadlines, is set by the engine (getDefaultMonthDuration). The formulas above are in months of the game calendar.
```

## How often new offers come

- **Subsidies Availability**: Rarely, Sometimes (the default), Often, Very Often give one new offer every 12, 6, 3 or 1 months; **Never** turns subsidies off (`subvention_util.tl:13-38`, `mod.script.tl:247-248`).
- The interval grows with the **company rank**: ×1 at rank 1 up to ×2 at rank 15 (`subvention_util.tl:19-22`).
- **Declining** an offer halves the next interval; accepting or a new offer resets it (`subventions.script.tl:429`, `subventions.script.tl:395`, `subventions.script.tl:118`).
- No new offer while **5 contracts** are accepted and running (`subventions.script.tl:23`, `subventions.script.tl:256-262`). The first offer comes after half a month.
- The same target (industry, town and cargo, pair of towns) is offered **only once per game**, even after a missed or failed contract (`subventions.script.tl:107-113`, `subventions.script.tl:186`).
- Difficulty presets, availability / risk (`difficulty_util.tl:104-105`, `difficulty_util.tl:132-133`, `difficulty_util.tl:159-160`, `difficulty_util.tl:186-187`): Easy Often / None, Medium Sometimes / Fair, Hard Rarely / Risky, **Very Hard Never**: no subsidies at all.
- The town rating check that would allow subsidies only in towns rated Very Good exists but is switched off (`town_util.tl:1574-1580`, `deliver_cargo_town.script.tl:272-275`).

## Good to know

- Accept freely when the target is easy: declining or ignoring has no cost, but **failing** costs the advance back plus a fine that can be larger than the advance.
- For **Supply Town** and **Supply Industry**, start delivering with every line you want to benefit: only the lines that delivered during the contract get the 2x Income for 5 years.
- **Connect Towns** with far-apart towns gives the most town experience, and needs a single passenger.
- **Supply Industry** pays nothing more on completion: its reward is the 2x Income alone.

```check
official: "Accept an offer to begin the contract; declining it has no penalty." "Possible rewards include town experience, an additional payment, or a limited-time 2x income effect on eligible transport lines." "The upfront reward is reversed, and an additional fine or loss of town reputation may apply." ([Subsidies](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:subsidies))
scripts: Four types; one passenger completes Connect Towns; the 2x lasts 60 months on the lines that delivered during the contract; Supply Industry gives only the 2x; money scaled by the year (×1 to ×4); one new offer every 1–12 months, longer at high company rank; at most 5 accepted; each target offered once per game.
result: refines
```
