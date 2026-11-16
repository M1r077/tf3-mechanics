---
title: Samoloty, lotniska i helikoptery
summary: Lotnisko polowe czy lotnisko, który samolot gdzie ląduje, terminale, drugi pas, heliporty oraz lista wszystkich statków powietrznych z ich ładunkiem, pojemnością i prędkością.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
game: 40425
fact: 2 | rozmiary samolotów: małe i duże
fact: 1950 | pierwsze lotnisko i pierwsze helikoptery
fact: 1980 | drugi pas
fact: 5 | statków powietrznych na hangar
---

Każdy samolot jest **mały** albo **duży**. **Lotnisko polowe** przyjmuje tylko małe samoloty; **lotnisko** przyjmuje oba, a helikoptery przy budynku głównym. Helikoptery mają też własne stacje.

```diagram air_access
```

## Lotnisko polowe i lotnisko

- **Lotnisko polowe**: "Lotnisko z jednym pasem startowym dla małych samolotów." Warianty od 1920, 1950 i 1980; 1, 2 lub 3 terminale i opcjonalna zajezdnia (`airfield.tl:49`, `airfield.tl:76`, `airfield_era_a.metacon.tl:3`).
- **Lotnisko**: "Lotnisko z maksymalnie dwoma pasami startowymi dla małych i wielkich samolotów." Warianty od 1950 i 1980; 2, 3 lub 4 terminale i kierunek lądowania (`airport.tl:24`, `airport.tl:80`, `airport1950.metacon.tl:3-4`).
- Terminale lotniska polowego przyjmują tylko małe samoloty; terminale lotniska przyjmują oba rozmiary (`af_terminal.module.lua:715`, `ap_terminal.module.lua:897`).
- Budynek główny lotniska ma lądowiska dla helikopterów (`ap_main.module.lua:532`), a od 1950 lotnisko może dostać terminal helikopterowy (`ap_terminal_heli.module.lua:897`, `ap_terminal_heli.module.lua:971`).
- **Drugi pas**: moduł lotniska od 1980 (`airport_2nd_runway.module.lua:5`). Niektóre moduły lotniska go wymagają i bez niego pokazują "Potrzebujesz drugiego pasa" (`airport.script.lua:261`).
- Wszystkie stacje lotnicze przyjmują pasażerów i każdy ładunek (`airfield.tl:59`, `airport.tl:34`).

| Budynek | Czekający pasażerowie | Źródło |
|---|---|---|
| Terminal lotniska polowego | do 250 | `af_terminal.module.lua:773` |
| Budynek główny lotniska | do 400 | `ap_main.module.lua:667` |
| Terminal lotniska | do 850 | `ap_terminal.module.lua:951` |
| Terminal helikopterowy lotniska | do 450 | `ap_terminal_heli.module.lua:990` |

## Hangary i stacje helikopterów

- **Hangar** lotniska polowego lub lotniska mieści 5 statków powietrznych i konserwuje je w promieniu 550 m (`af_hangar.module.lua:273-278`, `ap_hangar.module.lua:456-461`).
- **Heliport** (od 1950): kupuje i konserwuje helikoptery, zajezdnia na 5, promień konserwacji 800 m (`heliport.script.lua:301-306`).
- **Platforma helikopterowa** (od 1950): małe lądowisko dla pasażerów i ładunku, bez zajezdni (`helipad.con.lua:29-33`).

## Koszty

Cena i utrzymanie pierwszego wariantu, z mnożnikiem epoki. Mnożnik wynosi ×3 zarówno dla pierwszego lotniska polowego (1920, `airfield.tl:8`), jak i pierwszego lotniska (1950, `airport.tl:8`), a od 1980 ×9; moduły go nie mają ([Koszty, utrzymanie i kredyty](costs.html)).

