---
title: Landmarks, celebrations and fun elements
summary: What each landmark costs in cargo, when it unlocks and what it does for the vehicles of its town, how the Landmark Required Resources setting scales it, and what celebrations, fireworks, blimps and UFOs really do.
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40444
fact: 9 + 3 | landmarks: 9 in the base game (ranks 2 to 15), 3 more with the DLC packs (rank 1)
fact: +20 % / +25 % / −20 % / −25 % | top speed, pollution or comfort for the vehicles of its town
fact: ×0 to ×4 | cargo needed, with the Landmark Required Resources setting
fact: 2-4 years | between two UFOs
---

A landmark is built like a construction site: you unlock it with a company rank, place it, and then **deliver cargo** to it. When the site has all its cargo, the landmark is finished and gives a bonus to the vehicles of **its town**. The headquarters is a separate building with its own rules (see [Company rank, perks and headquarters](company.html)).

## The landmarks

Cargo at **Landmark Required Resources** Normal (×1).

| Landmark | Rank | Cargo to deliver | Bonus for the vehicles of its town | Source |
|---|---|---|---|---|
| **Amphitheater** | 2 | 800 stone | road vehicles: noise **−25 %** | `arena.con.lua:10`, `arena.con.lua:20-26`, `arena.con.lua:39` |
| **Great Lighthouse** | 5 | 1,200 stone, 200 fuel | ships: top speed **+20 %** | `lighthouse.con.lua:10`, `lighthouse.con.lua:14`, `lighthouse.con.lua:29`, `lighthouse.con.lua:48` |
| **White Heron Castle** | 7 | 1,200 stone, 400 planks | trains: pollution **−20 %** | `white_heron_castle.con.lua:10`, `white_heron_castle.con.lua:14`, `white_heron_castle.con.lua:28`, `white_heron_castle.con.lua:47` |
| **Ship Museum** | 9 | 600 logs, 600 planks, 200 fabric | ships: comfort **+25 %** | `ship_museum.con.lua:10-18`, `ship_museum.con.lua:36`, `ship_museum.con.lua:55` |
| **Castle Neuschwanstein** | 10 | 1,000 stone, 600 planks, 200 dyes | road vehicles: comfort **+25 %** | `neuschwanstein.con.lua:10-18`, `neuschwanstein.con.lua:36`, `neuschwanstein.con.lua:55` |
| **Statue of Liberty** | 11 | 800 stone, 400 steel, 400 sheet metal | ships: pollution **−20 %** | `statue_of_liberty.con.lua:10-18`, `statue_of_liberty.con.lua:38`, `statue_of_liberty.con.lua:57` |
| **Summer Palace** | 13 | 600 stone, 300 planks, 300 dyes, 300 furniture | aircraft: pollution **−20 %** | `summer_palace.con.lua:10-22`, `summer_palace.con.lua:44`, `summer_palace.con.lua:63` |
| **Opera House** | 14 | 800 stone, 400 glass, 400 sheet metal, 400 fabric | trains: comfort **+25 %** | `opera_house.con.lua:10-22`, `opera_house.con.lua:44`, `opera_house.con.lua:63` |
| **Houses of Parliament** | 15 | 800 stone, 400 planks, 400 glass, 400 furniture | road vehicles, trains, ships and aircraft: top speed **+20 %** | `westminster.con.lua:10-22`, `westminster.con.lua:45`, `westminster.con.lua:79` |

**DLC landmarks.** Two DLC packs add three more, unlocked from rank 1. Their files are in the game's DLC folders (Deluxe Upgrade Pack and Pre-order Pack), outside the base files this wiki indexes, so they have no source links here.

| Landmark | DLC | Rank | Cargo to deliver | Bonus for the vehicles of its town |
|---|---|---|---|---|
| **Eiffel Tower** | Deluxe Upgrade Pack | 1 | 400 steel | road vehicles: top speed **+25 %** |
| **Taj Mahal** | Deluxe Upgrade Pack | 1 | 800 stone | aircraft: noise **−25 %** |
| **Great Pyramid** | Pre-order Pack | 1 | 800 stone | trains: top speed **+25 %** |

