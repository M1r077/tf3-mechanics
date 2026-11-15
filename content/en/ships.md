---
title: Ships and ports
summary: Small and large ships, which port takes which, port terminals and costs, and the list of all ships with their cargo, capacity and speed.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
fact: 2 | ship sizes: small and large
fact: 1, 2, 4 | terminals per port
fact: 27 | ships in the base game
fact: ×9 | price and upkeep of the 1990 port variant
---

Every ship is **small** or **large**. A large ship can only dock at a **large port**; a small ship docks at both. The in-game guide says it too: "Large ships can only dock at large harbors."

```diagram ship_access
```

## Small and large ports

- Two ports in the build menu: **Small Passenger/Cargo Port** and **Large Passenger/Cargo Port**. Both take passengers and every cargo (`harbor_modular.tl:92`, `harbor_modular.tl:122`).
- The small port is built from small piers, which accept only small ships (`small_pier.module.lua:7`). The large port uses medium piers, which accept both sizes (`medium_pier.module.lua:6`, `harbor_modular.script.lua:35-39`).
- **Terminals**: 1, 2 or 4, chosen when you build (`harbor_modular.tl:16`, `harbor_modular.script.lua:33`).
- A pier terminal holds 100 waiting passengers on a small pier and 50 on a medium pier (`modules.script.lua:872`, `modules.script.lua:1004`).
- Ports must be placed along a coast, on navigable water (`harbor_modular.tl:29`).
- Each ship sets its own size in its vehicle file; the game turns it into the small or large ship mode (`model_metadata_util.lua:1411-1412`).

## Costs

There is one port variant per era: 1900, 1950 and 1990 (`harbor_modular.tl:71-73`). Price and upkeep are multiplied by 3 for a variant from 1940 and by 9 for one from 1980 (`harbor_modular.tl:76`):

| Port | Price (first variant) | Upkeep per year (first variant) | Source |
|---|---|---|---|
| Small port | 144,000 – 444,000 | 24,000 – 74,000 | `harbor_modular.tl:88-89` |
| Large port | 228,000 – 678,000 | 38,000 – 113,000 | `harbor_modular.tl:118-119` |

- The two values are the smallest and the largest layout.
- Port upkeep also follows the calendar year, ×1 in 1900 to ×6 in 2020, like warehouses and airports ([Costs, upkeep and loans](costs.html)).
- Ports are noisy and dirty: 180 to 280 for both ([Pollution and noise](emission.html)).
- A ship's price and running costs are computed from its speed and capacity, like road vehicles and aircraft ([Costs, upkeep and loans](costs.html)).

## All ships

Speed in km/h, rounded. "Cargo" lists the cargo classes of the vehicle file; "any cargo" means every cargo type.

| Ship | Years | Size | Cargo | Capacity | Speed | Load speed |
|---|---|---|---|---|---|---|
| Dunara Castle | 1875–1930 | large | passengers, any cargo | 80 | 20 | 20 |
| Canadian Trawler | 1884–1948 | small | any cargo | 40 | 35 | 10 |
| Waimarie | 1889–1940 | small | passengers | 80 | 30 | 15 |
| Sydfart | 1900–1930 | small | liquid, flatbed, goods, bulk | 80 | 30 | 20 |
| PS Trillium | 1910–1955 | large | passengers | 200 | 35 | 15 |
| Sternwheeler | 1915–1960 | small | passengers, any cargo | 60 | 40 | 10 |
| Terra Nova | 1925–1975 | large | bulk, flatbed, goods | 100 | 45 | 30 |
| Votrans Towboat Tanker | 1935–1990 | small | liquid | 120 | 33 | 20 |
| Votrans Towboat Cargo | 1935–1990 | small | bulk, flatbed, goods | 120 | 33 | 20 |
| MS Stadt Kiel | 1943–1990 | small | passengers | 80 | 30 | 20 |
| Borealis | 1948–1994 | small | any cargo | 60 | 38 | 20 |
| Wopper | 1950–2005 | small | liquid, flatbed, goods, bulk | 160 | 30 | 25 |
| Meridian Ferry | 1956–2011 | small | passengers | 240 | 30 | 15 |
| Cap Arkona | 1965–2010 | large | passengers | 200 | 40 | 20 |
| Tora Coaster Ship | 1970–2020 | large | liquid, flatbed, goods, bulk | 320 | 40 | 25 |
| AP1-88 Hovercraft | 1980– | small | passengers | 240 | 90 | 15 |
| Hercules XI Towboat | 1990– | large | flatbed, goods, bulk | 120 | 32 | 20 |
| Baltica | 1994– | small | any cargo | 80 | 40 | 20 |
| HADAG Type 2000 | 1995– | small | passengers | 100 | 35 | 25 |
| Damen Tanker 800 | 1996– | small | liquid | 160 | 28 | 30 |
| Damen Fast Ferry | 2003– | large | passengers | 220 | 75 | 20 |
| Luise Deymann | 2013– | large | liquid | 240 | 30 | 35 |
| MS Diamant | 2013– | large | passengers | 280 | 45 | 35 |
| Virgo Towboat | 2015– | large | flatbed, goods, bulk | 160 | 40 | 15 |
| GHL Oita Hovercraft | 2023– | small | passengers | 320 | 100 | 20 |
| Yara Birkeland | 2030– | large | flatbed, goods, bulk | 480 | 42 | 10 |
| Solar Shuttle | 2035– | small | passengers | 80 | 30 | 30 |

## Good to know

- **Check the size before you build a small port.** Several of the biggest cargo ships (Tora, Virgo, Yara Birkeland) are large, and they will not dock there.
- **"No Path for Big Ships"** is a separate warning for large ships: the game found no water path a large ship can use. Which water is open to which size is decided by the game engine, not by the scripts, which only show the warning (`vehicle_warning.script.tl:28-36`).
- **Ship waypoints** must be placed on water ("Ship waypoints must be on water.").
- The ship depot and the ship maintenance station are separate buildings; maintenance works in a radius around them ([Vehicles: condition, age and load speed](vehicles.html)).

```check
official: "Passenger and cargo ships are available in two sizes: small and large. Large ships can only dock at large harbors, so make sure the harbor matches the size of the ships assigned to the line." (in-game guide "Water Infrastructure")
scripts: Same: small piers accept only SMALL_SHIP, medium piers SHIP and SMALL_SHIP; both ports take passengers and all cargo; 1, 2 or 4 terminals; three era variants at ×1 / ×3 / ×9; 16 small and 11 large ships in the base game.
result: refines
```
