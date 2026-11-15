---
title: Przemysł
summary: Reguły produkcji, zapasy, parcele i rozbudowa, dlaczego zakład nie rośnie lub nie ma premii, kiedy nieużywany zakład się zamyka i jak pojawiają się nowe zakłady.
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
fact: 5 lat | bez załadunku i zużycia czyni zakład kandydatem do zamknięcia
fact: 1,1 % | szansy na rok przy Rzadko (domyślne), potem 730 dni odliczania
fact: +50–150 % | premii z towaru premiującego, stałej dla zakładu
fact: 3 miesiące | premii z jednej partii towaru premiującego
fact: ×2/3 – ×1,5 | Docelowe zagęszczenie przemysłu: nowych zakładów nie da się wyłączyć
---

Każdy zakład działa według **reguł**: „weź to z zapasów wejściowych, połóż tamto w zapasach wyjściowych”, stałą liczbę razy w roku. Zakłady surowcowe (kopalnie, gospodarstwa, odwierty) nie potrzebują wejścia; ich wielkość zależy od **parcel**. Dwie premie mogą mnożyć produkcję: **towar premiujący** (tylko zakłady surowcowe) i **pracownicy**.

## Reguły produkcji

- Reguła podaje towar zużyty i wytworzony w jednym cyklu oraz liczbę cykli w roku: cykl trwa rok ÷ ta liczba (`industry_react_util.tl:51-57`). Sekcja Produkcja okna zakładu pokazuje to małymi liczbami.
- Liczba **Maks.** w oknie to: na cykl × cykle na rok × premie × ustawienie **Wydajność przemysłu** (`industry_util.tl:310-379`).
- **Wydajność przemysłu**: 50 %, 75 %, 100 %, 150 % lub 200 %. Ustawienia wstępne: Niski 150 %, Normalny 100 %, Wysoki 75 %, Bardzo wysoki 50 % (`difficulty_util.tl:41`, `difficulty_util.tl:93`, `difficulty_util.tl:120`, `difficulty_util.tl:148`, `difficulty_util.tl:175`, `mod.script.tl:196-197`).
- Przykład, Stalownia: 6 rudy żelaza + 6 węgla → 3 stal + 4 blacha, 121,7 cyklu w roku: 730 rudy żelaza i 730 węgla → 365 stali i 487 blachy (`steel_mill.con.lua:43-71`). Brak jednego wejścia zatrzymuje regułę.
- Fabryka konserw ma dwie reguły: ryby + blacha albo mięso + blacha (`food_factory.con.lua:43-74`).

```engine
Silnik wykonuje reguły. Może wydłużyć cykl: podpowiedź cyklu pokazuje wtedy „(+ … z powodu czasu dostawy)” (`industry_react_util.tl:61-76`). Kiedy i o ile, nie ma w skryptach, więc rzeczywista produkcja może zostać poniżej Maks.
```

## Zapasy

- Każdy towar ma własny zapas z limitem: np. Kopalnia węgla trzyma 100 narzędzi i 400 węgla, Stalownia 800 rudy żelaza, 800 węgla, 400 stali i 500 blachy (`coal_mine.con.lua:44-67`, `steel_mill.con.lua:43-71`).
- Zapasy nigdy się nie psują (`industryutil.lua:25-29`): towar czeka tak długo, jak trzeba.
- Pełny zapas wyjściowy nie zatrzymuje produkcji: nadwyżka jest wyrzucana (oficjalna wiki). Wykres **Przepływ towarów** pokazuje **Zużyte**, **Wyprodukowane** i **Zniszczone** (`industry_eow.script.tl:804-816`).
- Z parametrem budowy **Przybywa** ustawionym na Wył. reguły tracą wejścia, a zakład nie ma zapasów wejściowych (`industryutil.lua:280-287`, `industryutil.lua:383-387`, `industryutil.lua:432-441`).

## Parcele i rozbudowa

