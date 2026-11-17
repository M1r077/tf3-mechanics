---
title: Meldingen en waarschuwingen
summary: Wanneer elke waarschuwing verschijnt en wanneer ze verdwijnt: vastgelopen voertuigen, onbruikbare of overvolle stations, lijn- en halteproblemen, stadsbeoordelingen, voertuigstaat, sluitende industrieën, en welke waarschuwingen standaard niet in het logboek komen.
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 5 min | speltijd stilstaan voordat een voertuig als vastgelopen wordt gemeld
fact: 20 % | staat die de waarschuwing geeft, tot het voertuig weer boven 30 % zit
fact: 11 | meldingstypes uit in een nieuw spel
fact: 75 dagen | tussen twee controles op stations zonder wegaansluiting
---

De meeste waarschuwingen zijn **blijvend**: een spelscript controleert de situatie steeds opnieuw, de waarschuwing blijft zolang het probleem er is en verdwijnt vanzelf als het is opgelost. De controles zijn om beurten over 4 updates verdeeld, dus een waarschuwing kan even nodig hebben om te verschijnen of te verdwijnen (`notifications.script.tl:13`, `notifications.script.tl:49`).

## Wanneer elke waarschuwing verschijnt

| Waarschuwing | Verschijnt wanneer | Verdwijnt wanneer | Bron |
|---|---|---|---|
| **Voertuig staat vast** | een van je voertuigen is onderweg, niet door jou gestopt, en heeft **5 minuten** speltijd snelheid 0 | het weer rijdt | `notifications.script.tl:557-580` |
| **Station niet operationeel** | geen enkele terminal van het station laadt of lost reizigers en er ligt **niets** in het verzorgingsgebied (geen magazijn, industrie of stadsgebouw), terwijl een van je lijnen er stopt | er iets in het verzorgingsgebied komt | `notifications.script.tl:602-617`, `notifications.script.tl:630-647`, `station_useless.script.tl:39` |
| **Halte overvol** | het station heeft meer wachtende reizigers of vracht dan het aankan (overloop), terwijl een van je lijnen er stopt; reizigers vertrekken | de overloop stopt | `notifications.script.tl:599`, `notifications.script.tl:649-661`, `overcrowding.script.tl:23` |
| **Voertuigstaat** | een voertuig van jou staat op **20 %** of lager | het weer boven **30 %** zit | `notifications.script.tl:310-318` |
| **Stadsbeoordeling zeer slecht** | een van de beoordelingen van de stad zakt naar Zeer slecht (onder 1/6) | de beoordeling weer Middelmatig of beter is | `notifications.script.tl:230-238`, `town_util.tl:763-769`, `town_util.tl:983-985` |
| **Stadsbeoordeling daalt** | een beoordeling is Slecht of Middelmatig (onder 50 %) zonder in de waarschuwing Zeer slecht te zitten | de beoordeling Goed of beter is | `notifications.script.tl:240-248` |
| **Sluiting van industrie** | een industrie begint aan haar sluitingsaftelling | ze sluit, of op tijd weer gebruikt wordt | `notifications.script.tl:439-451`, `industry_close.script.tl:53-59` |
| **Geen wegaansluiting** | een station is niet op een weg aangesloten; elke **75 dagen** gecontroleerd | de volgende controle een weg vindt | `notifications.script.tl:16`, `notifications.script.tl:423-436` |
| **Probleem met lossen** | vracht van een voertuig wordt op zijn lijn nooit gelost | ze gelost wordt | `notifications.script.tl:277-290`, `cargo_rtc_warning.script.tl:28-37` |

- Een voertuig **in het depot** telt nooit als vastgelopen: die controle staat in het script uit (`notifications.script.tl:563-564`). Een voertuig dat jij hebt gestopt telt ook nooit.
- De controle van Station niet operationeel kijkt alleen naar het verzorgingsgebied. Een station waar al reizigers laden of lossen bij een terminal wordt nooit gemeld (`notifications.script.tl:606-610`).
- Hoe je een stadsbeoordeling verhoogt: [Stadsgroei](towns.html) en [Reputatie](reputation.html). Hoe de sluitingsaftelling werkt en hoe je ze stopt: [Industrieën](industries.html). Wat de staat met een voertuig doet: [Kosten, onderhoud en leningen](costs.html).

```engine
Of een station overloopt, of een voertuig een route heeft, of een lijn zijn stations kan bereiken en hoe lang de rit tussen twee steden mag duren, bepaalt de engine (calculateStationGroupCargo, getVehicleProblems, getLineProblems, getTownProblems). De scripts maken van die antwoorden alleen waarschuwingen.
```

