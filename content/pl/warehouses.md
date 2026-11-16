---
title: Magazyny
summary: Moduły uniwersalne lub specjalistyczne, co mieści każdy zapas, przypinanie rodzaju towaru, szybkość załadunku, koszty i zanieczyszczenie oraz czego magazyn nie robi.
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
game: 40425
fact: 500 | jednostek towaru na moduł, niezależnie od jego typu
fact: ×2 | szybkość załadunku przy module specjalistycznym, ×1 przy uniwersalnym
fact: 150 000 / 300 000 | cena modułu uniwersalnego / specjalistycznego
fact: 0 | przychodu za towar rozładowany w magazynie
---

Magazyn to wejście i zestaw **modułów**. Przechowuje towar między dwiema liniami: jedna linia go rozładowuje, druga ładuje ponownie. Stacje docierają do niego przez swój obszar obsługi; miasta i zakłady przemysłowe nigdy nic z niego nie biorą (oficjalna wiki).

## Moduły uniwersalne lub specjalistyczne

| Moduł | Zapas | Mieści | Mnożnik załadunku | Źródło |
|---|---|---|---|---|
| **Magazyn uniwersalny** | wszystkie moduły uniwersalne dzielą **jeden** zapas | dowolny towar, mieszany | ×1 | `warehouse.script.lua:272-295`, `modules.script.lua:49` |
| **Magazyn płynów**, **Magazyn towarów sypkich**, **Magazyn towarów niewymiarowych**, **Magazyn produktów** | **jeden zapas na moduł** | jeden rodzaj towaru naraz, ze swojej klasy | ×2 | `warehouse.script.lua:296-314`, `modules.script.lua:120`, `modules.script.lua:165`, `modules.script.lua:247`, `modules.script.lua:296` |

- Każdy moduł dodaje **500** jednostek (`modules.script.lua:49`, `modules.script.lua:120`). Pięć modułów uniwersalnych tworzy jeden zapas 2 500; pięć modułów płynów tworzy pięć zapasów po 500.
- Pasażerowie nigdy nie są przechowywani (`warehouse.script.lua:279`, `warehouse.script.lua:304`).
- Moduł specjalistyczny przyjmuje jeden rodzaj towaru naraz: aby przechowywać ropę naftową i paliwo, potrzebujesz dwóch modułów płynów (oficjalna wiki).
- ×2 modułu specjalistycznego mnoży się z mnożnikiem peronu: peron do towarów sypkich i moduł towarów sypkich dają ×4. Szczegóły: [Szybkość załadunku i rozładunku](loading.html).

## Uniwersalny czy specjalistyczny?

1. **Wiele rodzajów towaru, małe ilości**: uniwersalny. Jeden wspólny zapas, połowa ceny i połowa zanieczyszczenia.
2. **Jeden towar w dużych ilościach** (węgiel, ropa naftowa, drewno): specjalistyczny. Pojazdy rozładowują i ładują tam dwa razy szybciej, ale potrzebujesz jednego modułu na rodzaj towaru.
3. **Żywność i inny towar o krótkim czasie dostawy**: specjalistyczny; oficjalna wiki mówi, że te moduły zatrzymują licznik czasu dostawy (patrz niżej).
4. Oba rodzaje można łączyć w jednym magazynie: moduły uniwersalne nadal tworzą jeden zapas, każdy moduł specjalistyczny własny.

## Czy magazyn przyspiesza rozładunek?

- **Moduł specjalistyczny**: tak, ×2 dla towaru, który przyjmuje. Podpowiedź załadunku pojazdu pokazuje „Specjalistyczny magazyn: +100 %” (`cargo_react_util.tl:51-54`).
- **Moduł uniwersalny**: nie. Jego zapas jest tworzony z ×1; ×2, którego żąda moduł, jest pomijane (`warehouse.script.lua:284`, `warehouse.script.lua:288-289`).
- Gdy część towaru trafia do magazynu, a część do zakładu, pojazd obsługuje je po kolei, więc szybkość zmienia się podczas jednego postoju (zmierzone w grze, patrz [Szybkość załadunku i rozładunku](loading.html)).

## Sekcja Zapasy

- Jeden wiersz na zapas: przyjmowany towar, ilość i po najechaniu kursorem **Średni pozostały czas dostawy** (`entity_window_util.tl:408-410`).
- **Przypnij rodzaj towaru**: przy module specjalistycznym kliknij ikonę towaru. Gra przebudowuje magazyn z tym modułem zarezerwowanym dla tego towaru (`entity_window_util.tl:339-367`, `warehouse.script.lua:308`). Usunięcie lub zastąpienie modułu kasuje przypięcie (`warehouse.script.lua:403-405`).
- **Porzuć cały ładunek**: od razu opróżnia ten wiersz (`entity_window_util.tl:423-434`). Towar przepada.
- Obu przycisków brakuje tylko w magazynie należącym do innego gracza; twoje magazyny i magazyny bez właściciela je mają (`warehouse_eow.script.tl:127-137`, `gui/entity_window/warehouse/warehouse.tl:38`, `entity_util.tl:83-86`).
- Wykres **Statystyki** pokazuje **Przybywa** (rozładowane) i **Wyjeżdża** (załadowane) na rok (`warehouse_eow.script.tl:159-160`).

