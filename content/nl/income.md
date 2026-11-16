---
title: Vrachtinkomsten en bezorgtijd
summary: Wat een bezorging oplevert (afstand in vogelvlucht, hoogteverschil, bedrijfsrang, subsidies) en wat te laat komen echt kost.
domain: economy
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
game: 40425
fact: 3,8 | dezelfde inkomstenfactor voor elke vracht
fact: +8 × stijging | meters stijging opgeteld bij de afstand
fact: 100 % | betaald, ook als de bezorging te laat is
---

Een bezorging betaalt voor de **afstand in vogelvlucht**, en verder niets van de rit. Snelheid telt om een andere reden: elke vracht heeft een **tijdslimiet**, en te late bezorgingen verlagen de beoordeling **Bezorging** van de stad, niet je inkomsten.

```diagram income_formula
```

## De inkomstenformule

De hele formule staat in één kort spelscript (`cargo_income.script.lua:10-13`):

1. **Inkomstenfactor** van de vracht. Elke vracht uit het basisspel gebruikt dezelfde functie en dezelfde prijzen (`initialPrice = 4`, `finalPrice = 3.2`), wat **3,8 voor alle 36 vrachten** oplevert (`cargotype.script.lua:7-13`, `coal.cargo.lua:21-22`). Steenkool betaalt over dezelfde afstand precies evenveel als goederen.
2. Instelling **Inkomsten vracht**: 50 %, 75 %, 100 %, 125 % of 150 % (`difficulty_util.tl:38`, `mod.script.tl:211`). Alle vier de niveaupresets gebruiken 100 % (`difficulty_util.tl:97`).
3. **Afstand**, zie hieronder.

De functie krijgt de reistijd mee, maar **gebruikt die niet** (`cargotype.script.lua:7-13`): een trage of te late bezorging betaalt hetzelfde.

## Afstand: rechte lijn plus stijging

```diagram income_distance
```

- De afstand is de **rechte lijn in 3D** tussen de twee punten, niet de lengte van je route (`cargo_income.script.lua:3-7`).
- Als het hoogteverschil positief is, wordt **8 × die hoogte** opgeteld (`cargo_income.script.lua:5`): 100 m stijging betaalt als 800 m extra. In de andere richting wordt niets afgetrokken.
- Een kronkelende lijn verdient dus evenveel als een rechte, maar je betaalt onderhoud voor elke meter spoor of weg die je hebt gebouwd.

```engine
De engine kiest de twee punten en geeft ze door aan het script. In het spel gemeten (zie hieronder): het zijn de **bron** van de vracht (de industrie of het stadsgebouw dat haar produceerde) en de **afnemer** die haar ontvangt, zoals de officiële wiki zegt ("between the source and the final destination").
```

## Vracht die van lijn wisselt

Als een eenheid over meerdere lijnen reist, bijvoorbeeld schip → opslagplaats → trein, betaalt het spel haar toch **maar één keer**:

```diagram income_split
```

1. Uitladen bij een opslagplaats of een overstapstation betaalt **niets**. Van ongeveer 17.000 gemeten betalingen gingen er maar 43 naar een voorraad die geen afnemer was.
2. Als het laatste voertuig aan de afnemer levert, wordt de eenheid betaald met de formule hierboven, voor de rechte lijn **van de bron naar de afnemer**. De trajecten en de echte route tellen niet, dus een omweg via een opslagplaats levert niets extra op.
3. Dat geld wordt verdeeld over de lijnen van de keten, **naar verhouding van de lengte in rechte lijn van elk traject**: van het ene ophaalpunt naar het volgende, en van het laatste ophaalpunt naar de afnemer. De stijgingsbonus telt bij deze verdeling niet mee.
4. Het leverende voertuig houdt eerst het hele bedrag vast, met één deel per traject. Het wordt een paar seconden speltijd later geboekt (mediaan ongeveer 6 s), waarbij elke lijn en elk voertuig zijn eigen deel krijgt. Het saldo van een lijn verandert dus kort na de bezorging, niet bij de opslagplaats.

Een korte aanvoerlijn naar een opslagplaats verdient dus weinig, ook al doet ze al het verzamelwerk; het lange traject verdient het meeste. Elke lijn toont haar echte deel wel in haar eigen saldo.

```engine
De scripts berekenen alleen het totaal (`economy/cargo_income.script.lua`); de verdeling doet de engine en is niet zichtbaar in de scripts. De regels hierboven zijn gemeten met een alleen-lezen testmod: ongeveer 1.700 betalingen van eenheden met 2 of 3 trajecten, en de rekeningwijzigingen van elke betrokken lijn en elk betrokken voertuig. In 769 zuivere gevallen (één eenheid, één betaling) kwam de verdeling elke keer tot op 1 % overeen met de trajectlengtes; een verdeling met de stijgingsbonus klopte in maar 59 % ervan, een gelijke verdeling in geen enkel.
```

## Wat het bedrag verder verandert

| Wat | Effect | Bron |
|---|---|---|
| **Bedrijfsrang** met de instelling Inflatie | rang 1: ×1, gelijkmatig dalend tot rang 15: ×0,9 (Laag), **×0,75 (Gemiddeld)**, ×0,6 (Hoog), ×0,5 (Zeer hoog); Geen: altijd ×1 | `company_progression_util.tl:25-40`, `difficulty_util.tl:50`, `mod.script.tl:694-697` |
| **Voltooide subsidie** | ×2 voor leveringen aan het industriebedrijf of de stad van het contract, op de lijnen die voor het contract hebben geleverd | `deliver_cargo.script.tl:463-469`, `deliver_cargo_town.script.tl:554-565` |
| **Te late bezorging** | geen effect op de inkomsten | `cargotype.script.lua:7-13` |

