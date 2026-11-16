---
title: Town growth: XP, ratings and size
summary: Where a town's XP comes from, how the six ratings set its growth rate, and how much bigger each level makes it.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
game: 40425
fact: 0 % | growth when one rating is Very Poor
fact: ×1.5 | XP for each next level (1,000 for level 2)
fact: ×40 | size after 17 levels gained
---

A town only grows from **your** transport: passengers who arrive by your lines and cargo delivered to its buildings give it XP. Its ratings decide how much of that XP counts, and every level gained makes the town bigger.

```diagram town_xp
```

## Where XP comes from

| Source | Raw XP | Source |
|---|---|---|
| Passenger arriving **by your lines** at a town building | 5 · 10 · 20: home and job or shop in the same town, a neighbour town, a town farther away | `town_growth.script.tl:649-701`, `town_growth_config.res.lua:6` |
| Cargo unit delivered to a town building | 10 · 20 · 40 for cargo tier 0 · 1 · 2 | `town_growth.script.tl:642`, `town_growth_config.res.lua:5` |
| Subsidy reward "town experience" | a share of the current level, also × growth rate | `subvention_util.tl:144-152`, `town_growth.script.tl:608` |

- The XP goes to the town of the building where the passenger or cargo **arrives**. A commuter between two towns gives XP to both: to the job's town on the way there, to the home town on the way back.
- Trips to or from an **industry** give no XP (`town_growth.script.tl:680-683`). Trips on foot or by car give none either: only trips made with your lines count (`town_growth.script.tl:656`).
- Time alone gives nothing: the XP per tick is 0 (`town_cargo_util.tl:6`).
- Cargo tiers: **0** bricks, cement, fish, fuel, meat, planks, vegetables; **1** beverages, books, clothes, furniture, machines, tinned food, tools; **2** vehicles (`placementparamsutil.lua:506-616`).

Every raw XP is multiplied by the town's **growth rate** (`town_growth.script.tl:60-63`). The town window shows it as **Growth Rate:**.

## The growth rate

The growth rate comes from two ratings of the town window (`town_util.tl:607-633`, `town_util.tl:954-962`):

1. **Town Authority**: the **lowest** of its six ratings, not the average (`town_util.tl:754-784`).
2. **Supplies**: the passenger and cargo supply levels averaged, rounded up (`town_util.tl:555-589`).

```diagram growth_matrix
```

- Each rating has six levels: a value of 0–1 is cut into sixths (`town_util.tl:983-985`). **Excellent** needs 5/6 = 83 % or more.
- With **one** rating at Very Poor, the authority is Very Poor and the growth rate is **0 %**: the town stops, whatever you deliver.
- 100 % needs Excellent authority with Very Good supplies or better, or Very Good authority with Excellent supplies.
- Your **headquarters** adds +5 % to the town closest to it, several extensions add +5 %, some less or nothing; the value is in each module file (`headquarter.script.tl:510-515`, `landmark_util.tl:51-70`). This bonus multiplies the rate, so it does nothing at 0 %.

```tip scripts
**A town has stopped growing? Fix its worst rating first.** The Town Authority is the lowest of the six ratings, so one Very Poor rating holds the town at 0 % and improving the others changes nothing.
```

## The six authority ratings

| Rating | What lowers it | Source |
|---|---|---|
| **Reputation** | landscaping, demolishing town buildings, removing trees or rocks, failed subsidies; each cut main connection to another town −1/3 | `town_util.tl:396-404`, `town_util.tl:1608`, `town_react_util.tl:30-43` |
| **Traffic** | congested streets in the town | `town_util.tl:445-456` |
| **Happiness** | share of unhappy travellers (at least 15 people assumed) | `town_util.tl:479-503` |
| **Delivery** | share of late cargo deliveries (see [Cargo income](income.html)) | `town_util.tl:505-519` |
| **Noise** | town noise: 65 dB or less → full rating, 80 dB → 0 | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Pollution** | average pollution per 16 m cell of the town area, on the scripts' log scale ("dB", not a sound level): 60 → full, 74 → 0 | `town_util.tl:413-431`, `emission_config.tl:23-24` |

The **sensitivity** settings move these limits: Reputation is only Off / On, the five others have seven steps from Off to Extreme, Normal being ×1 (Noise and Pollution go further at the top: up to ×3.5 and ×5, against ×3 for the others); Off means always full rating (`difficulty_util.tl:44-49`).

## Supplies

- **Passengers**: line usage of the town × 2, so **50 % line usage gives the full rating** (`town_util.tl:546-553`).
- **Cargo**: supply ÷ demand of each district (residential, commercial, industrial), all its cargos together; the **best** district counts, not the average (`town_util.tl:521-543`).
- A town with nothing to supply counts as full supplies. A town that gets neither passengers nor cargo from you counts as "no deliveries": growth rate 0 % (`town_util.tl:565-588`).

```tip scripts
**You don't need every resident on your lines: 50 % line usage already gives the full passenger rating.**
```

New cargo demands come with levels (`placementparamsutil.lua:618-660`): one commercial and one industrial at the start, a second commercial at level 5, a second industrial at level 7, a third commercial at level 9, a third industrial at level 11. They are only added once the town has received at least one cargo delivery (`town_growth.script.tl:286-288`). The game prefers cargos that few other towns already ask for (`town_growth.script.tl:258-266`).

