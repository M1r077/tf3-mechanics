---
title: Vervuiling en geluidsoverlast
summary: Wat geluid en vervuiling uitstoot, wanneer een gebouw meer uitstoot, hoe steden het beoordelen, en wat Vergroenen van de industrie en de Zuiveringsinstallatie echt doen.
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
fact: 65–80 dB | geluid in de stad: volle beoordeling bij 65, nul bij 80
fact: 60–74 | vervuiling in de stad, op de logaritmische schaal van de scripts (geen geluidsniveau): volle beoordeling bij 60, nul bij 74
fact: −80 % | geluid en vervuiling van een vergroend industriebedrijf
fact: 700 m | bereik van de Zuiveringsinstallatie
---

Voertuigen, sporen, straten, stations, depots, opslagplaatsen en industriebedrijven stoten allemaal **geluid** en **vervuiling** uit. Twee stadsbeoordelingen, **Geluidsoverlast** en **Vervuiling**, vergelijken wat de stad bereikt met vaste grenzen. Een slechte beoordeling verlaagt de beoordeling van de **Plaatselijke autoriteit** en dus de groei (zie [Steden](towns.html)).

## Wanneer een gebouw meer uitstoot

Een spelscript stelt om de paar updates de emissie van vier soorten gebouwen in, tussen een rustig en een druk niveau (`emissions.script.tl:12-18`):

| Gebouw | Stoot meer uit als | Bron |
|---|---|---|
| **Industriebedrijf** | het produceert, en opnieuw bij elke boost (vracht of arbeiders); minder, richting stilstandniveau, als zijn uitvoervoorraad vol is | `emissions.script.tl:152-194` |
| **Station** | het drukker is: wachtende mensen en vracht tegenover zijn capaciteit | `emissions.script.tl:211-222` |
| **Depot**, **onderhoudsstation** | meer voertuigen zijn onderhoud gebruiken | `emissions.script.tl:223-234` |
| **Opslagplaats** | haar voorraden voller zijn | `emissions.script.tl:237-250` |

- Elk industriebedrijf heeft zijn eigen vier niveaus: stilstaand, producerend, één keer geboost, twee keer geboost (`industryutil.lua:464-475`; de standaard 0 / 78 / 84 / 88 geldt alleen voor een industriebedrijf zonder eigen waarden). De meeste stoten ook stilstaand iets uit: een kolenmijn gaat van 2 → 10 → 20 → 30 vervuiling, zijn velden 2 → 30 → 60 → 90 (`coal_mine.con.lua:99-135`, zie [Industriebedrijven](industries.html)).
- Een industriebedrijf waarvan de uitvoer niet wordt opgehaald, zakt terug naar zijn stilstandniveau: het bedienen verhoogt zijn vervuiling.
- Voertuigen en sporen stoten ook uit; een voertuig in slechte staat stoot meer uit met de instelling **Effect voertuigonderhoud** (zie [Kosten, onderhoud en leningen](costs.html)).

## Wat het bouwmenu toont

| Gebouw | Geluid | Vervuiling | Bron |
|---|---|---|---|
| Haven | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| Luchthaven | 8–56 | 80–560 | `airport.tl:28-29` |
| Treinstation | 25 | 45–350 | `modular_station.con.lua:97-98` |
| Spoordepot | 50 | 100 | `rail_depot.con.lua:32-33` |
| Weg- en tramdepot | 40 | 80 | `road_depot.con.lua:30-31`, `tram_depot.con.lua:32-33` |
| Metrostation | 40 | 80 | `underground_station.con.lua:75-76` |
| Vrachtwagen- en busstation | 1–10 | 12–76 | `modular_terminal.con.lua:67-68` |
| Onderhoudsstations | 20 | 40–50 | `road_maint_station.con.lua:30-31`, `rail_maint_station.con.lua:30-31` |
| Opslagplaats | 20 | 50 (universeel) of 100 (gespecialiseerd) | `warehouses/warehouse.tl:51`, `warehouses/warehouse.tl:73-74` |

Twee waarden zijn de spreiding die het menu toont, van laagste naar hoogste, zoals de prijsspreiding ernaast (`construction_desc_react_util.tl:733-746`); één waarde is één getal. In bedrijf stoot elk gebouw meer uit naarmate het drukker is (tabel hierboven). Houd havens, luchthavens en grote vrachtstations weg van huizen.

## Hoe een stad het beoordeelt

| Beoordeling | Gemeten | Volle beoordeling | Nul | Bron |
|---|---|---|---|---|
| **Geluidsoverlast** | geluid bij de gebouwen van de stad | 65 dB of minder | 80 dB | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Vervuiling** | gemiddelde vervuiling per cel van 16 m van het stadsgebied (oppervlak geteld als minstens 5 en hoogstens 10 km²), omgerekend naar de logaritmische schaal van de scripts ("dB") | 60 of minder | 74 | `town_util.tl:413-431`, `emission_config.tl:23-30` |

