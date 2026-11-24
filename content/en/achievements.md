---
title: Achievements
summary: What the game script checks for each Free Game achievement and when, which ones count only base-game vehicles, cargo and animals, and which checks are left to the engine.
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-24
game: 40444
fact: 17 | achievements unlocked by the game script itself
fact: 500 m | height of the first wagon of a train at a stop for Summit Stopover
fact: < 1 % | town reputation for It Wasn't Me
fact: 10 | landmarks that must have the same closest town for Centralized
---

The official wiki lists 41 achievements. The game script (`achievements.script.tl`) unlocks **17** of them itself and feeds **9 cross-game counters**; the others (campaign, weather, town size, warehouse, interest, boosters, cars, 1900-2000, steam in the 2000s) are checked elsewhere, by the engine or the platform. Every check first asks the engine whether the achievement can still be unlocked; whether mods or settings block it is decided there (`achievements.script.tl:632`, `achievements.script.tl:510`).

## Achievements checked by the script

| Achievement | What the script checks | Source |
|---|---|---|
| **Package Arrived** | one cargo item reaches its destination | `achievements.script.tl:221-225`, `achievements.script.tl:632-636` |
| **On Behalf Of** | one subsidy completed | `achievements.script.tl:241-244`, `achievements.script.tl:638-642` |
| **Subsidy Streak** | 10 subsidies completed with no failed one between them; a failed subsidy resets the count to 0 | `achievements.script.tl:243-249`, `achievements.script.tl:644-648` |
| **Caretaker** | a town's delivery rating changes to **Excellent** | `achievements.script.tl:270-276`, `towns.script.tl:27-30`, `achievements.script.tl:650-654` |
| **Urban Development** | a town levels up | `achievements.script.tl:253-255`, `town_growth.script.tl:92` |
| **Increased Demand** | a town gets a new cargo type demand | `achievements.script.tl:257-259`, `achievements.script.tl:668-672` |
| **It Wasn't Me** | a town's Reputation goes **down** to below **1 %** | `achievements.script.tl:261-267`, `towns.script.tl:33-36` |
| **Promotion** | the company gains a rank | `achievements.script.tl:280-282`, `achievements.script.tl:680-684` |
| **Career Ladder** | the company reaches the highest rank | `achievements.script.tl:284-290`, `achievements.script.tl:686-690` |
| **Landscaper** | you place trees, and only trees, in one build (nothing removed, not by reforestation) | `achievements.script.tl:346-377` |
| **Perfectionist** | the same station is demolished, rebuilt, demolished and rebuilt, in that order, with no other station built or removed between | `achievements.script.tl:304-341`, `achievements.script.tl:694-710` |
| **Centralized** | exactly 10 completed landmarks have the same closest town | `achievements.script.tl:382-395`, `achievements.script.tl:713-721` |
| **Summit Stopover** | one of your trains arrives at a stop with its first wagon higher than **500 m** | `achievements.script.tl:407-417`, `achievements.script.tl:723-727` |
| **Offshore** | one of your helicopters arrives at a stop of an oil platform | `achievements.script.tl:420-450`, `achievements.script.tl:729-733` |
| **Heritage Fleet** | every ship model of the base game is running on one of your ship lines at the same time | `achievements.script.tl:735-776` |
| **Encounter of the 3rd Kind** | you click a UFO | `achievements.script.tl:793-806` |
| **Timekeeper** | you change the time of day by hand | `achievements.script.tl:839-844` |

- **Perfectionist** only counts a build that adds or removes one whole station: adding a platform or a module to a station does not count (`achievements.script.tl:301-302`).
- **Centralized** counts each landmark when it is finished, for the town closest to it at that moment (`achievements.script.tl:386`).
- **Heritage Fleet** is only checked when a ship model that has never stopped before arrives at a stop; it looks at the vehicles of your ship lines, not at ships in a depot (`achievements.script.tl:736`, `achievements.script.tl:750-766`).
- **It Wasn't Me** needs Reputation, not another rating: see [Reputation](reputation.html).

```tip scripts
Summit Stopover checks the height of the first wagon when the train stops, not the height of the station building. Build the station on a mountain above 500 m and run one train there.
```

## Cross-game counters

