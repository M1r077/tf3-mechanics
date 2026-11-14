---
title: Przychód z towarów i czas dostawy
summary: Ile płaci dostawa (odległość w linii prostej, wzniesienie, ranga firmy, subsydia) i ile naprawdę kosztuje spóźnienie.
domain: economy
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: 3,8 | ten sam mnożnik przychodu dla każdego towaru
fact: +8 × wzniesienie | metry wzniesienia dodawane do odległości
fact: 100 % | zapłaty nawet za spóźnioną dostawę
---

Dostawa jest opłacana za **odległość w linii prostej**, nic innego w podróży się nie liczy. Szybkość ma znaczenie z innego powodu: każdy towar ma **limit czasu**, a spóźnione dostawy obniżają ocenę **Dostawa** miasta, a nie twój przychód.

```diagram income_formula
```

## Wzór na przychód

Cały wzór to jeden krótki skrypt gry (`cargo_income.script.lua:10-13`):

1. **Mnożnik przychodu** towaru. Każdy towar z podstawowej gry używa tej samej funkcji i tych samych cen (`initialPrice = 4`, `finalPrice = 3.2`), co daje **3,8 dla wszystkich 36 towarów** (`cargotype.script.lua:7-13`, `coal.cargo.lua:21-22`). Węgiel na tej samej odległości płaci dokładnie tyle samo co produkty gotowe.
2. Ustawienie **Przychód z towarów**: 50 %, 75 %, 100 %, 125 % lub 150 % (`difficulty_util.tl:38`, `mod.script.tl:211`). Wszystkie cztery gotowe poziomy trudności używają 100 % (`difficulty_util.tl:97`).
3. **Odległość**, patrz niżej.

Funkcja otrzymuje czas podróży, ale **go nie używa** (`cargotype.script.lua:7-13`): powolna lub spóźniona dostawa płaci tyle samo.

## Odległość: linia prosta plus wzniesienie

```diagram income_distance
```

- Odległość to **linia prosta w 3D** między dwoma punktami, a nie długość twojej trasy (`cargo_income.script.lua:3-7`).
- Gdy różnica wysokości jest dodatnia, dodawane jest **8 × ta wysokość** (`cargo_income.script.lua:5`): 100 m wzniesienia płaci jak 800 m więcej. W przeciwnym kierunku nic nie jest odejmowane.
- Dlatego kręta linia zarabia tyle samo co prosta, ale płacisz za utrzymanie każdego zbudowanego metra toru lub drogi.

```engine
Silnik wybiera dwa punkty i przekazuje je do skryptu. Zmierzone w grze (patrz niżej): to **źródło** towaru (przemysł lub budynek miejski, który go wyprodukował) i **odbiorca**, który go przyjmuje, tak jak mówi oficjalna wiki ("between the source and the final destination").
```

## Towar, który zmienia linię

Gdy jednostka towaru jedzie kilkoma liniami, na przykład statek → magazyn → pociąg, gra i tak płaci za nią **tylko raz**:

```diagram income_split
```

1. Rozładunek w magazynie lub na stacji przesiadkowej nie przynosi **nic**. Z około 17 000 zmierzonych płatności tylko 43 trafiły do zapasu, który nie był odbiorcą.
2. Gdy ostatni pojazd dostarcza towar do odbiorcy, jednostka jest opłacana według powyższego wzoru, za linię prostą **od źródła do odbiorcy**. Odcinki i rzeczywista trasa się nie liczą, więc objazd przez magazyn nie daje nic więcej.
3. Te pieniądze są dzielone między linie łańcucha **proporcjonalnie do długości każdego odcinka w linii prostej**: od jednego punktu załadunku do następnego i od ostatniego punktu załadunku do odbiorcy. Premia za wzniesienie nie liczy się w tym podziale.
4. Dostarczający pojazd najpierw trzyma całą kwotę, z jedną częścią na każdy odcinek. Jest ona księgowana kilka sekund czasu gry później (mediana około 6 s), a każda linia i każdy pojazd dostaje swoją część. Saldo linii zmienia się więc krótko po dostawie, a nie w magazynie.

Dlatego krótka linia dowozowa do magazynu zarabia mało, choć wykonuje całe zbieranie; najwięcej zarabia długi odcinek. Każda linia i tak pokazuje swoją rzeczywistą część we własnym saldzie.

```engine
Skrypty liczą tylko sumę (economy/cargo_income.script.lua); podział wykonuje silnik i nie jest widoczny w skryptach. Powyższe zasady zmierzono testowym modem tylko do odczytu: około 1700 płatności za jednostki z 2 lub 3 odcinkami oraz zmiany na kontach każdej uczestniczącej linii i każdego pojazdu. W 769 czystych przypadkach (jedna jednostka, jedna płatność) podział za każdym razem zgadzał się z długościami odcinków z dokładnością do 1 %; podział z premią za wzniesienie zgadzał się tylko w 59 % z nich, równy podział w żadnym.
```

## Co jeszcze zmienia kwotę

| Co | Efekt | Źródło |
|---|---|---|
| **Ranga firmy** z ustawieniem „Inflacja” | ranga 1: ×1, równomiernie malejąco do rangi 15: ×0,9 („Niska”), **×0,75 („Normalna”)**, ×0,6 („Wysoka”), ×0,5 („Bardzo wysoka”); „Brak”: zawsze ×1 | `company_progression_util.tl:25-40`, `difficulty_util.tl:50`, `mod.script.tl:694-697` |
| **Wykonane subsydium** | ×2 na liniach, które dostarczały towar w ramach kontraktu | `deliver_cargo.script.tl:463-469`, `deliver_cargo_town.script.tl:554-565` |
| **Spóźniona dostawa** | brak wpływu na przychód | `cargotype.script.lua:7-13` |

