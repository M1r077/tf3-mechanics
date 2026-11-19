---
title: Prestaties
summary: Wat het spelscript voor elke prestatie in het Vrije spel controleert en wanneer, welke alleen voertuigen, vracht en dieren van het basisspel tellen, en welke controles aan de engine worden overgelaten.
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-17
game: 40444
fact: 17 | prestaties die het spelscript zelf ontgrendelt
fact: 500 m | hoogte van de eerste wagon van een trein bij een halte voor Topper
fact: < 1 % | reputatie van de stad voor De hatelijke nul
fact: 10 | bezienswaardigheden die dezelfde dichtstbijzijnde stad moeten hebben voor Overzichtelijk
---

De officiële wiki noemt 41 prestaties. Het spelscript (`achievements.script.tl`) ontgrendelt er zelf **17** en voedt **9 spelbrede tellers**; de rest (campagne, weer, stadsgrootte, magazijn, rente, boosters, auto's, 1900-2000, stoom in de jaren 2000) wordt elders gecontroleerd, door de engine of het platform. Elke controle vraagt eerst aan de engine of de prestatie nog ontgrendeld kan worden; of mods of instellingen dat blokkeren, wordt daar beslist (`achievements.script.tl:632`, `achievements.script.tl:510`).

## Prestaties die het script controleert

| Prestatie | Wat het script controleert | Bron |
|---|---|---|
| **Pakket bezorgd** | één vrachtstuk bereikt zijn bestemming | `achievements.script.tl:221-225`, `achievements.script.tl:632-636` |
| **Mede mogelijk gemaakt door** | één subsidie voltooid | `achievements.script.tl:241-244`, `achievements.script.tl:638-642` |
| **Subsidiepakker** | 10 subsidies voltooid zonder mislukte ertussen; een mislukte subsidie zet de telling terug op 0 | `achievements.script.tl:243-249`, `achievements.script.tl:644-648` |
| **Zorgplicht** | de leveringsbeoordeling van een stad wordt **Uitstekend** | `achievements.script.tl:270-276`, `towns.script.tl:27-30`, `achievements.script.tl:650-654` |
| **Stedelijke ontwikkeling** | een stad stijgt een niveau | `achievements.script.tl:253-255`, `town_growth.script.tl:92` |
| **Groeiende vraag** | een stad krijgt vraag naar een nieuw vrachttype | `achievements.script.tl:257-259`, `achievements.script.tl:668-672` |
| **De hatelijke nul** | de Reputatie van een stad **daalt** tot onder **1 %** | `achievements.script.tl:261-267`, `towns.script.tl:33-36` |
| **Promotie** | het bedrijf stijgt een rang | `achievements.script.tl:280-282`, `achievements.script.tl:680-684` |
| **Carrièreladder** | het bedrijf bereikt de hoogste rang | `achievements.script.tl:284-290`, `achievements.script.tl:686-690` |
| **Landschapsverfraaiing** | je plaatst bomen, en alleen bomen, in één bouwactie (niets verwijderd, niet via herbebossing) | `achievements.script.tl:346-377` |
| **Perfectionist** | hetzelfde station wordt gesloopt, herbouwd, gesloopt en herbouwd, in die volgorde, zonder dat ertussen een ander station wordt gebouwd of verwijderd | `achievements.script.tl:304-341`, `achievements.script.tl:694-710` |
| **Overzichtelijk** | precies 10 voltooide bezienswaardigheden hebben dezelfde dichtstbijzijnde stad | `achievements.script.tl:382-395`, `achievements.script.tl:713-721` |
| **Topper** | een van je treinen komt aan bij een halte met de eerste wagon hoger dan **500 m** | `achievements.script.tl:407-417`, `achievements.script.tl:723-727` |
| **Offshore** | een van je helikopters komt aan bij een halte van een olieplatform | `achievements.script.tl:420-450`, `achievements.script.tl:729-733` |
| **Opgescheept** | elk scheepsmodel van het basisspel vaart tegelijk op een van je scheepvaartlijnen | `achievements.script.tl:735-776` |
| **Buitenaards bezoek** | je klikt op een ufo | `achievements.script.tl:793-806` |
| **Tijdreiziger** | je verandert het tijdstip van de dag met de hand | `achievements.script.tl:839-844` |

- **Perfectionist** telt alleen een bouwactie die één heel station toevoegt of verwijdert: een perron of module aan een station toevoegen telt niet (`achievements.script.tl:301-302`).
- **Overzichtelijk** telt elke bezienswaardigheid wanneer ze af is, voor de stad die er op dat moment het dichtst bij ligt (`achievements.script.tl:386`).
- **Opgescheept** wordt alleen gecontroleerd als een scheepsmodel dat nog nooit gestopt heeft bij een halte aankomt; het kijkt naar de voertuigen van je scheepvaartlijnen, niet naar schepen in een depot (`achievements.script.tl:736`, `achievements.script.tl:750-766`).
- **De hatelijke nul** vraagt om Reputatie, niet om een andere beoordeling: zie [Reputatie van steden](reputation.html).

```tip scripts
Topper controleert de hoogte van de eerste wagon wanneer de trein stopt, niet de hoogte van het stationsgebouw. Bouw het station op een berg boven 500 m en laat er één trein rijden.
```

## Spelbrede tellers

Deze lopen door van spel tot spel (het platform bewaart ze). Het script stuurt alleen wat sinds de vorige controle is veranderd.

| Teller | Prestatie | Wat telt | Bron |
|---|---|---|---|
| Spoorlengte | **Reis om de aarde** | de groei van de totale lengte in het logboek (in km); er gaat niets af als je sloopt | `achievements.script.tl:511-523` |
| Bevolking | **Wereldbevolking** | de groei van de bevolking van de kaart, vanaf de bevolking bij het laden van het spel | `achievements.script.tl:512`, `achievements.script.tl:525-533` |
| Reizigers | **Alles voor de reiziger** | reizigers die een reis op een van je lijnen hebben afgemaakt | `achievements.script.tl:236-238`, `achievements.script.tl:535-541` |
| Vracht | **Goed, beter, best** | afgeleverde vrachtstukken | `achievements.script.tl:543-549` |
| Klimaten | **Ultieme tycoon** | het klimaat van de kaart, wanneer het bedrijf daar de hoogste rang bereikt | `achievements.script.tl:551-567` |
| Inkomsten | **Zwemmen in het geld** | je opgetelde inkomsten, in miljarden | `achievements.script.tl:202-204`, `achievements.script.tl:569-590` |
| Vrachttypes | **Door weer en wind** | elk vrachttype van het basisspel één keer afgeleverd | `achievements.script.tl:20-22`, `achievements.script.tl:230-232`, `achievements.script.tl:592-607` |
| Voertuigen | **Kenner** | elk voertuigmodel van het basisspel dat één keer bij een halte aankomt | `achievements.script.tl:16-18`, `achievements.script.tl:469-481`, `achievements.script.tl:609-625` |
| Dieren | **Dierenvriend** | elk dier van het basisspel waarop je één keer klikt | `achievements.script.tl:24-26`, `achievements.script.tl:809-834` |

- Voertuigen, vracht en dieren uit mods tellen nooit mee voor deze tellers: alleen bestanden van het basisspel (`::/vehicle`, `::/cargos`, `::/animal`) worden genomen (`achievements.script.tl:16-26`).
- Voor Kenner moet een voertuig **bij een halte aankomen** van een lijn; kopen is niet genoeg.

```engine
Of een prestatie nog ontgrendeld kan worden (isAchievementUnlockable), of de tellers uitgeschakeld zijn (areStatsDisabled), de doelen van elke teller en de 24 prestaties die niet in het script staan, worden door de engine en het platform afgehandeld. De officiële wiki zegt dat prestaties over het algemeen niet beschikbaar zijn met niet-cosmetische mods of met spelinstellingen die afwijken van de standaardwaarden.
```

## Goed om te weten

- Elke "eerste keer"-prestatie wordt vergeleken met de vorige controle: ze vraagt om een **nieuwe** gebeurtenis in een spel waarin de prestatie nog open is; een oude subsidie of rang uit een opgeslagen spel telt niet opnieuw (`achievements.script.tl:633`, `achievements.script.tl:779`).
- Je rang, subsidies en Reputatie worden uitgelegd in [Bedrijfsrang, voordelen en hoofdkwartier](company.html), [Subsidies](subsidies.html) en [Reputatie van steden](reputation.html).

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: 17 prestaties en 9 tellers staan in het script. Het verfijnt de officiële teksten: Zorgplicht betekent dat de leveringsbeoordeling Uitstekend bereikt, De hatelijke nul een Reputatie onder 1 %, Topper de eerste wagon boven 500 m, Perfectionist slopen-herbouwen-slopen-herbouwen van hetzelfde station, en Opgescheept alle scheepsmodellen van het basisspel tegelijk op lijnen. Alleen voertuigen, vracht en dieren van het basisspel tellen voor de tellers.
result: refines
```
