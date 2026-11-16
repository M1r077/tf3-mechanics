---
title: Pojazdy: stan, wiek i szybkość załadunku
summary: Co oznaczają statystyki pojazdów, jak działają stan i wiek, co robią bazy i stacje konserwacji, skąd biorą się cena i koszty eksploatacji oraz kiedy wymienić pojazd.
domain: vehicles
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-16
game: 40425
fact: 5 | poziomów stanu, od Bardzo zły do Bardzo dobry, po 20 %
fact: 20 % | stanu, przy którym pojawia się ostrzeżenie Stan pojazdu
fact: 6 lat | kosztów eksploatacji: cena pojazdu
fact: 4 do 16 | pojazdów w puli konserwacji jednej bazy lub stacji konserwacji
---

Każdy pojazd ma stałe statystyki (prędkość, pojemność, szybkość załadunku, cena, koszty eksploatacji, okres trwałości) i dwie zmieniające się wartości: **stan** i **wiek**. Stan spada podczas jazdy i jest przywracany przez konserwację. Wiek tylko rośnie.

## Statystyki w sklepie z pojazdami

- Sklep pokazuje każdą statystykę jako pasek. Pasek porównuje pojazd z innymi tego samego rodzaju transportu i epoki, a nie ze stałą skalą (`vehicle_util.tl:210-245`, `vehicle_util.tl:248-270`).
- Dla pociągu sklep pokazuje **najwyższą** szybkość załadunku spośród wszystkich jego części (`vehicle_store_util.tl:333`).
- Pojazd, którego plik nie ustawia szybkości załadunku, hałasu, zanieczyszczenia ani komfortu, dostaje wartość obliczoną z pozostałych statystyk (rok, prędkość, moc, masa, rozmiar) (`model_metadata_util.lua:395-417`, `vehicle_metadata_util.lua:233-256`). Obliczona szybkość załadunku jest zaokrąglana do 0,5 i nigdy nie jest niższa niż 1 (`vehicle_metadata_util.lua:267-269`).

## Który pojazd ładuje najszybciej?

Szybkość załadunku pojazdu to tylko pierwszy czynnik; peron i zapas ją mnożą (patrz [Szybkość załadunku i rozładunku](loading.html)).

| Rodzaj transportu | Szybkość załadunku pokazana jako pełny pasek (ostatnia epoka) | Źródło |
|---|---|---|
| Statki | 10 do 45 (od 2003) | `vehicle_util.tl:219-223` |
| Pojazdy drogowe, tramwaje | 0,5 do 10 (od 1995) | `vehicle_util.tl:232-243` |
| Pociągi | 0,1 do 10 (od 1981) | `vehicle_util.tl:226-229` |
| Samoloty | 1 do 4 (od 1978) | `vehicle_util.tl:212-216` |

- Statki mają zdecydowanie najwyższe szybkości załadunku, samoloty najniższą skalę.
- Porównuj pojazdy jednego rodzaju transportu w sklepie w kolumnie szybkości załadunku; nowsze modele zwykle są wyżej na pasku.
- Każdy towar ma współczynnik załadunku 0,0625, pasażerowie 1 (`coal.cargo.lua:29`, `passengers.cargo.lua:23`).

```engine
Jak szybkość załadunku pojazdu, współczynnik załadunku towaru oraz mnożniki peronu i zapasu łączą się w rzeczywisty czas załadunku, oblicza silnik. Skrypty podają tylko dane wejściowe.
```

## Stan

| Stan | Poziom | Źródło |
|---|---|---|
| powyżej 80 % | **Bardzo dobry** | `vehicle_util.tl:159-172` |
| 60–80 % | **Dobry** | `vehicle_util.tl:159-172` |
| 40–60 % | **Kiepski** | `vehicle_util.tl:159-172` |
| 20–40 % | **Zły** | `vehicle_util.tl:159-172` |
| do 20 % | **Bardzo zły** | `vehicle_util.tl:159-172` |

