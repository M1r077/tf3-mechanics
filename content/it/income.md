---
title: Entrate dalle merci e tempi di consegna
summary: Quanto paga una consegna (distanza in linea d'aria, dislivello, grado dell'azienda, commesse) e quanto costa davvero un ritardo.
domain: economy
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
game: 40444
fact: 3,8 | lo stesso fattore di entrata per tutte le merci
fact: +8 × salita | metri di salita aggiunti alla distanza
fact: 100% | pagato anche quando la consegna è in ritardo
---

Una consegna paga la **distanza in linea d'aria**, e nient'altro del viaggio. La velocità conta per un altro motivo: ogni merce ha un **tempo limite**, e le consegne in ritardo abbassano la valutazione **Consegna** della cittadina, non le tue entrate.

```diagram income_formula
```

## La formula delle entrate

L'intera formula è un breve script del gioco (`cargo_income.script.lua:10-13`):

1. **Fattore di entrata** della merce. Tutte le merci del gioco base usano la stessa funzione e gli stessi prezzi (`initialPrice = 4`, `finalPrice = 3.2`), il che dà **3,8 per tutte le 36 merci** (`cargotype.script.lua:7-13`, `coal.cargo.lua:21-22`). Il carbone paga esattamente quanto le merci generiche sulla stessa distanza.
2. Impostazione **Entrate carichi**: 50%, 75%, 100%, 125% o 150% (`difficulty_util.tl:38`, `mod.script.tl:212`). Tutti e quattro i livelli di difficoltà predefiniti usano 100% (`difficulty_util.tl:97`, `difficulty_util.tl:124`, `difficulty_util.tl:152`, `difficulty_util.tl:179`).
3. **Distanza**, vedi sotto.

La funzione riceve il tempo di viaggio ma **non lo usa** (`cargotype.script.lua:7-13`): una consegna lenta o in ritardo paga lo stesso.

## Distanza: linea retta più salita

```diagram income_distance
```

- La distanza è la **linea retta in 3D** tra i due punti, non la lunghezza del tuo percorso (`cargo_income.script.lua:3-7`).
- Quando la merce è consegnata più in alto della sua origine, si aggiunge **8 × quel dislivello** (`cargo_income.script.lua:5`): 100 m pagano come 800 m in più. Gli script usano la differenza di quota che il motore passa loro; la sua direzione non è visibile negli script. Una differenza negativa non sottrae nulla.
- Quindi una linea tortuosa rende quanto una diritta, ma paghi la manutenzione di ogni metro di binario o di strada che hai costruito.

```engine
Il motore sceglie i due punti e li passa allo script. Misurato in gioco (vedi sotto): sono l'**origine** della merce (l'industria o l'edificio della cittadina che l'ha prodotta) e il **consumatore** che la riceve, come dice la wiki ufficiale ("between the source and the final destination").
```

## Merci che cambiano linea

Quando un'unità viaggia su più linee, per esempio nave → magazzino → treno, il gioco la paga comunque **una sola volta**:

```diagram income_split
```

1. Lo scarico in un magazzino o in una stazione di trasbordo non paga **nulla**. Su circa 17.000 pagamenti misurati, solo 43 sono andati a una destinazione che non era un consumatore.
2. Quando l'ultimo veicolo consegna al consumatore, l'unità viene pagata con la formula qui sopra, per la linea retta **dall'origine al consumatore**. Le tratte e il percorso reale non contano, quindi una deviazione attraverso un magazzino non rende nulla in più.
3. Quel denaro viene diviso tra le linee della catena **in proporzione alla lunghezza in linea retta di ogni tratta**: da un punto di carico al successivo, e dall'ultimo punto di carico al consumatore. Il bonus di salita non conta in questa ripartizione.
4. Il veicolo che consegna trattiene prima l'intero importo, con una quota per tratta. Viene contabilizzato qualche secondo di tempo di gioco dopo (mediana circa 6 s), e ogni linea e ogni veicolo riceve la propria quota. Il saldo di una linea quindi si muove poco dopo la consegna, non al magazzino.

Così una breve linea di adduzione verso un magazzino rende poco, anche se fa tutta la raccolta; la tratta lunga guadagna la maggior parte. Ogni linea mostra comunque la sua quota reale nel proprio saldo.

```engine
Gli script calcolano solo il totale (`economy/cargo_income.script.lua`); la ripartizione è fatta dal motore e non è visibile negli script. Le regole qui sopra sono state misurate con una mod di prova in sola lettura: circa 1.700 pagamenti di unità con 2 o 3 tratte, e le variazioni di conto di ogni linea e veicolo coinvolti. In 769 casi puliti (un'unità, un pagamento) la ripartizione corrispondeva alle lunghezze delle tratte entro l'1% ogni volta; una ripartizione con il bonus di salita corrispondeva solo nel 59% dei casi, una ripartizione in parti uguali in nessuno.
```

## Che cos'altro cambia l'importo

| Che cosa | Effetto | Fonte |
|---|---|---|
| **Grado azienda** con l'impostazione Inflazione | grado 1: ×1, in calo uniforme fino al grado 15: ×0,9 (Ridotta), **×0,75 (Normale)**, ×0,6 (Elevata), ×0,5 (Molto elevata); Nessuna: sempre ×1 | `company_progression_util.tl:25-40`, `difficulty_util.tl:50`, `mod.script.tl:695-698` |
| **Commessa completata** | ×2 per le consegne all'industria o alla cittadina del contratto, sulle linee che hanno consegnato per il contratto | `deliver_cargo.script.tl:456-462`, `deliver_cargo_town.script.tl:547-558` |
| **Consegna in ritardo** | nessun effetto sulle entrate | `cargotype.script.lua:7-13` |