- Zakłady surowcowe i Hodowla bydła mają **parcele** (pola, szyby, wieże wiertnicze). Ich poziom to liczba parcel (`industryutil.lua:602-617`).
- Reguła rośnie z parcelami: produkcja na cykl × parcele ÷ **wszystkie parcele tego typu zakładu**, zaokrąglone, co najmniej 1. Wejścia maleją w tej samej proporcji (`industryutil.lua:225-259`). Kopalnia węgla (8 typów parcel) z 4 parcelami robi 8 węgla na cykl zamiast 16.
- Każdy zakład dostaje maksimum: losowo między połową parcel a wszystkimi, albo Mały / Średni / Duży (50 / 75 / 100 %) z parametrem **Wielkość zakładu** (`industryutil.lua:519-537`). Kopalnia z maksimum 5 z 8 nigdy nie osiąga pełnej reguły.
- Przy Średni, jeśli 75 % po zaokrągleniu daje wszystkie parcele, maksimum to wszystkie parcele minus jedna (`industryutil.lua:523-526`). Nowy zakład zaczyna z parcelami, które silnik buduje przy postawieniu; jego poziom wynika z nich (`industryutil.lua:602-617`).
- Co pół roku **czasu gry** gra może dodać **jedną parcelę** (`industries_config.res.lua:5`, `industries.script.tl:161-167`). Używane jest pół standardowego roku, więc szybkość kalendarza nie zmienia częstotliwości (zobacz [Czas gry i kalendarz](time.html)).
- Szansa to (ocena − 25 %) ÷ 50 %, gdzie ocena = ocena produkcji × część produkcji, którą wywozisz (najwyżej 1): 25 % lub mniej nigdy, 75 % lub więcej zawsze (`industries.script.tl:168-179`).
- Zakład, którego towaru nie wywozisz, **nigdy więc nie rośnie**. Fabryki nie mają parcel i nigdy nie rosną.
- Przy maksimum okno pisze **Zakład przemysłowy jest rozwinięty maksymalnie.**; gdy budynki, tory lub drogi przeszkadzają, **Dalszy rozwój zakładu przemysłowego jest zablokowany.** (`industry_react_util.tl:588-602`, `industries.script.tl:13-38`). Żaden skrypt nie usuwa parcel; według oficjalnej wiki zburzone parcele obniżają produkcję.
- Skrypt gry pomija zakłady należące do ciebie, zakłady z ręcznym rozwojem i zakłady w odliczaniu do zamknięcia: nigdy nie dostają od niego parceli (`industries.script.tl:94-99`, `industries.script.tl:147-157`).

Przykład, **Poręba**: 20 parcel, 8 drewna na cykl, 30,4 cyklu w roku (`forest.con.lua:54-66`, `forest.con.lua:75-98`). Na cykl robi 8 × parcele ÷ 20, zaokrąglone, co najmniej 1 (`industryutil.lua:231-241`):

| Parcele (poziom) | Drewno na cykl | Drewno na rok (Maks., bez premii, Wydajność 100 %) |
|---|---|---|
| 1–3 | 1 | 30 |
| 4–6 | 2 | 61 |
| 7–8 | 3 | 91 |
| 9–11 | 4 | 122 |
| 12–13 | 5 | 152 |
| 14–16 | 6 | 183 |
| 17–18 | 7 | 213 |
| 19–20 | 8 | 243 |

Produkcja rośnie skokami: nowa parcela nie zawsze podnosi produkcję.

## Dlaczego mój zakład nie rośnie?

```diagram ind_growth
```

1. **Towar nie jest wywożony**: ocena liczy część produkcji załadowaną do twoich pojazdów. Przy ocenie produkcji 100 % wywóz 25 % lub mniej nie daje szansy, 50 % daje szansę połowy, 75 % lub więcej parcelę co pół roku.
2. **Przy maksimum**: **Zakład przemysłowy jest rozwinięty maksymalnie.** Maksimum jest losowane przy budowie (od połowy do wszystkich parcel) i nigdy się nie zmienia.
3. **Zablokowany**: **Dalszy rozwój zakładu przemysłowego jest zablokowany.** Usuń drogi, tory lub budynki z miejsca następnej parceli (pokazanego w oknie).
4. **To nie zakład surowcowy**: fabryki nie mają parcel.
5. **Odliczanie do zamknięcia**, zakład należy do ciebie lub ma ręczny rozwój: brak wzrostu ze skryptu (wyżej).
6. **Brak produkcji**: zakład, który w roku nic nie wyprodukował, jest pomijany (`industries.script.tl:168-171`).

