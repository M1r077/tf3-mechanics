---
title: Ranga firmy, zalety i centrala
summary: Co podnosi rangę firmy, co odblokowuje każda ranga, jak działają pozwolenia i poszukiwania, co naprawdę daje centrala i ile kosztuje cię wyższa ranga.
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40425
fact: 15 | rang firmy, od Stażysty do Magnata
fact: ×12,5 | populacji świata potrzeba do rangi 15, w porównaniu ze startem
fact: ×0,75 | dochodu na randze 15 przy Inflacji Normalnej
fact: 0 | rang traconych, gdy populacja spada
---

Ranga firmy nie zależy od pieniędzy ani dostaw: zależy od **populacji całej mapy**. Każda nowa ranga odblokowuje zalety (zabytki, poszukiwania, kampanie reklamowe, Zazielenianie przemysłu, moduły centrali), a przy ustawieniu **Inflacja** obniża też trochę wszystkie twoje dochody.

## Co podnosi rangę

- Gra zapamiętuje **populację świata na starcie** gry: mieszkańców wszystkich miast (`company.script.tl:392-396`, `company_util.tl:365-371`).
- Potem porównuje **najwyższą** kiedykolwiek osiągniętą populację świata z tą wartością startową (`company_growth.script.tl:25-27`). Wartość tylko rośnie: kurczące się miasta nigdy nie odbierają ci rangi.
- Rangę 1 osiąga się przy wartości startowej, rangę 15 przy około **12,5-krotności** tej wartości (`company_progression_util.tl:6-14`, `company_progression_util.tl:95-120`, `town_growth_function.tl:13-20`).
- W misjach kampanii i w edytorze map nie ma rangi (`company_growth.script.tl:74-79`).

| Ranga | Rola | Populacja świata w porównaniu ze startem |
|---|---|---|
| 1 | Stażysta | ×1 |
| 2 | Mechanik | ×1,02 |
| 3 | Inżynier | ×1,08 |
| 4 | Koordynator | ×1,2 |
| 5 | Ekspert | ×1,4 |
| 6 | Kierownik | ×1,7 |
| 7 | Nadzorca | ×2,1 |
| 8 | Zarządca | ×2,6 |
| 9 | Wicedyrektor | ×3,3 |
| 10 | Dyrektor | ×4,2 |
| 11 | Dyrektor naczelny | ×5,3 |
| 12 | Zastępca wiceprezesa | ×6,7 |
| 13 | Wiceprezes | ×8,3 |
| 14 | Prezes | ×10,2 |
| 15 | Magnat | ×12,5 |

Proporcje obliczono ze skryptów dla populacji startowej 50 000 lub więcej (`company_progression_util.tl:6-14`, `company_static_util.tl:6-24`). Na małej mapie są nieco wyższe dla środkowych rang (ranga 8 wymaga ×2,85 przy 5 000 mieszkańców); rangi 1 i 15 zostają na ×1 i ×12,5.

- Ranga podąża więc za **wzrostem miast**: miasta rosną dzięki twoim pasażerom i ładunkom, zob. [Wzrost miast](towns.html).
- Pierwsze rangi przychodzą szybko, ostatnie wymagają, by miasta na mapie były wielokrotnie większe.

## Nowa ranga jest stosowana w oknie firmy

Gdy populacja przekroczy próg, pojawia się **powiadomienie o awansie**; kliknięcie otwiera okno firmy na tej randze (`company_growth.script.tl:96-107`, `company_notification_rank_up.script.tl:8-9`).

- Nowe zalety odblokowują się dopiero, gdy ta ranga zostanie **wybrana w oknie firmy**: okno wysyła wtedy odblokowanie (`company.tl:420-423`, `company_growth.script.tl:55-62`). Menu budowy sprawdzają tę zastosowaną rangę (`company_util.tl:92`, `company_util.tl:171-178`).
- Mnożnik dochodu z następnej sekcji podąża za rangą **osiągniętą**, zastosowaną lub nie (`company_growth.script.tl:47-48`).

```tip scripts
Po awansie kliknij powiadomienie (albo otwórz okno firmy i wybierz nową rangę), aby dostać zalety. Czekanie nic nie daje: dochód jest już obniżony.
```

## Ile kosztuje wyższa ranga: ustawienie Inflacja

Przy **Inflacji** wszystkie dochody z ładunków i pasażerów spadają równomiernie od ×1 na randze 1 do minimum na randze 15 (`company_progression_util.tl:25-40`, `company_growth.script.tl:159-170`).

