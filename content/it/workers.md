---
title: I lavoratori e il booster dei lavoratori
summary: Come i residenti trovano lavoro in un'industria, quali contano per il booster e quanto vale il booster.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-15
fact: 10 / 20 | lavoratori necessari per il booster
fact: 2 anni | per quanto tempo conta un arrivo
fact: ×1,5–2,5 | fattore del booster, fisso per ogni industria
---

Ogni industria offre dei luoghi di lavoro. Quando arrivano abbastanza lavoratori **con le tue linee passeggeri**, l'industria produce di più. La finestra dell'industria mostra due numeri diversi, e confonderli è la causa più comune di malintesi.

```diagram workers_flow
```

## Chi può lavorare in un'industria

- Ogni industria del gioco base ha **20 luoghi di lavoro** (`industrialCapacity = 20`).
- I luoghi di lavoro sono configurati in modo che i residenti **non possano raggiungerli a piedi né in auto**: solo le tue linee possono portarli lì (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Ogni residente ha una casa, un negozio e un lavoro. Il gioco sceglie il lavoro tra i luoghi che quel residente può raggiungere; un'industria ha un peso di destinazione di 2,0 (`industryutil.lua:455`).

```engine
Il modo in cui un residente sceglie un lavoro tra tutti i luoghi che può raggiungere (tempo di viaggio, costo, il peso di 2,0) è calcolato dal motore. Gli script forniscono solo i dati di ingresso.
```

## Lavoratori assegnati

Sono i residenti il cui lavoro è questa industria. È la barra dei luoghi di lavoro nella finestra dell'industria e la colonna **Luoghi di lavoro** delle statistiche delle industrie ("12/20") (`entity_window_util.tl:1238`, `statistic_industries.tl:305`). Essere assegnati da soli **non** attiva nulla: i lavoratori devono davvero compiere il viaggio.

## Lavoratori contati per il booster

Un piccolo script del gioco osserva ogni arrivo (`industry_workers.script.tl`):

1. Quando un residente arriva a un'industria e il suo **ultimo spostamento è avvenuto con le tue linee**, l'arrivo viene registrato con l'ora di gioco (`industry_workers.script.tl:86-118`).
2. Vengono conservati solo gli arrivi degli **ultimi 2 anni di gioco** (`industry_productivity_util.tl:3`: `2 * getDefaultYearDuration()`).
3. Vengono conservati al massimo i **20 arrivi più recenti** (`industry_workers.script.tl:4`, `KeepHistoryCount = 20`).
4. Quando la stessa persona arriva di nuovo, il nuovo arrivo sostituisce quello vecchio: ogni residente conta **una sola volta** (`industry_workers.script.tl:56-70`).

```diagram workers_window
```

## Quando il booster si attiva e si disattiva

- L'industria riceve il booster quando i lavoratori contati raggiungono **la metà dei luoghi di lavoro**: `contati ≥ luoghi × 0,5` (`industry_productivity_util.tl:35-48`, `RequiredWorkersFractionForBoost = 0.5`). Con 20 luoghi di lavoro: **10 lavoratori**.
- La sezione Booster della finestra dell'industria mostra esattamente questo: "contati / necessari", con il numero necessario arrotondato per eccesso (`industry_react_util.tl:627`).
- Il controllo viene ripetuto ogni volta che arrivano nuovi lavoratori o che l'arrivo più vecchio supera i 2 anni (`industry_workers.script.tl:40-43`). Per questo il booster **si disattiva da solo** circa 2 anni dopo che i lavoratori hanno smesso di arrivare.

## Quanto vale il booster

- La produzione viene moltiplicata per il **fattore del booster** dell'industria, mostrato nella finestra come "+X%" (`industry_react_util.tl:716`).
- Il fattore viene estratto una sola volta dal seme casuale dell'industria: **tra ×1,5 e ×2,5**, e non cambia mai per quell'industria (`industry_productivity_util.tl:58-72`). Un'industria senza seme usa ×2.
- Quindi due miniere identiche possono avere booster dei lavoratori diversi: controlla il "+X%" prima di scegliere quale servire.

## Esempio

Una miniera di carbone con 20 luoghi di lavoro e "+84%".

| Situazione | Contati | Booster attivo? | Produzione |
|---|---|---|---|
| Nuova linea di autobus: 14 residenti assegnati, nessuno è ancora arrivato | 0 | no | ×1 |
| 12 residenti diversi sono arrivati in autobus quest'anno | 12 | sì (≥ 10) | ×1,84 |
| Linea di autobus rimossa; nessuno arriva per 2 anni | scende a 0 | si disattiva | ×1 |

## Portare i lavoratori a un'industria

```diagram workers_trip
```

- Un lavoratore viene contato quando **arriva all'industria** stessa, la meta del suo viaggio (`targetOrAtEntity`) è l'industria e il suo ultimo modo di spostamento è **Linee** (`industry_workers.script.tl:86-94`). Scendere a una fermata non basta: la persona deve raggiungere l'industria.
- Ogni residente ha un modo di spostamento per destinazione (casa, negozio, lavoro). La finestra dell'industria elenca i lavoratori assegnati con un'icona per questo modo: **Cammina**, **Auto** o **Linee** (`entity_window_util.tl:1400-1435`). Per un'industria dovrebbe essere sempre Linee, perché a piedi e in auto lì non è permesso (`industryutil.lua:451-457`).
- Quindi "niente a piedi" vuol dire che l'intero viaggio non può essere a piedi o in auto. Non vuol dire "mai a piedi": un viaggio con Linee inizia e finisce comunque a piedi tra le fermate e gli edifici (vedi la nota sul motore sotto).
- **I cambi contano.** Lo script guarda solo il modo del viaggio, non quante linee sono state usate (`industry_workers.script.tl:91`). Un lavoratore da una città a quattro linee di distanza conta come uno della porta accanto, ma può metterci molto di più ad arrivare.
- **Qualsiasi tua linea può portarli**, anche una linea che trasporta merci, purché i suoi veicoli prendano passeggeri e la fermata carichi passeggeri. Lo script non controlla il tipo di veicolo (`industry_workers.script.tl:86-118`). I giocatori segnalano meno problemi con linee passeggeri separate.
- Alcune industrie (per esempio le piattaforme petrolifere) hanno una fermata integrata, che prende passeggeri e merci (`industryutil.lua:156-165`).
- La finestra dell'industria mostra, per ogni lavoratore assegnato, se è **In posizione** o **In viaggio** (`entity_window_util.tl:1371-1384`). La sezione Booster elenca i lavoratori contati con il loro **Tempo rimanente** sui 2 anni (`entity_window_util.tl:1579-1630`, `industry_eow.script.tl:644-649`).
- Un'industria senza ancora nessun lavoratore mostra: "Collega questo luogo al trasporto pubblico per consentire ai residenti di lavorare qui." (`entity_window_util.tl:1650-1652`).

```engine
Quale fermata serve un'industria, quanto cammina un lavoratore da una fermata all'ingresso dell'industria, e i residenti di quali città prendono il lavoro sono decisi dal motore (bacini di utenza, ricerca del percorso, scelta del lavoro). Gli script non fissano alcun limite di distanza per i lavoratori. I giocatori segnalano che una stazione il cui bacino copriva l'industria per le merci non portava lavoratori finché un autobus non è andato fino all'ingresso dell'industria (discussione Steam "Problem getting workers to site").
```

```tip
**Ottieni in fretta il potenziamento dei lavoratori (e il contratto Trasporta lavoratori): inizia con una linea semplice.**

1. Crea una **nuova linea passeggeri** da una fermata all'industria a **una sola città**.
2. Posiziona la fermata in città in modo che il suo bacino **non tocchi nessuna delle tue altre stazioni passeggeri**.
3. Un solo veicolo basta per iniziare.

I posti di lavoro vengono assegnati quando la linea apre: in due prove **tutti i 20 posti sono andati a quella sola città**, e il potenziamento è partito dopo **346 s e 925 s** di tempo di gioco (una volta con un solo veicolo). Quando la fermata in città toccava il bacino di una stazione della rete, alcuni posti sono andati a una città lontana e gli ultimi lavoratori hanno impiegato molto di più (964 s). Misurato con [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) e il [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard); chi ottiene un posto lo decide comunque il motore.
```

## Commessa Trasporto di forza lavoro

- Viene offerta solo per un'industria con posti di lavoro, il cui booster dei lavoratori non è ancora attivo e che ha spedito o ricevuto merci nell'ultimo anno, secondo i dati annuali del motore (`deliver_workers.script.tl:121-131`, `industry_util.tl:541-558`). Se basti solo ricevere dipende da come il motore compila le regole di produzione; non è negli script.
- Viene completata quando il booster dei lavoratori si attiva: gli stessi 10 arrivi diversi su 20 con le tue linee (`deliver_workers.script.tl:152-156`). Non si conta nient'altro; non c'è una regola nascosta.
- La barra di avanzamento sulla scheda del contratto è "lavoratori contati ÷ metà dei luoghi di lavoro" (`deliver_workers.script.tl:267-272`, `industry_util.tl:11-18`).
- Le frecce sulla mappa del contratto partono dalle **5 città più vicine**. Sono solo un indizio: lo script le disegna per distanza, non in base a chi ha il lavoro (`deliver_workers.script.tl:297-317`).
- Vedi [Commesse: offerte, scadenze e ricompense](subsidies.html) per soldi e scadenza.

## Perché i miei lavoratori non arrivano?

| Controllo | Dove guardare | Perché |
|---|---|---|
| Qualcuno ha il lavoro? | Barra dei luoghi di lavoro ("12/20") | Senza lavoratori assegnati nessuno viaggia. La scelta del lavoro dipende dal motore. |
| Icona del modo dei lavoratori | Elenco lavoratori: Cammina / Auto / Linee | Contano solo i viaggi con Linee (`industry_workers.script.tl:91`). |
| Si stanno muovendo? | **In viaggio** / **In posizione** | "In viaggio" a lungo: cambi lenti o sovraccarichi, o nessun percorso dall'ultima fermata. |
| L'ultima fermata raggiunge l'ingresso dell'industria? | Bacino della fermata, strada d'ingresso | Segnalato dai giocatori; dipende dal motore. Un breve autobus fino all'ingresso ha aiutato. |
| La fermata carica passeggeri? | Fermata della linea, Filtro carico | I passeggeri devono essere caricati e scaricati a entrambi i capi del viaggio. |
| 10 persone **diverse** in 2 anni? | Sezione Booster, **Tempo rimanente** | La stessa persona conta una volta; gli arrivi più vecchi escono (`industry_workers.script.tl:56-70`). |
| Più di 40 luoghi di lavoro (mod)? | Barra dei luoghi di lavoro | Con 20 arrivi conservati non può mai arrivare a metà. |

## Da sapere

- Il limite di 20 arrivi conservati e la regola del 50% fanno sì che un'industria con **più di 40 luoghi di lavoro** (possibile con le mod) non possa mai ricevere il booster dei lavoratori.
- La commessa **Trasporto di forza lavoro** viene completata quando questo booster si attiva (`deliver_workers.script.tl:152-156`).
- Le merci booster (fertilizzanti, macchinari, strumenti) sono un booster **separato** delle industrie di materie prime, non trattato qui.
- La mod [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) mostra, nella finestra dell'industria, da quali cittadine provengono i lavoratori assegnati e quelli del booster, con frecce sulla mappa.

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: "Sufficient" = metà dei luoghi di lavoro (10 su 20); "recently" = gli ultimi 2 anni di gioco, i 20 arrivi più recenti, uno per persona, solo con le tue linee; fattore del booster da ×1,5 a ×2,5 a seconda dell'industria. I cambi contano; il modo del viaggio deve essere Linee, e camminare da una fermata fa parte di un tale viaggio.
result: refines
```
