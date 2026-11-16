---
title: Koszty, utrzymanie i kredyty
summary: Co zmieniają ustawienia kosztów, które koszty rosną z rokiem kalendarzowym, jak liczone są ceny pojazdów i ile naprawdę kosztuje kredyt.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
game: 40425
fact: ×6 | mnożnik roku dla utrzymania magazynów, portów i lotnisk do 2020
fact: 6 lat | kosztów bieżących: cena pojazdu
fact: raz | naliczane jest oprocentowanie kredytu od kwoty, a nie co roku
fact: 4 | kredyty naraz
---

Ustawienie **Inflacja** nie podnosi żadnych kosztów: obniża tylko twój przychód, gdy rośnie ranga firmy (patrz [Przychód z towarów](income.html)). Koszty rosną za to z **rokiem kalendarzowym**, a cztery suwaki skalują je od początku gry.

```diagram cost_years
```

## Ustawienia kosztów

| Ustawienie | Wartości | Gotowe poziomy „Niski” · „Normalny” · „Wysoki” · „Bardzo wysoki” | Źródło |
|---|---|---|---|
| **Koszty pojazdów**, **Konserwacja pojazdów** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:39`, `difficulty_util.tl:98-99`, `difficulty_util.tl:125-126` |
| **Koszty infrastruktury**, **Utrzymanie infrastruktury** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:100-101`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Wpływ konserwacji pojazdów** | „Brak” ×0 · „Niski” ×0,5 · „Średni” ×1 · „Wysoki” ×1,5 · „Bardzo wysoki” ×2 | „Niski” · „Średni” · „Wysoki” · „Bardzo wysoki” | `difficulty_util.tl:42`, `difficulty_util.tl:103`, `difficulty_util.tl:185` |
| **Inflacja** | tylko przychód, patrz [Przychód z towarów](income.html) | „Niska” · „Normalna” · „Wysoka” · „Bardzo wysoka” | `difficulty_util.tl:50`, `mod.script.tl:694-697` |

- **Koszty infrastruktury** skalują cenę ulic, torów, mostów, tuneli, przejazdów, budynków i modułów, a także prac terenowych (`post_run_util.tl:23-52`, `post_run_util.tl:83-120`, `construction.script.tl:31-35`, `mod.script.tl:223-226`). Skalują też koszt rozbiórki budynków (`construction.script.tl:39-44`). **Utrzymanie infrastruktury** skaluje ich utrzymanie (`post_run_util.tl:43-45`, `post_run_util.tl:105-112`, `entity_window_util.tl:186`).
- **Koszty pojazdów** i **Konserwacja pojazdów** skalują cenę zakupu i koszty bieżące każdego pojazdu (`post_run_util.tl:54-81`).
- **Wpływ konserwacji pojazdów** ustala, jak mocno pojazd w złym stanie traci prędkość, moc i komfort oraz zyskuje hałas, zanieczyszczenie i koszty bieżące (`mod.script.tl:241-245`).

## Co rośnie z rokiem kalendarzowym

- **Utrzymanie budynków**: ×1 w 1900, ×1,5 w 1920, ×2,2 w 1940, ×3,2 w 1960, ×4 w 1980, ×5 w 2000, ×6 w 2020 (`mod.script.tl:92-100`). Okno budynku i menu budowy stosują go do każdego budynku oznaczonego jako zależny od roku, a menu budowy oznacza te: magazyny, lądowiska, lotniska i porty (`entity_window_util.tl:186-193`, `construction_react_util.tl:1149`, `warehouse.tl:7`, `harbor_modular.tl:24`).
- **Moduły** dodane do takiego budynku kosztują według roku budowy budynku, a ich utrzymanie według bieżącego roku (`construction.tl:3720-3727`, `construction.tl:4364-4367`).
- **Warianty epok**: zajezdnie, stacje konserwacji, magazyny, dworce, porty i lotniska mają jeden wariant na epokę, a każdy późniejszy kosztuje **×3** (epoka B) lub **×9** (epoka C) pierwszego (`rail_depot.con.lua:7`, `warehouse.tl:48`, `modular_station.con.lua:71`, `harbor_modular.tl:76`, `airport.tl:8`).
- **Pieniądze z subsydiów**: od ×1 w 1900 do ×4 od 2000 (`finances_util.tl:87-90`). **Kwoty kredytów**: od ×0,4 w 1900 do ×2,4 w 2020 (`loan_util.tl:7-10`).
- **Przychód** nie ma żadnego mnożnika roku (`cargo_income.script.lua:10-13`).

```engine
O tym, jakie utrzymanie jest naprawdę pobierane i czy ulice, tory i pojazdy też podlegają tabeli lat, decyduje silnik (getCostMultiplierForYear; podstawowa konfiguracja ustawia tylko chargeMaintenanceInterval = 60, `mod.script.tl:105`). Skrypty liczą tylko wartości pokazywane w oknach i w menu budowy, według tabeli powyżej. Żaden skrypt nie ustawia flagi „zależny od roku” dla innych budynków.
```

