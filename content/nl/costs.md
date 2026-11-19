---
title: Kosten, onderhoud en leningen
summary: Wat de kosteninstellingen veranderen, welke kosten met het kalenderjaar stijgen, hoe voertuigprijzen worden berekend en wat een lening echt kost.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
game: 40444
fact: ×6 | jaarfactor op het onderhoud van opslagplaatsen, havens en luchthavens tot 2020
fact: 6 jaar | gebruikskosten: de prijs van een voertuig
fact: één keer | wordt de rente van een lening over het bedrag berekend, niet elk jaar
fact: 4 | leningen tegelijk
---

De instelling **Inflatie** verhoogt geen enkele kost: ze verlaagt alleen je inkomsten als de bedrijfsrang stijgt (zie [Vrachtinkomsten](income.html)). De kosten stijgen in plaats daarvan met het **kalenderjaar**, en vier schuifregelaars schalen ze vanaf de start.

```diagram cost_years
```

## De kosteninstellingen

| Instelling | Waarden | Presets Makkelijk · Gemiddeld · Moeilijk · Heel moeilijk | Bron |
|---|---|---|---|
| **Kosten voertuigen**, **Voertuigonderhoud** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:39`, `difficulty_util.tl:98-101`, `difficulty_util.tl:125-128`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Kosten infrastructuur**, **Onderhoud infrastructuur** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:98-101`, `difficulty_util.tl:125-128`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Effect voertuigonderhoud** | Geen ×0 · Laag ×0,5 · Gemiddeld ×1 · Hoog ×1,5 · Zeer hoog ×2 | Laag · Gemiddeld · Hoog · Zeer hoog | `difficulty_util.tl:42`, `difficulty_util.tl:103`, `difficulty_util.tl:185` |
| **Inflatie** | alleen inkomsten, zie [Vrachtinkomsten](income.html) | Laag · Gemiddeld · Hoog · Zeer hoog | `difficulty_util.tl:50`, `mod.script.tl:695-698` |

- **Kosten infrastructuur** schaalt de prijs van straten, sporen, bruggen, tunnels, overwegen, gebouwen en modules, en ook terreinwerk (`post_run_util.tl:23-52`, `post_run_util.tl:83-120`, `construction.script.tl:31-35`, `mod.script.tl:224-227`). Het schaalt ook de sloopkosten van gebouwen (`construction.script.tl:39-44`). **Onderhoud infrastructuur** schaalt bij het laden het onderhoud van straten, sporen, bruggen, tunnels, overwegen en modules (`post_run_util.tl:43-45`, `post_run_util.tl:105-112`). Bij gebouwen passen de scripts het alleen toe in het gebouwvenster (`entity_window_util.tl:186`); wat wordt afgeschreven, beslist de engine.
- **Kosten voertuigen** en **Voertuigonderhoud** schalen de aankoopprijs en de gebruikskosten van elk voertuig (`post_run_util.tl:54-81`).
- **Effect voertuigonderhoud** bepaalt hoe sterk een voertuig in slechte staat snelheid, vermogen en comfort verliest en meer geluid, vervuiling en gebruikskosten krijgt (`mod.script.tl:242-246`).

## Wat met het kalenderjaar stijgt

- **Onderhoud van gebouwen**: ×1 in 1900, ×1,5 in 1920, ×2,2 in 1940, ×3,2 in 1960, ×4 in 1980, ×5 in 2000, ×6 in 2020 (`mod.script.tl:92-100`). Het gebouwvenster en het bouwmenu passen dit toe op elk gebouw dat het jaar moet volgen, en het bouwmenu markeert elke meta-constructie (in het basisspel: opslagplaatsen, vliegvelden, luchthavens en havens) (`entity_window_util.tl:186-193`, `construction_react_util.tl:1152`, `warehouse.tl:7`, `harbor_modular.tl:24`).
- **Modules** van zo'n gebouw kosten de prijs van het bouwjaar van het gebouw, hun onderhoud dat van het huidige jaar (`construction.tl:3741-3748`, `construction.tl:4413-4416`).
- **Tijdperkvarianten**: depots, onderhoudsstations, opslagplaatsen, stations, havens en luchthavens hebben één variant per tijdperk, en elke latere variant kost **×3** (tijdperk B) of **×9** (tijdperk C) van de eerste (`rail_depot.con.lua:7`, `warehouse.tl:48`, `modular_station.con.lua:71`, `harbor_modular.tl:76`, `airport.tl:8`).
- **Geld van subsidies**: ×1 in 1900 tot ×4 vanaf 2000 (`finances_util.tl:87-90`). **Leningbedragen**: ×0,4 in 1900 tot ×2,4 in 2020 (`loan_util.tl:7-10`).
- **Inkomsten** hebben helemaal geen jaarfactor (`cargo_income.script.lua:10-13`).

