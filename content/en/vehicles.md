---
title: Vehicles: condition, age and load speed
summary: What the vehicle stats mean, how condition and age work, what depots and maintenance stations do, where price and running costs come from, and when to replace a vehicle.
domain: vehicles
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-16
fact: 5 | condition levels, from Very Bad to Very Good, 20 % each
fact: 20 % | condition that triggers the Vehicle Condition warning
fact: 6 years | of running costs: the price of a vehicle
fact: 4 to 16 | vehicles in the maintenance pool of one depot or maintenance station
---

Every vehicle has fixed stats (speed, capacity, load speed, price, running costs, lifespan) and two values that change: its **condition** and its **age**. Condition falls while it runs and is restored by maintenance. Age only grows.

## The stats in the vehicle store

- The store shows each stat as a bar. The bar compares the vehicle with the others of the same carrier and era, not with a fixed scale (`vehicle_util.tl:210-245`, `vehicle_util.tl:248-270`).
- For a train, the store shows the **highest** load speed of all its parts (`vehicle_store_util.tl:333`).
- A vehicle whose file sets no load speed, noise, pollution or comfort gets a value computed from its other stats (year, speed, power, weight, size) (`model_metadata_util.lua:395-417`, `vehicle_metadata_util.lua:233-256`). The computed load speed is rounded to 0.5 and never below 1 (`vehicle_metadata_util.lua:267-269`).

## Which vehicle loads fastest?

The load speed of the vehicle is only the first factor; platform and stock multiply it (see [Loading and unloading speed](loading.html)).

| Carrier | Load speed shown as full bar (latest era) | Source |
|---|---|---|
| Ships | 10 to 45 (from 2003) | `vehicle_util.tl:219-223` |
| Road vehicles, trams | 0.5 to 10 (from 1995) | `vehicle_util.tl:232-243` |
| Trains | 0.1 to 10 (from 1981) | `vehicle_util.tl:226-229` |
| Aircraft | 1 to 4 (from 1978) | `vehicle_util.tl:212-216` |

- Ships have by far the highest load speeds, aircraft the lowest scale.
- Compare vehicles of one carrier in the store with the load speed column; newer models usually sit higher on the bar.
- Every freight cargo has a load factor of 0.0625, passengers 1 (`coal.cargo.lua:29`, `passengers.cargo.lua:23`).

```engine
How the vehicle load speed, the cargo load factor and the platform and stock factors are combined into the actual loading time is computed by the engine. The scripts only give the inputs.
```

## Condition

| Condition | Level | Source |
|---|---|---|
| above 80 % | **Very Good** | `vehicle_util.tl:159-172` |
| 60–80 % | **Good** | `vehicle_util.tl:159-172` |
| 40–60 % | **Mediocre** | `vehicle_util.tl:159-172` |
| 20–40 % | **Bad** | `vehicle_util.tl:159-172` |
| up to 20 % | **Very Bad** | `vehicle_util.tl:159-172` |

- A train's condition is the **average** of all its wagons and locomotives (`vehicle_util.tl:285-295`).
- Below 80 % a vehicle starts to lose top speed, power and comfort, and to gain noise, pollution and running costs (`vehicle_store_util.tl:230-259`). The vehicle window lists these penalties under **Condition**.
- How strong these penalties are is set by **Vehicle Maintenance Effect** (None, Low, Medium, High, Very High); with None, condition has no effect (`mod.script.tl:241-245`, `vehicle_store_util.tl:211-228`). Details: [Costs, upkeep and loans](costs.html).
- At **20 %** or less you get the **Vehicle Condition** warning. It stays until the vehicle is back above **30 %** (`notifications.script.tl:310-318`).
- A cloned vehicle is a new purchase: condition 100 %, new purchase date (`manager_window.tl:8502-8506`).

```engine
How fast condition falls, how much a visit to a maintenance station restores, and the size of each penalty (getMaintenanceTopSpeedPenalty and the others) are engine values. Each vehicle model can also set its own top-speed penalty per level (`vehicle_store_util.tl:250-253`).
```

## Depots and maintenance stations

Vehicles are maintained by a depot or maintenance station nearby. Each one serves a limited number of vehicles: its **Maintenance Pool**.

