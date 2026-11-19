---
title: Commesse: offerte, scadenze e ricompense
summary: I quattro tipi di contratto, che cosa li completa davvero, che cosa ottieni e che cosa rischi, e ogni quanto arrivano nuove offerte.
domain: subsidies
official: gamemanual:management:subsidies
status: verified
updated: 2026-11-15
game: 40444
change: 40444 | Collegamento urbano: la linea che riceve il ×2 viene fissata al completamento del contratto; un passeggero conta solo dopo l'accettazione dell'offerta; qualsiasi linea diretta con un veicolo passeggeri blocca l'offerta.
fact: 4 | tipi di contratto in una partita libera
fact: 5 | contratti accettati al massimo contemporaneamente
fact: ×2 | di entrate per 5 anni sulle linee che hanno consegnato
fact: 0 | penalità per aver rifiutato un'offerta
---

Una commessa (chiamata subvention nei file del gioco) è un contratto: un'industria o una cittadina propone un compito, ricevi qualcosa quando accetti, di più se lo completi in tempo, e restituisci l'anticipo più una penalità se superi la scadenza. Rifiutare un'offerta, o lasciarla scadere, non costa nulla.

```diagram subsidy_life
```

## I quattro tipi di contratto

```diagram subsidy_types
```

| Contratto | Obiettivo | Che cosa lo completa | Fonte |
|---|---|---|---|
| **Fornitura industriale** | un'industria che non ha mai prodotto nulla e che ha bisogno di una merce già prodotta da qualche parte sulla mappa (`deliver_cargo.script.tl:163`) | il numero richiesto di consegne a essa, **di una qualsiasi delle sue merci in entrata** | `deliver_cargo.script.tl:60-67`, `deliver_cargo.script.tl:236-240`, `deliver_cargo.script.tl:463-472` |
| **Fornitura urbana** | una merce che la cittadina richiede e non riceve affatto | il numero richiesto di unità **di quella merce** consegnate agli edifici della cittadina | `deliver_cargo_town.script.tl:559-574` |
| **Collegamento urbano** | due cittadine | **un solo** passeggero che inizia un viaggio tra le due cittadine su una linea che ferma in entrambe | `deliver_passengers.script.tl:252-274`, `subvention_util.tl:561-592` |
| **Trasporto di forza lavoro** | un'industria che spedisce o riceve già merci, non ancora potenziata | il suo potenziamento dei lavoratori diventa attivo (metà dei suoi posti di lavoro) | `deliver_workers.script.tl:121-131`, `deliver_workers.script.tl:152-156` |

- Ogni nuova offerta sceglie uno dei tipi che possono comparire in quel momento, con la stessa probabilità (`subventions.script.tl:147-169`).
- **Fornitura industriale** e **Fornitura urbana** contano le consegne, non i viaggi: ogni unità pagata che arriva all'obiettivo aggiunge 1. I trasbordi sono ammessi (`deliver_cargo.script.tl:463-472`).
- **Collegamento urbano** non richiede un numero di passeggeri: il primo passeggero che sale sulla tua linea tra le due cittadine lo completa. "Diretto" significa che quel tratto si fa su un'unica linea che serve entrambe le cittadine. Nessuna offerta compare se una linea carica già passeggeri in entrambe le cittadine e ha un veicolo che può trasportarli (`deliver_passengers.script.tl:76-85`).
- Le cittadine vicine sono molto più probabili: il peso di una coppia è (peso della distanza)^7 × 100 più la **media** dei valori delle due cittadine, ciascuno di almeno 1, che il motore legge alla posizione della cittadina dalla sua griglia delle infrastrutture del giocatore (`deliver_passengers.script.tl:159`, `deliver_passengers.script.tl:183`, `deliver_passengers.script.tl:188`). Il peso della distanza è 1 a 1 km e scende in modo uniforme fino a 0,01 a 20 km (`deliver_passengers.script.tl:157-159`, `deliver_passengers.script.tl:175-191`). La parte della distanza vale quindi circa 19 a 5 km, circa 1 a 10 km e quasi zero oltre circa 15 km, dove restano solo i valori delle cittadine.
- **Fornitura urbana** preferisce merci già prodotte da qualche parte sulla mappa: 16 volte più probabili delle altre (`deliver_cargo_town.script.tl:283-286`).
- La quantità da consegnare dipende dall'impostazione **Rischio commesse**:

| Rischio commesse | Fornitura industriale | Fornitura urbana (al massimo la domanda della cittadina) | Fonte |
|---|---|---|---|
| Nessuno | 10–50 | 10–30 | `deliver_cargo.script.tl:106-120`, `deliver_cargo_town.script.tl:171-194` |
| Sostenibile | 50–100 | 30–100 | |
| Rischioso | 75–150 | 35–125 | |
| Molto rischioso | 150–300 | 45–150 | |

