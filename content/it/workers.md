---
title: I lavoratori e il booster dei lavoratori
summary: Come i residenti trovano lavoro in un'industria, quali contano per il booster e quanto vale il booster.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-14
fact: 10 / 20 | lavoratori necessari per il booster
fact: 2 anni | per quanto tempo conta un arrivo
fact: ×1,5–2,5 | fattore del booster, fisso per ogni industria
---

Ogni industria offre dei luoghi di lavoro. Quando arrivano abbastanza lavoratori **con le tue linee passeggeri**, l'industria produce di più. La finestra dell'industria mostra due numeri diversi, e confonderli è la causa più comune di malintesi.

```diagram workers_flow
```

## Chi può lavorare in un'industria

- Ogni industria del gioco base ha **20 luoghi di lavoro** (`industrialCapacity = 20` nel .con.lua di ogni industria).
- I luoghi di lavoro sono configurati in modo che i residenti **non possano raggiungerli a piedi né in auto**: solo le tue linee possono portarli lì (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Ogni residente ha una casa, un negozio e un lavoro. Il gioco sceglie il lavoro tra i luoghi che quel residente può raggiungere; un'industria ha un peso di destinazione di 2,0 (`industryutil.lua:455`).

```engine
Il modo in cui un residente sceglie un lavoro tra tutti i luoghi che può raggiungere (tempo di viaggio, costo, il peso di 2,0) è calcolato dal motore. Gli script forniscono solo i dati di ingresso.
```

## Lavoratori assegnati

Sono i residenti il cui lavoro è questa industria. È la barra dei luoghi di lavoro nella finestra dell'industria e la colonna **Luoghi di lavoro** delle statistiche delle industrie ("12/20") (`entity_window_util.tl:1238`, `statistic_industries.tl:305`). Essere assegnati da soli **non** attiva nulla: i lavoratori devono davvero compiere il viaggio.

## Lavoratori contati per il booster

Un piccolo script del gioco, `industry_workers.script.tl`, osserva ogni arrivo:

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

## Da sapere

- Il limite di 20 arrivi conservati e la regola del 50% fanno sì che un'industria con **più di 40 luoghi di lavoro** (possibile con le mod) non possa mai ricevere il booster dei lavoratori.
- La commessa "Trasporto di forza lavoro" viene completata quando questo booster si attiva (wiki ufficiale, Subsidies).
- Le merci booster (fertilizzanti, macchinari, strumenti) sono un booster **separato** delle industrie di materie prime, non trattato qui.
- La mod [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) mostra, nella finestra dell'industria, da quali cittadine provengono i lavoratori assegnati e quelli del booster, con frecce sulla mappa.

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: "Sufficient" = metà dei luoghi di lavoro (10 su 20); "recently" = gli ultimi 2 anni di gioco, i 20 arrivi più recenti, uno per persona, solo con le tue linee; fattore del booster da ×1,5 a ×2,5 a seconda dell'industria.
result: refines
```
