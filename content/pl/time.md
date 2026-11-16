---
title: Czas gry i kalendarz
summary: Szybkość gry i szybkość kalendarza to dwie różne rzeczy. Ile trwa dzień i rok, co zmienia wolniejszy lub wstrzymany kalendarz, a czego nie zmienia.
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
game: 40425
fact: 4 s | jeden dzień kalendarza przy szybkości kalendarza ×1 i szybkości gry 1x
fact: ≈ 24 min | jeden rok kalendarza przy tych samych szybkościach
fact: 0 ×0,25 ×0,5 ×1 ×2 ×4 | stopnie szybkości kalendarza
fact: 0 1x 2x 4x | stopnie szybkości gry
---

Gra ma **dwa zegary**. **Szybkość gry** (pauza, 1x, 2x, 4x) przyspiesza wszystko: pojazdy, produkcję, miasta. **Szybkość kalendarza** ustala tylko, jak szybko zmienia się data. Prawie każda reguła gry liczy się w czasie gry, nie w dniach kalendarza.

## Dwa ustawienia

| Ustawienie | Stopnie | Co zmienia | Źródło |
|---|---|---|---|
| **Szybkość gry** | Pauza, 1x, 2x, 4x | jak szybko działa cała symulacja | `game_bar_widgets.tl:199-203` |
| **Szybkość kalendarza** | Wstrzymano, ×0.25, ×0.5, ×1, ×2, ×4 | ile sekund czasu gry trwa jeden dzień | `game_bar_widgets.tl:321-335`, `game_bar_widgets.tl:351` |

- Przy szybkości kalendarza ×1 dzień trwa **4 sekundy** czasu gry (oficjalna wiki), więc miesiąc to około 2 minut, a rok około **24 minut** przy 1x. Zmierzone za pomocą [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard): 4,0 s na dzień przy ×1, 1 s przy ×4, 8 s przy ×0.5, 16 s przy ×0.25.
- ×4 przyspiesza datę czterokrotnie; **Wstrzymano** zatrzymuje datę, a symulacja trwa dalej.
- 2x i 4x to maksimum: gra je obniża, gdy komputer nie nadąża (`game.tl:636-642`). Zmierzone: 2x dało średnio 1,9x, 4x dało 3,6x.
- **Godzina** i pogoda to trzeci, wizualny zegar: domyślnie zmieniają się same, niezależnie od kalendarza (`game_time_config.res.lua:5`, `weather_config.res.lua:5`).

## Co zależy od czasu gry, niezależnie od kalendarza

Te rzeczy liczą się w czasie gry, więc wolniejszy lub wstrzymany kalendarz ich nie spowalnia:

- **Produkcja**: czas produkcji zakładu to stała część standardowego roku (`industry_react_util.tl:51`). Okno zakładu pokazuje go w dniach bieżącego kalendarza (`industry_react_util.tl:23`): przy ×0.25 to samo tempo pokazuje ćwierć dni.
- **Raty kredytu**: jedna co standardowy miesiąc czasu gry, także przy wstrzymanym kalendarzu (`loan.script.tl:83-88`).
- **Terminy dotacji** i czas trwania premii, 5 standardowych lat (`subvention_util.tl:286`, `subvention_util.tl:290-292`).
- **Odbudowa reputacji miast** (`towns.script.tl:121-130`), **efekty pracowników**, liczone z najwyżej 2 standardowych lat (`industry_productivity_util.tl:3`), i **zamknięcie zakładu** po latach bez obsługi (`industries.script.tl:119-128`).
- **Oceny dostaw** miast, z ostatniego półrocza (`town_util.tl:840`).
- **Nowe zakłady**: przy wstrzymanym kalendarzu pojawiły się 3 w 1809 s czasu gry, co 760 s i 728 s, w tym samym rytmie co przy działającym kalendarzu (około 730 s). Zmierzone za pomocą [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard); zobacz [Zakłady](industries.html).

Gdy kalendarz działa, gra pokazuje te czasy w latach, miesiącach i dniach bieżącej szybkości kalendarza (`util.tl:40-49`).

## Co zależy od daty w kalendarzu

- **Nowe pojazdy, stacje i budynki** pojawiają się według roku (oficjalna wiki: "Different calendar speeds only affect the availability of vehicles and infrastructure").
- **Koszty rosnące z rokiem**: utrzymanie budynków, warianty epok, kwoty dotacji i kredytów zależą od daty. Szczegóły: [Koszty, utrzymanie i kredyty](costs.html).

## Przy wstrzymanym kalendarzu

1. Data, a więc i rok, stoją w miejscu: brak nowych pojazdów, a koszty zależne od roku się nie zmieniają.
2. Czasy są pokazywane w **minutach i sekundach** zamiast w dniach (`util.tl:41-43`, `industry_react_util.tl:16-21`).
3. Kredyt pokazuje ratę **na min.** zamiast na rok (`finances_loan_gui.tl:223-231`), a kredytu własnego nie można zaciągnąć (`finances_loan_gui.tl:393`).
4. Produkcja, płatności, terminy i reputacja zachowują swoje tempo w czasie gry.

## Warto wiedzieć

- Chcesz więcej czasu na rozbudowę sieci, zanim pojawią się nowe pojazdy? Obniż szybkość kalendarza: przychód na minutę gry się nie zmienia.
- Produkcja "na rok" zależy od szybkości kalendarza; porównuj zakłady przy tej samej szybkości.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) zachowuje czytelne wykresy finansów przy wstrzymanym kalendarzu.

```engine
Długość standardowego dnia, miesiąca i roku (getDefaultDayDuration i pozostałe) pochodzi z silnika. Skrypt miast liczy miesiąc jako 30 × 4 sekundy (`towns.script.tl:121`), co pasuje do zmierzonego dnia 4 sekund; kilka innych stałych zakłada jeszcze dzień 2 sekund (`cargotype.script.lua:3`, `mod.script.tl:172`).
```

```check
official: "By default a day in the game lasts 4 seconds." "Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent." ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: Szybkość kalendarza od ×0.25 do ×4 lub wstrzymany, względem standardowego dnia; produkcja, kredyty, dotacje, reputacja i liczniki pracowników działają w czasie gry; wstrzymany kalendarz pokazuje czasy w minutach, płatności na minutę i blokuje nowe kredyty; zmierzone: 4 s na dzień przy ×1.
result: refines
```
