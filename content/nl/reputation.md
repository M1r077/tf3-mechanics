---
title: Reputatie van steden
summary: Wat de beoordeling Reputatie van een stad verlaagt, hoe snel die terugkomt, wat feesten en marketingcampagnes echt doen, en waarom een onderbroken weg tussen twee steden zo duur is.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
fact: −33 % | per onderbroken hoofdaansluiting naar een andere stad
fact: ≈ 67 % | herstel per jaar bij kalendersnelheid ×1 (≈ 200 % tijdens een marketingcampagne); het stadsvenster toont 33 % en 100 %
fact: 0,25 % | per verwijderde volgroeide boom bij de stad
fact: 2 mln. m³ | terreinwerk kost de hele reputatie
---

**Reputatie** is een van de zes beoordelingen in het stadsvenster, en de Plaatselijke autoriteit neemt de **laagste** daarvan (zie [Stadsgroei](towns.html)). Ze begint op 100 % en daalt alleen door wat **jij** bouwt of laat mislukken: terreinwerk, verwijderde bomen en rotsen, gesloopte stadsgebouwen, mislukte subsidies en onderbroken hoofdaansluitingen. Tijd, feesten en marketingcampagnes brengen haar terug.

```diagram rep_recovery
```

## Wat haar verlaagt

Elke bouw die je bevestigt, wordt gecontroleerd voordat hij wordt uitgevoerd; de kosten gaan naar de betrokken stad (`towns.script.tl:271-291`, `town_util.tl:1062-1080`). Alleen je eigen bouwwerken tellen, en in de kaarteditor telt niets (`town_util.tl:1078-1080`, `towns.script.tl:58`).

| Reden in het stadsvenster | Wat reputatie kost | Bron |
|---|---|---|
| **Bomen verwijderd** | 0,25 % per boom, × de afstandsfactor tot de dichtstbijzijnde stad, × de grootte van de boom (kleine bomen tellen minder) | `town_util.tl:1144-1150`, `town_util.tl:865`, `model_metadata_util.lua:655-680` |
| **Rotsen verwijderd** | 0,25 % per rots, × de afstandsfactor | `town_util.tl:1148-1149`, `town_util.tl:884-885` |
| **Landschapsverfraaiing** | 0,00005 % per m³ verhoogd **of** verlaagd terrein: 2 miljoen m³ = 100 %. Terrein dat sporen, wegen en gebouwen vormen telt ook (tot de helft minder bij bouwwerken boven 50.000 m²), net als nieuw tunnelvolume | `town_util.tl:873-886`, `town_util.tl:1245-1269`, `town_util.tl:1403-1436` |
| **Gesloopte gebouwen** | 100 % voor 40,5 % verwijderde capaciteit van een wijk (woningen, winkels of banen van die stad) | `town_util.tl:867-869`, `town_util.tl:1165-1184` |
| **Mislukte subsidie** | Bevoorraad stad: 10 % tot 60–90 % (naar risico); Steden verbinden: 10–100 % × de afstandsfactor, in **beide** steden (zie [Subsidies](subsidies.html)) | `deliver_cargo_town.script.tl:202-210`, `deliver_passengers.script.tl:113-114`, `towns.script.tl:331-333` |
| **Onderbroken hoofdaansluitingen** | **1/3** per andere stad waarvan de hoofdaansluiting onderbroken of te lang is | `town_util.tl:376-394`, `town_util.tl:1608` |

- Elke reden is begrensd op 100 % (`town_util.tl:1611-1620`).
- Tijdens het bouwen toont de tooltip **Reputatie: −x %**, met het aantal getroffen steden als het er meerdere zijn (`construction_react_util.tl:3818-3864`). Hij rekent vanaf een volle beoordeling.
- Bomen planten of rotsen plaatsen heft alleen **Bomen verwijderd** of **Rotsen verwijderd** op, met dezelfde 0,25 % per stuk. Het doet niets voor de andere redenen, en niets bij volle reputatie (`town_util.tl:1228-1238`, `town_util.tl:1630-1641`).
- De instelling Reputatie van een nieuw spel is **Uit** of **Aan** (Aan in elke voorinstelling). Uit betekent altijd een volle beoordeling (`difficulty_util.tl:44`, `difficulty_util.tl:110`, `town_util.tl:396-399`).

```engine
Hoe snel de afstandsfactor daalt tussen een stad en een verwijderde boom, welk terreinvolume elke stad krijgt, welke bomen een spoor of weg automatisch verwijdert, en welke wegen als hoofdaansluiting van een stad tellen (en wanneer een rit "te lang" is) zijn waarden van de engine (getImpactFromDistance, getTerrainBrushVolumeImpact, getTerrainAlignmentImpact, getAutoRemovalEntityImpact, getTownProblems).
```

## Onderbroken hoofdaansluitingen

Een hoofdaansluiting telt als onderbroken wanneer het spel **De wegverbinding tussen steden is onderbroken** of **De reistijd tussen steden is te lang** meldt (`town_util.tl:378-380`, `town_warning.script.tl:7-22`). Elke betrokken andere stad kost 1/3, en de beoordeling toont het **meteen** (`town_util.tl:401-403`):

| Onderbroken aansluitingen | Reputatie hoogstens | Beoordeling | Bron |
|---|---|---|---|
| 1 | 67 % | Zeer goed | `town_util.tl:983-985` |
| 2 | 33 % | Middelmatig | `town_util.tl:983-985` |
| 3 | 0 % | Zeer slecht: de stad groeit niet meer | `town_util.tl:607-633` |

