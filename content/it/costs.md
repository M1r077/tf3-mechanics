---
title: Costi, manutenzione e prestiti
summary: Cosa cambiano le impostazioni dei costi, quali costi crescono con l'anno del calendario, come si calcola il prezzo dei veicoli e quanto costa davvero un prestito.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: ×6 | fattore dell'anno sulla manutenzione di magazzini, porti e aeroporti nel 2020
fact: 6 anni | di costi operativi: il prezzo di un veicolo
fact: una volta | il tasso di un prestito si applica all'importo, non ogni anno
fact: 4 | prestiti contemporaneamente
---

L'impostazione **Inflazione** non aumenta nessun costo: abbassa solo le tue entrate man mano che cresce il grado dell'azienda (vedi [Entrate dalle merci](income.html)). I costi crescono invece con l'**anno del calendario**, e quattro cursori li scalano fin dall'inizio.

```diagram cost_years
```

## Le impostazioni dei costi

| Impostazione | Valori | Livelli Facile · Normale · Difficile · Molto difficile | Fonte |
|---|---|---|---|
| **Costo veicoli**, **Manutenzione veicolo** | 50% · 75% · 100% · 125% · 150% | 50% · 100% · 125% · 150% | `difficulty_util.tl:39`, `difficulty_util.tl:98-99`, `difficulty_util.tl:125-126` |
| **Costi infrastrutture**, **Manutenzione infrastrutture** | 50% · 75% · 100% · 125% · 150% | 50% · 100% · 125% · 150% | `difficulty_util.tl:100-101`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Effetto manutenzione veicoli** | Nessuno ×0 · Ridotto ×0,5 · Medio ×1 · Elevato ×1,5 · Molto elevato ×2 | Ridotto · Medio · Elevato · Molto elevato | `difficulty_util.tl:42`, `difficulty_util.tl:103`, `difficulty_util.tl:185` |
| **Inflazione** | solo entrate, vedi [Entrate dalle merci](income.html) | Ridotta · Normale · Elevata · Molto elevata | `difficulty_util.tl:50`, `mod.script.tl:694-697` |

- **Costi infrastrutture** scala il prezzo di strade, binari, ponti, gallerie, incroci, edifici e moduli, e anche dei lavori sul terreno (`post_run_util.tl:23-52`, `post_run_util.tl:83-120`, `construction.script.tl:31-35`, `mod.script.tl:223-226`). Scala anche il costo di demolizione degli edifici (`construction.script.tl:39-44`). **Manutenzione infrastrutture** ne scala la manutenzione (`post_run_util.tl:43-45`, `post_run_util.tl:105-112`, `entity_window_util.tl:186`).
- **Costo veicoli** e **Manutenzione veicolo** scalano il prezzo d'acquisto e i costi operativi di ogni veicolo (`post_run_util.tl:54-81`).
- **Effetto manutenzione veicoli** stabilisce quanto un veicolo in cattive condizioni perde velocità, potenza e comfort e guadagna rumore, inquinamento e costi operativi (`mod.script.tl:241-245`).

## Cosa cresce con l'anno del calendario

- **Manutenzione degli edifici**: ×1 nel 1900, ×1,5 nel 1920, ×2,2 nel 1940, ×3,2 nel 1960, ×4 nel 1980, ×5 nel 2000, ×6 nel 2020 (`mod.script.tl:92-100`). La finestra dell'edificio e il menu di costruzione lo applicano a ogni edificio contrassegnato per seguire l'anno, e il menu di costruzione contrassegna questi: magazzini, aerodromi, aeroporti e porti (`entity_window_util.tl:186-193`, `construction_react_util.tl:1149`, `warehouse.tl:7`, `harbor_modular.tl:24`).
- I **moduli** aggiunti a un edificio del genere costano secondo l'anno in cui l'edificio è stato costruito, la loro manutenzione secondo l'anno attuale (`construction.tl:3720-3727`, `construction.tl:4364-4367`).
- **Varianti per epoca**: depositi, edifici di manutenzione, magazzini, stazioni, porti e aeroporti hanno una variante per epoca, e ogni variante successiva costa **×3** (epoca B) o **×9** (epoca C) rispetto alla prima (`rail_depot.con.lua:7`, `warehouse.tl:48`, `modular_station.con.lua:71`, `harbor_modular.tl:76`, `airport.tl:8`).
- **Denaro delle commesse**: da ×1 nel 1900 fino a ×4 dal 2000 (`finances_util.tl:87-90`). **Importo dei prestiti**: da ×0,4 nel 1900 fino a ×2,4 nel 2020 (`loan_util.tl:7-10`).
- Le **entrate** non hanno alcun fattore dell'anno (`cargo_income.script.lua:10-13`).