- Il moltiplicatore del grado si applica a **tutti** i pagamenti di merci e passeggeri (`company_growth.script.tl:159-170`). I livelli di difficoltà predefiniti usano Inflazione Ridotta (Facile), Normale (Normale), Elevata (Difficile), Molto elevata (Molto difficile) (`difficulty_util.tl:108`, `difficulty_util.tl:136`, `difficulty_util.tl:163`, `difficulty_util.tl:190`).
- Il ×2 delle commesse vale solo per le linee che hanno consegnato durante il contratto, per un tempo limitato (wiki ufficiale, Subsidies).

## Passeggeri

I passeggeri usano la stessa distanza e un fattore di entrata fisso di circa 3,61 (`cargotype.script.lua:50-53`), moltiplicato per **0,5 + il fattore di prezzo del biglietto del veicolo** (`cargo_income.script.lua:14-17`). Quando un modello di veicolo non imposta il suo fattore di comfort, il gioco imposta il fattore di prezzo a 0,3 per autobus e tram, 0,9 per gli aerei, 0,1 per le navi e 0,5 per i treni (`base_mod.lua:46-61`); per gli altri modelli è un valore del motore, non visibile negli script. Una commessa passeggeri raddoppia solo i passeggeri che viaggiano tra le sue due cittadine, sulla sua unica linea, quella che ha completato il contratto (`deliver_passengers.script.tl:288-293`).

## Tempi limite di consegna

Ogni merce ha il proprio tempo limite (`meat.cargo.lua:30`, `coal.cargo.lua:30`). Gli alimenti freschi hanno il più breve: carne 900 s, carbone 3.000 s (3,3 × più lungo), minerale di ferro, sabbia, pietra e acciaio 4.500 s:

```diagram delivery_times
```

- **Finanze › Tempi di consegna** mostra il limite di ogni merce sulla tua mappa; lo strato soddisfazione merci colora i percorsi dal verde al rosso.
- Una consegna conta come **in ritardo** quando arriva dopo il suo limite (`towns.script.tl:422`).
- I moduli di magazzino specializzati **congelano** il tempo della merce che conservano (wiki ufficiale, Warehouses).

```engine
Il motore trasforma il tempo di base nel tempo limite mostrato in Finanze (gli script lo leggono con getAdjustedDeliveryTime) e decide quando un'unità è in ritardo. Solo i valori relativi qui sopra provengono dai file delle merci.
```

## Quanto costa un ritardo: la valutazione Consegna

Le merci in ritardo vengono pagate per intero, ma ogni cittadina tiene una valutazione **Consegna** (`town_util.tl:505-519`):

1. Il gioco conta le consegne alla cittadina nell'**ultimo mezzo anno**, e quante erano in ritardo (se ne presumono almeno 10, così le prime consegne non la fanno oscillare).
2. Quota puntuale → valutazione: sotto un limite inferiore la valutazione è 0, sopra un limite superiore è 1, lineare nel mezzo. Con la sensibilità predefinita (**Normale**): **30% puntuali → 0, 100% → 1**, quindi il 90% di consegne puntuali dà 0,86.
3. L'impostazione **Sensibilità consegne** sposta i limiti (`difficulty_util.tl:47`). No: sempre 1. Livelli predefiniti: Facile Ridotta, Normale Normale, Difficile Elevata, Molto difficile Molto elevata (`difficulty_util.tl:113`, `difficulty_util.tl:141`, `difficulty_util.tl:168`, `difficulty_util.tl:195`).

```diagram delivery_rating
```

Consegna è una delle sei valutazioni la cui più bassa determina l'indice di crescita della cittadina: una sola valutazione Pessima ferma la cittadina (vedi [Crescita delle cittadine](towns.html)).

## Esempio

La stessa consegna di carbone, a 5 km in linea d'aria.

| Situazione | Pagato |
|---|---|
| in piano, qualsiasi lunghezza del percorso | **100%** |
| a 10 km | **200%** |
| consegnata 100 m più in alto dell'origine | **116%** |
| consegnata in ritardo | **100%** (la valutazione Consegna scende) |
| grado azienda 15, Inflazione Normale | **75%** |
| consegna coperta da una commessa completata | **200%** |

## Da sapere

- Poiché tutte le merci pagano lo stesso per chilometro, **scegli le merci in base a volume, distanza e tempo limite**, non al prezzo.
- I tempi limite contano soprattutto per carne, pesce, verdure e bevande: linee brevi o magazzini che congelano il tempo.
- Ogni unità consegnata a un edificio della cittadina dà anche esperienza a quella cittadina, per le merci la cui categoria ha un livello (`town_growth.script.tl:641-642`, `town_growth_config.res.lua:5`).

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks), [Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Stesso fattore 3,8 per tutte le merci; distanza in 3D più 8 × la salita; il grado dell'azienda riduce le entrate fino a ×0,75 al grado 15 (Inflazione Normale); ×2 dopo una commessa; il tempo non è usato per le entrate; misurato in gioco: un'unità che cambia linea viene pagata una sola volta, al consumatore, e divisa tra le linee in base alla lunghezza delle tratte; valutazione Consegna dalla quota puntuale dell'ultimo mezzo anno (Normale: 30% → 0, 100% → 1).
result: refines
```
