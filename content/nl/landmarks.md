---
title: Bezienswaardigheden, vieringen en leuke elementen
summary: Wat elke bezienswaardigheid aan vracht kost, wanneer ze vrijkomt en wat ze doet voor de voertuigen van haar stad, hoe de instelling Grondstoffen voor trekpleisters dat schaalt, en wat vieringen, vuurwerk, zeppelins en ufo's echt doen.
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 9 | bezienswaardigheden, één per bedrijfsrang van 2 tot 15
fact: +20 % / −20 % / +25 % | topsnelheid, vervuiling of comfort voor de voertuigen van haar stad
fact: ×0 tot ×4 | benodigde vracht, met de instelling Grondstoffen voor trekpleisters
fact: 2-4 jaar | tussen twee ufo's
---

Een bezienswaardigheid wordt gebouwd als een bouwplaats: je speelt haar vrij met een bedrijfsrang, plaatst haar en **levert er vracht aan**. Wanneer de bouwplaats al haar vracht heeft, is de bezienswaardigheid voltooid en geeft ze een bonus aan de voertuigen van **haar stad**. Het hoofdkwartier is een apart gebouw met eigen regels (zie [Bedrijfsrang, voordelen en hoofdkwartier](company.html)).

## De bezienswaardigheden

Vracht bij **Grondstoffen voor trekpleisters** ×1 (Gemiddeld).

| Bezienswaardigheid | Rang | Te leveren vracht | Bonus voor de voertuigen van haar stad | Bron |
|---|---|---|---|---|
| **Amfitheater** | 2 | 800 stenen | wegvoertuigen: geluid **−25 %** | `arena.con.lua:10`, `arena.con.lua:20-26`, `arena.con.lua:39` |
| **Grote Vuurtoren** | 5 | 1.200 stenen, 200 brandstof | schepen: topsnelheid **+20 %** | `lighthouse.con.lua:10`, `lighthouse.con.lua:14`, `lighthouse.con.lua:29`, `lighthouse.con.lua:48` |
| **Wittereigerkasteel** | 7 | 1.200 stenen, 400 planken | treinen: vervuiling **−20 %** | `white_heron_castle.con.lua:10`, `white_heron_castle.con.lua:14`, `white_heron_castle.con.lua:28`, `white_heron_castle.con.lua:47` |
| **Maritiem Museum** | 9 | 600 boomstammen, 600 planken, 200 textiel | schepen: comfort **+25 %** | `ship_museum.con.lua:10-18`, `ship_museum.con.lua:36`, `ship_museum.con.lua:55` |
| **Slot Neuschwanstein** | 10 | 1.000 stenen, 600 planken, 200 kleurstoffen | wegvoertuigen: comfort **+25 %** | `neuschwanstein.con.lua:10-18`, `neuschwanstein.con.lua:36`, `neuschwanstein.con.lua:55` |
| **Vrijheidsbeeld** | 11 | 800 stenen, 400 staal, 400 plaatmetaal | schepen: vervuiling **−20 %** | `statue_of_liberty.con.lua:10-18`, `statue_of_liberty.con.lua:38`, `statue_of_liberty.con.lua:57` |
| **Zomerpaleis** | 13 | 600 stenen, 300 planken, 300 kleurstoffen, 300 meubels | vliegtuigen: vervuiling **−20 %** | `summer_palace.con.lua:10-22`, `summer_palace.con.lua:44`, `summer_palace.con.lua:63` |
| **Opera** | 14 | 800 stenen, 400 glas, 400 plaatmetaal, 400 textiel | treinen: comfort **+25 %** | `opera_house.con.lua:10-22`, `opera_house.con.lua:44`, `opera_house.con.lua:63` |
| **Houses of Parliament** | 15 | 800 stenen, 400 planken, 400 glas, 400 meubels | wegvoertuigen, treinen, schepen en vliegtuigen: topsnelheid **+20 %** | `westminster.con.lua:10-22`, `westminster.con.lua:45`, `westminster.con.lua:79` |

- Elke bezienswaardigheid wordt één keer vrijgespeeld, door haar rang; hoe de rang groeit staat in [Bedrijfsrang, voordelen en hoofdkwartier](company.html).
- Bezienswaardigheden kosten in hun bestanden niets om te bouwen en niets per jaar: alleen de vracht (`arena.con.lua:59-64`).
- De bouwplaats slaat de helft van elke vracht tegelijk op, dus zijn er minstens twee leveringen van elke vracht nodig (`arena.con.lua:13-18`).

## Een bezienswaardigheid bouwen

