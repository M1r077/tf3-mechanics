---
title: Subsydia: oferty, terminy i nagrody
summary: Cztery rodzaje kontraktów, co naprawdę je wypełnia, co zyskujesz i czym ryzykujesz oraz jak często pojawiają się nowe oferty.
domain: subsidies
official: gamemanual:management:subsidies
status: verified
updated: 2026-11-15
fact: 4 | rodzaje kontraktów w grze swobodnej
fact: 5 | przyjętych kontraktów najwyżej naraz
fact: ×2 | przychodu przez 5 lat na liniach, które dostarczały
fact: 0 | kary za odrzucenie oferty
---

Subsydium to kontrakt: zakład przemysłowy lub miasto proponuje zadanie, przy przyjęciu coś dostajesz, więcej, gdy wykonasz je na czas, a gdy przekroczysz termin, zwracasz zaliczkę i płacisz dodatkową karę. Odrzucenie oferty lub pozwolenie, by wygasła, nic nie kosztuje.

```diagram subsidy_life
```

## Cztery rodzaje kontraktów

```diagram subsidy_types
```

| Kontrakt | Cel | Co go wypełnia | Źródło |
|---|---|---|---|
| **Zaopatrz zakład przemysłowy** | zakład przemysłowy, który jeszcze nigdy nic nie wyprodukował | wymagana liczba dostaw do niego, **dowolnym z jego surowców wejściowych** | `deliver_cargo.script.tl:54-61`, `deliver_cargo.script.tl:230-234`, `deliver_cargo.script.tl:470-479` |
| **Zaopatrz miasto** | towar, którego miasto potrzebuje i w ogóle nie dostaje | wymagana liczba jednostek **tego towaru** dostarczonych do budynków miasta | `deliver_cargo_town.script.tl:566-581` |
| **Połącz miasta** | dwa miasta | **jeden** pasażer, który zaczyna podróż między tymi miastami linią zatrzymującą się w obu | `deliver_passengers.script.tl:263-280`, `subvention_util.tl:561-592` |
| **Przewieź pracowników** | zakład przemysłowy, który już wysyła lub przyjmuje towary i nie ma jeszcze premii | włącza się jego premia za pracowników (połowa miejsc pracy) | `deliver_workers.script.tl:121-131`, `deliver_workers.script.tl:152-156` |

- Każda nowa oferta wybiera, z równymi szansami, jeden z rodzajów, które mogą się w danej chwili pojawić (`subventions.script.tl:147-169`).
- **Zaopatrz zakład przemysłowy** i **Zaopatrz miasto** liczą dostawy, a nie kursy: każda opłacona jednostka, która dotrze do celu, dodaje 1. Przeładunki są dozwolone (`deliver_cargo.script.tl:470-479`).
- **Połącz miasta** nie wymaga żadnej liczby pasażerów: wypełnia go pierwszy pasażer, który wsiądzie do twojej linii między tymi dwoma miastami. „Bez przesiadki” oznacza, że ten odcinek podróży odbywa się jedną linią obsługującą oba miasta. Oferta się nie pojawia, jeśli jakaś linia już przewozi pasażerów między nimi (`deliver_passengers.script.tl:72-78`).
- Bliskie miasta są dużo bardziej prawdopodobne: waga pary spada z 1 przy 1 km lub mniej do 0,01 przy 20 km, do potęgi 7 (`deliver_passengers.script.tl:175-191`).
- **Zaopatrz miasto** woli towary, które są już gdzieś produkowane na mapie: 16 razy bardziej prawdopodobne niż pozostałe (`deliver_cargo_town.script.tl:277-280`).
- Ilość do dostarczenia zależy od ustawienia **Ryzyko subsydiów**:

| Ryzyko subsydiów | Zaopatrz zakład przemysłowy | Zaopatrz miasto (najwyżej zapotrzebowanie miasta) | Źródło |
|---|---|---|---|
| „Brak” | 10–50 | 10–30 | `deliver_cargo.script.tl:100-114`, `deliver_cargo_town.script.tl:165-188` |
| „Rozsądne” | 50–100 | 30–100 | |
| „Ryzykowne” | 75–150 | 35–125 | |
| „Bardzo ryzykowne” | 150–300 | 45–150 | |

## Czym jest bezprzesiadkowe połączenie?

