---
title: Zanieczyszczenie i hałas
summary: Co emituje hałas i zanieczyszczenie, kiedy budynek emituje więcej, jak oceniają to miasta i co naprawdę robią Zazielenianie przemysłu i Oczyszczalnia.
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
game: 40425
fact: 65–80 dB | hałas w mieście: pełna ocena przy 65, zero przy 80
fact: 60–74 | zanieczyszczenie w mieście, w skali logarytmicznej skryptów (to nie poziom dźwięku): pełna ocena przy 60, zero przy 74
fact: −80 % | hałas i zanieczyszczenie zazielenionego zakładu
fact: 700 m | zasięg Oczyszczalni
---

Pojazdy, tory, ulice, stacje, zajezdnie, magazyny i zakłady przemysłowe emitują **hałas** i **zanieczyszczenie**. Dwie oceny miasta, **Hałas** i **Zanieczyszczenie**, porównują to, co dociera do miasta, ze stałymi limitami. Zła ocena obniża ocenę **Władz miejskich**, a więc i wzrost (zobacz [Miasta](towns.html)).

## Kiedy budynek emituje więcej

Skrypt gry co kilka aktualizacji ustawia emisję czterech rodzajów budynków, między poziomem spokojnym a ruchliwym (`emissions.script.tl:12-18`):

| Budynek | Emituje więcej, gdy | Źródło |
|---|---|---|
| **Zakład przemysłowy** | produkuje, i znowu z każdym wzmocnieniem (towar lub pracownicy); mniej, w stronę poziomu bezczynności, gdy jego zapas wyjściowy jest pełny | `emissions.script.tl:152-194` |
| **Stacja** | jest bardziej zajęta: czekający ludzie i towar względem jej pojemności | `emissions.script.tl:211-222` |
| **Zajezdnia**, **stacja serwisowa** | więcej pojazdów korzysta z jej serwisu | `emissions.script.tl:223-234` |
| **Magazyn** | jego zapasy są pełniejsze | `emissions.script.tl:237-250` |

- Każdy zakład ma własne cztery poziomy: bezczynność, produkcja, jedno wzmocnienie, dwa wzmocnienia (`industryutil.lua:464-475`; domyślne 0 / 78 / 84 / 88 dotyczy tylko zakładu bez własnych wartości). Większość emituje trochę nawet w bezczynności: kopalnia węgla przechodzi 2 → 10 → 20 → 30 zanieczyszczenia, jej pola 2 → 30 → 60 → 90 (`coal_mine.con.lua:99-135`, zobacz [Zakłady przemysłowe](industries.html)).
- Zakład, którego produkcji nikt nie odbiera, wraca do poziomu bezczynności: obsługa podnosi jego zanieczyszczenie.
- Pojazdy i tory też emitują; pojazd w złym stanie emituje więcej przy ustawieniu **Wpływ konserwacji pojazdów** (zobacz [Koszty, utrzymanie i pożyczki](costs.html)).

## Co pokazuje menu budowy

| Budynek | Hałas | Zanieczyszczenie | Źródło |
|---|---|---|---|
| Port | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| Lotnisko | 8–56 | 80–560 | `airport.tl:28-29` |
| Stacja kolejowa | 25 | 45–350 | `modular_station.con.lua:97-98` |
| Zajezdnia kolejowa | 50 | 100 | `rail_depot.con.lua:32-33` |
| Zajezdnia drogowa i tramwajowa | 40 | 80 | `road_depot.con.lua:30-31`, `tram_depot.con.lua:32-33` |
| Stacja metra | 40 | 80 | `underground_station.con.lua:75-76` |
| Stacja ciężarówek i autobusów | 1–10 | 12–76 | `modular_terminal.con.lua:67-68` |
| Stacje serwisowe | 20 | 40–50 | `road_maint_station.con.lua:30-31`, `rail_maint_station.con.lua:30-31` |
| Magazyn | 20 | 50 (uniwersalny) lub 100 (specjalistyczny) | `warehouses/warehouse.tl:51`, `warehouses/warehouse.tl:73-74` |

Dwie wartości to zakres pokazany w menu, od najniższej do najwyższej, jak zakres ceny obok (`construction_desc_react_util.tl:733-746`); jedna wartość to pojedyncza liczba. W działaniu każdy budynek emituje więcej, im bardziej jest zajęty (tabela wyżej). Trzymaj porty, lotniska i duże stacje towarowe z dala od domów.

## Jak ocenia to miasto

| Ocena | Mierzone | Pełna ocena | Zero | Źródło |
|---|---|---|---|---|
| **Hałas** | hałas przy budynkach miasta | 65 dB lub mniej | 80 dB | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Zanieczyszczenie** | średnie zanieczyszczenie na komórkę 16 m obszaru miasta (obszar liczony jako co najmniej 5 i najwyżej 10 km²), przeliczone na skalę logarytmiczną skryptów („dB”) | 60 lub mniej | 74 | `town_util.tl:413-431`, `emission_config.tl:23-30` |

