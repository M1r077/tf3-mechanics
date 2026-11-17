---
title: Powiadomienia i ostrzeżenia
summary: Kiedy pojawia się każde ostrzeżenie i kiedy znika: pojazdy, które utknęły, stacje nieużyteczne lub przepełnione, problemy z liniami i przystankami, oceny miast, stan pojazdów, zamykany przemysł oraz które ostrzeżenia domyślnie nie trafiają do dziennika.
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 5 min | postoju w czasie gry, zanim pojazd zostanie zgłoszony jako unieruchomiony
fact: 20 % | stanu, który wywołuje ostrzeżenie, dopóki pojazd nie wróci powyżej 30 %
fact: 11 | typów powiadomień wyłączonych w nowej grze
fact: 75 dni | między dwoma sprawdzeniami stacji bez połączenia z drogą
---

Większość ostrzeżeń jest **trwała**: skrypt gry sprawdza sytuację raz po raz, ostrzeżenie trwa, dopóki problem istnieje, i znika samo, gdy zostanie rozwiązany. Sprawdzenia są rozłożone kolejno na 4 aktualizacje, więc ostrzeżenie może pojawić się lub zniknąć z lekkim opóźnieniem (`notifications.script.tl:13`, `notifications.script.tl:49`).

## Kiedy pojawia się każde ostrzeżenie

| Ostrzeżenie | Pojawia się, gdy | Znika, gdy | Źródło |
|---|---|---|---|
| **Pojazd utknął** | jeden z twoich pojazdów jest w drodze, nie został przez ciebie zatrzymany i ma prędkość 0 przez **5 minut** czasu gry | znowu ruszy | `notifications.script.tl:557-580` |
| **Stacja nie działa** | żaden terminal stacji nie ładuje ani nie wyładowuje pasażerów i w obszarze obsługi **nic** nie ma (żadnego magazynu, zakładu ani budynku miejskiego), a zatrzymuje się tam jedna z twoich linii | coś znajdzie się w obszarze obsługi | `notifications.script.tl:602-617`, `notifications.script.tl:630-647`, `station_useless.script.tl:39` |
| **Stacja jest przepełniona** | na stacji czeka więcej pasażerów lub towarów, niż może pomieścić (przepełnienie), a zatrzymuje się tam jedna z twoich linii; pasażerowie odchodzą | przepełnienie się skończy | `notifications.script.tl:599`, `notifications.script.tl:649-661`, `overcrowding.script.tl:23` |
| **Stan pojazdu** | twój pojazd ma stan **20 %** lub niższy | wróci powyżej **30 %** | `notifications.script.tl:310-318` |
| **Ocena miasta bardzo zła** | jedna z ocen miasta spada do poziomu Bardzo złe (poniżej 1/6) | ocena wróci do Kiepskie lub lepszej | `notifications.script.tl:230-238`, `town_util.tl:763-769`, `town_util.tl:983-985` |
| **Ocena miasta spada** | ocena jest Złe lub Kiepskie (poniżej 50 %), a nie jest objęta ostrzeżeniem Bardzo złe | ocena jest Dobre lub lepsza | `notifications.script.tl:240-248` |
| **Zamknięcie przemysłu** | zakład zaczyna odliczanie do zamknięcia | zostanie zamknięty albo na czas znowu użyty | `notifications.script.tl:439-451`, `industry_close.script.tl:53-59` |
| **Brak połączenia z drogą** | stacja nie jest połączona z drogą; sprawdzane co **75 dni** | następne sprawdzenie znajdzie drogę | `notifications.script.tl:16`, `notifications.script.tl:423-436` |
| **Problem z rozładunkiem** | towar pojazdu nigdy nie jest rozładowywany na jego linii | zostanie rozładowany | `notifications.script.tl:277-290`, `cargo_rtc_warning.script.tl:28-37` |

- Pojazd **w zajezdni** nigdy nie liczy się jako unieruchomiony: to sprawdzenie jest w skrypcie wyłączone (`notifications.script.tl:563-564`). Pojazd zatrzymany przez ciebie też nie.
- Sprawdzenie „Stacja nie działa” patrzy tylko na obszar obsługi. Stacja, na której pasażerowie już ładują się lub wysiadają przy terminalu, nigdy nie jest zgłaszana (`notifications.script.tl:606-610`).
- Jak podnieść ocenę miasta: [Rozwój miast](towns.html) i [Reputacja](reputation.html). Jak działa odliczanie do zamknięcia i jak je zatrzymać: [Przemysł](industries.html). Co stan robi z pojazdem: [Koszty, utrzymanie i pożyczki](costs.html).

```engine
To, czy stacja jest przepełniona, czy pojazd ma trasę, czy linia może dotrzeć do swoich stacji i jak długo może trwać podróż między dwoma miastami, ustala silnik (calculateStationGroupCargo, getVehicleProblems, getLineProblems, getTownProblems). Skrypty tylko zamieniają jego odpowiedzi w ostrzeżenia.
```