Karta **Połącz miasta** prosi: „Stwórz bezprzesiadkowe połączenie między miastami {fromTownName} i {toTownName}, a potem przewoź między nimi pasażerów.” (`deliver_passengers.script.tl:14`).

- **Jedna linia z przystankiem w każdym mieście.** Gra przechodzi przez przystanki linii i bierze miasto każdego z nich; linia się liczy, gdy co najmniej jeden przystanek leży w każdym z dwóch miast. Inne przystanki, ich kolejność i typ pojazdu (autobus, tramwaj, pociąg, statek, samolot) nie mają znaczenia (`subvention_util.tl:561-592`).
- **Wypełnia go jeden pasażer**: pierwszy pasażer, który jedzie tą linią z przystanku w jednym mieście do przystanku w drugim, w dowolnym kierunku (`deliver_passengers.script.tl:263-280`, `deliver_passengers.script.tl:210-218`). Sprawdzenie patrzy tylko na ten przejazd, więc przesiadka przed nim lub po nim nie powinna mieć znaczenia.
- **Miasto przystanku** to miasto pierwszej stacji jego grupy stacji (`town_util.tl:1844-1873`). O tym, do którego miasta należy stacja, decyduje silnik.
- **Brak oferty**, gdy jakaś linia ma już w każdym mieście przystanek, który ładuje pasażerów, oraz pojazd, który zabiera pasażerów (`deliver_passengers.script.tl:72-78`). Linia tylko towarowa między nimi nie blokuje oferty.
- Kontrakt kończy się jako **Koniec subsydium**, gdy jedno z dwóch miast albo linia, która go wypełniła, zmieni się w sposób, który gra liczy jako nową wersję (`deliver_passengers.script.tl:232-240`).

```engine
To, do którego miasta należy stacja (stationSystem.getTown), kiedy dokładnie pasażer „zaczyna korzystać” z linii (OnStartedLineUsage) i które zmiany linii liczą się jako nowa wersja, ustala silnik. Nie sprawdzono, czy zmiana linii po wypełnieniu kontraktu kończy efekt „Podwojony dochód”.
```

## Nagrody i kary

Każdy kontrakt ma trzy listy, pokazane na jego karcie jako **W chwili przyjęcia**, **W chwili wypełnienia** i **W chwili niepowodzenia** (`subvention_util.tl:449-471`). Przy niepowodzeniu zaliczka jest zawsze zwracana, a do tego dochodzi jeszcze jedna kara (`deliver_cargo.script.tl:134-136`).

| Kontrakt | W chwili przyjęcia | W chwili wypełnienia | W chwili niepowodzenia | Źródło |
|---|---|---|---|---|
| Zaopatrz zakład przemysłowy | pieniądze | tylko efekt **„Podwojony dochód”** | zwrot zaliczki + kara | `deliver_cargo.script.tl:120-136` |
| Zaopatrz miasto | pieniądze **lub** reputacja w mieście | doświadczenie miasta **lub** pieniądze, plus podwojony dochód | zwrot zaliczki + utrata reputacji **lub** kara | `deliver_cargo_town.script.tl:194-229` |
| Połącz miasta | pieniądze, więcej za odległe miasta | doświadczenie w **obu** miastach, plus podwojony dochód | zwrot zaliczki + utrata reputacji w **obu** miastach | `deliver_passengers.script.tl:105-119` |
| Przewieź pracowników | pieniądze | pieniądze | zwrot zaliczki + kara | `deliver_workers.script.tl:92-116` |

