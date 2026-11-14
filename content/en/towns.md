---
title: Town growth: XP, ratings and size
summary: Where a town's XP comes from, how the six ratings set its growth rate, and how much bigger each level makes it.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-14
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
- Your **headquarters** adds +5 % to the town closest to it, and most of its extensions add another +5 % each (`headquarter.script.tl:510-515`, `landmark_util.tl:51-70`). This bonus multiplies the rate, so it does nothing at 0 %.

## The six authority ratings

| Rating | What lowers it | Source |
|---|---|---|
| **Reputation** | landscaping, demolishing town buildings, removing trees; each cut main connection to another town −1/3 | `town_util.tl:396-404`, `town_util.tl:1608` |
| **Traffic** | congested streets in the town | `town_util.tl:445-456` |
| **Happiness** | share of unhappy travellers (at least 15 people assumed) | `town_util.tl:479-503` |
| **Delivery** | share of late cargo deliveries (see [Cargo income](income.html)) | `town_util.tl:505-519` |
| **Noise** | town noise: 65 dB or less → full rating, 80 dB → 0 | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Pollution** | average pollution of the town area: 60 dB → full, 74 dB → 0 | `town_util.tl:413-431`, `emission_config.tl:23-24` |

The **sensitivity** settings of each rating (seven steps, the first is Off) move these limits; Off means always full rating (`difficulty_util.tl:44-49`).

## Supplies

- **Passengers**: line usage of the town × 2, so **50 % line usage gives the full rating** (`town_util.tl:546-553`).
- **Cargo**: supply ÷ demand of each district (commercial, industrial); the **best** district counts, not the average (`town_util.tl:521-529`).
- A town with nothing to supply counts as full supplies. A town that gets neither passengers nor cargo from you counts as "no deliveries": growth rate 0 % (`town_util.tl:565-588`).

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