| Inflacja | Dochód na randze 15 | Źródło |
|---|---|---|
| Brak | ×1 (bez zmian) | `difficulty_util.tl:50`, `mod.script.tl:694-697` |
| Niska | ×0,9 | |
| Normalna | ×0,75 | |
| Wysoka | ×0,6 | |
| Bardzo wysoka | ×0,5 | |

- Przy Normalnej każda ranga kosztuje około 1,8 % dochodu: ×0,96 na randze 3, ×0,875 na randze 8, ×0,75 na randze 15.
- Inflacja nie podnosi żadnych kosztów; koszty podążają za rokiem kalendarzowym (zob. [Koszty, utrzymanie i pożyczki](costs.html)).
- Wyższa ranga sprawia też, że nowe oferty subsydiów są rzadsze (zob. [Subsydia](subsidies.html)).

## Pozwolenia

Większość zalet jest ograniczona **pozwoleniami**. Ranga daje pozwolenia na zaletę; każdy budynek lub użycie zabiera jedno (`company_util.tl:33-80`, `company_util.tl:206`).

- Pozwolenia **sumują się** przez rangi: zaleta, która daje 1 na randze 3 i 1 na randze 5, pozwala na 2 od rangi 5 (`company_util.tl:51-56`).
- Budynek oddaje pozwolenie po wyburzeniu: gra liczy to, co stoi (`company_util.tl:143-163`, `company_util.tl:203-206`).
- Poszukiwania, kampanie reklamowe i zazielenianie zużywają pozwolenie przy starcie (`company.script.tl:416-423`, `company.script.tl:459-462`, `company.script.tl:496-500`). Menu budowy pokazuje wtedy **Już użyto** lub **Regeneracja** (`company_util.tl:207-226`).
- Pozwolenie na **Marketing** wraca **5 lat** po każdej kampanii (`marketing.res.lua:6-7`, `company.script.tl:66-94`).

| Zaleta | Pozwolenia | Źródło |
|---|---|---|
| Centrala | 1 na randze 1 | `hq.res.lua:6` |
| Kampania reklamowa | 1 na randze 4, wraca po 5 latach | `marketing.res.lua:6-7` |
| Zazielenianie przemysłu | 1 na randze 3, 6, 9, 12 i 15 | `industry_greenify_tool.script.tl:101-102` |
| Oczyszczalnia | 15 na randze 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Zabytki | po jednym: Amfiteatr 2, Wielka Latarnia 5, Zamek Białej Czapli 7, Muzeum Morskie 9, Zamek Neuschwanstein 10, Statua Wolności 11, Pałac Letni 13, Opera Miejska 14, Gmach Parlamentu 15 | `arena.con.lua:39`, `lighthouse.con.lua:48`, `white_heron_castle.con.lua:47`, `ship_museum.con.lua:55`, `neuschwanstein.con.lua:55`, `statue_of_liberty.con.lua:57`, `summer_palace.con.lua:63`, `opera_house.con.lua:63`, `westminster.con.lua:79` |

Co robi każda zaleta: [Reputacja](reputation.html) (Kampania reklamowa), [Zanieczyszczenie i hałas](emission.html) (Zazielenianie, Oczyszczalnia).

## Poszukiwania

Poszukiwanie szuka surowca w pobliżu miasta i, jeśli się uda, zakłada tam nowy zakład przemysłowy.

| Surowiec | Ranga | Źródło |
|---|---|---|
| Ryby | 2 | `exploration_fish.res.lua:9-11` |
| Glina | 3 | `exploration_clay.res.lua:9-11` |
| Ropa surowa | 4 | `exploration_crude_oil.res.lua:9-11` |
| Zboża, warzywa | 4, **jedno wspólne pozwolenie** (Przemysł) | `exploration_grain.res.lua:9`, `exploration_vegetables.res.lua:9`, `permit_key_farm.res.lua:6` |
| Drewno | 5 | `exploration_logs.res.lua:9-11` |
| Węgiel, ruda żelaza | 6 | `exploration_coal.res.lua:9-11`, `exploration_iron_ore.res.lua:9-11` |
| Kamień, wełna | 8 | `exploration_stone.res.lua:9-11`, `exploration_wool.res.lua:9-11` |
| Piasek | 9 | `exploration_sand.res.lua:9-11` |
| Guma | 12 | `exploration_rubber.res.lua:9-11` |

