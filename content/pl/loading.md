---
title: Szybkość załadunku i rozładunku
summary: Od czego zależy, czy pojazd ładuje się na przystanku szybko, czy wolno: od pojazdu, od sekcji peronu i od zapasu, który oddaje lub przyjmuje towar.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-15
game: 40425
fact: ×2 | specjalistyczna sekcja peronu
fact: ×0,25 | niewłaściwa sekcja lub za długi pociąg
fact: ×4 | najlepszy przypadek: specjalistyczny peron i magazyn
---

Czas, jaki pojazd spędza na załadunku lub rozładunku, to jego własna szybkość załadunku pomnożona przez dwa mnożniki: jeden dla **peronu**, drugi dla **zapasu** po drugiej stronie (magazyn, zakład przemysłowy, miasto).

```diagram loading_factors
```

## 1. Pojazd

Każdy pojazd ma bazową szybkość załadunku, widoczną w sklepie z pojazdami i w oknie pojazdu („2.0x”). Wszystko, co opisano niżej, ją mnoży.

## 2. Mnożnik peronu

Dla gry peron nie jest rzędem modułów, lecz **listą sekcji, po jednej na każdą klasę towaru**, w której długości wszystkich modułów danej klasy są sumowane.

```diagram loading_sections
```

| Wagony… | Mnożnik | Źródło |
|---|---|---|
| na sekcji swojej klasy (wagony do towarów sypkich na sekcji do towarów sypkich) | **×2** | `modular_station.script.lua:1042` |
| na sekcji uniwersalnej | ×1 | `modular_station.script.lua:1042` |
| na peronie nie ma sekcji ich klasy | **×0,25** (stała podpowiedzi ładowania; sam mnożnik stosuje silnik) | `cargo_react_util.tl:60` |
| poza długością peronu (za długi pociąg) | **×0,25** (stała podpowiedzi ładowania; sam mnożnik stosuje silnik) | `cargo_react_util.tl:61` |

- Mnożnik jest **mieszany według udziału w pociągu**: jeśli 3/4 wagonów pasuje, a 1/4 nie, mnożnik wynosi ¾ × 2 + ¼ × 0,25 ≈ ×1,56 (`cargo_react_util.tl:63-70`; ten sam podział gra pokazuje jako „Częściowo specjalistyczny terminal”).
- **Gdzie** wagony stoją na peronie, nie ma znaczenia, liczą się tylko zsumowane długości (zmierzone w grze).
- Drogi: specjalistyczne terminale ciężarówek dają ×2 (`modular_terminal.script.lua:2956`); małe przystanki uliczne dają zawsze ×1 (`small_stops.script.lua:19`).
- Perony pasażerskie dają ×1.

## 3. Mnożnik zapasu

Przy rozładunku każda jednostka towaru trafia do odbiorcy: modułu magazynu, zakładu przemysłowego lub budynku w mieście. Zapas odbiorcy ma własny mnożnik.

| Odbiorca | Mnożnik | Źródło |
|---|---|---|
| **specjalistyczny** moduł magazynu (płyny, towary sypkie, towary niewymiarowe, produkty) | **×2** | `modules.script.lua:120`, `warehouse.script.lua:297-314` |
| magazyn **uniwersalny** | ×1 | `warehouse.script.lua:272-285` |
| zakład przemysłowy | ×1 | zmierzone w grze |

- Każdy moduł magazynu żąda ×2, ale moduły uniwersalne tylko dodają pojemność do **jednego wspólnego zapasu uniwersalnego**, który jest tworzony z ×1. Własny zapas z ×2 dostają tylko moduły specjalistyczne.
- Podpowiedź w grze nazywa ten mnożnik „Specjalistyczny magazyn: +100 %” (`cargo_react_util.tl:51-54`).
- Podczas jednego rozładunku gra obsługuje odbiorców **po kolei**, więc gdy część towaru trafia do magazynu, a część do zakładu, szybkość zmienia się w trakcie rozładunku pociągu (zmierzone w grze).

```engine
To, który odbiorca dostaje każdą jednostkę, oraz końcowe mnożenie odbywają się w silniku. Powyższe mnożniki to dane wejściowe, które przekazują mu skrypty; wynik sprawdzono na wartościach udostępnianych przez silnik (sonda moda [Platform Details](https://mod.io/g/transportfever3/m/platform-details), październik 2026).
```

