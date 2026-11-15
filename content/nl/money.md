---
title: Waarom verlies ik geld?
summary: Wat oplevert, wat kost, en een controle in zes stappen om de lijnen te vinden die geld verliezen en waarom, met links naar de pagina's die elk punt uitleggen.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-15
fact: 1 | betaling per eenheid, bij de afnemer, voor de rechte lijn
fact: 0 | betaald bij een opslagplaats of een overstap
fact: 100 % | betaald, ook als het te laat is
fact: ×6 | jaarfactor op het onderhoud van opslagplaatsen, havens en luchthavens in 2020
---

Een bezorging betaalt voor **één rechte lijn**, van waar de vracht gemaakt is tot waar hij gebruikt wordt, en alleen als hij daar aankomt. Alles wat je bouwt en koopt kost elk jaar geld, een deel steeds meer met het kalenderjaar. Een lijn verliest geld als haar deel van de betalingen kleiner is dan de kosten die ze meebrengt.

```diagram money_flow
```

## Wat oplevert

- **De afstand in vogelvlucht** van de bron naar de afnemer, plus 8 × het hoogteverschil. De lengte van je route telt niet (`cargo_income.script.lua:3-7`, `cargo_income.script.lua:5`).
- **Elke vracht betaalt hetzelfde** per kilometer: de inkomstenfactor is 3,8 voor allemaal (`cargotype.script.lua:7-13`).
- **Eén keer, bij de afnemer.** Lossen bij een opslagplaats of een overstapstation levert niets op. De betaling wordt daarna over de lijnen van de keten verdeeld volgens de lengte in vogelvlucht van elk deel (gemeten in het spel).
- **Te late vracht wordt volledig betaald**: de reistijd wordt niet gebruikt (`cargotype.script.lua:7-13`). Te laat komen verlaagt in plaats daarvan de beoordeling **Bezorging** van de stad.
- **De bedrijfsrang** verlaagt alle inkomsten met de instelling **Inflatie**: bij rang 15 ×0,75 bij Gemiddeld (`company_progression_util.tl:25-40`).
- Een **voltooide subsidie** verdubbelt de inkomsten van de lijnen die geleverd hebben, 5 jaar lang (`subvention_util.tl:286`).

Details: [Vrachtinkomsten en bezorgtijd](income.html).

## Wat kost

- **Voertuigen**: de bedrijfskosten volgen gemiddelde snelheid × capaciteit, en de prijs is 6 jaar bedrijfskosten (`model_metadata_util.lua:499-518`, `model_metadata_util.lua:548-549`).
- **Sporen en wegen**: ongeveer een zesde van de bouwprijs per km en per jaar; hogesnelheidsspoor kost 9 keer zoveel als gewoon spoor (`simple.street_template.lua:33`, `high_speed.street_template.lua:35`).
- **Depots, stations, opslagplaatsen, havens, luchthavens**: varianten uit latere tijdperken kosten ×3 en ×9 (`rail_depot.con.lua:7`, `warehouse.tl:48`), en het onderhoud van opslagplaatsen, havens en luchthavens volgt ook het jaar, van ×1 in 1900 tot ×6 in 2020 (`mod.script.tl:92-100`).
- **Leningen**: de rente wordt één keer over het bedrag gerekend, verdeeld over de looptijd (`loan_util.tl:102-111`).
- **Inflatie verhoogt geen enkele kost**. Ze verlaagt alleen de inkomsten.

Details: [Kosten, onderhoud en leningen](costs.html).

## Zes controles, op volgorde

```diagram money_check
```

1. **Welke lijnen verliezen geld?** Kijk naar de balans van elke lijn, niet naar het totaal van het bedrijf. De mod [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) toont de balans van elke lijn over de laatste 12 maanden en het gemiddelde over meerdere jaren.
2. **Gaat de vracht ver?** Alleen de rechte lijn van bron naar afnemer betaalt. Een korte aanvoerlijn naar een opslagplaats krijgt alleen het deel van haar eigen korte stuk ([Vrachtinkomsten en bezorgtijd](income.html)).
3. **Rijdt hij vol?** Een voertuig kost hetzelfde vol of leeg. Kijk naar lege terugritten, het **Vulniveau** en de **volledige belading** van elke halte ([Vertrekinstellingen: volledige belading, Vulniveau en stoptijden](departure.html)).
4. **Wordt hij gelost waar het betaalt?** Wat niet in de lijst Lading van een halte staat, wordt gelost in elke voorraad in de buurt, ook een opslagplaats, en een opslagplaats betaalt niets ([Laad- en lossnelheid](loading.html), [Opslagplaatsen](warehouses.html)). Vracht die niet in volle voorraden van de stad past, blijft aan boord ([Stadsgroei: XP, beoordelingen en grootte](towns.html)).
5. **Te veel voertuig?** Snelheid en capaciteit kosten geld, maar snelheid betaalt niet: ze helpt alleen als ze meer ritten per jaar geeft. In de stad kan een oude, trage bus winstgevender zijn dan een nieuwe, snelle ([Kosten, onderhoud en leningen](costs.html)).
6. **Vaste kosten.** Depots, extra opslagmodules, snel spoor en gebouwen uit een later tijdperk kosten elk jaar, gebruikt of niet ([Kosten, onderhoud en leningen](costs.html)).

## Goed om te weten

- **Kies vracht op volume en afstand**, niet op prijs: elke vracht betaalt hetzelfde per km.
- Een **lange hoofdlijn** die door korte lijnen wordt gevoed, verdient het meeste geld; de aanvoerlijnen tonen kleine balansen, maar het gaat om de hele keten.
- **Meer te vervoeren**: een geboost bedrijf produceert meer ([Werknemers en de werknemersboost](workers.html), [Industrie](industries.html)), en een grotere stad vraagt meer vracht.
- Een lijn sneller maken verhoogt de betaling per eenheid niet. Het helpt alleen als dezelfde voertuigen meer ritten maken.

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks))
scripts: Hetzelfde: rechte lijn plus 8 × hoogteverschil, dezelfde factor voor elke vracht, reistijd niet gebruikt; gemeten in het spel: één keer betaald bij de afnemer en verdeeld volgens de lengte van elk deel; kosten volgen snelheid × capaciteit bij voertuigen, 1/6 van de prijs bij sporen, tijdperkvarianten ×3 / ×9 en jaarfactor ×1 tot ×6 bij gebouwen; Inflatie verlaagt alleen de inkomsten.
result: refines
```