| Building | Maintenance pool | Radius | Vehicles stored | Source |
|---|---|---|---|---|
| Train depot | 6 | 800 m | 5 | `rail_depot.script.lua:341-349` |
| Train maintenance station | 12 | 800 m | – | `rail_maint_station.script.lua:151-157` |
| Road depot, tram depot | 12 | 400 m | 10 / 8 | `road_depot.script.lua:189-198`, `tram_depot.script.lua:217-226` |
| Road maintenance station | 16 | 600 m | – | `road_maint_station.script.lua:234-240` |
| Ship depot | 8 | 1000 m | 5 | `water_depot.script.lua:370-379` |
| Ship maintenance station | 12 | 1400 m | – | `water_maint_station.script.lua:256-262` |
| Airfield or airport hangar | 16 | 550 m | 5 | `af_hangar.module.lua:272-280`, `ap_hangar.module.lua:455-463` |
| Heliport | 4 | 800 m | 5 | `heliport.script.lua:300-309` |

- The building window shows "used / pool" (for example 14 / 12) and the list of vehicles it serves, with their condition (`entity_window_util.tl:2010-2039`, `maintenance_station_eow.script.tl:188-215`).
- A fuller pool makes the building noisier and dirtier: emissions go up with the share of the pool in use (`emissions.script.tl:223-234`).
- A train maintenance station serves twice as many trains as a train depot: 12 against 6.
- Maintenance stations cannot buy or store vehicles, but their radius is often larger than the depot's: 600 m against 400 m on roads, 1400 m against 1000 m for ships. Only the road maintenance station also maintains trams.
- The official wiki suggests waypoints to send vehicles past a maintenance building.

```engine
Which station a vehicle is assigned to, what happens when more vehicles use a station than its pool, and the catchment radius used, are decided by the engine.
```

## Price and running costs

- Base-game vehicles have no fixed price: running costs come from speed and capacity, and the price is **6 years** of running costs (`model_metadata_util.lua:548-549`). Full formula: [Costs, upkeep and loans](costs.html).
- **Vehicle Costs** and **Vehicle Maintenance** scale both from 50 % to 150 % (`post_run_util.tl:54-81`).
- A vehicle in bad condition pays more running costs, on top of the base value (`vehicle_store_util.tl:256-259`).

## Age and lifespan

- Each model has a **lifespan** in years (`vehicle_metadata_util.lua:79-83`). The **Age** column of the line window shows the age; its tooltip shows the share of the lifetime used and the time left, or **Lifetime Reached** (`line_eow.script.tl:133-147`).
- For a train, the **oldest** part counts (`vehicle_util.tl:36-52`). One old wagon makes the whole train show as old.

```engine
What reaching the lifespan changes (for example faster loss of condition or lower sale value) is not in the scripts. The scripts only display age and lifespan.
```

## When should I replace old vehicles?

1. **Condition stays low** even with a maintenance station nearby: the vehicle loses speed and pays more running costs. Check the pool of the station first: it may be full.
2. **Lifetime Reached** in the Age tooltip: the model is past its planned life.
3. **A better model exists**: faster or bigger vehicles cost more to run, but they carry more (price follows speed × capacity).
4. Use **Replace Vehicles** in the line manager. It opens the store with a comparison against the current vehicle (`vehicle_store_window.tl:4893-4928`, `vehicle_store_window.tl:2611`).

## Good to know

- Build enough maintenance capacity: one train depot serves only 6 trains.
- With **Vehicle Maintenance Effect** on None, condition does not matter.
- **Send to Depot** sends a vehicle to the nearest reachable depot, not to the one where it was bought (official wiki).
- [Vehicle Comparison](https://mod.io/g/transportfever3/m/vehicle-comparison) helps compare models before replacing them.

```check
official: "This section shows how well the vehicle is maintained and how the maintenance state affects the vehicle properties." "Loading speed modifies a vehicle's base loading speed which can be seen in the vehicle window or in the vehicle store." ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles))
scripts: Five condition levels of 20 %; penalties to speed, power, comfort, emissions and running costs below 80 %, scaled by Vehicle Maintenance Effect; warning at 20 %, cleared above 30 %. Maintenance pool 4 to 16 vehicles per building. Price = 6 years of running costs. Age of a train = its oldest part. Missing load speeds are computed from the other stats, rounded to 0.5, at least 1.
result: refines
```
