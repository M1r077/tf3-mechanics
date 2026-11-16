---
title: Subsidies: aanbiedingen, termijnen en beloningen
summary: De vier soorten contracten, wat ze echt voltooit, wat je krijgt en wat je riskeert, en hoe vaak er nieuwe aanbiedingen komen.
domain: subsidies
official: gamemanual:management:subsidies
status: verified
updated: 2026-11-15
fact: 4 | soorten contracten in vrij spelen
fact: 5 | aanvaarde contracten hooguit tegelijk
fact: ×2 | inkomsten gedurende 5 jaar op de lijnen die hebben geleverd
fact: 0 | boete voor het afwijzen van een aanbieding
---

Een subsidie is een contract: een industriebedrijf of een stad biedt een taak aan, je krijgt iets bij aanvaarding, meer als je de taak op tijd voltooit, en je betaalt de vooruitbetaling plus een boete terug als je de termijn mist. Een aanbieding afwijzen of laten verlopen kost niets.

```diagram subsidy_life
```

## De vier soorten contracten

```diagram subsidy_types
```

| Contract | Doel | Wat het voltooit | Bron |
|---|---|---|---|
| **Bevoorraad industriebedrijf** | een industriebedrijf dat nog nooit iets heeft geproduceerd | het gevraagde aantal bezorgingen eraan, **met elk van zijn invoervrachten** | `deliver_cargo.script.tl:54-61`, `deliver_cargo.script.tl:230-234`, `deliver_cargo.script.tl:470-479` |
| **Bevoorraad stad** | een vracht die de stad vraagt en helemaal niet krijgt | het gevraagde aantal eenheden **van die vracht**, bezorgd aan gebouwen van de stad | `deliver_cargo_town.script.tl:566-581` |
| **Steden verbinden** | twee steden | **één** reiziger die een rit tussen de twee steden begint op een lijn die in beide stopt | `deliver_passengers.script.tl:263-280`, `subvention_util.tl:561-592` |
| **Werknemers vervoeren** | een industriebedrijf dat al vracht verstuurt of ontvangt, nog zonder boost | zijn werknemersboost wordt actief (de helft van zijn werkplekken) | `deliver_workers.script.tl:121-131`, `deliver_workers.script.tl:152-156` |

- Elke nieuwe aanbieding kiest met gelijke kansen een van de soorten die op dat moment kunnen verschijnen (`subventions.script.tl:147-169`).
- **Bevoorraad industriebedrijf** en **Bevoorraad stad** tellen bezorgingen, geen ritten: elke betaalde eenheid die bij het doel aankomt, telt als 1. Overslaan is toegestaan (`deliver_cargo.script.tl:470-479`).
- **Steden verbinden** vraagt geen aantal reizigers: de eerste reiziger die tussen de twee steden in je lijn stapt, voltooit het. "Directe verbinding" betekent dat dit deel van de reis op één lijn gaat die beide steden bedient. Er komt geen aanbieding als er al een lijn reizigers tussen ze vervoert (`deliver_passengers.script.tl:72-78`).
- Steden dicht bij elkaar zijn veel waarschijnlijker: het gewicht van een paar daalt van 1 bij 1 km of minder tot 0,01 bij 20 km, tot de macht 7 (`deliver_passengers.script.tl:175-191`).
- **Bevoorraad stad** geeft de voorkeur aan vrachten die al ergens op de kaart worden geproduceerd: 16 keer waarschijnlijker dan de andere (`deliver_cargo_town.script.tl:277-280`).
- De te leveren hoeveelheid hangt af van de instelling **Risico subsidies**:

| Risico subsidies | Bevoorraad industriebedrijf | Bevoorraad stad (hooguit de vraag van de stad) | Bron |
|---|---|---|---|
| Geen | 10–50 | 10–30 | `deliver_cargo.script.tl:100-114`, `deliver_cargo_town.script.tl:165-188` |
| Normaal | 50–100 | 30–100 | |
| Risicovol | 75–150 | 35–125 | |
| Zeer risicovol | 150–300 | 45–150 | |

## Wat is een directe verbinding?

De kaart **Steden verbinden** vraagt: "Leg een directe verbinding aan tussen {fromTownName} en {toTownName} voor het reizigersvoer tussen beide plaatsen." (`deliver_passengers.script.tl:14`).

