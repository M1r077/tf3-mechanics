---
title: Subsidies: aanbiedingen, termijnen en beloningen
summary: De vier soorten contracten, wat ze echt voltooit, wat je krijgt en wat je riskeert, en hoe vaak er nieuwe aanbiedingen komen.
domain: subsidies
official: gamemanual:management:subsidies
status: verified
updated: 2026-11-15
game: 40444
change: 40444 | Steden verbinden: de lijn die de 2x krijgt, ligt vast zodra het contract voltooid is; een reiziger telt pas na aanvaarding van de aanbieding; elke directe lijn met een reizigersvoertuig blokkeert de aanbieding.
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
| **Bevoorraad industriebedrijf** | een industriebedrijf dat nog nooit iets heeft geproduceerd en een vracht nodig heeft die al ergens op de kaart wordt geproduceerd (`deliver_cargo.script.tl:163`) | het gevraagde aantal bezorgingen eraan, **met elk van zijn invoervrachten** | `deliver_cargo.script.tl:60-67`, `deliver_cargo.script.tl:236-240`, `deliver_cargo.script.tl:463-472` |
| **Bevoorraad stad** | een vracht die de stad vraagt en helemaal niet krijgt | het gevraagde aantal eenheden **van die vracht**, bezorgd aan gebouwen van de stad | `deliver_cargo_town.script.tl:559-574` |
| **Steden verbinden** | twee steden | **één** reiziger die een rit tussen de twee steden begint op een lijn die in beide stopt | `deliver_passengers.script.tl:252-274`, `subvention_util.tl:561-592` |
| **Werknemers vervoeren** | een industriebedrijf dat al vracht verstuurt of ontvangt, nog zonder boost | zijn werknemersboost wordt actief (de helft van zijn werkplekken) | `deliver_workers.script.tl:121-131`, `deliver_workers.script.tl:152-156` |

- Elke nieuwe aanbieding kiest met gelijke kansen een van de soorten die op dat moment kunnen verschijnen (`subventions.script.tl:147-169`).
- **Bevoorraad industriebedrijf** en **Bevoorraad stad** tellen bezorgingen, geen ritten: elke betaalde eenheid die bij het doel aankomt, telt als 1. Overslaan is toegestaan (`deliver_cargo.script.tl:463-472`).
- **Steden verbinden** vraagt geen aantal reizigers: de eerste reiziger die tussen de twee steden in je lijn stapt, voltooit het. "Directe verbinding" betekent dat dit deel van de reis op één lijn gaat die beide steden bedient. Er komt geen aanbieding als een lijn al in beide steden reizigers laadt en een voertuig heeft dat ze kan vervoeren (`deliver_passengers.script.tl:76-85`).
- Steden dicht bij elkaar zijn veel waarschijnlijker: het gewicht van een paar is (afstandsgewicht)^7 × 100 plus het **gemiddelde** van de waarden van de twee steden, elk minstens 1, die de engine op de positie van de stad uit zijn raster van spelerinfrastructuur leest (`deliver_passengers.script.tl:159`, `deliver_passengers.script.tl:183`, `deliver_passengers.script.tl:188`). Het afstandsgewicht is 1 bij 1 km en daalt gelijkmatig tot 0,01 bij 20 km (`deliver_passengers.script.tl:157-159`, `deliver_passengers.script.tl:175-191`). Het afstandsdeel is dus ongeveer 19 bij 5 km, ongeveer 1 bij 10 km en bijna nul vanaf ongeveer 15 km; dan blijven alleen de waarden van de steden over.
- **Bevoorraad stad** geeft de voorkeur aan vrachten die al ergens op de kaart worden geproduceerd: 16 keer waarschijnlijker dan de andere (`deliver_cargo_town.script.tl:283-286`).
- De te leveren hoeveelheid hangt af van de instelling **Risico subsidies**:

| Risico subsidies | Bevoorraad industriebedrijf | Bevoorraad stad (hooguit de vraag van de stad) | Bron |
|---|---|---|---|
| Geen | 10–50 | 10–30 | `deliver_cargo.script.tl:106-120`, `deliver_cargo_town.script.tl:171-194` |
| Normaal | 50–100 | 30–100 | |
| Risicovol | 75–150 | 35–125 | |
| Zeer risicovol | 150–300 | 45–150 | |

## Wat is een directe verbinding?

De kaart **Steden verbinden** vraagt: "Leg een directe verbinding aan tussen {fromTownName} en {toTownName} voor het reizigersvoer tussen beide plaatsen." (`deliver_passengers.script.tl:14`).

- **Eén lijn met een halte in elke stad.** Het spel loopt de haltes van de lijn af en neemt van elke halte de stad; de lijn telt als er in elk van de twee steden minstens één halte ligt. Andere haltes, hun volgorde en het voertuigtype (bus, tram, trein, schip, vliegtuig) maken niet uit (`subvention_util.tl:561-592`).
- **Eén reiziger voltooit het**: de eerste reiziger, na aanvaarding van de aanbieding, die met die lijn van een halte in de ene stad naar een halte in de andere rijdt, in beide richtingen (`deliver_passengers.script.tl:252-274`, `deliver_passengers.script.tl:207-215`). De controle kijkt alleen naar deze rit, dus overstappen ervoor of erna zou niet moeten uitmaken.
- **De stad van een halte** is de stad van het eerste station van zijn stationsgroep (`town_util.tl:1844-1873`). Bij welke stad een station hoort, beslist de engine.
- **Geen aanbieding** als een willekeurige lijn al in elke stad een halte heeft die reizigers laadt en een voertuig dat reizigers meeneemt; elke zulke lijn wordt gecontroleerd (`deliver_passengers.script.tl:76-85`). Een lijn met alleen vracht tussen ze blokkeert de aanbieding niet.
- Het contract eindigt als **Subsidie ingetrokken** als een van de twee steden, of de lijn die het voltooide, zo verandert dat het spel het als een nieuwe versie telt (`deliver_passengers.script.tl:229-237`).

```engine
Bij welke stad een station hoort (stationSystem.getTown), wanneer precies een reiziger een lijn "begint te gebruiken" (OnStartedLineUsage) en welke wijzigingen van een lijn als een nieuwe versie tellen, hangt van de engine af. Of een wijziging van de lijn na voltooiing het effect 2x inkomsten beëindigt, is niet getest.
```

## Beloningen en boetes

Elk contract heeft drie lijsten, op zijn kaart getoond als **Bij aanvaarding**, **Na voltooiing** en **Bij mislukking**; de scripts passen ze toe bij aanvaarding, voltooiing en mislukking (`subvention_util.tl:449-471`). Bij mislukking wordt alles teruggenomen wat bij aanvaarding is gegeven, plus één boete, of twee bij Steden verbinden, een reputatieverlies in elke stad (`subvention_util.tl:457-463`, `deliver_cargo.script.tl:140-142`, `deliver_passengers.script.tl:118-121`).

| Contract | Bij aanvaarding | Na voltooiing | Bij mislukking | Bron |
|---|---|---|---|---|
| Bevoorraad industriebedrijf | geld | alleen het effect **2x inkomsten** | vooruitbetaling terug + boete | `deliver_cargo.script.tl:126-142` |
| Bevoorraad stad | geld **of** reputatie in de stad | stadservaring **of** geld, plus 2x inkomsten | vooruitbetaling terug + reputatieverlies **of** boete | `deliver_cargo_town.script.tl:200-235` |
| Steden verbinden | geld, meer bij verre steden | stadservaring in **beide** steden, plus 2x inkomsten | vooruitbetaling terug + reputatieverlies in **beide** steden | `deliver_passengers.script.tl:112-126` |
| Werknemers vervoeren | geld | geld | vooruitbetaling terug + boete | `deliver_workers.script.tl:92-116` |

