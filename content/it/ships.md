---
title: Navi e porti
summary: Navi piccole e grandi, quale porto accoglie quale, terminal e costi dei porti, e l'elenco di tutte le navi con merci, capacità e velocità.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
game: 40425
fact: 2 | dimensioni delle navi: piccola e grande
fact: 1, 2, 4 | terminal per porto
fact: 27 | navi nel gioco base
fact: ×9 | prezzo e manutenzione della variante di porto del 1990
---

Ogni nave è **piccola** o **grande**. Una nave grande può attraccare solo in un **porto grande**; una nave piccola attracca in entrambi. Lo dice anche la guida del gioco: "Nota bene: le navi grandi possono attraccare esclusivamente nei porti grandi."

```diagram ship_access
```

## Porti piccoli e grandi

- Due porti nel menu di costruzione: **Porto passeggeri/merci piccolo** e **Porto passeggeri/merci grande**. Entrambi accettano passeggeri e tutte le merci (`harbor_modular.tl:92`, `harbor_modular.tl:122`).
- Il porto piccolo è fatto di moli piccoli, che accettano solo navi piccole (`small_pier.module.lua:7`). Il porto grande usa moli medi, che accettano entrambe le dimensioni (`medium_pier.module.lua:6`, `harbor_modular.script.lua:35-39`).
- **Terminal**: 1, 2 o 4, scelti alla costruzione (`harbor_modular.tl:16`, `harbor_modular.script.lua:33`).
- Un terminal di molo accoglie 100 passeggeri in attesa su un molo piccolo e 50 su un molo medio (`modules.script.lua:872`, `modules.script.lua:1004`).
- Mentre posizioni un porto, lo script mostra solo il livello dell'acqua navigabile (`harbor_modular.tl:26-30`). Dove un porto si può posizionare lo decide il motore di gioco.
- Ogni nave stabilisce la propria dimensione nel suo file del veicolo; il gioco la trasforma nella modalità nave piccola o grande (`model_metadata_util.lua:1411-1412`).

## Costi

C'è una variante di porto per epoca: 1900, 1950 e 1990 (`harbor_modular.tl:71-73`). Prezzo e manutenzione sono moltiplicati per 3 per una variante dal 1940 e per 9 per una dal 1980 (`harbor_modular.tl:76`):

| Porto | Prezzo (prima variante) | Manutenzione annua (prima variante) | Fonte |
|---|---|---|---|
| Porto piccolo | 144.000 - 444.000 | 24.000 - 74.000 | `harbor_modular.tl:88-89` |
| Porto grande | 228.000 - 678.000 | 38.000 - 113.000 | `harbor_modular.tl:118-119` |

- I due valori sono la configurazione più piccola e quella più grande.
- Anche la manutenzione dei porti segue l'anno del calendario, da ×1 nel 1900 a ×6 nel 2020, come magazzini e aeroporti ([Costi, manutenzione e prestiti](costs.html)).
- I porti sono rumorosi e inquinanti: da 180 a 280 per entrambi ([Inquinamento e rumore](emission.html)).
- Prezzo e costi di esercizio di una nave sono calcolati da velocità e capacità, come per i veicoli stradali e gli aerei ([Costi, manutenzione e prestiti](costs.html)).

## Tutte le navi

Velocità in km/h, arrotondata. "Merci" elenca le classi di merci del file del veicolo; "qualsiasi merce" indica ogni tipo di merce. La capacità è il totale mostrato dal negozio dei veicoli: la somma dei compartimenti, ciascuno con la sua configurazione di carico più grande (`vehicle_store_util.tl:70-95`).

