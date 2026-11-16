---
title: Stadsgroei: XP, beoordelingen en grootte
summary: Waar de XP van een stad vandaan komt, hoe de zes beoordelingen het groeitempo bepalen en hoeveel groter elk niveau de stad maakt.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
game: 40425
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
- Je **hoofdkwartier** geeft +5 % aan de stad die er het dichtst bij ligt, meerdere uitbreidingen geven +5 %, sommige minder of niets; de waarde staat in het bestand van elke module (`headquarter.script.tl:510-515`, `landmark_util.tl:51-70`). Deze bonus vermenigvuldigt het tempo, dus bij 0 % doet hij niets.

```tip scripts
**Groeit een stad niet meer? Verbeter eerst haar slechtste beoordeling.** De Plaatselijke autoriteit is de laagste van de zes beoordelingen: één beoordeling op Zeer slecht houdt de stad op 0 %, en de andere verbeteren verandert niets.
```

## De zes beoordelingen van de autoriteit

| Beoordeling | Wat haar verlaagt | Bron |
|---|---|---|
| **Reputatie** | terrein bewerken, stadsgebouwen slopen, bomen of rotsen weghalen, mislukte subsidies; elke verbroken hoofdverbinding met een andere stad −1/3 | `town_util.tl:396-404`, `town_util.tl:1608`, `town_react_util.tl:30-43` |
| **Verkeer** | verstopte straten in de stad | `town_util.tl:445-456` |
| **Blijdschap** | aandeel ontevreden reizigers (minstens 15 personen aangenomen) | `town_util.tl:479-503` |
| **Bezorging** | aandeel te late vrachtbezorgingen (zie [Vrachtinkomsten](income.html)) | `town_util.tl:505-519` |
| **Geluidsoverlast** | geluid in de stad: 65 dB of minder → volle beoordeling, 80 dB → 0 | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Vervuiling** | gemiddelde vervuiling per cel van 16 m van het stadsgebied, op de logaritmische schaal van de scripts ("dB", geen geluidsniveau): 60 → vol, 74 → 0 | `town_util.tl:413-431`, `emission_config.tl:23-24` |

De **gevoeligheids**instellingen verschuiven deze grenzen: Reputatie is alleen Uit / Aan, de vijf andere hebben zeven stappen van Uit tot Extreem, met Gemiddeld ×1 (Geluid en Vervuiling gaan bovenaan verder: tot ×3,5 en ×5, tegen ×3 voor de andere); Uit betekent altijd volle beoordeling (`difficulty_util.tl:44-49`).

## Bevoorrading

- **Reizigers**: lijngebruik van de stad × 2, dus **50 % lijngebruik geeft de volle beoordeling** (`town_util.tl:546-553`).
- **Vracht**: aanbod ÷ vraag van elk district (woon, commercieel, industrie), al zijn vracht samen; het **beste** district telt, niet het gemiddelde (`town_util.tl:521-543`).
- Een stad die niets te bevoorraden heeft, telt als volledig bevoorraad. Een stad die van jou geen reizigers en geen vracht krijgt, telt als "geen bezorgingen": groeitempo 0 % (`town_util.tl:565-588`).

```tip scripts
**Je hebt niet alle inwoners op je lijnen nodig: 50 % lijngebruik geeft al de volle reizigersbeoordeling.**
```

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

## Vrachtvraag en voorraden van gebouwen

- De vraag van een stad is de som van haar **gebouwen**. Elk gebouw heeft een kleine invoervoorraad per vracht waar zijn district om vraagt: capaciteit ÷ 4, naar boven afgerond, × de factor van die vracht in de behoeften van de stad (1 tenzij anders ingesteld; waar de factor vandaan komt staat niet in de scripts) (`townbuildingutil.lua:226-251`). Elke vracht legt een townConsumptionFactor van 1, 0,5 of 0,25 vast (`placementparamsutil.lua:506-616`); hoe die bij het gebouw komt, zit in de engine. Het spel merkt op dat deze voorraadgrootte "is currently nowhere shown in the UI" (op dit moment nergens in de interface wordt getoond) (`townbuildingutil.lua:249`).
- De vraag in het stadsvenster is de totale limiet van deze voorraden; het aanbod dat voor de beoordeling telt, is begrensd tot de vraag (`town_util.tl:95-99`, `town_util.tl:194-198`). Grotere steden vragen meer omdat ze meer gebouwen hebben.
- Het gebouwvenster toont een **Verbruikspercentage**: hoe snel het gebouw zijn vracht verbruikt vergeleken met zijn maximum (`town_building.tl:103-132`).
- XP en betaling komen wanneer een eenheid de voorraad van een gebouw binnenkomt (`town_growth.script.tl:620-642`).
- Een halte bereikt alleen de gebouwen in haar verzorgingsgebied. Hun voorraden kunnen vol zijn terwijl de stad als geheel nog tekort heeft: dan **blijft** de vracht die niet past **in het voertuig**, tenzij **Alle vracht bij aankomst verplicht lossen** is aangevinkt ("Vracht ook lossen als er geen ruimte is.") (`cargofilter_window.tl:757-763`), wat vernietigt wat niet past (zie [Laad- en lossnelheid](loading.html)).
- Vracht die aan boord blijft, geeft de melding **Probleem met lossen**: "{vehicle} heeft {cargoCount} stuks vracht niet gelost op de lijn." (`cargo_rtc_warning.script.tl:28-41`, `cargo_rtc_warning.script.tl:37`); het typelabel is **Vracht niet gelost** (`cargo_rtc_warning.res.lua:6`).
- **Vrachtvraag steden** ("Bepaal het maximale aantal vrachtvragen per stad."): 2, 4 of 6, standaard 2 (`difficulty_util.tl:54`, `difficulty_util.tl:83`, `mod.script.tl:173`, `mod.script.tl:205`). De scripts voegen vrachtbehoeften toe per niveau (zie hierboven) en geven deze waarde door aan de engine.

```engine
Hoe snel een gebouw zijn voorraad verbruikt (consumeFrequency), welk gebouw in een verzorgingsgebied elke eenheid krijgt, wat er gebeurt met vracht die rondgereden wordt en hoe de engine Vrachtvraag steden gebruikt, ligt in de engine.
```

## Kan ik een stad tegenhouden in haar groei?

- In een normaal spel is er **geen instelling** voor een maximale stadsgrootte (`difficulty_util.tl:90-199`).
- In de **sandboxmodus** heeft het stadsvenster een kaart **Beoogde capaciteit wijk** met **Stedelijke ontwikkeling inschakelen** (`town_eow.script.tl:1041-1052`, `town_eow.script.tl:1170-1171`, `town_eow_editor_initial_capacity.res.lua:6`). Uitgevinkt krijgt de stad geen XP en wordt ze niet van grootte veranderd; het venster toont **Stadsontwikkeling inactief** (`town_growth.script.tl:28`, `town_growth.script.tl:345`, `town_eow.script.tl:107`).
- Zonder sandbox kan het alleen indirect: een stad groeit alleen door jouw reizigers en vracht, en één beoordeling Zeer slecht houdt haar tegen (zie hierboven).

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
