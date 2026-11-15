---
title: Ustawienia odjazdu: ładowanie do pełna, Poziom napełnienia i czasy postoju
summary: Kiedy pojazd opuszcza przystanek: trzy tryby odjazdu, poziom napełnienia dla każdego towaru oraz minimalny, maksymalny i dodatkowy czas postoju.
domain: stations
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-15
fact: 600 s | domyślny Max. czas postoju nowego przystanku
fact: 30 s / 60 s | domyślne Maks. dodatkowe oczekiwanie, drogi / kolej
fact: 0–100 % | Poziom napełnienia, dla każdego towaru, jako część pojemności pojazdu
---

Każdy przystanek linii ma własne ustawienia odjazdu, w oknie „Filtr towarów” przystanku (kliknij przystanek w oknie linii). Decydują one, **ile** pojazd tam ładuje i **jak długo** może czekać.

## Ustawienia

| Ustawienie | Wartości | Nowy przystanek | Źródło |
|---|---|---|---|
| „Załaduj, jeśli dostępny”, „Do pełna (dowolny)”, „Do pełna (wszystkie)” | jedna z trzech | Załaduj, jeśli dostępny (zmierzone) | `cargofilter_window.tl:798-821` |
| „Min. czas postoju” | 0–600 s, krok 10 | 0 s (zmierzone) | `cargofilter_window.tl:841-845` |
| „Max. czas postoju” | 0–600 s lub „---” (bez limitu, suwak na końcu) | **600 s** (zmierzone) | `cargofilter_window.tl:855-863` |
| „Maks. dodatkowe oczekiwanie” | 0–600 s, krok 10 | 60 s; 30 s na stacji drogowej lub tramwajowej bez kolei | `cargofilter_window.tl:827-831`, `line_util.tl:478-490` |
| „Poziom napełnienia”, dla każdego ładowanego towaru | 0–100 %, krok 1 | 100 % | `cargofilter_window.tl:698-704`, `line_util.tl:511` |

- Kliknięcie czasu otwiera pole liczbowe: można w nim wpisać wartości powyżej 600 s (`cargofilter_window.tl:204-208`).
- Trzy czasy zachowują kolejność: podniesienie minimum lub dodatkowego oczekiwania powyżej maksimum podnosi też maksimum (`cargofilter_window.tl:834-835`, `cargofilter_window.tl:848-849`, `cargofilter_window.tl:865-869`).
- Zmiana któregokolwiek z nich oznacza linię jako własną: konfiguracja automatyczna nie rusza już jej list Ładunek (`cargofilter_window.tl:438`, zobacz [Szybkość załadunku i rozładunku](loading.html)). Sama konfiguracja automatyczna nigdy nie zmienia trybu ani czasów (`line_util.tl:495-513`).

## Poziom napełnienia: limit dla każdego towaru

Poziom napełnienia to największa ilość danego towaru, jaką pojazd zabiera na tym przystanku, jako część pojemności pojazdu, zaokrąglona do najbliższej jednostki (zmierzone w grze).

| Pojazd | Poziom napełnienia | Odjeżdża z |
|---|---|---|
| ciężarówka, 15 miejsc, kłody | 50 % | **8** (7,5 zaokrąglone w górę) |
| ciężarówka, 22 miejsca, tkanina | 70 % | za każdym razem **15** (15,4) |
| pociąg, 18 miejsc, szkło | 48 % | najwyżej **9** (8,64) |
| tramwaj, 28 miejsc, paliwo | 66 % | najwyżej **18** (18,48) |

- Towar już na pokładzie się liczy: tramwaj, który przyjechał z 14 paliwa, odjechał z 18, a nie z 14 + 18.
- Powyżej limitu nic nie jest z tego powodu ładowane **ani rozładowywane**: ciężarówka, która przyjechała z 22 nawozu (limit 11), odjechała z 22.
- **0 %** oznacza: nie ładuj tu tego towaru.
- W trybie ładowania do pełna limit liczy się jako pełny: ciężarówki z drewnem z poziomem napełnienia 50 % czekały około 270 s i odjechały z 8 z 15, a nie z 15.
- Nie ma procentu rozładunku. O rozładunku decydują lista Ładunek i „Wymuś rozładowanie wszystkich towarów po przybyciu” ([Szybkość załadunku i rozładunku](loading.html)).

