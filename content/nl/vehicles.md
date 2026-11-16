---
title: Voertuigen: staat, leeftijd en laadsnelheid
summary: Wat de voertuigstatistieken betekenen, hoe staat en leeftijd werken, wat depots en onderhoudsstations doen, waar prijs en bedrijfskosten vandaan komen, en wanneer je een voertuig vervangt.
domain: vehicles
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-16
game: 40425
fact: 5 | staatniveaus, van Zeer slecht tot Zeer goed, elk 20 %
fact: 20 % | staat die de waarschuwing Voertuigstaat activeert
fact: 6 jaar | bedrijfskosten: de prijs van een voertuig
fact: 4 tot 16 | voertuigen in de onderhoudsgroep van één depot of onderhoudsstation
---

Elk voertuig heeft vaste statistieken (snelheid, capaciteit, laadsnelheid, prijs, bedrijfskosten, levensduur) en twee waarden die veranderen: zijn **staat** en zijn **leeftijd**. De staat daalt terwijl het rijdt en wordt door onderhoud hersteld. De leeftijd groeit alleen.

## De statistieken in de voertuigwinkel

- De winkel toont elke statistiek als een balk. De balk vergelijkt het voertuig met de andere van hetzelfde vervoermiddel en tijdperk, niet met een vaste schaal (`vehicle_util.tl:210-245`, `vehicle_util.tl:248-270`).
- Voor een trein toont de winkel de **hoogste** laadsnelheid van al zijn onderdelen (`vehicle_store_util.tl:333`).
- Een voertuig waarvan het bestand geen laadsnelheid, geluid, vervuiling of comfort instelt, krijgt een waarde berekend uit zijn andere statistieken (jaar, snelheid, vermogen, gewicht, grootte) (`model_metadata_util.lua:395-417`, `vehicle_metadata_util.lua:233-256`). De berekende laadsnelheid wordt afgerond op 0,5 en is nooit lager dan 1 (`vehicle_metadata_util.lua:267-269`).

## Welk voertuig laadt het snelst?

De laadsnelheid van het voertuig is alleen de eerste factor; perron en voorraad vermenigvuldigen haar (zie [Laad- en lossnelheid](loading.html)).

| Vervoermiddel | Laadsnelheid getoond als volle balk (laatste tijdperk) | Bron |
|---|---|---|
| Schepen | 10 tot 45 (vanaf 2003) | `vehicle_util.tl:219-223` |
| Wegvoertuigen, trams | 0,5 tot 10 (vanaf 1995) | `vehicle_util.tl:232-243` |
| Treinen | 0,1 tot 10 (vanaf 1981) | `vehicle_util.tl:226-229` |
| Vliegtuigen | 1 tot 4 (vanaf 1978) | `vehicle_util.tl:212-216` |

- Schepen hebben verreweg de hoogste laadsnelheden, vliegtuigen de laagste schaal.
- Vergelijk voertuigen van één vervoermiddel in de winkel met de kolom laadsnelheid; nieuwere modellen staan meestal hoger op de balk.
- Elke vracht heeft een laadfactor van 0,0625, passagiers 1 (`coal.cargo.lua:29`, `passengers.cargo.lua:23`).

```engine
Hoe de laadsnelheid van het voertuig, de laadfactor van de vracht en de perron- en voorraadfactoren tot de echte laadtijd worden gecombineerd, berekent de engine. De scripts geven alleen de invoer.
```

## Staat

| Staat | Niveau | Bron |
|---|---|---|
| boven 80 % | **Zeer goed** | `vehicle_util.tl:159-172` |
| 60–80 % | **Goed** | `vehicle_util.tl:159-172` |
| 40–60 % | **Middelmatig** | `vehicle_util.tl:159-172` |
| 20–40 % | **Slecht** | `vehicle_util.tl:159-172` |
| tot 20 % | **Zeer slecht** | `vehicle_util.tl:159-172` |