- Zolang de onderbreking duurt, wordt de straf ook stap voor stap over 3 maanden in de opgeslagen score geschreven (`towns.script.tl:137-145`). Na het herstel van de weg komt dat opgeslagen deel alleen met het normale herstel terug: een lange onderbreking blijft nog een tijd reputatie kosten.
- 67 % ligt precies op de grens van Zeer goed: elk ander klein verlies zet de stad op Goed.

```tip scripts
**Bouw de nieuwe weg voordat je de oude weghaalt.** Elke onderbroken hoofdaansluiting kost meteen een derde van de reputatie, en hoe langer het duurt, hoe langer het herstel.
```

## Hoe ze terugkomt

- **Vanzelf**: één niveau (1/6) per 3 maanden speltijd (360 s), elke maand (120 s) tijdens een marketingcampagne (`towns.script.tl:121-135`). Bij kalendersnelheid ×1 is dat ongeveer **67 %** per jaar, **200 %** met een campagne: van 0 % weer vol in ongeveer 1,5 jaar. Het stadsvenster toont **Jaarlijks herstel** 33 % en 100 %: vaste teksten, de helft van de echte snelheid (`town_react_util.tl:1066`). Gemeten bij een teststad: één niveau per 358 s, per 120 s met een campagne.
- Het herstel verdeelt de winst over alle redenen; het gaat nooit voorbij de onderbroken aansluitingen die nog open zijn (`town_util.tl:1649-1687`).
- **Feesten** geven **+50 %** voor de eerste passagier die in een stad op een van je lijnen stapt, +50 % voor de eerste vracht aan een stad, +50 % bij elke niveaustijging van de stad, en +20 % voor de dichtstbijzijnde stad bij de eerste vracht aan elke industrie (`celebrations.script.tl:181-273`). Het bericht eindigt dan met **Reputatie in stad verbeterd.** of **Reputatie verbeterd in …** (`celebration_react_util.tl:63-75`). Ze tellen alleen als de reputatie niet vol is, en niet in campagnemissies (`celebrations.script.tl:79-93`, `celebrations.script.tl:140-142`).
- **Bevoorraad stad** kan bij aanvaarding +5 % tot +20 % × de risicofactor geven (`deliver_cargo_town.script.tl:195-199`). Zoals elke winst haalt dat alleen bestaande verliezen weg (`towns.script.tl:324-330`).

## Marketingcampagne

| Wat | Waarde | Bron |
|---|---|---|
| Prijs | 10 M × jaarfactor: 4 M in 1900 tot 25 M in 2020, afgerond op 1 M | `marketing_campaign_tool.script.tl:9-14` |
| Vereist | één vergunning uit de bedrijfsvoordelen | `marketing_campaign_tool.script.tl:83-95`, `company.script.tl:416-423` |
| Duur | één jaar | `marketing_campaign_tool.script.tl:136` |
| Reputatie | herstel ×3 (≈ 200 % per jaar, het venster toont 100 %); **geen** directe winst | `towns.script.tl:126`, `town_util.tl:915-925` |
| Bewoners | je lijnen in die stad tellen als half zo duur wanneer bewoners kiezen hoe ze reizen | `marketing_campaign_tool.script.tl:137`, `towns.script.tl:376-398` |

```engine
Het script rekent 360 seconden speltijd per niveau (120 met een campagne), met een maand van 30 dagen van 4 seconden. Het herstel volgt de speltijd: met een tragere kalender duurt een kalenderjaar langer, dus komt er per getoond jaar meer terug. Hoe sterk de gehalveerde lijnkosten bewoners naar je lijnen trekken, beslist de routekeuze van de engine.
```

## Goed om te weten

- Let op de bouwtooltip: toont hij **Reputatie: −x %**, dan is een tunnel of een zachter tracé vaak goedkoper dan de reputatie.
- Laat nooit een hoofdweg tussen twee steden onderbroken: elke kost meteen −33 %, en drie onderbrekingen stoppen de stad.
- Een marketingcampagne bij volle reputatie helpt alleen je lijnen, niet de beoordeling. Start haar direct na groot werk, wanneer het herstel iets in te halen heeft.
- De bonus **Reputatieherstel** van de grote hoofdkwartiermodule (+1 %) staat in het tabblad Bonussen, maar in de scripts verandert hij alleen een waarde die geen enkele beoordeling leest (`hq_module_l.module.lua:171`, `towns.script.tl:157`, `town_util.tl:829`, `town_util.tl:857`).
- De prestatie **De hatelijke nul** vraagt een stad met 0 % reputatie in vrij spelen (`achievements.script.tl:261-267`).

```check
official: "Reputation reflects how the town and surrounding nature are treated. Landscaping, removing town buildings and breaking main connections to other towns can lower it, while celebrations and marketing campaigns can improve it. Reputation lost by removing trees can be recovered by planting new ones." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Dezelfde oorzaken, plus verwijderde rotsen, tunnels, het terrein van sporen en wegen en mislukte subsidies. Elke onderbroken of te lange hoofdaansluiting kost meteen 1/3; drie stoppen de stad. Het herstel is vanzelf ongeveer 67 % per jaar en ongeveer 200 % met een marketingcampagne, het dubbele van wat het stadsvenster toont (33 % en 100 %); de campagne geeft niets meteen. Bomen planten heft alleen het verlies door bomen op. De bonus Reputatieherstel van het hoofdkwartier heeft in de scripts geen effect.
result: differs
```
