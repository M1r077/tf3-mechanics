---
title: Statki i porty
summary: Małe i duże statki, który port przyjmuje które, terminale i koszty portów oraz lista wszystkich statków z ich ładunkiem, pojemnością i prędkością.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
game: 40444
fact: 2 | rozmiary statków: małe i duże
fact: 1, 2, 4 | terminale na port
fact: 27 | statków w podstawowej grze
fact: ×9 | cena i utrzymanie wariantu portu z 1990
---

Każdy statek jest **mały** albo **duży**. Duży statek może przybić tylko do **dużego portu**; mały przybija do obu. Mówi to też przewodnik w grze: "Zwróć uwagę, że duże statki mogą przybijać tylko do dużych przystani."

```diagram ship_access
```

## Małe i duże porty

- Dwa porty w menu budowy: **Mały port pasażersko-towarowy** i **Duży port pasażersko-towarowy**. Oba przyjmują pasażerów i każdy ładunek (`harbor_modular.tl:92`, `harbor_modular.tl:122`).
- Mały port składa się z małych pomostów, które przyjmują tylko małe statki (`small_pier.module.lua:7`). Duży port używa średnich pomostów, które przyjmują oba rozmiary (`medium_pier.module.lua:6`, `harbor_modular.script.lua:35-39`).
- **Terminale**: 1, 2 lub 4, wybierane przy budowie (`harbor_modular.tl:16`, `harbor_modular.script.lua:33`).
- Terminal pomostu mieści 100 czekających pasażerów na małym pomoście i 50 na średnim (`modules.script.lua:872`, `modules.script.lua:1004`).
- Podczas stawiania portu skrypt tylko włącza warstwę żeglownej wody (`harbor_modular.tl:26-30`). Gdzie wolno postawić port, decyduje silnik gry.
- Każdy statek określa swój rozmiar w pliku pojazdu; gra zamienia go na tryb małego lub dużego statku (`model_metadata_util.lua:1411-1412`).

## Koszty

Jest jeden wariant portu na epokę: 1900, 1950 i 1990 (`harbor_modular.tl:71-73`). Cena i utrzymanie są mnożone przez 3 dla wariantu od 1940 i przez 9 dla wariantu od 1980 (`harbor_modular.tl:76`):

| Port | Cena (pierwszy wariant) | Utrzymanie rocznie (pierwszy wariant) | Źródło |
|---|---|---|---|
| Mały port | 144 000 - 444 000 | 24 000 - 74 000 | `harbor_modular.tl:88-89` |
| Duży port | 228 000 - 678 000 | 38 000 - 113 000 | `harbor_modular.tl:118-119` |

- Dwie wartości to najmniejszy i największy układ.
- Utrzymanie portów zależy też od roku kalendarzowego, od ×1 w 1900 do ×6 w 2020, jak w magazynach i na lotniskach ([Koszty, utrzymanie i kredyty](costs.html)).
- Porty są głośne i brudne: 180 do 280 dla obu ([Zanieczyszczenie i hałas](emission.html)).
- Cena i koszty bieżące statku są liczone z jego prędkości i pojemności, jak w pojazdach drogowych i samolotach ([Koszty, utrzymanie i kredyty](costs.html)).

## Wszystkie statki

Prędkość w km/h, zaokrąglona. "Ładunek" podaje klasy ładunku z pliku pojazdu; "każdy ładunek" oznacza każdy typ ładunku. Pojemność to suma pokazywana w sklepie pojazdów: wszystkie przedziały razem, każdy liczony według największej konfiguracji ładunku (`vehicle_store_util.tl:70-95`).

