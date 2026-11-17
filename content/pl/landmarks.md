---
title: Zabytki, obchody i elementy zabawy
summary: Ile ładunku kosztuje każdy zabytek, kiedy się odblokowuje i co daje pojazdom swojego miasta, jak skaluje go ustawienie Surowce budynków specjalnych oraz co naprawdę robią obchody, fajerwerki, sterowce i UFO.
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 9 | zabytków, po jednym na rangę firmy od 2 do 15
fact: +20 % / −20 % / +25 % | prędkość maksymalna, zanieczyszczenie lub komfort pojazdów jego miasta
fact: ×0 do ×4 | potrzebnego ładunku, z ustawieniem Surowce budynków specjalnych
fact: 2-4 lata | między dwoma UFO
---

Zabytek buduje się jak plac budowy: odblokowujesz go rangą firmy, stawiasz, a potem **dostarczasz do niego ładunek**. Gdy plac ma cały ładunek, zabytek jest ukończony i daje bonus pojazdom **swojego miasta**. Siedziba to osobny budynek z własnymi zasadami (zob. [Ranga firmy, korzyści i siedziba](company.html)).

## Zabytki

Ładunek przy **Surowce budynków specjalnych** ×1 (Wysoka).

| Zabytek | Ranga | Ładunek do dostarczenia | Bonus dla pojazdów jego miasta | Źródło |
|---|---|---|---|---|
| **Amfiteatr** | 2 | 800 kamienia | pojazdy drogowe: hałas **−25 %** | `arena.con.lua:10`, `arena.con.lua:20-26`, `arena.con.lua:39` |
| **Wielka Latarnia** | 5 | 1 200 kamienia, 200 paliwa | statki: prędkość maksymalna **+20 %** | `lighthouse.con.lua:10`, `lighthouse.con.lua:14`, `lighthouse.con.lua:29`, `lighthouse.con.lua:48` |
| **Zamek Białej Czapli** | 7 | 1 200 kamienia, 400 desek | pociągi: zanieczyszczenie **−20 %** | `white_heron_castle.con.lua:10`, `white_heron_castle.con.lua:14`, `white_heron_castle.con.lua:28`, `white_heron_castle.con.lua:47` |
| **Muzeum Morskie** | 9 | 600 drewna, 600 desek, 200 płócien | statki: komfort **+25 %** | `ship_museum.con.lua:10-18`, `ship_museum.con.lua:36`, `ship_museum.con.lua:55` |
| **Zamek Neuschwanstein** | 10 | 1 000 kamienia, 600 desek, 200 barwników | pojazdy drogowe: komfort **+25 %** | `neuschwanstein.con.lua:10-18`, `neuschwanstein.con.lua:36`, `neuschwanstein.con.lua:55` |
| **Statua Wolności** | 11 | 800 kamienia, 400 stali, 400 blachy | statki: zanieczyszczenie **−20 %** | `statue_of_liberty.con.lua:10-18`, `statue_of_liberty.con.lua:38`, `statue_of_liberty.con.lua:57` |
| **Pałac Letni** | 13 | 600 kamienia, 300 desek, 300 barwników, 300 mebli | samoloty: zanieczyszczenie **−20 %** | `summer_palace.con.lua:10-22`, `summer_palace.con.lua:44`, `summer_palace.con.lua:63` |
| **Opera Miejska** | 14 | 800 kamienia, 400 szkła, 400 blachy, 400 płócien | pociągi: komfort **+25 %** | `opera_house.con.lua:10-22`, `opera_house.con.lua:44`, `opera_house.con.lua:63` |
| **Gmach Parlamentu** | 15 | 800 kamienia, 400 desek, 400 szkła, 400 mebli | pojazdy drogowe, pociągi, statki i samoloty: prędkość maksymalna **+20 %** | `westminster.con.lua:10-22`, `westminster.con.lua:45`, `westminster.con.lua:79` |

- Każdy zabytek odblokowuje się raz, swoją rangą; jak rośnie ranga, opisuje [Ranga firmy, korzyści i siedziba](company.html).
- W swoich plikach zabytki nic nie kosztują przy budowie ani rocznie: tylko ładunek (`arena.con.lua:59-64`).
- Plac przechowuje naraz połowę każdego ładunku, więc potrzeba co najmniej dwóch dostaw każdego (`arena.con.lua:13-18`).

## Budowa zabytku