## Tory, drogi i budynki

Pliki ulic i torów podają cenę i roczne utrzymanie na metr; menu budowy pokazuje je na kilometr (`construction_react_util.tl:2463`, `construction_react_util.tl:2477-2485`). W większości typów utrzymanie to **jedna szósta** ceny budowy:

| Typ | Dostępny od | Budowa za km | Utrzymanie za km i rok | Źródło |
|---|---|---|---|---|
| Prosty tor | start | 60 000 | 10 000 | `simple.street_template.lua:9`, `simple.street_template.lua:33` |
| Tor standardowy | 1930 | 180 000 | 30 000 | `standard.street_template.lua:11`, `standard.street_template.lua:35` |
| Tor dużych prędkości | 1980 | 540 000 | 90 000 | `high_speed.street_template.lua:11`, `high_speed.street_template.lua:35` |
| Mała stara droga wiejska | start | 60 000 | 10 000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:58` |
| Duża nowa ulica miejska | 1940 | 540 000 | 90 000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:91` |

- Sieć trakcyjna dodaje **30 %** ceny toru; buspas 10 %, tor tramwajowy 20 %, elektryczny tor tramwajowy 40 % ceny ulicy (`mod.script.tl:24-28`).
- Podniesienie terenu kosztuje 4,5 za m³, obniżenie 5,25 za m³, oba × Koszty infrastruktury; usunięcie pola 200 000 (`mod.script.tl:20-22`, `mod.script.tl:33`, `mod.script.tl:225-226`).
- Budynek bez własnego utrzymania płaci rocznie **jedną szóstą swojej ceny**, liczoną od ceny przed ustawieniem Koszty infrastruktury (`construction.script.tl:25-27`).
- Podstawowa konfiguracja ustawia współczynnik zwrotu przy wyburzeniu 0,75 i czas zwrotu 60 (`mod.script.tl:30-31`): wyburzenie tego, co właśnie zbudowałeś, oddaje większość pieniędzy. Stosuje to silnik.

Roczne utrzymanie zapisane w plikach, dla pierwszego wariantu (przed 1940) i późniejszych; magazyny dostają dodatkowo mnożnik roku opisany wyżej:

| Budynek | Pierwszy wariant | ×3 (od 1940) | ×9 (od 1980) | Źródło |
|---|---|---|---|---|
| Zajezdnia kolejowa, stocznia | 100 000 | 300 000 | 900 000 | `rail_depot.con.lua:34`, `water_depot.con.lua:32` |
| Zajezdnia drogowa | 30 000 | 90 000 | 270 000 | `road_depot.con.lua:32` |
| Zajezdnia tramwajowa | 20 000 | 60 000 | 180 000 | `tram_depot.con.lua:34` |
| Stacja konserwacji pociągów lub statków | 40 000 | 120 000 | 360 000 | `rail_maint_station.con.lua:32`, `water_maint_station.con.lua:32` |
| Stacja konserwacji pojazdów drogowych | 10 000 | 30 000 | 90 000 | `road_maint_station.con.lua:32` |
| Magazyn uniwersalny | 25 000 | 75 000 | 225 000 | `warehouse.tl:48-52`, `warehouse.tl:75` |
| Magazyn specjalistyczny | 50 000 | 150 000 | 450 000 | `warehouse.tl:51`, `warehouse.tl:75` |

Budowa każdego z tych budynków kosztuje **6 ×** jego utrzymanie (`rail_depot.con.lua:35`, `warehouse.tl:76`): 2,7 M za magazyn specjalistyczny ostatniej epoki, przed mnożnikiem roku.

- Pierwsze **lądowisko** (do 1950) używa już ×3 drugiej epoki: jego test czyta rok końcowy wariantu zamiast roku początkowego (`airfield.tl:8`, `airfield_era_a.metacon.tl:3`).

## Pojazdy

Żaden pojazd z podstawowej gry nie ma stałej ceny: gra liczy ją z prędkości i pojemności pojazdu przy wczytywaniu modelu (`model_metadata_util.lua:488-552`):