## Ładowanie do pełna i czasy postoju

- **Załaduj, jeśli dostępny**: pojazd bierze to, co jest, i odjeżdża.
- **Do pełna (wszystkie)**: pojazd czeka, aż będzie pełny. Ciężarówki z drewnem czekały 460–566 s i odjechały z 15 z 15.
- **Do pełna (dowolny)**: pojazd odjeżdża, gdy jeden towar jest pełny. Pociąg na drewno i deski odjechał ze 143 i 144 kłodami po 369–380 s; dwa inne odjazdy po około 30 s z 57 i 118 kłodami nie są wyjaśnione.
- **Max. czas postoju** kończy oczekiwanie, nawet gdy nic nie załadowano. Pociąg z warzywami w trybie Do pełna (wszystkie) z maksimum 120 s albo zapełnił się (64 z 64) w około 25 s, albo odjechał po 116–120 s z 26 lub **0**. Z domyślnymi 600 s odjechał z 26 z 64 po 596–600 s.
- **Min. czas postoju** to cały postój, łącznie z załadunkiem, a nie dodatkowy czas po nim: przy 60 s pociągi ze szkłem stały za każdym razem 55–61 s, niezależnie od tego, co ładowały.
- **Maks. dodatkowe oczekiwanie**: „Maximum wait time after loading to improve vehicle distribution” (`cargofilter_window.tl:827`). Okno pojazdu pokazuje podczas oczekiwania „Utrzymuje bezpieczną odległość” (`entity_window_util.tl:2279-2286`).
- **Kilka pojazdów na jednym przystanku ładuje się jednocześnie**, niezależnie od tego, kiedy każdy przyjechał (widziane w grze). Dwie ciężarówki z drewnem, które przyjechały w odstępie około 90 s, odjechały w tej samej sekundzie, każda z 8. Jak towar jest między nie dzielony, nie zmierzono.

```engine
Skrypty tylko przechowują ustawienia; o tym, kiedy pojazd odjeżdża, decyduje silnik.
```

Powyższe reguły zmierzono z bazą danych [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) (migawki co 2 s, więc czasy postoju mają ±2 s), listopad 2026.

## Warto wiedzieć

- Długie oczekiwanie w trybie do pełna na przystanku, na który dociera mało towaru, blokuje peron: inne pojazdy linii stoją za nim w kolejce.
- Krótki Max. czas postoju w trybie do pełna może sprawić, że pojazdy odjadą puste, jeśli wrócą, zanim pojawi się nowy towar.
- Raz pociąg w trybie Do pełna (wszystkie) stał 783–992 s przy maksimum 600 s. Przyczyny nie znaleziono.

```check
official: "Full load (any): The vehicle will stop and wait until one cargo type is fully loaded. Full load (all): The vehicle will stop and wait until it is fully loaded." "In the vanilla game "all" and "any" only applies to trains and ships […] Any other vehicle type will wait for full load in both cases." Each cargo is loaded "to what percentage of a vehicle's total capacity". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles#departure_configuration))
scripts: Trzy tryby odjazdu, Min. / Max. czas postoju 0–600 s (lub bez limitu), Maks. dodatkowe oczekiwanie 0–600 s (60 s, 30 s drogi), Poziom napełnienia 0–100 % dla każdego towaru; zmierzone: Poziom napełnienia ogranicza towar na pokładzie, zaokrąglony do najbliższej jednostki, i liczy się jako pełny przy ładowaniu do pełna; Max. czas postoju kończy ładowanie do pełna, nawet puste; Min. czas postoju obejmuje załadunek; pojazdy na jednym przystanku ładują się razem.
result: refines
```