- De staat van een trein is het **gemiddelde** van al zijn wagons en locomotieven (`vehicle_util.tl:285-295`).
- Onder 80 % begint een voertuig topsnelheid, vermogen en comfort te verliezen, en geluid, vervuiling en bedrijfskosten te winnen (`vehicle_store_util.tl:230-259`). Het voertuigvenster toont deze straffen onder **Staat**.
- Hoe sterk deze straffen zijn, stelt **Effect voertuigonderhoud** in (Geen, Laag, Gemiddeld, Hoog, Zeer hoog); met Geen heeft de staat geen effect (`mod.script.tl:241-245`, `vehicle_store_util.tl:211-228`). Details: [Kosten, onderhoud en leningen](costs.html).
- Bij **20 %** of minder krijg je de waarschuwing **Voertuigstaat**. Ze blijft tot het voertuig weer boven **30 %** is (`notifications.script.tl:310-318`).
- Een gekloond voertuig is een nieuwe aankoop: staat 100 %, nieuwe aankoopdatum (`manager_window.tl:8502-8506`).

```engine
Hoe snel de staat daalt, hoeveel een bezoek aan een onderhoudsstation herstelt, en de grootte van elke straf (getMaintenanceTopSpeedPenalty en de andere) zijn waarden van de engine. Elk voertuigmodel kan ook zijn eigen topsnelheidsstraf per niveau instellen (`vehicle_store_util.tl:250-253`).
```

## Depots en onderhoudsstations

Voertuigen worden onderhouden door een depot of onderhoudsstation in de buurt. Elk bedient een beperkt aantal voertuigen: zijn **Onderhoudsgroep**.

| Gebouw | Onderhoudsgroep | Straal | Gestalde voertuigen | Bron |
|---|---|---|---|---|
| Treindepot | 6 | 800 m | 5 | `rail_depot.script.lua:341-349` |
| Treinonderhoudsstation | 12 | 800 m | – | `rail_maint_station.script.lua:151-157` |
| Wegdepot, tramdepot | 12 | 400 m | 10 / 8 | `road_depot.script.lua:189-198`, `tram_depot.script.lua:217-226` |
| Wegonderhoudsstation | 16 | 600 m | – | `road_maint_station.script.lua:234-240` |
| Scheepsdepot | 8 | 1000 m | 5 | `water_depot.script.lua:370-379` |
| Scheepsonderhoudsstation | 12 | 1400 m | – | `water_maint_station.script.lua:256-262` |
| Hangar van vliegveld of luchthaven | 16 | 550 m | 5 | `af_hangar.module.lua:272-280`, `ap_hangar.module.lua:455-463` |
| Helihaven | 4 | 800 m | 5 | `heliport.script.lua:300-309` |

- Het gebouwvenster toont "gebruikt / groep" (bijvoorbeeld 14 / 12) en de lijst van voertuigen die het bedient, met hun staat (`entity_window_util.tl:2010-2039`, `maintenance_station_eow.script.tl:188-215`).
- Een vollere groep maakt het gebouw luidruchtiger en vuiler: de emissies stijgen met het gebruikte deel van de groep (`emissions.script.tl:223-234`).
- Een treinonderhoudsstation bedient twee keer zoveel treinen als een treindepot: 12 tegen 6.
- Onderhoudsstations kunnen geen voertuigen kopen of stallen, maar hun straal is vaak groter dan die van het depot: 600 m tegen 400 m op de weg, 1400 m tegen 1000 m voor schepen. Alleen het wegonderhoudsstation onderhoudt ook trams.
- De officiële wiki raadt waypoints aan om voertuigen langs een onderhoudsgebouw te sturen.

```engine
Aan welk station een voertuig wordt toegewezen, wat er gebeurt als meer voertuigen een station gebruiken dan zijn groep, en de gebruikte straal van het verzorgingsgebied, beslist de engine.
```

## Prijs en bedrijfskosten