- Mnożnik rangi dotyczy **wszystkich** płatności za towary i pasażerów (`company_growth.script.tl:159-170`). Gotowe poziomy trudności używają inflacji „Niska” („Niski”), „Normalna” („Normalny”), „Wysoka” („Wysoki”), „Bardzo wysoka” („Bardzo wysoki”) (`difficulty_util.tl:108`).
- ×2 z subsydium dotyczy tylko linii, które dostarczały towar w czasie kontraktu, i to przez ograniczony czas (oficjalna wiki, Subsidies).

## Pasażerowie

Pasażerowie używają tej samej odległości i stałego mnożnika przychodu około 3,61 (`cargotype.script.lua:50-53`), pomnożonego przez **0,5 + mnożnik ceny biletu pojazdu** (`cargo_income.script.lua:14-17`). Gdy model pojazdu nie ustawia własnego mnożnika komfortu, gra ustawia mnożnik ceny na 0,3 dla autobusów i tramwajów, 0,9 dla samolotów, 0,1 dla statków i 0,5 dla pociągów (`base_mod.lua:46-61`); dla pozostałych modeli to wartość silnika, niewidoczna w skryptach. Subsydium pasażerskie również podwaja przychód na swojej linii (`deliver_passengers.script.tl:284-298`).

## Limity czasu dostawy

Każdy towar ma własny limit czasu (`timeToDeliverInSeconds` w każdym pliku .cargo.lua, na przykład `meat.cargo.lua:30`, `coal.cargo.lua:30`). Najkrótszy ma świeża żywność, ciężkie surowce pięć razy dłuższy:

```diagram delivery_times
```

- **Finanse › Czas dostawy** pokazuje limit każdego towaru na twojej mapie; warstwa satysfakcji z dostaw koloruje trasy od zielonego do czerwonego.
- Dostawa liczy się jako **opóźniona**, gdy dotrze po upływie limitu (`towns.script.tl:425`).
- Specjalistyczne moduły magazynu **zatrzymują** licznik czasu przechowywanego towaru (oficjalna wiki, Warehouses).

```engine
Silnik przelicza czas bazowy na limit czasu pokazywany w „Finansach” (skrypty odczytują go przez getAdjustedDeliveryTime) i decyduje, kiedy towar jest spóźniony. Z plików towarów pochodzą tylko powyższe wartości względne.
```

## Ile kosztuje spóźnienie: ocena „Dostawa”

Spóźniony towar jest opłacany w całości, ale każde miasto ma ocenę **Dostawa** (`town_util.tl:505-519`):

1. Gra liczy dostawy do miasta z **ostatniego półrocza** i to, ile z nich było spóźnionych (przyjmuje się co najmniej 10 dostaw, aby pierwsze dostawy nie wahały oceną).
2. Udział dostaw na czas → ocena: poniżej dolnego progu ocena wynosi 0, powyżej górnego 1, pomiędzy nimi liniowo. Przy domyślnej wrażliwości (**„Normalna”**): **30 % na czas → 0, 100 % → 1**, więc 90 % na czas daje 0,86.
3. Ustawienie **Wrażliwość na dostawy** przesuwa progi (`difficulty_util.tl:47`). „Wył.”: zawsze 1. Gotowe poziomy: „Niski” – „Mała”, „Normalny” – „Normalna”, „Wysoki” – „Duża”, „Bardzo wysoki” – „Bardzo duża” (`difficulty_util.tl:113`).

```diagram delivery_rating
```

„Dostawa” to jedna z sześciu ocen, z których najniższa ustala tempo rozwoju miasta: jedna ocena „Bardzo złe” zatrzymuje miasto (patrz [Rozwój miast](towns.html)).

## Przykład

Ta sama dostawa węgla, 5 km w linii prostej.

| Sytuacja | Zapłata |
|---|---|
| płaski teren, dowolna długość trasy | **100 %** |
| 10 km w linii prostej | **200 %** |
| cel 100 m wyżej | **116 %** |
| dostarczone z opóźnieniem | **100 %** (ocena „Dostawa” spada) |
| ranga firmy 15, inflacja „Normalna” | **75 %** |
| linia wykonanego subsydium | **200 %** |

## Warto wiedzieć

- Ponieważ każdy towar płaci tyle samo za kilometr, **wybieraj towary według wolumenu, odległości i limitu czasu**, a nie według ceny.
- Limity czasu są najważniejsze dla mięsa, ryb, warzyw i napojów: krótkie linie albo magazyny, które zatrzymują licznik.
- Każda jednostka dostarczona do budynku w mieście daje temu miastu również doświadczenie (`town_growth.script.tl:642`, `town_growth_config.res.lua:5`).

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks), [Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Ten sam mnożnik 3,8 dla wszystkich towarów; odległość w 3D plus 8 × wzniesienie; ranga firmy obniża przychód do ×0,75 przy randze 15 (inflacja „Normalna”); ×2 po subsydium; czas nie wpływa na przychód; zmierzone w grze: jednostka, która zmienia linię, jest opłacana raz, u odbiorcy, i dzielona między linie według długości odcinków; ocena „Dostawa” z udziału dostaw na czas w ostatnim półroczu („Normalna”: 30 % → 0, 100 % → 1).
result: refines
```
