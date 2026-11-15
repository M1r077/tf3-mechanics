---
title: Speltijd en kalender
summary: Spelsnelheid en kalendersnelheid zijn twee verschillende dingen. Hoe lang een dag en een jaar duren, wat een tragere of gepauzeerde kalender verandert, en wat niet.
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
fact: 4 s | één kalenderdag bij kalendersnelheid ×1, spelsnelheid 1x
fact: ≈ 24 min | één kalenderjaar bij dezelfde snelheden
fact: 0 ×0,25 ×0,5 ×1 ×2 ×4 | stappen van de kalendersnelheid
fact: 0 1x 2x 4x | stappen van de spelsnelheid
---

Het spel heeft **twee klokken**. De **spelsnelheid** (pauze, 1x, 2x, 4x) laat alles sneller lopen: voertuigen, productie, steden. De **kalendersnelheid** bepaalt alleen hoe snel de datum loopt. Bijna elke regel van het spel telt in speltijd, niet in kalenderdagen.

## De twee instellingen

| Instelling | Stappen | Wat het verandert | Bron |
|---|---|---|---|
| **Spelsnelheid** | Pauzeren, 1x, 2x, 4x | hoe snel de hele simulatie loopt | `game_bar_widgets.tl:199-203` |
| **Kalendersnelheid** | Gepauzeerd, ×0.25, ×0.5, ×1, ×2, ×4 | hoeveel speltijdseconden één dag duurt | `game_bar_widgets.tl:321-335`, `game_bar_widgets.tl:351` |

- Bij kalendersnelheid ×1 duurt een dag **4 seconden** speltijd (officiële wiki), dus een maand duurt ongeveer 2 minuten en een jaar ongeveer **24 minuten** bij 1x. Gemeten met het [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard): 4,0 s per dag bij ×1, 1 s bij ×4, 8 s bij ×0.5, 16 s bij ×0.25.
- ×4 laat de datum vier keer sneller lopen; **Gepauzeerd** stopt de datum, de simulatie gaat door.
- 2x en 4x zijn een maximum: het spel verlaagt ze als de computer het niet bijhoudt (`game.tl:636-642`). Gemeten: 2x gaf gemiddeld 1,9x, 4x gaf 3,6x.
- Het **Tijdstip** en het weer zijn een derde, visuele klok: standaard veranderen ze vanzelf, los van de kalender (`game_time_config.res.lua:5`, `weather_config.res.lua:5`).

## Wat speltijd volgt, los van de kalender

Deze worden in speltijd geteld, dus een tragere of gepauzeerde kalender vertraagt ze niet:

- **Productie**: de productietijd van een industrie is een vast deel van een standaardjaar (`industry_react_util.tl:51`). Het industrievenster toont die in dagen van de huidige kalender (`industry_react_util.tl:23`): bij ×0.25 toont hetzelfde tempo een kwart van de dagen.
- **Aflossingen van leningen**: één per standaardmaand speltijd, ook met een gepauzeerde kalender (`loan.script.tl:83-88`).
- **Deadlines van subsidies** en de ×2-inkomstenbonus (`subvention_util.tl:290-292`).
- **Herstel van de reputatie van steden** (`towns.script.tl:121-130`), **arbeidersboosts** (`industry_productivity_util.tl:3`) en **sluiting van industrieën** na jaren zonder bediening (`industries.script.tl:119-128`).
- **Leveringsbeoordelingen** van steden, over het laatste halfjaar (`town_util.tl:840`).

Met een lopende kalender toont het spel deze tijdsduren in jaren, maanden en dagen van de huidige kalendersnelheid (`util.tl:40-49`).

## Wat de kalenderdatum volgt

- **Nieuwe voertuigen, stations en gebouwen** verschijnen per jaar (officiële wiki: "Different calendar speeds only affect the availability of vehicles and infrastructure").
- **Kosten die met het jaar stijgen**: onderhoud van gebouwen, varianten per tijdperk, subsidiebedragen en leningbedragen volgen de datum. Details: [Kosten, onderhoud en leningen](costs.html).

## Met een gepauzeerde kalender

1. De datum en dus het jaar blijven vast: geen nieuwe voertuigen, en de kosten per jaar blijven waar ze zijn.
2. Tijdsduren worden getoond in **minuten en seconden** in plaats van dagen (`util.tl:41-43`, `industry_react_util.tl:16-21`).
3. Een lening toont haar aflossing **per min.** in plaats van per jaar (`finances_loan_gui.tl:223-231`), en de aangepaste lening kan niet worden afgesloten (`finances_loan_gui.tl:393`).
4. Productie, betalingen, deadlines en reputatie houden hun tempo in speltijd.

## Goed om te weten

- Wil je meer tijd om een netwerk te laten groeien voordat nieuwe voertuigen komen? Verlaag de kalendersnelheid: je inkomsten per spelminuut veranderen niet.
- Productie "per jaar" hangt af van de kalendersnelheid; vergelijk industrieën bij dezelfde snelheid.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) houdt de financiële grafieken leesbaar met een gepauzeerde kalender.

```engine
De lengte van de standaarddag, -maand en -jaar (getDefaultDayDuration en de andere) komt van de engine. Het stadsscript telt een maand als 30 × 4 seconden (`towns.script.tl:121`), wat past bij de gemeten dag van 4 seconden; een paar andere constanten gaan nog uit van een dag van 2 seconden (`cargotype.script.lua:3`, `mod.script.tl:172`).
```

```check
official: "By default a day in the game lasts 4 seconds." "Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent." ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: Kalendersnelheid ×0.25 tot ×4 of gepauzeerd, ten opzichte van de standaarddag; productie, leningen, subsidies, reputatie en arbeiderstimers lopen op speltijd; een gepauzeerde kalender toont tijdsduren in minuten, betalingen per minuut en blokkeert nieuwe leningen; gemeten: 4 s per dag bij ×1.
result: refines
```
