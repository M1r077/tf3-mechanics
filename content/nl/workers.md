---
title: Werknemers en de werknemersboost
summary: Hoe inwoners een baan bij een industriebedrijf krijgen, welke meetellen voor de boost en hoe groot de boost is.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-14
fact: 10 / 20 | werknemers nodig voor de boost
fact: 2 jaar | zo lang telt een aankomst mee
fact: ×1,5–2,5 | boostfactor, vast per industriebedrijf
---

Elk industriebedrijf biedt werkplekken. Als er genoeg werknemers **met jouw reizigerslijnen aankomen**, produceert het bedrijf meer. Het industrievenster toont twee verschillende getallen, en die door elkaar halen is de meest voorkomende bron van verwarring.

```diagram workers_flow
```

## Wie bij een industriebedrijf kan werken

- Elk industriebedrijf uit het basisspel heeft **20 werkplekken** (`industrialCapacity = 20` in de .con.lua van elk bedrijf).
- De werkplekken zijn zo ingesteld dat inwoners er **niet te voet of met de auto** kunnen komen: alleen jouw lijnen kunnen ze brengen (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Elke inwoner heeft een woning, een winkel en een baan. Het spel kiest de baan uit de plekken die de inwoner kan bereiken; een industriebedrijf heeft een bestemmingsgewicht van 2,0 (`industryutil.lua:455`).

```engine
Hoe een inwoner één baan kiest uit alle plekken die hij kan bereiken (reistijd, kosten, het gewicht van 2,0), berekent de engine. De scripts leveren alleen de invoer.
```

## Toegewezen werknemers

De inwoners van wie dit industriebedrijf de baan is. Dit is de werkplekkenbalk in het industrievenster en de kolom **Werkplekken** in de industriestatistieken ("12/20") (`entity_window_util.tl:1238`, `statistic_industries.tl:305`). Toegewezen werknemers alleen leveren **geen** boost op: ze moeten er echt naartoe reizen.

## Werknemers die meetellen voor de boost

Een klein spelscript, `industry_workers.script.tl`, houdt elke aankomst bij:

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

## Goed om te weten

- De grens van 20 bewaarde aankomsten en de 50%-regel betekenen dat een industriebedrijf met **meer dan 40 werkplekken** (mogelijk met mods) nooit een werknemersboost zou kunnen krijgen.
- De subsidie "Werknemers vervoeren" is voltooid zodra deze boost actief wordt (officiële wiki, Subsidies).
- Boostervracht (kunstmest, machines, gereedschap) is een **aparte** boost van grondstofbedrijven en valt buiten deze pagina.
- De mod [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) toont in het industrievenster uit welke steden de toegewezen en de boostwerknemers komen, met pijlen op de kaart.

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: "Voldoende" = de helft van de werkplekken (10 van 20); "recent" = de laatste 2 speljaren, de laatste 20 aankomsten, één per persoon, alleen met jouw lijnen; boostfactor ×1,5 tot ×2,5 per industriebedrijf.
result: refines
```