```engine
La manutenzione addebitata davvero, e se anche strade, binari e veicoli seguono la tabella degli anni, lo decide il motore (getCostMultiplierForYear; la configurazione base fissa solo chargeMaintenanceInterval = 60, `mod.script.tl:105`). Gli script calcolano solo i valori mostrati nelle finestre e nel menu di costruzione, con la tabella qui sopra. Nessuno script attiva il contrassegno «segui l'anno» degli altri edifici.
```

## Binari, strade ed edifici

I file di strade e binari indicano il prezzo e la manutenzione annua per metro; il menu di costruzione li mostra per chilometro (`construction_react_util.tl:2463`, `construction_react_util.tl:2477-2485`). Per la maggior parte dei tipi la manutenzione è **un sesto** del prezzo di costruzione:

| Tipo | Disponibile dal | Costruzione per km | Manutenzione per km e anno | Fonte |
|---|---|---|---|---|
| Binario semplice | inizio | 60.000 | 10.000 | `simple.street_template.lua:9`, `simple.street_template.lua:33` |
| Binario standard | 1930 | 180.000 | 30.000 | `standard.street_template.lua:11`, `standard.street_template.lua:35` |
| Binario ad alta velocità | 1980 | 540.000 | 90.000 | `high_speed.street_template.lua:11`, `high_speed.street_template.lua:35` |
| Strada di campagna vecchia piccola | inizio | 60.000 | 10.000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:58` |
| Strada urbana moderna grande | 1940 | 540.000 | 90.000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:91` |

- La catenaria aggiunge il **30%** del prezzo del binario; una corsia per autobus il 10%, un binario del tram il 20%, un binario del tram elettrico il 40% del prezzo della strada (`mod.script.tl:24-28`).
- Alzare il terreno costa 4,5 per m³, abbassarlo 5,25 per m³, entrambi × Costi infrastrutture; rimuovere un campo 200.000 (`mod.script.tl:20-22`, `mod.script.tl:33`, `mod.script.tl:225-226`).
- Un edificio che non fissa una manutenzione paga **un sesto del suo prezzo** all'anno, calcolato sul prezzo prima dell'impostazione Costi infrastrutture (`construction.script.tl:25-27`).
- La configurazione base fissa un fattore di rimborso alla demolizione di 0,75 e un tempo di rimborso di 60 (`mod.script.tl:30-31`): se demolisci quello che hai appena costruito, recuperi gran parte del denaro. Lo applica il motore.

Manutenzione annua scritta nei file, per la prima variante (prima del 1940) e le successive; i magazzini ricevono in più il fattore dell'anno visto sopra:

| Edificio | Prima variante | ×3 (dal 1940) | ×9 (dal 1980) | Fonte |
|---|---|---|---|---|
| Deposito ferroviario, deposito navale | 100.000 | 300.000 | 900.000 | `rail_depot.con.lua:34`, `water_depot.con.lua:32` |
| Deposito stradale | 30.000 | 90.000 | 270.000 | `road_depot.con.lua:32` |
| Deposito tranviario | 20.000 | 60.000 | 180.000 | `tram_depot.con.lua:34` |
| Edificio manutenzione treni o navi | 40.000 | 120.000 | 360.000 | `rail_maint_station.con.lua:32`, `water_maint_station.con.lua:32` |
| Edificio manutenzione stradale | 10.000 | 30.000 | 90.000 | `road_maint_station.con.lua:32` |
| Magazzino universale | 25.000 | 75.000 | 225.000 | `warehouse.tl:48-52`, `warehouse.tl:75` |
| Magazzino specializzato | 50.000 | 150.000 | 450.000 | `warehouse.tl:51`, `warehouse.tl:75` |

Costruire ognuno di questi edifici costa **6 ×** la sua manutenzione (`rail_depot.con.lua:35`, `warehouse.tl:76`): 2,7 M per un magazzino specializzato dell'ultima epoca, prima del fattore dell'anno.

- Il primo **aerodromo** (fino al 1950) usa già il ×3 della seconda epoca: il suo controllo legge l'anno finale della variante invece dell'anno iniziale (`airfield.tl:8`, `airfield_era_a.metacon.tl:3`).

## Veicoli

Nessun veicolo del gioco base ha un prezzo fisso: il gioco lo calcola dalla velocità e dalla capacità del veicolo quando carica il modello (`model_metadata_util.lua:488-552`):

