---
title: Opslagplaatsen
summary: Universele of gespecialiseerde modules, wat elke voorraad bevat, een vrachttype vastzetten, laadsnelheid, kosten en vervuiling, en wat een opslagplaats niet doet.
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
game: 40425
fact: 500 | eenheden vracht per module, van elk type
fact: ×2 | laadsnelheid bij een gespecialiseerde module, ×1 bij een universele
fact: 150.000 / 300.000 | prijs van een universele / gespecialiseerde module
fact: 0 | inkomsten voor vracht die bij een opslagplaats wordt gelost
---

Een opslagplaats is een ingang met een aantal **modules**. Ze bewaart vracht tussen twee lijnen: de ene lijn lost hem, een andere laadt hem weer. Stations bereiken haar via hun verzorgingsgebied; steden en industriebedrijven nemen er nooit iets uit (officiële wiki).

## Universele of gespecialiseerde modules

| Module | Voorraad | Bevat | Laadfactor | Bron |
|---|---|---|---|---|
| **Universele opslag** | alle universele modules delen **één** voorraad | elke vracht, gemengd | ×1 | `warehouse.script.lua:272-295`, `modules.script.lua:49` |
| **Vloeistoffenopslag**, **Bulkopslag**, **Diepladeropslag**, **Goederenopslag** | **één voorraad per module** | één vrachttype tegelijk, van zijn klasse | ×2 | `warehouse.script.lua:296-314`, `modules.script.lua:120`, `modules.script.lua:165`, `modules.script.lua:247`, `modules.script.lua:296` |

- Elke module voegt **500** eenheden toe (`modules.script.lua:49`, `modules.script.lua:120`). Vijf universele modules vormen één voorraad van 2.500; vijf vloeistofmodules vormen vijf voorraden van 500.
- Passagiers worden nooit opgeslagen (`warehouse.script.lua:279`, `warehouse.script.lua:304`).
- Een gespecialiseerde module neemt één vrachttype tegelijk aan: om ruwe olie en brandstof op te slaan heb je twee vloeistofmodules nodig (officiële wiki).
- De ×2 van een gespecialiseerde module wordt vermenigvuldigd met de perronfactor: een bulkperron en een bulkmodule geven ×4. Details: [Laad- en lossnelheid](loading.html).

## Universeel of gespecialiseerd?

1. **Veel vrachttypen, kleine hoeveelheden**: universeel. Eén gedeelde voorraad, de helft van de prijs en de helft van de vervuiling.
2. **Eén vracht in grote hoeveelheden** (steenkool, ruwe olie, boomstammen): gespecialiseerd. Voertuigen lossen en laden daar twee keer zo snel, maar je hebt één module per vrachttype nodig.
3. **Voedsel en andere vracht met een korte bezorgtijd**: gespecialiseerd; volgens de officiële wiki bevriezen deze modules de bezorgtimer (zie hieronder).
4. Beide soorten kunnen in één opslagplaats gemengd worden: de universele modules vormen nog steeds één voorraad, elke gespecialiseerde module haar eigen.

## Versnelt een opslagplaats het lossen?

- **Gespecialiseerde module**: ja, ×2 voor de vracht die ze aanneemt. De laadtooltip van het voertuig toont "Gespecialiseerde opslagplaats: +100 %" (`cargo_react_util.tl:51-54`).
- **Universele module**: nee. Haar voorraad wordt met ×1 aangemaakt; de ×2 die de module vraagt, wordt genegeerd (`warehouse.script.lua:284`, `warehouse.script.lua:288-289`).
- Gaat een deel van de vracht naar een opslagplaats en een deel naar een industriebedrijf, dan bedient het voertuig ze om de beurt, dus de snelheid verandert tijdens één stop (gemeten in het spel, zie [Laad- en lossnelheid](loading.html)).

## De sectie Voorraad

- Eén rij per voorraad: de vracht die ze aanneemt, de hoeveelheid, en bij aanwijzen de **Gemiddelde resterende bezorgtijd** (`entity_window_util.tl:408-410`).
- **Een vrachttype vastzetten**: klik bij een gespecialiseerde module op een vrachtpictogram. Het spel bouwt de opslagplaats opnieuw, met die module gereserveerd voor deze vracht (`entity_window_util.tl:339-367`, `warehouse.script.lua:308`). De module verwijderen of vervangen wist de vastzetting (`warehouse.script.lua:403-405`).
- **Alle vracht annuleren**: leegt die rij in één keer (`entity_window_util.tl:423-434`). De vracht gaat verloren.
- Beide knoppen ontbreken alleen bij een opslagplaats van een andere speler; die van jou en opslagplaatsen zonder eigenaar hebben ze (`warehouse_eow.script.tl:127-137`, `gui/entity_window/warehouse/warehouse.tl:38`, `entity_util.tl:83-86`).
- De grafiek **Statistieken** toont **Inkomend** (gelost) en **Uitgaand** (geladen) per jaar (`warehouse_eow.script.tl:159-160`).

