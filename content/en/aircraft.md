---
title: Airplanes, airports and helicopters
summary: Airfield or airport, which airplane lands where, terminals, the second runway, heliports, and the list of all aircraft with their cargo, capacity and speed.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
fact: 2 | airplane sizes: small and large
fact: 1950 | first airport, and first helicopters
fact: 1980 | second runway
fact: 5 | aircraft per hangar
---

Every airplane is **small** or **large**. An **airfield** takes only small airplanes; an **airport** takes both, and helicopters at its main building. Helicopters also have stations of their own.

```diagram air_access
```

## Airfield and airport

- **Airfield**: "It can be used by small airplanes." Variants from 1920, 1950 and 1980; 1, 2 or 3 terminals and an optional depot (`airfield.tl:49`, `airfield.tl:76`, `airfield_era_a.metacon.tl:3`).
- **Airport**: "It can be used by small and large airplanes." Variants from 1950 and 1980; 2, 3 or 4 terminals and a landing direction (`airport.tl:24`, `airport.tl:80`, `airport1950.metacon.tl:3-4`).
- Airfield terminals accept only small airplanes; airport terminals accept both sizes (`af_terminal.module.lua:715`, `ap_terminal.module.lua:897`).
- The airport main building has helicopter pads (`ap_main.module.lua:532`), and from 1950 an airport can get a helicopter terminal (`ap_terminal_heli.module.lua:897`, `ap_terminal_heli.module.lua:971`).
- **Second runway**: an airport module from 1980 (`airport_2nd_runway.module.lua:5`). Some airport modules need it and show "You Need a 2nd Runway" without it (`airport.script.lua:261`).
- All air stations take passengers and every cargo (`airfield.tl:59`, `airport.tl:34`).

| Building | Waiting passengers | Source |
|---|---|---|
| Airfield terminal | up to 250 | `af_terminal.module.lua:773` |
| Airport main building | up to 400 | `ap_main.module.lua:667` |
| Airport terminal | up to 850 | `ap_terminal.module.lua:951` |
| Airport helicopter terminal | up to 450 | `ap_terminal_heli.module.lua:990` |

## Hangars and helicopter stations

- An airfield or airport **hangar** holds 5 aircraft, and maintains aircraft in a radius of 550 m (`af_hangar.module.lua:273-278`, `ap_hangar.module.lua:456-461`).
- **Heliport** (from 1950): buys and maintains helicopters, depot of 5, maintenance radius 800 m (`heliport.script.lua:301-306`).
- **Helipad** (from 1950): a small landing pad for passengers and cargo, without a depot (`helipad.con.lua:29-33`).

## Costs

Price and upkeep of the first variant, era coefficient included. The coefficient is ×3 for both the first airfield (1920, `airfield.tl:8`) and the first airport (1950, `airport.tl:8`), then ×9 from 1980; modules have none ([Costs, upkeep and loans](costs.html)).

| Building | Price | Upkeep per year | Source |
|---|---|---|---|
| Airfield | 3,600,000 – 9,000,000 | 150,000 – 600,000 | `airfield.tl:8`, `airfield.tl:55-56` |
| Airport | 5,400,000 – 13,500,000 | 900,000 – 2,250,000 | `airport.tl:8`, `airport.tl:30-31` |
| Airfield module (main building, terminal, hangar) | 600,000 | 100,000 | `af_main.module.lua:316-317`, `af_hangar.module.lua:326-327` |
| Airport module (terminal, hangar, second runway…) | 900,000 | 150,000 | `ap_main.module.lua:672-673`, `ap_hangar.module.lua:508-509`, `airport_2nd_runway.module.lua:27-28` |

- Airport and airfield upkeep also follows the calendar year, ×1 in 1900 to ×6 in 2020 ([Costs, upkeep and loans](costs.html)).
- An aircraft's price and running costs are computed from its speed and capacity, like ships and road vehicles ([Costs, upkeep and loans](costs.html)).

## All airplanes

Speed in km/h, rounded. "Any cargo" means every cargo type. Capacity is the total the vehicle store shows: the sum of the compartments, each counted at its largest load configuration (`vehicle_store_util.tl:70-95`).