- Stan pociągu to **średnia** wszystkich jego wagonów i lokomotyw (`vehicle_util.tl:285-295`).
- Poniżej 80 % pojazd zaczyna tracić prędkość maksymalną, moc i komfort, a zyskiwać hałas, zanieczyszczenie i koszty eksploatacji (`vehicle_store_util.tl:230-259`). Okno pojazdu wymienia te kary w sekcji **Stan techniczny**.
- Siłę tych kar ustawia **Wpływ konserwacji pojazdów** („Brak”, „Niski”, „Średni”, „Wysoki”, „Bardzo wysoki”); przy „Brak” stan nie ma wpływu (`mod.script.tl:241-245`, `vehicle_store_util.tl:211-228`). Szczegóły: [Koszty, utrzymanie i kredyty](costs.html).
- Przy **20 %** lub mniej pojawia się ostrzeżenie **Stan pojazdu**. Pozostaje, dopóki pojazd nie wróci powyżej **30 %** (`notifications.script.tl:310-318`).
- Sklonowany pojazd to nowy zakup: stan 100 %, nowa data zakupu (`manager_window.tl:8502-8506`).

```engine
Jak szybko spada stan, ile przywraca wizyta w stacji konserwacji i wielkość każdej kary (getMaintenanceTopSpeedPenalty i pozostałe) to wartości silnika. Każdy model pojazdu może też ustawić własną karę prędkości maksymalnej na poziom (`vehicle_store_util.tl:250-253`).
```

## Bazy i stacje konserwacji

Pojazdy są konserwowane przez pobliską bazę lub stację konserwacji. Każda obsługuje ograniczoną liczbę pojazdów: swoją **Pulę konserwacji**.

| Budynek | Pula konserwacji | Promień | Pojazdy w bazie | Źródło |
|---|---|---|---|---|
| Baza kolejowa | 6 | 800 m | 5 | `rail_depot.script.lua:341-349` |
| Kolejowa stacja konserwacji | 12 | 800 m | – | `rail_maint_station.script.lua:151-157` |
| Baza drogowa, baza tramwajowa | 12 | 400 m | 10 / 8 | `road_depot.script.lua:189-198`, `tram_depot.script.lua:217-226` |
| Drogowa stacja konserwacji | 16 | 600 m | – | `road_maint_station.script.lua:234-240` |
| Stocznia | 8 | 1000 m | 5 | `water_depot.script.lua:370-379` |
| Wodna stacja konserwacji | 12 | 1400 m | – | `water_maint_station.script.lua:256-262` |
| Hangar lotniska lub portu lotniczego | 16 | 550 m | 5 | `af_hangar.module.lua:272-280`, `ap_hangar.module.lua:455-463` |
| Lądowisko dla helikopterów | 4 | 800 m | 5 | `heliport.script.lua:300-309` |

- Okno budynku pokazuje „zajęte / pula” (na przykład 14 / 12) i listę obsługiwanych pojazdów wraz z ich stanem (`entity_window_util.tl:2010-2039`, `maintenance_station_eow.script.tl:188-215`).
- Pełniejsza pula sprawia, że budynek jest głośniejszy i brudniejszy: emisje rosną wraz z zajętą częścią puli (`emissions.script.tl:223-234`).
- Kolejowa stacja konserwacji obsługuje dwa razy więcej pociągów niż baza kolejowa: 12 wobec 6.
- Stacje konserwacji nie kupują ani nie przechowują pojazdów, ale ich promień jest często większy niż bazy: 600 m wobec 400 m na drogach, 1400 m wobec 1000 m dla statków. Tylko drogowa stacja konserwacji obsługuje też tramwaje.
- Oficjalna wiki radzi używać punktów trasy, by kierować pojazdy obok budynku konserwacji.

```engine
Do której stacji pojazd zostaje przypisany, co się dzieje, gdy stację używa więcej pojazdów niż wynosi jej pula, oraz używany promień obszaru obsługi, decyduje silnik.
```

## Cena i koszty eksploatacji