- **Pieniądze**, przed skalowaniem według roku: zaliczka od 1,5 mln do 3,75 mln × mnożnik ryzyka („Brak” ×2, „Rozsądne” ×1, „Ryzykowne” ×0,75, „Bardzo ryzykowne” ×0,5); kara od 3 mln do 6 mln; zapłata za wykonanie od 3,75 mln do 11,25 mln (`deliver_cargo.script.tl:120-128`, `deliver_workers.script.tl:102-104`).
- Kwoty rosną z **rokiem kalendarzowym**, a nie z ustawieniem „Inflacja”: ×1 w 1900, równomiernie do ×4 od 2000, zaokrąglone w górę do 10 000 (`finances_util.tl:87-90`). W finansach są księgowane jako **Subsydia** (`subvention_util.tl:126-135`).
- **Zaopatrz miasto** daje nagrody i kary pieniężne tylko wtedy, gdy stan twojego konta jest poniżej 100 mln; powyżej może to zrobić już tylko 1 oferta na 10 (`deliver_cargo_town.script.tl:206-217`).
- **Doświadczenie miasta** to część bieżącego poziomu miasta: od 20 % do 100 % XP między jego poziomem a następnym (`deliver_cargo_town.script.tl:216`, `town_growth.script.tl:605-608`). W **Połącz miasta** jest mnożone przez mnożnik odległości, od 0,3 przy 1 km do 3,0 przy 20 km: odległe miasta mogą zyskać kilka poziomów (`deliver_passengers.script.tl:94-96`, `deliver_passengers.script.tl:116-118`).
- **Reputacja** utracona po niepowodzeniu widnieje w ocenie reputacji miasta jako **Nieuzyskane subsydia** (`towns.script.tl:313-334`). Reputacja zyskana przy przyjęciu tylko usuwa istniejące kary, nie może przekroczyć maksimum (`town_util.tl:1644-1647`).

## Efekt „Podwojony dochód”

- Trwa **60 miesięcy** (5 lat) od wypełnienia kontraktu (`subvention_util.tl:286`, `subvention_util.tl:292`).
- **Zaopatrz zakład przemysłowy**: dostawy do tego zakładu, na liniach, które dostarczały do niego w czasie kontraktu (`deliver_cargo.script.tl:463-469`).
- **Zaopatrz miasto**: dostawy do dowolnego budynku tego miasta, **dowolnego towaru**, na liniach, które dostarczały towar z kontraktu (`deliver_cargo_town.script.tl:554-565`).
- **Połącz miasta**: pasażerowie między tymi dwoma miastami na linii, która wypełniła kontrakt (`deliver_passengers.script.tl:281-304`).
- **Przewieź pracowników** nie ma żadnego efektu przychodowego (`deliver_workers.script.tl:90`).
- Linia, która zaczęła dostarczać dopiero po wypełnieniu kontraktu, nic nie dostaje: lista linii jest wypełniana tylko w czasie kontraktu.
- Dwa kontrakty nigdy nie podwajają tej samej płatności dwukrotnie: gdy pasuje kilka, liczy się tylko ostatnia odpowiedź (`subventions.script.tl:570-583`).

```tip scripts
**Chcesz podwójny dochód na kilku liniach? Niech wszystkie dostarczają przed wypełnieniem kontraktu.** Linia dodana później nic nie dostaje.
```

```engine
To, jak ×2 z subsydium łączy się z mnożnikiem rangi firmy (ustawienie „Inflacja”), ustala silnik: oba skrypty zwracają tylko mnożnik dla każdej płatności. Czym jest jedna pozycja płatności (zapewne jedna jednostka towaru lub jeden pasażer), również ustala silnik.
```

## Terminy

Termin biegnie od przyjęcia. Jest dłuższy, gdy towar musi pokonać dużą odległość, i krótszy przy wyższym ryzyku (mnożnik ryzyka „Brak” ×2, „Rozsądne” ×1, „Ryzykowne” ×0,75, „Bardzo ryzykowne” ×0,5 albo ×0,625 dla kontraktów pasażerskich i pracowniczych):

| Kontrakt | Termin w miesiącach | Użyta odległość | Źródło |
|---|---|---|---|
| Zaopatrz zakład przemysłowy, Zaopatrz miasto | (6 + 32 × E) × mnożnik ryzyka | do najbliższego zakładu produkującego ten towar | `deliver_cargo.script.tl:116-117` |
| Połącz miasta | (9 + 4 × E) × mnożnik ryzyka | między dwoma miastami | `deliver_passengers.script.tl:98-99` |
| Przewieź pracowników | (6 + 15 × E) × mnożnik ryzyka × mnożnik epoki (×1,75 przed 1940, ×1,25 przed 1980) | do najbliższego miasta | `deliver_workers.script.tl:75-87` |

E to czas, którego pociąg z prędkością maksymalną epoki (od 120 km/h w 1900 do 300 km/h od 1981) potrzebuje na tę odległość, zaokrąglony w górę, co najmniej 1 (`subvention_util.tl:486-489`, `vehicle_util.tl:225-230`).

