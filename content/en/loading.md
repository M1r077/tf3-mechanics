---
title: Loading and unloading speed
summary: What makes a vehicle load fast or slow at a stop: the vehicle, the platform sections and the stock that gives or receives the cargo.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-15
game: 40425
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
| with no section of their class on the platform | **×0.25** (constant of the loading tooltip; the factor itself is applied by the engine) | `cargo_react_util.tl:60` |
| beyond the platform length (train too long) | **×0.25** (constant of the loading tooltip; the factor itself is applied by the engine) | `cargo_react_util.tl:61` |

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
Which receiver gets each unit, and the final multiplication, happen in the engine. The factors above are the inputs the scripts give it; the result was checked with the values the engine exposes ([Platform Details](https://mod.io/g/transportfever3/m/platform-details) probe, October 2026).
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

## Where the cargo is unloaded

Each stop of a line has a **Load** list, in the stop's "Cargo Filter" window. At the stop the vehicle keeps on board the cargo in that list; the rest is unloaded into any stock in the catchment area that takes it, a warehouse included (measured in game).

- That is how a train ends up emptying itself into a warehouse halfway along its line. In game: at a stop next to a warehouse, with only plastic in its list, the tools on board went into the warehouse, although it was nearly full.
- A passenger platform has no freight transfer: freight stays on board there (measured in game).
- To keep the cargo on board, add it to the Load list of that stop.

```tip
**Cargo disappears at a stop next to a warehouse? Add it to that stop's Load list.** Everything not in the list is unloaded into any stock in reach, and a warehouse pays nothing for it.
```

| Option in "Cargo Filter" | What it does | Source |
|---|---|---|
| "Force Unload All Cargo On Arrival" | tooltip: "Unload cargo even if stocks are full"; what happens to the cargo that does not fit is decided by the engine. Off for a new stop. | `cargofilter_window.tl:757`, `line_util.tl:476` |
| "Destroy Cargo On Arrival When Config Changes" | unloads or destroys the cargo on board when cargo for another load configuration of the vehicle is waiting at this stop; which of the two is up to the engine | `cargofilter_window.tl:767` |
| "Replace with Newer Cargo if Available" | destroys cargo that came back to the stop where it was loaded, when newer cargo of the same type is waiting | `cargofilter_window.tl:778` |

- With the first option off, the cargo icon shows "≤" and the tooltip "Unload Only if Stocks Have Capacity" (`cargofilter_window.tl:124`, `cargofilter_window.tl:158`).

## Several cargos on one line

- A stop's Load list is a yes/no per cargo type, with **no order**: the player cannot set which cargo loads first. The icons are just drawn in the game's cargo order (`line_util.tl:471-475`, `line_util.tl:510`, `cargofilter_window.tl:533-535`).
- A wagon or truck that takes several cargos has, per compartment, several **load configurations**; the compartment's capacity is the largest of them, not their sum (`model_metadata_util.lua:682-733`, `vehicle_metadata_util.lua:27-37`). So it carries one of them at a time.
- New vehicles have the automatic choice of configuration switched on for every compartment (`vehicle_react_util.tl:339`), and the game has no window to choose the cargo of a vehicle by hand.
- Passengers and freight can share a line: the scripts never refuse freight at a stop because it also takes passengers (`line_util.tl:1381-1386`). Freight is only dropped from a stop whose terminal cannot load or unload cargo (`line_util.tl:554-559`).
- With several cargos, **Full Load (Any)** and **Full Load (All)** behave differently: see [Departure settings: full load, Fill Level and stop times](departure.html).
- When the configuration does not fit, the line shows **Some Cargo Type Configurations of This Line Are Clashing**, for example "No vehicle on the line can transport some of the cargo configured to be loaded." (`line_warning.script.tl:10-36`).

```engine
In which order several cargos are loaded, how a shared stock is split between waiting vehicles, and how a vehicle picks its load configuration are decided by the engine.
```

## The automatic configuration

As long as nobody has saved a change in a stop's "Cargo Filter" window, which switches it off for good on that line (`line_util.tl:495-498`, `cargofilter_window.tl:438`), the game fills the Load lists itself each time the line is created, a stop is added or removed, the stops are reordered, or a waypoint is added (`manager_window.tl:6712`, `:6786`, `:6845`, `:6879`, `:6963`). Moving a stop to another station or platform, and removing or moving a waypoint, do not run it (`manager_window.tl:6851-6868`, `manager_window.tl:6968-6992`).

- It starts again from empty lists, with passengers at passenger stations (`line_util.tl:542-588`).
- It looks for producers and consumers among industries and town buildings only: warehouses do not count (`cargo_util.tl:518-526`).
- It puts a cargo in a stop's Load list when the cargo is needed further on and nothing at the stop takes it. A warehouse counts as taking everything it stores (`line_util.tl:676-693`): at a stop next to a warehouse that stores the cargo, the cargo is left out of the list, and the train unloads it there.
- Once a filter has been changed by hand, the line is marked as custom (`cargofilter_window.tl:438`) and the automatic configuration never touches it again, even when stops are added later (`line_util.tl:496`).

```engine
The scripts only write the Load lists; the unloading itself is done by the engine. The rule above (what is not in the list is unloaded into any stock that takes it) was observed in game with [Platform Details](https://mod.io/g/transportfever3/m/platform-details), November 2026.
```

## Good to know

- Stations inside an industry are always specialised to the cargo that industry needs (official wiki).
- Specialised warehouse modules also freeze the delivery timer of the cargo they store (official wiki); a universal warehouse does not.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) shows both factors for every vehicle at a platform, and where the unloaded cargo went.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Specialized warehouses "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Specialised section ×2, universal ×1, no matching section ×0.25, beyond the platform ×0.25, mixed by share of the train; specialised warehouse module ×2, universal warehouse ×1.
result: refines
```