- Each landmark is unlocked once, by its rank; how the rank grows is in [Company rank, perks and headquarters](company.html).
- Landmarks cost nothing to build and nothing per year in their files: only the cargo (`arena.con.lua:59-64`).
- The site stores half of each cargo at a time, so it needs at least two deliveries of each (`arena.con.lua:13-18`).

## Building a landmark

- The site has **4 stages**. It moves up as cargo arrives: stage 2 at one third of all the cargo, stage 3 at two thirds, finished at 100 %. Each cargo only counts up to its own amount, so extra stone does not make up for missing planks (`landmarks.script.tl:34-46`).
- The bonus works only when the landmark is **finished** (`landmark_util_serialized.tl:393-395`). The message "Construction finished" appears then (`landmarks.script.tl:49-61`).
- The **Landmark Required Resources** setting multiplies all the cargo: None ×0, Low ×0.5, Normal ×1, High ×2, Very High ×4. The presets are Easy ×0.5, Medium ×1, Hard ×2, Very Hard ×4. At ×0 a landmark is finished as soon as it is placed (`difficulty_util.tl:40`, `difficulty_util.tl:107`, `difficulty_util.tl:135`, `difficulty_util.tl:162`, `difficulty_util.tl:189`, `landmarks.script.tl:38`, `landmarks.script.tl:46`).

## Who gets the bonus

- The bonus goes to the town **closest to the landmark**, and to the vehicles whose closest town is that town, of the carrier listed (`landmark_util.tl:6-47`, `landmarks.script.tl:208-236`).
- When a vehicle drives into the area of another town, it takes that town's bonuses and loses the old ones (`landmarks.script.tl:279-299`).
- Bonuses of several landmarks in the same town **add up**: two +20 % top speeds give +40 % (`landmark_util.tl:46`, `vehicle_modifier.script.tl:3-16`).

```engine
Which town is the "closest town" of a landmark or of a moving vehicle is decided by the engine (getConstructionClosestTown, closestTown). How the engine turns +25 % comfort or +20 % top speed into trips and income is engine work too.
```

```tip scripts
Put the Houses of Parliament in the town where most of your vehicles run: +20 % top speed for every carrier. A second +20 % comes from the Great Lighthouse for ships in the same town. The Centralized achievement asks for 10 finished landmarks with the same closest town; the headquarters does not count, as it has no cargo to deliver. The base game holds 9 landmarks and the DLC packs add 3 (counted); whether Centralized can be reached without a DLC is unknown (see [Achievements](achievements.html)).
```

## Celebrations

A celebration is the little party shown over a town when something happens for the first time. It also raises the town's **Reputation**, but only when the Reputation is not already full.

| Event | Reputation | Source |
|---|---|---|
| first passenger boards one of your lines in the town | +50 % | `celebrations.script.tl:228-252` |
| first cargo delivered to the town | +50 % | `celebrations.script.tl:187-198` |
| the town levels up | +50 % | `celebrations.script.tl:260-272` |
| first cargo delivered to an industry | +20 % to the town closest to it | `celebrations.script.tl:202-219` |

- A town levelling up also gets **fireworks**, unless they are turned off (`town_growth.script.tl:108-112`).
- How Reputation works: [Reputation](reputation.html).

## Fun elements

- A **blimp** flies over a town when you start a Marketing Campaign there (`fun_elements.script.tl:112-117`).
- A **UFO** appears every **2 to 4 years** of game time, chosen at random, when there is none on the map (`fun_elements.script.tl:10`, `fun_elements.script.tl:79-91`). Click it for the Encounter of the 3rd Kind achievement.
- None of them changes the economy.

## Good to know

- Pick the town before building: the bonus does not follow your lines, only the vehicles near that town.
- On Very Hard a landmark needs four times the cargo: the Houses of Parliament then takes 3,200 stone and 1,600 of each of the other cargo.

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: Nine base landmarks, one per rank from 2 to 15, plus three DLC landmarks at rank 1, each built from delivered cargo in 4 stages, scaled by Landmark Required Resources ×0 to ×4. Once finished each gives one bonus (+20 % or +25 % top speed, −20 % pollution, −25 % noise or +25 % comfort) to the vehicles of one carrier in its closest town; bonuses add up. Celebrations add 50 % or 20 % Reputation; a UFO comes every 2 to 4 years.
result: adds
```
