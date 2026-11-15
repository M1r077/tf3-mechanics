---
title: Costs, upkeep and loans
summary: What the cost settings change, which costs grow with the calendar year, how vehicle prices are computed, and what a loan really costs.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: ×6 | year factor on the upkeep of warehouses, harbours and airports by 2020
fact: 6 years | of running costs: the price of a vehicle
fact: once | a loan's interest rate is charged on the amount, not every year
fact: 4 | loans at the same time
---

The **Inflation** setting does not raise any cost: it only lowers your income as the company rank grows (see [Cargo income](income.html)). Costs grow with the **calendar year** instead, and four sliders scale them from the start.

```diagram cost_years
```

## The cost settings

| Setting | Values | Presets Easy · Medium · Hard · Very Hard | Source |
|---|---|---|---|
| **Vehicle Costs**, **Vehicle Maintenance** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:39`, `difficulty_util.tl:98-99`, `difficulty_util.tl:125-126` |
| **Infrastructure Costs**, **Infrastructure Upkeep** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:100-101`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Vehicle Maintenance Effect** | None ×0 · Low ×0.5 · Medium ×1 · High ×1.5 · Very High ×2 | Low · Medium · High · Very High | `difficulty_util.tl:42`, `difficulty_util.tl:103`, `difficulty_util.tl:185` |
| **Inflation** | income only, see [Cargo income](income.html) | Low · Normal · High · Very High | `difficulty_util.tl:50`, `mod.script.tl:694-697` |

- **Infrastructure Costs** scales the price of streets, tracks, bridges, tunnels, crossings, buildings and modules, and also terrain work (`post_run_util.tl:23-52`, `post_run_util.tl:83-120`, `construction.script.tl:31-35`, `mod.script.tl:223-226`). **Infrastructure Upkeep** scales their upkeep (`post_run_util.tl:43-45`, `post_run_util.tl:105-112`, `entity_window_util.tl:186`).
- **Vehicle Costs** and **Vehicle Maintenance** scale the purchase price and the running costs of every vehicle (`post_run_util.tl:54-81`).
- **Vehicle Maintenance Effect** sets how strongly a vehicle in bad condition loses speed, power and comfort and gains noise, pollution and running costs (`mod.script.tl:241-245`).

## What grows with the calendar year

- **Building upkeep**: ×1 in 1900, ×1.5 in 1920, ×2.2 in 1940, ×3.2 in 1960, ×4 in 1980, ×5 in 2000, ×6 in 2020 (`mod.script.tl:92-100`). The building window and the build menu apply it to every building marked to follow the year, and the build menu marks these: warehouses, airfields, airports and harbours (`entity_window_util.tl:186-193`, `construction_react_util.tl:1149`, `warehouse.tl:7`, `harbor_modular.tl:24`).
- **Modules** added to such a building are priced at the year the building was built, their upkeep at the current year (`construction.tl:3720-3727`, `construction.tl:4364-4367`).
- **Era variants**: depots, maintenance stations, warehouses, stations, harbours and airports have one variant per era, and each later variant costs **×3** (era B) or **×9** (era C) of the first (`rail_depot.con.lua:7`, `warehouse.tl:48`, `modular_station.con.lua:71`, `harbor_modular.tl:76`, `airport.tl:8`).
- **Subsidy cash**: ×1 in 1900 up to ×4 from 2000 (`finances_util.tl:87-90`). **Loan amounts**: ×0.4 in 1900 up to ×2.4 in 2020 (`loan_util.tl:7-10`).
- **Income** has no year factor at all (`cargo_income.script.lua:10-13`).

```engine
The upkeep that is actually charged, and whether streets, tracks and vehicles also follow the year table, is decided by the engine (getCostMultiplierForYear; the base config only sets chargeMaintenanceInterval = 60, `mod.script.tl:105`). The scripts only compute the values shown in the windows and the build menu, with the table above. No script sets the "follow the year" flag of the other buildings.
```

## Tracks, roads and buildings

Street and track files give the price and the yearly upkeep per metre; the build menu shows them per kilometre (`construction_react_util.tl:2463`, `construction_react_util.tl:2477-2485`). For most types the upkeep is **one sixth** of the build price:

| Type | Available from | Build per km | Upkeep per km and year | Source |
|---|---|---|---|---|
| Simple track | start | 60,000 | 10,000 | `simple.street_template.lua:9`, `simple.street_template.lua:33` |
| Standard track | 1930 | 180,000 | 30,000 | `standard.street_template.lua:11`, `standard.street_template.lua:35` |
| High-speed track | 1980 | 540,000 | 90,000 | `high_speed.street_template.lua:11`, `high_speed.street_template.lua:35` |
| Small old country road | start | 60,000 | 10,000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:58` |
| Large new town street | 1940 | 540,000 | 90,000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:91` |

- Catenary adds **30 %** of the track price; a bus lane 10 %, a tram track 20 %, an electric tram track 40 % of the street price (`mod.script.tl:24-28`).
- Raising terrain costs 4.5 per m³, lowering it 5.25 per m³, removing a field 200,000 (`mod.script.tl:20-22`, `mod.script.tl:33`).
- A building that sets no upkeep pays **one sixth of its price** per year (`construction.script.tl:25-27`).
- The base config sets a bulldoze refund factor of 0.75 and a refund time of 60 (`mod.script.tl:30-31`): removing what you just built gives most of the money back. The engine applies it.

Yearly upkeep written in the files, for the first variant (before 1940) and the later ones; warehouses also get the year factor above on top:

