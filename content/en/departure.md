---
title: Departure settings: full load, Fill Level and stop times
summary: When a vehicle leaves a stop: the three departure modes, the Fill Level of each cargo, and the minimum, maximum and additional stop times.
domain: stations
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-15
game: 40425
fact: 600 s | default Max. Stop Time of a new stop
fact: 30 s / 60 s | default Max. Additional Wait, road / rail
fact: 0–100 % | Fill Level, per cargo, of the vehicle's capacity
---

Each stop of a line has its own departure settings, in the stop's "Cargo Filter" window (click the stop in the line window). They decide **how much** the vehicle loads there and **how long** it may wait.

## The settings

| Setting | Values | New stop | Source |
|---|---|---|---|
| "Load if Available", "Full Load (Any)", "Full Load (All)" | one of three | Load if Available (measured) | `cargofilter_window.tl:798-821` |
| "Min. Stop Time" | 0–600 s, step 10 | 0 s (measured) | `cargofilter_window.tl:841-845` |
| "Max. Stop Time" | 0–600 s, or "---" (no limit, slider at the end) | **600 s** (measured) | `cargofilter_window.tl:855-863` |
| "Max. Additional Wait" | 0–600 s, step 10 | 60 s; 30 s at a road or tram station without rail | `cargofilter_window.tl:827-831`, `line_util.tl:478-490` |
| "Fill Level", per loaded cargo | 0–100 %, step 1 | 100 % | `cargofilter_window.tl:698-704`, `line_util.tl:472` |

- Clicking a time opens a number box: values above 600 s can be typed there (`cargofilter_window.tl:204-208`).
- The three times keep each other in order: raising the minimum or the additional wait above the maximum raises the maximum too (`cargofilter_window.tl:834-836`, `cargofilter_window.tl:848-850`); lowering the maximum lowers the other two (`cargofilter_window.tl:865-869`). Nothing is adjusted while the maximum is "---".
- Changing any of them marks the line as custom: the automatic configuration no longer touches its Load lists (`cargofilter_window.tl:438`, see [Loading and unloading speed](loading.html)). The automatic configuration itself never changes the mode or the times, but it resets every Fill Level to 100 % (`line_util.tl:495-719`, `line_util.tl:511`, `line_util.tl:543`).

## Fill Level: a cap per cargo

The Fill Level is the most of that cargo the vehicle takes at this stop, as a share of the vehicle's capacity, rounded to the nearest unit (measured in game).

| Vehicle | Fill Level | Leaves with |
|---|---|---|
| truck, 15 places, logs | 50 % | **8** (7.5 rounded up) |
| truck, 22 places, fabric | 70 % | **15** every time (15.4) |
| train, 18 places, glass | 48 % | at most **9** (8.64) |
| tram, 28 places, fuel | 66 % | at most **18** (18.48) |

- Cargo already on board counts: a tram that arrived with 14 fuel left with 18, not 14 + 18.
- Above the cap nothing is loaded **and nothing is unloaded** because of it: a truck that arrived with 22 fertilizer (cap 11) left with 22.
- **0 %** means: do not load this cargo here.
- With a Full Load mode, the cap counts as full: timber trucks with a 50 % Fill Level waited about 270 s and left with 8 of 15, not 15.
- There is no unload percentage. Unloading is decided by the Load list and "Force Unload All Cargo On Arrival" ([Loading and unloading speed](loading.html)).

## Full Load and the stop times

- **Load if Available**: the vehicle takes what is there and leaves.
- **Full Load (All)**: the vehicle waits until it is full. Timber trucks waited 460–566 s and left with 15 of 15.
- **Full Load (Any)**: the vehicle leaves when one cargo is full. A timber and planks train left with 143 and 144 logs after 369–380 s; two other departures after about 30 s with 57 and 118 logs are not explained.
- **Max. Stop Time** ends the wait, even with nothing loaded. A vegetables train in Full Load (All) with a 120 s maximum either filled up (64 of 64) in about 25 s, or left after 116–120 s with 26 or **0**. With the default 600 s it left with 26 of 64 after 596–600 s.
- **Min. Stop Time** is the whole stop, loading included, not extra time after it: with 60 s, glass trains stopped 55–61 s every time, whatever they loaded.
- **Max. Additional Wait**: "Maximum wait time after loading to improve vehicle distribution" (`cargofilter_window.tl:828`). The vehicle window shows "Ensuring safe distance" while the vehicle waits for its scheduled departure (`entity_window_util.tl:2283-2284`), presumably during this wait.
- **Several vehicles at one stop load at the same time**, whenever each one arrived (seen in game). Two timber trucks that arrived about 90 s apart left at the same second, each with 8. How the cargo is shared between them was not measured.

```engine
The scripts only store the settings; when a vehicle leaves is decided by the engine.
```

The rules above were measured with the [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) database (snapshots every 2 s, so stop times are ±2 s), November 2026.

## Good to know

- A long wait with Full Load at a stop where little cargo arrives blocks the platform: other vehicles of the line queue behind it.
- A short Max. Stop Time with Full Load can send vehicles away empty if they come back before new cargo is there.
- Once, a train in Full Load (All) stopped 783–992 s with a 600 s maximum. The cause was not found.

```check
official: "Full load (any): The vehicle will stop and wait until one cargo type is fully loaded. Full load (all): The vehicle will stop and wait until it is fully loaded." "In the vanilla game "all" and "any" only applies to trains and ships […] Any other vehicle type will wait for full load in both cases." Each cargo is loaded "to what percentage of a vehicle's total capacity". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles#departure_configuration))
scripts: Three departure modes, Min. / Max. Stop Time 0–600 s (or no limit), Max. Additional Wait 0–600 s (60 s, 30 s road), Fill Level 0–100 % per cargo; measured: Fill Level caps the cargo on board, rounded to the nearest unit, and counts as full for Full Load; Max. Stop Time ends a full load, even empty; Min. Stop Time includes loading; vehicles at one stop load together.
result: refines
```
