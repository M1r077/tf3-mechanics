---
title: Ulice, tory, mosty i sygnalizatory
summary: Prędkość, cena i utrzymanie każdego typu toru i ulicy, ile kosztują i na co pozwalają mosty, tunele, przejazdy i sygnalizatory, co naprawdę zmieniają aleje i ekrany akustyczne oraz gdzie opisano zajezdnie.
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40444
fact: 100 / 160 / 350 km/h | tory podstawowe, standardowe i dużych prędkości
fact: ×9 | cena i utrzymanie torów dużych prędkości w porównaniu z torami podstawowymi
fact: +30 % | ceny toru za sieć trakcyjną
fact: -65 % | hałasu ulicy lub toru z ekranem akustycznym
---

Każdy typ ulicy i toru ma prędkość maksymalną, cenę za metr i utrzymanie za metr i rok, wszystko zapisane w jego pliku. Mosty, przejazdy i niektóre dekoracje ulic dodają własne ograniczenie prędkości. Poniższe koszty dotyczą ustawień **Koszty infrastruktury** i **Utrzymanie infrastruktury** na 100 % (patrz [Koszty, utrzymanie i kredyty](costs.html)).

## Tory

| Tor | Od | Prędkość maksymalna | Budowa za km | Utrzymanie za km i rok | Źródło |
|---|---|---|---|---|---|
| Tory podstawowe | start | 100 km/h | 60 000 | 10 000 | `simple.street_template.lua:9`, `simple.street_template.lua:28`, `simple.street_template.lua:33` |
| Tory standardowe | 1930 | 160 km/h | 180 000 | 30 000 | `standard.street_template.lua:4`, `standard.street_template.lua:11`, `standard.street_template.lua:30`, `standard.street_template.lua:35` |
| Tory dużych prędkości | 1980 | 350 km/h | 540 000 | 90 000 | `high_speed.street_template.lua:4`, `high_speed.street_template.lua:11`, `high_speed.street_template.lua:30`, `high_speed.street_template.lua:35` |

- **Sieć trakcyjna** kosztuje **30 %** więcej niż tor (`mod.script.tl:24-25`). Jest dostępna od 1921 na torach podstawowych i od początku każdego nowszego typu (`simple_catenary.street_template.lua:4`). W plikach nie kosztuje nic dodatkowo rocznie: wariant elektryczny ma to samo utrzymanie (`simple_catenary.street_template.lua:34`).
- Wszystkie trzy typy pozwalają na te same nachylenia i łuki: **8,5 %** przy budowie (suwak Pochyłość sięga do tej wartości), najwyżej 13 % dla kształtu toru oraz promień łuku 55 m przy budowie, co najmniej 40 m (`standard.street_template.lua:36-37`, `standard.street_template.lua:48-49`, `construction_react_util.tl:241-242`, `construction_react_util.tl:1824`).
- Zanieczyszczenie samego toru rośnie z typem: 2, 4 i 6 (`simple.street_template.lua:18`, `standard.street_template.lua:20`, `high_speed.street_template.lua:20`).

```engine
O ile łuk obniża prędkość pociągu (speedCoeffs każdego typu toru) i jaką prędkość narzędzie budowy pokazuje dla łuku, liczy silnik.
```

```tip scripts
Tory dużych prędkości kosztują 9 razy więcej niż tory podstawowe, przy budowie i co roku. Kładź je tylko tam, gdzie pociągi naprawdę jeżdżą szybciej niż 160 km/h; gdzie indziej wystarczą tory standardowe, a dla wolnych bocznic towarowych tory podstawowe.
```

## Ulice

