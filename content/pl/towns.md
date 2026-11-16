---
title: Rozwój miast: doświadczenie, oceny i wielkość
summary: Skąd miasto bierze doświadczenie, jak sześć ocen ustala tempo jego rozwoju i o ile każdy poziom je powiększa.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
game: 40425
fact: 0 % | rozwoju, gdy jedna ocena jest „Bardzo złe”
fact: ×1,5 | doświadczenia na każdy kolejny poziom (1000 na poziom 2)
fact: ×40 | wielkość po zdobyciu 17 poziomów
---

Miasto rozwija się wyłącznie dzięki **twojemu** transportowi: pasażerowie, którzy przyjeżdżają twoimi liniami, i towary dostarczone do jego budynków dają mu doświadczenie (XP). Oceny miasta decydują, jaka część tego doświadczenia się liczy, a każdy zdobyty poziom powiększa miasto.

```diagram town_xp
```

## Skąd bierze się doświadczenie

| Źródło | Bazowe XP | Źródło |
|---|---|---|
| Pasażer przybywający **twoimi liniami** do budynku w mieście | 5 · 10 · 20: dom i praca lub sklep w tym samym mieście, w sąsiednim mieście, w dalszym mieście | `town_growth.script.tl:649-701`, `town_growth_config.res.lua:6` |
| Jednostka towaru dostarczona do budynku w mieście | 10 · 20 · 40 dla towaru poziomu 0 · 1 · 2 | `town_growth.script.tl:642`, `town_growth_config.res.lua:5` |
| Nagroda za subsydium „doświadczenie miasta” | część bieżącego poziomu, również × tempo rozwoju | `subvention_util.tl:144-152`, `town_growth.script.tl:608` |

- Doświadczenie trafia do miasta, w którym stoi budynek, do którego pasażer lub towar **przybywa**. Mieszkaniec dojeżdżający do pracy między dwoma miastami daje doświadczenie obu: miastu pracy w drodze tam, miastu zamieszkania w drodze powrotnej.
- Podróże do **zakładu przemysłowego** lub z niego nie dają doświadczenia (`town_growth.script.tl:680-683`). Podróże pieszo lub samochodem też nie: liczą się tylko podróże twoimi liniami (`town_growth.script.tl:656`).
- Sam upływ czasu nic nie daje: doświadczenie za takt wynosi 0 (`town_cargo_util.tl:6`).
- Poziomy towarów: **0** cegły, cement, ryby, paliwo, mięso, deski, warzywa; **1** napoje, książki, ubrania, meble, maszyny, konserwy, narzędzia; **2** pojazdy (`placementparamsutil.lua:506-616`).

Każde bazowe XP jest mnożone przez **tempo rozwoju** miasta (`town_growth.script.tl:60-63`). Okno miasta pokazuje je jako **Stan rozwoju:**.

## Tempo rozwoju

Tempo rozwoju zależy od dwóch ocen w oknie miasta (`town_util.tl:607-633`, `town_util.tl:954-962`):

1. **Władze miejskie**: **najniższa** z sześciu ocen miasta, a nie średnia (`town_util.tl:754-784`).
2. **Zaopatrzenie**: średnia poziomów zaopatrzenia w pasażerów i towary, zaokrąglona w górę (`town_util.tl:555-589`).

```diagram growth_matrix
```

- Każda ocena ma sześć poziomów: wartość 0–1 jest dzielona na szóste części (`town_util.tl:983-985`). Poziom **„Znakomite”** wymaga 5/6 = 83 % lub więcej.
- Gdy **jedna** ocena jest na poziomie „Bardzo złe”, władze miejskie też są „Bardzo złe”, a tempo rozwoju wynosi **0 %**: miasto stoi w miejscu, cokolwiek dostarczasz.
- 100 % wymaga władz „Znakomite” przy zaopatrzeniu „Bardzo dobre” lub lepszym albo władz „Bardzo dobre” przy zaopatrzeniu „Znakomite”.
- Twoja **centrala** dodaje +5 % najbliższemu miastu, kilka rozbudów dodaje +5 %, niektóre mniej lub nic; wartość jest w pliku każdego modułu (`headquarter.script.tl:510-515`, `landmark_util.tl:51-70`). Ta premia mnoży tempo, więc przy 0 % nic nie daje.

```tip scripts
**Miasto przestało rosnąć? Najpierw popraw jego najgorszą ocenę.** Władze miejskie to najniższa z sześciu ocen: jedna ocena „Bardzo złe” trzyma miasto na 0 %, a poprawa pozostałych nic nie zmienia.
```

## Sześć ocen władz miejskich