## Co pokazuje gra

- Wskaźnik załadunku jest rysowany jako **przyspieszony** powyżej ×1,5 i jako **spowolniony** poniżej ×0,75 (`cargo_react_util.tl:119-122`).
- Najedź na niego kursorem: podpowiedź wymienia „Specjalistyczny terminal”, „Specjalizacje nie pasują do siebie”, „Zbyt krótki terminal” i „Specjalistyczny magazyn”, każdy z jego wartością procentową (`cargo_react_util.tl:76-99`).

## Przykład

Pociąg z 8 wagonów do towarów sypkich, o długości 160 m, rozładowuje węgiel.

| Stacja | Peron | Odbiorca | Mnożnik |
|---|---|---|---|
| peron uniwersalny 160 m | ×1 | stalownia | **×1** |
| peron do towarów sypkich 160 m | ×2 | stalownia | **×2** |
| peron do towarów sypkich 160 m | ×2 | specjalistyczny magazyn towarów sypkich | **×4** |
| peron do towarów sypkich 160 m | ×2 | magazyn uniwersalny | **×2** |
| peron uniwersalny 120 m (pociąg dłuższy o 40 m) | ¾ × 1 + ¼ × 0,25 ≈ ×0,81 | stalownia | **×0,81** |

## Gdzie towar jest rozładowywany

Każdy przystanek linii ma listę **Ładunek**, w oknie „Filtr towarów” przystanku. Na przystanku pojazd zatrzymuje na pokładzie towar z tej listy; reszta jest rozładowywana do każdego zapasu w obszarze obsługi, który ją przyjmuje, także do magazynu (zmierzone w grze).

- Tak pociąg opróżnia się do magazynu w połowie swojej linii. W grze: na przystanku obok magazynu, z samym plastikiem na liście, narzędzia z pokładu trafiły do magazynu, choć był prawie pełny.
- Peron pasażerski nie przeładowuje towarów: towar zostaje tam na pokładzie (zmierzone w grze).
- Aby zatrzymać towar na pokładzie, dodaj go do listy Ładunek tego przystanku.

```tip
**Towar znika na przystanku obok magazynu? Dodaj go do listy Ładunek tego przystanku.** Wszystko, czego nie ma na liście, jest rozładowywane do zapasu w zasięgu, a magazyn nic za to nie płaci.
```

| Opcja w „Filtr towarów” | Co robi | Źródło |
|---|---|---|
| „Wymuś rozładowanie wszystkich towarów po przybyciu” | podpowiedź: „Rozładuj towary, nawet jeśli zapasy są pełne”; co dzieje się z towarem, który się nie mieści, decyduje silnik. Wyłączona dla nowego przystanku. | `cargofilter_window.tl:757`, `line_util.tl:476` |
| „Przy zmianie konfiguracji zniszcz ładunek po przybyciu” | rozładowuje lub niszczy towar na pokładzie, gdy na tym przystanku czeka towar dla innej konfiguracji załadunku pojazdu; co z tych dwóch, decyduje silnik | `cargofilter_window.tl:767` |
| „Zastąp nowym ładunkiem, jeśli jest dostępny” | niszczy towar, który wrócił na przystanek, gdzie go załadowano, gdy czeka nowszy towar tego samego rodzaju | `cargofilter_window.tl:778` |

- Gdy pierwsza opcja jest wyłączona, ikona towaru pokazuje „≤”, a podpowiedź „Rozładuj tylko, jeśli jest miejsce” (`cargofilter_window.tl:124`, `cargofilter_window.tl:158`).

## Kilka towarów na jednej linii

