---
title: Streets, tracks, bridges and signals
summary: Speed, price and upkeep of every track and street type, what bridges, tunnels, crossings and signals cost and allow, what alleys and noise barriers really change, and where depots are explained.
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40444
fact: 100 / 160 / 350 km/h | simple, standard and high-speed track
fact: ×9 | price and upkeep of high-speed track compared with simple track
fact: +30 % | price of catenary on a track
fact: −65 % | noise of a street or track with a noise barrier
---

Each street and track type has a top speed, a price per metre and an upkeep per metre and year, all written in its file. Bridges, crossings and some street decorations add their own speed limit. The costs below are at **Infrastructure Costs** and **Infrastructure Upkeep** 100 % (see [Costs, upkeep and loans](costs.html)).

## Tracks

| Track | From | Top speed | Build per km | Upkeep per km and year | Source |
|---|---|---|---|---|---|
| Simple Tracks | start | 100 km/h | 60,000 | 10,000 | `simple.street_template.lua:9`, `simple.street_template.lua:28`, `simple.street_template.lua:33` |
| Standard Tracks | 1930 | 160 km/h | 180,000 | 30,000 | `standard.street_template.lua:4`, `standard.street_template.lua:11`, `standard.street_template.lua:30`, `standard.street_template.lua:35` |
| High-Speed Tracks | 1980 | 350 km/h | 540,000 | 90,000 | `high_speed.street_template.lua:4`, `high_speed.street_template.lua:11`, `high_speed.street_template.lua:30`, `high_speed.street_template.lua:35` |

- **Catenary** costs **30 %** more than the track (`mod.script.tl:24-25`). It is available from 1921 on simple track and from the start of each newer type (`simple_catenary.street_template.lua:4`). It costs nothing extra per year in the files: the electric variant has the same upkeep (`simple_catenary.street_template.lua:34`).
- All three types allow the same incline and curves: **8.5 %** when you build (the Incline slider goes up to that), 13 % at most for the shape of the track, and a curve radius of 55 m when you build, 40 m at least (`standard.street_template.lua:36-37`, `standard.street_template.lua:48-49`, `construction_react_util.tl:241-242`, `construction_react_util.tl:1824`).
- Pollution of the track itself grows with its type: 2, 4 and 6 (`simple.street_template.lua:18`, `standard.street_template.lua:20`, `high_speed.street_template.lua:20`).

```engine
How much a curve lowers the speed of a train (the speedCoeffs of each track type) and what speed the build tool shows for a curve are computed by the engine.
```

```tip scripts
High-speed track costs 9 times simple track, to build and every year. Lay it only where trains really run faster than 160 km/h; standard track is enough elsewhere, and simple track for slow freight branches.
```

## Streets