```engine
Het onderhoud dat echt wordt afgeschreven, en of straten, sporen en voertuigen ook de jaartabel volgen, bepaalt de engine (getCostMultiplierForYear; de basisconfiguratie zet alleen chargeMaintenanceInterval = 60, `mod.script.tl:105`). De scripts berekenen alleen de waarden die in de vensters en het bouwmenu staan, met de tabel hierboven. Geen enkel script zet de vlag "het jaar volgen" van de andere gebouwen.
```

## Sporen, wegen en gebouwen

Straat- en spoorbestanden geven de prijs en het jaarlijkse onderhoud per meter; het bouwmenu toont ze per kilometer (`construction_react_util.tl:2466`, `construction_react_util.tl:2480-2488`). Bij de meeste typen is het onderhoud **een zesde** van de bouwprijs:

| Type | Beschikbaar vanaf | Bouw per km | Onderhoud per km en jaar | Bron |
|---|---|---|---|---|
| Eenvoudig spoor | start | 60.000 | 10.000 | `simple.street_template.lua:9`, `simple.street_template.lua:33` |
| Standaardspoor | 1930 | 180.000 | 30.000 | `standard.street_template.lua:11`, `standard.street_template.lua:35` |
| Hogesnelheidsspoor | 1980 | 540.000 | 90.000 | `high_speed.street_template.lua:11`, `high_speed.street_template.lua:35` |
| Kleine oude landweg | start – 1940 | 60.000 | 10.000 | `country_old_small.street_template.lua:4-5`, `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:58` |
| Grote nieuwe stadsstraat | 1940 | 540.000 | 90.000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:91` |

- Een bovenleiding kost **30 %** van de spoorprijs extra; een busbaan 10 %, een tramspoor 20 %, een elektrisch tramspoor 40 % van de straatprijs (`mod.script.tl:24-28`).
- Terrein ophogen kost 4,5 per m³, verlagen 5,25 per m³, beide × Kosten infrastructuur; een akker weghalen 200.000 (`mod.script.tl:20-22`, `mod.script.tl:33`, `mod.script.tl:226-227`).
- Een gebouw zonder eigen onderhoud betaalt **een zesde van zijn prijs** per jaar, berekend op de prijs vóór de instelling Kosten infrastructuur (`construction.script.tl:25-27`).
- De basisconfiguratie zet een sloopvergoeding van 0,75 en een termijn van 60 (`mod.script.tl:30-31`): wat je net hebt gebouwd, levert bij slopen het meeste geld terug. De engine past dit toe.

Jaarlijks onderhoud volgens de bestanden, voor de eerste variant (vóór 1940) en de latere; opslagplaatsen krijgen daar ook nog de jaarfactor hierboven bovenop:

| Gebouw | Eerste variant | ×3 (vanaf 1940) | ×9 (vanaf 1980) | Bron |
|---|---|---|---|---|
| Treindepot, scheepsdepot | 100.000 | 300.000 | 900.000 | `rail_depot.con.lua:34`, `water_depot.con.lua:32` |
| Wegdepot | 30.000 | 90.000 | 270.000 | `road_depot.con.lua:32` |
| Tramdepot | 20.000 | 60.000 | 180.000 | `tram_depot.con.lua:34` |
| Onderhoudsstation trein of schip | 40.000 | 120.000 | 360.000 | `rail_maint_station.con.lua:32`, `water_maint_station.con.lua:32` |
| Onderhoudsstation weg | 10.000 | 30.000 | 90.000 | `road_maint_station.con.lua:32` |
| Universele opslagplaats | 25.000 | 75.000 | 225.000 | `warehouse.tl:48-52`, `warehouse.tl:75` |
| Gespecialiseerde opslagplaats | 50.000 | 150.000 | 450.000 | `warehouse.tl:51`, `warehouse.tl:75` |

Elk van deze gebouwen kost **6 ×** zijn onderhoud om te bouwen (`rail_depot.con.lua:35`, `warehouse.tl:76`): 2,7 M voor een gespecialiseerde opslagplaats van het laatste tijdperk, vóór de jaarfactor.

- Het eerste **vliegveld** (tot 1950) gebruikt al de ×3 van het tweede tijdperk: de test leest het eindjaar van de variant in plaats van het beginjaar (`airfield.tl:8`, `airfield_era_a.metacon.tl:3`).

## Voertuigen

Geen voertuig uit het basisspel heeft een vaste prijs: het spel berekent die uit de snelheid en de capaciteit van het voertuig als het model wordt geladen (`model_metadata_util.lua:488-552`):

1. **Gebruikskosten per jaar** = ongeveer 675 × gemiddelde snelheid (m/s) × capaciteit / 4 (`model_metadata_util.lua:499-518`). De 675 komt van de gemiddelde inkomsten per km, verlaagd om ruimte te laten voor lege terugritten, de aankoop en de dalende ticketprijzen (`model_metadata_util.lua:500-508`).
2. De **gemiddelde snelheid** ligt onder de topsnelheid (v in km/h): wegvoertuigen en trams v^0,78 + 4, treinen v^0,86 + 10, vliegtuigen −0,0000203 × v² + 0,17 × v + 28,36 (v hoogstens 4.000), schepen 65 % van de topsnelheid (`model_metadata_util.lua:448-474`).
3. **Treinen**: een wagon telt de helft van zijn capaciteit; een locomotief telt ook vermogen ÷ topsnelheid (km/h) × 12,5 als capaciteit, ook gehalveerd (`model_metadata_util.lua:511-512`, `model_metadata_util.lua:526-540`). Een sterke, trage locomotief is duur.
4. **Prijs** = **6 ×** de jaarlijkse gebruikskosten (`model_metadata_util.lua:548-549`).

Voorbeeld bij 100 %: een bus van 35 km/h voor 48 reizigers kost ongeveer 45.000 per jaar aan gebruik en ongeveer 270.000 om te kopen.

- De staat van een voertuig heeft vijf niveaus (100–80 %, daarna elke 20 %) (`vehicle_store_util.tl:231-234`); bij **20 %** waarschuwt het spel, tot hij weer boven 30 % is (`notifications.script.tl:310-318`).

```engine
Hoe snel de staat van een voertuig daalt, hoeveel de gebruikskosten daardoor stijgen en of voertuigprijzen met het jaar veranderen, zijn enginewaarden (getMaintenanceRunningCostPenalty en de andere straffen); de scripts schalen ze alleen met Effect voertuigonderhoud.
```

## Leningen

```diagram loan_interest
```

| Soort | Bedrag rond 1960 (×0,4 in 1900, ×2,4 in 2020) | Looptijd | Rente | Bron |
|---|---|---|---|---|
| Klein | 5–10 M | 1–5 jaar | 3–5 % | `loan_util.tl:12-22` |
| Gemiddeld | 15–25 M | 3–8 jaar | 5–8 % | `loan_util.tl:24-34` |
| Groot | 30–50 M | 5–12 jaar | 8–10 % | `loan_util.tl:36-46` |
| Extra groot | 40–60 M | 10–24 jaar | 10–12 % | `loan_util.tl:48-58` |

- De kaart noemt het **Jaarlijkse rente**, maar de rente wordt **één keer** over het bedrag berekend: de totale rente is bedrag × rente, wat de looptijd ook is. Je betaalt ze in gelijke delen elke maand, samen met de aflossing (`loan_util.tl:102-111`, `loan_util.tl:126-136`, `loan.script.tl:83-99`). Een lange lening is dus per jaar goedkoper dan een korte met dezelfde rente.
- **Afbetalen** betaalt alleen de rest van de hoofdsom: de resterende rente vervalt (`loan.script.tl:171-190`). De knop vraagt dat bedrag in contanten (`finances_loan_gui.tl:284-286`).
- De rentes hangen **niet** af van de moeilijkheid: elke soort heeft zijn eigen vaste bereik (`loan_util.tl:12-58`).
- Hooguit **4 leningen** tegelijk (`loan_util.tl:4`, `loan.script.tl:134`). Een aanbieding wordt na een half jaar vervangen; de plek van een lening die je nam, blijft 4 tot 8 maanden leeg (`loan.script.tl:61-76`, `loan.script.tl:150`).
- Bij de start van een spel krijgt elk van de vier plekken de waarden van een willekeurige soort, dus de eerste "kleine" aanbieding kan een grote lening zijn; zodra een aanbieding vernieuwd wordt, biedt elke plek zijn eigen soort (`loan_util.tl:60-74`, `loan.script.tl:63-75`).

```tip scripts
**Neem de langste lening en los vroeg af.** De totale rente is bij elke looptijd gelijk, de maandbedragen zijn kleiner, en Afbetalen schrapt de resterende rente.
```

## Goed om te weten

- Neem de **langste** lening die je kunt krijgen: de rente is in totaal hetzelfde, verdeeld over meer maanden, en je kunt vroeg afbetalen zonder de rest te betalen.
- Gebouwen met tijdperkvarianten kosten ×3 en ×9 in latere tijdperken, en hun onderhoud blijft stijgen met het jaar: een gespecialiseerde opslagplaats van het laatste tijdperk is een grote vaste last.
- Een snel voertuig met een grote capaciteit kost meer in gebruik, maar vervoert ook meer: prijs en gebruikskosten volgen snelheid × capaciteit, net als de inkomsten die het kan verdienen.

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: De rente van een lening hangt alleen af van de soort (3–12 %), niet van de moeilijkheid, en wordt één keer over het bedrag berekend, verdeeld over de maanden van de looptijd; vroeg afbetalen schrapt de resterende rente. Inflatie verandert alleen de inkomsten; het onderhoud van gebouwen volgt het jaar (×1 tot ×6); voertuigprijs = 6 × jaarlijkse gebruikskosten, beide uit snelheid en capaciteit.
result: differs
```
