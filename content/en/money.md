---
title: Why am I losing money?
summary: What pays, what costs, and a six-step check to find the lines that lose money and why, with links to the pages that explain each point.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-15
game: 40425
fact: 1 | payment per item, at the consumer, for the straight line
fact: 0 | paid at a warehouse or a transfer
fact: 100 % | paid even when late
fact: ×6 | year factor on warehouse, harbour and airport upkeep by 2020
---

A delivery pays for **one straight line**, from where the cargo was made to where it is used, and only when it arrives there. Everything you build and buy costs money every year, some of it more and more with the calendar year. A line loses money when its share of the payments is smaller than the costs it brings.

```diagram money_flow
```

## What pays

- **Distance as the crow flies** from the source to the consumer, plus 8 × the climb. The length of your route does not count (`cargo_income.script.lua:3-7`, `cargo_income.script.lua:5`).
- **Every cargo pays the same** per kilometre: the income factor is 3.8 for all of them (`cargotype.script.lua:7-13`).
- **Once, at the consumer.** Unloading at a warehouse or a transfer station pays nothing. The payment is then split between the lines of the chain by the straight-line length of each leg (measured in game).
- **Late cargo is paid in full**: the travel time is not used (`cargotype.script.lua:7-13`). Being late lowers the town's Delivery rating instead.
- **Company rank** lowers all income with the **Inflation** setting: at rank 15, ×0.75 at Normal (`company_progression_util.tl:25-40`).
- A **completed subsidy** doubles, for 5 years, the income of the deliveries it covers: to its industry, to its town, or passengers between its two towns, on its lines only (`subvention_util.tl:286`). See [Subsidies](subsidies.html).

Details: [Cargo income and delivery time](income.html).

## What costs

- **Vehicles**: running costs follow average speed × capacity, and the price is 6 years of running costs (`model_metadata_util.lua:499-518`, `model_metadata_util.lua:548-549`).
- **Tracks and roads**: about one sixth of the build price per km and year; high-speed track costs 9 times simple track (`simple.street_template.lua:33`, `high_speed.street_template.lua:35`).
- **Depots, stations, warehouses, harbours, airports**: later era variants cost ×3 and ×9 (`rail_depot.con.lua:7`, `warehouse.tl:48`), and the upkeep of warehouses, harbours and airports also follows the year, ×1 in 1900 to ×6 in 2020 (`mod.script.tl:92-100`).
- **Loans**: the rate is charged once on the amount, spread over the term (`loan_util.tl:102-111`).
- **Inflation does not raise any cost**. It only lowers income.

Details: [Costs, upkeep and loans](costs.html).

## Six checks, in order

```diagram money_check
```

1. **Which lines lose money?** Look at each line's balance, not the company total. The [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) mod shows each line's balance over the last 12 months and its average over several years.
2. **Does the cargo go far?** Only the straight line from source to consumer pays. A short feeder to a warehouse gets only the share of its own short leg ([Cargo income and delivery time](income.html)).
3. **Does it run full?** A vehicle costs the same full or empty. Look at empty return trips, the **Fill Level** and **Full Load** of each stop ([Departure settings: full load, Fill Level and stop times](departure.html)).
4. **Is it unloaded where it pays?** What is not in a stop's Load list is unloaded into any stock nearby, a warehouse included, and a warehouse pays nothing ([Loading and unloading speed](loading.html), [Warehouses](warehouses.html)). Cargo that does not fit in full town stocks stays on board ([Town growth: XP, ratings and size](towns.html)).
5. **Too much vehicle?** Speed and capacity cost money, but speed does not pay: it only helps when it gives more trips a year. In town, an old slow bus can be more profitable than a new fast one ([Costs, upkeep and loans](costs.html)).
6. **Fixed costs.** Depots, extra warehouse modules, fast track and buildings of a later era cost every year, used or not ([Costs, upkeep and loans](costs.html)).

## Good to know

- **Choose cargos by volume and distance**, not by price: every cargo pays the same per km.
- A **long main line** fed by short lines earns most of the money; the feeders show small balances, but the chain as a whole is what counts.
- **More to carry**: a boosted industry produces more ([Workers and the workers boost](workers.html), [Industries](industries.html)), and a bigger town asks for more cargo.
- Speeding up a line does not raise the payment per item. It only helps if the same vehicles do more trips.

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks))
scripts: Same: straight line plus 8 × climb, the same factor for every cargo, travel time not used; measured in game: paid once at the consumer and split by leg length; costs follow speed × capacity for vehicles, 1/6 of the price for tracks, ×3 / ×9 era variants and ×1 to ×6 year factor for buildings; Inflation lowers only income.
result: refines
```
