---
title: Straten, sporen, bruggen en seinen
summary: Snelheid, prijs en onderhoud van elk spoor- en straattype, wat bruggen, tunnels, overwegen en seinen kosten en toestaan, wat lanen en geluidsschermen echt veranderen, en waar depots worden uitgelegd.
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40444
fact: 100 / 160 / 350 km/h | eenvoudig spoor, standaardspoor en hogesnelheidslijn
fact: ×9 | prijs en onderhoud van een hogesnelheidslijn vergeleken met eenvoudig spoor
fact: +30 % | prijs van een bovenleiding op een spoor
fact: -65 % | geluid van een straat of spoor met een geluidsscherm
---

Elk straat- en spoortype heeft een topsnelheid, een prijs per meter en een onderhoud per meter en jaar, allemaal in zijn bestand. Bruggen, overwegen en sommige straatversieringen voegen hun eigen snelheidslimiet toe. De kosten hieronder gelden bij **Kosten infrastructuur** en **Onderhoud infrastructuur** 100 % (zie [Kosten, onderhoud en leningen](costs.html)).

## Sporen

| Spoor | Vanaf | Topsnelheid | Bouw per km | Onderhoud per km en jaar | Bron |
|---|---|---|---|---|---|
| Eenvoudig spoor | start | 100 km/h | 60.000 | 10.000 | `simple.street_template.lua:9`, `simple.street_template.lua:28`, `simple.street_template.lua:33` |
| Standaardspoor | 1930 | 160 km/h | 180.000 | 30.000 | `standard.street_template.lua:4`, `standard.street_template.lua:11`, `standard.street_template.lua:30`, `standard.street_template.lua:35` |
| Hogesnelheidslijn | 1980 | 350 km/h | 540.000 | 90.000 | `high_speed.street_template.lua:4`, `high_speed.street_template.lua:11`, `high_speed.street_template.lua:30`, `high_speed.street_template.lua:35` |

- Een **bovenleiding** kost **30 %** meer dan het spoor (`mod.script.tl:24-25`). Ze is beschikbaar vanaf 1921 op eenvoudig spoor en vanaf de start van elk nieuwer type (`simple_catenary.street_template.lua:4`). Volgens de bestanden kost ze per jaar niets extra: de elektrische variant heeft hetzelfde onderhoud (`simple_catenary.street_template.lua:34`).
- Alle drie de typen staan dezelfde helling en bochten toe: **8,5 %** bij het bouwen (de schuifregelaar Hoek gaat tot daar), hooguit 13 % voor de vorm van het spoor, en een bochtstraal van 55 m bij het bouwen, minstens 40 m (`standard.street_template.lua:36-37`, `standard.street_template.lua:48-49`, `construction_react_util.tl:241-242`, `construction_react_util.tl:1824`).
- De vervuiling van het spoor zelf stijgt met het type: 2, 4 en 6 (`simple.street_template.lua:18`, `standard.street_template.lua:20`, `high_speed.street_template.lua:20`).

```engine
Hoeveel een bocht de snelheid van een trein verlaagt (de speedCoeffs van elk spoortype) en welke snelheid het bouwgereedschap voor een bocht toont, berekent de engine.
```

```tip scripts
Een hogesnelheidslijn kost 9 keer zoveel als eenvoudig spoor, bij de bouw en elk jaar. Leg ze alleen waar treinen echt sneller dan 160 km/h rijden; elders volstaat standaardspoor, en eenvoudig spoor voor trage goederenzijlijnen.
```

## Straten

