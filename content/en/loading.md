---
title: Loading and unloading speed
summary: What makes a vehicle load fast or slow at a stop: the vehicle, the platform sections and the stock that gives or receives the cargo.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-14
fact: ×2 | specialised platform section
fact: ×0.25 | wrong section or train too long
fact: ×4 | best case: specialised platform and warehouse
---

The time a vehicle spends loading or unloading is its own load speed multiplied by two factors: one for the **platform**, one for the **stock** on the other side (warehouse, industry, town).

```diagram loading_factors
```

## 1. The vehicle

Each vehicle has a base load speed, shown in the vehicle store and in the vehicle window ("2.0x"). Everything below multiplies it.

## 2. The platform factor

A platform is not a row of modules for the game: it is a **list of sections, one per cargo class**, with the lengths of all modules of that class added up.

```diagram loading_sections
```

| Wagons… | Factor | Source |
|---|---|---|
| on a section of their class (bulk wagons, bulk section) | **×2** | `modular_station.script.lua:1042` |
| on a universal section | ×1 | `modular_station.script.lua:1042` |
| with no section of their class on the platform | **×0.25** | `cargo_react_util.tl:60` |
| beyond the platform length (train too long) | **×0.25** | `cargo_react_util.tl:61` |

- The factor is a **mix by share of the train**: if 3/4 of the wagons match and 1/4 do not, the factor is ¾ × 2 + ¼ × 0.25 ≈ ×1.56 (`cargo_react_util.tl:63-70`, the same split the game shows as "Partially Specialized Terminal").
- **Where** the wagons stand on the platform does not matter, only the summed lengths do (measured in game).
- Road: specialised truck terminals give ×2 (`modular_terminal.script.lua:2956`); the small street stops are always ×1 (`small_stops.script.lua:19`).
- Passenger platforms are ×1.

## 3. The stock factor

When cargo is unloaded, each unit goes to a receiver: a warehouse module, an industry or a town building. The receiver's stock has its own factor.

| Receiver | Factor | Source |
|---|---|---|
| **specialised** warehouse module (liquid, bulk, flatbed, goods) | **×2** | `modules.script.lua:120`, `warehouse.script.lua:297-314` |
| **universal** warehouse | ×1 | `warehouse.script.lua:272-285` |
| industry | ×1 | measured in game |

- Every warehouse module asks for ×2, but universal modules only add capacity to **one shared universal stock**, which is created with ×1. Only specialised modules get their own stock with ×2.
- The game's tooltip calls this factor "Specialized Warehouse: +100 %" (`cargo_react_util.tl:51-54`).
- During one unloading the game serves the receivers **in turn**, so the speed changes while the train unloads when part of the cargo goes to a warehouse and part to an industry (measured in game).

```engine
Which receiver gets each unit, and the final multiplication, happen in the engine. The factors above are the inputs the scripts give it; the result was checked with the values the engine exposes (Platform Details probe, October 2026).
```

## What the game shows

- The loading indicator is drawn as **boosted** above ×1.5 and as **slowed** below ×0.75 (`cargo_react_util.tl:119-122`).
- Hover it: the tooltip lists "Specialized Terminal", "Specializations Don't Match", "Terminal Too Short" and "Specialized Warehouse", each with its percentage (`cargo_react_util.tl:76-99`).

## Example

A train of 8 bulk wagons, 160 m long, unloading coal.

| Station | Platform | Receiver | Factor |
|---|---|---|---|
| universal platform 160 m | ×1 | steel mill | **×1** |
| bulk platform 160 m | ×2 | steel mill | **×2** |
| bulk platform 160 m | ×2 | specialised bulk warehouse | **×4** |
| bulk platform 160 m | ×2 | universal warehouse | **×2** |
| universal platform 120 m (train 40 m too long) | ¾ × 1 + ¼ × 0.25 ≈ ×0.81 | steel mill | **×0.81** |

## Good to know

- Stations inside an industry are always specialised to the cargo that industry needs (official wiki).
- Specialised warehouse modules also freeze the delivery timer of the cargo they store (official wiki); a universal warehouse does not.
- Platform Details shows both factors for every vehicle at a platform, and where the unloaded cargo went.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Specialized warehouses "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Specialised section ×2, universal ×1, no matching section ×0.25, beyond the platform ×0.25, mixed by share of the train; specialised warehouse module ×2, universal warehouse ×1.
result: refines
```