```engine
Ocena produkcji (getProductionRating), roczna produkcja i wywieziona ilość (getCargoOutputPerYear, getCargoShippedPerYear) oraz miejsce nowej parceli (makeIndustryExtendProposal) to wartości silnika.
```

## Towar premiujący

13 zakładów surowcowych ma drugą regułę, **premię**: 4 razy w roku bierze partię towaru premiującego z zapasu wejściowego i daje bonus, dopóki działa.

| Zakład | Parcele | Przy pełnej wielkości, na rok | Partia premii (4 na rok) | Źródło |
|---|---|---|---|---|
| Glinianka | 8 | 365 gliny | 12 narzędzi | `clay_pit.con.lua:42-82` |
| Kopalnia węgla | 8 | 320 węgla | 13 narzędzi | `coal_mine.con.lua:44-85` |
| Plantacja bawełny | 21 | 274 wełny | 17 nawozów | `cotton_farm.con.lua:42-98` |
| Gospodarstwo rolne | 20 | 274 zboża + 183 warzyw | 17 nawozów | `farm.con.lua:44-106` |
| Stawy rybackie | 18 | 263 ryb | 12 narzędzi | `fishing_grounds.con.lua:44-101` |
| Poręba | 20 | 243 drewna | 15 maszyn | `forest.con.lua:44-99` |
| Kopalnia rudy żelaza | 8 | 365 rudy żelaza | 15 maszyn | `iron_ore_mine.con.lua:44-84` |
| Platforma wiertnicza | 9 | 365 ropy surowej | 12 maszyn | `oil_platform.con.lua:45-96` |
| Kiwon | 14 | 548 ropy surowej | 15 maszyn | `oil_well.con.lua:44-94` |
| Kamieniołom | 7 | 365 kamienia | 12 narzędzi | `quarry.con.lua:44-83` |
| Plantacja kauczuku | 23 | 365 gumy | 17 nawozów | `rubber_farm.con.lua:41-102` |
| Pogłębiarka | 9 | 365 piasku | 15 maszyn | `sand_excavator.con.lua:44-92` |
| Piaskarnia | 8 | 365 piasku | 12 narzędzi | `sand_pit.con.lua:44-84` |

- Bonus jest losowany raz na zakład: **od +50 % do +150 %**, zaokrąglony do 1 % (`industryutil.lua:394-405`). Sekcja Premia pokazuje go jako „+X %” (`industry_util.tl:428-434`). Z parametrem **Współczynnik premii** wynosi zamiast tego +50 %, +75 %, +100 %, +125 % lub +150 % (`industryutil.lua:289-299`).
- Okno pokazuje premię jako aktywną, dopóki trwa ostatnia partia (3 miesiące), albo gdy tylko zapas zawiera pełną partię (`industry_util.tl:55-91`).
- Partia **nie** maleje z parcelami: mała kopalnia potrzebuje tylu narzędzi co duża (`industryutil.lua:227-229`).
- Obie premie się mnożą: produkcja × współczynnik pracowników × (1 + bonus premii) (`industry_util.tl:42-104`).

## Premia za pracowników

Połowa miejsc pracy (10 z 20) musi być zajęta przez mieszkańców, którzy w ostatnich 2 latach **przyjechali twoimi liniami pasażerskimi**; współczynnik wynosi ×1,5 do ×2,5, stały dla zakładu (`industry_productivity_util.tl:35-72`). Pracownicy tylko przydzieleni się nie liczą. Szczegóły: [Pracownicy i premia za pracowników](workers.html).

## Dlaczego mój zakład nie ma premii?

1. **To nie zakład surowcowy**: fabryki nie mają reguły premii, tylko premię za pracowników (`steel_mill.con.lua:61-70`).
2. **Niepełna partia**: zapas musi zawierać pełną partię, np. 13 narzędzi dla Kopalni węgla. Poniżej 4 partii rocznie (52 narzędzia) premia gaśnie między dostawami.
3. **Zły towar**: narzędzia, maszyny lub nawozy zależnie od zakładu (tabela wyżej).
4. **Pracownicy**: przydzieleni to za mało; sekcja Premia liczy przyjazdy („12/10”) (`industry_react_util.tl:617-654`). Zobacz [Pracownicy i premia za pracowników](workers.html).

## Kiedy nieużywany zakład się zamyka?

```diagram ind_closure
```

