---
title: Werknemers en de werknemersboost
summary: Hoe inwoners een baan bij een industriebedrijf krijgen, welke meetellen voor de boost en hoe groot de boost is.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-15
fact: 10 / 20 | werknemers nodig voor de boost
fact: 2 jaar | zo lang telt een aankomst mee
fact: ×1,5–2,5 | boostfactor, vast per industriebedrijf
---

Elk industriebedrijf biedt werkplekken. Als er genoeg werknemers **met jouw reizigerslijnen aankomen**, produceert het bedrijf meer. Het industrievenster toont twee verschillende getallen, en die door elkaar halen is de meest voorkomende bron van verwarring.

```diagram workers_flow
```

## Wie bij een industriebedrijf kan werken

- Elk industriebedrijf uit het basisspel heeft **20 werkplekken** (`industrialCapacity = 20`).
- De werkplekken zijn zo ingesteld dat inwoners er **niet te voet of met de auto** kunnen komen: alleen jouw lijnen kunnen ze brengen (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Elke inwoner heeft een woning, een winkel en een baan. Het spel kiest de baan uit de plekken die de inwoner kan bereiken; een industriebedrijf heeft een bestemmingsgewicht van 2,0 (`industryutil.lua:455`).

```engine
Hoe een inwoner één baan kiest uit alle plekken die hij kan bereiken (reistijd, kosten, het gewicht van 2,0), berekent de engine. De scripts leveren alleen de invoer.
```

## Toegewezen werknemers

De inwoners van wie dit industriebedrijf de baan is. Dit is de werkplekkenbalk in het industrievenster en de kolom **Werkplekken** in de industriestatistieken ("12/20") (`entity_window_util.tl:1238`, `statistic_industries.tl:305`). Toegewezen werknemers alleen leveren **geen** boost op: ze moeten er echt naartoe reizen.

## Werknemers die meetellen voor de boost

Een klein spelscript houdt elke aankomst bij (`industry_workers.script.tl`):

1. Als een inwoner bij een industriebedrijf aankomt en zijn **laatste verplaatsing met jouw lijnen** was, wordt de aankomst met de speltijd genoteerd (`industry_workers.script.tl:86-118`).
2. Alleen aankomsten van de **laatste 2 speljaren** worden bewaard (`industry_productivity_util.tl:3`: `2 * getDefaultYearDuration()`).
3. Hooguit de **laatste 20** aankomsten worden bewaard (`industry_workers.script.tl:4`, `KeepHistoryCount = 20`).
4. Komt dezelfde persoon opnieuw aan, dan vervangt de nieuwe aankomst de oude: elke inwoner telt **één keer** (`industry_workers.script.tl:56-70`).

```diagram workers_window
```

## Wanneer de boost begint en stopt

- Het bedrijf krijgt de boost zodra de getelde werknemers **de helft van de werkplekken** bereiken: `geteld ≥ werkplekken × 0,5` (`industry_productivity_util.tl:35-48`, `RequiredWorkersFractionForBoost = 0.5`). Bij 20 werkplekken: **10 werknemers**.
- Het onderdeel Boosters in het industrievenster toont precies dit: "geteld / nodig", met nodig naar boven afgerond (`industry_react_util.tl:627`).
- De controle loopt opnieuw zodra er nieuwe aankomsten zijn of de oudste ouder dan 2 jaar wordt (`industry_workers.script.tl:40-43`). De boost **stopt dus vanzelf** ongeveer 2 jaar nadat er geen werknemers meer komen.

## Hoe groot de boost is

- De productie wordt vermenigvuldigd met de **boostfactor** van het bedrijf, in het venster getoond als "+X %" (`industry_react_util.tl:716`).
- De factor wordt één keer bepaald uit de willekeurige seed van het bedrijf: **tussen ×1,5 en ×2,5**, en verandert voor dat bedrijf nooit (`industry_productivity_util.tl:58-72`). Een bedrijf zonder seed gebruikt ×2.
- Twee identieke mijnen kunnen dus een verschillende werknemersboost hebben: kijk naar de "+X %" voordat je kiest welke je bedient.

## Voorbeeld

Een steenkolenmijn met 20 werkplekken en "+84 %".

| Situatie | Geteld | Boost? | Productie |
|---|---|---|---|
| Nieuwe buslijn: 14 inwoners toegewezen, nog niemand aangekomen | 0 | nee | ×1 |
| 12 verschillende inwoners kwamen dit jaar met de bus | 12 | ja (≥ 10) | ×1,84 |
| Buslijn verwijderd; 2 jaar lang komt niemand | zakt naar 0 | stopt | ×1 |

## Werknemers naar een industriebedrijf brengen

```diagram workers_trip
```

- Een werknemer telt mee als hij **bij het bedrijf zelf aankomt**, het doel van zijn reis (`targetOrAtEntity`) het bedrijf is en zijn laatste vervoerswijze **Lijnen** is (`industry_workers.script.tl:86-94`). Uitstappen bij een halte is niet genoeg: de persoon moet het bedrijf bereiken.
- Elke inwoner heeft één vervoerswijze per bestemming (woning, winkel, baan). Het industrievenster toont de toegewezen werknemers met een icoon voor deze wijze: **Stap**, **Auto** of **Lijnen** (`entity_window_util.tl:1400-1435`). Voor een bedrijf zou het altijd Lijnen moeten zijn, omdat lopen en auto daar niet zijn toegestaan (`industryutil.lua:451-457`).
- „Niet lopen” betekent dus dat de hele reis geen wandeling of autorit mag zijn. Het betekent niet „helemaal niet lopen”: een reis met Lijnen begint en eindigt nog steeds te voet tussen de haltes en de gebouwen (zie de engine-notitie hieronder).
- **Overstappen telt.** Het script kijkt alleen naar de wijze van de reis, niet naar hoeveel lijnen gebruikt zijn (`industry_workers.script.tl:91`). Een werknemer uit een stad vier lijnen verderop telt net zo als een van naast de deur, maar kan veel langer over de reis doen.
- **Elk van jouw lijnen kan ze brengen**, ook een lijn die vracht vervoert, zolang de voertuigen passagiers meenemen en de halte passagiers laadt. Het script controleert het voertuigtype niet (`industry_workers.script.tl:86-118`). Spelers melden minder problemen met aparte passagierslijnen.
- Sommige bedrijven (bijvoorbeeld olieplatforms) hebben een eigen ingebouwde halte, die passagiers en vracht neemt (`industryutil.lua:156-165`).
- Het industrievenster toont voor elke toegewezen werknemer of hij **Momenteel hier** of **Onderweg** is (`entity_window_util.tl:1371-1384`). Het onderdeel Booster toont de getelde werknemers met hun **Resterende tijd** van de 2 jaar (`entity_window_util.tl:1579-1630`, `industry_eow.script.tl:644-649`).
- Een bedrijf zonder werknemers toont: "Sluit deze locatie aan op het openbaar vervoer, zodat de inwoners er kunnen gaan werken." (`entity_window_util.tl:1650-1652`).

```engine
Welke halte een bedrijf bedient, hoe ver een werknemer van een halte naar de ingang van het bedrijf loopt, en de inwoners van welke steden de baan nemen, beslist de engine (verzorgingsgebieden, routebepaling, baankeuze). De scripts stellen geen afstandsgrens voor werknemers. Spelers melden dat een station waarvan het verzorgingsgebied het bedrijf voor vracht dekte, geen werknemers bracht tot er een bus naar de ingang van het bedrijf reed (Steam-topic "Problem getting workers to site").
```

```tip
**Krijg de werknemersboost (en het contract Werknemers vervoeren) snel: begin met een eenvoudige lijn.**

1. Maak een **nieuwe passagierslijn** van een halte bij het bedrijf naar **één stad**.
2. Plaats de halte in de stad zo dat het verzorgingsgebied **geen van je andere passagiersstations raakt**.
3. Eén voertuig is genoeg om te beginnen.

De banen worden verdeeld wanneer de lijn opent: in twee tests gingen **alle 20 banen naar die ene stad**, en de boost begon na **346 s en 925 s** speltijd (één keer met maar één voertuig). Toen de halte in de stad het verzorgingsgebied van een netwerkstation raakte, gingen een paar banen naar een verre stad en deden de laatste werknemers er veel langer over (964 s). Gemeten met [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) en het [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard); wie een baan krijgt, bepaalt nog steeds de engine.
```

## Subsidie Werknemers vervoeren

- Hij wordt alleen aangeboden voor een bedrijf met arbeidsplaatsen waarvan de werknemersboost nog niet actief is en dat het afgelopen jaar vracht heeft verstuurd of ontvangen, volgens de jaarcijfers van de engine (`deliver_workers.script.tl:121-131`, `industry_util.tl:541-558`). Of alleen ontvangen genoeg is, hangt af van hoe de engine de productieregels vult; dat staat niet in de scripts.
- Hij is voltooid zodra de werknemersboost actief wordt: dezelfde 10 van 20 verschillende aankomsten met jouw lijnen (`deliver_workers.script.tl:152-156`). Er telt niets anders; er is geen verborgen regel.
- De voortgangsbalk op de contractkaart is "getelde werknemers ÷ de helft van de werkplekken" (`deliver_workers.script.tl:267-272`, `industry_util.tl:11-18`).
- De pijlen op de contractkaart komen van de **5 dichtstbijzijnde steden**. Ze zijn alleen een hint: het script tekent ze op afstand, niet op wie de baan heeft (`deliver_workers.script.tl:297-317`).
- Zie [Subsidies: aanbiedingen, termijnen en beloningen](subsidies.html) voor geld en termijn.

## Waarom komen mijn werknemers niet aan?

| Controle | Waar kijken | Waarom |
|---|---|---|
| Heeft iemand de baan? | Werkplekkenbalk ("12/20") | Zonder toegewezen werknemers reist niemand. De baankeuze ligt bij de engine. |
| Wijze-icoon van de werknemers | Werknemerslijst: Stap / Auto / Lijnen | Alleen reizen met Lijnen kunnen meetellen (`industry_workers.script.tl:91`). |
| Zijn ze onderweg? | **Onderweg** / **Momenteel hier** | Lang "Onderweg": trage of overvolle overstappen, of geen route vanaf de laatste halte. |
| Bereikt de laatste halte de ingang van het bedrijf? | Verzorgingsgebied van de halte, toegangsweg | Gemeld door spelers; ligt bij de engine. Een korte bus naar de ingang hielp. |
| Laadt de halte passagiers? | Lijnhalte, Vrachtfilter | Passagiers moeten aan beide kanten van de reis geladen en gelost worden. |
| 10 **verschillende** personen in 2 jaar? | Onderdeel Booster, **Resterende tijd** | Dezelfde persoon telt één keer; oudere aankomsten vallen af (`industry_workers.script.tl:56-70`). |
| Meer dan 40 werkplekken (mods)? | Werkplekkenbalk | Kan met 20 bewaarde aankomsten nooit de helft halen. |

## Goed om te weten

- De grens van 20 bewaarde aankomsten en de 50%-regel betekenen dat een industriebedrijf met **meer dan 40 werkplekken** (mogelijk met mods) nooit een werknemersboost zou kunnen krijgen.
- De subsidie **Werknemers vervoeren** is voltooid zodra deze boost actief wordt (`deliver_workers.script.tl:152-156`).
- Boostervracht (kunstmest, machines, gereedschap) is een **aparte** boost van grondstofbedrijven en valt buiten deze pagina.
- De mod [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) toont in het industrievenster uit welke steden de toegewezen en de boostwerknemers komen, met pijlen op de kaart.

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: "Voldoende" = de helft van de werkplekken (10 van 20); "recent" = de laatste 2 speljaren, de laatste 20 aankomsten, één per persoon, alleen met jouw lijnen; boostfactor ×1,5 tot ×2,5 per industriebedrijf. Overstappen telt; de reiswijze moet Lijnen zijn, en lopen vanaf een halte hoort bij zo'n reis.
result: refines
```