- De rangvermenigvuldiger geldt voor **elke** betaling voor vracht en reizigers (`company_growth.script.tl:159-170`). De niveaupresets gebruiken Inflatie Laag (Makkelijk), Gemiddeld (Gemiddeld), Hoog (Moeilijk), Zeer hoog (Heel moeilijk) (`difficulty_util.tl:108`).
- De ×2 van subsidies geldt alleen voor de lijnen die tijdens het contract hebben geleverd, en voor beperkte tijd (officiële wiki, Subsidies).

## Reizigers

Reizigers gebruiken dezelfde afstand en een vaste inkomstenfactor van ongeveer 3,61 (`cargotype.script.lua:50-53`), vermenigvuldigd met **0,5 + de ticketprijsfactor van het voertuig** (`cargo_income.script.lua:14-17`). Als een voertuigmodel geen comfortfactor instelt, zet het spel de prijsfactor op 0,3 voor bussen en trams, 0,9 voor vliegtuigen, 0,1 voor schepen en 0,5 voor treinen (`base_mod.lua:46-61`); voor de andere modellen is het een enginewaarde, niet zichtbaar in de scripts. Een reizigerssubsidie verdubbelt alleen de reizigers tussen haar twee steden, op haar ene lijn (`deliver_passengers.script.tl:292-296`).

## Tijdslimieten voor bezorging

Elke vracht heeft haar eigen tijdslimiet (`meat.cargo.lua:30`, `coal.cargo.lua:30`). Vers voedsel heeft de kortste, zware grondstoffen een vijf keer langere:

```diagram delivery_times
```

- **Financiën › Bezorgtijd** toont de limiet van elke vracht op jouw kaart; de laag Vrachttevredenheid kleurt de routes van groen tot rood.
- Een bezorging telt als **vertraagd** als ze na haar limiet aankomt (`towns.script.tl:425`).
- Gespecialiseerde opslagmodules **bevriezen** de timer van de vracht die ze opslaan (officiële wiki, Warehouses).

```engine
De engine zet de basistijd om in de tijdslimiet die in Financiën wordt getoond (de scripts lezen die met getAdjustedDeliveryTime) en bepaalt wanneer een eenheid te laat is. Alleen de relatieve waarden hierboven komen uit de vrachtbestanden.
```

## Wat te laat komen kost: de beoordeling Bezorging

Te late vracht wordt volledig betaald, maar elke stad houdt een beoordeling **Bezorging** bij (`town_util.tl:505-519`):

1. Het spel telt de bezorgingen aan de stad in het **afgelopen halfjaar**, en hoeveel daarvan te laat waren (er worden er minstens 10 aangenomen, zodat de eerste bezorgingen de score niet laten omslaan).
2. Aandeel op tijd → beoordeling: onder een ondergrens is de beoordeling 0, boven een bovengrens 1, daartussen lineair. Met de standaardgevoeligheid (**Gemiddeld**): **30 % op tijd → 0, 100 % → 1**, dus 90 % op tijd geeft 0,86.
3. De instelling **Gevoeligheid bezorging** verschuift de grenzen (`difficulty_util.tl:47`). Uit: altijd 1. Presets: Makkelijk Laag, Gemiddeld Gemiddeld, Moeilijk Hoog, Heel moeilijk Zeer hoog (`difficulty_util.tl:113`).

```diagram delivery_rating
```

Bezorging is een van de zes beoordelingen waarvan de laagste het groeitempo van de stad bepaalt: één beoordeling Zeer slecht zet de stad stil (zie [Stadsgroei](towns.html)).

## Voorbeeld

Dezelfde steenkoolbezorging, 5 km in vogelvlucht.

| Situatie | Betaald |
|---|---|
| vlak, elke routelengte | **100 %** |
| 10 km uit elkaar | **200 %** |
| bestemming 100 m hoger | **116 %** |
| te laat bezorgd | **100 %** (beoordeling Bezorging daalt) |
| bedrijfsrang 15, Inflatie Gemiddeld | **75 %** |
| levering gedekt door een voltooide subsidie | **200 %** |

## Goed om te weten

- Omdat elke vracht per kilometer hetzelfde betaalt, **kies je vrachten op volume, afstand en tijdslimiet**, niet op prijs.
- Tijdslimieten tellen het zwaarst bij vlees, vis, groente en drank: korte lijnen of opslagplaatsen die de timer bevriezen.
- Elke eenheid die aan een stadsgebouw wordt bezorgd, geeft die stad ook ervaring (`town_growth.script.tl:642`, `town_growth_config.res.lua:5`).

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks), [Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Dezelfde factor 3,8 voor alle vrachten; afstand in 3D plus 8 × stijging; de bedrijfsrang verlaagt de inkomsten tot ×0,75 bij rang 15 (Inflatie Gemiddeld); ×2 na een subsidie; de tijd wordt niet gebruikt voor de inkomsten; in het spel gemeten: een eenheid die van lijn wisselt, wordt één keer betaald, bij de afnemer, en over de lijnen verdeeld naar trajectlengte; beoordeling Bezorging uit het aandeel op tijd van het afgelopen halfjaar (Gemiddeld: 30 % → 0, 100 % → 1).
result: refines
```
