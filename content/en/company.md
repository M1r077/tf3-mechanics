---
title: Company rank, perks and headquarters
summary: What raises your company rank, what each rank unlocks, how permits and prospections work, what the headquarters really gives, and what a higher rank costs you.
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40444
fact: 15 | company ranks, from Junior to Tycoon
fact: ×12.5 | world population needed for rank 15, compared with the start
fact: ×0.75 | income at rank 15 with Inflation Normal
fact: 0 | ranks lost when the population falls
---

Your company rank does not come from money or deliveries: it comes from the **population of the whole map**. Every new rank unlocks perks (landmarks, prospections, Marketing Campaigns, Industry Greenification, headquarters modules), and with the **Inflation** setting it also lowers all your income a little.

## What raises the rank

- The game remembers the **world population at the start** of the game: the residents of all towns (`company.script.tl:392-396`, `company_util.tl:365-371`).
- It then compares the **highest** world population ever reached with that start value (`company_growth.script.tl:25-27`). The value only goes up: towns that shrink never cost you a rank.
- Rank 1 is reached at the start value, rank 15 at about **12.5 times** it (`company_progression_util.tl:6-14`, `company_progression_util.tl:95-120`, `town_growth_function.tl:13-20`).
- There is no rank in campaign missions and in the map editor (`company_growth.script.tl:74-79`).

| Rank | Role | World population, compared with the start |
|---|---|---|
| 1 | Junior | ×1 |
| 2 | Mechanic | ×1.02 |
| 3 | Engineer | ×1.08 |
| 4 | Coordinator | ×1.2 |
| 5 | Expert | ×1.4 |
| 6 | Team Leader | ×1.7 |
| 7 | Supervisor | ×2.1 |
| 8 | Manager | ×2.6 |
| 9 | Director | ×3.3 |
| 10 | Senior Director | ×4.2 |
| 11 | CEO | ×5.3 |
| 12 | Chairperson | ×6.7 |
| 13 | Vice President | ×8.3 |
| 14 | President | ×10.2 |
| 15 | Tycoon | ×12.5 |

The ratios are computed from the scripts for a start population of 50,000 or more (`company_progression_util.tl:6-14`, `company_static_util.tl:6-24`). On a small map they are slightly higher for the middle ranks (rank 8 needs ×2.85 at 5,000 residents); ranks 1 and 15 stay at ×1 and ×12.5.

- So the rank follows **town growth**: towns grow from your passengers and cargo, see [Town growth](towns.html).
- The first ranks come quickly, the last ones need the map's towns to be many times bigger.

## A new rank is applied in the company window

When the population passes a threshold, a **rank-up notification** appears; clicking it opens the company window on that rank (`company_growth.script.tl:96-107`, `company_notification_rank_up.script.tl:8-9`).

- The new perks are unlocked only when that rank is **selected in the company window**: the window then sends the unlock (`company.tl:420-423`, `company_growth.script.tl:55-62`). The build menus check this applied rank (`company_util.tl:92`, `company_util.tl:171-178`).
- The income multiplier of the next section follows the rank **reached**, applied or not (`company_growth.script.tl:47-48`).

```tip scripts
After a rank-up, click the notification (or open the company window and select the new rank) to get the perks. Waiting gives you nothing: the income is already lowered.
```

## What a higher rank costs: the Inflation setting

With **Inflation**, all cargo and passenger income falls evenly from ×1 at rank 1 to a minimum at rank 15 (`company_progression_util.tl:25-40`, `company_growth.script.tl:159-170`).

| Inflation | Income at rank 15 | Source |
|---|---|---|
| None | ×1 (no change) | `difficulty_util.tl:50`, `mod.script.tl:695-698` |
| Low | ×0.9 | |
| Normal | ×0.75 | |
| High | ×0.6 | |
| Very High | ×0.5 | |

- At Normal, each rank costs about 1.8 % of income: ×0.96 at rank 3, ×0.875 at rank 8, ×0.75 at rank 15.
- Inflation does not raise any cost; costs follow the calendar year (see [Costs, upkeep and loans](costs.html)).
- A higher rank also makes new subsidy offers rarer (see [Subsidies](subsidies.html)).

## Permits

Most perks are limited by **permits**. A rank gives permits for a perk; each building or use takes one (`company_util.tl:33-80`, `company_util.tl:206`).

- Permits **add up** over the ranks: a perk that gives 1 at rank 3 and 1 at rank 5 allows 2 from rank 5 on (`company_util.tl:51-56`).
- A building gives its permit back when it is demolished: the game counts what is standing (`company_util.tl:143-163`, `company_util.tl:203-206`).
- Prospections, Marketing Campaigns and Greenification use a permit up when they start (`company.script.tl:416-423`, `company.script.tl:459-462`, `company.script.tl:496-500`). The build menu then shows **Already Used** or **Cooldown** (`company_util.tl:207-226`).
- The **Marketing** permit comes back **5 years** after each campaign (`marketing.res.lua:6-7`, `company.script.tl:66-94`).

| Perk | Permits | Source |
|---|---|---|
| Headquarters | 1 at rank 1 | `hq.res.lua:6` |
| Marketing Campaign | 1 at rank 4, back after 5 years | `marketing.res.lua:6-7` |
| Industry Greenification | 1 at rank 3, 6, 9, 12 and 15 | `industry_greenify_tool.script.tl:101-102` |
| Cleaning Plant | 15 at rank 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Landmarks | one each: Amphitheater 2, Great Lighthouse 5, White Heron Castle 7, Ship Museum 9, Castle Neuschwanstein 10, Statue of Liberty 11, Summer Palace 13, Opera House 14, Houses of Parliament 15 | `arena.con.lua:39`, `lighthouse.con.lua:48`, `white_heron_castle.con.lua:47`, `ship_museum.con.lua:55`, `neuschwanstein.con.lua:55`, `statue_of_liberty.con.lua:57`, `summer_palace.con.lua:63`, `opera_house.con.lua:63`, `westminster.con.lua:79` |