| Ocena | Co ją obniża | Źródło |
|---|---|---|
| **Reputacja** | kształtowanie terenu, wyburzanie budynków w mieście, usuwanie drzew lub skał, nieudane dotacje; każde przerwane główne połączenie z innym miastem −1/3 | `town_util.tl:396-404`, `town_util.tl:1608`, `town_react_util.tl:30-43` |
| **Ruch drogowy** | zakorkowane ulice w mieście | `town_util.tl:445-456` |
| **Zadowolenie** | udział niezadowolonych podróżnych (przyjmuje się co najmniej 15 osób) | `town_util.tl:479-503` |
| **Dostawa** | udział spóźnionych dostaw towarów (patrz [Przychód z towarów](income.html)) | `town_util.tl:505-519` |
| **Hałas** | hałas w mieście: 65 dB lub mniej → pełna ocena, 80 dB → 0 | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Zanieczyszczenie** | średnie zanieczyszczenie na komórkę 16 m obszaru miasta, w skali logarytmicznej skryptów („dB”, to nie poziom dźwięku): 60 → pełna, 74 → 0 | `town_util.tl:413-431`, `emission_config.tl:23-24` |

Ustawienia **wrażliwości** przesuwają te progi: Reputacja ma tylko „Wył.” / „Wł.”, pozostałe pięć ma siedem stopni od „Wył.” do „Skrajnie duża”, a „Normalna” to ×1 (Hałas i Zanieczyszczenie sięgają wyżej: do ×3,5 i ×5, wobec ×3 u pozostałych); „Wył.” oznacza zawsze pełną ocenę (`difficulty_util.tl:44-49`).

## Zaopatrzenie

- **Pasażerowie**: obciążenie linii w mieście × 2, więc **50 % obciążenia linii daje pełną ocenę** (`town_util.tl:546-553`).
- **Towary**: zaopatrzenie ÷ popyt każdej dzielnicy (mieszkalnej, handlowej, przemysłowej), wszystkie jej towary razem; liczy się **najlepsza** dzielnica, a nie średnia (`town_util.tl:521-543`).
- Miasto, któremu nie ma czego dostarczać, liczy się jako w pełni zaopatrzone. Miasto, które nie dostaje od ciebie ani pasażerów, ani towarów, liczy się jako „bez dostaw”: tempo rozwoju 0 % (`town_util.tl:565-588`).

```tip scripts
**Nie potrzebujesz wszystkich mieszkańców na swoich liniach: 50 % wykorzystania daje już pełną ocenę pasażerów.**
```

Nowe zapotrzebowania na towary pojawiają się wraz z poziomami (`placementparamsutil.lua:618-660`): jedno handlowe i jedno przemysłowe na starcie, drugie handlowe na poziomie 5, drugie przemysłowe na poziomie 7, trzecie handlowe na poziomie 9, trzecie przemysłowe na poziomie 11. Są dodawane dopiero wtedy, gdy miasto otrzymało co najmniej jedną dostawę towaru (`town_growth.script.tl:286-288`). Gra woli towary, o które prosi niewiele innych miast (`town_growth.script.tl:258-266`).

## Poziomy i wielkość

- Poziom 2 wymaga 1000 XP, każdy kolejny 1,5 raza więcej niż poprzedni (`town_cargo_util.tl:81-97`, `town_growth_config.res.lua:7`): poziom 5 przy łącznie 8125 XP, poziom 10 przy około 75 000, poziom 18 („Duża metropolia”, ostatni) przy około 2 milionach.
- Miasta umieszczone z większą liczbą domów startują wyżej: od poziomu 2, 3 lub 4 (`town_cargo_util.tl:43-54`).
- **Wielkość docelowa** zależy od poziomów zdobytych od startu, łącznie z postępem w kierunku następnego (`town_cargo_util.tl:100-110`, `town_growth_function.tl:4-11`):

```diagram town_size
```

- Przyrost wielkości jest dzielony między dzielnice mieszkalne, handlowe i przemysłowe według tego, jak dobrze każda jest obsługiwana: pasażerowie dla mieszkań, zaopatrzenie w towary dla pozostałych (`town_growth.script.tl:404-421`). Gdy dzielnica zajmuje 40 % miasta, jej maksymalny udział w nowej wielkości spada ze 100 % do 50 % w miarę, jak dochodzi do 50 % miasta (podobne limity obowiązują dla całej mapy) (`town_growth.script.tl:509-522`). Jeśli żadna dzielnica nie jest obsługiwana, miasto nie rośnie, nawet mając doświadczenie (`town_growth.script.tl:415`).

```engine
Silnik oblicza obciążenie linii, prędkość ruchu, mapy hałasu i zanieczyszczenia oraz listę spóźnionych dostaw, a także buduje nowe domy i ulice. Najmniejszy udział, jaki dzielnica zawsze dostaje (townGrowthMinDistrictFraction), to wartość silnika.
```

## Popyt na towary i zapasy budynków

