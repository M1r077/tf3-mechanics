---
title: Aeroplani, aeroporti ed elicotteri
summary: Aerodromo o aeroporto, quale aeroplano atterra dove, terminal, la seconda pista, eliporti, e l'elenco di tutti i velivoli con merci, capacità e velocità.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
fact: 2 | dimensioni degli aeroplani: piccolo e grande
fact: 1950 | primo aeroporto e primi elicotteri
fact: 1980 | seconda pista
fact: 5 | velivoli per hangar
---

Ogni aeroplano è **piccolo** o **grande**. Un **aerodromo** accetta solo aeroplani piccoli; un **aeroporto** accetta entrambi, e gli elicotteri presso l'edificio principale. Gli elicotteri hanno anche stazioni proprie.

```diagram air_access
```

## Aerodromo e aeroporto

- **Aerodromo**: "Aerodromo dotato di una pista per velivoli piccoli." Varianti del 1920, 1950 e 1980; 1, 2 o 3 terminal e un deposito opzionale (`airfield.tl:49`, `airfield.tl:76`, `airfield_era_a.metacon.tl:3`).
- **Aeroporto**: "Aeroporto dotato di una o due piste per velivoli piccoli e grandi." Varianti del 1950 e 1980; 2, 3 o 4 terminal e una direzione di atterraggio (`airport.tl:24`, `airport.tl:80`, `airport1950.metacon.tl:3-4`).
- I terminal dell'aerodromo accettano solo aeroplani piccoli; quelli dell'aeroporto accettano entrambe le dimensioni (`af_terminal.module.lua:715`, `ap_terminal.module.lua:897`).
- L'edificio principale dell'aeroporto ha piazzole per elicotteri (`ap_main.module.lua:532`), e dal 1950 un aeroporto può avere un terminal per elicotteri (`ap_terminal_heli.module.lua:897`, `ap_terminal_heli.module.lua:971`).
- **Seconda pista**: un modulo dell'aeroporto dal 1980 (`airport_2nd_runway.module.lua:5`). Alcuni moduli dell'aeroporto la richiedono e senza di essa mostrano "Seconda pista necessaria" (`airport.script.lua:261`).
- Tutte le stazioni aeree accettano passeggeri e tutte le merci (`airfield.tl:59`, `airport.tl:34`).

| Edificio | Passeggeri in attesa | Fonte |
|---|---|---|
| Terminal dell'aerodromo | fino a 250 | `af_terminal.module.lua:773` |
| Edificio principale dell'aeroporto | fino a 400 | `ap_main.module.lua:667` |
| Terminal dell'aeroporto | fino a 850 | `ap_terminal.module.lua:951` |
| Terminal elicotteri dell'aeroporto | fino a 450 | `ap_terminal_heli.module.lua:990` |

## Hangar e stazioni per elicotteri

- Un **hangar** di aerodromo o aeroporto ospita 5 velivoli e ne esegue la manutenzione in un raggio di 550 m (`af_hangar.module.lua:273-278`, `ap_hangar.module.lua:456-461`).
- **Eliporto** (dal 1950): acquista e mantiene gli elicotteri, deposito da 5, raggio di manutenzione 800 m (`heliport.script.lua:301-306`).
- **Elisuperficie** (dal 1950): una piccola piazzola di atterraggio per passeggeri e merci, senza deposito (`helipad.con.lua:29-33`).

## Costi

Prezzo e manutenzione della prima variante. Le varianti successive costano ×3 o ×9 ([Costi, manutenzione e prestiti](costs.html)); il primo aerodromo usa già ×3 (`airfield.tl:8`).

| Edificio | Prezzo | Manutenzione annua | Fonte |
|---|---|---|---|
| Aerodromo | 1.200.000 - 3.000.000 | 50.000 - 200.000 | `airfield.tl:55-56` |
| Aeroporto | 1.800.000 - 4.500.000 | 300.000 - 750.000 | `airport.tl:30-31` |
| Modulo dell'aerodromo (edificio principale, terminal, hangar) | 600.000 | 100.000 | `af_main.module.lua:316-317`, `af_hangar.module.lua:326-327` |
| Modulo dell'aeroporto (terminal, hangar, seconda pista) | 900.000 | 150.000 | `ap_main.module.lua:672-673`, `ap_hangar.module.lua:508-509`, `airport_2nd_runway.module.lua:27-28` |

- Anche la manutenzione di aeroporti e aerodromi segue l'anno del calendario, da ×1 nel 1900 a ×6 nel 2020 ([Costi, manutenzione e prestiti](costs.html)).
- Prezzo e costi di esercizio di un velivolo sono calcolati da velocità e capacità, come per le navi e i veicoli stradali ([Costi, manutenzione e prestiti](costs.html)).

## Tutti gli aeroplani

Velocità in km/h, arrotondata. "Qualsiasi merce" indica ogni tipo di merce. La capacità è il totale mostrato dal negozio dei veicoli: la somma dei compartimenti, ciascuno con la sua configurazione di carico più grande (`vehicle_store_util.tl:70-95`).