| Straat | Jaren | Topsnelheid | Bouw per km | Onderhoud per km en jaar | Bron |
|---|---|---|---|---|---|
| Smalle straat (oud) | tot 1940 | 20 km/h | 36.000 | 6.000 | `town_old_xsmall.street_template.lua:4-5`, `town_old_xsmall.street_template.lua:8`, `town_old_xsmall.street_template.lua:27`, `town_old_xsmall.street_template.lua:56` |
| Kleine straat (oud) | tot 1940 | 40 km/h | 60.000 | 10.000 | `town_old_small.street_template.lua:8`, `town_old_small.street_template.lua:27`, `town_old_small.street_template.lua:56` |
| Grote straat (oud) | tot 1940 | 60 km/h | 180.000 | 30.000 | `town_old_large.street_template.lua:8`, `town_old_large.street_template.lua:27`, `town_old_large.street_template.lua:88` |
| Smalle straat (nieuw) | vanaf 1940 | 30 km/h | 120.000 | 20.000 | `town_new_xsmall.street_template.lua:4`, `town_new_xsmall.street_template.lua:11`, `town_new_xsmall.street_template.lua:30`, `town_new_xsmall.street_template.lua:59` |
| Kleine straat (nieuw) | vanaf 1940 | 50 km/h | 180.000 | 30.000 | `town_new_small.street_template.lua:11`, `town_new_small.street_template.lua:30`, `town_new_small.street_template.lua:59` |
| Middelgrote straat (nieuw) | vanaf 1940 | 50 km/h | 360.000 | 60.000 | `town_new_medium.street_template.lua:11`, `town_new_medium.street_template.lua:30`, `town_new_medium.street_template.lua:75` |
| Grote straat (nieuw) | vanaf 1940 | 60 km/h | 540.000 | 90.000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:30`, `town_new_large.street_template.lua:91` |
| Kleine autoweg (oud) | tot 1940 | 60 km/h | 60.000 | 10.000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:29`, `country_old_small.street_template.lua:58` |
| Kleine autoweg (nieuw) | vanaf 1940 | 80 km/h | 180.000 | 30.000 | `country_new_small.street_template.lua:10`, `country_new_small.street_template.lua:31`, `country_new_small.street_template.lua:60` |
| Eenbaans-snelweg | vanaf 1940 | 100 km/h | 180.000 | 30.000 | `highway_new_small.street_template.lua:10`, `highway_new_small.street_template.lua:32`, `highway_new_small.street_template.lua:53` |
| Tweebaans-snelweg | vanaf 1940 | 120 km/h | 360.000 | 60.000 | `highway_new_medium.street_template.lua:10`, `highway_new_medium.street_template.lua:32`, `highway_new_medium.street_template.lua:61` |
| Driebaans-snelweg | vanaf 1940 | 120 km/h | 540.000 | 90.000 | `highway_new_large.street_template.lua:10`, `highway_new_large.street_template.lua:32`, `highway_new_large.street_template.lua:69` |
| Tramspoor (oud) | tot 1910 | 40 km/h | 36.000 | 6.000 | `tram_old.street_template.lua:4-5`, `tram_old.street_template.lua:8`, `tram_old.street_template.lua:27`, `tram_old.street_template.lua:40` |
| Tramspoor (nieuw) | vanaf 1925 | 100 km/h | 120.000 | 20.000 | `tram_new.street_template.lua:4`, `tram_new.street_template.lua:9`, `tram_new.street_template.lua:29`, `tram_new.street_template.lua:42` |

- De **wissel van 1940** maakt stadsstraten 10 km/h sneller maar **drie keer** zo duur, bij de bouw en elk jaar: een kleine straat gaat van 60.000 naar 180.000 per km.
- De middelgrote en grote varianten van autowegen kosten 2 en 3 keer de kleine, bij dezelfde snelheid (`country_new_large.street_template.lua:10`, `country_new_large.street_template.lua:31`).
- Toevoegingen aan een straat: een **busbaan** +10 %, een **tramspoor** +20 %, een **elektrisch tramspoor** +40 % van de straatprijs (`mod.script.tl:24-28`).
- De speler bezit straten meestal niet, ook niet die hij zelf heeft gebouwd; met het straatgereedschap kun je de eigenaar van een straat wijzigen (officiële wiki). Wie het onderhoud van een straat betaalt, beslist de engine.

## Lanen en geluidsschermen

| Gereedschap | Geluid | Vervuiling | Topsnelheid | Waar | Bron |
|---|---|---|---|---|---|
| Laantool (bomen) | -10 % | -50 % | **-25 %** | straten met een stoep, niet op bruggen of in tunnels | `alley.edge.lua:39-40`, `alley.edge.lua:53-56` |
| Geluidsschermtool | -65 % | geen verandering | geen verandering | straten en sporen, niet in tunnels | `barrier_b.edge.lua:43`, `barrier_b.edge.lua:47`, `barrier_track_b.edge.lua:43` |

- Beide kosten in hun bestanden 100 en 10 per jaar, zoals een straat per meter (`alley.edge.lua:8`, `alley.edge.lua:12`, `barrier_b.edge.lua:7`, `barrier_b.edge.lua:11`).
- De straattypen "met bomen" en "met schermen" in het bouwmenu zijn dezelfde straten met deze versieringen er al op (`town_new_medium_trees.street_template.lua:12-14`). Het bouwmenu telt hun effecten op (`construction_react_util.tl:2119-2142`).
- Een straat met bomen is dus **een kwart trager**: een nieuwe middelgrote straat met bomen staat ongeveer 38 km/h toe in plaats van 50.

```tip scripts
Tegen geluid gebruik je het geluidsscherm: -65 % en geen snelheidsverlies. Bomen zijn het middel tegen vervuiling (-50 %), maar ze maken de straat een kwart trager.
```

Hoe steden geluid en vervuiling beoordelen: [Vervuiling en geluid](emission.html).

## Bruggen en tunnels