- **Eén lijn met een halte in elke stad.** Het spel loopt de haltes van de lijn af en neemt van elke halte de stad; de lijn telt als er in elk van de twee steden minstens één halte ligt. Andere haltes, hun volgorde en het voertuigtype (bus, tram, trein, schip, vliegtuig) maken niet uit (`subvention_util.tl:561-592`).
- **Eén reiziger voltooit het**: de eerste reiziger die met die lijn van een halte in de ene stad naar een halte in de andere rijdt, in beide richtingen (`deliver_passengers.script.tl:263-280`, `deliver_passengers.script.tl:210-218`). De controle kijkt alleen naar deze rit, dus overstappen ervoor of erna zou niet moeten uitmaken.
- **De stad van een halte** is de stad van het eerste station van zijn stationsgroep (`town_util.tl:1844-1873`). Bij welke stad een station hoort, beslist de engine.
- **Geen aanbieding** als een lijn al in elke stad een halte heeft die reizigers laadt en een voertuig dat reizigers meeneemt (`deliver_passengers.script.tl:72-78`). Een lijn met alleen vracht tussen ze blokkeert de aanbieding niet.
- Het contract eindigt als **Subsidie ingetrokken** als een van de twee steden, of de lijn die het voltooide, zo verandert dat het spel het als een nieuwe versie telt (`deliver_passengers.script.tl:232-240`).

```engine
Bij welke stad een station hoort (stationSystem.getTown), wanneer precies een reiziger een lijn "begint te gebruiken" (OnStartedLineUsage) en welke wijzigingen van een lijn als een nieuwe versie tellen, hangt van de engine af. Of een wijziging van de lijn na voltooiing het effect 2x inkomsten beëindigt, is niet getest.
```

## Beloningen en boetes

Elk contract heeft drie lijsten, op zijn kaart getoond als **Bij aanvaarding**, **Na voltooiing** en **Bij mislukking** (`subvention_util.tl:449-471`). Bij mislukking wordt de vooruitbetaling altijd terugbetaald, plus nog een boete (`deliver_cargo.script.tl:134-136`).

| Contract | Bij aanvaarding | Na voltooiing | Bij mislukking | Bron |
|---|---|---|---|---|
| Bevoorraad industriebedrijf | geld | alleen het effect **2x inkomsten** | vooruitbetaling terug + boete | `deliver_cargo.script.tl:120-136` |
| Bevoorraad stad | geld **of** reputatie in de stad | stadservaring **of** geld, plus 2x inkomsten | vooruitbetaling terug + reputatieverlies **of** boete | `deliver_cargo_town.script.tl:194-229` |
| Steden verbinden | geld, meer bij verre steden | stadservaring in **beide** steden, plus 2x inkomsten | vooruitbetaling terug + reputatieverlies in **beide** steden | `deliver_passengers.script.tl:105-119` |
| Werknemers vervoeren | geld | geld | vooruitbetaling terug + boete | `deliver_workers.script.tl:92-116` |

- **Geld**, vóór de schaling met het jaar: vooruitbetaling 1,5 mln tot 3,75 mln × de risicofactor (Geen ×2, Normaal ×1, Risicovol ×0,75, Zeer risicovol ×0,5); boete 3 mln tot 6 mln; betaling bij voltooiing 3,75 mln tot 11,25 mln (`deliver_cargo.script.tl:120-128`, `deliver_workers.script.tl:102-104`).
- Geld groeit met het **kalenderjaar**, niet met de instelling Inflatie: ×1 in 1900, gelijkmatig stijgend tot ×4 vanaf 2000, naar boven afgerond op 10.000 (`finances_util.tl:87-90`). Het wordt in de financiën geboekt als **Subsidies** (`subvention_util.tl:126-135`).
- **Bevoorraad stad** geeft geldbeloningen en geldboetes alleen zolang je banksaldo onder 100 mln ligt; daarboven kan dat nog maar bij 1 op de 10 aanbiedingen (`deliver_cargo_town.script.tl:206-217`).
- **Stadservaring** is een deel van het huidige niveau van de stad: 20 % tot 100 % van de XP tussen haar niveau en het volgende (`deliver_cargo_town.script.tl:216`, `town_growth.script.tl:605-608`). Bij **Steden verbinden** wordt ze vermenigvuldigd met de afstandsfactor, van 0,3 bij 1 km tot 3,0 bij 20 km: verre steden kunnen meerdere niveaus winnen (`deliver_passengers.script.tl:94-96`, `deliver_passengers.script.tl:116-118`).
- **Reputatie** die na een mislukking verloren gaat, staat in de reputatiebeoordeling van de stad als **Mislukte subsidie** (`towns.script.tl:313-334`). Reputatie die bij aanvaarding wordt gewonnen, haalt alleen bestaande aftrekken weg; ze gaat nooit boven het maximum (`town_util.tl:1644-1647`).

