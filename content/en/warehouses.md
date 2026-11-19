---
title: Warehouses
summary: Universal or specialised modules, what each stock holds, pinning a cargo type, load speed, costs and pollution, and what a warehouse does not do.
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
game: 40444
fact: 500 | units of cargo per module, whatever its type
fact: ×2 | load speed at a specialised module, ×1 at a universal one
fact: 150,000 / 300,000 | price of a universal / specialised module
fact: 0 | income for cargo unloaded at a warehouse
---

A warehouse is an entrance and a set of **modules**. It stores cargo between two lines: one line unloads it, another loads it again. Stations reach it through their catchment area; towns and industries never take anything from it (official wiki).

## Universal or specialised modules

| Module | Stock | Holds | Load factor | Source |
|---|---|---|---|---|
| **Universal** | all universal modules share **one** stock | any cargo, mixed | ×1 | `warehouse.script.lua:272-295`, `modules.script.lua:49` |
| **Liquid**, **Bulk**, **Flatbed**, **Goods** | **one stock per module** | one cargo type at a time, of its class | ×2 | `warehouse.script.lua:296-314`, `modules.script.lua:120`, `modules.script.lua:165`, `modules.script.lua:247`, `modules.script.lua:296` |

- Every module adds **500** units (`modules.script.lua:49`, `modules.script.lua:120`). Five universal modules make one stock of 2,500; five liquid modules make five stocks of 500.
- Passengers are never stored (`warehouse.script.lua:279`, `warehouse.script.lua:304`).
- A specialised module takes one cargo type at a time: to store crude oil and fuel you need two liquid modules (official wiki).
- The ×2 of a specialised module multiplies with the platform factor: a bulk platform and a bulk module give ×4. Details: [Loading speed](loading.html).

## Universal or specialised?

1. **Many cargo types, small amounts**: universal. One shared stock, half the price and half the pollution.
2. **One cargo in large amounts** (coal, crude oil, logs): specialised. Vehicles unload and load twice as fast there, but you need one module per cargo type.
3. **Food and other cargo with a short delivery time**: specialised; the official wiki says these modules freeze the delivery timer (see below).
4. Both kinds can be mixed in one warehouse: the universal modules still form one stock, each specialised module its own.

## Does a warehouse speed up unloading?

- **Specialised module**: yes, ×2 for the cargo it takes. The loading tooltip of the vehicle shows "Specialized Warehouse: +100 %" (`cargo_react_util.tl:51-54`).
- **Universal module**: no. Its stock is created with ×1; the ×2 asked by the module is ignored (`warehouse.script.lua:284`, `warehouse.script.lua:288-289`).
- When part of the cargo goes to a warehouse and part to an industry, the vehicle serves them in turn, so the speed changes during one stop (measured in game, see [Loading speed](loading.html)).

## The Stocks section

- One row per stock: the cargo it takes, the amount, and the **Average Remaining Delivery Time** on hover (`entity_window_util.tl:408-410`).
- **Pin a cargo type**: on a specialised module, click a cargo icon. The game rebuilds the warehouse with that module reserved to this cargo (`entity_window_util.tl:339-367`, `warehouse.script.lua:308`). Removing or replacing the module clears its pin (`warehouse.script.lua:403-405`).
- **Discard All Cargo**: empties that row at once (`entity_window_util.tl:423-434`). The cargo is lost.
- Both buttons are missing only on a warehouse owned by another player; yours and warehouses with no owner have them (`warehouse_eow.script.tl:127-137`, `gui/entity_window/warehouse/warehouse.tl:38`, `entity_util.tl:83-86`).
- The **Statistics** chart shows **Incoming** (unloaded) and **Outgoing** (loaded) per year (`warehouse_eow.script.tl:159-160`).

## Costs and pollution

| | Universal module | Specialised module | Source |
|---|---|---|---|
| Price | 150,000 | 300,000 | `wh_universal.module.lua:18`, `wh_liquid.module.lua:22` |
| Upkeep per year | 25,000 | 50,000 | `wh_universal.module.lua:19`, `wh_liquid.module.lua:23` |
| Noise | 20 | 20 | `wh_universal.module.lua:33`, `wh_liquid.module.lua:37` |
| Pollution | 25 | 50 | `wh_universal.module.lua:34`, `wh_liquid.module.lua:38` |

- The warehouse adds its own pollution: **25**, or **50** as soon as one specialised module is built (`warehouse.script.lua:327`, `warehouse.script.lua:338-345`).
- The build menu has one entry per class and era (from 1900, 1940 and 1980) (`warehouses/warehouse.tl:3-5`); later eras show ×3 and ×9 (`warehouses/warehouse.tl:48`, `warehouses/warehouse.tl:75-76`), and warehouse upkeep also grows with the year. Details: [Costs, upkeep and loans](costs.html).
- Bulk, flatbed and goods modules cost the same as liquid ones (`wh_bulk.module.lua:22-23`, `wh_flatbed.module.lua:22-23`, `wh_goods.module.lua:18-19`).

```engine
The scripts give two emission levels, the second twice the first (`warehouse.script.lua:342-343`); the warehouse moves from the first to the second as its stocks fill up, full stocks = twice (`emissions.script.tl:237-249`). The price actually charged for modules is computed by the engine.
```

## What a warehouse does not do

- **It pays nothing.** Unloading at a warehouse earns no income; the item is paid once, when it reaches its consumer, for the straight distance from its source (measured in game, see [Cargo income](income.html)).
- **It does not feed towns or industries** near it: they only take cargo from vehicles (official wiki).
- **It is not a destination for the automatic line configuration**, which looks for producers and consumers only; but a stop next to a warehouse that stores a cargo leaves that cargo out of the Load list, so trains unload it there (see [Loading speed](loading.html)).
- **It needs no road.** The entrance snaps to a street, but cargo only moves through station catchment areas (`warehouse.script.lua:386-389`, official wiki). The warehouse window shows its catchment area (`gui/entity_window/warehouse/warehouse.tl:88-96`).

```engine
Where unloaded cargo goes, and whether a stored item's delivery timer stops, are decided by the engine. No script freezes the timer: the official wiki says specialised modules do, and a universal one does not.
```

## Good to know

- Check the Load list of every stop near a warehouse: what is not in it is unloaded into the warehouse, even halfway along the line.
- A full stock refuses more cargo unless the stop uses "Force Unload All Cargo On Arrival" ("Unload cargo even if stocks are full"); the cargo that does not fit is destroyed: the game gives the station as its destination, and a station never consumes cargo (measured in game, see [Loading speed](loading.html)).
- To keep a specialised module for one cargo, pin its cargo type in the Stocks section.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) lists, per station, the warehouses in reach with their stocks; [Platform Details](https://mod.io/g/transportfever3/m/platform-details) shows where the unloaded cargo went.

```check
official: "Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types." Specialised warehouses "freeze the cargo item's delivery timer" and "enable faster loading / unloading speeds". "In specialized warehouses, only one cargo type can be stored at a time for a given module." ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Universal modules form one shared stock with load factor ×1, each specialised module its own stock of 500 with ×2 and one cargo type. A specialised module costs twice as much (300,000, upkeep 50,000) and pollutes twice as much (50). The timer freeze is not in the scripts.
result: refines
```