| Statek | Lata | Rozmiar | Ładunek | Pojemność | Prędkość | Szybkość załadunku |
|---|---|---|---|---|---|---|
| Dunara Castle | 1875-1930 | duży | pasażerowie, każdy ładunek | **160** (2 × 80) | 20 | 20 |
| Kanadyjski trawler | 1884-1948 | mały | każdy ładunek | 40 | 35 | 10 |
| Waimarie | 1889-1940 | mały | pasażerowie | 80 | 30 | 15 |
| Sydfart | 1900-1930 | mały | płynny, platforma, towary, sypki | 80 | 30 | 20 |
| PS Trillium | 1910-1955 | duży | pasażerowie | 200 | 35 | 15 |
| Sternwheeler | 1915-1960 | mały | pasażerowie, każdy ładunek | **120** (2 × 60) | 40 | 10 |
| Terra Nova | 1925-1975 | duży | sypki, platforma, towary | **200** (2 × 100) | 45 | 30 |
| Holownik tankowiec Votrans | 1935-1990 | mały | płynny | 120 | 33 | 20 |
| Holownik towarowy Votrans | 1935-1990 | mały | sypki, platforma, towary | 120 | 33 | 20 |
| MS Stadt Kiel | 1943-1990 | mały | pasażerowie | 80 | 30 | 20 |
| Borealis | 1948-1994 | mały | każdy ładunek | 60 | 38 | 20 |
| Wopper | 1950-2005 | mały | płynny, platforma, towary, sypki | 160 | 30 | 25 |
| Prom Meridian | 1956-2011 | mały | pasażerowie | 240 | 30 | 15 |
| Cap Arkona | 1965-2010 | duży | pasażerowie | 200 | 40 | 20 |
| Kabotażowiec Tora | 1970-2020 | duży | płynny, platforma, towary, sypki | 320 | 40 | 25 |
| Poduszkowiec AP1-88 | 1980- | mały | pasażerowie | 240 | 90 | 15 |
| Holownik Hercules XI | 1990- | duży | platforma, towary, sypki | **240** (2 × 120) | 32 | 20 |
| Baltica | 1994- | mały | każdy ładunek | 80 | 40 | 20 |
| HADAG Type 2000 | 1995- | mały | pasażerowie | 100 | 35 | 25 |
| Damen Tanker 800 | 1996- | mały | płynny | **320** (2 × 160) | 28 | 30 |
| Szybki prom Damen | 2003- | duży | pasażerowie | 220 | 75 | 20 |
| Luise Deymann | 2013- | duży | płynny | **480** (2 × 240) | 30 | 35 |
| MS Diamant | 2013- | duży | pasażerowie | 280 | 45 | 35 |
| Holownik Virgo | 2015- | duży | platforma, towary, sypki | **320** (2 × 160) | 40 | 15 |
| Poduszkowiec GHL Oita | 2023- | mały | pasażerowie | 320 | 100 | 20 |
| Yara Birkeland | 2030- | duży | platforma, towary, sypki | 480 | 42 | 10 |
| Prom Solarny | 2035- | mały | pasażerowie | 80 | 30 | 30 |

## Dobrze wiedzieć

- **Sprawdź rozmiar, zanim zbudujesz mały port.** Kilka największych statków towarowych (Tora, Virgo, Yara Birkeland) jest dużych i tam nie przybiją.
- **"Brak trasy dla dużych statków"** to osobne ostrzeżenie dla dużych statków: gra nie znalazła drogi wodnej, z której może skorzystać duży statek. O tym, która woda jest otwarta dla którego rozmiaru, decyduje silnik gry, a nie skrypty, które tylko pokazują ostrzeżenie (`vehicle_warning.script.tl:28-36`).
- **Punkty nawigacyjne statków** trzeba stawiać na wodzie ("Punkty nawigacyjne dla statków muszą znajdować się na wodzie.").
- Stocznia i stacja konserwacji statków to osobne budynki; konserwacja działa w promieniu wokół nich ([Pojazdy: stan, wiek i szybkość załadunku](vehicles.html)).

```check
official: "Passenger and cargo ships are available in two sizes: small and large. Large ships can only dock at large harbors, so make sure the harbor matches the size of the ships assigned to the line." (in-game guide "Water Infrastructure")
scripts: To samo: małe pomosty przyjmują tylko SMALL_SHIP, średnie SHIP i SMALL_SHIP; oba porty przyjmują pasażerów i każdy ładunek; 1, 2 lub 4 terminale; trzy warianty epok z ×1 / ×3 / ×9; 16 małych i 11 dużych statków w podstawowej grze.
result: refines
```
