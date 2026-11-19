---
title: Reputacja miast
summary: Co obniża ocenę Reputacja miasta, jak szybko wraca, co naprawdę dają uroczystości i kampanie reklamowe oraz dlaczego przerwana droga między dwoma miastami tak dużo kosztuje.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
game: 40444
fact: −33 % | za każde przerwane połączenie główne z innym miastem
fact: ≈ 67 % | odzysku na rok przy tempie kalendarza ×1 (≈ 200 % w czasie kampanii reklamowej); okno miasta pokazuje 33 % i 100 %
fact: 0,25 % | za każde usunięte dorosłe drzewo przy mieście
fact: 2 mln m³ | prac ziemnych kosztuje całą reputację
---

**Reputacja** to jedna z sześciu ocen w oknie miasta, a Władze miejskie biorą **najniższą** z nich (zobacz [Rozwój miast](towns.html)). Zaczyna się od 100 % i spada tylko przez to, co **ty** budujesz lub zawalasz: prace ziemne, usunięte drzewa i skały, wyburzone budynki miasta, nieuzyskane subsydia i przerwane połączenia główne. Czas, uroczystości i kampanie reklamowe ją przywracają.

```diagram rep_recovery
```

## Co ją obniża

Każda budowa, którą zatwierdzasz, jest sprawdzana przed wykonaniem; koszt trafia do danego miasta (`towns.script.tl:268-288`, `town_util.tl:1062-1080`). Liczą się tylko twoje budowy, a w edytorze map nic się nie liczy (`town_util.tl:1078-1080`, `towns.script.tl:230`, `towns.script.tl:268`).

| Powód w oknie miasta | Co kosztuje reputację | Źródło |
|---|---|---|
| **Usunięte drzewa** | 0,25 % za drzewo, × współczynnik odległości od najbliższego miasta, × wielkość drzewa (małe drzewa liczą się mniej) | `town_util.tl:1144-1150`, `town_util.tl:865`, `model_metadata_util.lua:655-680` |
| **Usunięte skały** | 0,25 % za skałę, × współczynnik odległości | `town_util.tl:1148-1149`, `town_util.tl:884-885` |
| **Kształtowanie terenu** | 0,00005 % za m³ terenu podniesionego **lub** obniżonego: 2 miliony m³ = 100 %. Liczy się też teren kształtowany przez tory, drogi i budynki (zmniejszany od 10 000 m², do połowy od 50 000 m²) oraz netto objętość nowych tuneli | `town_util.tl:873-886`, `town_util.tl:1245-1269`, `town_util.tl:1403-1436` |
| **Wyburzone budynki** | 100 % za 40,5 % usuniętej pojemności dzielnicy (mieszkania, sklepy lub miejsca pracy tego miasta) | `town_util.tl:867-869`, `town_util.tl:1165-1184` |
| **Nieuzyskane subsydia** | Zaopatrz miasto: jedna losowo wybrana kara, utrata reputacji (od 10 % do 60–90 % wg ryzyka) albo kara pieniężna; zawsze utrata reputacji, gdy kara pieniężna nie jest oferowana. Połącz miasta: 10–100 % × współczynnik odległości, w **obu** miastach (zobacz [Subsydia](subsidies.html)) | `deliver_cargo_town.script.tl:208-216`, `deliver_cargo_town.script.tl:215-217`, `deliver_cargo_town.script.tl:231`, `deliver_passengers.script.tl:120-121`, `towns.script.tl:328-330` |
| **Przerwane połączenia główne** | **1/3** za każde inne miasto, którego połączenie główne jest przerwane lub za długie | `town_util.tl:376-394`, `town_util.tl:1608` |