| Budynek | Cena | Utrzymanie rocznie | Źródło |
|---|---|---|---|
| Lotnisko polowe | 3 600 000 - 9 000 000 | 150 000 - 600 000 | `airfield.tl:8`, `airfield.tl:55-56` |
| Lotnisko | 5 400 000 - 13 500 000 | 900 000 - 2 250 000 | `airport.tl:8`, `airport.tl:30-31` |
| Moduł lotniska polowego (budynek główny, terminal, hangar) | 600 000 | 100 000 | `af_main.module.lua:316-317`, `af_hangar.module.lua:326-327` |
| Moduł lotniska (budynek główny, terminal, hangar, drugi pas) | 900 000 | 150 000 | `ap_main.module.lua:672-673`, `ap_terminal.module.lua:949-950`, `ap_hangar.module.lua:508-509`, `airport_2nd_runway.module.lua:27-28` |

- Utrzymanie lotnisk i lotnisk polowych zależy też od roku kalendarzowego, od ×1 w 1900 do ×6 w 2020 ([Koszty, utrzymanie i kredyty](costs.html)).
- Cena i koszty bieżące statku powietrznego są liczone z jego prędkości i pojemności, jak w statkach i pojazdach drogowych ([Koszty, utrzymanie i kredyty](costs.html)).

## Wszystkie samoloty

Prędkość w km/h, zaokrąglona. "Każdy ładunek" oznacza każdy typ ładunku. Pojemność to suma pokazywana w sklepie pojazdów: wszystkie przedziały razem, każdy liczony według największej konfiguracji ładunku (`vehicle_store_util.tl:70-95`).

| Samolot | Lata | Rozmiar | Ładunek | Pojemność | Prędkość | Szybkość załadunku |
|---|---|---|---|---|---|---|
| Junkers F 13 Herta | 1920-1950 | mały | pasażerowie | 16 | 135 | - |
| Vickers J6860 Victoria | 1922-1960 | mały | każdy ładunek | 32 | 150 | 2,5 |
| Fokker F VII A | 1925-1960 | mały | pasażerowie | 32 | 175 | 2 |
| Junkers JU-52 „Żelazna Anka” | 1933-1982 | mały | pasażerowie, każdy ładunek | **48** (2 × 24) | 200 | 3 |
| Douglas DC-3 | 1935-1995 | mały | pasażerowie | 56 | 300 | 2,5 |
| Curtiss C-46 Commando | 1942-1980 | mały | każdy ładunek | 80 | 280 | - |
| Douglas DC-4 | 1944-1998 | mały | pasażerowie | 100 | 365 | 3 |
| Bristol Type 170 towarowy | 1949-2005 | mały | pasażerowie, każdy ładunek | **80** (2 × 40) | 350 | 1,5 |
| Lockheed L-1049 „Super Connie” | 1952-1986 | duży | pasażerowie | 120 | 486 | 3 |
| Lockheed L-1049D/H „Super Connie” | 1959-2000 | duży | każdy ładunek | **120** (2 × 60) | 486 | 2,5 |
| De Havilland DH.106 Comet | 1960-2000 | duży | pasażerowie | 160 | 724 | 3 |
| Canadair CL-44 towarowy | 1962-2005 | duży | każdy ładunek | **144** (3 × 48) | 645 | 2 |
| Convair CV 990 Coronado | 1962-2020 | duży | pasażerowie | 200 | 917 | 2 |
| Lockheed L-100 Hercules | 1976-2000 | mały | każdy ładunek | **132** (3 × 44) | 400 | 3 |
| McDonnell Douglas DC-10-30 | 1978- | duży | pasażerowie | 400 | 960 | 2,5 |
| McDonnell Douglas DC-10-30CF | 1978- | duży | każdy ładunek | **396** (3 × 132) | 960 | 4 |
| Airbus A310 300F towarowy | 1982- | duży | każdy ładunek | 160 | 850 | 3 |
| Short 330 Sherpa | 1984- | mały | pasażerowie, każdy ładunek | **80** (2 × 40) | 455 | 2,5 |
| Airbus A320 | 1985- | duży | pasażerowie | 180 | 753 | 3 |
| Br. Aerospace 146 | 1985- | mały | pasażerowie | 112 | 753 | 3 |
| Br. Aerospace 146 towarowy | 1985- | mały | każdy ładunek | **96** (2 × 48) | 753 | 2 |
| Fokker 100 | 1988- | duży | pasażerowie | 160 | 845 | 3,5 |
| Tupolew Tu-204 | 1995- | duży | pasażerowie | 280 | 850 | 4 |
| Tupolew Tu-204C towarowy | 1995- | duży | każdy ładunek | **204** (3 × 68) | 850 | 2 |
| Boeing 737-700 | 1998- | duży | pasażerowie | 200 | 974 | 2,5 |
| Boeing 737-700-C towarowy | 1998- | duży | każdy ładunek | **160** (2 × 80) | 974 | 3 |
| Bombardier DHC-8 | 2000- | mały | pasażerowie | 120 | 648 | 3 |
| Bombardier DHC-8 towarowy | 2008- | mały | każdy ładunek | 120 | 648 | 2 |
| Suchoj Superjet 100 | 2011- | mały | pasażerowie | 160 | 870 | 3 |
| Airbus Canada A220 | 2013- | duży | pasażerowie | 180 | 830 | 5 |

