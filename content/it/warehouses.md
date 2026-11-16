---
title: Magazzini
summary: Moduli universali o specializzati, che cosa contiene ogni scorta, fissare un tipo di carico, velocità di caricamento, costi e inquinamento, e che cosa un magazzino non fa.
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
game: 40425
fact: 500 | unità di carico per modulo, di qualsiasi tipo
fact: ×2 | velocità di caricamento a un modulo specializzato, ×1 a uno universale
fact: 150.000 / 300.000 | prezzo di un modulo universale / specializzato
fact: 0 | entrate per il carico scaricato in un magazzino
---

Un magazzino è un ingresso e un insieme di **moduli**. Conserva il carico tra due linee: una linea lo scarica, un'altra lo ricarica. Le stazioni lo raggiungono tramite il loro bacino d'utenza; cittadine e industrie non ne prendono mai nulla (wiki ufficiale).

## Moduli universali o specializzati

| Modulo | Scorta | Contiene | Fattore di caricamento | Fonte |
|---|---|---|---|---|
| **Magazzino universale** | tutti i moduli universali condividono **un'unica** scorta | qualsiasi carico, misto | ×1 | `warehouse.script.lua:272-295`, `modules.script.lua:49` |
| **Magazzino liquidi**, **Magazzino merci sfuse**, **Magazzino merci ingombranti**, **Magazzino merci** | **una scorta per modulo** | un tipo di carico alla volta, della sua classe | ×2 | `warehouse.script.lua:296-314`, `modules.script.lua:120`, `modules.script.lua:165`, `modules.script.lua:247`, `modules.script.lua:296` |

- Ogni modulo aggiunge **500** unità (`modules.script.lua:49`, `modules.script.lua:120`). Cinque moduli universali formano una scorta da 2.500; cinque moduli per liquidi formano cinque scorte da 500.
- I passeggeri non vengono mai immagazzinati (`warehouse.script.lua:279`, `warehouse.script.lua:304`).
- Un modulo specializzato accetta un solo tipo di carico alla volta: per conservare petrolio greggio e carburante servono due moduli per liquidi (wiki ufficiale).
- Il ×2 di un modulo specializzato si moltiplica con il fattore della piattaforma: una piattaforma per merci sfuse e un modulo per merci sfuse danno ×4. Dettagli: [Velocità di carico e scarico](loading.html).

## Universale o specializzato?

1. **Molti tipi di carico, piccole quantità**: universale. Un'unica scorta condivisa, metà prezzo e metà inquinamento.
2. **Un solo carico in grandi quantità** (carbone, petrolio greggio, tronchi): specializzato. I veicoli lì scaricano e caricano due volte più veloci, ma serve un modulo per tipo di carico.
3. **Cibo e altri carichi con un tempo di consegna breve**: specializzato; il wiki ufficiale dice che questi moduli congelano il tempo di consegna (vedi sotto).
4. I due tipi si possono mescolare in un magazzino: i moduli universali formano sempre un'unica scorta, ogni modulo specializzato la sua.

## Un magazzino accelera lo scarico?

- **Modulo specializzato**: sì, ×2 per il carico che accetta. Il tooltip di caricamento del veicolo mostra "Magazzino specializzato: +100%" (`cargo_react_util.tl:51-54`).
- **Modulo universale**: no. La sua scorta viene creata con ×1; il ×2 chiesto dal modulo viene ignorato (`warehouse.script.lua:284`, `warehouse.script.lua:288-289`).
- Quando parte del carico va a un magazzino e parte a un'industria, il veicolo li serve a turno, quindi la velocità cambia durante una stessa fermata (misurato in gioco, vedi [Velocità di carico e scarico](loading.html)).

## La sezione Scorte

- Una riga per scorta: il carico che accetta, la quantità e, passandoci sopra con il mouse, il **Tempo consegna rimanente medio** (`entity_window_util.tl:408-410`).
- **Fissare un tipo di carico**: su un modulo specializzato, fai clic su un'icona di carico. Il gioco ricostruisce il magazzino con quel modulo riservato a quel carico (`entity_window_util.tl:339-367`, `warehouse.script.lua:308`). Rimuovere o sostituire il modulo cancella la sua scelta (`warehouse.script.lua:403-405`).
- **Scarta tutti i carichi**: svuota subito quella riga (`entity_window_util.tl:423-434`). Il carico va perso.
- Entrambi i pulsanti mancano solo in un magazzino che appartiene a un altro giocatore; i tuoi e i magazzini senza proprietario li hanno (`warehouse_eow.script.tl:127-137`, `gui/entity_window/warehouse/warehouse.tl:38`, `entity_util.tl:83-86`).
- Il grafico **Statistiche** mostra **In entrata** (scaricato) e **In uscita** (caricato) per anno (`warehouse_eow.script.tl:159-160`).