| Aeroplano | Anni | Dimensione | Merci | Capacità | Velocità | Velocità di carico |
|---|---|---|---|---|---|---|
| Junkers F 13 Herta | 1920-1950 | piccolo | passeggeri | 16 | 135 | - |
| Vickers J6860 Victoria | 1922-1960 | piccolo | qualsiasi merce | 32 | 150 | 2,5 |
| Fokker F VII A | 1925-1960 | piccolo | passeggeri | 32 | 175 | 2 |
| Junkers JU-52 Iron Annie | 1933-1982 | piccolo | passeggeri, qualsiasi merce | **48** (2 × 24) | 200 | 3 |
| Douglas DC-3 | 1935-1995 | piccolo | passeggeri | 56 | 300 | 2,5 |
| Curtiss C-46 Commando | 1942-1980 | piccolo | qualsiasi merce | 80 | 280 | - |
| Douglas DC-4 | 1944-1998 | piccolo | passeggeri | 100 | 365 | 3 |
| Bristol Type 170 cargo | 1949-2005 | piccolo | passeggeri, qualsiasi merce | **80** (2 × 40) | 350 | 1,5 |
| Lockheed L-1049 Super connie | 1952-1986 | grande | passeggeri | 120 | 486 | 3 |
| Lockheed L-1049D/H Super connie | 1959-2000 | grande | qualsiasi merce | **120** (2 × 60) | 486 | 2,5 |
| De Havilland DH.106 Comet | 1960-2000 | grande | passeggeri | 160 | 724 | 3 |
| Canadair CL-44 cargo | 1962-2005 | grande | qualsiasi merce | **144** (3 × 48) | 645 | 2 |
| Convair CV 990 Coronado | 1962-2020 | grande | passeggeri | 200 | 917 | 2 |
| Lockheed L-100 Hercules | 1976-2000 | piccolo | qualsiasi merce | **132** (3 × 44) | 400 | 3 |
| McDonnell Douglas DC-10-30 | 1978- | grande | passeggeri | 400 | 960 | 2,5 |
| McDonnell Douglas DC-10-30CF | 1978- | grande | qualsiasi merce | **396** (3 × 132) | 960 | 4 |
| Airbus A310 300F cargo | 1982- | grande | qualsiasi merce | 160 | 850 | 3 |
| Short 330 Sherpa | 1984- | piccolo | passeggeri, qualsiasi merce | **80** (2 × 40) | 455 | 2,5 |
| Airbus A320 | 1985- | grande | passeggeri | 180 | 753 | 3 |
| British Aerospace 146 | 1985- | piccolo | passeggeri | 112 | 753 | 3 |
| Br. Aerospace 146 cargo | 1985- | piccolo | qualsiasi merce | **96** (2 × 48) | 753 | 2 |
| Fokker 100 | 1988- | grande | passeggeri | 160 | 845 | 3,5 |
| Tupolev Tu-204 | 1995- | grande | passeggeri | 280 | 850 | 4 |
| Tupolev Tu-204C cargo | 1995- | grande | qualsiasi merce | **204** (3 × 68) | 850 | 2 |
| Boeing 737-700 | 1998- | grande | passeggeri | 200 | 974 | 2,5 |
| Boeing 737-700-C cargo | 1998- | grande | qualsiasi merce | **160** (2 × 80) | 974 | 3 |
| Bombardier DHC-8 | 2000- | piccolo | passeggeri | 120 | 648 | 3 |
| Bombardier DHC-8 cargo | 2008- | piccolo | qualsiasi merce | 120 | 648 | 2 |
| Sukhoi Superjet 100 | 2011- | piccolo | passeggeri | 160 | 870 | 3 |
| Airbus Canada A220 | 2013- | grande | passeggeri | 180 | 830 | 5 |

## Tutti gli elicotteri

| Elicottero | Anni | Merci | Capacità | Velocità | Velocità di carico |
|---|---|---|---|---|---|
| Bell 47 | 1950-1990 | passeggeri, qualsiasi merce | 8 | 150 | 2 |
| Piasecki H-21 Workhorse | 1952-1985 | passeggeri, qualsiasi merce | 80 (48 merci) | 210 | 3 |
| Sikorsky S-64 Skycrane | 1962-2017 | qualsiasi merce | 40 | 213 | 4 |
| Bell 206 Long Ranger | 1965-2025 | passeggeri | 32 | 241 | 2,5 |
| Boeing Vertol 234 Chinook | 1980- | passeggeri, qualsiasi merce | 80 | 269 | 2 |
| AgustaWestland AW101 Merlin | 1990- | passeggeri | 60 | 278 | 3 |
| Mil Mi-26TC | 1993- | qualsiasi merce | 120 | 295 | 4 |
| Eurocopter 120B Colibri | 1998- | passeggeri | 48 | 210 | 3 |
| Kaman K-MAX | 2005- | qualsiasi merce | 60 | 190 | 3 |
| Airbus H225 Super Puma | 2013- | passeggeri | 48 | 288 | 3 |
| NextGen VTOL | 2030- | passeggeri | 56 | 610 | 4 |

## Buono a sapersi

- **Gli aeroplani piccoli restano utili fino alla fine.** Il DHC-8, la sua versione cargo e il Sukhoi Superjet 100 sono piccoli, quindi basta loro un aerodromo.
- **Prima del 1952 non esiste alcun aeroplano grande**, quindi un aeroporto costruito presto non dà ancora accesso a velivoli più grandi.
- Gli aeroplani volano in linea retta e il pagamento conta solo la distanza in linea d'aria, quindi una deviazione non costa loro nulla in più ([Entrate dalle merci e tempi di consegna](income.html)).
- La lunghezza minima della pista, le rotte di volo e l'atterraggio sono decisi dal motore di gioco; gli script non li mostrano.

```check
official: "It can be used by small airplanes." (Airfield) "It can be used by small and large airplanes." (Airport), build menu descriptions.
scripts: Uguale: i terminal dell'aerodromo accettano solo SMALL_AIRCRAFT, quelli dell'aeroporto AIRCRAFT e SMALL_AIRCRAFT, elicotteri presso l'edificio principale dell'aeroporto, eliporto ed elisuperficie dal 1950, seconda pista dal 1980, hangar da 5; 15 aeroplani piccoli e 15 grandi e 11 elicotteri nel gioco base.
result: agrees
```