## Che cos'è un collegamento diretto?

La scheda **Collegamento urbano** chiede: "Crea un collegamento diretto tra {fromTownName} e {toTownName} per trasportare i passeggeri da una cittadina all'altra." (`deliver_passengers.script.tl:14`).

- **Una linea con una fermata in ogni cittadina.** Il gioco scorre le fermate della linea e prende la cittadina di ognuna; la linea conta quando almeno una fermata si trova in ciascuna delle due cittadine. Le altre fermate, il loro ordine e il tipo di veicolo (autobus, tram, treno, nave, aereo) non contano (`subvention_util.tl:561-592`).
- **Un solo passeggero lo completa**: il primo passeggero, dopo che hai accettato l'offerta, che viaggia su quella linea da una fermata di una cittadina a una fermata dell'altra, in entrambe le direzioni (`deliver_passengers.script.tl:252-274`, `deliver_passengers.script.tl:207-215`). Il controllo guarda solo questo viaggio, quindi cambiare linea prima o dopo non dovrebbe contare.
- **La cittadina di una fermata** è la cittadina della prima stazione del suo gruppo di stazioni (`town_util.tl:1844-1873`). A quale cittadina appartiene una stazione lo decide il motore.
- **Nessuna offerta** quando una linea qualsiasi ha già in ogni cittadina una fermata che carica passeggeri e un veicolo che trasporta passeggeri; ogni linea di questo tipo viene controllata (`deliver_passengers.script.tl:76-85`). Una linea solo merci tra di esse non blocca l'offerta.
- Il contratto finisce come **Commessa revocata** quando una delle due cittadine, o la linea che l'ha completato, cambia in un modo che il gioco conta come una nuova versione (`deliver_passengers.script.tl:229-237`).

```engine
A quale cittadina appartiene una stazione (stationSystem.getTown), quando esattamente un passeggero "inizia a usare" una linea (OnStartedLineUsage) e quali modifiche di una linea contano come una nuova versione è deciso dal motore. Non è stato testato se una modifica della linea dopo l'adempimento faccia terminare l'effetto Entrate x2.
```

## Ricompense e penalità

Ogni contratto tiene tre elenchi, mostrati sulla sua scheda come **In accettazione**, **In adempimento** e **In fallimento**; gli script li applicano all'accettazione, all'adempimento e al fallimento (`subvention_util.tl:449-471`). In caso di fallimento viene ripreso tutto ciò che è stato dato all'accettazione, più una penalità, o due per Collegamento urbano, una perdita di reputazione in ogni cittadina (`subvention_util.tl:457-463`, `deliver_cargo.script.tl:140-142`, `deliver_passengers.script.tl:118-121`).

| Contratto | In accettazione | In adempimento | In fallimento | Fonte |
|---|---|---|---|---|
| Fornitura industriale | denaro | solo l'effetto **Entrate x2** | anticipo restituito + multa | `deliver_cargo.script.tl:126-142` |
| Fornitura urbana | denaro **o** reputazione nella cittadina | esperienza della cittadina **o** denaro, più Entrate x2 | anticipo restituito + perdita di reputazione **o** multa | `deliver_cargo_town.script.tl:200-235` |
| Collegamento urbano | denaro, di più per cittadine lontane | esperienza in **entrambe** le cittadine, più Entrate x2 | anticipo restituito + perdita di reputazione in **entrambe** le cittadine | `deliver_passengers.script.tl:112-126` |
| Trasporto di forza lavoro | denaro | denaro | anticipo restituito + multa | `deliver_workers.script.tl:92-116` |