- De bouwplaats heeft **4 fasen**. Ze gaat omhoog naarmate de vracht aankomt: fase 2 bij een derde van alle vracht, fase 3 bij twee derde, voltooid bij 100 %. Elke vracht telt maar tot haar eigen hoeveelheid, dus extra stenen maken ontbrekende planken niet goed (`landmarks.script.tl:34-46`).
- De bonus werkt pas wanneer de bezienswaardigheid **voltooid** is (`landmark_util_serialized.tl:393-395`). Dan verschijnt de melding "Bouw voltooid" (`landmarks.script.tl:49-61`).
- De instelling **Grondstoffen voor trekpleisters** vermenigvuldigt alle vracht: Geen ×0, Laag ×0,5, Gemiddeld ×1, Hoog ×2 of Zeer hoog ×4. De presets zijn Makkelijk ×0,5, Gemiddeld ×1, Moeilijk ×2, Heel moeilijk ×4. Bij ×0 is een bezienswaardigheid voltooid zodra ze geplaatst is (`difficulty_util.tl:40`, `difficulty_util.tl:107`, `difficulty_util.tl:135`, `difficulty_util.tl:162`, `difficulty_util.tl:189`, `landmarks.script.tl:38`, `landmarks.script.tl:46`).

## Wie de bonus krijgt

- De bonus gaat naar de stad die **het dichtst bij de bezienswaardigheid** ligt, en naar de voertuigen van het genoemde vervoermiddel waarvan dat de dichtstbijzijnde stad is (`landmark_util.tl:6-47`, `landmarks.script.tl:208-236`).
- Wanneer een voertuig het gebied van een andere stad binnenrijdt, krijgt het de bonussen van die stad en verliest het de oude (`landmarks.script.tl:279-299`).
- Bonussen van meerdere bezienswaardigheden in dezelfde stad **tellen op**: twee keer +20 % topsnelheid geeft +40 % (`landmark_util.tl:46`, `vehicle_modifier.script.tl:3-16`).

```engine
Welke stad de "dichtstbijzijnde stad" van een bezienswaardigheid of van een rijdend voertuig is, beslist de engine (getConstructionClosestTown, closestTown). Hoe de engine +25 % comfort of +20 % topsnelheid omzet in reizen en inkomsten is ook werk van de engine.
```

```tip scripts
Zet de Houses of Parliament in de stad waar de meeste van je voertuigen rijden: +20 % topsnelheid voor elk vervoermiddel. Een tweede +20 % komt van de Grote Vuurtoren voor schepen in dezelfde stad. De prestatie Overzichtelijk vraagt 10 voltooide bezienswaardigheden met dezelfde dichtstbijzijnde stad, terwijl de spelbestanden naast het hoofdkwartier 9 bezienswaardigheden bevatten (geteld); of ze in deze build haalbaar is, is onbekend (zie [Prestaties](achievements.html)).
```

## Vieringen

Een viering is het feestje dat boven een stad verschijnt wanneer er voor het eerst iets gebeurt. Het verhoogt ook de **Reputatie** van de stad, maar alleen wanneer de Reputatie nog niet vol is.

| Gebeurtenis | Reputatie | Bron |
|---|---|---|
| eerste passagier stapt in de stad in op een van je lijnen | +50 % | `celebrations.script.tl:228-252` |
| eerste vracht geleverd aan de stad | +50 % | `celebrations.script.tl:187-198` |
| de stad gaat een niveau omhoog | +50 % | `celebrations.script.tl:260-272` |
| eerste vracht geleverd aan een industrie | +20 % voor de stad die er het dichtst bij ligt | `celebrations.script.tl:202-219` |

- Een stad die een niveau omhoog gaat krijgt ook **vuurwerk**, tenzij dat uitgeschakeld is (`town_growth.script.tl:108-112`).
- Hoe Reputatie werkt: [Reputatie](reputation.html).

## Leuke elementen

- Een **zeppelin** vliegt over een stad wanneer je daar een Marketingcampagne start (`fun_elements.script.tl:112-117`).
- Een **ufo** verschijnt elke **2 tot 4 jaar** speltijd, willekeurig gekozen, wanneer er geen op de kaart is (`fun_elements.script.tl:10`, `fun_elements.script.tl:79-91`). Klik erop voor de prestatie Buitenaards bezoek.
- Geen van beide verandert de economie.

## Goed om te weten

- Kies de stad vóór het bouwen: de bonus volgt je lijnen niet, alleen de voertuigen bij die stad.
- Op Heel moeilijk heeft een bezienswaardigheid vier keer zoveel vracht nodig: de Houses of Parliament vraagt dan 3.200 stenen en 1.600 van elke andere vracht.

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: Negen bezienswaardigheden, één per rang van 2 tot 15, elk gebouwd uit geleverde vracht in 4 fasen, geschaald door Grondstoffen voor trekpleisters ×0 tot ×4. Eenmaal voltooid geeft elk één bonus (+20 % topsnelheid, −20 % vervuiling, −25 % geluid of +25 % comfort) aan de voertuigen van één vervoermiddel in de dichtstbijzijnde stad; bonussen tellen op. Vieringen geven 50 % of 20 % Reputatie; een ufo komt elke 2 tot 4 jaar.
result: adds
```