| Ulica | Lata | Prędkość maksymalna | Budowa za km | Utrzymanie za km i rok | Źródło |
|---|---|---|---|---|---|
| Wąska ulica (stara) | do 1940 | 20 km/h | 36 000 | 6 000 | `town_old_xsmall.street_template.lua:4-5`, `town_old_xsmall.street_template.lua:8`, `town_old_xsmall.street_template.lua:27`, `town_old_xsmall.street_template.lua:56` |
| Mała ulica (stara) | do 1940 | 40 km/h | 60 000 | 10 000 | `town_old_small.street_template.lua:8`, `town_old_small.street_template.lua:27`, `town_old_small.street_template.lua:56` |
| Szeroka ulica (stara) | do 1940 | 60 km/h | 180 000 | 30 000 | `town_old_large.street_template.lua:8`, `town_old_large.street_template.lua:27`, `town_old_large.street_template.lua:88` |
| Wąska ulica (nowa) | od 1940 | 30 km/h | 120 000 | 20 000 | `town_new_xsmall.street_template.lua:4`, `town_new_xsmall.street_template.lua:11`, `town_new_xsmall.street_template.lua:30`, `town_new_xsmall.street_template.lua:59` |
| Mała ulica (nowa) | od 1940 | 50 km/h | 180 000 | 30 000 | `town_new_small.street_template.lua:11`, `town_new_small.street_template.lua:30`, `town_new_small.street_template.lua:59` |
| Średnia ulica (nowa) | od 1940 | 50 km/h | 360 000 | 60 000 | `town_new_medium.street_template.lua:11`, `town_new_medium.street_template.lua:30`, `town_new_medium.street_template.lua:75` |
| Szeroka ulica (nowa) | od 1940 | 60 km/h | 540 000 | 90 000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:30`, `town_new_large.street_template.lua:91` |
| Wąska szosa (stara) | do 1940 | 60 km/h | 60 000 | 10 000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:29`, `country_old_small.street_template.lua:58` |
| Wąska szosa (nowa) | od 1940 | 80 km/h | 180 000 | 30 000 | `country_new_small.street_template.lua:10`, `country_new_small.street_template.lua:31`, `country_new_small.street_template.lua:60` |
| Autostrada jednopasmowa | od 1940 | 100 km/h | 180 000 | 30 000 | `highway_new_small.street_template.lua:10`, `highway_new_small.street_template.lua:32`, `highway_new_small.street_template.lua:53` |
| Autostrada dwupasmowa | od 1940 | 120 km/h | 360 000 | 60 000 | `highway_new_medium.street_template.lua:10`, `highway_new_medium.street_template.lua:32`, `highway_new_medium.street_template.lua:61` |
| Autostrada trzypasmowa | od 1940 | 120 km/h | 540 000 | 90 000 | `highway_new_large.street_template.lua:10`, `highway_new_large.street_template.lua:32`, `highway_new_large.street_template.lua:69` |
| Tory tramwajowe (stare) | do 1910 | 40 km/h | 36 000 | 6 000 | `tram_old.street_template.lua:4-5`, `tram_old.street_template.lua:8`, `tram_old.street_template.lua:27`, `tram_old.street_template.lua:40` |
| Tory tramwajowe (nowe) | od 1925 | 100 km/h | 120 000 | 20 000 | `tram_new.street_template.lua:4`, `tram_new.street_template.lua:9`, `tram_new.street_template.lua:29`, `tram_new.street_template.lua:42` |

- **Zmiana w 1940** sprawia, że ulice miejskie są o 10 km/h szybsze, ale **trzy razy** droższe, przy budowie i co roku: mała ulica drożeje z 60 000 do 180 000 za km.
- Średnie i szerokie warianty szos kosztują 2 i 3 razy tyle co wąska, przy tej samej prędkości (`country_new_large.street_template.lua:10`, `country_new_large.street_template.lua:31`).
- Dodatki do ulicy: **buspas** +10 %, **tor tramwajowy** +20 %, **elektryczny tor tramwajowy** +40 % ceny ulicy (`mod.script.tl:24-28`).
- Gracz zwykle nie jest właścicielem ulic, nawet tych, które sam zbudował; narzędzia ulic mogą zmienić właściciela ulicy (oficjalna wiki). O tym, kto płaci za utrzymanie ulicy, decyduje silnik.

## Aleje i ekrany akustyczne

| Narzędzie | Hałas | Zanieczyszczenie | Prędkość maksymalna | Gdzie | Źródło |
|---|---|---|---|---|---|
| Narzędzie alei (drzewa) | -10 % | -50 % | **-25 %** | ulice z chodnikiem, nie na mostach ani w tunelach | `alley.edge.lua:39-40`, `alley.edge.lua:53-56` |
| Narzędzie ekranów akustycznych | -65 % | bez zmian | bez zmian | ulice i tory, nie w tunelach | `barrier_b.edge.lua:43`, `barrier_b.edge.lua:47`, `barrier_track_b.edge.lua:43` |

- Oba kosztują w swoich plikach 100 i 10 rocznie, jak ulica za metr (`alley.edge.lua:8`, `alley.edge.lua:12`, `barrier_b.edge.lua:7`, `barrier_b.edge.lua:11`).
- Typy ulic „z drzewami” i „z ekranami” w menu budowy to te same ulice z już nałożonymi dekoracjami (`town_new_medium_trees.street_template.lua:12-14`). Menu budowy sumuje ich efekty (`construction_react_util.tl:2119-2142`).
- Ulica z drzewami jest więc **o jedną czwartą wolniejsza**: nowa średnia ulica z drzewami pozwala na około 38 km/h zamiast 50.

```tip scripts
Przeciw hałasowi używaj ekranu akustycznego: -65 % i bez utraty prędkości. Drzewa to narzędzie przeciw zanieczyszczeniu (-50 %), ale spowalniają ulicę o jedną czwartą.
```

Jak miasta oceniają hałas i zanieczyszczenie: [Zanieczyszczenie i hałas](emission.html).

## Mosty i tunele