- Lista **Ładunek** przystanku to tak/nie dla każdego rodzaju towaru, **bez kolejności**: gracz nie może ustawić, który towar jest ładowany jako pierwszy. Ikony są po prostu rysowane w kolejności towarów w grze (`line_util.tl:471-475`, `line_util.tl:510`, `cargofilter_window.tl:533-535`).
- Wagon lub ciężarówka przyjmujące kilka towarów mają w każdym przedziale kilka **konfiguracji załadunku**; pojemność przedziału to największa z nich, a nie ich suma (`model_metadata_util.lua:682-733`, `vehicle_metadata_util.lua:27-37`). Przewożą więc naraz tylko jedną z nich.
- Nowe pojazdy mają włączony automatyczny wybór konfiguracji dla każdego przedziału (`vehicle_react_util.tl:339`), a gra nie ma żadnego okna do ręcznego wyboru towaru pojazdu.
- Pasażerowie i towary mogą dzielić linię: skrypty nigdy nie odrzucają towaru na przystanku dlatego, że przyjmuje on też pasażerów (`line_util.tl:1381-1386`). Towar jest usuwany tylko z przystanku, którego terminal nie może ładować ani rozładowywać towarów (`line_util.tl:554-559`).
- Przy kilku towarach **Do pełna (dowolny)** i **Do pełna (wszystkie)** działają inaczej: zobacz [Ustawienia odjazdu: ładowanie do pełna, Poziom napełnienia i czasy postoju](departure.html).
- Gdy konfiguracja nie pasuje, linia pokazuje **Niektóre konfiguracje rodzajów ładunków tej linii są sprzeczne**, na przykład "Brak na linii pojazdu mogącego załadować towar pomimo skonfigurowania jego załadunku." (`line_warning.script.tl:10-36`).

```engine
O tym, w jakiej kolejności ładowanych jest kilka towarów, jak wspólny zapas jest dzielony między czekające pojazdy i jak pojazd wybiera konfigurację załadunku, decyduje silnik.
```

## Konfiguracja automatyczna

Dopóki nikt nie zapisał zmiany w oknie „Filtr towarów” przystanku, co wyłącza ją na tej linii na stałe (`line_util.tl:495-498`, `cargofilter_window.tl:438`), gra sama wypełnia listy Ładunek za każdym razem, gdy linia jest tworzona, przystanek jest dodawany lub usuwany, kolejność przystanków się zmienia albo dodawany jest punkt trasy (`manager_window.tl:6712`, `:6786`, `:6845`, `:6879`, `:6963`). Przeniesienie przystanku na inną stację lub peron oraz usunięcie lub przesunięcie punktu trasy jej nie uruchamiają (`manager_window.tl:6851-6868`, `manager_window.tl:6968-6992`).

- Zaczyna od pustych list, z pasażerami na stacjach pasażerskich (`line_util.tl:542-588`).
- Szuka producentów i odbiorców tylko wśród zakładów i budynków miejskich: magazyny się nie liczą (`cargo_util.tl:518-526`).
- Wpisuje towar na listę Ładunek przystanku, gdy towar jest potrzebny dalej, a na przystanku nic go nie przyjmuje. Magazyn liczy się tak, jakby przyjmował wszystko, co przechowuje (`line_util.tl:676-693`): na przystanku obok magazynu, który przechowuje ten towar, towar zostaje poza listą, a pociąg go tam rozładowuje.
- Gdy tylko filtr zostanie zmieniony ręcznie, linia jest oznaczona jako własna (`cargofilter_window.tl:438`) i konfiguracja automatyczna już jej nie rusza, nawet gdy później dochodzą przystanki (`line_util.tl:496`).

```engine
Skrypty tylko zapisują listy Ładunek; samo rozładowanie wykonuje silnik. Powyższą regułę (to, czego nie ma na liście, jest rozładowywane do każdego zapasu, który to przyjmuje) zaobserwowano w grze z [Platform Details](https://mod.io/g/transportfever3/m/platform-details), listopad 2026.
```

## Warto wiedzieć

- Stacje wewnątrz zakładu przemysłowego są zawsze wyspecjalizowane w towarze, którego potrzebuje ten zakład (oficjalna wiki).
- Specjalistyczne moduły magazynu dodatkowo zatrzymują licznik czasu dostawy przechowywanego towaru (oficjalna wiki); magazyn uniwersalny tego nie robi.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) pokazuje oba mnożniki dla każdego pojazdu przy peronie oraz to, dokąd trafił rozładowany towar.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Specjalistyczne magazyny "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Sekcja specjalistyczna ×2, uniwersalna ×1, brak pasującej sekcji ×0,25, poza peronem ×0,25, mieszane według udziału w pociągu; specjalistyczny moduł magazynu ×2, magazyn uniwersalny ×1.
result: refines
```
