---
title: Stadsgroei: XP, beoordelingen en grootte
summary: Waar de XP van een stad vandaan komt, hoe de zes beoordelingen het groeitempo bepalen en hoeveel groter elk niveau de stad maakt.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-14
fact: 0 % | groei als één beoordeling Zeer slecht is
fact: ×1,5 | XP voor elk volgend niveau (1.000 voor niveau 2)
fact: ×40 | grootte na 17 gewonnen niveaus
---

Een stad groeit alleen door **jouw** vervoer: reizigers die met jouw lijnen aankomen en vracht die aan haar gebouwen wordt bezorgd, geven haar XP. Haar beoordelingen bepalen hoeveel van die XP meetelt, en elk gewonnen niveau maakt de stad groter.

```diagram town_xp
```

## Waar XP vandaan komt

| Bron | Ruwe XP | Bron |
|---|---|---|
| Reiziger die **met jouw lijnen** bij een stadsgebouw aankomt | 5 · 10 · 20: woning en baan of winkel in dezelfde stad, een naburige stad, een verder weg gelegen stad | `town_growth.script.tl:649-701`, `town_growth_config.res.lua:6` |
| Vrachteenheid bezorgd aan een stadsgebouw | 10 · 20 · 40 voor vrachtniveau 0 · 1 · 2 | `town_growth.script.tl:642`, `town_growth_config.res.lua:5` |
| Subsidiebeloning "stadservaring" | een deel van het huidige niveau, ook × groeitempo | `subvention_util.tl:144-152`, `town_growth.script.tl:608` |

- De XP gaat naar de stad van het gebouw waar de reiziger of de vracht **aankomt**. Een forens tussen twee steden geeft XP aan beide: op de heenweg aan de stad van de baan, op de terugweg aan de woonplaats.
- Ritten van of naar een **industriebedrijf** geven geen XP (`town_growth.script.tl:680-683`). Ritten te voet of met de auto ook niet: alleen ritten met jouw lijnen tellen (`town_growth.script.tl:656`).
- Tijd alleen levert niets op: de XP per tick is 0 (`town_cargo_util.tl:6`).
- Vrachtniveaus: **0** bakstenen, cement, vis, brandstof, vlees, planken, groente; **1** drank, boeken, kleding, meubels, machines, conserven, gereedschap; **2** voertuigen (`placementparamsutil.lua:506-616`).

Alle ruwe XP wordt vermenigvuldigd met het **groeitempo** van de stad (`town_growth.script.tl:60-63`). Het stadsvenster toont dit als **Groei:**.

## Het groeitempo

Het groeitempo komt uit twee beoordelingen in het stadsvenster (`town_util.tl:607-633`, `town_util.tl:954-962`):

1. **Plaatselijke autoriteit**: de **laagste** van haar zes beoordelingen, niet het gemiddelde (`town_util.tl:754-784`).
2. **Bevoorrading**: het gemiddelde van de bevoorradingsniveaus voor reizigers en vracht, naar boven afgerond (`town_util.tl:555-589`).

```diagram growth_matrix
```

- Elke beoordeling heeft zes niveaus: een waarde van 0–1 wordt in zesden verdeeld (`town_util.tl:983-985`). **Uitstekend** vraagt 5/6 = 83 % of meer.
- Staat **één** beoordeling op Zeer slecht, dan is de autoriteit Zeer slecht en het groeitempo **0 %**: de stad staat stil, wat je ook bezorgt.
- 100 % vraagt autoriteit Uitstekend met bevoorrading Zeer goed of beter, of autoriteit Zeer goed met bevoorrading Uitstekend.
- Je **hoofdkwartier** geeft +5 % aan de stad die er het dichtst bij ligt, en de meeste uitbreidingen geven elk nog eens +5 % (`headquarter.script.tl:510-515`, `landmark_util.tl:51-70`). Deze bonus vermenigvuldigt het tempo, dus bij 0 % doet hij niets.

## De zes beoordelingen van de autoriteit

| Beoordeling | Wat haar verlaagt | Bron |
|---|---|---|
| **Reputatie** | terrein bewerken, stadsgebouwen slopen, bomen weghalen; elke verbroken hoofdverbinding met een andere stad −1/3 | `town_util.tl:396-404`, `town_util.tl:1608` |
| **Verkeer** | verstopte straten in de stad | `town_util.tl:445-456` |
| **Blijdschap** | aandeel ontevreden reizigers (minstens 15 personen aangenomen) | `town_util.tl:479-503` |
| **Bezorging** | aandeel te late vrachtbezorgingen (zie [Vrachtinkomsten](income.html)) | `town_util.tl:505-519` |
| **Geluidsoverlast** | geluid in de stad: 65 dB of minder → volle beoordeling, 80 dB → 0 | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Vervuiling** | gemiddelde vervuiling van het stadsgebied: 60 dB → vol, 74 dB → 0 | `town_util.tl:413-431`, `emission_config.tl:23-24` |