| Street | Years | Top speed | Build per km | Upkeep per km and year | Source |
|---|---|---|---|---|---|
| Narrow Street (old) | until 1940 | 20 km/h | 36,000 | 6,000 | `town_old_xsmall.street_template.lua:4-5`, `town_old_xsmall.street_template.lua:8`, `town_old_xsmall.street_template.lua:27`, `town_old_xsmall.street_template.lua:56` |
| Small Street (old) | until 1940 | 40 km/h | 60,000 | 10,000 | `town_old_small.street_template.lua:8`, `town_old_small.street_template.lua:27`, `town_old_small.street_template.lua:56` |
| Large Street (old) | until 1940 | 60 km/h | 180,000 | 30,000 | `town_old_large.street_template.lua:8`, `town_old_large.street_template.lua:27`, `town_old_large.street_template.lua:88` |
| Narrow Street (new) | from 1940 | 30 km/h | 120,000 | 20,000 | `town_new_xsmall.street_template.lua:4`, `town_new_xsmall.street_template.lua:11`, `town_new_xsmall.street_template.lua:30`, `town_new_xsmall.street_template.lua:59` |
| Small Street (new) | from 1940 | 50 km/h | 180,000 | 30,000 | `town_new_small.street_template.lua:11`, `town_new_small.street_template.lua:30`, `town_new_small.street_template.lua:59` |
| Medium Street (new) | from 1940 | 50 km/h | 360,000 | 60,000 | `town_new_medium.street_template.lua:11`, `town_new_medium.street_template.lua:30`, `town_new_medium.street_template.lua:75` |
| Large Street (new) | from 1940 | 60 km/h | 540,000 | 90,000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:30`, `town_new_large.street_template.lua:91` |
| Small Country Road (old) | until 1940 | 60 km/h | 60,000 | 10,000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:29`, `country_old_small.street_template.lua:58` |
| Small Country Road (new) | from 1940 | 80 km/h | 180,000 | 30,000 | `country_new_small.street_template.lua:10`, `country_new_small.street_template.lua:31`, `country_new_small.street_template.lua:60` |
| One-Lane Highway | from 1940 | 100 km/h | 180,000 | 30,000 | `highway_new_small.street_template.lua:10`, `highway_new_small.street_template.lua:32`, `highway_new_small.street_template.lua:53` |
| Two-Lane Highway | from 1940 | 120 km/h | 360,000 | 60,000 | `highway_new_medium.street_template.lua:10`, `highway_new_medium.street_template.lua:32`, `highway_new_medium.street_template.lua:61` |
| Three-Lane Highway | from 1940 | 120 km/h | 540,000 | 90,000 | `highway_new_large.street_template.lua:10`, `highway_new_large.street_template.lua:32`, `highway_new_large.street_template.lua:69` |
| Tram Tracks (old) | until 1910 | 40 km/h | 36,000 | 6,000 | `tram_old.street_template.lua:4-5`, `tram_old.street_template.lua:8`, `tram_old.street_template.lua:27`, `tram_old.street_template.lua:40` |
| Tram Tracks (new) | from 1925 | 100 km/h | 120,000 | 20,000 | `tram_new.street_template.lua:4`, `tram_new.street_template.lua:9`, `tram_new.street_template.lua:29`, `tram_new.street_template.lua:42` |

- The **1940 change** makes town streets 10 km/h faster but **three times** as expensive, to build and every year: a small street goes from 60,000 to 180,000 per km.
- The medium and large variants of country roads cost 2 and 3 times the small one, at the same speed (`country_new_large.street_template.lua:10`, `country_new_large.street_template.lua:31`).
- Adding to a street: a **bus lane** +10 %, a **tram track** +20 %, an **electric tram track** +40 % of the street price (`mod.script.tl:24-28`).
- The player usually does not own streets, even those built by the player; the street tools can change who owns a street (official wiki). Who pays the upkeep of a street is decided by the engine.

## Alleys and noise barriers

| Tool | Noise | Pollution | Top speed | Where | Source |
|---|---|---|---|---|---|
| Alley Tool (trees) | −10 % | −50 % | **−25 %** | streets with a sidewalk, not on bridges or in tunnels | `alley.edge.lua:39-40`, `alley.edge.lua:53-56` |
| Noise Barrier Tool | −65 % | no change | no change | streets and tracks, not in tunnels | `barrier_b.edge.lua:43`, `barrier_b.edge.lua:47`, `barrier_track_b.edge.lua:43` |

- Both cost 100 and 10 a year in their files, like a street per metre (`alley.edge.lua:8`, `alley.edge.lua:12`, `barrier_b.edge.lua:7`, `barrier_b.edge.lua:11`).
- The street types "with trees" and "with barriers" of the build menu are the same streets with these decorations already on them (`town_new_medium_trees.street_template.lua:12-14`). The build menu adds up their effects (`construction_react_util.tl:2119-2142`).
- So a street with trees is **a quarter slower**: a new medium street with trees allows about 38 km/h instead of 50.

```tip scripts
Against noise, use the Noise Barrier: −65 % and no speed loss. Trees are the tool against pollution (−50 %), but they slow the street by a quarter.
```

How towns rate noise and pollution: [Pollution and noise](emission.html).

## Bridges and tunnels