What each perk does: [Reputation](reputation.html) (Marketing Campaign), [Pollution and noise](emission.html) (Greenification, Cleaning Plant).

## Prospections

A prospection looks for a resource near a town and, when it succeeds, founds a new industry there.

| Resource | Rank | Source |
|---|---|---|
| Fish | 2 | `exploration_fish.res.lua:9-11` |
| Clay | 3 | `exploration_clay.res.lua:9-11` |
| Crude oil | 4 | `exploration_crude_oil.res.lua:9-11` |
| Grain, vegetables | 4, **one shared permit** (Industry) | `exploration_grain.res.lua:9`, `exploration_vegetables.res.lua:9`, `permit_key_farm.res.lua:6` |
| Logs | 5 | `exploration_logs.res.lua:9-11` |
| Coal, iron ore | 6 | `exploration_coal.res.lua:9-11`, `exploration_iron_ore.res.lua:9-11` |
| Stone, wool | 8 | `exploration_stone.res.lua:9-11`, `exploration_wool.res.lua:9-11` |
| Sand | 9 | `exploration_sand.res.lua:9-11` |
| Rubber | 12 | `exploration_rubber.res.lua:9-11` |

- Each resource has **one** permit, used when the prospection starts (`company.script.tl:451-462`).
- It runs for up to **6 months**. Once a month it tries to place the industry, with a chance rising from 20 % to 60 % over the 6 months (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`).
- A try also fails when the game finds no place for that industry near the town (`company.script.tl:199-210`).
- If the last try fails, **the permit comes back** and a notification says so (`company.script.tl:106-126`, `company.script.tl:170-181`).
- Only one prospection per town and resource can run at a time (`company.script.tl:442-447`).

```engine
Where the new industry may stand (makeIndustrySpawnProposal near the town) is decided by the engine: a fish prospection far from water, or a town with no free land around it, simply fails and gives the permit back.
```

## The headquarters

| What | Value | Source |
|---|---|---|
| Price and upkeep | free, no upkeep | `headquarter.script.tl:526-527` |
| Permit | 1, at rank 1 | `headquarter.con.lua:6-7`, `hq.res.lua:6` |
| Town growth | +5 % to the town closest to it | `headquarter.script.tl:510-515`, `landmark_util.tl:51-70` |
| Workplaces | 24 | `headquarter.con.lua:16`, `headquarter.script.tl:505-508` |

- The +5 % is a bonus on that town's growth rate, so it does nothing when the town's rate is 0 % (see [Town growth](towns.html)).
- **Modules** cost 50,000 each and are limited by permits that grow with the rank (`hq_module_m.module.lua:83`, `hq_module_m.module.lua:137`).
- Only two modules carry a bonus in the files: **Medium Building** +1 % town growth (`hq_module_m.module.lua:139-142`) and **Large Building** +1 % Reputation Recovery (`hq_module_l.module.lua:169-172`). The recovery bonus is read by no town rating (see [Reputation](reputation.html)). The other modules are decorative.
- Each module file also starts with a table that gives +5 % town growth, but nothing in the file uses it (`hq_corner_l.module.lua:148-159`, `hq_statue.module.lua:46-57`). Only the bonus inside the module's `metadata` is added up (`headquarter_addon.script.tl:18-29`).

| Module | Permits gained at rank (×2 = two) | Total at rank 15 |
|---|---|---|
| Ground Flag | 1 ×2, 6, 7, 8, 9, 11, 12, 13, 14 | 10 |
| Corner Building | 3, 5, 7 ×2, 9, 11, 13, 15 | 8 |
| Medium Building | 2, 4, 10 ×2, 15 ×2 | 6 |
| Large Building | 5, 6, 10, 12 | 4 |
| Balcony | 8 ×2, 14 ×2 | 4 |
| Large Fountain | 10 ×2, 14 ×2 | 4 |
| Dome | 6, 15 ×2 | 3 |
| Roof Flag | 7, 10, 13 | 3 |
| Tennis Court | 11, 12, 14 | 3 |
| Ancient Tree | 13, 15 ×2 | 3 |
| Statue | 14 ×2 | 2 |
| Pool | 15 | 1 |

Sources: the `rankAndPermits` line of each module file (`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`).

```tip scripts
Put the headquarters in the town you want to grow fastest, and add Medium Buildings there: they are the only modules with a growth bonus.
```

## Good to know

- To rank up, grow the towns: more passengers and cargo to more towns, with good ratings. Money in the bank does not count.
- Plan your landmarks and prospections: each comes once, at a fixed rank.
- On a map with Inflation, a rank-up is good for perks and bad for income. At Normal the whole way to rank 15 costs a quarter of all income.

```check
official: "The company rank depends on the population of the map. … Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Same rule: the highest world population reached, compared with the population at the start, ×12.5 for rank 15; never lost. A new rank must be selected in the company window to unlock its perks, while Inflation lowers income at once. Only two modules have a bonus (Medium Building +1 % growth, Large Building +1 % Reputation Recovery, which no rating reads); the others are decorative.
result: refines
```