- **Denaro**, prima della scala per anno: anticipo da 1,5 M a 3,75 M × il fattore di rischio (Nessuno ×2, Sostenibile ×1, Rischioso ×0,75, Molto rischioso ×0,5, o ×0,625 per Collegamento urbano e Trasporto di forza lavoro), e per Collegamento urbano anche × il fattore di distanza (da 0,3 a 3,0); multa da 3 M a 6 M; pagamento al completamento da 3,75 M a 11,25 M (`deliver_cargo.script.tl:106-134`, `deliver_passengers.script.tl:89-113`, `deliver_workers.script.tl:64-104`). Ogni importo è anche moltiplicato per un fattore della configurazione di base, `subventionFinancialRewardMultiplier` (`deliver_cargo.script.tl:126`), il cui valore non è fissato negli script.
- Il denaro cresce con l'**anno del calendario**, non con l'impostazione Inflazione: ×1 nel 1900, in aumento uniforme fino a ×4 nel 2000 e dopo, arrotondato per eccesso a 10.000 (`finances_util.tl:87-90`). Viene registrato come **Commesse** nelle finanze (`subvention_util.tl:126-135`).
- **Fornitura urbana** può avere un pagamento in denaro al completamento e una multa in denaro solo se il tuo conto bancario è sotto i 100 M quando l'offerta viene creata; al di sopra, solo 1 offerta su 10 può ancora, le altre danno esperienza alla cittadina e tolgono reputazione. L'anticipo non cambia (`deliver_cargo_town.script.tl:200-235`).
- L'**esperienza della cittadina** è una quota del suo livello attuale: dal 20% al 100% dell'XP tra il suo livello e il successivo (`deliver_cargo_town.script.tl:222`, `town_growth.script.tl:605-608`). Per **Collegamento urbano** viene moltiplicata per il fattore di distanza, da 0,3 a 1 km fino a 3,0 a 20 km: cittadine lontane possono guadagnare più livelli (`deliver_passengers.script.tl:101-103`, `deliver_passengers.script.tl:123-125`).
- La **reputazione** persa dopo un fallimento compare nella valutazione Reputazione della cittadina come **Commessa non completata** (`towns.script.tl:310-331`). La reputazione ottenuta all'accettazione elimina solo penalità esistenti, non può superare il massimo (`town_util.tl:1644-1647`).

## L'effetto Entrate x2

- Dura **60 mesi** (5 anni) dopo l'adempimento del contratto (`subvention_util.tl:286`, `subvention_util.tl:292`).
- **Fornitura industriale**: le consegne a quell'industria, sulle linee che l'hanno rifornita durante il contratto (`deliver_cargo.script.tl:456-462`).
- **Fornitura urbana**: le consegne a qualsiasi edificio di quella cittadina, **qualsiasi merce**, sulle linee che hanno consegnato la merce del contratto (`deliver_cargo_town.script.tl:547-558`).
- **Collegamento urbano**: i passeggeri tra le due cittadine, su **una** sola linea diretta: la linea che ha completato il contratto. Non cambia più dopo il completamento, anche con più linee dirette (`deliver_passengers.script.tl:252-299`).
- La scheda nomina le linee: "2x Income for {duration} on All Supplying Lines" per Fornitura industriale e Fornitura urbana (`deliver_cargo.script.tl:40-41`, `deliver_cargo_town.script.tl:44-45`), "2x Income for {duration} on First Established Connection" per Collegamento urbano (`deliver_passengers.script.tl:48-51`).
- **Trasporto di forza lavoro** non ha effetto sulle entrate (`deliver_workers.script.tl:189-190`).
- Per Fornitura industriale e Fornitura urbana, una linea che ha iniziato a consegnare solo dopo l'adempimento del contratto non ottiene nulla: l'elenco delle linee viene riempito solo durante il contratto.
- Due contratti non raddoppiano mai due volte lo stesso pagamento: quando ne corrispondono diversi, viene usata solo l'ultima risposta (`subventions.script.tl:570-583`).

```tip scripts
**Vuoi il reddito doppio di Fornitura industriale o Fornitura urbana su più linee? Falle consegnare tutte prima che il contratto sia adempiuto.** Una linea aggiunta dopo non ottiene nulla. Collegamento urbano raddoppia una sola linea, quella che l'ha completato: fai trasportare il primo passeggero dalla linea che vuoi raddoppiata.
```

```engine
Come il ×2 di una commessa si combina con il moltiplicatore del grado dell'azienda (impostazione Inflazione) è deciso dal motore: entrambi gli script restituiscono solo un moltiplicatore per ogni pagamento. Che cosa sia una voce di pagamento (presumibilmente un'unità di merce o un passeggero) è anch'esso deciso dal motore.
```

## Scadenze

La scadenza parte quando accetti. È più lunga quando la merce deve viaggiare lontano e più breve con un rischio più alto (fattore di rischio Nessuno ×2, Sostenibile ×1, Rischioso ×0,75, Molto rischioso ×0,5, oppure ×0,625 per i contratti di passeggeri e di lavoratori):

| Contratto | Scadenza in mesi | Distanza usata | Fonte |
|---|---|---|---|
| Fornitura industriale, Fornitura urbana | (6 + 32 × E) × fattore di rischio | fino all'industria più vicina che produce la merce | `deliver_cargo.script.tl:122-123` |
| Collegamento urbano | (9 + 4 × E) × fattore di rischio | tra le due cittadine | `deliver_passengers.script.tl:105-106` |
| Trasporto di forza lavoro | (6 + 15 × E) × fattore di rischio × fattore d'epoca (×1,75 prima del 1940, ×1,25 prima del 1980) | fino alla cittadina più vicina | `deliver_workers.script.tl:75-87` |