```tip scripts
Pojazd utknął, Problem z pojazdem, Stan pojazdu, Stacja jest przepełniona i Stacja nie jest dostępna są w nowej grze wyłączone w dzienniku. Włącz je w ustawieniach powiadomień: to właśnie one mówią o korku, brakującej trasie albo zużytej flocie.
```

## Problemy z liniami, przystankami i pojazdami

Pochodzą wprost ze sprawdzeń, które silnik wykonuje na twoich liniach i pojazdach; skrypt nadaje każdemu tytuł.

| Ostrzeżenie | Przypadki | Źródło |
|---|---|---|
| **Problem z linią** | za mało stacji; stacja dwa razy z rzędu; stacje niezgodne ze sobą; nie udało się połączyć stacji; nie udało się połączyć alternatywnych terminali | `line_warning.script.tl:46-128` |
| **Linia jest nieprawidłowo skonfigurowana** | rodzaj towaru, którego nie można nigdzie załadować albo nigdzie rozładować; żaden pojazd nie przewiezie towaru ustawionego do załadunku; pojazdy, które nie przewożą żadnego z ustawionych towarów, albo pojazdy towarowe na linii pasażerskiej; w ogóle nie ustawiono towaru | `line_warning.script.tl:15-36`, `line_warning.script.tl:133` |
| **Problem z dworcem** | przystanek, którego obecne pojazdy nie mogą używać; przystanek pasażerski używany przez pojazdy towarowe (jeden lub wszystkie); przystanek towarowy używany przez pojazdy pasażerskie; ustawiony rodzaj towaru, którego nie można załadować ani rozładować na tym przystanku | `line_station_warning.script.tl:6-87` |
| **Problem z pojazdem** | brak zelektryfikowanej trasy; brak trasy dla dużych samolotów; brak trasy dla dużych statków; brak jakiejkolwiek trasy; dwa pociągi blokujące się nawzajem | `vehicle_warning.script.tl:6-58` |
| **Miasto nie jest połączone** | droga między dwoma miastami jest przerwana; podróż między dwoma miastami trwa za długo | `town_warning.script.tl:7-19` |

- „Brak trasy dla dużych samolotów” i „Brak trasy dla dużych statków” oznaczają, że pojazd jest za duży na pas startowy, nabrzeże lub drogę wodną swojej linii: zobacz [Samoloty](aircraft.html) i [Statki](ships.html).

## Dziennik, okienka i ustawienia

- Każdy typ ostrzeżenia można wyłączyć w ustawieniach powiadomień („Konfiguruj powiadomienia”). Wyłączony typ nie dostaje okienka i nie jest zapisywany w dzienniku (`notification_util.tl:145-146`, `notification_log.tl:480`).
- W **nowej grze** 11 typów jest wyłączonych od początku: **Pojazd utknął**, **Problem z pojazdem**, **Stan pojazdu**, **Stacja jest przepełniona**, **Stacja nie jest dostępna**, **Stacja nie jest połączona**, **Miasto nie jest połączone**, **Towar nie został rozładowany** oraz komunikaty firmy o postępie Poszukiwań, Kampanii reklamowej i Zazieleniania przemysłu (`stuck_vehicle.res.lua:7`, `vehicle_warning.res.lua:8`, `noroadconnection.res.lua:8`, `vehiclecondition.res.lua:8`, `overcrowding.res.lua:8`, `station_useless.res.lua:7`, `town_warning.res.lua:8`, `cargo_rtc_warning.res.lua:8`, `notification_util.tl:32-39`).
- Jednorazowe komunikaty (nowy pojazd, nowa budowla, awans rangi, dotacje) ukrywają okienko po **60 sekundach** czasu gry; zostają w historii (`notification_util.tl:10`, `notifications.script.tl:85-94`).
- Powiadomienie kończy się też, gdy wszystko, na co wskazuje, zostało usunięte lub przebudowane (`notifications.script.tl:95-107`).
- W misji powiadomienia startują wstrzymane, dopóki misja ich nie włączy (`notifications.script.tl:700-704`).

## Warto wiedzieć

- Ostrzeżenie o unieruchomieniu po 5 minutach nie mówi dlaczego. Sprawdź pojazd: czerwony sygnał, sygnał jednokierunkowy ustawiony odwrotnie albo ostrzeżenie Problem z pojazdem dla tego samego pojazdu.
- „Stacja nie działa” znaczy tylko „jeszcze nic w obszarze obsługi”. Przesuń stację bliżej domów, zakładu lub magazynu albo ją powiększ.
- Przepełniona stacja traci pasażerów: dodaj pojazdy albo skróć interwał (zobacz [Odjazd i oczekiwanie](departure.html)).

```check
official: The official wiki's User Interface page describes the notification button, the log and its filters, without the conditions of each warning. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: Powyższe warunki: unieruchomienie po 5 minutach z prędkością 0 w drodze, stan pojazdu od 20 % do 30 %, ocena miasta Bardzo złe poniżej 1/6, połączenie z drogą sprawdzane co 75 dni, 11 typów domyślnie wyłączonych.
result: adds
```
