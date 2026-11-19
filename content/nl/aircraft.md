---
title: Vliegtuigen, luchthavens en helikopters
summary: Vliegveld of luchthaven, welk vliegtuig waar landt, terminals, de tweede landingsbaan, heliports, en de lijst van alle luchtvaartuigen met hun vracht, capaciteit en snelheid.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
game: 40444
fact: 2 | vliegtuiggroottes: klein en groot
fact: 1950 | eerste luchthaven en eerste helikopters
fact: 1980 | tweede landingsbaan
fact: 5 | luchtvaartuigen per hangar
---

Elk vliegtuig is **klein** of **groot**. Een **vliegveld** neemt alleen kleine vliegtuigen aan; een **luchthaven** neemt beide aan, en helikopters bij het hoofdgebouw. Helikopters hebben ook eigen stations.

```diagram air_access
```

## Vliegveld en luchthaven

- **Vliegveld**: "Geschikt voor kleine vliegtuigen." Varianten vanaf 1920, 1950 en 1980; 1, 2 of 3 terminals en een optioneel depot (`airfield.tl:49`, `airfield.tl:76`, `airfield_era_a.metacon.tl:3`).
- **Luchthaven**: "Geschikt voor kleine en grote vliegtuigen." Varianten vanaf 1950 en 1980; 2, 3 of 4 terminals en een landingsrichting (`airport.tl:24`, `airport.tl:80`, `airport1950.metacon.tl:3-4`).
- Terminals van een vliegveld nemen alleen kleine vliegtuigen aan; terminals van een luchthaven nemen beide groottes aan (`af_terminal.module.lua:715`, `ap_terminal.module.lua:897`).
- Het hoofdgebouw van de luchthaven heeft helikopterplatforms (`ap_main.module.lua:532`), en vanaf 1950 kan een luchthaven een helikopterterminal krijgen (`ap_terminal_heli.module.lua:897`, `ap_terminal_heli.module.lua:971`).
- **Tweede landingsbaan**: een luchthavenmodule vanaf 1980 (`airport_2nd_runway.module.lua:5`). Sommige luchthavenmodules hebben haar nodig en tonen zonder haar "Je hebt een 2e landingsbaan nodig" (`airport.script.lua:261`).
- Alle luchtvaartstations nemen passagiers en alle vracht aan (`airfield.tl:59`, `airport.tl:34`).

| Gebouw | Wachtende passagiers | Bron |
|---|---|---|
| Terminal van vliegveld | tot 250 | `af_terminal.module.lua:773` |
| Hoofdgebouw van luchthaven | tot 400 | `ap_main.module.lua:667` |
| Terminal van luchthaven | tot 850 | `ap_terminal.module.lua:951` |
| Helikopterterminal van luchthaven | tot 450 | `ap_terminal_heli.module.lua:990` |

## Hangars en helikopterstations

- Een **hangar** van een vliegveld of luchthaven biedt plaats aan 5 luchtvaartuigen en onderhoudt luchtvaartuigen in een straal van 550 m (`af_hangar.module.lua:273-278`, `ap_hangar.module.lua:456-461`).
- **Heliport** (vanaf 1950): koopt en onderhoudt helikopters, depot voor 5, onderhoudsstraal 800 m (`heliport.script.lua:301-306`).
- **Helipad** (vanaf 1950): een klein landingsplatform voor passagiers en vracht, zonder depot (`helipad.con.lua:29-33`).

## Kosten

Prijs en onderhoud van de eerste variant, tijdperkfactor inbegrepen. De factor is ×3 voor zowel het eerste vliegveld (1920, `airfield.tl:8`) als de eerste luchthaven (1950, `airport.tl:8`), daarna ×9 vanaf 1980; modules hebben er geen ([Kosten, onderhoud en leningen](costs.html)).

| Gebouw | Prijs | Onderhoud per jaar | Bron |
|---|---|---|---|
| Vliegveld | 3.600.000 - 9.000.000 | 150.000 - 600.000 | `airfield.tl:8`, `airfield.tl:55-56` |
| Luchthaven | 5.400.000 - 13.500.000 | 900.000 - 2.250.000 | `airport.tl:8`, `airport.tl:30-31` |
| Vliegveldmodule (hoofdgebouw, terminal, hangar) | 600.000 | 100.000 | `af_main.module.lua:316-317`, `af_hangar.module.lua:326-327` |
| Luchthavenmodule (hoofdgebouw, terminal, hangar, tweede landingsbaan) | 900.000 | 150.000 | `ap_main.module.lua:672-673`, `ap_terminal.module.lua:949-950`, `ap_hangar.module.lua:508-509`, `airport_2nd_runway.module.lua:27-28` |

- Het onderhoud van luchthavens en vliegvelden volgt ook het kalenderjaar, ×1 in 1900 tot ×6 in 2020 ([Kosten, onderhoud en leningen](costs.html)).
- De prijs en gebruikskosten van een luchtvaartuig worden berekend uit zijn snelheid en capaciteit, net als bij schepen en wegvoertuigen ([Kosten, onderhoud en leningen](costs.html)).

## Alle vliegtuigen

Snelheid in km/u, afgerond. "Alle vracht" betekent elk vrachttype. De capaciteit is het totaal dat de voertuigwinkel toont: de som van de compartimenten, elk met zijn grootste laadconfiguratie (`vehicle_store_util.tl:70-95`).