| Nave | Anni | Dimensione | Merci | Capacità | Velocità | Velocità di carico |
|---|---|---|---|---|---|---|
| Dunara Castle | 1875-1930 | grande | passeggeri, qualsiasi merce | **160** (2 × 80) | 20 | 20 |
| Battello da pesca canadese | 1884-1948 | piccola | qualsiasi merce | 40 | 35 | 10 |
| Waimarie | 1889-1940 | piccola | passeggeri | 80 | 30 | 15 |
| Sydfart | 1900-1930 | piccola | liquidi, merci ingombranti, merci, merci sfuse | 80 | 30 | 20 |
| PS Trillium | 1910-1955 | grande | passeggeri | 200 | 35 | 15 |
| Battello a ruota di poppa | 1915-1960 | piccola | passeggeri, qualsiasi merce | **120** (2 × 60) | 40 | 10 |
| Terra Nova | 1925-1975 | grande | merci sfuse, merci ingombranti, merci | **200** (2 × 100) | 45 | 30 |
| Spintore cisterna Votrans | 1935-1990 | piccola | liquidi | 120 | 33 | 20 |
| Spintore da carico Votrans | 1935-1990 | piccola | merci sfuse, merci ingombranti, merci | 120 | 33 | 20 |
| MS Stadt Kiel | 1943-1990 | piccola | passeggeri | 80 | 30 | 20 |
| Borealis | 1948-1994 | piccola | qualsiasi merce | 60 | 38 | 20 |
| Wopper | 1950-2005 | piccola | liquidi, merci ingombranti, merci, merci sfuse | 160 | 30 | 25 |
| Meridian Ferry | 1956-2011 | piccola | passeggeri | 240 | 30 | 15 |
| Cap Arkona | 1965-2010 | grande | passeggeri | 200 | 40 | 20 |
| Nave da cabotaggio Tora | 1970-2020 | grande | liquidi, merci ingombranti, merci, merci sfuse | 320 | 40 | 25 |
| AP1-88 Hovercraft | 1980- | piccola | passeggeri | 240 | 90 | 15 |
| Spintore Hercules XI | 1990- | grande | merci ingombranti, merci, merci sfuse | **240** (2 × 120) | 32 | 20 |
| Baltica | 1994- | piccola | qualsiasi merce | 80 | 40 | 20 |
| HADAG Type 2000 | 1995- | piccola | passeggeri | 100 | 35 | 25 |
| Damen Tanker 800 | 1996- | piccola | liquidi | **320** (2 × 160) | 28 | 30 |
| Damen Fast Ferry | 2003- | grande | passeggeri | 220 | 75 | 20 |
| Luise Deymann | 2013- | grande | liquidi | **480** (2 × 240) | 30 | 35 |
| MS Diamant | 2013- | grande | passeggeri | 280 | 45 | 35 |
| Spintore Virgo | 2015- | grande | merci ingombranti, merci, merci sfuse | **320** (2 × 160) | 40 | 15 |
| GHL Oita Hovercraft | 2023- | piccola | passeggeri | 320 | 100 | 20 |
| Yara Birkeland | 2030- | grande | merci ingombranti, merci, merci sfuse | 480 | 42 | 10 |
| Solar Shuttle | 2035- | piccola | passeggeri | 80 | 30 | 30 |

## Buono a sapersi

- **Controlla la dimensione prima di costruire un porto piccolo.** Diverse delle navi da carico più grandi (Tora, Virgo, Yara Birkeland) sono grandi e lì non attraccheranno.
- **"Nessun percorso per grandi navi"** è un avviso a parte per le navi grandi: il gioco non ha trovato alcun percorso sull'acqua utilizzabile da una nave grande. Quale acqua è aperta a quale dimensione lo decide il motore di gioco, non gli script, che mostrano solo l'avviso (`vehicle_warning.script.tl:28-36`).
- **Le tappe delle navi** vanno posizionate sull'acqua ("Le tappe navali devono essere sull'acqua.").
- Il deposito navale e la stazione di manutenzione navale sono edifici separati; la manutenzione agisce in un raggio intorno a essi ([Veicoli: condizione, età e velocità di carico](vehicles.html)).

```check
official: "Passenger and cargo ships are available in two sizes: small and large. Large ships can only dock at large harbors, so make sure the harbor matches the size of the ships assigned to the line." (in-game guide "Water Infrastructure")
scripts: Uguale: i moli piccoli accettano solo SMALL_SHIP, quelli medi SHIP e SMALL_SHIP; entrambi i porti accettano passeggeri e tutte le merci; 1, 2 o 4 terminal; tre varianti d'epoca a ×1 / ×3 / ×9; 16 navi piccole e 11 grandi nel gioco base.
result: refines
```