- Każdy powód ma limit 100 % (`town_util.tl:1611-1620`).
- Podczas budowy podpowiedź pokazuje **Reputacja: –x %**, z liczbą dotkniętych miast, jeśli jest ich kilka (`construction_react_util.tl:3829-3875`). Liczy koszt od pełnej oceny.
- Sadzenie drzew lub stawianie skał znosi tylko **Usunięte drzewa** lub **Usunięte skały**, po tych samych 0,25 % za sztukę. Nie pomaga przy innych powodach ani przy pełnej reputacji (`town_util.tl:1228-1238`, `town_util.tl:1630-1641`).
- Ustawienie Reputacja nowej gry to **Wył.** lub **Wł.** (Wł. w każdym ustawieniu wstępnym). Wył. oznacza zawsze pełną ocenę (`difficulty_util.tl:44`, `difficulty_util.tl:110`, `town_util.tl:396-399`).

```engine
Jak szybko spada współczynnik odległości między miastem a usuniętym drzewem, jaką objętość terenu dostaje każde miasto, które drzewa tor lub droga usuwa automatycznie i które drogi liczą się jako połączenie główne miasta (oraz kiedy podróż jest „za długa”) to wartości silnika (getImpactFromDistance, getTerrainBrushVolumeImpact, getTerrainAlignmentImpact, getAutoRemovalEntityImpact, getTownProblems).
```

## Przerwane połączenia główne

Połączenie główne liczy się jako przerwane, gdy gra zgłasza **Połączenie drogowe między miastami zostało przerwane** lub **Czas podróży między miastami jest zbyt długi** (`town_util.tl:378-380`, `town_warning.script.tl:7-22`). Każde inne takie miasto kosztuje 1/3, a ocena pokazuje to **od razu** (`town_util.tl:401-403`):

| Przerwane połączenia | Reputacja najwyżej | Ocena | Źródło |
|---|---|---|---|
| 1 | 67 % | Bardzo dobre | `town_util.tl:983-985` |
| 2 | 33 % | Kiepskie | `town_util.tl:983-985` |
| 3 | 0 % | Bardzo złe: miasto przestaje rosnąć | `town_util.tl:607-633` |

- Dopóki przerwa trwa, kara jest też zapisywana w zapisanym wyniku, krok po kroku, przez 3 miesiące (`towns.script.tl:134-142`). Po naprawie drogi ta zapisana część wraca tylko w normalnym tempie odzysku: długa przerwa jeszcze przez jakiś czas kosztuje reputację.
- 67 % leży dokładnie na granicy Bardzo dobre: każda inna drobna strata obniża miasto do Dobre.

```tip scripts
**Zbuduj nową drogę, zanim usuniesz starą.** Każde przerwane połączenie główne od razu kosztuje jedną trzecią reputacji, a im dłużej trwa, tym dłużej trwa powrót.
```

## Jak wraca

- **Sama**: jeden poziom (1/6) co 3 miesiące czasu gry (360 s), co miesiąc (120 s) w czasie kampanii reklamowej (`towns.script.tl:118-132`). Przy tempie kalendarza ×1 to około **67 %** na rok, **200 %** z kampanią: od 0 % do pełna w około 1,5 roku. Okno miasta pokazuje **Roczny odzysk** 33 % i 100 %: stałe teksty, połowa rzeczywistego tempa (`town_react_util.tl:1066`). Zmierzone w mieście testowym: jeden poziom co 358 s, co 120 s z kampanią.
- Odzysk rozkłada zysk na wszystkie powody; nigdy nie przekracza wciąż otwartych przerwanych połączeń (`town_util.tl:1649-1687`).
- **Uroczystości** dodają **+50 %** za pierwszego pasażera, który w mieście wsiada do jednej z twoich linii, +50 % za pierwszy ładunek dostarczony do miasta, +50 % przy każdym awansie miasta na wyższy poziom i +20 % dla najbliższego miasta za pierwszy ładunek dostarczony do każdego przemysłu (`celebrations.script.tl:181-273`). Komunikat kończy się wtedy na **Reputacja w osiedlu wzrosła.** lub **Wzrost reputacji (…).** (`celebration_react_util.tl:63-75`). Liczą się tylko, gdy reputacja jest poniżej tego, na co pozwalają jeszcze przerwane połączenia główne (pełna minus 1/3 za każde przerwane połączenie), a ustawienie Reputacja jest na „Wł.”, i nie w misjach kampanii (`celebrations.script.tl:79-93`, `celebrations.script.tl:140-142`).
- **Zaopatrz miasto** daje przy przyjęciu albo zaliczkę w gotówce, albo od +5 % do +20 % × współczynnik ryzyka, losowo (`deliver_cargo_town.script.tl:203-206`, `deliver_cargo_town.script.tl:226-228`). Jak każdy zysk usuwa tylko istniejące straty (`towns.script.tl:321-327`).