| Building | First variant | ×3 (from 1940) | ×9 (from 1980) | Source |
|---|---|---|---|---|
| Train depot, ship depot | 100,000 | 300,000 | 900,000 | `rail_depot.con.lua:34`, `water_depot.con.lua:32` |
| Road depot | 30,000 | 90,000 | 270,000 | `road_depot.con.lua:32` |
| Tram depot | 20,000 | 60,000 | 180,000 | `tram_depot.con.lua:34` |
| Train or ship maintenance station | 40,000 | 120,000 | 360,000 | `rail_maint_station.con.lua:32`, `water_maint_station.con.lua:32` |
| Road maintenance station | 10,000 | 30,000 | 90,000 | `road_maint_station.con.lua:32` |
| Universal warehouse | 25,000 | 75,000 | 225,000 | `warehouse.tl:48-52`, `warehouse.tl:75` |
| Specialised warehouse | 50,000 | 150,000 | 450,000 | `warehouse.tl:51`, `warehouse.tl:75` |

Each of these buildings costs **6 ×** its upkeep to build (`rail_depot.con.lua:35`, `warehouse.tl:76`): 2.7 M for a specialised warehouse of the last era, before the year factor.

- The first **airfield** (until 1950) already uses the ×3 of the second era: its test reads the end year of the variant instead of the start year (`airfield.tl:8`, `airfield_era_a.metacon.tl:3`).

## Vehicles

No base-game vehicle has a fixed price: the game computes it from the vehicle's speed and capacity when it loads the model (`model_metadata_util.lua:488-552`):

1. **Running costs per year** = about 675 × average speed (m/s) × capacity / 4 (`model_metadata_util.lua:499-518`). The 675 comes from the average income per km, reduced to leave room for empty return trips, the purchase and the falling ticket prices (`model_metadata_util.lua:500-508`).
2. The **average speed** is below the top speed: for road vehicles (top speed in km/h)^0.78 + 4, for trains ^0.86 + 10, ships 65 % of the top speed (`model_metadata_util.lua:448-474`).
3. **Trains**: a wagon counts half its capacity; a locomotive also counts power ÷ top speed (km/h) × 12.5 as capacity, halved too (`model_metadata_util.lua:511-512`, `model_metadata_util.lua:526-540`). A strong, slow locomotive is expensive.
4. **Price** = **6 ×** the yearly running costs (`model_metadata_util.lua:548-549`).

Example at 100 %: a 35 km/h bus for 48 passengers runs at about 45,000 per year and costs about 270,000.

- The condition of a vehicle uses five levels (100–80 %, then every 20 %) (`vehicle_store_util.tl:231-234`); at **20 %** the game warns about it until it is back above 30 % (`notifications.script.tl:310-318`).

```engine
How fast a vehicle's condition falls, how much running costs rise with it, and whether vehicle prices change with the year are engine values (getMaintenanceRunningCostPenalty and the other penalties); the scripts only scale them with Vehicle Maintenance Effect.
```

## Loans

```diagram loan_interest
```

| Kind | Amount around 1960 (×0.4 in 1900, ×2.4 in 2020) | Term | Rate | Source |
|---|---|---|---|---|
| Small | 5–10 M | 1–5 years | 3–5 % | `loan_util.tl:12-22` |
| Medium | 15–25 M | 3–8 years | 5–8 % | `loan_util.tl:24-34` |
| Large | 30–50 M | 5–12 years | 8–10 % | `loan_util.tl:36-46` |
| Extra large | 40–60 M | 10–24 years | 10–12 % | `loan_util.tl:48-58` |

- The card calls it **Annual Interest Rate**, but the rate is applied **once** to the amount: the total interest is amount × rate, whatever the term. It is paid in equal parts every month with the principal (`loan_util.tl:102-111`, `loan_util.tl:126-136`, `loan.script.tl:83-99`). A long loan is therefore cheaper per year than a short one with the same rate.
- **Repay** pays only the rest of the principal: the remaining interest is dropped (`loan.script.tl:171-190`). The button needs that amount in cash (`finances_loan_gui.tl:284-286`).
- The rates do **not** depend on the difficulty: each kind has its own fixed range (`loan_util.tl:12-58`).
- At most **4 loans** at once (`loan_util.tl:4`, `loan.script.tl:134`). An offer is replaced after half a year; the slot of a loan you took stays empty for 4 to 8 months (`loan.script.tl:61-76`, `loan.script.tl:150`).
- At the start of a game each of the four slots gets the values of a random kind, so the first "small" offer can be a large loan; once an offer is renewed, each slot offers its own kind (`loan_util.tl:60-74`, `loan.script.tl:63-75`).

```tip scripts
**Take the longest loan, then repay early.** The total interest is the same for every term, the monthly payments are smaller, and Repay drops the interest that is left.
```

## Good to know

- Take the **longest** loan you can: the interest is the same total, spread over more months, and you can repay early without paying the rest.
- Buildings with era variants cost ×3 and ×9 in later eras, and their upkeep keeps growing with the year: a specialised warehouse of the last era is a large fixed cost.
- A fast vehicle with a large capacity costs more to run, but it also carries more: price and running costs follow speed × capacity, like the income it can earn.

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: The rate of a loan depends only on its kind (3–12 %), not on the difficulty, and it is charged once on the amount, spread over the months of the term; repaying early drops the remaining interest. Inflation changes only income; building upkeep follows the year (×1 to ×6); vehicle price = 6 × yearly running costs, both from speed and capacity.
result: differs
```
