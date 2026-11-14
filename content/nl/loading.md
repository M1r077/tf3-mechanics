---
title: Laad- en lossnelheid
summary: Wat een voertuig snel of langzaam laat laden bij een halte: het voertuig, de perronsecties en de voorraad die de vracht afgeeft of ontvangt.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-14
fact: ×2 | gespecialiseerde perronsectie
fact: ×0,25 | verkeerde sectie of trein te lang
fact: ×4 | in het beste geval: gespecialiseerd perron en opslagplaats
---

De tijd die een voertuig bezig is met laden of lossen, is zijn eigen laadsnelheid vermenigvuldigd met twee factoren: een voor het **perron** en een voor de **voorraad** aan de andere kant (opslagplaats, industriebedrijf, stad).

```diagram loading_factors
```

## 1. Het voertuig

Elk voertuig heeft een basislaadsnelheid, te zien in de showroom en in het voertuigvenster ("2.0x"). Alles hieronder vermenigvuldigt die.

## 2. De perronfactor

Voor het spel is een perron geen rij modules, maar een **lijst van secties, één per vrachtklasse**, waarbij de lengtes van alle modules van die klasse worden opgeteld.

```diagram loading_sections
```

| Wagons… | Factor | Bron |
|---|---|---|
| op een sectie van hun klasse (bulkwagons, bulksectie) | **×2** | `modular_station.script.lua:1042` |
| op een universele sectie | ×1 | `modular_station.script.lua:1042` |
| zonder sectie van hun klasse aan het perron | **×0,25** | `cargo_react_util.tl:60` |
| voorbij de perronlengte (trein te lang) | **×0,25** | `cargo_react_util.tl:61` |

- De factor is een **mix naar aandeel van de trein**: als 3/4 van de wagons past en 1/4 niet, is de factor ¾ × 2 + ¼ × 0,25 ≈ ×1,56 (`cargo_react_util.tl:63-70`, dezelfde verdeling die het spel toont als "Gedeeltelijk gespecialiseerde terminal").
- **Waar** de wagons aan het perron staan, maakt niet uit, alleen de opgetelde lengtes tellen (gemeten in het spel).
- Weg: gespecialiseerde vrachtwagenterminals geven ×2 (`modular_terminal.script.lua:2956`); de kleine haltes langs de straat zijn altijd ×1 (`small_stops.script.lua:19`).
- Reizigersperrons zijn ×1.

## 3. De voorraadfactor

Bij het lossen gaat elke eenheid naar een ontvanger: een opslagmodule, een industriebedrijf of een stadsgebouw. De voorraad van de ontvanger heeft zijn eigen factor.

| Ontvanger | Factor | Bron |
|---|---|---|
| **gespecialiseerde** opslagmodule (vloeistof, bulk, dieplader, goederen) | **×2** | `modules.script.lua:120`, `warehouse.script.lua:297-314` |
| **universele** opslagplaats | ×1 | `warehouse.script.lua:272-285` |
| industriebedrijf | ×1 | gemeten in het spel |

- Elke opslagmodule vraagt om ×2, maar universele modules voegen alleen capaciteit toe aan **één gedeelde universele voorraad**, die met ×1 wordt aangemaakt. Alleen gespecialiseerde modules krijgen een eigen voorraad met ×2.
- De tooltip van het spel noemt deze factor "Gespecialiseerde opslagplaats: +100 %" (`cargo_react_util.tl:51-54`).
- Tijdens één losbeurt bedient het spel de ontvangers **om de beurt**, dus de snelheid verandert tijdens het lossen als een deel van de vracht naar een opslagplaats gaat en een deel naar een industriebedrijf (gemeten in het spel).

```engine
Welke ontvanger elke eenheid krijgt, en de uiteindelijke vermenigvuldiging, gebeuren in de engine. De factoren hierboven zijn de invoer die de scripts eraan geven; het resultaat is gecontroleerd met de waarden die de engine beschikbaar stelt (meting met [Platform Details](https://mod.io/g/transportfever3/m/platform-details), oktober 2026).
```

## Wat het spel toont

- De laadindicator wordt boven ×1,5 als **versneld** en onder ×0,75 als **vertraagd** weergegeven (`cargo_react_util.tl:119-122`).
- Beweeg de muis erover: de tooltip toont "Gespecialiseerde terminal", "Specialisaties komen niet overeen", "Terminal te kort" en "Gespecialiseerde opslagplaats", elk met een percentage (`cargo_react_util.tl:76-99`).

## Voorbeeld

Een trein van 8 bulkwagons, 160 m lang, lost steenkool.

| Station | Perron | Ontvanger | Factor |
|---|---|---|---|
| universeel perron 160 m | ×1 | staalbedrijf | **×1** |
| bulkperron 160 m | ×2 | staalbedrijf | **×2** |
| bulkperron 160 m | ×2 | gespecialiseerde bulkopslag | **×4** |
| bulkperron 160 m | ×2 | universele opslagplaats | **×2** |
| universeel perron 120 m (trein 40 m te lang) | ¾ × 1 + ¼ × 0,25 ≈ ×0,81 | staalbedrijf | **×0,81** |

## Goed om te weten

- Stations binnen een industriebedrijf zijn altijd gespecialiseerd in de vracht die dat bedrijf nodig heeft (officiële wiki).
- Gespecialiseerde opslagmodules bevriezen ook de bezorgtimer van de vracht die ze opslaan (officiële wiki); een universele opslagplaats doet dat niet.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) toont beide factoren voor elk voertuig aan een perron, en waar de geloste vracht naartoe ging.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Gespecialiseerde opslagplaatsen "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Gespecialiseerde sectie ×2, universeel ×1, geen passende sectie ×0,25, voorbij het perron ×0,25, gemengd naar aandeel van de trein; gespecialiseerde opslagmodule ×2, universele opslagplaats ×1.
result: refines
```