- Alleen de **woonwijk** heeft last van geluid; commerciële en industriële gebouwen niet (officiële wiki). Het venster van een huis toont het geluid op zijn plek (`town_building.tl:165-183`).
- Vervuiling wordt over het hele gebied gemiddeld, dus één bron ver van het centrum weegt in een grote stad minder dan in een kleine.
- De instellingen **Gevoeligheid geluidsoverlast** en **Gevoeligheid vervuiling** verschuiven de grenzen: twee keer de gevoeligheid telt als +3 dB (`town_util.tl:426-428`, `town_util.tl:439-441`). Vervuiling gebruikt dezelfde logaritmische schaal als geluid (10·log10): +3 "dB" betekent twee keer zoveel vervuiling. Het is geen geluidsniveau.

| Stap | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Bron |
|---|---|---|---|---|---|---|---|---|
| Geluidsoverlast | Uit (altijd vol) | ×¼ | ×½ | ×1 | ×1,4 | ×1,8 | ×3,5 | `difficulty_util.tl:48` |
| Vervuiling | Uit (altijd vol) | ×¼ | ×½ | ×1 | ×1,7 | ×3 | ×5 | `difficulty_util.tl:49` |

De voorinstellingen Makkelijk, Gemiddeld, Moeilijk en Zeer moeilijk gebruiken stap 3, 4, 5 en 6 (`difficulty_util.tl:114-115`, `difficulty_util.tl:142-143`, `difficulty_util.tl:169-170`, `difficulty_util.tl:196-197`).

## Vergroenen van de industrie

| | | Bron |
|---|---|---|
| Effect | geluid en vervuiling van het industriebedrijf ×0,2 (−80 %), voorgoed | `emission_config.tl:32`, `emissions.script.tl:184-192` |
| Gebruik | één bij bedrijfsrang 3, 6, 9, 12 en 15 | `industry_greenify_tool.script.tl:99-104` |
| Grens | één keer per industriebedrijf; een tweede poging gebruikt geen vergunning | `company.script.tl:489-494` |

- Het effect hoort bij die versie van het industriebedrijf: als het opnieuw wordt gebouwd, gaat het verloren (`emissions.script.tl:187-190`).
- Beste gebruik: het drukste industriebedrijf vlak naast een stad, want een geboost industriebedrijf stoot het meest uit.

## De Zuiveringsinstallatie

Een bedrijfsvoordeel dat vervuiling in de omgeving verwijdert.

| | | Bron |
|---|---|---|
| Prijs | 100.000.000 | `pollution_cleanup_facility.script.lua:560` |
| Onderhoud per jaar | 10.000.000 | `pollution_cleanup_facility.script.lua:561` |
| Beschikbaar | 15 bij bedrijfsrang 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Nodig | **Machines**: 8 per cyclus, twee cycli per jaar; 20 arbeiders | `pollution_cleanup_facility.con.lua:43-60` |
| Bereik | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| Toestand | Vervuiling | Geluid | Bron |
|---|---|---|---|
| stil (geen machines) | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| werkend | −10.000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| één keer geboost | −20.000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| twee keer geboost | −40.000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

- Zonder machines doet ze bijna niets: ze moet bevoorraad worden als een industriebedrijf.
- Ze is luid: bouw haar buiten de woonwijk, binnen 700 m van het vervuilde gebied.
- Haar boostfactor voor arbeiders is ×2 (`pollution_cleanup_facility.script.lua:549`). Zie [Arbeiders](workers.html).

## Goed om te weten

- Open het stadsvenster of de lagen voor geluid en vervuiling om de beoordeling en de brandpunten te zien.
- Een volle uitvoervoorraad verlaagt de emissie van een industriebedrijf richting stilstandniveau, maar kost je zijn vracht: verplaats liever de stad dan het industriebedrijf uit te hongeren.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) en [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) helpen je de drukste stations te vinden.

```engine
De engine berekent de geluids- en vervuilingskaarten, hoe de waarden zich verspreiden, de emissies van voertuigen en sporen, en wanneer een industriebedrijf opnieuw wordt gebouwd. Het script stelt alleen het niveau van elk gebouw en de grenzen van de stad in.
```

```check
official: "Noise reflects noise levels in residential areas." "Pollution reflects pollution levels across the town area." De woonwijk "is sensitive to noise"; de commerciële wijk "is robust against the influence of noise". ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Geluidsbeoordeling 65 → 80 dB, vervuiling 60 → 74 dB, gemiddeld over 5–10 km²; gevoeligheid voegt 10·log10 dB toe; industriebedrijven, stations, depots en opslagplaatsen stoten meer uit als ze druk zijn; een volle uitvoervoorraad verlaagt de emissie van een industriebedrijf richting stilstandniveau; vergroenen −80 %, één keer per industriebedrijf; de Zuiveringsinstallatie verwijdert tot 40.000 vervuiling binnen 700 m en heeft machines nodig.
result: refines
```