- Pojazdy z podstawowej gry nie mają stałej ceny: koszty eksploatacji wynikają z prędkości i pojemności, a cena to **6 lat** kosztów eksploatacji (`model_metadata_util.lua:548-549`). Pełny wzór: [Koszty, utrzymanie i kredyty](costs.html).
- **Koszty pojazdów** i **Konserwacja pojazdów** skalują się obie od 50 % do 150 % (`post_run_util.tl:54-81`).
- Pojazd w złym stanie płaci wyższe koszty eksploatacji, ponad wartość bazową (`vehicle_store_util.tl:256-259`).

## Wiek i okres trwałości

- Każdy model ma **okres trwałości** w latach (`vehicle_metadata_util.lua:79-83`). Kolumna **Wiek** w oknie linii pokazuje wiek; jej podpowiedź pokazuje pozostały czas albo **Osiągnięto koniec okresu trwałości** (`line_eow.script.tl:133-147`). Część okresu trwałości w tej podpowiedzi wynosi **0 %**, dopóki okres trwałości nie minie: skrypt zaokrągla ułamek w dół przed pokazaniem (`line_eow.script.tl:139`), a ta sama część jest gdzie indziej liczona w całości (`vehicle_util.tl:311`). Patrz raczej na pozostały czas.
- Dla pociągu liczy się **najstarsza** część (`vehicle_util.tl:36-52`). Jeden stary wagon sprawia, że cały pociąg wygląda na stary.

```engine
Co zmienia osiągnięcie okresu trwałości (na przykład szybszą utratę stanu lub niższą wartość sprzedaży), nie ma w skryptach. Skrypty tylko wyświetlają wiek i okres trwałości.
```

## Kiedy wymieniać stare pojazdy?

1. **Stan pozostaje niski** mimo pobliskiej stacji konserwacji: pojazd traci prędkość i płaci wyższe koszty eksploatacji. Najpierw sprawdź pulę stacji: może być pełna.
2. **Osiągnięto koniec okresu trwałości** w podpowiedzi Wiek: model przekroczył planowany okres eksploatacji.
3. **Istnieje lepszy model**: szybsze lub większe pojazdy kosztują więcej w eksploatacji, ale przewożą więcej (cena wynika z prędkości × pojemności).
4. Użyj **Wymień pojazdy** w menedżerze linii. Otwiera sklep z porównaniem z obecnym pojazdem (`vehicle_store_window.tl:4893-4928`, `vehicle_store_window.tl:2611`).

```tip scripts
**Pojazdy przy bazie wciąż są w złym stanie? Otwórz jej okno i sprawdź „użyte / pula”.** Baza kolejowa obsługuje 6 pociągów, kolejowa stacja konserwacji 12. Co silnik robi z pojazdami ponad pulę, nie ma w skryptach; drugi budynek to bezpieczna odpowiedź.
```

## Dobrze wiedzieć

- Zbuduj wystarczającą zdolność konserwacji: jedna baza kolejowa obsługuje tylko 6 pociągów.
- Gdy **Wpływ konserwacji pojazdów** ma wartość „Brak”, stan nie ma znaczenia.
- **Wyślij do bazy** wysyła pojazd do najbliższej osiągalnej bazy, a nie do tej, w której został kupiony (oficjalna wiki).
- [Vehicle Comparison](https://mod.io/g/transportfever3/m/vehicle-comparison) pomaga porównać modele przed ich wymianą.

```check
official: "This section shows how well the vehicle is maintained and how the maintenance state affects the vehicle properties." "Loading speed modifies a vehicle's base loading speed which can be seen in the vehicle window or in the vehicle store." ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles))
scripts: Pięć poziomów stanu po 20 %; kary do prędkości, mocy, komfortu, emisji i kosztów eksploatacji poniżej 80 %, skalowane przez Wpływ konserwacji pojazdów; ostrzeżenie przy 20 %, znika powyżej 30 %. Pula konserwacji od 4 do 16 pojazdów na budynek. Cena = 6 lat kosztów eksploatacji. Wiek pociągu = jego najstarsza część. Brakujące szybkości załadunku są obliczane z pozostałych statystyk, zaokrąglane do 0,5, co najmniej 1.
result: refines
```