E è il tempo che un treno alla velocità massima dell'epoca (da 120 km/h dal 1900 fino a 300 km/h dal 1981) impiega per quella distanza, arrotondato per eccesso, almeno 1 (`subvention_util.tl:486-489`, `vehicle_util.tl:225-230`).

- Un'offerta non accettata scompare dopo circa **6 mesi** (da 150 a 210 giorni), senza alcuna penalità (`subvention_util.tl:284`, `subvention_util.tl:290`).
- Finché un contratto **Fornitura industriale** o **Trasporto di forza lavoro** è in corso, l'industria obiettivo non può chiudere: una chiusura prevista viene annullata (`subvention_util.tl:473-484`).
- Se l'obiettivo scompare o viene ricostruito durante il contratto, il gioco mostra **Commessa revocata**, ma le penalità di fallimento si applicano come per una scadenza mancata (`subventions.script.tl:172-190`, `subvention_util.tl:406-412`).
- Non c'è alcun pulsante per annullare un contratto accettato.

```engine
Quanto dura un mese di gioco, e quindi la durata reale delle scadenze, è stabilito dal motore (getDefaultMonthDuration). Le formule qui sopra sono in mesi del calendario di gioco.
```

## Ogni quanto arrivano nuove offerte

- **Disponibilità commesse**: Raramente, Occasionalmente (predefinito), Frequentemente, Regolarmente danno una nuova offerta ogni 12, 6, 3 o 1 mesi; **Mai** disattiva le commesse (`subvention_util.tl:13-38`, `mod.script.tl:248-249`).
- L'intervallo cresce con il **grado dell'azienda**: ×1 al grado 1 fino a ×2 al grado 15 (`subvention_util.tl:19-22`).
- **Rifiutare** un'offerta dimezza l'intervallo successivo; accettare o una nuova offerta lo ripristina (`subventions.script.tl:429`, `subventions.script.tl:395`, `subventions.script.tl:118`).
- Nessuna nuova offerta finché **5 contratti** sono accettati e in corso (`subventions.script.tl:23`, `subventions.script.tl:256-262`). La prima offerta arriva dopo mezzo mese (`subventions.script.tl:25`).
- Lo stesso obiettivo (industria, cittadina e merce, coppia di cittadine) viene offerto **una sola volta per partita**, anche dopo un contratto mancato o fallito (`subventions.script.tl:107-113`, `subventions.script.tl:186`).
- Livelli di difficoltà predefiniti, disponibilità / rischio (`difficulty_util.tl:104-105`, `difficulty_util.tl:132-133`, `difficulty_util.tl:159-160`, `difficulty_util.tl:186-187`): Facile Frequentemente / Nessuno, Normale Occasionalmente / Sostenibile, Difficile Raramente / Rischioso, **Molto difficile Mai**: nessuna commessa.
- Il controllo della valutazione che consentirebbe commesse solo nelle cittadine valutate Ottima esiste, ma è disattivato (`town_util.tl:1574-1580`, `deliver_cargo_town.script.tl:278-281`).

## Da sapere

- Accetta senza timori quando l'obiettivo è facile: rifiutare o ignorare non costa nulla, ma **fallire** costa la restituzione dell'anticipo più una multa che può superare l'anticipo.
- Per **Fornitura urbana** e **Fornitura industriale**, inizia a consegnare con tutte le linee che vuoi far beneficiare: solo le linee che hanno consegnato durante il contratto ottengono le Entrate x2 per 5 anni.
- **Collegamento urbano** con cittadine lontane tra loro dà più esperienza, e basta un solo passeggero.
- **Fornitura industriale** non paga nulla in più al completamento: la sua ricompensa sono solo le Entrate x2.

```check
official: "Accept an offer to begin the contract; declining it has no penalty." "Possible rewards include town experience, an additional payment, or a limited-time 2x income effect on eligible transport lines." "The upfront reward is reversed, and an additional fine or loss of town reputation may apply." ([Subsidies](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:subsidies))
scripts: Quattro tipi; un solo passeggero completa Collegamento urbano; il ×2 dura 60 mesi sulle linee che hanno consegnato durante il contratto; Fornitura industriale dà solo il ×2; denaro in base all'anno (da ×1 a ×4); una nuova offerta ogni 1–12 mesi, più rade a un grado alto dell'azienda; al massimo 5 accettati; ogni obiettivo offerto una volta per partita.
result: refines
```