- Każdy surowiec ma **jedno** pozwolenie, zużywane przy starcie poszukiwania (`company.script.tl:451-462`).
- Trwa do **6 miesięcy**. Raz w miesiącu próbuje umieścić zakład, z szansą rosnącą od 20 % do 60 % w ciągu 6 miesięcy (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`).
- Próba nie udaje się też, gdy gra nie znajdzie miejsca na ten zakład w pobliżu miasta (`company.script.tl:199-210`).
- Jeśli ostatnia próba się nie uda, **pozwolenie wraca**, a powiadomienie o tym informuje (`company.script.tl:106-126`, `company.script.tl:170-181`).
- Na raz może trwać tylko jedno poszukiwanie na miasto i surowiec (`company.script.tl:442-447`).

```engine
Gdzie może stanąć nowy zakład (makeIndustrySpawnProposal w pobliżu miasta), decyduje silnik: poszukiwanie ryb daleko od wody albo miasto bez wolnego terenu wokół po prostu się nie udaje i oddaje pozwolenie.
```

## Centrala

| Co | Wartość | Źródło |
|---|---|---|
| Cena i utrzymanie | za darmo, bez utrzymania | `headquarter.script.tl:526-527` |
| Pozwolenie | 1, na randze 1 | `headquarter.con.lua:6-7`, `hq.res.lua:6` |
| Wzrost miasta | +5 % dla najbliższego miasta | `headquarter.script.tl:510-515`, `landmark_util.tl:51-70` |
| Miejsca pracy | 24 | `headquarter.con.lua:16`, `headquarter.script.tl:505-508` |

- +5 % to premia do tempa wzrostu tego miasta, więc nic nie daje, gdy tempo miasta wynosi 0 % (zob. [Wzrost miast](towns.html)).
- **Moduły** kosztują po 50 000 i są ograniczone pozwoleniami, których przybywa z rangą (`hq_module_m.module.lua:83`, `hq_module_m.module.lua:137`).
- Tylko dwa moduły mają premię w plikach: **Średni budynek** +1 % wzrostu miasta (`hq_module_m.module.lua:139-142`) i **Duży budynek** +1 % Odzyskiwanie reputacji (`hq_module_l.module.lua:169-172`). Premii do odzysku nie czyta żadna ocena miasta (zob. [Reputacja](reputation.html)). Pozostałe moduły są dekoracyjne.
- Każdy plik modułu zaczyna się też tabelą dającą +5 % wzrostu miasta, ale nic w pliku jej nie używa (`hq_corner_l.module.lua:148-159`, `hq_statue.module.lua:46-57`). Sumowana jest tylko premia w `metadata` modułu (`headquarter_addon.script.tl:18-29`).

| Moduł | Pozwolenia zyskiwane na randze (×2 = dwa) | Razem na randze 15 |
|---|---|---|
| Flaga na maszcie | 1 ×2, 6, 7, 8, 9, 11, 12, 13, 14 | 10 |
| Skrzydło narożne | 3, 5, 7 ×2, 9, 11, 13, 15 | 8 |
| Średni budynek | 2, 4, 10 ×2, 15 ×2 | 6 |
| Duży budynek | 5, 6, 10, 12 | 4 |
| Balkon | 8 ×2, 14 ×2 | 4 |
| Duża fontanna | 10 ×2, 14 ×2 | 4 |
| Kopuła | 6, 15 ×2 | 3 |
| Flaga dachowa | 7, 10, 13 | 3 |
| Kort tenisowy | 11, 12, 14 | 3 |
| Stare drzewo | 13, 15 ×2 | 3 |
| Posąg | 14 ×2 | 2 |
| Sadzawka | 15 | 1 |

Źródła: wiersz `rankAndPermits` każdego pliku modułu (`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`).

```tip scripts
Postaw centralę w mieście, które ma rosnąć najszybciej, i dodaj tam średnie budynki: to jedyne moduły z premią do wzrostu.
```

## Warto wiedzieć

- Aby awansować, rozwijaj miasta: więcej pasażerów i ładunków do większej liczby miast, przy dobrych ocenach. Pieniądze w banku się nie liczą.
- Planuj zabytki i poszukiwania: każde przychodzi raz, na stałej randze.
- Na mapie z Inflacją awans jest dobry dla zalet i zły dla dochodu. Przy Normalnej cała droga do rangi 15 kosztuje ćwierć wszystkich dochodów.

```check
official: "The company rank depends on the population of the map. … Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Ta sama zasada: najwyższa osiągnięta populacja świata w porównaniu z populacją na starcie, ×12,5 dla rangi 15; nigdy nietracona. Nową rangę trzeba wybrać w oknie firmy, by odblokować jej zalety, a Inflacja obniża dochód od razu. Tylko dwa moduły mają premię (Średni budynek +1 % wzrostu, Duży budynek +1 % Odzyskiwanie reputacji, której nie czyta żadna ocena); pozostałe są dekoracyjne.
result: refines
```