## Koszty i zanieczyszczenie

| | Moduł uniwersalny | Moduł specjalistyczny | Źródło |
|---|---|---|---|
| Cena | 150 000 | 300 000 | `wh_universal.module.lua:18`, `wh_liquid.module.lua:22` |
| Utrzymanie na rok | 25 000 | 50 000 | `wh_universal.module.lua:19`, `wh_liquid.module.lua:23` |
| Hałas | 20 | 20 | `wh_universal.module.lua:33`, `wh_liquid.module.lua:37` |
| Zanieczyszczenie | 25 | 50 | `wh_universal.module.lua:34`, `wh_liquid.module.lua:38` |

- Magazyn dodaje własne zanieczyszczenie: **25** lub **50**, gdy tylko zostanie zbudowany jeden moduł specjalistyczny (`warehouse.script.lua:327`, `warehouse.script.lua:338-345`).
- Menu budowy ma jedną pozycję na klasę i epokę (od 1900, 1940 i 1980) (`warehouses/warehouse.tl:3-5`); późniejsze epoki pokazują ×3 i ×9, a utrzymanie magazynów rośnie też z rokiem. Szczegóły: [Koszty, utrzymanie i kredyty](costs.html).
- Moduły towarów sypkich, towarów niewymiarowych i produktów kosztują tyle samo co moduły płynów (`wh_bulk.module.lua:22-23`, `wh_flatbed.module.lua:22-23`, `wh_goods.module.lua:18-19`).

```engine
Skrypty podają dwa poziomy emisji, drugi dwa razy wyższy od pierwszego (`warehouse.script.lua:342-343`); magazyn przechodzi od pierwszego do drugiego w miarę zapełniania zapasów, pełne zapasy = dwa razy (`emissions.script.tl:237-249`). Cenę faktycznie pobieraną za moduły liczy silnik.
```

## Czego magazyn nie robi

- **Nic nie płaci.** Rozładunek w magazynie nie daje przychodu; towar jest opłacany raz, gdy dotrze do odbiorcy, za odległość w linii prostej od swojego źródła (zmierzone w grze, patrz [Przychód z towarów i czas dostawy](income.html)).
- **Nie zaopatruje miast ani zakładów** w pobliżu: biorą one towar tylko z pojazdów (oficjalna wiki).
- **Nie jest celem dla automatycznej konfiguracji linii**, która szuka tylko producentów i odbiorców; ale przystanek obok magazynu, który przechowuje dany towar, zostawia ten towar poza listą Ładunek, więc pociągi go tam rozładowują (patrz [Szybkość załadunku i rozładunku](loading.html)).
- **Nie potrzebuje drogi.** Wejście przyciąga się do ulicy, ale towar przemieszcza się tylko przez obszary obsługi stacji (`warehouse.script.lua:386-389`, oficjalna wiki). Okno magazynu pokazuje jego obszar obsługi (`gui/entity_window/warehouse/warehouse.tl:88-96`).

```engine
Dokąd trafia rozładowany towar i czy licznik czasu dostawy przechowywanego towaru się zatrzymuje, decyduje silnik. Żaden skrypt nie zatrzymuje licznika: oficjalna wiki mówi, że moduły specjalistyczne to robią, a uniwersalny nie.
```

## Warto wiedzieć

- Sprawdź listę Ładunek każdego przystanku w pobliżu magazynu: to, czego na niej nie ma, jest rozładowywane do magazynu, nawet w połowie linii.
- Pełny zapas odmawia przyjęcia kolejnego towaru, chyba że przystanek używa „Wymuś rozładowanie wszystkich towarów po przybyciu”, co niszczy to, co się nie mieści (patrz [Szybkość załadunku i rozładunku](loading.html)).
- Aby zachować moduł specjalistyczny dla jednego towaru, przypnij jego rodzaj towaru w sekcji Zapasy.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) pokazuje dla każdej stacji magazyny w zasięgu wraz z ich zapasami; [Platform Details](https://mod.io/g/transportfever3/m/platform-details) pokazuje, dokąd trafił rozładowany towar.

```check
official: "Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types." Specjalistyczne magazyny "freeze the cargo item's delivery timer" i "enable faster loading / unloading speeds". "In specialized warehouses, only one cargo type can be stored at a time for a given module." ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Moduły uniwersalne tworzą jeden wspólny zapas z mnożnikiem załadunku ×1, każdy moduł specjalistyczny własny zapas 500 z ×2 i jednym rodzajem towaru. Moduł specjalistyczny kosztuje dwa razy więcej (300 000, utrzymanie 50 000) i zanieczyszcza dwa razy bardziej (50). Zatrzymania licznika nie ma w skryptach.
result: refines
```