| Airplane | Years | Size | Cargo | Capacity | Speed | Load speed |
|---|---|---|---|---|---|---|
| Junkers F 13 Herta | 1920–1950 | small | passengers | 16 | 135 | – |
| Vickers J6860 Victoria | 1922–1960 | small | any cargo | 32 | 150 | 2.5 |
| Fokker F VII A | 1925–1960 | small | passengers | 32 | 175 | 2 |
| Junkers JU-52 Iron Annie | 1933–1982 | small | passengers, any cargo | **48** (2 × 24) | 200 | 3 |
| Douglas DC-3 | 1935–1995 | small | passengers | 56 | 300 | 2.5 |
| Curtiss C-46 Commando | 1942–1980 | small | any cargo | 80 | 280 | – |
| Douglas DC-4 | 1944–1998 | small | passengers | 100 | 365 | 3 |
| Bristol Type 170 Freighter | 1949–2005 | small | passengers, any cargo | **80** (2 × 40) | 350 | 1.5 |
| Lockheed L-1049 Super Connie | 1952–1986 | large | passengers | 120 | 486 | 3 |
| Lockheed L-1049D/H Super Connie | 1959–2000 | large | any cargo | **120** (2 × 60) | 486 | 2.5 |
| De Havilland DH.106 Comet | 1960–2000 | large | passengers | 160 | 724 | 3 |
| Canadair CL-44 Freighter | 1962–2005 | large | any cargo | **144** (3 × 48) | 645 | 2 |
| Convair CV 990 Coronado | 1962–2020 | large | passengers | 200 | 917 | 2 |
| Lockheed L-100 Hercules | 1976–2000 | small | any cargo | **132** (3 × 44) | 400 | 3 |
| McDonnell Douglas DC-10-30 | 1978– | large | passengers | 400 | 960 | 2.5 |
| McDonnell Douglas DC-10-30CF | 1978– | large | any cargo | **396** (3 × 132) | 960 | 4 |
| Airbus A310 300F Freighter | 1982– | large | any cargo | 160 | 850 | 3 |
| Short 330 Sherpa | 1984– | small | passengers, any cargo | **80** (2 × 40) | 455 | 2.5 |
| Airbus A320 | 1985– | large | passengers | 180 | 753 | 3 |
| Br. Aerospace 146 | 1985– | small | passengers | 112 | 753 | 3 |
| Br. Aerospace 146 Freighter | 1985– | small | any cargo | **96** (2 × 48) | 753 | 2 |
| Fokker 100 | 1988– | large | passengers | 160 | 845 | 3.5 |
| Tupolev Tu-204 | 1995– | large | passengers | 280 | 850 | 4 |
| Tupolev Tu-204C Freighter | 1995– | large | any cargo | **204** (3 × 68) | 850 | 2 |
| Boeing 737-700 | 1998– | large | passengers | 200 | 974 | 2.5 |
| Boeing 737-700-C Freighter | 1998– | large | any cargo | **160** (2 × 80) | 974 | 3 |
| Bombardier DHC-8 | 2000– | small | passengers | 120 | 648 | 3 |
| Bombardier DHC-8 Freighter | 2008– | small | any cargo | 120 | 648 | 2 |
| Sukhoi Superjet 100 | 2011– | small | passengers | 160 | 870 | 3 |
| Airbus Canada A220 | 2013– | large | passengers | 180 | 830 | 5 |

## All helicopters

| Helicopter | Years | Cargo | Capacity | Speed | Load speed |
|---|---|---|---|---|---|
| Bell 47 | 1950–1990 | passengers, any cargo | 8 | 150 | 2 |
| Piasecki H-21 Workhorse | 1952–1985 | passengers, any cargo | 80 (48 cargo) | 210 | 3 |
| Sikorsky S-64 Skycrane | 1962–2017 | any cargo | 40 | 213 | 4 |
| Bell 206 Long Ranger | 1965–2025 | passengers | 32 | 241 | 2.5 |
| Boeing Vertol 234 Chinook | 1980– | passengers, any cargo | 80 | 269 | 2 |
| AgustaWestland AW101 Merlin | 1990– | passengers | 60 | 278 | 3 |
| Mil Mi-26TC | 1993– | any cargo | 120 | 295 | 4 |
| Eurocopter 120B Colibri | 1998– | passengers | 48 | 210 | 3 |
| Kaman K-MAX | 2005– | any cargo | 60 | 190 | 3 |
| Airbus H225 Super Puma | 2013– | passengers | 48 | 288 | 3 |
| NextGen VTOL | 2030– | passengers | 56 | 610 | 4 |

## Good to know

- **Small airplanes stay useful to the end.** The DHC-8, its freighter and the Sukhoi Superjet 100 are small, so an airfield is enough for them.
- **Before 1952 there is no large airplane**, so an early airport gives no access to bigger aircraft yet.
- Airplanes fly in a straight line, and the payment counts only the straight-line distance, so a detour costs them nothing extra ([Cargo income and delivery time](income.html)).
- The minimum runway length, flight paths and landing are decided by the game engine; the scripts do not show them.

```check
official: "It can be used by small airplanes." (Airfield) "It can be used by small and large airplanes." (Airport), build menu descriptions.
scripts: Same: airfield terminals accept SMALL_AIRCRAFT only, airport terminals AIRCRAFT and SMALL_AIRCRAFT, helicopters at the airport main building, heliport and helipad from 1950, second runway from 1980, hangars of 5; 15 small and 15 large airplanes and 11 helicopters in the base game.
result: agrees
```