## Het effect 2x inkomsten

- Het duurt **60 maanden** (5 jaar) na de voltooiing van het contract (`subvention_util.tl:286`, `subvention_util.tl:292`).
- **Bevoorraad industriebedrijf**: bezorgingen aan dat industriebedrijf, op de lijnen die er tijdens het contract aan hebben geleverd (`deliver_cargo.script.tl:463-469`).
- **Bevoorraad stad**: bezorgingen aan elk gebouw van die stad, **elke vracht**, op de lijnen die de contractvracht hebben geleverd (`deliver_cargo_town.script.tl:554-565`).
- **Steden verbinden**: reizigers tussen de twee steden, op maar **één** directe lijn: de laatste directe lijn waarop een reiziger tussen die steden is ingestapt. Dit wordt ook na het contract bijgewerkt, dus met twee directe lijnen kan de ×2 van de ene naar de andere gaan (`deliver_passengers.script.tl:263-296`).
- **Werknemers vervoeren** heeft geen effect op de inkomsten (`deliver_workers.script.tl:90`).
- Bij Bevoorraad industriebedrijf en Bevoorraad stad geldt: een lijn die pas na de voltooiing begint te leveren, krijgt niets: de lijst met lijnen wordt alleen tijdens het contract gevuld.
- Twee contracten verdubbelen dezelfde betaling nooit twee keer: als er meerdere passen, telt alleen het laatste antwoord (`subventions.script.tl:570-583`).

```tip scripts
**Dubbel inkomen van Bevoorraad industriebedrijf of Bevoorraad stad op meerdere lijnen? Laat ze allemaal leveren voordat het contract voltooid is.** Een lijn die daarna komt, krijgt niets. Steden verbinden verdubbelt maar één lijn, de laatste directe waarop reizigers zijn ingestapt: houd één directe lijn tussen de twee steden.
```

```engine
Hoe de ×2 van een subsidie samengaat met de vermenigvuldiger van de bedrijfsrang (instelling Inflatie), bepaalt de engine: beide scripts geven alleen een vermenigvuldiger per betaling terug. Wat één betalingsregel is (vermoedelijk één vrachteenheid of één reiziger), bepaalt ook de engine.
```

## Termijnen

De termijn begint bij aanvaarding. Hij is langer als de vracht ver moet reizen en korter bij een hoger risico (risicofactor Geen ×2, Normaal ×1, Risicovol ×0,75, Zeer risicovol ×0,5, of ×0,625 voor de reizigers- en werknemerscontracten):

| Contract | Termijn in maanden | Gebruikte afstand | Bron |
|---|---|---|---|
| Bevoorraad industriebedrijf, Bevoorraad stad | (6 + 32 × E) × risicofactor | tot het dichtstbijzijnde industriebedrijf dat de vracht produceert | `deliver_cargo.script.tl:116-117` |
| Steden verbinden | (9 + 4 × E) × risicofactor | tussen de twee steden | `deliver_passengers.script.tl:98-99` |
| Werknemers vervoeren | (6 + 15 × E) × risicofactor × tijdperkfactor (×1,75 vóór 1940, ×1,25 vóór 1980) | tot de dichtstbijzijnde stad | `deliver_workers.script.tl:75-87` |

E is de tijd die een trein met de topsnelheid van het tijdperk (120 km/h vanaf 1900 tot 300 km/h vanaf 1981) nodig heeft voor die afstand, naar boven afgerond, minstens 1 (`subvention_util.tl:486-489`, `vehicle_util.tl:225-230`).