- Od hałasu cierpi tylko dzielnica **mieszkalna**; budynki handlowe i przemysłowe nie (oficjalna wiki). Okno domu pokazuje hałas w jego miejscu (`town_building.tl:165-183`).
- Zanieczyszczenie jest uśredniane z całego obszaru, więc jedno źródło daleko od centrum waży mniej w dużym mieście niż w małym.
- Ustawienia **Wrażliwość na hałas** i **Wrażliwość na zanieczyszczenie** przesuwają limity: dwa razy większa wrażliwość liczy się jako +3 dB (`town_util.tl:426-428`, `town_util.tl:439-441`). Zanieczyszczenie używa tej samej skali logarytmicznej co hałas (10·log10): +3 „dB” oznacza dwa razy więcej zanieczyszczenia. To nie jest poziom dźwięku.

| Stopień | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Źródło |
|---|---|---|---|---|---|---|---|---|
| Hałas | Wył. (zawsze pełna) | ×¼ | ×½ | ×1 | ×1,4 | ×1,8 | ×3,5 | `difficulty_util.tl:48` |
| Zanieczyszczenie | Wył. (zawsze pełna) | ×¼ | ×½ | ×1 | ×1,7 | ×3 | ×5 | `difficulty_util.tl:49` |

Ustawienia wstępne Łatwy, Średni, Trudny i Bardzo trudny używają stopni 3, 4, 5 i 6 (`difficulty_util.tl:114-115`, `difficulty_util.tl:142-143`, `difficulty_util.tl:169-170`, `difficulty_util.tl:196-197`).

## Zazielenianie przemysłu

| | | Źródło |
|---|---|---|
| Efekt | hałas i zanieczyszczenie zakładu ×0,2 (−80 %), na stałe | `emission_config.tl:32`, `emissions.script.tl:184-192` |
| Użycia | jedno przy randze firmy 3, 6, 9, 12 i 15 | `industry_greenify_tool.script.tl:99-104` |
| Limit | raz na zakład; druga próba nie zużywa pozwolenia | `company.script.tl:489-494` |

- Efekt jest związany z tą wersją zakładu: gdy zakład zostanie przebudowany, przepada (`emissions.script.tl:187-190`).
- Najlepsze użycie: najbardziej ruchliwy zakład tuż obok miasta, bo wzmocniony zakład emituje najwięcej.

## Oczyszczalnia

Atut firmy, który usuwa zanieczyszczenie wokół siebie.

| | | Źródło |
|---|---|---|
| Cena | 100 000 000 | `pollution_cleanup_facility.script.lua:560` |
| Utrzymanie na rok | 10 000 000 | `pollution_cleanup_facility.script.lua:561` |
| Dostępna | 15 przy randze firmy 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Potrzebuje | **Maszyny**: 8 na cykl, dwa cykle na rok; 20 pracowników | `pollution_cleanup_facility.con.lua:43-60` |
| Zasięg | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| Stan | Zanieczyszczenie | Hałas | Źródło |
|---|---|---|---|
| bezczynna (brak maszyn) | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| pracuje | −10 000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| wzmocniona raz | −20 000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| wzmocniona dwa razy | −40 000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

- Bez maszyn prawie nic nie robi: trzeba ją zaopatrywać jak zakład przemysłowy.
- Jest głośna: buduj ją poza dzielnicą mieszkalną, w promieniu 700 m od zanieczyszczonego obszaru.
- Jej mnożnik wzmocnienia przez pracowników wynosi ×2 (`pollution_cleanup_facility.script.lua:549`). Zobacz [Pracownicy](workers.html).

## Warto wiedzieć

- Otwórz okno miasta albo warstwy hałasu i zanieczyszczenia, aby zobaczyć ocenę i gorące punkty.
- Pełny zapas wyjściowy obniża emisję zakładu w stronę poziomu bezczynności, ale kosztuje cię jego towar: lepiej przenieść miasto, niż głodzić zakład.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) i [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) pomagają znaleźć najbardziej zajęte stacje.

```engine
Silnik oblicza mapy hałasu i zanieczyszczenia, rozchodzenie się wartości, emisje pojazdów i torów oraz to, kiedy zakład zostaje przebudowany. Skrypt ustawia tylko poziom każdego budynku i limity miasta.
```

```check
official: "Noise reflects noise levels in residential areas." "Pollution reflects pollution levels across the town area." Dzielnica mieszkalna "is sensitive to noise"; dzielnica handlowa "is robust against the influence of noise". ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Ocena hałasu 65 → 80 dB, zanieczyszczenie 60 → 74 dB uśredniane z 5–10 km²; wrażliwość dodaje 10·log10 dB; zakłady, stacje, zajezdnie i magazyny emitują więcej, gdy są zajęte; pełny zapas wyjściowy obniża emisję zakładu w stronę poziomu bezczynności; zazielenianie −80 %, raz na zakład; Oczyszczalnia usuwa do 40 000 zanieczyszczenia w promieniu 700 m i potrzebuje maszyn.
result: refines
```