De **gevoeligheids**instellingen van elke beoordeling (zeven stappen, de eerste is Uit) verschuiven deze grenzen; Uit betekent altijd volle beoordeling (`difficulty_util.tl:44-49`).

## Bevoorrading

- **Reizigers**: lijngebruik van de stad × 2, dus **50 % lijngebruik geeft de volle beoordeling** (`town_util.tl:546-553`).
- **Vracht**: aanbod ÷ vraag van elk district (commercieel, industrie); het **beste** district telt, niet het gemiddelde (`town_util.tl:521-529`).
- Een stad die niets te bevoorraden heeft, telt als volledig bevoorraad. Een stad die van jou geen reizigers en geen vracht krijgt, telt als "geen bezorgingen": groeitempo 0 % (`town_util.tl:565-588`).

Nieuwe vrachtbehoeften komen met de niveaus (`placementparamsutil.lua:618-660`): één commerciële en één industriële aan het begin, een tweede commerciële op niveau 5, een tweede industriële op niveau 7, een derde commerciële op niveau 9, een derde industriële op niveau 11. Ze worden pas toegevoegd zodra de stad minstens één vrachtbezorging heeft ontvangen (`town_growth.script.tl:286-288`). Het spel geeft de voorkeur aan vrachten waar nog weinig andere steden om vragen (`town_growth.script.tl:258-266`).

## Niveaus en grootte

- Niveau 2 vraagt 1.000 XP, elk volgend niveau 1,5 keer zoveel als het vorige (`town_cargo_util.tl:81-97`, `town_growth_config.res.lua:7`): niveau 5 bij 8.125 XP in totaal, niveau 10 bij ongeveer 75.000, niveau 18 (Grote metropool, het laatste) bij ongeveer 2 miljoen.
- Steden die met meer woningen worden geplaatst, beginnen hoger: niveau 2, 3 of 4 (`town_cargo_util.tl:43-54`).
- De **doelgrootte** hangt af van de niveaus die sinds de start zijn gewonnen, inclusief de voortgang naar het volgende (`town_cargo_util.tl:100-110`, `town_growth_function.tl:4-11`):

```diagram town_size
```

- De extra grootte wordt verdeeld over de woonwijken, de commerciële districten en de industriegebieden naar hoe goed elk wordt bediend: reizigersgebruik voor woningen, vrachtbevoorrading voor de andere (`town_growth.script.tl:404-421`). Zodra een district 40 % van de stad beslaat, daalt het grootste deel van de nieuwe grootte dat het kan krijgen van 100 % naar 50 % naarmate het 50 % van de stad bereikt (vergelijkbare grenzen gelden voor de hele kaart) (`town_growth.script.tl:509-522`). Wordt geen enkel district bediend, dan groeit de stad niet, zelfs niet met XP (`town_growth.script.tl:415`).

```engine
De engine berekent het lijngebruik, de verkeerssnelheid, de geluids- en vervuilingskaarten en de lijst van te late bezorgingen, en bouwt de nieuwe huizen en straten. Het kleinste aandeel dat een district altijd krijgt (townGrowthMinDistrictFraction) is een enginewaarde.
```

## Goed om te weten

- **Verbeter eerst de slechtste beoordeling**: de autoriteit is het minimum, dus de andere verbeteren helpt niets.
- Reizigers tussen **twee steden** geven 2 keer (buren) of 4 keer (verder weg) de XP van ritten binnen één stad, en aan beide steden.
- Commerciële vrachten hebben alleen niveau 0–1; alleen **voertuigen** (industrie) geven 40 XP per eenheid, en een stad vraagt er normaal pas om vanaf haar derde industriële behoefte (niveau 11).
- Een stad ver van je hoofdkwartier krijgt de bonus niet: alleen de dichtstbijzijnde stad.

```check
official: "A town needs 1,000 total XP to reach level 2. The XP required for each following level-up is 1.5 times the amount required for the previous level-up." Reizigers 5 / 10 / 20 XP, vracht 10 / 20 / 40 XP. "The Town Authority rating is determined by the lowest of six ratings." "A line usage of 50% gives the maximum rating." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Dezelfde getallen. Groeitempo 0–100 % in stappen van 20 % uit autoriteit × bevoorrading; één beoordeling Zeer slecht zet de groei stil; geen XP voor ritten naar industriebedrijven; vrachtbehoeften pas na een eerste vrachtbezorging; de derde commerciële behoefte kan in het basisspel geen niveau 2 zijn (er is geen commerciële vracht van niveau 2); grootte ×40 na 17 gewonnen niveaus.
result: refines
```