1. **Costi operativi annui** = circa 675 × velocità media (m/s) × capacità / 4 (`model_metadata_util.lua:499-518`). Il 675 viene dalle entrate medie per km, ridotte per lasciare margine ai viaggi di ritorno a vuoto, all'acquisto e al calo dei prezzi dei biglietti (`model_metadata_util.lua:500-508`).
2. La **velocità media** è inferiore alla velocità massima (v in km/h): veicoli stradali e tram v^0,78 + 4, treni v^0,86 + 10, aerei −0,0000203 × v² + 0,17 × v + 28,36 (v al massimo 4.000), navi il 65% della velocità massima (`model_metadata_util.lua:448-474`).
3. **Treni**: un vagone conta metà della sua capacità; una locomotiva conta in più potenza ÷ velocità massima (km/h) × 12,5 come capacità, anch'essa dimezzata (`model_metadata_util.lua:511-512`, `model_metadata_util.lua:526-540`). Una locomotiva potente e lenta è costosa.
4. **Prezzo** = **6 ×** i costi operativi annui (`model_metadata_util.lua:548-549`).

Esempio al 100%: un autobus da 35 km/h per 48 passeggeri costa circa 45.000 all'anno di esercizio e circa 270.000 all'acquisto.

- Le condizioni di un veicolo hanno cinque livelli (100–80%, poi ogni 20%) (`vehicle_store_util.tl:231-234`); al **20%** il gioco lo segnala finché non torna sopra il 30% (`notifications.script.tl:310-318`).

```engine
Quanto velocemente calano le condizioni di un veicolo, quanto salgono di conseguenza i costi operativi e se i prezzi dei veicoli cambiano con l'anno sono valori del motore (getMaintenanceRunningCostPenalty e le altre penalità); gli script li scalano solo con l'Effetto manutenzione veicoli.
```

## Prestiti

```diagram loan_interest
```

| Tipo | Importo verso il 1960 (×0,4 nel 1900, ×2,4 nel 2020) | Durata | Tasso | Fonte |
|---|---|---|---|---|
| Piccolo | 5–10 M | 1–5 anni | 3–5% | `loan_util.tl:12-22` |
| Medio | 15–25 M | 3–8 anni | 5–8% | `loan_util.tl:24-34` |
| Grande | 30–50 M | 5–12 anni | 8–10% | `loan_util.tl:36-46` |
| Molto grande | 40–60 M | 10–24 anni | 10–12% | `loan_util.tl:48-58` |

- La scheda lo chiama **Tasso d'interesse annuale**, ma il tasso si applica **una sola volta** all'importo: gli interessi totali sono importo × tasso, qualunque sia la durata. Si pagano in parti uguali ogni mese insieme al capitale (`loan_util.tl:102-111`, `loan_util.tl:126-136`, `loan.script.tl:83-99`). Un prestito lungo costa quindi meno all'anno di uno breve allo stesso tasso.
- **Ripaga** paga solo il resto del capitale: gli interessi rimanenti vengono cancellati (`loan.script.tl:171-190`). Il pulsante richiede quell'importo in cassa (`finances_loan_gui.tl:284-286`).
- I tassi **non** dipendono dalla difficoltà: ogni tipo ha il suo intervallo fisso (`loan_util.tl:12-58`).
- Al massimo **4 prestiti** contemporaneamente (`loan_util.tl:4`, `loan.script.tl:134`). Un'offerta viene sostituita dopo mezzo anno; lo spazio di un prestito che hai preso resta vuoto da 4 a 8 mesi (`loan.script.tl:61-76`, `loan.script.tl:150`).
- All'inizio di una partita, ciascuno dei quattro spazi riceve i valori di un tipo casuale, quindi la prima offerta «piccola» può essere un prestito grande; una volta rinnovata l'offerta, ogni spazio propone il proprio tipo (`loan_util.tl:60-74`, `loan.script.tl:63-75`).

```tip scripts
**Prendi il prestito più lungo e ripaga presto.** Gli interessi totali sono gli stessi per ogni durata, le rate mensili sono più basse, e Ripaga cancella gli interessi rimanenti.
```

## Buono a sapersi

- Prendi il prestito **più lungo** possibile: gli interessi totali sono gli stessi, distribuiti su più mesi, e puoi ripagare prima senza pagare il resto.
- Gli edifici con varianti per epoca costano ×3 e ×9 nelle epoche successive, e la loro manutenzione continua a crescere con l'anno: un magazzino specializzato dell'ultima epoca è un grosso costo fisso.
- Un veicolo veloce e di grande capacità costa di più in esercizio, ma trasporta anche di più: prezzo e costi operativi seguono velocità × capacità, come le entrate che può generare.

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Il tasso di un prestito dipende solo dal suo tipo (3–12%), non dalla difficoltà, e si applica una volta all'importo, distribuito sui mesi della durata; ripagare prima cancella gli interessi rimanenti. L'Inflazione cambia solo le entrate; la manutenzione degli edifici segue l'anno (da ×1 a ×6); prezzo di un veicolo = 6 × i suoi costi operativi annui, entrambi ricavati da velocità e capacità.
result: differs
```