```tip scripts
Voertuig staat vast, Probleem met voertuig, Voertuigstaat, Halte overvol en Station niet bruikbaar staan in een nieuw spel uit in het logboek. Zet ze aan in de meldingsinstellingen: juist die waarschuwingen vertellen je over een opstopping, een ontbrekende route of een versleten vloot.
```

## Lijn-, halte- en voertuigproblemen

Deze komen rechtstreeks uit de controles van de engine op je lijnen en voertuigen; het script geeft elk een titel.

| Waarschuwing | Gevallen | Bron |
|---|---|---|
| **Probleem met lijn** | te weinig stations; een station twee keer achter elkaar; stations die niet bij elkaar passen; stations konden niet verbonden worden; alternatieve terminals konden niet verbonden worden | `line_warning.script.tl:46-128` |
| **Lijn is verkeerd geconfigureerd** | een vrachtsoort die nergens geladen of nergens gelost kan worden; geen voertuig kan een vracht vervoeren die geladen moet worden; voertuigen die geen van de ingestelde vrachten vervoeren, of vrachtvoertuigen op een reizigerslijn; helemaal geen vracht ingesteld | `line_warning.script.tl:15-36`, `line_warning.script.tl:133` |
| **Probleem met station** | een halte die de huidige voertuigen niet kunnen gebruiken; een reizigershalte gebruikt door vrachtvoertuigen (één of alle); een vrachthalte gebruikt door reizigersvoertuigen; een ingestelde vrachtsoort die bij die halte niet geladen of gelost kan worden | `line_station_warning.script.tl:6-87` |
| **Probleem met voertuig** | geen geëlektrificeerde route; geen route voor grote vliegtuigen; geen route voor grote schepen; helemaal geen route; twee treinen die elkaar blokkeren | `vehicle_warning.script.tl:6-58` |
| **Stad niet verbonden** | de weg tussen twee steden is onderbroken; de rit tussen twee steden duurt te lang | `town_warning.script.tl:7-19` |

- "Geen route voor grote vliegtuigen" en "Geen route voor grote schepen" betekenen dat het voertuig te groot is voor een startbaan, kade of vaarweg op zijn lijn: zie [Vliegtuigen](aircraft.html) en [Schepen](ships.html).

## Logboek, pop-ups en instellingen

- Elk waarschuwingstype kan uitgezet worden in de meldingsinstellingen ("Meldingsregistratie configureren"). Een uitgezet type krijgt geen pop-up en wordt niet in het logboek bewaard (`notification_util.tl:145-146`, `notification_log.tl:480`).
- In een **nieuw spel** staan 11 types vanaf het begin uit: **Voertuig staat vast**, **Probleem met voertuig**, **Voertuigstaat**, **Halte overvol**, **Station niet bruikbaar**, **Halte is niet verbonden**, **Stad niet verbonden**, **Vracht niet gelost**, en de voortgangsberichten van het bedrijf voor Prospectie, Marketingcampagne en Vergroenen van de industrie (`stuck_vehicle.res.lua:7`, `vehicle_warning.res.lua:8`, `noroadconnection.res.lua:8`, `vehiclecondition.res.lua:8`, `overcrowding.res.lua:8`, `station_useless.res.lua:7`, `town_warning.res.lua:8`, `cargo_rtc_warning.res.lua:8`, `notification_util.tl:32-39`).
- Eenmalige berichten (nieuw voertuig, nieuw bouwwerk, rang omhoog, subsidies) verbergen hun pop-up na **60 seconden** speltijd; ze blijven in de geschiedenis (`notification_util.tl:10`, `notifications.script.tl:85-94`).
- Een melding eindigt ook wanneer alles waar ze naar wijst is verwijderd of herbouwd (`notifications.script.tl:95-107`).
- In een missie starten de meldingen gepauzeerd, tot de missie ze aanzet (`notifications.script.tl:700-704`).

## Goed om te weten

- Een vastgelopen-waarschuwing na 5 minuten zegt niet waarom. Kijk naar het voertuig: een rood sein, een eenrichtingssein de verkeerde kant op, of een waarschuwing Probleem met voertuig voor hetzelfde voertuig.
- "Station niet operationeel" betekent alleen "nog niets in het verzorgingsgebied". Zet het station dichter bij huizen, een industrie of een magazijn, of maak het groter.
- Een overvol station verliest reizigers: voeg voertuigen toe, of verkort het interval (zie [Vertrek en wachten](departure.html)).

```check
official: The official wiki's User Interface page describes the notification button, the log and its filters, without the conditions of each warning. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: De voorwaarden hierboven: vastgelopen na 5 minuten met snelheid 0 onderweg, voertuigstaat bij 20 % tot 30 %, stadsbeoordeling Zeer slecht onder 1/6, wegaansluiting elke 75 dagen gecontroleerd, 11 types standaard uit.
result: adds
```