- Een aanbieding die niet wordt aanvaard, verdwijnt na ongeveer **6 maanden** (150 tot 210 dagen), zonder boete (`subvention_util.tl:284`, `subvention_util.tl:290`).
- Zolang een contract **Bevoorraad industriebedrijf** of **Werknemers vervoeren** loopt, kan het doelbedrijf niet sluiten: een geplande sluiting wordt geannuleerd (`subvention_util.tl:473-484`).
- Als het doel tijdens het contract verdwijnt of opnieuw wordt gebouwd, toont het spel **Subsidie ingetrokken**, maar de boetes worden toegepast als bij een gemiste termijn (`subventions.script.tl:172-190`, `subvention_util.tl:406-412`).
- Er is geen knop om een aanvaard contract te annuleren.

```engine
Hoe lang een spelmaand duurt, en dus de echte lengte van de termijnen, legt de engine vast (getDefaultMonthDuration). De formules hierboven zijn in maanden van de spelkalender.
```

## Hoe vaak nieuwe aanbiedingen komen

- **Beschikbaarheid subsidies**: Zelden, Soms (standaard), Vaak, Zeer vaak geven elke 12, 6, 3 of 1 maand een nieuwe aanbieding; **Nooit** zet subsidies uit (`subvention_util.tl:13-38`, `mod.script.tl:247-248`).
- De tussentijd groeit met de **bedrijfsrang**: ×1 bij rang 1 tot ×2 bij rang 15 (`subvention_util.tl:19-22`).
- Een aanbieding **afwijzen** halveert de volgende tussentijd; aanvaarden of een nieuwe aanbieding zet hem terug (`subventions.script.tl:429`, `subventions.script.tl:395`, `subventions.script.tl:118`).
- Geen nieuwe aanbieding zolang er **5 contracten** aanvaard zijn en lopen (`subventions.script.tl:23`, `subventions.script.tl:256-262`). De eerste aanbieding komt na een halve maand.
- Hetzelfde doel (industriebedrijf, stad en vracht, stedenpaar) wordt **maar één keer per spel** aangeboden, ook na een gemist of mislukt contract (`subventions.script.tl:107-113`, `subventions.script.tl:186`).
- Niveaupresets, beschikbaarheid / risico (`difficulty_util.tl:104-105`, `difficulty_util.tl:132-133`, `difficulty_util.tl:159-160`, `difficulty_util.tl:186-187`): Makkelijk Vaak / Geen, Gemiddeld Soms / Normaal, Moeilijk Zelden / Risicovol, **Heel moeilijk Nooit**: helemaal geen subsidies.
- De controle die subsidies alleen zou toestaan in steden met de beoordeling Zeer goed, bestaat wel, maar staat uit (`town_util.tl:1574-1580`, `deliver_cargo_town.script.tl:272-275`).

## Goed om te weten

- Aanvaard gerust als het doel makkelijk is: afwijzen of negeren kost niets, maar **mislukken** kost de vooruitbetaling plus een boete die groter kan zijn dan de vooruitbetaling.
- Lever bij **Bevoorraad stad** en **Bevoorraad industriebedrijf** met elke lijn die ervan moet profiteren: alleen de lijnen die tijdens het contract hebben geleverd, krijgen 5 jaar lang 2x inkomsten.
- **Steden verbinden** met ver uit elkaar liggende steden geeft de meeste stadservaring en vraagt maar één reiziger.
- **Bevoorraad industriebedrijf** betaalt bij voltooiing niets extra: de beloning is alleen de 2x inkomsten.

```check
official: "Accept an offer to begin the contract; declining it has no penalty." "Possible rewards include town experience, an additional payment, or a limited-time 2x income effect on eligible transport lines." "The upfront reward is reversed, and an additional fine or loss of town reputation may apply." ([Subsidies](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:subsidies))
scripts: Vier soorten; één reiziger voltooit Steden verbinden; de ×2 duurt 60 maanden op de lijnen die tijdens het contract hebben geleverd; Bevoorraad industriebedrijf geeft alleen de ×2; geld geschaald met het jaar (×1 tot ×4); elke 1–12 maanden een nieuwe aanbieding, minder vaak bij hoge bedrijfsrang; hooguit 5 aanvaard; elk doel één keer per spel.
result: refines
```