- Nieprzyjęta oferta znika po około **6 miesiącach** (od 150 do 210 dni), bez żadnej kary (`subvention_util.tl:284`, `subvention_util.tl:290`).
- Dopóki trwa kontrakt **Zaopatrz zakład przemysłowy** lub **Przewieź pracowników**, docelowy zakład nie może zostać zamknięty: zaplanowane zamknięcie jest anulowane (`subvention_util.tl:473-484`).
- Jeśli cel zniknie lub zostanie przebudowany w czasie kontraktu, gra pokazuje **Koniec subsydium**, ale kary są naliczane jak przy przekroczonym terminie (`subventions.script.tl:172-190`, `subvention_util.tl:406-412`).
- Nie ma przycisku do anulowania przyjętego kontraktu.

```engine
Długość miesiąca gry, a więc rzeczywistą długość terminów, ustala silnik (getDefaultMonthDuration). Powyższe wzory podają miesiące kalendarza gry.
```

## Jak często pojawiają się nowe oferty

- **Dostępność subsydiów**: „Rzadko”, „Czasem” (domyślnie), „Często”, „Bardzo często” dają nową ofertę co 12, 6, 3 lub 1 miesiąc; **„Nigdy”** wyłącza subsydia (`subvention_util.tl:13-38`, `mod.script.tl:247-248`).
- Odstęp rośnie z **rangą firmy**: ×1 przy randze 1 do ×2 przy randze 15 (`subvention_util.tl:19-22`).
- **Odrzucenie** oferty skraca następny odstęp o połowę; przyjęcie lub nowa oferta go resetuje (`subventions.script.tl:429`, `subventions.script.tl:395`, `subventions.script.tl:118`).
- Nowych ofert nie ma, dopóki **5 kontraktów** jest przyjętych i w toku (`subventions.script.tl:23`, `subventions.script.tl:256-262`). Pierwsza oferta pojawia się po pół miesiąca.
- Ten sam cel (zakład, miasto i towar, para miast) jest oferowany **tylko raz na grę**, nawet po przekroczonym terminie lub nieudanym kontrakcie (`subventions.script.tl:107-113`, `subventions.script.tl:186`).
- Gotowe poziomy trudności, dostępność / ryzyko (`difficulty_util.tl:104-105`, `difficulty_util.tl:132-133`, `difficulty_util.tl:159-160`, `difficulty_util.tl:186-187`): „Niski” „Często” / „Brak”, „Normalny” „Czasem” / „Rozsądne”, „Wysoki” „Rzadko” / „Ryzykowne”, **„Bardzo wysoki” „Nigdy”**: żadnych subsydiów.
- Warunek, który pozwalałby na subsydia tylko w miastach z oceną „Bardzo dobre”, istnieje, ale jest wyłączony (`town_util.tl:1574-1580`, `deliver_cargo_town.script.tl:272-275`).

## Warto wiedzieć

- Przyjmuj śmiało, gdy cel jest łatwy: odrzucenie lub zignorowanie nic nie kosztuje, ale **niepowodzenie** kosztuje zwrot zaliczki plus karę, która może być większa niż zaliczka.
- Przy **Zaopatrz miasto** i **Zaopatrz zakład przemysłowy** zacznij dostarczać każdą linią, która ma na tym skorzystać: tylko linie dostarczające w czasie kontraktu dostają podwojony dochód przez 5 lat.
- **Połącz miasta** z odległymi miastami daje najwięcej doświadczenia miasta i wymaga tylko jednego pasażera.
- **Zaopatrz zakład przemysłowy** nie płaci nic więcej za wykonanie: jego nagrodą jest wyłącznie podwojony dochód.

```check
official: "Accept an offer to begin the contract; declining it has no penalty." "Possible rewards include town experience, an additional payment, or a limited-time 2x income effect on eligible transport lines." "The upfront reward is reversed, and an additional fine or loss of town reputation may apply." ([Subsidies](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:subsidies))
scripts: Cztery rodzaje; jeden pasażer wypełnia „Połącz miasta”; ×2 trwa 60 miesięcy na liniach, które dostarczały w czasie kontraktu; „Zaopatrz zakład przemysłowy” daje tylko ×2; kwoty skalowane według roku (×1 do ×4); nowa oferta co 1–12 miesięcy, rzadziej przy wysokiej randze firmy; najwyżej 5 przyjętych; każdy cel oferowany raz na grę.
result: refines
```
