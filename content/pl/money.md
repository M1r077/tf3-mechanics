---
title: Dlaczego tracę pieniądze?
summary: Co przynosi pieniądze, co kosztuje, i sprawdzenie w sześciu krokach, które linie tracą pieniądze i dlaczego, z linkami do stron, które wyjaśniają każdy punkt.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-15
game: 40444
fact: 1 | zapłata za sztukę, u odbiorcy, za linię prostą
fact: 0 | zapłaty w magazynie lub przy przeładunku
fact: 100 % | zapłaty nawet przy spóźnieniu
fact: ×6 | pokazywany mnożnik roku dla utrzymania magazynów, lądowisk, lotnisk i portów w 2020
---

Dostawa płaci za **jedną linię prostą**, od miejsca, gdzie towar powstał, do miejsca, gdzie jest używany, i tylko wtedy, gdy tam dotrze. Wszystko, co budujesz i kupujesz, kosztuje co roku, a część coraz więcej wraz z rokiem kalendarzowym. Linia traci pieniądze, gdy jej część zapłat jest mniejsza niż koszty, które przynosi.

```diagram money_flow
```

## Co przynosi pieniądze

- **Odległość w linii prostej** od źródła do odbiorcy, plus 8 × wzniesienie. Długość twojej trasy się nie liczy (`cargo_income.script.lua:3-7`, `cargo_income.script.lua:5`).
- **Każdy towar płaci tyle samo** za kilometr: mnożnik przychodu wynosi 3,8 dla wszystkich (`cargotype.script.lua:7-13`).
- **Raz, u odbiorcy.** Rozładunek w magazynie lub na stacji przeładunkowej nic nie daje. Zapłata jest potem dzielona między linie łańcucha według długości w linii prostej każdego odcinka (zmierzone w grze).
- **Spóźniony towar jest opłacany w całości**: czas podróży nie jest używany (`cargotype.script.lua:7-13`). Spóźnienie obniża za to ocenę „Dostawa” miasta.
- **Ranga firmy** obniża cały przychód z ustawieniem „Inflacja”: na randze 15 ×0,75 przy „Normalna” (`company_progression_util.tl:25-40`).
- **Wykonane subsydium** podwaja przez 5 lat przychód z dostaw, które obejmuje: do jego zakładu, do jego miasta lub pasażerów między jego dwoma miastami, tylko na jego liniach (`subvention_util.tl:286`). Zobacz [Subsydia: oferty, terminy i nagrody](subsidies.html).

Szczegóły: [Przychód z towarów i czas dostawy](income.html).

## Co kosztuje

- **Pojazdy**: koszty eksploatacji idą za średnią prędkością × pojemność, a cena to 6 lat kosztów eksploatacji (`model_metadata_util.lua:499-518`, `model_metadata_util.lua:548-549`).
- **Tory i drogi**: około jednej szóstej ceny budowy na km i rok; tor dużych prędkości kosztuje 9 razy więcej niż zwykły tor (`simple.street_template.lua:33`, `high_speed.street_template.lua:35`).
- **Zajezdnie, stacje, magazyny, porty, lotniska**: warianty z późniejszych epok kosztują ×3 i ×9 (`rail_depot.con.lua:7`, `warehouse.tl:48`), a dla magazynów, lądowisk, lotnisk i portów okno budynku pokazuje utrzymanie zależne od roku, od ×1 w 1900 do ×6 w 2020 (`mod.script.tl:92-100`, `entity_window_util.tl:188-192`). O tym, co jest pobierane, decyduje silnik.
- **Kredyty**: odsetki są liczone raz od kwoty i rozłożone na okres spłaty (`loan_util.tl:102-111`).
- **„Inflacja” nie podnosi żadnych kosztów**. Obniża tylko przychód.

Szczegóły: [Koszty, utrzymanie i kredyty](costs.html).

## Sześć sprawdzeń, po kolei

```diagram money_check
```

1. **Które linie tracą pieniądze?** Patrz na bilans każdej linii, nie na sumę firmy. Mod [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) pokazuje bilans każdej linii z ostatnich 12 miesięcy i jej średnią z kilku lat.
2. **Czy towar jedzie daleko?** Płaci tylko linia prosta od źródła do odbiorcy. Krótka linia dowozowa do magazynu dostaje tylko część za swój krótki odcinek ([Przychód z towarów i czas dostawy](income.html)).
3. **Czy jeździ pełny?** Pojazd kosztuje tyle samo pełny i pusty. Sprawdź puste powroty, **Poziom napełnienia** i **ładowanie do pełna** na każdym przystanku ([Ustawienia odjazdu: ładowanie do pełna, Poziom napełnienia i czasy postoju](departure.html)).
4. **Czy jest rozładowany tam, gdzie płacą?** To, czego nie ma na liście Ładunek przystanku, jest rozładowywane do każdego pobliskiego zapasu, także magazynu, a magazyn nic nie płaci ([Szybkość załadunku i rozładunku](loading.html), [Magazyny](warehouses.html)). Towar, który nie mieści się w pełnych zapasach miasta, zostaje na pokładzie ([Rozwój miast: doświadczenie, oceny i wielkość](towns.html)).
5. **Za dużo pojazdu?** Prędkość i pojemność kosztują, ale prędkość nie płaci: pomaga tylko wtedy, gdy daje więcej kursów w roku. W mieście stary, wolny autobus może być bardziej opłacalny niż nowy, szybki ([Koszty, utrzymanie i kredyty](costs.html)).
6. **Koszty stałe.** Zajezdnie, dodatkowe moduły magazynu, szybkie tory i budynki z późniejszej epoki kosztują co roku, używane czy nie ([Koszty, utrzymanie i kredyty](costs.html)).

## Warto wiedzieć

- **Wybieraj towary według ilości i odległości**, nie według ceny: każdy towar płaci tyle samo za km.
- **Długa linia główna** zasilana krótkimi liniami zarabia większość pieniędzy; linie dowozowe pokazują małe bilanse, ale liczy się cały łańcuch.
- **Więcej do przewiezienia**: wzmocniony zakład produkuje więcej ([Pracownicy i premia za pracowników](workers.html), [Przemysł](industries.html)), a większe miasto chce więcej towarów.
- Przyspieszenie linii nie podnosi zapłaty za sztukę. Pomaga tylko, jeśli te same pojazdy robią więcej kursów.

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks))
scripts: Tak samo: linia prosta plus 8 × wzniesienie, ten sam mnożnik dla każdego towaru, czas podróży nieużywany; zmierzone w grze: zapłata raz u odbiorcy i podział według długości odcinka; koszty idą za prędkością × pojemność dla pojazdów, 1/6 ceny dla torów, warianty epok ×3 / ×9 i mnożnik roku od ×1 do ×6 dla budynków; „Inflacja” obniża tylko przychód.
result: refines
```