## Costi e inquinamento

| | Modulo universale | Modulo specializzato | Fonte |
|---|---|---|---|
| Prezzo | 150.000 | 300.000 | `wh_universal.module.lua:18`, `wh_liquid.module.lua:22` |
| Manutenzione annua | 25.000 | 50.000 | `wh_universal.module.lua:19`, `wh_liquid.module.lua:23` |
| Rumore | 20 | 20 | `wh_universal.module.lua:33`, `wh_liquid.module.lua:37` |
| Inquinamento | 25 | 50 | `wh_universal.module.lua:34`, `wh_liquid.module.lua:38` |

- Il magazzino aggiunge un proprio inquinamento: **25**, oppure **50** non appena viene costruito un modulo specializzato (`warehouse.script.lua:327`, `warehouse.script.lua:338-345`).
- Il menu di costruzione ha una voce per classe ed epoca (dal 1900, 1940 e 1980) (`warehouses/warehouse.tl:3-5`); le epoche successive mostrano ×3 e ×9 (`warehouses/warehouse.tl:48`, `warehouses/warehouse.tl:75-76`), e anche la manutenzione dei magazzini cresce con l'anno. Dettagli: [Costi, manutenzione e prestiti](costs.html).
- I moduli per merci sfuse, merci ingombranti e merci generiche costano quanto quelli per liquidi (`wh_bulk.module.lua:22-23`, `wh_flatbed.module.lua:22-23`, `wh_goods.module.lua:18-19`).

```engine
Gli script danno due livelli di emissione, il secondo doppio del primo (`warehouse.script.lua:342-343`); il magazzino passa dal primo al secondo man mano che le scorte si riempiono, scorte piene = il doppio (`emissions.script.tl:237-249`). Il prezzo davvero addebitato per i moduli lo calcola il motore.
```

## Che cosa un magazzino non fa

- **Non paga nulla.** Scaricare in un magazzino non dà entrate; l'unità viene pagata una sola volta, quando raggiunge il suo consumatore, per la distanza in linea d'aria dalla sua origine (misurato in gioco, vedi [Entrate dalle merci e tempi di consegna](income.html)).
- **Non rifornisce cittadine né industrie** vicine: prendono il carico solo dai veicoli (wiki ufficiale).
- **Non è una destinazione per la configurazione automatica delle linee**, che cerca solo produttori e consumatori; ma una fermata accanto a un magazzino che conserva un carico lascia quel carico fuori dalla lista Carico, quindi i treni lo scaricano lì (vedi [Velocità di carico e scarico](loading.html)).
- **Non ha bisogno di strada.** L'ingresso si aggancia a una strada, ma il carico si sposta solo attraverso i bacini d'utenza delle stazioni (`warehouse.script.lua:386-389`, wiki ufficiale). La finestra del magazzino mostra il suo bacino d'utenza (`gui/entity_window/warehouse/warehouse.tl:88-96`).

```engine
Dove va il carico scaricato, e se il tempo di consegna di un'unità immagazzinata si ferma, lo decide il motore. Nessuno script congela il tempo: il wiki ufficiale dice che i moduli specializzati lo fanno, e uno universale no.
```

## Da sapere

- Controlla la lista Carico di ogni fermata vicino a un magazzino: ciò che non c'è viene scaricato nel magazzino, anche a metà linea.
- Una scorta piena rifiuta altro carico, a meno che la fermata usi "Forza scarico di tutte le merci all'arrivo" ("Scarica le merci anche se le scorte sono piene"); cosa succede alle merci che non entrano lo decide il motore (vedi [Velocità di carico e scarico](loading.html)).
- Per tenere un modulo specializzato per un solo carico, fissa il suo tipo di carico nella sezione Scorte.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) elenca, per stazione, i magazzini raggiungibili con le loro scorte; [Platform Details](https://mod.io/g/transportfever3/m/platform-details) mostra dove è finito il carico scaricato.

```check
official: "Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types." Specialized warehouses "freeze the cargo item's delivery timer" and "enable faster loading / unloading speeds". "In specialized warehouses, only one cargo type can be stored at a time for a given module." ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: I moduli universali formano un'unica scorta condivisa con fattore di caricamento ×1, ogni modulo specializzato una scorta propria da 500 con ×2 e un solo tipo di carico. Un modulo specializzato costa il doppio (300.000, manutenzione 50.000) e inquina il doppio (50). Il congelamento del tempo non è negli script.
result: refines
```