- Voertuigen uit het basisspel hebben geen vaste prijs: de bedrijfskosten komen uit snelheid en capaciteit, en de prijs is **6 jaar** bedrijfskosten (`model_metadata_util.lua:548-549`). Volledige formule: [Kosten, onderhoud en leningen](costs.html).
- **Kosten voertuigen** en **Voertuigonderhoud** schalen beide van 50 % tot 150 % (`post_run_util.tl:54-81`).
- Een voertuig in slechte staat betaalt meer bedrijfskosten, bovenop de basiswaarde (`vehicle_store_util.tl:256-259`).

## Leeftijd en levensduur

- Elk model heeft een **levensduur** in jaren (`vehicle_metadata_util.lua:79-83`). De kolom **Leeftijd** van het lijnvenster toont de leeftijd; de tooltip toont de resterende tijd, of **Max. levensduur bereikt** (`line_eow.script.tl:133-147`). Het deel van de levensduur in die tooltip staat op **0 %** tot de levensduur bereikt is: het script rondt de breuk naar beneden af voordat die getoond wordt (`line_eow.script.tl:139`), terwijl hetzelfde deel elders volledig berekend wordt (`vehicle_util.tl:311`). Kijk in plaats daarvan naar de resterende tijd.
- Voor een trein telt het **oudste** onderdeel (`vehicle_util.tl:36-52`). Eén oude wagon laat de hele trein als oud verschijnen.

```engine
Wat het bereiken van de levensduur verandert (bijvoorbeeld sneller verlies van staat of een lagere verkoopwaarde), staat niet in de scripts. De scripts tonen alleen leeftijd en levensduur.
```

## Wanneer moet ik oude voertuigen vervangen?

1. **De staat blijft laag**, zelfs met een onderhoudsstation in de buurt: het voertuig verliest snelheid en betaalt meer bedrijfskosten. Controleer eerst de groep van het station: die kan vol zijn.
2. **Max. levensduur bereikt** in de tooltip van Leeftijd: het model is voorbij zijn geplande levensduur.
3. **Er bestaat een beter model**: snellere of grotere voertuigen kosten meer in bedrijf, maar ze vervoeren meer (de prijs volgt snelheid × capaciteit).
4. Gebruik **Voertuigen vervangen** in de lijnbeheerder. Het opent de winkel met een vergelijking met het huidige voertuig (`vehicle_store_window.tl:4893-4928`, `vehicle_store_window.tl:2611`).

```tip scripts
**Blijven voertuigen in slechte staat naast een depot? Open het venster en kijk naar "gebruikt / pool".** Een treindepot bedient 6 treinen, een treinonderhoudsstation 12. Wat de engine doet met voertuigen boven de pool staat niet in de scripts; een tweede gebouw is het veilige antwoord.
```

## Goed om te weten

- Bouw genoeg onderhoudscapaciteit: één treindepot bedient maar 6 treinen.
- Met **Effect voertuigonderhoud** op Geen doet de staat er niet toe.
- **Naar depot sturen** stuurt een voertuig naar het dichtstbijzijnde bereikbare depot, niet naar het depot waar het gekocht is (officiële wiki).
- [Vehicle Comparison](https://mod.io/g/transportfever3/m/vehicle-comparison) helpt modellen te vergelijken voordat je ze vervangt.

```check
official: "This section shows how well the vehicle is maintained and how the maintenance state affects the vehicle properties." "Loading speed modifies a vehicle's base loading speed which can be seen in the vehicle window or in the vehicle store." ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles))
scripts: Vijf staatniveaus van 20 %; straffen op snelheid, vermogen, comfort, emissies en bedrijfskosten onder 80 %, geschaald door Effect voertuigonderhoud; waarschuwing bij 20 %, gewist boven 30 %. Onderhoudsgroep van 4 tot 16 voertuigen per gebouw. Prijs = 6 jaar bedrijfskosten. Leeftijd van een trein = zijn oudste onderdeel. Ontbrekende laadsnelheden worden berekend uit de andere statistieken, afgerond op 0,5, minstens 1.
result: refines
```
