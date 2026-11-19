---
title: Perché perdo soldi?
summary: Cosa paga, cosa costa, e un controllo in sei passi per trovare le linee che perdono soldi e perché, con link alle pagine che spiegano ogni punto.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-15
game: 40444
fact: 1 | pagamento per unità, al consumatore, per la linea d'aria
fact: 0 | pagato in un magazzino o in un trasbordo
fact: 100 % | pagato anche in ritardo
fact: ×6 | fattore anno mostrato sulla manutenzione di magazzini, aerodromi, aeroporti e porti nel 2020
---

Una consegna paga per **una sola linea d'aria**, da dove la merce è stata prodotta a dove viene usata, e solo quando arriva lì. Tutto ciò che costruisci e compri costa soldi ogni anno, una parte sempre di più con l'anno del calendario. Una linea perde soldi quando la sua parte dei pagamenti è più piccola dei costi che porta.

```diagram money_flow
```

## Cosa paga

- **La distanza in linea d'aria** dalla fonte al consumatore, più 8 × il dislivello. La lunghezza del tuo percorso non conta (`cargo_income.script.lua:3-7`, `cargo_income.script.lua:5`).
- **Ogni merce paga uguale** per chilometro: il fattore di entrata è 3,8 per tutte (`cargotype.script.lua:7-13`).
- **Una volta, al consumatore.** Scaricare in un magazzino o in una stazione di trasbordo non paga nulla. Il pagamento viene poi diviso tra le linee della catena in base alla lunghezza in linea d'aria di ogni tratta (misurato in gioco).
- **La merce in ritardo è pagata per intero**: il tempo di viaggio non viene usato (`cargotype.script.lua:7-13`). Il ritardo abbassa invece la valutazione **Consegna** della cittadina.
- **Il grado azienda** abbassa tutte le entrate con l'impostazione **Inflazione**: al grado 15, ×0,75 a Normale (`company_progression_util.tl:25-40`).
- Una **commessa completata** raddoppia, per 5 anni, le entrate delle consegne che copre: alla sua industria, alla sua cittadina o i passeggeri tra le sue due cittadine, solo sulle sue linee (`subvention_util.tl:286`). Vedi [Commesse: offerte, scadenze e ricompense](subsidies.html).

Dettagli: [Entrate dalle merci e tempi di consegna](income.html).

## Cosa costa

- **Veicoli**: i costi di esercizio seguono la velocità media × la capacità, e il prezzo vale 6 anni di costi di esercizio (`model_metadata_util.lua:499-518`, `model_metadata_util.lua:548-549`).
- **Binari e strade**: circa un sesto del prezzo di costruzione per km e per anno; il binario ad alta velocità costa 9 volte il binario semplice (`simple.street_template.lua:33`, `high_speed.street_template.lua:35`).
- **Depositi, stazioni, magazzini, porti, aeroporti**: le varianti di epoche successive costano ×3 e ×9 (`rail_depot.con.lua:7`, `warehouse.tl:48`), e per magazzini, aerodromi, aeroporti e porti la finestra dell'edificio mostra una manutenzione che segue l'anno, da ×1 nel 1900 a ×6 nel 2020 (`mod.script.tl:92-100`, `entity_window_util.tl:188-192`). Ciò che viene addebitato lo decide il motore.
- **Prestiti**: il tasso viene addebitato una volta sull'importo, distribuito sulla durata (`loan_util.tl:102-111`).
- **L'Inflazione non alza nessun costo**. Abbassa solo le entrate.

Dettagli: [Costi, manutenzione e prestiti](costs.html).

## Sei controlli, in ordine

```diagram money_check
```

1. **Quali linee perdono soldi?** Guarda il bilancio di ogni linea, non il totale dell'azienda. La mod [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) mostra il bilancio di ogni linea negli ultimi 12 mesi e la sua media su più anni.
2. **La merce va lontano?** Paga solo la linea d'aria dalla fonte al consumatore. Una breve linea di raccolta verso un magazzino riceve solo la parte della sua breve tratta ([Entrate dalle merci e tempi di consegna](income.html)).
3. **Viaggia piena?** Un veicolo costa uguale pieno o vuoto. Guarda i ritorni a vuoto, il **Riempi livello** e il **carico completo** di ogni fermata ([Impostazioni di partenza: carico completo, Riempi livello e tempi di sosta](departure.html)).
4. **Viene scaricata dove paga?** Ciò che non è nella lista Carico di una fermata viene scaricato in qualsiasi scorta vicina, magazzini compresi, e un magazzino non paga nulla ([Velocità di carico e scarico](loading.html), [Magazzini](warehouses.html)). La merce che non entra nelle scorte piene della cittadina resta a bordo ([Crescita delle cittadine: XP, valutazioni e dimensioni](towns.html)).
5. **Troppo veicolo?** Velocità e capacità costano soldi, ma la velocità non paga: aiuta solo quando dà più viaggi all'anno. In città, un vecchio autobus lento può rendere più di uno nuovo e veloce ([Costi, manutenzione e prestiti](costs.html)).
6. **Costi fissi.** Depositi, moduli di magazzino in più, binari veloci ed edifici di un'epoca successiva costano ogni anno, usati o no ([Costi, manutenzione e prestiti](costs.html)).

## Buono a sapersi

- **Scegli le merci per volume e distanza**, non per prezzo: ogni merce paga uguale per km.
- Una **lunga linea principale** alimentata da linee brevi guadagna la maggior parte dei soldi; le linee di raccolta mostrano bilanci piccoli, ma conta la catena intera.
- **Più da trasportare**: un'industria potenziata produce di più ([I lavoratori e il booster dei lavoratori](workers.html), [Industrie](industries.html)), e una cittadina più grande chiede più merci.
- Rendere più veloce una linea non alza il pagamento per unità. Aiuta solo se gli stessi veicoli fanno più viaggi.

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks))
scripts: Uguale: linea d'aria più 8 × dislivello, lo stesso fattore per ogni merce, tempo di viaggio non usato; misurato in gioco: pagato una volta al consumatore e diviso per lunghezza della tratta; i costi seguono velocità × capacità per i veicoli, 1/6 del prezzo per i binari, varianti d'epoca ×3 / ×9 e fattore anno da ×1 a ×6 per gli edifici; l'Inflazione abbassa solo le entrate.
result: refines
```