| Most | Lata | Prędkość maksymalna | Dla | Cena bazowa | Źródło |
|---|---|---|---|---|---|
| Most kamienny | od startu | 90 km/h | tory, ulice | 200 | `stone.bridge.lua:169-170`, `stone.bridge.lua:181-183`, `stone.bridge.lua:193` |
| Most kratownicowy | do 1970 | 60 km/h | jeden typ dla torów, jeden dla ulic | 100 | `trestle.bridge.lua:200-201`, `trestle.bridge.lua:212-214`, `trestle.bridge.lua:226`, `trestle_s.bridge.lua:212` |
| Most stalowy | od 1940 | 140 km/h | tory, ulice | 200 | `steel.bridge.lua:243`, `steel.bridge.lua:259`, `steel.bridge.lua:269` |
| Most wiszący | od 1940 | 180 km/h | tory, ulice | 600 | `suspension.bridge.lua:277`, `suspension.bridge.lua:294`, `suspension.bridge.lua:304` |
| Most betonowy | od 1970 | 280 km/h | tory, ulice | 200 | `concrete.bridge.lua:162`, `concrete.bridge.lua:176`, `concrete.bridge.lua:187` |
| Most wantowy | od 2000 | 220 km/h | tory, ulice | 750 | `cable.bridge.lua:214`, `cable.bridge.lua:231`, `cable.bridge.lua:240` |
| Most podwieszony | od 2010 | 350 km/h | tory, ulice | 650 | `tarch.bridge.lua:253`, `tarch.bridge.lua:270`, `tarch.bridge.lua:280` |

- Ograniczenie mostu działa **dodatkowo** do ograniczenia toru: linia dużych prędkości na moście stalowym jedzie tam 140 km/h. Przed 1970 żaden most nie pozwala na więcej niż 180 km/h, przed 2010 żaden na 350 km/h.
- **Tunele** (Tunel kamienny, Tunel betonowy od 1970) nie mają w plikach **żadnego ograniczenia prędkości** i mają tę samą cenę bazową 600 (`tunnel_a.tunnel.lua:187-188`, `tunnel_a_car.tunnel.lua:185`, `tunnel_b.tunnel.lua:191-194`).
- Ceny mostów i tuneli podlegają ustawieniu Koszty infrastruktury (`post_run_util.tl:50-51`).

```engine
Cenę bazową mostu lub tunelu silnik przelicza na cenę za metr, z wysokością lub głębokością (costFactors); oficjalna wiki mówi, że zależy ona od długości oraz wysokości nad ziemią lub głębokości pod nią. Ta sama cena bazowa może więc dać bardzo różne rachunki. Tunele kosztują miasto Reputację (patrz [Reputacja](reputation.html)).
```

```tip scripts
Dla szybkiej linii przez dolinę przed 1970 most wiszący (180 km/h) jest jedynym mostem szybszym niż 140 km/h; tunel nie ma żadnego ograniczenia.
```

## Przejazdy kolejowe i sygnalizatory

| Co | Lata | Prędkość maksymalna toru | Cena | Źródło |
|---|---|---|---|---|
| Prosty przejazd kolejowy | 1850 - 1925 | 120 km/h | 4 000 | `era_a_eu.rcr.lua:14-17`, `era_a_eu.rcr.lua:26` |
| Przejazd kolejowy ze szlabanem połówkowym | 1925 - 1975 | 160 km/h | 16 000 | `era_b_eu.rcr.lua:15-18`, `era_b_eu.rcr.lua:27` |
| Współczesny przejazd kolejowy ze szlabanem połówkowym | od 1975 | 160 km/h | 16 000 | `era_c_eu.rcr.lua:15-17`, `era_c_eu.rcr.lua:26` |
| Sygnalizator (semafor do 1950, świetlny od 1950) | wszystkie | - | 9 000, utrzymanie 1 500 rocznie | `signal_path_a.con.lua:4-5`, `signal_path_a.con.lua:10-11`, `signal_path_c.con.lua:4-5` |

- Przejazd kolejowy ogranicza tor najwyżej do 160 km/h: linie dużych prędkości potrzebują mostów lub tuneli nad ulicami.
- Każdy sygnalizator można ustawić na **Jeden kierunek** (`signal_path_a.con.lua:51-52`). Jak sygnalizatory dzielą tor na odcinki, wyjaśnia strona Railway Signals oficjalnej wiki.

## Zajezdnie i stacje konserwacji

Ile kosztują zajezdnie i stacje konserwacji, ile pojazdów obsługują i w jakim promieniu: [Linie i pojazdy](vehicles.html) oraz [Koszty, utrzymanie i kredyty](costs.html).

## Warto wiedzieć

- Przed 1940 modernizacja ulic miejskich jest tania; po 1940 każda nowa lub przebudowana ulica miejska kosztuje trzy razy więcej i ma trzy razy wyższe utrzymanie.
- Na szybkiej linii sprawdź każdy most i każdy przejazd kolejowy: najwolniejszy wyznacza tam prędkość.
- Prędkość opłaca się tylko wtedy, gdy daje więcej kursów (patrz [Dlaczego tracę pieniądze?](money.html)).

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: Te same prędkości co w oficjalnych tabelach torów, ulic i mostów. W plikach ograniczenia mostów dotyczą też ulic, tunele nie mają żadnych, przejazdy kolejowe ograniczają tory do 120 lub 160 km/h, drzewa spowalniają ulicę o 25 % i zmniejszają zanieczyszczenie o 50 %, ale hałas tylko o 10 %, a ekrany akustyczne zmniejszają hałas o 65 % bez spowalniania.
result: refines
```