| Vliegtuig | Jaren | Grootte | Vracht | Capaciteit | Snelheid | Laadsnelheid |
|---|---|---|---|---|---|---|
| Junkers F 13 Herta | 1920-1950 | klein | passagiers | 16 | 135 | - |
| Vickers J6860 Victoria | 1922-1960 | klein | alle vracht | 32 | 150 | 2,5 |
| Fokker F VII A | 1925-1960 | klein | passagiers | 32 | 175 | 2 |
| Junkers JU-52 Iron Annie | 1933-1982 | klein | passagiers, alle vracht | **48** (2 × 24) | 200 | 3 |
| Douglas DC-3 | 1935-1995 | klein | passagiers | 56 | 300 | 2,5 |
| Curtiss C-46 Commando | 1942-1980 | klein | alle vracht | 80 | 280 | - |
| Douglas DC-4 | 1944-1998 | klein | passagiers | 100 | 365 | 3 |
| Bristol Type 170 (vracht) | 1949-2005 | klein | passagiers, alle vracht | **80** (2 × 40) | 350 | 1,5 |
| Lockheed L-1049 Super Connie | 1952-1986 | groot | passagiers | 120 | 486 | 3 |
| Lockheed L-1049D/H Super Connie | 1959-2000 | groot | alle vracht | **120** (2 × 60) | 486 | 2,5 |
| De Havilland DH.106 Comet | 1960-2000 | groot | passagiers | 160 | 724 | 3 |
| Canadair CL-44 (vracht) | 1962-2005 | groot | alle vracht | **144** (3 × 48) | 645 | 2 |
| Convair CV 990 Coronado | 1962-2020 | groot | passagiers | 200 | 917 | 2 |
| Lockheed L-100 Hercules | 1976-2000 | klein | alle vracht | **132** (3 × 44) | 400 | 3 |
| McDonnell Douglas DC-10-30 | 1978- | groot | passagiers | 400 | 960 | 2,5 |
| McDonnell Douglas DC-10-30CF | 1978- | groot | alle vracht | **396** (3 × 132) | 960 | 4 |
| Airbus A310 300F (vracht) | 1982- | groot | alle vracht | 160 | 850 | 3 |
| Short 330 Sherpa | 1984- | klein | passagiers, alle vracht | **80** (2 × 40) | 455 | 2,5 |
| Airbus A320 | 1985- | groot | passagiers | 180 | 753 | 3 |
| Br. Aerospace 146 | 1985- | klein | passagiers | 112 | 753 | 3 |
| Br. Aerospace 146 (vracht) | 1985- | klein | alle vracht | **96** (2 × 48) | 753 | 2 |
| Fokker 100 | 1988- | groot | passagiers | 160 | 845 | 3,5 |
| Toepolev Tu-204 | 1995- | groot | passagiers | 280 | 850 | 4 |
| Toepolev Tu-204C (vracht) | 1995- | groot | alle vracht | **204** (3 × 68) | 850 | 2 |
| Boeing 737-700 | 1998- | groot | passagiers | 200 | 974 | 2,5 |
| Boeing 737-700-C (vracht) | 1998- | groot | alle vracht | **160** (2 × 80) | 974 | 3 |
| Bombardier DHC-8 | 2000- | klein | passagiers | 120 | 648 | 3 |
| Bombardier DHC-8 (vracht) | 2008- | klein | alle vracht | 120 | 648 | 2 |
| Soechoj Superjet 100 | 2011- | klein | passagiers | 160 | 870 | 3 |
| Airbus Canada A220 | 2013- | groot | passagiers | 180 | 830 | 5 |

## Alle helikopters

| Helikopter | Jaren | Vracht | Capaciteit | Snelheid | Laadsnelheid |
|---|---|---|---|---|---|
| Bell 47 | 1950-1990 | passagiers, alle vracht | 8 | 150 | 2 |
| Piasecki H-21 Workhorse | 1952-1985 | passagiers, alle vracht | 80 (48 vracht) | 210 | 3 |
| Sikorsky S-64 Skycrane | 1962-2017 | alle vracht | 40 | 213 | 4 |
| Bell 206 Long Ranger | 1965-2025 | passagiers | 32 | 241 | 2,5 |
| Boeing Vertol 234 Chinook | 1980- | passagiers, alle vracht | 80 | 269 | 2 |
| AgustaWestland AW101 Merlin | 1990- | passagiers | 60 | 278 | 3 |
| Mil Mi-26TC | 1993- | alle vracht | 120 | 295 | 4 |
| Eurocopter 120B Colibri | 1998- | passagiers | 48 | 210 | 3 |
| Kaman K-MAX | 2005- | alle vracht | 60 | 190 | 3 |
| Airbus H225 Super Puma | 2013- | passagiers | 48 | 288 | 3 |
| NextGen VTOL | 2030- | passagiers | 56 | 610 | 4 |

## Goed om te weten

- **Kleine vliegtuigen blijven tot het einde nuttig.** De DHC-8, zijn vrachtversie en de Soechoj Superjet 100 zijn klein, dus een vliegveld volstaat voor hen.
- **Vóór 1952 is er geen groot vliegtuig**, dus een vroege luchthaven geeft nog geen toegang tot grotere toestellen.
- Vliegtuigen vliegen in een rechte lijn en de betaling telt alleen de afstand in rechte lijn, dus een omweg kost hen niets extra ([Vrachtinkomsten en bezorgtijd](income.html)).
- De minimale lengte van de landingsbaan, vliegroutes en het landen worden bepaald door de game-engine; de scripts tonen ze niet.

```check
official: "It can be used by small airplanes." (Airfield) "It can be used by small and large airplanes." (Airport), build menu descriptions.
scripts: Hetzelfde: terminals van vliegvelden nemen alleen SMALL_AIRCRAFT aan, terminals van luchthavens AIRCRAFT en SMALL_AIRCRAFT, helikopters bij het hoofdgebouw van de luchthaven, heliport en helipad vanaf 1950, tweede landingsbaan vanaf 1980, hangars voor 5; 15 kleine en 15 grote vliegtuigen en 11 helikopters in het basisspel.
result: agrees
```
