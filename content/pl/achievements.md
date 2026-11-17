---
title: Osiągnięcia
summary: Co skrypt gry sprawdza dla każdego osiągnięcia w Wolnej grze i kiedy, które liczą tylko pojazdy, ładunki i zwierzęta z gry podstawowej, a które sprawdzenia zostawia silnikowi.
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-17
game: 40425
fact: 17 | osiągnięć odblokowywanych przez sam skrypt gry
fact: 500 m | wysokość pierwszego wagonu pociągu na przystanku dla Transport górski
fact: < 1 % | reputacja miasta dla To nie ja
fact: 10 | zabytków, które muszą mieć to samo najbliższe miasto dla Centralizacja
---

Oficjalna wiki wymienia 41 osiągnięć. Skrypt gry `achievements.script.tl` sam odblokowuje **17** z nich i zasila **9 liczników między grami**; pozostałe (kampania, pogoda, wielkość miasta, magazyn, odsetki, boostery, samochody, 1900-2000, para w latach 2000.) są sprawdzane gdzie indziej, przez silnik lub platformę. Każde sprawdzenie najpierw pyta silnik, czy osiągnięcie da się jeszcze odblokować; o tym, czy blokują je mody lub ustawienia, decyduje silnik (`achievements.script.tl:632`, `achievements.script.tl:510`).

## Osiągnięcia sprawdzane przez skrypt

| Osiągnięcie | Co sprawdza skrypt | Źródło |
|---|---|---|
| **Paczka przyszła** | jedna sztuka ładunku dociera do celu | `achievements.script.tl:221-225`, `achievements.script.tl:632-636` |
| **Zapomoga** | jedno subsydium zrealizowane | `achievements.script.tl:241-244`, `achievements.script.tl:638-642` |
| **Seria subsydiów** | 10 subsydiów zrealizowanych bez nieudanego pomiędzy; nieudane subsydium zeruje licznik | `achievements.script.tl:243-249`, `achievements.script.tl:644-648` |
| **Opieka** | ocena dostaw miasta zmienia się na **Znakomite** | `achievements.script.tl:270-276`, `towns.script.tl:30-33`, `achievements.script.tl:650-654` |
| **Budujemy nowy dom** | miasto awansuje o poziom | `achievements.script.tl:253-255`, `town_growth.script.tl:92` |
| **Więcej, więcej!** | miasto zgłasza zapotrzebowanie na nowy typ ładunku | `achievements.script.tl:257-259`, `achievements.script.tl:668-672` |
| **To nie ja** | Reputacja miasta **spada** poniżej **1 %** | `achievements.script.tl:261-267`, `towns.script.tl:36-39` |
| **Awans** | firma zdobywa rangę | `achievements.script.tl:280-282`, `achievements.script.tl:680-684` |
| **Szczeble kariery** | firma osiąga najwyższą rangę | `achievements.script.tl:284-290`, `achievements.script.tl:686-690` |
| **Ogrodnictwo** | stawiasz drzewa, i tylko drzewa, w jednej budowie (nic nie usunięto, nie przez zalesianie) | `achievements.script.tl:346-377` |
| **Perfekcjonizm** | ta sama stacja zostaje wyburzona, odbudowana, wyburzona i odbudowana, w tej kolejności, bez budowy lub usunięcia innej stacji pomiędzy | `achievements.script.tl:304-341`, `achievements.script.tl:694-710` |
| **Centralizacja** | dokładnie 10 ukończonych zabytków ma to samo najbliższe miasto | `achievements.script.tl:382-395`, `achievements.script.tl:713-721` |
| **Transport górski** | jeden z twoich pociągów przyjeżdża na przystanek z pierwszym wagonem wyżej niż **500 m** | `achievements.script.tl:407-417`, `achievements.script.tl:723-727` |
| **Transport morski** | jeden z twoich helikopterów przylatuje na przystanek platformy wiertniczej | `achievements.script.tl:420-450`, `achievements.script.tl:729-733` |
| **Historyczna flota** | każdy model statku z gry podstawowej pływa jednocześnie na jednej z twoich linii wodnych | `achievements.script.tl:735-776` |
| **Bliskie spotkanie 3. stopnia** | klikasz UFO | `achievements.script.tl:793-806` |
| **Zegarmistrzostwo** | ręcznie zmieniasz porę dnia | `achievements.script.tl:839-844` |

