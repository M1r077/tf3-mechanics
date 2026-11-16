---
title: Laad- en lossnelheid
summary: Wat een voertuig snel of langzaam laat laden bij een halte: het voertuig, de perronsecties en de voorraad die de vracht afgeeft of ontvangt.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-15
game: 40425
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
| zonder sectie van hun klasse aan het perron | **×0,25** (constante van de laadtooltip; de factor zelf past de engine toe) | `cargo_react_util.tl:60` |
| voorbij de perronlengte (trein te lang) | **×0,25** (constante van de laadtooltip; de factor zelf past de engine toe) | `cargo_react_util.tl:61` |

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

## Waar de vracht gelost wordt

Elke halte van een lijn heeft een lijst **Lading**, in het venster "Vrachtfilter" van de halte. Bij de halte houdt het voertuig de vracht uit die lijst aan boord; de rest wordt gelost in elke voorraad in het verzorgingsgebied die hem aanneemt, ook in een opslagplaats (gemeten in het spel).

- Zo leegt een trein zich halverwege zijn lijn in een opslagplaats. In het spel: bij een halte naast een opslagplaats, met alleen plastic in de lijst, gingen de gereedschappen aan boord naar de opslagplaats, ook al was die bijna vol.
- Een passagiersperron heeft geen vrachtoverslag: daar blijft de vracht aan boord (gemeten in het spel).
- Wil je de vracht aan boord houden, voeg hem dan toe aan de lijst Lading van die halte.

```tip
**Verdwijnt vracht bij een halte naast een opslag? Zet die in de lijst Lading van die halte.** Alles wat niet in de lijst staat, wordt gelost in een voorraad binnen bereik, en de opslag betaalt er niets voor.
```

| Optie in "Vrachtfilter" | Wat het doet | Bron |
|---|---|---|
| "Alle vracht bij aankomst verplicht lossen" | tooltip: "Vracht lossen, ook als de voorraden vol zijn"; wat er gebeurt met de vracht die niet past, bepaalt de engine. Uit bij een nieuwe halte. | `cargofilter_window.tl:757`, `line_util.tl:476` |
| "Vracht bij aankomst vernietigen na wijziging configuratie" | lost of vernietigt de vracht aan boord als er bij deze halte vracht wacht voor een andere laadconfiguratie van het voertuig; welke van de twee bepaalt de engine | `cargofilter_window.tl:767` |
| "Vervangen door nieuwere vracht indien beschikbaar" | vernietigt vracht die terug is bij de halte waar hij geladen werd, als er nieuwere vracht van hetzelfde type wacht | `cargofilter_window.tl:778` |

- Staat de eerste optie uit, dan toont het vrachtpictogram "≤" en de tooltip "Alleen lossen als er ruimte is" (`cargofilter_window.tl:124`, `cargofilter_window.tl:158`).

## Meerdere soorten vracht op één lijn

- De lijst **Lading** van een halte is een ja/nee per vrachttype, **zonder volgorde**: de speler kan niet instellen welke vracht als eerste geladen wordt. De pictogrammen worden gewoon in de vrachtvolgorde van het spel getekend (`line_util.tl:471-475`, `line_util.tl:510`, `cargofilter_window.tl:533-535`).
- Een wagon of vrachtwagen die meerdere soorten vracht aanneemt, heeft per compartiment meerdere **laadconfiguraties**; de capaciteit van het compartiment is de grootste daarvan, niet hun som (`model_metadata_util.lua:682-733`, `vehicle_metadata_util.lua:27-37`). Hij vervoert er dus één tegelijk.
- Bij nieuwe voertuigen staat de automatische keuze van de configuratie aan voor elk compartiment (`vehicle_react_util.tl:339`), en het spel heeft geen venster om de vracht van een voertuig met de hand te kiezen.
- Passagiers en vracht kunnen een lijn delen: de scripts weigeren nooit vracht bij een halte omdat die ook passagiers aanneemt (`line_util.tl:1381-1386`). Vracht wordt alleen geschrapt bij een halte waarvan de terminal geen vracht kan laden of lossen (`line_util.tl:554-559`).
- Met meerdere soorten vracht gedragen **Volledige belading (willekeurig)** en **Volledige belading (alle)** zich verschillend: zie [Vertrekinstellingen: volledige belading, Vulniveau en stoptijden](departure.html).
- Als de configuratie niet past, toont de lijn **Sommige ladingstypeconfiguraties van deze lijn conflicteren**, bijvoorbeeld "Een deel van de vracht die zal worden geladen, is niet geschikt voor de voertuigen op de lijn." (`line_warning.script.tl:10-36`).

```engine
In welke volgorde meerdere soorten vracht geladen worden, hoe een gedeelde voorraad over wachtende voertuigen verdeeld wordt en hoe een voertuig zijn laadconfiguratie kiest, wordt door de engine bepaald.
```

## De automatische configuratie

Zolang niemand een wijziging heeft opgeslagen in het venster "Vrachtfilter" van een halte, wat haar op die lijn voorgoed uitschakelt (`line_util.tl:495-498`, `cargofilter_window.tl:438`), vult het spel de lijsten Lading zelf telkens als de lijn wordt aangemaakt, een halte wordt toegevoegd of verwijderd, de haltes worden herschikt of een waypoint wordt toegevoegd (`manager_window.tl:6712`, `:6786`, `:6845`, `:6879`, `:6963`). Een halte naar een ander station of perron verplaatsen, en een waypoint verwijderen of verplaatsen, start haar niet (`manager_window.tl:6851-6868`, `manager_window.tl:6968-6992`).

- Ze begint opnieuw met lege lijsten, met passagiers bij passagiersstations (`line_util.tl:542-588`).
- Ze zoekt producenten en afnemers alleen onder industriebedrijven en stadsgebouwen: opslagplaatsen tellen niet mee (`cargo_util.tl:518-526`).
- Ze zet een vracht op de lijst Lading van een halte als die verderop nodig is en niets bij de halte hem aanneemt. Een opslagplaats telt alsof hij alles aanneemt wat hij opslaat (`line_util.tl:676-693`): bij een halte naast een opslagplaats die die vracht opslaat, blijft de vracht van de lijst en lost de trein hem daar.
- Zodra een filter met de hand is gewijzigd, is de lijn gemarkeerd als aangepast (`cargofilter_window.tl:438`) en raakt de automatische configuratie haar nooit meer aan, ook niet als er later haltes bijkomen (`line_util.tl:496`).

```engine
De scripts schrijven alleen de lijsten Lading; het lossen zelf doet de engine. De regel hierboven (wat niet op de lijst staat, wordt gelost in elke voorraad die het aanneemt) is in het spel waargenomen met [Platform Details](https://mod.io/g/transportfever3/m/platform-details), november 2026.
```

## Goed om te weten

- Stations binnen een industriebedrijf zijn altijd gespecialiseerd in de vracht die dat bedrijf nodig heeft (officiële wiki).
- Gespecialiseerde opslagmodules bevriezen ook de bezorgtimer van de vracht die ze opslaan (officiële wiki); een universele opslagplaats doet dat niet.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) toont beide factoren voor elk voertuig aan een perron, en waar de geloste vracht naartoe ging.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Gespecialiseerde opslagplaatsen "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Gespecialiseerde sectie ×2, universeel ×1, geen passende sectie ×0,25, voorbij het perron ×0,25, gemengd naar aandeel van de trein; gespecialiseerde opslagmodule ×2, universele opslagplaats ×1.
result: refines
```