## Kosten en vervuiling

| | Universele module | Gespecialiseerde module | Bron |
|---|---|---|---|
| Prijs | 150.000 | 300.000 | `wh_universal.module.lua:18`, `wh_liquid.module.lua:22` |
| Onderhoud per jaar | 25.000 | 50.000 | `wh_universal.module.lua:19`, `wh_liquid.module.lua:23` |
| Geluid | 20 | 20 | `wh_universal.module.lua:33`, `wh_liquid.module.lua:37` |
| Vervuiling | 25 | 50 | `wh_universal.module.lua:34`, `wh_liquid.module.lua:38` |

- De opslagplaats voegt haar eigen vervuiling toe: **25**, of **50** zodra er één gespecialiseerde module is gebouwd (`warehouse.script.lua:327`, `warehouse.script.lua:338-345`).
- Het bouwmenu heeft één item per klasse en tijdperk (vanaf 1900, 1940 en 1980) (`warehouses/warehouse.tl:3-5`); latere tijdperken tonen ×3 en ×9 (`warehouses/warehouse.tl:48`, `warehouses/warehouse.tl:75-76`), en het onderhoud van opslagplaatsen stijgt ook met het jaar. Details: [Kosten, onderhoud en leningen](costs.html).
- Bulk-, dieplader- en goederenmodules kosten hetzelfde als vloeistofmodules (`wh_bulk.module.lua:22-23`, `wh_flatbed.module.lua:22-23`, `wh_goods.module.lua:18-19`).

```engine
De scripts geven twee emissieniveaus, het tweede twee keer het eerste (`warehouse.script.lua:342-343`); de opslagplaats gaat van het eerste naar het tweede naarmate de voorraden vollopen, volle voorraden = twee keer (`emissions.script.tl:237-249`). De prijs die echt voor modules wordt afgeschreven, berekent de engine.
```

## Wat een opslagplaats niet doet

- **Ze betaalt niets.** Lossen bij een opslagplaats levert geen inkomsten op; de vracht wordt één keer betaald, als hij zijn afnemer bereikt, voor de rechte afstand vanaf zijn bron (gemeten in het spel, zie [Vrachtinkomsten en bezorgtijd](income.html)).
- **Ze bevoorraadt geen steden of industriebedrijven** in de buurt: die nemen alleen vracht van voertuigen aan (officiële wiki).
- **Ze is geen bestemming voor de automatische lijnconfiguratie**, die alleen producenten en afnemers zoekt; maar een halte naast een opslagplaats die een vracht opslaat, laat die vracht uit de lijst Lading, zodat treinen hem daar lossen (zie [Laad- en lossnelheid](loading.html)).
- **Ze heeft geen weg nodig.** De ingang klikt vast aan een straat, maar vracht beweegt alleen via verzorgingsgebieden van stations (`warehouse.script.lua:386-389`, officiële wiki). Het venster van de opslagplaats toont haar verzorgingsgebied (`gui/entity_window/warehouse/warehouse.tl:88-96`).

```engine
Waar geloste vracht naartoe gaat, en of de bezorgtimer van opgeslagen vracht stopt, beslist de engine. Geen enkel script bevriest de timer: de officiële wiki zegt dat gespecialiseerde modules dat doen en een universele niet.
```

## Goed om te weten

- Controleer de lijst Lading van elke halte bij een opslagplaats: wat er niet in staat, wordt in de opslagplaats gelost, ook halverwege de lijn.
- Een volle voorraad weigert meer vracht, tenzij de halte "Alle vracht bij aankomst verplicht lossen" ("Vracht lossen, ook als de voorraden vol zijn") gebruikt; wat er gebeurt met de vracht die niet past, bepaalt de engine (zie [Laad- en lossnelheid](loading.html)).
- Wil je een gespecialiseerde module voor één vracht houden, zet dan haar vrachttype vast in de sectie Voorraad.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) toont per station de opslagplaatsen binnen bereik met hun voorraden; [Platform Details](https://mod.io/g/transportfever3/m/platform-details) toont waar de geloste vracht naartoe ging.

```check
official: "Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types." Gespecialiseerde opslagplaatsen "freeze the cargo item's delivery timer" en "enable faster loading / unloading speeds". "In specialized warehouses, only one cargo type can be stored at a time for a given module." ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Universele modules vormen één gedeelde voorraad met laadfactor ×1, elke gespecialiseerde module een eigen voorraad van 500 met ×2 en één vrachttype. Een gespecialiseerde module kost twee keer zoveel (300.000, onderhoud 50.000) en vervuilt twee keer zoveel (50). Het bevriezen van de timer staat niet in de scripts.
result: refines
```