- **Geld**, vóór de schaling met het jaar: vooruitbetaling 1,5 mln tot 3,75 mln × de risicofactor (Geen ×2, Normaal ×1, Risicovol ×0,75, Zeer risicovol ×0,5, of ×0,625 bij Steden verbinden en Werknemers vervoeren), en bij Steden verbinden ook × de afstandsfactor (0,3 tot 3,0); boete 3 mln tot 6 mln; betaling bij voltooiing 3,75 mln tot 11,25 mln (`deliver_cargo.script.tl:106-134`, `deliver_passengers.script.tl:89-113`, `deliver_workers.script.tl:64-104`). Elk bedrag wordt ook vermenigvuldigd met een factor uit de basisconfiguratie, `subventionFinancialRewardMultiplier` (`deliver_cargo.script.tl:126`), waarvan de waarde niet in de scripts staat.
- Geld groeit met het **kalenderjaar**, niet met de instelling Inflatie: ×1 in 1900, gelijkmatig stijgend tot ×4 vanaf 2000, naar boven afgerond op 10.000 (`finances_util.tl:87-90`). Het wordt in de financiën geboekt als **Subsidies** (`subvention_util.tl:126-135`).
- **Bevoorraad stad** kan alleen een geldbetaling bij voltooiing en een geldboete hebben als je banksaldo onder 100 mln ligt wanneer de aanbieding wordt gemaakt; daarboven kan dat nog maar bij 1 op de 10 aanbiedingen, de andere geven stadservaring en nemen in plaats daarvan reputatie af. De vooruitbetaling verandert niet (`deliver_cargo_town.script.tl:200-235`).
- **Stadservaring** is een deel van het huidige niveau van de stad: 20 % tot 100 % van de XP tussen haar niveau en het volgende (`deliver_cargo_town.script.tl:222`, `town_growth.script.tl:605-608`). Bij **Steden verbinden** wordt ze vermenigvuldigd met de afstandsfactor, van 0,3 bij 1 km tot 3,0 bij 20 km: verre steden kunnen meerdere niveaus winnen (`deliver_passengers.script.tl:101-103`, `deliver_passengers.script.tl:123-125`).
- **Reputatie** die na een mislukking verloren gaat, staat in de reputatiebeoordeling van de stad als **Mislukte subsidie** (`towns.script.tl:310-331`). Reputatie die bij aanvaarding wordt gewonnen, haalt alleen bestaande aftrekken weg; ze gaat nooit boven het maximum (`town_util.tl:1644-1647`).

## Het effect 2x inkomsten

- Het duurt **60 maanden** (5 jaar) na de voltooiing van het contract (`subvention_util.tl:286`, `subvention_util.tl:292`).
- **Bevoorraad industriebedrijf**: bezorgingen aan dat industriebedrijf, op de lijnen die er tijdens het contract aan hebben geleverd (`deliver_cargo.script.tl:456-462`).
- **Bevoorraad stad**: bezorgingen aan elk gebouw van die stad, **elke vracht**, op de lijnen die de contractvracht hebben geleverd (`deliver_cargo_town.script.tl:547-558`).
- **Steden verbinden**: reizigers tussen de twee steden, op maar **één** directe lijn: de lijn die het contract voltooide. Na de voltooiing verandert dit niet meer, ook niet met meerdere directe lijnen (`deliver_passengers.script.tl:252-299`).
- De kaart noemt de lijnen: "2x Income for {duration} on All Supplying Lines" bij Bevoorraad industriebedrijf en Bevoorraad stad (`deliver_cargo.script.tl:40-41`, `deliver_cargo_town.script.tl:44-45`), "2x Income for {duration} on First Established Connection" bij Steden verbinden (`deliver_passengers.script.tl:48-51`).
- **Werknemers vervoeren** heeft geen effect op de inkomsten (`deliver_workers.script.tl:189-190`).
- Bij Bevoorraad industriebedrijf en Bevoorraad stad geldt: een lijn die pas na de voltooiing begint te leveren, krijgt niets: de lijst met lijnen wordt alleen tijdens het contract gevuld.
- Twee contracten verdubbelen dezelfde betaling nooit twee keer: als er meerdere passen, telt alleen het laatste antwoord (`subventions.script.tl:570-583`).

