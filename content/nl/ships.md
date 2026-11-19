---
title: Schepen en havens
summary: Kleine en grote schepen, welke haven welke schepen aanneemt, terminals en kosten van havens, en de lijst van alle schepen met hun vracht, capaciteit en snelheid.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
game: 40444
fact: 2 | scheepsgroottes: klein en groot
fact: 1, 2, 4 | terminals per haven
fact: 27 | schepen in het basisspel
fact: ×9 | prijs en onderhoud van de havenvariant van 1990
---

Elk schip is **klein** of **groot**. Een groot schip kan alleen aanmeren in een **grote haven**; een klein schip meert in beide aan. De gids in het spel zegt het ook: "Hou er rekening mee dat grote schepen alleen aan kunnen meren in grote havens."

```diagram ship_access
```

## Kleine en grote havens

- Twee havens in het bouwmenu: **Kleine passagiers- en vrachthaven** en **Grote passagiers- en vrachthaven**. Beide nemen passagiers en alle vracht aan (`harbor_modular.tl:92`, `harbor_modular.tl:122`).
- De kleine haven bestaat uit kleine pieren, die alleen kleine schepen aannemen (`small_pier.module.lua:7`). De grote haven gebruikt middelgrote pieren, die beide groottes aannemen (`medium_pier.module.lua:6`, `harbor_modular.script.lua:35-39`).
- **Terminals**: 1, 2 of 4, te kiezen bij het bouwen (`harbor_modular.tl:16`, `harbor_modular.script.lua:33`).
- Een pierterminal biedt plaats aan 100 wachtende passagiers op een kleine pier en 50 op een middelgrote pier (`modules.script.lua:872`, `modules.script.lua:1004`).
- Tijdens het plaatsen van een haven toont het script alleen de laag met bevaarbaar water (`harbor_modular.tl:26-30`). Waar een haven mag staan, bepaalt de engine.
- Elk schip legt zijn eigen grootte vast in zijn voertuigbestand; het spel maakt daar de modus klein of groot schip van (`model_metadata_util.lua:1411-1412`).

## Kosten

Er is één havenvariant per tijdperk: 1900, 1950 en 1990 (`harbor_modular.tl:71-73`). Prijs en onderhoud worden vermenigvuldigd met 3 voor een variant vanaf 1940 en met 9 voor een variant vanaf 1980 (`harbor_modular.tl:76`):

| Haven | Prijs (eerste variant) | Onderhoud per jaar (eerste variant) | Bron |
|---|---|---|---|
| Kleine haven | 144.000 - 444.000 | 24.000 - 74.000 | `harbor_modular.tl:88-89` |
| Grote haven | 228.000 - 678.000 | 38.000 - 113.000 | `harbor_modular.tl:118-119` |

- De twee waarden zijn de kleinste en de grootste indeling.
- Het onderhoud van havens volgt ook het kalenderjaar, ×1 in 1900 tot ×6 in 2020, net als bij opslagplaatsen en luchthavens ([Kosten, onderhoud en leningen](costs.html)).
- Havens maken lawaai en vervuilen: 180 tot 280 voor beide ([Vervuiling en geluidsoverlast](emission.html)).
- De prijs en gebruikskosten van een schip worden berekend uit zijn snelheid en capaciteit, net als bij wegvoertuigen en vliegtuigen ([Kosten, onderhoud en leningen](costs.html)).

## Alle schepen

Snelheid in km/u, afgerond. "Vracht" toont de vrachtklassen uit het voertuigbestand; "alle vracht" betekent elk vrachttype. De capaciteit is het totaal dat de voertuigwinkel toont: de som van de compartimenten, elk met zijn grootste laadconfiguratie (`vehicle_store_util.tl:70-95`).