1. **Koszty bieżące na rok** = około 675 × średnia prędkość (m/s) × pojemność / 4 (`model_metadata_util.lua:499-518`). Liczba 675 pochodzi ze średniego przychodu na km, zmniejszonego, by zostawić miejsce na puste kursy powrotne, zakup i spadające ceny biletów (`model_metadata_util.lua:500-508`).
2. **Średnia prędkość** jest niższa od maksymalnej (v w km/h): pojazdy drogowe i tramwaje v^0,78 + 4, pociągi v^0,86 + 10, samoloty −0,0000203 × v² + 0,17 × v + 28,36 (v najwyżej 4000), statki 65 % prędkości maksymalnej (`model_metadata_util.lua:448-474`).
3. **Pociągi**: wagon liczy się jako połowa swojej pojemności; lokomotywa liczy też moc ÷ prędkość maksymalną (km/h) × 12,5 jako pojemność, również o połowę (`model_metadata_util.lua:511-512`, `model_metadata_util.lua:526-540`). Mocna, wolna lokomotywa jest droga.
4. **Cena** = **6 ×** roczne koszty bieżące (`model_metadata_util.lua:548-549`).

Przykład przy 100 %: autobus 35 km/h na 48 pasażerów kosztuje około 45 000 rocznie w eksploatacji i około 270 000 w zakupie.

- Stan pojazdu ma pięć poziomów (100–80 %, potem co 20 %) (`vehicle_store_util.tl:231-234`); przy **20 %** gra ostrzega, dopóki stan nie wróci powyżej 30 % (`notifications.script.tl:310-318`).

```engine
Jak szybko spada stan pojazdu, jak bardzo rosną przez to koszty bieżące i czy ceny pojazdów zmieniają się z rokiem, to wartości silnika (getMaintenanceRunningCostPenalty i inne kary); skrypty tylko skalują je ustawieniem Wpływ konserwacji pojazdów.
```

## Kredyty

```diagram loan_interest
```

| Rodzaj | Kwota około 1960 (×0,4 w 1900, ×2,4 w 2020) | Termin spłaty | Oprocentowanie | Źródło |
|---|---|---|---|---|
| Mały | 5–10 M | 1–5 lat | 3–5 % | `loan_util.tl:12-22` |
| Średni | 15–25 M | 3–8 lat | 5–8 % | `loan_util.tl:24-34` |
| Duży | 30–50 M | 5–12 lat | 8–10 % | `loan_util.tl:36-46` |
| Bardzo duży | 40–60 M | 10–24 lat | 10–12 % | `loan_util.tl:48-58` |

- Karta nazywa to **Roczne odsetki**, ale stopa jest naliczana **raz** od kwoty: łączne odsetki to kwota × stopa, niezależnie od terminu. Płacisz je w równych częściach co miesiąc razem z kapitałem (`loan_util.tl:102-111`, `loan_util.tl:126-136`, `loan.script.tl:83-99`). Długi kredyt jest więc tańszy na rok niż krótki z tą samą stopą.
- **Spłać** płaci tylko resztę kapitału: pozostałe odsetki przepadają (`loan.script.tl:171-190`). Przycisk wymaga tej kwoty w gotówce (`finances_loan_gui.tl:284-286`).
- Stopy **nie** zależą od poziomu trudności: każdy rodzaj ma własny stały zakres (`loan_util.tl:12-58`).
- Najwyżej **4 kredyty** naraz (`loan_util.tl:4`, `loan.script.tl:134`). Oferta jest zastępowana po pół roku; miejsce po wziętym kredycie zostaje puste na 4 do 8 miesięcy (`loan.script.tl:61-76`, `loan.script.tl:150`).
- Na początku gry każde z czterech miejsc dostaje wartości losowego rodzaju, więc pierwsza „mała” oferta może być dużym kredytem; gdy oferta się odnowi, każde miejsce oferuje własny rodzaj (`loan_util.tl:60-74`, `loan.script.tl:63-75`).

```tip scripts
**Bierz najdłuższą pożyczkę i spłacaj wcześnie.** Łączne odsetki są takie same przy każdym okresie, raty miesięczne są mniejsze, a Spłać kasuje pozostałe odsetki.
```

## Warto wiedzieć

- Bierz **najdłuższy** kredyt, jaki możesz: odsetki są w sumie takie same, rozłożone na więcej miesięcy, a możesz spłacić wcześniej bez płacenia reszty.
- Budynki z wariantami epok kosztują ×3 i ×9 w późniejszych epokach, a ich utrzymanie dalej rośnie z rokiem: magazyn specjalistyczny ostatniej epoki to duży stały koszt.
- Szybki pojazd o dużej pojemności kosztuje więcej w eksploatacji, ale też więcej przewozi: cena i koszty bieżące idą za prędkością × pojemnością, tak jak przychód, który może zarobić.

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Oprocentowanie kredytu zależy tylko od jego rodzaju (3–12 %), nie od poziomu trudności, i jest naliczane raz od kwoty, rozłożone na miesiące terminu; wcześniejsza spłata kasuje pozostałe odsetki. Inflacja zmienia tylko przychód; utrzymanie budynków idzie za rokiem (od ×1 do ×6); cena pojazdu = 6 × roczne koszty bieżące, oba z prędkości i pojemności.
result: differs
```