Sprawdzenie odbywa się co 100 aktualizacji dla każdego zakładu (`industries.script.tl:84-85`):

1. **Kandydat**: żaden towar nie został **załadowany** do pojazdu ani **zużyty** przez **5 lat** (od budowy, jeśli nigdy) (`industries.script.tl:104-119`, `industries_config.res.lua:6`). Sama produkcja się nie liczy.
2. **Los**: co roku kandydat jest oznaczany z szansą z ustawienia **Częstotliwość zamykania przemysłu** (tabela niżej) (`industries.script.tl:120-131`).
3. **Odliczanie**: pojawia się powiadomienie **Zamknięcie przemysłu**, z 2 latami (730 dni) czasu (`industries_config.res.lua:7`, `industry_close.script.tl:53-67`). Potem zakład jest usuwany razem z własnymi odcinkami drogi (`industries.script.tl:147-155`, `industry_util.tl:560-601`).
4. **Uratowany**: jeden załadunek lub zużycie w trakcie odliczania je przerywa (`industries.script.tl:134-137`). Przyjęcie dotacji **Zaopatrz zakład przemysłowy** lub **Przewieź pracowników** dla niego też je przerywa (`subvention_util.tl:473-484`).

| Częstotliwość zamykania przemysłu | Szansa na rok jako kandydat | Połowa kandydatów oznaczona po | Ustawienie wstępne | Źródło |
|---|---|---|---|---|
| Nigdy | 0 | nigdy | Niski | `difficulty_util.tl:94` |
| Rzadko (domyślne) | 1,1 % | około 63 latach | Normalny | `difficulty_util.tl:121` |
| Czasem | 2,2 % | około 32 latach | Wysoki | `difficulty_util.tl:149` |
| Często | 4,4 % | około 16 latach | – | `difficulty_util.tl:37` |
| Bardzo często | 8,8 % | około 8 latach | Bardzo wysoki | `difficulty_util.tl:176` |

Szansa to 0,011 na rok × 0, 1, 2, 4 lub 8 (`mod.script.tl:171`, `mod.script.tl:202-203`, `difficulty_util.tl:37`). Zakłady należące do ciebie nigdy się nie zamykają, tak samo zakłady z ręcznym rozwojem i żaden zakład w samouczku (`industries.script.tl:94-102`).

```engine
Co liczy się jako „załadowane” i „zużyte” (logi itemsLoaded i itemsConsumed, np. czy liczy się towar premiujący), flaga manualDevelopment i dlaczego zakłady z zajezdnią są pomijane (`industries.script.tl:140-146`), zależy od silnika. Tak samo, co silnik robi z regułą premii, która straciła wejście (Przybywa wył.).
```

## Nowe zakłady

Silnik dodaje nowe zakłady w trakcie gry. Powiadomienie to **Założono nowy zakład przemysłowy**: „Śmiały przedsiębiorca wyczuł okazję do zarobku i założył zakład przemysłowy {industry}.” (`industry_spawn.script.tl:34-36`, `industry_spawn.res.lua:6`). Żaden skrypt gry nie wybiera miejsca, typu ani czasu i żaden nie filtruje tego, co proponuje silnik.

Co skrypty dają silnikowi (`mod.script.tl:128-133`, `mod.script.tl:166-168`, `mod.script.tl:194-195`):

| Wartość konfiguracji | Wartość | Znaczenie |
|---|---|---|
| spawnTargetTimeSpan | 50 × 365,25 standardowych dni | nazwany „czasem docelowym”: 50 standardowych lat czasu gry |
| spawnProbabilityExponent | 3,0 | wykładnik szansy pojawienia się (wzór w silniku) |
| spawnIndustries | wył. w edytorze map, wł. w grze | brak nowych zakładów w edytorze map |
| industryDensity | 1 × **Docelowe zagęszczenie przemysłu** | docelowa liczba zakładów |
| maxNumberPerArea, absoluteMinimum | 0,8 na km² (0,64 na konsolach), 24 | używane też przez generator map |

**Docelowe zagęszczenie przemysłu** („Ustaw docelowe zagęszczenie zakładów przemysłowych na mapie.”): 5 stopni, ×2/3, ×5/6, ×1, ×1,2, ×1,5 (`difficulty_util.tl:55`, `difficulty_util.tl:85`).