- Popyt miasta to suma jego **budynków**. Każdy budynek ma mały zapas wejściowy na każdy towar, o który prosi jego dzielnica: pojemność ÷ 4, zaokrąglona w górę, × współczynnik tego towaru w potrzebach miasta (1, chyba że ustawiono inaczej; skąd bierze się współczynnik, nie ma w skryptach) (`townbuildingutil.lua:226-251`). Każdy towar określa townConsumptionFactor równy 1, 0,5 lub 0,25 (`placementparamsutil.lua:506-616`); jak trafia on do budynku, leży po stronie silnika. Gra zaznacza, że ta wielkość zapasu „is currently nowhere shown in the UI” (obecnie nie jest nigdzie pokazywana w interfejsie) (`townbuildingutil.lua:249`).
- Popyt w oknie miasta to łączny limit tych zapasów; zaopatrzenie liczone do oceny jest ograniczone do popytu (`town_util.tl:95-99`, `town_util.tl:194-198`). Większe miasta proszą o więcej, bo mają więcej budynków.
- Okno budynku pokazuje **Współczynnik zużycia**: jak szybko budynek zużywa swój towar w porównaniu z maksimum (`town_building.tl:103-132`).
- Doświadczenie i zapłata przychodzą, gdy jednostka trafia do zapasu budynku (`town_growth.script.tl:620-642`).
- Przystanek obejmuje tylko budynki w swoim obszarze obsługi. Ich zapasy mogą być pełne, choć miastu jako całości wciąż brakuje towaru: wtedy towar, który się nie mieści, **zostaje w pojeździe**, chyba że zaznaczono **Wymuś rozładowanie wszystkich towarów po przybyciu** („Rozładuj, nawet jeśli zapas jest pełny.”) (`cargofilter_window.tl:757-763`), co niszczy to, co się nie mieści (patrz [Szybkość załadunku i rozładunku](loading.html)).
- Towar pozostały na pokładzie wywołuje powiadomienie **Problem z rozładunkiem**: „Nie rozładowano {cargoCount} szt. ładunku pojazdu {vehicle}.” (`cargo_rtc_warning.script.tl:28-41`, `cargo_rtc_warning.script.tl:37`); jego etykieta typu to **Towar nie został rozładowany** (`cargo_rtc_warning.res.lua:6`).
- **Popyt na towary w mieście** („Wybierz maksymalną liczbę towarów wymaganych przez miasto.”): 2, 4 lub 6, domyślnie 2 (`difficulty_util.tl:54`, `difficulty_util.tl:83`, `mod.script.tl:173`, `mod.script.tl:205`). Skrypty dodają zapotrzebowania według poziomu (patrz wyżej) i przekazują tę wartość silnikowi.

```engine
To, jak szybko budynek zużywa swój zapas (consumeFrequency), który budynek w obszarze obsługi dostaje każdą jednostkę, co dzieje się z towarem wożonym w kółko i jak silnik używa ustawienia Popyt na towary w mieście, leży po stronie silnika.
```

## Czy mogę powstrzymać rozwój miasta?

- W normalnej grze **nie ma ustawienia** maksymalnej wielkości miasta (`difficulty_util.tl:90-199`).
- W **trybie piaskownicy** okno miasta ma kartę **Docelowa pojemność dzielnic** z opcją **Włącz rozwój miast** (`town_eow.script.tl:1041-1052`, `town_eow.script.tl:1170-1171`, `town_eow_editor_initial_capacity.res.lua:6`). Po jej odznaczeniu miasto nie dostaje doświadczenia i nie zmienia wielkości; okno pokazuje **Rozwój miasta nieaktywny** (`town_growth.script.tl:28`, `town_growth.script.tl:345`, `town_eow.script.tl:107`).
- Bez piaskownicy pozostają tylko sposoby pośrednie: miasto rośnie wyłącznie dzięki twoim pasażerom i towarom, a jedna ocena „Bardzo złe” je zatrzymuje (patrz wyżej).

## Warto wiedzieć

- **Najpierw popraw najgorszą ocenę**: władze miejskie to minimum, więc poprawianie pozostałych nic nie daje.
- Pasażerowie między **dwoma miastami** dają 2 razy (sąsiednie) lub 4 razy (dalsze) więcej doświadczenia niż podróże wewnątrz jednego miasta, i to obu miastom.
- Towary handlowe mają tylko poziom 0–1; 40 XP za jednostkę dają tylko **pojazdy** (towar przemysłowy), a miasto zwykle prosi o nie dopiero od trzeciego zapotrzebowania przemysłowego (poziom 11).
- Miasto daleko od twojej centrali nie dostaje jej premii: dostaje ją tylko najbliższe miasto.

```check
official: "A town needs 1,000 total XP to reach level 2. The XP required for each following level-up is 1.5 times the amount required for the previous level-up." Pasażerowie 5 / 10 / 20 XP, towary 10 / 20 / 40 XP. "The Town Authority rating is determined by the lowest of six ratings." "A line usage of 50% gives the maximum rating." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Te same liczby. Tempo rozwoju 0–100 % w krokach po 20 % z władz miejskich × zaopatrzenia; jedna ocena „Bardzo złe” zatrzymuje rozwój; podróże do zakładów przemysłowych nie dają doświadczenia; zapotrzebowania na towary dodawane dopiero po pierwszej dostawie towaru; w podstawowej grze trzecie zapotrzebowanie handlowe nie może mieć poziomu 2 (brak handlowych towarów poziomu 2); wielkość ×40 po zdobyciu 17 poziomów.
result: refines
```
