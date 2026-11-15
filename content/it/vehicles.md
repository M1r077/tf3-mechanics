---
title: Veicoli: condizione, età e velocità di carico
summary: Cosa significano le statistiche dei veicoli, come funzionano condizione ed età, cosa fanno depositi e stazioni di manutenzione, da dove vengono prezzo e costi di esercizio, e quando sostituire un veicolo.
domain: vehicles
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-16
fact: 5 | livelli di condizione, da Pessima a Ottima, 20 % ciascuno
fact: 20 % | condizione che attiva l'avviso Condizione veicolo
fact: 6 anni | di costi di esercizio: il prezzo di un veicolo
fact: da 4 a 16 | veicoli nel fondo manutenzione di un deposito o di una stazione di manutenzione
---

Ogni veicolo ha statistiche fisse (velocità, capacità, velocità di carico, prezzo, costi di esercizio, durata) e due valori che cambiano: la sua **condizione** e la sua **età**. La condizione cala mentre viaggia e la manutenzione la ripristina. L'età cresce soltanto.

## Le statistiche nel negozio dei veicoli

- Il negozio mostra ogni statistica come una barra. La barra confronta il veicolo con gli altri dello stesso mezzo di trasporto e della stessa epoca, non con una scala fissa (`vehicle_util.tl:210-245`, `vehicle_util.tl:248-270`).
- Per un treno, il negozio mostra la velocità di carico **più alta** fra tutte le sue parti (`vehicle_store_util.tl:333`).
- Un veicolo il cui file non imposta velocità di carico, rumore, inquinamento o comfort riceve un valore calcolato dalle sue altre statistiche (anno, velocità, potenza, peso, dimensioni) (`model_metadata_util.lua:395-417`, `vehicle_metadata_util.lua:233-256`). La velocità di carico calcolata è arrotondata a 0,5 e mai inferiore a 1 (`vehicle_metadata_util.lua:267-269`).

## Quale veicolo carica più in fretta?

La velocità di carico del veicolo è solo il primo fattore; piattaforma e scorta la moltiplicano (vedi [Velocità di carico e scarico](loading.html)).

| Mezzo di trasporto | Velocità di carico mostrata come barra piena (ultima epoca) | Source |
|---|---|---|
| Navi | da 10 a 45 (dal 2003) | `vehicle_util.tl:219-223` |
| Veicoli stradali, tram | da 0,5 a 10 (dal 1995) | `vehicle_util.tl:232-243` |
| Treni | da 0,1 a 10 (dal 1981) | `vehicle_util.tl:226-229` |
| Aerei | da 1 a 4 (dal 1978) | `vehicle_util.tl:212-216` |

- Le navi hanno di gran lunga le velocità di carico più alte, gli aerei la scala più bassa.
- Confronta i veicoli di uno stesso mezzo di trasporto nel negozio con la colonna della velocità di carico; i modelli più recenti di solito stanno più in alto sulla barra.
- Ogni carico merci ha un fattore di carico di 0,0625, i passeggeri 1 (`coal.cargo.lua:29`, `passengers.cargo.lua:23`).

```engine
Come la velocità di carico del veicolo, il fattore di carico del carico e i fattori di piattaforma e scorta si combinano nel tempo di carico reale lo calcola il motore. Gli script forniscono solo i dati in ingresso.
```

## Condizione

| Condizione | Livello | Source |
|---|---|---|
| oltre l'80 % | **Ottima** | `vehicle_util.tl:159-172` |
| 60–80 % | **Buona** | `vehicle_util.tl:159-172` |
| 40–60 % | **Mediocre** | `vehicle_util.tl:159-172` |
| 20–40 % | **Scadente** | `vehicle_util.tl:159-172` |
| fino al 20 % | **Pessima** | `vehicle_util.tl:159-172` |

- La condizione di un treno è la **media** di tutti i suoi vagoni e locomotive (`vehicle_util.tl:285-295`).
- Sotto l'80 % un veicolo comincia a perdere velocità massima, potenza e comfort, e ad aumentare rumore, inquinamento e costi di esercizio (`vehicle_store_util.tl:230-259`). La finestra del veicolo elenca queste penalità sotto **Condizione**.
- L'intensità di queste penalità è impostata da **Effetto manutenzione veicoli** (Nessuno, Ridotto, Medio, Elevato, Molto elevato); con Nessuno la condizione non ha effetto (`mod.script.tl:241-245`, `vehicle_store_util.tl:211-228`). Dettagli: [Costi, manutenzione e prestiti](costs.html).
- Al **20 %** o meno ricevi l'avviso **Condizione veicolo**. Resta finché il veicolo non torna sopra il **30 %** (`notifications.script.tl:310-318`).
- Un veicolo clonato è un nuovo acquisto: condizione 100 %, nuova data di acquisto (`manager_window.tl:8502-8506`).

```engine
Quanto velocemente cala la condizione, quanto ripristina una visita a una stazione di manutenzione e l'entità di ogni penalità (getMaintenanceTopSpeedPenalty e le altre) sono valori del motore. Ogni modello di veicolo può anche impostare una propria penalità di velocità massima per livello (`vehicle_store_util.tl:250-253`).
```

## Depositi e stazioni di manutenzione

I veicoli ricevono manutenzione da un deposito o da una stazione di manutenzione vicini. Ognuno serve un numero limitato di veicoli: il suo **Fondo manutenzione**.

