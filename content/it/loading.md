---
title: Velocità di carico e scarico
summary: Che cosa fa caricare un veicolo velocemente o lentamente a una fermata: il veicolo, le sezioni della piattaforma e le scorte che cedono o ricevono il carico.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-14
fact: ×2 | sezione di piattaforma specializzata
fact: ×0,25 | sezione sbagliata o treno troppo lungo
fact: ×4 | caso migliore: piattaforma e magazzino specializzati
---

Il tempo che un veicolo impiega a caricare o scaricare è la sua velocità di caricamento moltiplicata per due fattori: uno per la **piattaforma**, uno per le **scorte** dall'altra parte (magazzino, industria, cittadina).

```diagram loading_factors
```

## 1. Il veicolo

Ogni veicolo ha una velocità di caricamento di base, mostrata nel Negozio veicoli e nella finestra del veicolo ("2.0x"). Tutto ciò che segue la moltiplica.

## 2. Il fattore della piattaforma

Per il gioco una piattaforma non è una fila di moduli: è un **elenco di sezioni, una per classe di carico**, con le lunghezze di tutti i moduli di quella classe sommate.

```diagram loading_sections
```

| Vagoni… | Fattore | Fonte |
|---|---|---|
| su una sezione della loro classe (vagoni per merci sfuse, sezione per merci sfuse) | **×2** | `modular_station.script.lua:1042` |
| su una sezione universale | ×1 | `modular_station.script.lua:1042` |
| senza alcuna sezione della loro classe sulla piattaforma | **×0,25** | `cargo_react_util.tl:60` |
| oltre la lunghezza della piattaforma (treno troppo lungo) | **×0,25** | `cargo_react_util.tl:61` |

- Il fattore è una **media pesata sulla quota del treno**: se 3/4 dei vagoni corrispondono e 1/4 no, il fattore è ¾ × 2 + ¼ × 0,25 ≈ ×1,56 (`cargo_react_util.tl:63-70`, la stessa suddivisione che il gioco mostra come "Terminal parzialmente specializzato").
- **Dove** si fermano i vagoni sulla piattaforma non conta, contano solo le lunghezze sommate (misurato in gioco).
- Strada: i terminal per camion specializzati danno ×2 (`modular_terminal.script.lua:2956`); le piccole fermate su strada sono sempre ×1 (`small_stops.script.lua:19`).
- Le piattaforme per passeggeri sono ×1.

## 3. Il fattore delle scorte

Allo scarico, ogni unità va a un destinatario: un modulo di magazzino, un'industria o un edificio della cittadina. Le scorte del destinatario hanno il loro fattore.

| Destinatario | Fattore | Fonte |
|---|---|---|
| modulo di magazzino **specializzato** (liquidi, merci sfuse, merci ingombranti, merci generiche) | **×2** | `modules.script.lua:120`, `warehouse.script.lua:297-314` |
| magazzino **universale** | ×1 | `warehouse.script.lua:272-285` |
| industria | ×1 | misurato in gioco |

- Ogni modulo di magazzino chiede ×2, ma i moduli universali aggiungono solo capacità a **un'unica scorta universale condivisa**, che viene creata con ×1. Solo i moduli specializzati hanno una scorta propria con ×2.
- Il tooltip del gioco chiama questo fattore "Magazzino specializzato: +100%" (`cargo_react_util.tl:51-54`).
- Durante uno stesso scarico il gioco serve i destinatari **a turno**: per questo la velocità cambia mentre il treno scarica, quando parte del carico va a un magazzino e parte a un'industria (misurato in gioco).

```engine
Quale destinatario riceve ogni unità, e la moltiplicazione finale, sono decisi dal motore. I fattori qui sopra sono i dati che gli script gli forniscono; il risultato è stato verificato con i valori che il motore espone (sonda di [Platform Details](https://mod.io/g/transportfever3/m/platform-details), ottobre 2026).
```

## Che cosa mostra il gioco

- L'indicatore di caricamento appare come **accelerato** sopra ×1,5 e come **rallentato** sotto ×0,75 (`cargo_react_util.tl:119-122`).
- Passaci sopra con il mouse: il tooltip elenca "Terminal specializzato", "Specializzazioni non corrispondenti", "Terminal troppo corto" e "Magazzino specializzato", ciascuno con la sua percentuale (`cargo_react_util.tl:76-99`).

## Esempio

Un treno di 8 vagoni per merci sfuse, lungo 160 m, che scarica carbone.

| Stazione | Piattaforma | Destinatario | Fattore |
|---|---|---|---|
| piattaforma universale di 160 m | ×1 | acciaieria | **×1** |
| piattaforma per merci sfuse di 160 m | ×2 | acciaieria | **×2** |
| piattaforma per merci sfuse di 160 m | ×2 | magazzino specializzato per merci sfuse | **×4** |
| piattaforma per merci sfuse di 160 m | ×2 | magazzino universale | **×2** |
| piattaforma universale di 120 m (treno più lungo di 40 m) | ¾ × 1 + ¼ × 0,25 ≈ ×0,81 | acciaieria | **×0,81** |

## Da sapere

- Le stazioni all'interno di un'industria sono sempre specializzate per il carico di cui quell'industria ha bisogno (wiki ufficiale).
- I moduli di magazzino specializzati congelano anche il tempo di consegna del carico che conservano (wiki ufficiale); un magazzino universale no.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) mostra entrambi i fattori per ogni veicolo a una piattaforma, e dove è finito il carico scaricato.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Specialized warehouses "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Sezione specializzata ×2, universale ×1, nessuna sezione corrispondente ×0,25, oltre la piattaforma ×0,25, media pesata sulla quota del treno; modulo di magazzino specializzato ×2, magazzino universale ×1.
result: refines
```
