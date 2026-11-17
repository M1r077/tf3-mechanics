---
title: Notifications and warnings
summary: When each warning appears and when it goes away: stuck vehicles, stations not usable or overcrowded, line and stop problems, town ratings, vehicle condition, closing industries, and which warnings are hidden from the log by default.
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 5 min | of game time standing still before a vehicle is reported stuck
fact: 20 % | condition that triggers the warning, until the vehicle is back above 30 %
fact: 11 | notification types off in a new game
fact: 75 days | between two checks for stations without a road connection
---

Most warnings are **persistent**: a game script checks the situation again and again, the warning stays while the problem is there and ends by itself when it is solved. The checks are spread over 4 updates in turn, so a warning can take a moment to appear or go away (`notifications.script.tl:13`, `notifications.script.tl:49`).

## When each warning appears

| Warning | Appears when | Goes away when | Source |
|---|---|---|---|
| **Vehicle Stuck** | one of your vehicles is on its way, not stopped by you, and has had speed 0 for **5 minutes** of game time | it moves again | `notifications.script.tl:557-580` |
| **Station Not Functional** | no terminal of the station loads or unloads passengers and **nothing** is in its catchment area (no warehouse, industry or town building), while one of your lines stops there | something enters the catchment area | `notifications.script.tl:602-617`, `notifications.script.tl:630-647`, `station_useless.script.tl:39` |
| **Station Overcrowded** | the station holds more waiting passengers or cargo than it can (overflow), while one of your lines stops there; passengers leave | the overflow ends | `notifications.script.tl:599`, `notifications.script.tl:649-661`, `overcrowding.script.tl:23` |
| **Vehicle Condition** | a vehicle of yours is at **20 %** condition or below | it is back above **30 %** | `notifications.script.tl:310-318` |
| **Town Rating Very Poor** | one of the town's ratings falls to Very Poor (below 1/6) | the rating is back to Mediocre or better | `notifications.script.tl:230-238`, `town_util.tl:763-769`, `town_util.tl:983-985` |
| **Town Rating Decreasing** | a rating is Poor or Mediocre (below 50 %) without being in the Very Poor warning | the rating is Good or better | `notifications.script.tl:240-248` |
| **Industry Closing** | an industry starts its closing countdown | it closes, or it is used again in time | `notifications.script.tl:439-451`, `industry_close.script.tl:53-59` |
| **No Road Connection** | a station is not connected to a road; checked every **75 days** | the next check finds a road | `notifications.script.tl:16`, `notifications.script.tl:423-436` |
| **Cargo Unload Problem** | cargo of a vehicle is never unloaded on its line | it is unloaded | `notifications.script.tl:277-290`, `cargo_rtc_warning.script.tl:28-37` |

- A vehicle **in the depot** never counts as stuck: that check is switched off in the script (`notifications.script.tl:563-564`). A vehicle you stopped never counts either.
- The Station Not Functional check looks at the catchment area only. A station that already has passengers loading or unloading at a terminal is never reported (`notifications.script.tl:606-610`).
- How to raise a town rating: [Town growth](towns.html) and [Reputation](reputation.html). How the closing countdown works and how to stop it: [Industries](industries.html). What condition does to a vehicle: [Costs, upkeep and loans](costs.html).

```engine
Whether a station overflows, whether a vehicle has a path, whether a line can reach its stations and how long the trip between two towns may last are found by the engine (calculateStationGroupCargo, getVehicleProblems, getLineProblems, getTownProblems). The scripts only turn its answers into warnings.
```

```tip scripts
Vehicle Stuck, Vehicle Problem, Vehicle Condition, Station Overcrowded and Station Not Usable are off in the log of a new game. Turn them on in the notification settings: they are the warnings that tell you about a jam, a missing path or a worn-out fleet.
```

## Line, stop and vehicle problems

These come straight from the engine's checks of your lines and vehicles; the script gives each one a title.

| Warning | Cases | Source |
|---|---|---|
| **Line Problem** | too few stations; a station twice in a row; stations incompatible with each other; stations could not be connected; alternative terminals could not be connected | `line_warning.script.tl:46-128` |
| **Line Is Misconfigured** | a cargo type that cannot be loaded anywhere, or unloaded anywhere; no vehicle can carry a cargo set to be loaded; vehicles that carry none of the configured cargo, or cargo-only vehicles on a passenger line; no cargo configured at all | `line_warning.script.tl:15-36`, `line_warning.script.tl:133` |
| **Station Problem** | a stop the current vehicles cannot use; a passenger stop used by cargo vehicles (one or all); a cargo stop used by passenger vehicles; a configured cargo type that cannot be loaded or unloaded at that stop | `line_station_warning.script.tl:6-87` |
| **Vehicle Problem** | no electrified path; no path for big aircraft; no path for big ships; no path at all; two trains blocking each other | `vehicle_warning.script.tl:6-58` |
| **Town Not Connected** | the road between two towns is interrupted; the trip between two towns takes too long | `town_warning.script.tl:7-19` |

- "No Path for Big Aircraft" and "No Path for Big Ships" mean the vehicle is too large for a runway, dock or waterway on its line: see [Aircraft](aircraft.html) and [Ships](ships.html).

## Log, pop-ups and settings

- Each warning type can be turned off in the notification settings ("Configure Notification Logging"). A turned-off type gets no pop-up and is not kept in the log (`notification_util.tl:145-146`, `notification_log.tl:480`).
- In a **new game**, 11 types are off from the start: **Vehicle Stuck**, **Vehicle Problem**, **Vehicle Condition**, **Station Overcrowded**, **Station Not Usable**, **Station Not Connected**, **Town Not Connected**, **Cargo Not Unloaded**, and the company's Prospecting, Marketing Campaign and Industry Greenification progress messages (`stuck_vehicle.res.lua:7`, `vehicle_warning.res.lua:8`, `noroadconnection.res.lua:8`, `vehiclecondition.res.lua:8`, `overcrowding.res.lua:8`, `station_useless.res.lua:7`, `town_warning.res.lua:8`, `cargo_rtc_warning.res.lua:8`, `notification_util.tl:32-39`).
- One-off messages (new vehicle, new construction, rank up, subsidies) hide their pop-up after **60 seconds** of game time; they stay in the history (`notification_util.tl:10`, `notifications.script.tl:85-94`).
- A notification also ends when everything it points at has been removed or rebuilt (`notifications.script.tl:95-107`).
- In a mission the notifications start paused, until the mission turns them on (`notifications.script.tl:700-704`).

## Good to know

- A stuck warning after 5 minutes does not say why. Look at the vehicle: a red signal, a one-way signal the wrong way, or a Vehicle Problem warning for the same vehicle.
- "Station Not Functional" only means "nothing in the catchment area yet". Move the station closer to houses, an industry or a warehouse, or enlarge it.
- An overcrowded station loses passengers: add vehicles, or shorten the interval (see [Departure and waiting](departure.html)).

```check
official: The official wiki's User Interface page describes the notification button, the log and its filters, without the conditions of each warning. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: The conditions above: stuck after 5 minutes at speed 0 on the way, vehicle condition at 20 % until 30 %, Very Poor town rating below 1/6, road connection checked every 75 days, 11 types off by default.
result: adds
```