```tip scripts
**Dubbel inkomen van Bevoorraad industriebedrijf of Bevoorraad stad op meerdere lijnen? Laat ze allemaal leveren voordat het contract voltooid is.** Een lijn die daarna komt, krijgt niets. Steden verbinden verdubbelt maar één lijn, de lijn die het voltooide: laat de lijn die je verdubbeld wilt hebben de eerste reiziger vervoeren.
```

```engine
Hoe de ×2 van een subsidie samengaat met de vermenigvuldiger van de bedrijfsrang (instelling Inflatie), bepaalt de engine: beide scripts geven alleen een vermenigvuldiger per betaling terug. Wat één betalingsregel is (vermoedelijk één vrachteenheid of één reiziger), bepaalt ook de engine.
```

## Termijnen

De termijn begint bij aanvaarding. Hij is langer als de vracht ver moet reizen en korter bij een hoger risico (risicofactor Geen ×2, Normaal ×1, Risicovol ×0,75, Zeer risicovol ×0,5, of ×0,625 voor de reizigers- en werknemerscontracten):

| Contract | Termijn in maanden | Gebruikte afstand | Bron |
|---|---|---|---|
| Bevoorraad industriebedrijf, Bevoorraad stad | (6 + 32 × E) × risicofactor | tot het dichtstbijzijnde industriebedrijf dat de vracht produceert | `deliver_cargo.script.tl:122-123` |
| Steden verbinden | (9 + 4 × E) × risicofactor | tussen de twee steden | `deliver_passengers.script.tl:105-106` |
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

- **Beschikbaarheid subsidies**: Zelden, Soms (standaard), Vaak, Zeer vaak geven elke 12, 6, 3 of 1 maand een nieuwe aanbieding; **Nooit** zet subsidies uit (`subvention_util.tl:13-38`, `mod.script.tl:248-249`).
- De tussentijd groeit met de **bedrijfsrang**: ×1 bij rang 1 tot ×2 bij rang 15 (`subvention_util.tl:19-22`).
- Een aanbieding **afwijzen** halveert de volgende tussentijd; aanvaarden of een nieuwe aanbieding zet hem terug (`subventions.script.tl:429`, `subventions.script.tl:395`, `subventions.script.tl:118`).
- Geen nieuwe aanbieding zolang er **5 contracten** aanvaard zijn en lopen (`subventions.script.tl:23`, `subventions.script.tl:256-262`). De eerste aanbieding komt na een halve maand (`subventions.script.tl:25`).
- Hetzelfde doel (industriebedrijf, stad en vracht, stedenpaar) wordt **maar één keer per spel** aangeboden, ook na een gemist of mislukt contract (`subventions.script.tl:107-113`, `subventions.script.tl:186`).
- Niveaupresets, beschikbaarheid / risico (`difficulty_util.tl:104-105`, `difficulty_util.tl:132-133`, `difficulty_util.tl:159-160`, `difficulty_util.tl:186-187`): Makkelijk Vaak / Geen, Gemiddeld Soms / Normaal, Moeilijk Zelden / Risicovol, **Heel moeilijk Nooit**: helemaal geen subsidies.
- De controle die subsidies alleen zou toestaan in steden met de beoordeling Zeer goed, bestaat wel, maar staat uit (`town_util.tl:1574-1580`, `deliver_cargo_town.script.tl:278-281`).

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
