---
title: Vertrekinstellingen: volledige belading, Vulniveau en stoptijden
summary: Wanneer een voertuig een halte verlaat: de drie vertrekmodi, het vulniveau van elke vracht en de minimale, maximale en extra stoptijden.
domain: stations
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-15
game: 40444
fact: 600 s | standaard Max. stoptijd van een nieuwe halte
fact: 30 s / 60 s | standaard Maximale extra wachttijd, weg / spoor
fact: 0–100 % | Vulniveau, per vracht, van de capaciteit van het voertuig
---

Elke halte van een lijn heeft eigen vertrekinstellingen, in het venster "Vrachtfilter" van de halte (klik op de halte in het lijnvenster). Ze bepalen **hoeveel** het voertuig daar laadt en **hoe lang** het mag wachten.

## De instellingen

| Instelling | Waarden | Nieuwe halte | Bron |
|---|---|---|---|
| "Laden indien beschikbaar", "Volledige belading (willekeurig)", "Volledige belading (alle)" | een van de drie | Laden indien beschikbaar (gemeten) | `cargofilter_window.tl:798-821` |
| "Min. stoptijd" | 0–600 s, stap 10 | 0 s (gemeten) | `cargofilter_window.tl:841-845` |
| "Max. stoptijd" | 0–600 s, of "---" (geen limiet, schuif aan het eind) | **600 s** (gemeten) | `cargofilter_window.tl:855-863` |
| "Maximale extra wachttijd" | 0–600 s, stap 10 | 60 s; 30 s bij een weg- of tramstation zonder spoor | `cargofilter_window.tl:827-831`, `line_util.tl:479-487` |
| "Vulniveau", per geladen vracht | 0–100 %, stap 1 | 100 % | `cargofilter_window.tl:698-704`, `line_util.tl:473` |

- Klikken op een tijd opent een invoervak: daar kun je waarden boven 600 s typen (`cargofilter_window.tl:204-208`).
- De drie tijden blijven op volgorde: als je het minimum of de extra wachttijd boven het maximum zet, gaat het maximum ook omhoog (`cargofilter_window.tl:834-836`, `cargofilter_window.tl:848-850`); het maximum verlagen verlaagt de andere twee (`cargofilter_window.tl:865-869`). Zolang het maximum "---" is, wordt niets aangepast.
- Elke wijziging markeert de lijn als aangepast: de automatische configuratie raakt haar lijsten Lading niet meer aan (`cargofilter_window.tl:438`, zie [Laad- en lossnelheid](loading.html)). De automatische configuratie zelf wijzigt nooit de modus of de tijden, maar zet elk Vulniveau terug op 100 % (`line_util.tl:497-721`, `line_util.tl:513`, `line_util.tl:545`).

## Vulniveau: een limiet per vracht

Het vulniveau is het maximum van die vracht dat het voertuig bij deze halte meeneemt, als aandeel van de capaciteit van het voertuig, afgerond op de dichtstbijzijnde eenheid (gemeten in het spel).

| Voertuig | Vulniveau | Vertrekt met |
|---|---|---|
| vrachtwagen, 15 plaatsen, boomstammen | 50 % | **8** (7,5 naar boven afgerond) |
| vrachtwagen, 22 plaatsen, textiel | 70 % | elke keer **15** (15,4) |
| trein, 18 plaatsen, glas | 48 % | hoogstens **9** (8,64) |
| tram, 28 plaatsen, brandstof | 66 % | hoogstens **18** (18,48) |

- Vracht die al aan boord is, telt mee: een tram die met 14 brandstof aankwam, vertrok met 18, niet met 14 + 18.
- Boven de limiet wordt daardoor niets geladen **en niets gelost**: een vrachtwagen die met 22 kunstmest aankwam (limiet 11), vertrok met 22.
- **0 %** betekent: deze vracht hier niet laden.
- Met een modus voor volledige belading telt de limiet als vol: vrachtwagens met boomstammen met een vulniveau van 50 % wachtten ongeveer 270 s en vertrokken met 8 van 15, niet 15.
- Er is geen lospercentage. Het lossen wordt bepaald door de lijst Lading en "Alle vracht bij aankomst verplicht lossen" ([Laad- en lossnelheid](loading.html)).

## Volledige belading en de stoptijden

- **Laden indien beschikbaar**: het voertuig neemt wat er is en vertrekt.
- **Volledige belading (alle)**: het voertuig wacht tot het vol is. Vrachtwagens met boomstammen wachtten 460–566 s en vertrokken met 15 van 15.
- **Volledige belading (willekeurig)**: het voertuig vertrekt als één vracht vol is. Een trein voor boomstammen en planken vertrok na 369–380 s met 143 en 144 boomstammen; twee andere vertrekken na ongeveer 30 s met 57 en 118 boomstammen zijn niet verklaard.
- **Max. stoptijd** beëindigt het wachten, ook als er niets geladen is. Een groentetrein in Volledige belading (alle) met een maximum van 120 s werd ofwel in ongeveer 25 s vol (64 van 64), ofwel vertrok na 116–120 s met 26 of **0**. Met de standaard 600 s vertrok hij na 596–600 s met 26 van 64.
- **Min. stoptijd** is de hele stop, laden inbegrepen, geen extra tijd erna: met 60 s stonden glastreinen elke keer 55–61 s stil, wat ze ook laadden.
- **Maximale extra wachttijd**: "Maximum wait time after loading to improve vehicle distribution" (`cargofilter_window.tl:828`). Het voertuigvenster toont "Veilige afstand bewaren" terwijl het op zijn geplande vertrek wacht (`entity_window_util.tl:2285-2286`), vermoedelijk tijdens deze wachttijd.
- **Meerdere voertuigen bij één halte laden tegelijk**, ongeacht wanneer elk aankwam (gezien in het spel). Twee vrachtwagens met boomstammen die ongeveer 90 s na elkaar aankwamen, vertrokken in dezelfde seconde, elk met 8. Hoe de vracht tussen hen verdeeld wordt, is niet gemeten.

```engine
De scripts slaan alleen de instellingen op; wanneer een voertuig vertrekt, bepaalt de engine.
```

De regels hierboven zijn gemeten met de database van [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) (snapshots elke 2 s, dus stoptijden zijn ±2 s), november 2026.

## Goed om te weten

- Lang wachten met volledige belading bij een halte waar weinig vracht aankomt, blokkeert het perron: andere voertuigen van de lijn staan erachter in de rij.
- Een korte Max. stoptijd met volledige belading kan voertuigen leeg laten vertrekken als ze terugkomen voordat er nieuwe vracht is.
- Eén keer stond een trein in Volledige belading (alle) 783–992 s stil met een maximum van 600 s. De oorzaak is niet gevonden.

```check
official: "Full load (any): The vehicle will stop and wait until one cargo type is fully loaded. Full load (all): The vehicle will stop and wait until it is fully loaded." "In the vanilla game "all" and "any" only applies to trains and ships […] Any other vehicle type will wait for full load in both cases." Each cargo is loaded "to what percentage of a vehicle's total capacity". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles#departure_configuration))
scripts: Drie vertrekmodi, Min. / Max. stoptijd 0–600 s (of geen limiet), Maximale extra wachttijd 0–600 s (60 s, 30 s weg), Vulniveau 0–100 % per vracht; gemeten: Vulniveau begrenst de vracht aan boord, afgerond op de dichtstbijzijnde eenheid, en telt als vol voor volledige belading; Max. stoptijd beëindigt een volledige belading, ook leeg; Min. stoptijd omvat het laden; voertuigen bij één halte laden samen.
result: refines
```