- **Perfekcjonizm** liczy tylko budowę, która dodaje lub usuwa całą stację: dodanie peronu lub modułu do stacji się nie liczy (`achievements.script.tl:301-302`).
- **Centralizacja** liczy każdy zabytek w chwili ukończenia, dla miasta, które jest wtedy najbliżej (`achievements.script.tl:386`).
- **Historyczna flota** jest sprawdzana tylko wtedy, gdy na przystanek przypływa model statku, który jeszcze nigdy się nie zatrzymał; patrzy na pojazdy twoich linii wodnych, nie na statki w zajezdni (`achievements.script.tl:736`, `achievements.script.tl:750-766`).
- **To nie ja** wymaga Reputacji, nie innej oceny: zobacz [Reputacja miast](reputation.html).

```tip scripts
Transport górski sprawdza wysokość pierwszego wagonu, gdy pociąg się zatrzymuje, a nie wysokość budynku stacji. Zbuduj stację na górze powyżej 500 m i puść tam jeden pociąg.
```

## Liczniki między grami

Te liczniki przechodzą z gry do gry (przechowuje je platforma). Skrypt wysyła tylko to, co zmieniło się od ostatniego sprawdzenia.

| Licznik | Osiągnięcie | Co się liczy | Źródło |
|---|---|---|---|
| Długość tras | **Dookoła świata** | przyrost całkowitej długości w dzienniku (w km); nic nie jest odejmowane przy usuwaniu | `achievements.script.tl:511-523` |
| Populacja | **Populacja globalna** | przyrost populacji mapy, od populacji w chwili wczytania gry | `achievements.script.tl:512`, `achievements.script.tl:525-533` |
| Pasażerowie | **Przewóz pasażerów** | pasażerowie, którzy ukończyli podróż na jednej z twoich linii | `achievements.script.tl:236-238`, `achievements.script.tl:535-541` |
| Ładunek | **Najlepszy sport to transport** | dostarczone sztuki ładunku | `achievements.script.tl:543-549` |
| Klimaty | **Magnateria** | klimat mapy, gdy firma osiąga na niej najwyższą rangę | `achievements.script.tl:551-567` |
| Dochód | **Kasa to zło** | twój zsumowany dochód, w miliardach | `achievements.script.tl:202-204`, `achievements.script.tl:569-590` |
| Typy ładunków | **Handel ponad wszystko** | każdy typ ładunku z gry podstawowej dostarczony raz | `achievements.script.tl:20-22`, `achievements.script.tl:230-232`, `achievements.script.tl:592-607` |
| Pojazdy | **Wszystkoizm** | każdy model pojazdu z gry podstawowej, który raz dotrze na przystanek | `achievements.script.tl:16-18`, `achievements.script.tl:469-481`, `achievements.script.tl:609-625` |
| Zwierzęta | **Miłość do zwierząt** | każde zwierzę z gry podstawowej, które raz klikniesz | `achievements.script.tl:24-26`, `achievements.script.tl:809-834` |

- Pojazdy, ładunki i zwierzęta z modów nigdy nie liczą się do tych liczników: brane są tylko pliki gry podstawowej (`::/vehicle`, `::/cargos`, `::/animal`) (`achievements.script.tl:16-26`).
- Dla Wszystkoizm pojazd musi **dotrzeć na przystanek** linii; samo kupno nie wystarczy.

```engine
To, czy osiągnięcie da się jeszcze odblokować (isAchievementUnlockable), czy liczniki są wyłączone (areStatsDisabled), cele każdego licznika i 24 osiągnięcia spoza skryptu obsługują silnik i platforma. Oficjalna wiki mówi, że osiągnięcia są zwykle niedostępne z modami niekosmetycznymi lub z ustawieniami rozgrywki odbiegającymi od standardowych.
```

## Warto wiedzieć

- Każde osiągnięcie „za pierwszym razem” jest porównywane z poprzednim sprawdzeniem: wymaga **nowego** zdarzenia w grze, w której osiągnięcie jest wciąż otwarte; stare subsydium lub ranga z zapisu nie liczą się ponownie (`achievements.script.tl:633`, `achievements.script.tl:779`).
- Twoja ranga, subsydia i Reputacja są opisane w [Ranga firmy, zalety i centrala](company.html), [Subsydia](subsidies.html) i [Reputacja miast](reputation.html).

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: W skrypcie jest 17 osiągnięć i 9 liczników. Uściśla on oficjalne opisy: Opieka oznacza ocenę dostaw na poziomie Znakomite, To nie ja Reputację poniżej 1 %, Transport górski pierwszy wagon powyżej 500 m, Perfekcjonizm wyburzenie-odbudowę-wyburzenie-odbudowę tej samej stacji, a Historyczna flota wszystkie modele statków z gry podstawowej jednocześnie na liniach. Do liczników liczą się tylko pojazdy, ładunki i zwierzęta z gry podstawowej.
result: refines
```