- Jest w ustawieniach zaawansowanych, w części ekonomii (`advanced_settings.tl:287-291`), i nie należy do ustawień wstępnych od Niski do Bardzo wysoki (`difficulty_util.tl:90-199`).
- W menu nowej gry **Zagęszczenie przemysłu** (zakłady na starcie, te same 5 mnożników) ustawia **Docelowe zagęszczenie przemysłu** na ten sam stopień (`new_game_or_map_settings_page.tl:159-166`, `new_game_react_util.tl:288-296`). Jeśli chcesz, by się różniły, zmień potem cel w ustawieniach zaawansowanych.
- **Żadne ustawienie tego nie wyłącza**: najniższy stopień to ×2/3. Tylko edytor map nie ma nowych zakładów. Mody to potrafią.
- Szybkość: czas docelowy jest w standardowych dniach, jak wszystkie reguły czasu gry, więc szybkość kalendarza ani wstrzymany kalendarz nie powinny go spowalniać. Zmierzone przy wstrzymanym kalendarzu: w 1809 s czasu gry pojawiły się 3 nowe zakłady, co 760 s i 728 s, więc wstrzymany kalendarz ich nie zatrzymuje. Zmierzone za pomocą [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) w 3 grach (około 500 nowych zakładów): nowe zakłady pojawiały się co około **730 s** czasu gry przy każdej szybkości kalendarza (×4, ×1, ×0,5, ×0,25). To około 45 dni kalendarza przy ×0,25 i 2 lata przy ×4.
- Poszukiwania zasobu (niżej) używają tego samego wywołania silnika z miastem, więc w silniku istnieje pojawienie się „koło miasta” (`company.script.tl:202`). Używa go też samouczek (`tutorial_init.tl:23-24`).

```engine
Wzór stojący za 50 latami i wykładnikiem 3, sposób liczenia docelowego zagęszczenia (na obszar mapy, na miasto?), wybór typu i miejsca (makeIndustrySpawnProposal) zależą od silnika. Żaden skrypt nie wyjaśnia, dlaczego kilka zakładów jednego typu może pojawić się blisko siebie („dziewięć kopalni węgla obok siebie”) ani dlaczego niektóre pojawiają się na drugim końcu mapy.
```

### Poszukiwania zasobu

Atut firmy **Poszukiwania zasobu** szuka nowego zakładu tego zasobu koło wybranego przez ciebie miasta: jedna próba na miesiąc, z szansą rosnącą od 20 % do 60 %, przez 6 miesięcy (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`). Jeśli zasób ma kilka typów zakładów, są próbowane w losowej kolejności (`company.script.tl:185-206`). Jeśli wszystkie próby się nie udadzą, zezwolenie wraca (`company.script.tl:106-110`).

## Warto wiedzieć

- Wywoź z każdego zakładu surowcowego, który ma rosnąć: niewywieziona produkcja blokuje rozbudowę, niezależnie od premii.
- Dawaj towar premiujący największym kopalniom i gospodarstwom: partia kosztuje tyle samo, bonus rośnie z parcelami.
- Zapasy się nie psują: możesz dostarczyć towar premiujący z góry, do limitu zapasu (100).
- Premie zwiększają hałas i zanieczyszczenie: Kopalnia węgla przechodzi z 10 zanieczyszczenia na 20 z jedną premią i 30 z dwiema (`coal_mine.con.lua:99-117`).
- Mniej nowych zakładów: ustaw **Docelowe zagęszczenie przemysłu** na najniższy stopień w ustawieniach zaawansowanych; nie da się ustawić zera.
- Przy ustawieniu domyślnym nieużywany zakład zamyka się rzadko; przy Bardzo często ładuj coś od czasu do czasu.

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 5 lat, nie 10, a produkcja się nie liczy: tylko towar załadowany do pojazdu lub zużyty. Po 5 latach zakład jest tylko kandydatem: co roku jest oznaczany z szansą od 1,1 % (Rzadko) do 8,8 % (Bardzo często). Odliczanie trwa 730 dni, jak podano. Towar premiujący daje od +50 % do +150 % na zakład, w partiach działających 3 miesiące. Nowe zakłady: brak ustawienia wł./wył., tylko Docelowe zagęszczenie przemysłu od ×2/3 do ×1,5; żadnych w edytorze map.
result: differs
```