| Bridge | Years | Top speed | For | Base price | Source |
|---|---|---|---|---|---|
| Stone Bridge | from the start | 90 km/h | tracks, streets | 200 | `stone.bridge.lua:169-170`, `stone.bridge.lua:181-183`, `stone.bridge.lua:193` |
| Trestle Bridge | until 1970 | 60 km/h | one type for tracks, one for streets | 100 | `trestle.bridge.lua:200-201`, `trestle.bridge.lua:212-214`, `trestle.bridge.lua:226`, `trestle_s.bridge.lua:212` |
| Steel Bridge | from 1940 | 140 km/h | tracks, streets | 200 | `steel.bridge.lua:243`, `steel.bridge.lua:259`, `steel.bridge.lua:269` |
| Suspension Bridge | from 1940 | 180 km/h | tracks, streets | 600 | `suspension.bridge.lua:277`, `suspension.bridge.lua:294`, `suspension.bridge.lua:304` |
| Concrete Bridge | from 1970 | 280 km/h | tracks, streets | 200 | `concrete.bridge.lua:162`, `concrete.bridge.lua:176`, `concrete.bridge.lua:187` |
| Cable-Stayed Bridge | from 2000 | 220 km/h | tracks, streets | 750 | `cable.bridge.lua:214`, `cable.bridge.lua:231`, `cable.bridge.lua:240` |
| Tied Arch Bridge | from 2010 | 350 km/h | tracks, streets | 650 | `tarch.bridge.lua:253`, `tarch.bridge.lua:270`, `tarch.bridge.lua:280` |

- The bridge limit applies **on top of** the track's: a high-speed line over a steel bridge runs at 140 km/h there. Before 1970 no bridge allows more than 180 km/h, before 2010 none allows 350 km/h.
- **Tunnels** (Rock Tunnel, Concrete Tunnel from 1970) have **no speed limit** in their files, and the same base price of 600 (`tunnel_a.tunnel.lua:187-188`, `tunnel_a_car.tunnel.lua:185`, `tunnel_b.tunnel.lua:191-194`).
- Bridge and tunnel prices follow Infrastructure Costs (`post_run_util.tl:50-51`).

```engine
The base price of a bridge or tunnel is turned into a price per metre by the engine, with the height or depth (costFactors); the official wiki says it depends on the length and the height above ground or the depth below it. The same base price can therefore give very different bills. Tunnels cost the town Reputation (see [Reputation](reputation.html)).
```

```tip scripts
For a fast line across a valley before 1970, a suspension bridge (180 km/h) is the only bridge faster than 140 km/h; a tunnel has no limit at all.
```

## Level crossings and signals

| What | Years | Top speed of the track | Price | Source |
|---|---|---|---|---|
| Simple Crossing | 1850 - 1925 | 120 km/h | 4,000 | `era_a_eu.rcr.lua:14-17`, `era_a_eu.rcr.lua:26` |
| Half-Barrier Crossing | 1925 - 1975 | 160 km/h | 16,000 | `era_b_eu.rcr.lua:15-18`, `era_b_eu.rcr.lua:27` |
| Modern Half-Barrier Crossing | from 1975 | 160 km/h | 16,000 | `era_c_eu.rcr.lua:15-17`, `era_c_eu.rcr.lua:26` |
| Path Signal (semaphore until 1950, light from 1950) | all | - | 9,000, upkeep 1,500 a year | `signal_path_a.con.lua:4-5`, `signal_path_a.con.lua:10-11`, `signal_path_c.con.lua:4-5` |

- A level crossing caps the track at 160 km/h at most: high-speed lines need bridges or tunnels over streets.
- Every signal can be set **One-Way** (`signal_path_a.con.lua:51-52`). How signals divide the track into blocks is explained in the official wiki's Railway Signals page.

## Depots and maintenance stations

What depots and maintenance stations cost, how many vehicles they serve and in what radius: [Lines and vehicles](vehicles.html) and [Costs, upkeep and loans](costs.html).

## Good to know

- Before 1940, upgrading town streets is cheap; after 1940 each new or rebuilt town street costs three times as much and three times the upkeep.
- On a fast line, check every bridge and level crossing: the slowest one sets the speed there.
- Speed only pays when it gives more trips (see [Why am I losing money?](money.html)).

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. … Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: Same speeds as the official tables for tracks, streets and bridges. In the files bridge limits also apply to streets, tunnels have none, level crossings cap tracks at 120 or 160 km/h, trees slow a street by 25 % and cut pollution by 50 % but noise only by 10 %, while noise barriers cut noise by 65 % without slowing.
result: refines
```
