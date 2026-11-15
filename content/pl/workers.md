---
title: Pracownicy i premia za pracowników
summary: Jak mieszkańcy dostają pracę w zakładzie przemysłowym, którzy z nich liczą się do premii i jak duża jest premia.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-14
fact: 10 / 20 | pracowników potrzeba do premii
fact: 2 lata | tak długo liczy się przyjazd
fact: ×1,5–2,5 | mnożnik premii, stały dla każdego zakładu
---

Każdy zakład przemysłowy oferuje miejsca pracy. Gdy wystarczająco wielu pracowników **przyjeżdża twoimi liniami pasażerskimi**, zakład produkuje więcej. Okno zakładu pokazuje dwie różne liczby, a ich mylenie jest najczęstszym źródłem nieporozumień.

```diagram workers_flow
```

## Kto może pracować w zakładzie

- Każdy zakład przemysłowy z podstawowej gry ma **20 miejsc pracy** (`industrialCapacity = 20`).
- Miejsca pracy są ustawione tak, że mieszkańcy **nie mogą tam dojść pieszo ani dojechać samochodem**: dowieźć ich mogą tylko twoje linie (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Każdy mieszkaniec ma dom, sklep i pracę. Gra wybiera pracę spośród miejsc, do których dany mieszkaniec może dotrzeć; zakład przemysłowy ma wagę celu podróży 2,0 (`industryutil.lua:455`).

```engine
To, jak mieszkaniec wybiera jedną pracę spośród wszystkich osiągalnych miejsc (czas podróży, koszt, waga 2,0), oblicza silnik. Skrypty dostarczają tylko dane wejściowe.
```

## Przydzieleni pracownicy

To mieszkańcy, których miejscem pracy jest ten zakład. Pokazuje ich pasek miejsc pracy w oknie zakładu i kolumna **Miejsca pracy** w statystykach zakładów przemysłowych („12/20”) (`entity_window_util.tl:1238`, `statistic_industries.tl:305`). Sami przydzieleni pracownicy **nie** dają żadnej premii: muszą rzeczywiście tam dojechać.

## Pracownicy liczeni do premii

Niewielki skrypt gry śledzi każdy przyjazd (`industry_workers.script.tl`):

1. Gdy mieszkaniec przybywa do zakładu, a jego **ostatni odcinek podróży odbył się twoimi liniami**, przyjazd jest zapisywany wraz z czasem gry (`industry_workers.script.tl:86-118`).
2. Przechowywane są tylko przyjazdy z **ostatnich 2 lat gry** (`industry_productivity_util.tl:3`: `2 * getDefaultYearDuration()`).
3. Przechowywanych jest najwyżej **20 ostatnich** przyjazdów (`industry_workers.script.tl:4`, `KeepHistoryCount = 20`).
4. Gdy ta sama osoba przyjeżdża ponownie, nowy przyjazd zastępuje starszy: każdy mieszkaniec liczy się **tylko raz** (`industry_workers.script.tl:56-70`).

```diagram workers_window
```

## Kiedy premia się włącza i wyłącza

- Zakład dostaje premię, gdy liczba zaliczonych pracowników osiąga **połowę miejsc pracy**: `zaliczeni ≥ miejsca pracy × 0,5` (`industry_productivity_util.tl:35-48`, `RequiredWorkersFractionForBoost = 0.5`). Przy 20 miejscach pracy to **10 pracowników**.
- Dokładnie to pokazuje sekcja „Premie” w oknie zakładu: „zaliczeni / potrzebni”, przy czym liczba potrzebnych jest zaokrąglana w górę (`industry_react_util.tl:627`).
- Sprawdzenie jest powtarzane przy każdym nowym przyjeździe oraz wtedy, gdy najstarszy przyjazd staje się starszy niż 2 lata (`industry_workers.script.tl:40-43`). Dlatego premia **wyłącza się sama** mniej więcej 2 lata po tym, jak pracownicy przestali przyjeżdżać.

## Jak duża jest premia

- Produkcja jest mnożona przez **mnożnik premii** zakładu, pokazany w oknie jako „+X %” (`industry_react_util.tl:716`).
- Mnożnik jest losowany jeden raz z losowego ziarna zakładu: **od ×1,5 do ×2,5**, i dla tego zakładu nigdy się nie zmienia (`industry_productivity_util.tl:58-72`). Zakład bez ziarna dostaje ×2.
- Dlatego dwie identyczne kopalnie mogą mieć różną premię za pracowników: sprawdź „+X %”, zanim wybierzesz, którą obsługiwać.

## Przykład

Kopalnia węgla z 20 miejscami pracy i „+84 %”.

| Sytuacja | Zaliczeni | Premia? | Produkcja |
|---|---|---|---|
| Nowa linia autobusowa: 14 mieszkańców przydzielonych, nikt jeszcze nie dojechał | 0 | nie | ×1 |
| W tym roku autobusem przyjechało 12 różnych mieszkańców | 12 | tak (≥ 10) | ×1,84 |
| Linia autobusowa usunięta; przez 2 lata nikt nie przyjeżdża | spada do 0 | wyłącza się | ×1 |

## Warto wiedzieć

- Limit 20 przechowywanych przyjazdów i zasada 50 % oznaczają, że zakład mający **więcej niż 40 miejsc pracy** (możliwe z modami) nigdy nie dostałby premii za pracowników.
- Subsydium „Przewieź pracowników” jest wykonane, gdy ta premia się włącza (oficjalna wiki, Subsidies).
- Towary premiowe (nawozy, maszyny, narzędzia) to **osobna** premia dla zakładów surowcowych, nieomawiana tutaj.
- Mod [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) pokazuje w oknie zakładu, z których miast pochodzą pracownicy przydzieleni i zaliczeni do premii, ze strzałkami na mapie.

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: „Wystarczająco” = połowa miejsc pracy (10 z 20); „ostatnio” = ostatnie 2 lata gry, 20 ostatnich przyjazdów, jeden na osobę, tylko twoimi liniami; mnożnik premii od ×1,5 do ×2,5, inny dla każdego zakładu.
result: refines
```