## Levels and size

- Level 2 needs 1,000 XP, each next level 1.5 times more than the one before (`town_cargo_util.tl:81-97`, `town_growth_config.res.lua:7`): level 5 at 8,125 XP in total, level 10 at about 75,000, level 18 (Large Metropolis, the last) at about 2 million.
- Towns placed with more homes start higher: level 2, 3 or 4 (`town_cargo_util.tl:43-54`).
- The **target size** depends on the levels gained since the start, including the progress towards the next one (`town_cargo_util.tl:100-110`, `town_growth_function.tl:4-11`):

```diagram town_size
```

- The extra size is shared between the residential, commercial and industrial districts by how well each is served: passenger use for homes, cargo supply for the others (`town_growth.script.tl:404-421`). Once a district holds 40 % of the town, the most it can take of the new size drops from 100 % to 50 % as it reaches 50 % of the town (similar limits apply across the whole map) (`town_growth.script.tl:509-522`). If no district is served at all, the town does not grow, even with XP (`town_growth.script.tl:415`).

```engine
The engine computes line usage, the traffic speed, the noise and pollution maps and the list of late deliveries, and builds the new houses and streets. The smallest share a district always gets (townGrowthMinDistrictFraction) is an engine value.
```

## Cargo demand and building stocks

- A town's demand is the sum of its **buildings**. Each building has one small input stock per cargo its district asks for: capacity ÷ 4, rounded up, × that cargo's factor in the town's needs (1 unless set otherwise; where the factor comes from is not in the scripts) (`townbuildingutil.lua:226-251`). Each cargo defines a townConsumptionFactor of 1, 0.5 or 0.25 (`placementparamsutil.lua:506-616`); how it reaches the building is engine-side. The game notes that this stock size "is currently nowhere shown in the UI" (`townbuildingutil.lua:249`).
- The town window's demand is the total limit of these stocks; the supply counted for the rating is capped at the demand (`town_util.tl:95-99`, `town_util.tl:194-198`). Bigger towns ask for more because they have more buildings.
- The building window shows a **Consumption Rating**: how fast the building uses its cargo compared with its maximum (`town_building.tl:103-132`).
- XP and payment come when a unit enters a building's stock (`town_growth.script.tl:620-642`).
- A stop only reaches the buildings in its catchment area. Their stocks can be full while the town as a whole is still short: then the cargo that does not fit **stays on the vehicle**, unless **Force Unload All Cargo On Arrival** is ticked ("Unload cargo even if stocks are full.") (`cargofilter_window.tl:757-763`), which destroys what does not fit (see [Loading and unloading speed](loading.html)).
- Cargo left on board raises the notification **Cargo Unload Problem**: "{cargoCount} cargo of {vehicle} was not unloaded on line." (`cargo_rtc_warning.script.tl:28-41`, `cargo_rtc_warning.script.tl:37`); its type label is **Cargo Not Unloaded** (`cargo_rtc_warning.res.lua:6`).
- **Town Cargo Demands** ("Choose the maximum number of cargo demands per town."): 2, 4 or 6, default 2 (`difficulty_util.tl:54`, `difficulty_util.tl:83`, `mod.script.tl:173`, `mod.script.tl:205`). The scripts add demands by level (above) and pass this value to the engine.

```engine
How fast a building consumes its stock (consumeFrequency), which building in a catchment gets each unit, what happens to cargo that is carried around, and how the engine uses Town Cargo Demands are engine-side.
```

## Can I stop a town from growing?

- In a normal game there is **no setting** for a maximum town size (`difficulty_util.tl:90-199`).
- In **sandbox mode**, the town window has a **Target District Capacities** card with **Enable Town Development** (`town_eow.script.tl:1041-1052`, `town_eow.script.tl:1170-1171`, `town_eow_editor_initial_capacity.res.lua:6`). Unticked, the town gets no XP and is not resized; the window shows **Town Development Inactive** (`town_growth.script.tl:28`, `town_growth.script.tl:345`, `town_eow.script.tl:107`).
- Without sandbox, the only ways are indirect: a town only grows from your passengers and cargo, and one Very Poor rating stops it (above).

## Good to know

- **Fix the worst rating first**: authority is the minimum, so improving the others does nothing.
- Passengers between **two towns** give 2 times (neighbours) or 4 times (farther) the XP of trips inside one town, and to both towns.
- Commercial cargos are tier 0–1 only; only **vehicles** (industrial) give 40 XP per unit, and a town normally asks for them only from its third industrial demand (level 11).
- A town far from your HQ does not get its bonus: only the closest town does.

```check
official: "A town needs 1,000 total XP to reach level 2. The XP required for each following level-up is 1.5 times the amount required for the previous level-up." Passengers 5 / 10 / 20 XP, cargo 10 / 20 / 40 XP. "The Town Authority rating is determined by the lowest of six ratings." "A line usage of 50% gives the maximum rating." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Same numbers. Growth rate 0–100 % in steps of 20 % from authority × supplies; one Very Poor rating stops growth; no XP from trips to industries; cargo demands added only after a first cargo delivery; the third commercial demand cannot be tier 2 in the base game (no commercial tier-2 cargo); size ×40 after 17 levels gained.
result: refines
```