## Wszystkie helikoptery

| Helikopter | Lata | Ładunek | Pojemność | Prędkość | Szybkość załadunku |
|---|---|---|---|---|---|
| Bell 47 | 1950-1990 | pasażerowie, każdy ładunek | 8 | 150 | 2 |
| Piasecki H-21 Workhorse | 1952-1985 | pasażerowie, każdy ładunek | 80 (48 ładunek) | 210 | 3 |
| Sikorsky S-64 Skycrane | 1962-2017 | każdy ładunek | 40 | 213 | 4 |
| Bell 206 Long Ranger | 1965-2025 | pasażerowie | 32 | 241 | 2,5 |
| Boeing Vertol 234 Chinook | 1980- | pasażerowie, każdy ładunek | 80 | 269 | 2 |
| AgustaWestland AW101 Merlin | 1990- | pasażerowie | 60 | 278 | 3 |
| Mil Mi-26TC | 1993- | każdy ładunek | 120 | 295 | 4 |
| Eurocopter 120B Colibri | 1998- | pasażerowie | 48 | 210 | 3 |
| Kaman K-MAX | 2005- | każdy ładunek | 60 | 190 | 3 |
| Airbus H225 Super Puma | 2013- | pasażerowie | 48 | 288 | 3 |
| NextGen VTOL | 2030- | pasażerowie | 56 | 610 | 4 |

## Dobrze wiedzieć

- **Małe samoloty są przydatne do końca.** DHC-8, jego wersja towarowa i Suchoj Superjet 100 są małe, więc wystarczy im lotnisko polowe.
- **Przed 1952 nie ma dużego samolotu**, więc wczesne lotnisko nie daje jeszcze dostępu do większych maszyn.
- Samoloty lecą w linii prostej, a zapłata liczy tylko odległość w linii prostej, więc objazd nic ich dodatkowo nie kosztuje ([Przychód z towarów i czas dostawy](income.html)).
- Minimalną długość pasa, trasy lotu i lądowanie określa silnik gry; skrypty ich nie pokazują.

```check
official: "It can be used by small airplanes." (Airfield) "It can be used by small and large airplanes." (Airport), build menu descriptions.
scripts: To samo: terminale lotnisk polowych przyjmują tylko SMALL_AIRCRAFT, terminale lotnisk AIRCRAFT i SMALL_AIRCRAFT, helikoptery przy budynku głównym lotniska, heliport i platforma helikopterowa od 1950, drugi pas od 1980, hangary na 5; 15 małych i 15 dużych samolotów oraz 11 helikopterów w podstawowej grze.
result: agrees
```