| Edificio | Fondo manutenzione | Raggio | Veicoli ospitati | Source |
|---|---|---|---|---|
| Deposito treni | 6 | 800 m | 5 | `rail_depot.script.lua:341-349` |
| Stazione di manutenzione treni | 12 | 800 m | – | `rail_maint_station.script.lua:151-157` |
| Deposito stradale, deposito tram | 12 | 400 m | 10 / 8 | `road_depot.script.lua:189-198`, `tram_depot.script.lua:217-226` |
| Stazione di manutenzione stradale | 16 | 600 m | – | `road_maint_station.script.lua:234-240` |
| Deposito navale | 8 | 1000 m | 5 | `water_depot.script.lua:370-379` |
| Stazione di manutenzione navale | 12 | 1400 m | – | `water_maint_station.script.lua:256-262` |
| Hangar di aerodromo o aeroporto | 16 | 550 m | 5 | `af_hangar.module.lua:272-280`, `ap_hangar.module.lua:455-463` |
| Eliporto | 4 | 800 m | 5 | `heliport.script.lua:300-309` |

- La finestra dell'edificio mostra "usati / fondo" (per esempio 14 / 12) e l'elenco dei veicoli che serve, con la loro condizione (`entity_window_util.tl:2010-2039`, `maintenance_station_eow.script.tl:188-215`).
- Un fondo più pieno rende l'edificio più rumoroso e più inquinante: le emissioni salgono con la quota del fondo in uso (`emissions.script.tl:223-234`).
- Una stazione di manutenzione treni serve il doppio dei treni di un deposito treni: 12 contro 6.
- Le stazioni di manutenzione non comprano né ospitano veicoli, ma il loro raggio è spesso più grande di quello del deposito: 600 m contro 400 m su strada, 1400 m contro 1000 m per le navi. Solo la stazione di manutenzione stradale fa manutenzione anche ai tram.
- Il wiki ufficiale suggerisce dei waypoint per far passare i veicoli da un edificio di manutenzione.

```engine
A quale stazione viene assegnato un veicolo, cosa succede quando una stazione è usata da più veicoli del suo fondo, e il raggio d'utenza usato, lo decide il motore.
```

## Prezzo e costi di esercizio

- I veicoli del gioco base non hanno un prezzo fisso: i costi di esercizio derivano da velocità e capacità, e il prezzo è pari a **6 anni** di costi di esercizio (`model_metadata_util.lua:548-549`). Formula completa: [Costi, manutenzione e prestiti](costs.html).
- **Costo veicoli** e **Manutenzione veicolo** li scalano entrambi dal 50 % al 150 % (`post_run_util.tl:54-81`).
- Un veicolo in cattive condizioni paga costi di esercizio maggiori, oltre al valore base (`vehicle_store_util.tl:256-259`).

## Età e durata

- Ogni modello ha una **durata** in anni (`vehicle_metadata_util.lua:79-83`). La colonna **Età** della finestra della linea mostra l'età; il suo tooltip mostra la quota di durata già consumata e il tempo rimanente, oppure **Durata massima raggiunta** (`line_eow.script.tl:133-147`).
- Per un treno conta la parte **più vecchia** (`vehicle_util.tl:36-52`). Un solo vagone vecchio fa apparire vecchio l'intero treno.

```engine
Cosa cambia al raggiungimento della durata (per esempio una perdita di condizione più rapida o un valore di vendita più basso) non è negli script. Gli script mostrano solo età e durata.
```

## Quando sostituire i veicoli vecchi?

1. **La condizione resta bassa** anche con una stazione di manutenzione vicina: il veicolo perde velocità e paga costi di esercizio maggiori. Controlla prima il fondo della stazione: potrebbe essere pieno.
2. **Durata massima raggiunta** nel tooltip di Età: il modello ha superato la durata prevista.
3. **Esiste un modello migliore**: i veicoli più veloci o più grandi costano di più in esercizio, ma trasportano di più (il prezzo segue velocità × capacità).
4. Usa **Sostituisci veicoli** nel gestore delle linee. Apre il negozio con un confronto con il veicolo attuale (`vehicle_store_window.tl:4893-4928`, `vehicle_store_window.tl:2611`).

```tip scripts
**I veicoli restano in cattive condizioni vicino a un deposito? Apri la sua finestra e controlla che la capacità non sia piena.** Un deposito treni serve 6 treni, una stazione di manutenzione treni 12.
```

## Buono a sapersi

- Costruisci abbastanza capacità di manutenzione: un deposito treni serve solo 6 treni.
- Con **Effetto manutenzione veicoli** su Nessuno, la condizione non conta.
- **Invia a deposito** manda un veicolo al deposito raggiungibile più vicino, non a quello dove è stato acquistato (wiki ufficiale).
- [Vehicle Comparison](https://mod.io/g/transportfever3/m/vehicle-comparison) aiuta a confrontare i modelli prima di sostituirli.

```check
official: "This section shows how well the vehicle is maintained and how the maintenance state affects the vehicle properties." "Loading speed modifies a vehicle's base loading speed which can be seen in the vehicle window or in the vehicle store." ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles))
scripts: Cinque livelli di condizione del 20 %; penalità a velocità, potenza, comfort, emissioni e costi di esercizio sotto l'80 %, scalate da Effetto manutenzione veicoli; avviso al 20 %, rimosso sopra il 30 %. Fondo manutenzione da 4 a 16 veicoli per edificio. Prezzo = 6 anni di costi di esercizio. Età di un treno = la sua parte più vecchia. Le velocità di carico mancanti sono calcolate dalle altre statistiche, arrotondate a 0,5, almeno 1.
result: refines
```