These go on from game to game (the platform stores them). The script only sends what changed since the last check.

| Counter | Achievement | What counts | Source |
|---|---|---|---|
| Track length | **Around the World** | the growth of the logbook's total length (in km); nothing is taken off when you remove | `achievements.script.tl:511-523` |
| Population | **Global Population** | the growth of the map's population, from the population when the game was loaded | `achievements.script.tl:512`, `achievements.script.tl:525-533` |
| Passengers | **Passenger Pioneer** | passengers who finished a trip on one of your lines | `achievements.script.tl:236-238`, `achievements.script.tl:535-541` |
| Cargo | **Cargo Pioneer** | cargo items delivered | `achievements.script.tl:543-549` |
| Climates | **Tycoon of Tycoons** | the climate of the map, when the company reaches the highest rank there | `achievements.script.tl:551-567` |
| Income | **Evil Money** | your income added up, in billions | `achievements.script.tl:202-204`, `achievements.script.tl:569-590` |
| Cargo types | **Master Salesman** | each base-game cargo type delivered once | `achievements.script.tl:20-22`, `achievements.script.tl:230-232`, `achievements.script.tl:592-607` |
| Vehicles | **Connoisseur** | each base-game vehicle model that arrives at a stop once | `achievements.script.tl:16-18`, `achievements.script.tl:469-481`, `achievements.script.tl:609-625` |
| Animals | **Animal Lover** | each base-game animal you click once | `achievements.script.tl:24-26`, `achievements.script.tl:809-834` |

- Vehicles, cargo and animals from mods never count for these counters: only files of the base game (`::/vehicle`, `::/cargos`, `::/animal`) are taken (`achievements.script.tl:16-26`).
- For Connoisseur a vehicle must **arrive at a stop** of a line; buying it is not enough.

```engine
Whether an achievement can still be unlocked (isAchievementUnlockable), whether the counters are switched off (areStatsDisabled), the targets of each counter and the 24 achievements not in the script are handled by the engine and the platform. The official wiki says achievements are generally unavailable with non-cosmetic mods or with gameplay settings away from the standard values.
```

## Mods and achievements

Using mods does **not** switch achievements off by itself. What counts is whether each active mod is marked **cosmetic**.

- Every mod has a `cosmetic` flag in its `mod.json`. The game's own API documentation (folder `api/tealdef`, field `ModDesc.cosmetic`) says: "If the mod is purely cosmetic, cosmetic mods still allow achievement from being earned while playing".
- The engine checks the list of active mods (`ModRep.couldAchievementsBeEarned`) and stores the result in each savegame (`achievementsEarnable`), same folder.
- The official DLCs and campaign missions are mods too, and all of them are marked cosmetic (`dlcs/*/mod.json`, `mods/release/urbangames_campaign*/mod.json`).
- When achievements are blocked, the game says so: it has the messages "Achievements Disabled!" and "Achievements cannot be earned." (`base/strings`).

So a game with only cosmetic mods can still earn achievements. A single non-cosmetic mod, or gameplay settings away from the standard values, is enough to block them (official wiki).

```engine
The exact rule (which settings count, and whether a savegame that was once blocked stays blocked after the mod is removed) is decided in the engine and is not in the readable files: unknown.
```

```tip scripts
The mod author chooses the flag. Check the `cosmetic` line in the mod's `mod.json`, or ask the author. A mod that changes gameplay (costs, production, rules) is usually not cosmetic.
```

## Good to know

- Each "first time" achievement is checked against the previous check: it needs a **new** event in a game where the achievement is still open, an old subsidy or rank from a save does not count again (`achievements.script.tl:633`, `achievements.script.tl:779`).
- Your rank, subsidies and Reputation are explained in [Company rank, perks and headquarters](company.html), [Subsidies](subsidies.html) and [Reputation](reputation.html).

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: 17 achievements and 9 counters are in the script. It refines the official texts: Caretaker means the delivery rating reaching Excellent, It Wasn't Me a Reputation below 1 %, Summit Stopover the first wagon above 500 m, Perfectionist demolish-rebuild-demolish-rebuild of the same station, and Heritage Fleet all base-game ship models on lines at once. Only base-game vehicles, cargo and animals count for the counters.
result: refines
```