| Brug | Jaren | Topsnelheid | Voor | Basisprijs | Bron |
|---|---|---|---|---|---|
| Stenen brug | vanaf de start | 90 km/h | sporen, straten | 200 | `stone.bridge.lua:169-170`, `stone.bridge.lua:181-183`, `stone.bridge.lua:193` |
| Schraagbrug | tot 1970 | 60 km/h | één type voor sporen, één voor straten | 100 | `trestle.bridge.lua:200-201`, `trestle.bridge.lua:212-214`, `trestle.bridge.lua:226`, `trestle_s.bridge.lua:212` |
| Stalen brug | vanaf 1940 | 140 km/h | sporen, straten | 200 | `steel.bridge.lua:243`, `steel.bridge.lua:259`, `steel.bridge.lua:269` |
| Ophangbrug | vanaf 1940 | 180 km/h | sporen, straten | 600 | `suspension.bridge.lua:277`, `suspension.bridge.lua:294`, `suspension.bridge.lua:304` |
| Betonnen brug | vanaf 1970 | 280 km/h | sporen, straten | 200 | `concrete.bridge.lua:162`, `concrete.bridge.lua:176`, `concrete.bridge.lua:187` |
| Tuibrug | vanaf 2000 | 220 km/h | sporen, straten | 750 | `cable.bridge.lua:214`, `cable.bridge.lua:231`, `cable.bridge.lua:240` |
| Verstijfde staafboogbrug | vanaf 2010 | 350 km/h | sporen, straten | 650 | `tarch.bridge.lua:253`, `tarch.bridge.lua:270`, `tarch.bridge.lua:280` |

- De limiet van de brug geldt **bovenop** die van het spoor: een hogesnelheidslijn over een stalen brug rijdt daar 140 km/h. Vóór 1970 staat geen enkele brug meer dan 180 km/h toe, vóór 2010 geen enkele 350 km/h.
- **Tunnels** (Stenen tunnel, Betonnen tunnel vanaf 1970) hebben in hun bestanden **geen snelheidslimiet**, en dezelfde basisprijs van 600 (`tunnel_a.tunnel.lua:187-188`, `tunnel_a_car.tunnel.lua:185`, `tunnel_b.tunnel.lua:191-194`).
- Brug- en tunnelprijzen volgen Kosten infrastructuur (`post_run_util.tl:50-51`).

```engine
De basisprijs van een brug of tunnel wordt door de engine omgezet in een prijs per meter, met de hoogte of diepte (costFactors); de officiële wiki zegt dat die afhangt van de lengte en de hoogte boven de grond of de diepte eronder. Dezelfde basisprijs kan dus heel verschillende rekeningen geven. Tunnels kosten de stad Reputatie (zie [Reputatie](reputation.html)).
```

```tip scripts
Voor een snelle lijn over een dal vóór 1970 is een ophangbrug (180 km/h) de enige brug die sneller is dan 140 km/h; een tunnel heeft helemaal geen limiet.
```

## Overwegen en seinen

| Wat | Jaren | Topsnelheid van het spoor | Prijs | Bron |
|---|---|---|---|---|
| Eenvoudige overweg | 1850 - 1925 | 120 km/h | 4.000 | `era_a_eu.rcr.lua:14-17`, `era_a_eu.rcr.lua:26` |
| Overweg met halve overwegbomen | 1925 - 1975 | 160 km/h | 16.000 | `era_b_eu.rcr.lua:15-18`, `era_b_eu.rcr.lua:27` |
| Moderne overweg met halve overwegbomen | vanaf 1975 | 160 km/h | 16.000 | `era_c_eu.rcr.lua:15-17`, `era_c_eu.rcr.lua:26` |
| Sein (armsein tot 1950, lichtsein vanaf 1950) | alle | - | 9.000, onderhoud 1.500 per jaar | `signal_path_a.con.lua:4-5`, `signal_path_a.con.lua:10-11`, `signal_path_c.con.lua:4-5` |

- Een overweg beperkt het spoor tot hooguit 160 km/h: hogesnelheidslijnen hebben bruggen of tunnels over straten nodig.
- Elk sein kan op **Eenrichtingsverkeer** worden gezet (`signal_path_a.con.lua:51-52`). Hoe seinen het spoor in blokken verdelen, staat op de pagina Railway Signals van de officiële wiki.

## Depots en onderhoudsstations

Wat depots en onderhoudsstations kosten, hoeveel voertuigen ze bedienen en in welke straal: [Lijnen en voertuigen](vehicles.html) en [Kosten, onderhoud en leningen](costs.html).

## Goed om te weten

- Vóór 1940 is het opwaarderen van stadsstraten goedkoop; na 1940 kost elke nieuwe of herbouwde stadsstraat drie keer zoveel en drie keer zoveel onderhoud.
- Controleer op een snelle lijn elke brug en elke overweg: de traagste bepaalt daar de snelheid.
- Snelheid loont alleen als ze meer ritten oplevert (zie [Waarom verlies ik geld?](money.html)).

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: Dezelfde snelheden als de officiële tabellen voor sporen, straten en bruggen. In de bestanden gelden bruglimieten ook voor straten, tunnels hebben er geen, overwegen beperken sporen tot 120 of 160 km/h, bomen maken een straat 25 % trager en verlagen de vervuiling met 50 % maar het geluid maar met 10 %, terwijl geluidsschermen het geluid met 65 % verlagen zonder te vertragen.
result: refines
```