## Kampania reklamowa

| Co | Wartość | Źródło |
|---|---|---|
| Cena | 10 M × współczynnik roku: 4 M w 1900 do 25 M w 2020, zaokrąglone do 1 M | `marketing_campaign_tool.script.tl:9-14` |
| Wymaga | jednego pozwolenia z zalet firmy | `marketing_campaign_tool.script.tl:83-95`, `company.script.tl:416-423` |
| Czas trwania | jeden rok | `marketing_campaign_tool.script.tl:136` |
| Reputacja | odzysk ×3 (≈ 200 % na rok, okno pokazuje 100 %); **żadnego** natychmiastowego zysku | `towns.script.tl:123`, `town_util.tl:915-925` |
| Mieszkańcy | twoje linie w tym mieście liczą się jako o połowę tańsze, gdy mieszkańcy wybierają, jak podróżować | `marketing_campaign_tool.script.tl:137`, `towns.script.tl:373-395` |

```engine
Skrypt liczy 360 sekund czasu gry na poziom (120 z kampanią), z miesiącem z 30 dni po 4 sekundy. Odzysk biegnie w czasie gry: przy wolniejszym kalendarzu rok kalendarza trwa dłużej, więc na pokazany rok wraca więcej. Jak mocno o połowę niższy koszt linii przyciąga mieszkańców do twoich linii, decyduje wybór trasy w silniku.
```

## Warto wiedzieć

- Patrz na podpowiedź przy budowie: jeśli pokazuje **Reputacja: –x %**, tunel lub łagodniejsza trasa często kosztuje mniej niż reputacja.
- Nigdy nie zostawiaj przerwanej głównej drogi między dwoma miastami: każda to od razu −33 %, a trzy przerwy zatrzymują miasto.
- Kampania reklamowa przy pełnej reputacji pomaga tylko twoim liniom, nie ocenie. Uruchom ją zaraz po dużych pracach, gdy odzysk ma co odrabiać.
- Premia **Odzyskiwanie reputacji** dużego modułu centrali (+1 %) widnieje w zakładce Premie, ale w skryptach zmienia tylko wartość, której żadna ocena nie czyta (`hq_module_l.module.lua:171`, `towns.script.tl:154`, `town_util.tl:829`, `town_util.tl:857`).
- Osiągnięcie **To nie ja** wymaga miasta, którego reputacja spada poniżej 1 % (`achievements.script.tl:261-267`).

```check
official: "Reputation reflects how the town and surrounding nature are treated. Landscaping, removing town buildings and breaking main connections to other towns can lower it, while celebrations and marketing campaigns can improve it. Reputation lost by removing trees can be recovered by planting new ones." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Te same przyczyny oraz usunięte skały, tunele, teren torów i dróg i nieuzyskane subsydia. Każde przerwane lub za długie połączenie główne kosztuje od razu 1/3; trzy zatrzymują miasto. Odzysk wynosi sam z siebie około 67 % na rok i około 200 % z kampanią reklamową, dwa razy tyle, ile pokazuje okno miasta (33 % i 100 %); kampania od razu nic nie daje. Sadzenie drzew znosi tylko stratę za drzewa. Premia Odzyskiwanie reputacji centrali nie działa w skryptach.
result: differs
```