| Schip | Jaren | Grootte | Vracht | Capaciteit | Snelheid | Laadsnelheid |
|---|---|---|---|---|---|---|
| Dunara Castle | 1875-1930 | groot | passagiers, alle vracht | **160** (2 × 80) | 20 | 20 |
| Canadese trawler | 1884-1948 | klein | alle vracht | 40 | 35 | 10 |
| Waimarie | 1889-1940 | klein | passagiers | 80 | 30 | 15 |
| Sydfart | 1900-1930 | klein | vloeibaar, laadbak, goederen, bulk | 80 | 30 | 20 |
| PS Trillium | 1910-1955 | groot | passagiers | 200 | 35 | 15 |
| Hekwieler | 1915-1960 | klein | passagiers, alle vracht | **120** (2 × 60) | 40 | 10 |
| Terra Nova | 1925-1975 | groot | bulk, laadbak, goederen | **200** (2 × 100) | 45 | 30 |
| Votrans (tankerduwboot) | 1935-1990 | klein | vloeibaar | 120 | 33 | 20 |
| Votrans (vrachtduwboot) | 1935-1990 | klein | bulk, laadbak, goederen | 120 | 33 | 20 |
| MS Stadt Kiel | 1943-1990 | klein | passagiers | 80 | 30 | 20 |
| Borealis | 1948-1994 | klein | alle vracht | 60 | 38 | 20 |
| Wopper | 1950-2005 | klein | vloeibaar, laadbak, goederen, bulk | 160 | 30 | 25 |
| Meridian (veerboot) | 1956-2011 | klein | passagiers | 240 | 30 | 15 |
| Cap Arkona | 1965-2010 | groot | passagiers | 200 | 40 | 20 |
| Tora-coaster | 1970-2020 | groot | vloeibaar, laadbak, goederen, bulk | 320 | 40 | 25 |
| AP1-88 Hovercraft | 1980- | klein | passagiers | 240 | 90 | 15 |
| Hercules XI (duwboot) | 1990- | groot | laadbak, goederen, bulk | **240** (2 × 120) | 32 | 20 |
| Baltica | 1994- | klein | alle vracht | 80 | 40 | 20 |
| HADAG Type 2000 | 1995- | klein | passagiers | 100 | 35 | 25 |
| Damen Tanker 800 | 1996- | klein | vloeibaar | **320** (2 × 160) | 28 | 30 |
| Damen Fast Ferry | 2003- | groot | passagiers | 220 | 75 | 20 |
| Luise Deymann | 2013- | groot | vloeibaar | **480** (2 × 240) | 30 | 35 |
| MS Diamant | 2013- | groot | passagiers | 280 | 45 | 35 |
| Virgo (duwboot) | 2015- | groot | laadbak, goederen, bulk | **320** (2 × 160) | 40 | 15 |
| GHL Oita Hovercraft | 2023- | klein | passagiers | 320 | 100 | 20 |
| Yara Birkeland | 2030- | groot | laadbak, goederen, bulk | 480 | 42 | 10 |
| Solar Shuttle | 2035- | klein | passagiers | 80 | 30 | 30 |

## Goed om te weten

- **Controleer de grootte voordat je een kleine haven bouwt.** Meerdere van de grootste vrachtschepen (Tora, Virgo, Yara Birkeland) zijn groot en meren daar niet aan.
- **"Geen route voor grote schepen"** is een aparte waarschuwing voor grote schepen: het spel vond geen waterroute die een groot schip kan gebruiken. Welk water open is voor welke grootte, bepaalt de game-engine, niet de scripts; die tonen alleen de waarschuwing (`vehicle_warning.script.tl:28-36`).
- **Scheepsroutepunten** moeten op water worden geplaatst ("Scheepsroutepunten moeten op het water zijn.").
- De scheepswerf en het scheepsonderhoudsstation zijn aparte gebouwen; onderhoud werkt in een straal eromheen ([Voertuigen: staat, leeftijd en laadsnelheid](vehicles.html)).

```check
official: "Passenger and cargo ships are available in two sizes: small and large. Large ships can only dock at large harbors, so make sure the harbor matches the size of the ships assigned to the line." (in-game guide "Water Infrastructure")
scripts: Hetzelfde: kleine pieren nemen alleen SMALL_SHIP aan, middelgrote pieren SHIP en SMALL_SHIP; beide havens nemen passagiers en alle vracht aan; 1, 2 of 4 terminals; drie tijdperkvarianten met ×1 / ×3 / ×9; 16 kleine en 11 grote schepen in het basisspel.
result: refines
```