- Plac ma **4 etapy**. Przechodzi wyżej w miarę napływu ładunku: etap 2 przy jednej trzeciej całego ładunku, etap 3 przy dwóch trzecich, ukończenie przy 100 %. Każdy ładunek liczy się tylko do własnej ilości, więc nadmiar kamienia nie zastąpi brakujących desek (`landmarks.script.tl:34-46`).
- Bonus działa dopiero, gdy zabytek jest **ukończony** (`landmark_util_serialized.tl:393-395`). Wtedy pojawia się komunikat "Budowa ukończona" (`landmarks.script.tl:49-61`).
- Ustawienie **Surowce budynków specjalnych** mnoży cały ładunek: Brak ×0, Niska ×0,5, Wysoka ×1, Bardzo wysoka ×2 lub Bardzo wysoki ×4. Gotowe poziomy to "Niski" ×0,5, "Normalny" ×1, "Wysoki" ×2, "Bardzo wysoki" ×4. Przy ×0 zabytek jest ukończony od razu po postawieniu (`difficulty_util.tl:40`, `difficulty_util.tl:107`, `difficulty_util.tl:135`, `difficulty_util.tl:162`, `difficulty_util.tl:189`, `landmarks.script.tl:38`, `landmarks.script.tl:46`).

## Kto dostaje bonus

- Bonus trafia do miasta **najbliższego zabytkowi** i do pojazdów podanego rodzaju transportu, których najbliższym miastem jest to miasto (`landmark_util.tl:6-47`, `landmarks.script.tl:208-236`).
- Gdy pojazd wjeżdża na obszar innego miasta, przejmuje bonusy tego miasta i traci dawne (`landmarks.script.tl:279-299`).
- Bonusy kilku zabytków w tym samym mieście **sumują się**: dwa razy +20 % prędkości maksymalnej daje +40 % (`landmark_util.tl:46`, `vehicle_modifier.script.tl:3-16`).

```engine
Które miasto jest "najbliższym miastem" zabytku lub jadącego pojazdu, decyduje silnik (getConstructionClosestTown, closestTown). Jak silnik przekłada +25 % komfortu lub +20 % prędkości maksymalnej na podróże i dochód, to również praca silnika.
```

```tip scripts
Postaw Gmach Parlamentu w mieście, w którym jeździ najwięcej twoich pojazdów: +20 % prędkości maksymalnej dla każdego rodzaju transportu. Drugie +20 % daje Wielka Latarnia statkom w tym samym mieście. Osiągnięcie Centralizacja wymaga 10 ukończonych zabytków z tym samym najbliższym miastem, a pliki gry zawierają 9 zabytków oprócz siedziby (policzone); czy da się je zdobyć w tej wersji, nie wiadomo (zob. [Osiągnięcia](achievements.html)).
```

## Obchody

Obchody to małe przyjęcie widoczne nad miastem, gdy coś dzieje się po raz pierwszy. Podnoszą też **Reputację** miasta, ale tylko gdy Reputacja nie jest już pełna.

| Zdarzenie | Reputacja | Źródło |
|---|---|---|
| pierwszy pasażer wsiada w mieście do jednej z twoich linii | +50 % | `celebrations.script.tl:228-252` |
| pierwszy ładunek dostarczony do miasta | +50 % | `celebrations.script.tl:187-198` |
| miasto awansuje na wyższy poziom | +50 % | `celebrations.script.tl:260-272` |
| pierwszy ładunek dostarczony do zakładu | +20 % dla najbliższego miasta | `celebrations.script.tl:202-219` |

- Miasto awansujące na wyższy poziom dostaje też **fajerwerki**, chyba że są wyłączone (`town_growth.script.tl:108-112`).
- Jak działa Reputacja: [Reputacja](reputation.html).

## Elementy zabawy

- **Sterowiec** przelatuje nad miastem, gdy uruchomisz tam Kampanię reklamową (`fun_elements.script.tl:112-117`).
- **UFO** pojawia się co **2 do 4 lat** czasu gry, losowo, gdy nie ma żadnego na mapie (`fun_elements.script.tl:10`, `fun_elements.script.tl:79-91`). Kliknij je, by zdobyć osiągnięcie Bliskie spotkanie 3. stopnia.
- Żadne z nich nie zmienia ekonomii.

## Warto wiedzieć

- Wybierz miasto przed budową: bonus nie podąża za twoimi liniami, tylko za pojazdami w pobliżu tego miasta.
- Na poziomie "Bardzo wysoki" zabytek potrzebuje czterokrotnie więcej ładunku: Gmach Parlamentu wymaga wtedy 3 200 kamienia i po 1 600 każdego innego ładunku.

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: Dziewięć zabytków, po jednym na rangę od 2 do 15, każdy budowany z dostarczonego ładunku w 4 etapach, skalowanego przez Surowce budynków specjalnych od ×0 do ×4. Po ukończeniu każdy daje jeden bonus (+20 % prędkości maksymalnej, −20 % zanieczyszczenia, −25 % hałasu lub +25 % komfortu) pojazdom jednego rodzaju transportu w najbliższym mieście; bonusy się sumują. Obchody dodają 50 % lub 20 % Reputacji; UFO pojawia się co 2 do 4 lat.
result: adds
```
