---
title: Reputazione delle cittadine
summary: Cosa abbassa la valutazione Reputazione di una cittadina, quanto in fretta torna, cosa fanno davvero celebrazioni e campagne marketing, e perché una strada interrotta tra due cittadine costa così tanto.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
fact: −33 % | per ogni collegamento principale interrotto verso un'altra cittadina
fact: ≈ 67 % | recuperato all'anno a velocità calendario ×1 (≈ 200 % durante una campagna marketing); la finestra della cittadina mostra 33 % e 100 %
fact: 0,25 % | per ogni albero adulto rimosso vicino alla cittadina
fact: 2 M m³ | di lavori sul terreno costano tutta la reputazione
---

La **Reputazione** è una delle sei valutazioni della finestra della cittadina, e l'Autorità cittadina prende la **più bassa** (vedi [Crescita delle cittadine](towns.html)). Parte dal 100 % e scende solo per ciò che **tu** costruisci o manchi: lavori sul terreno, alberi e rocce rimossi, edifici della cittadina demoliti, commesse non completate e collegamenti principali interrotti. Il tempo, le celebrazioni e le campagne marketing la fanno risalire.

```diagram rep_recovery
```

## Cosa la abbassa

Ogni costruzione che confermi viene controllata prima di essere applicata; il costo va alla cittadina interessata (`towns.script.tl:271-291`, `town_util.tl:1062-1080`). Contano solo le tue costruzioni, e nell'editor di mappe non conta nulla (`town_util.tl:1078-1080`, `towns.script.tl:58`).

| Motivo nella finestra della cittadina | Cosa costa reputazione | Fonte |
|---|---|---|
| **Alberi rimossi** | 0,25 % per albero, × il fattore di distanza dalla cittadina più vicina, × la dimensione dell'albero (gli alberi piccoli contano meno) | `town_util.tl:1144-1150`, `town_util.tl:865`, `model_metadata_util.lua:655-680` |
| **Rocce rimosse** | 0,25 % per roccia, × il fattore di distanza | `town_util.tl:1148-1149`, `town_util.tl:884-885` |
| **Progettazione paesaggi** | 0,00005 % per m³ di terreno alzato **o** abbassato: 2 milioni di m³ = 100 %. Conta anche il terreno modellato da binari, strade ed edifici (ridotto a partire da 10.000 m², fino alla metà da 50.000 m²), e il volume netto dei nuovi tunnel | `town_util.tl:873-886`, `town_util.tl:1245-1269`, `town_util.tl:1403-1436` |
| **Edifici demoliti** | 100 % per il 40,5 % della capacità di un distretto rimossa (abitazioni, negozi o posti di lavoro di quella cittadina) | `town_util.tl:867-869`, `town_util.tl:1165-1184` |
| **Commessa non completata** | Fornitura urbana: dal 10 % fino al 60–90 % (secondo il rischio); Collegamento urbano: 10–100 % × il fattore di distanza, in **entrambe** le cittadine (vedi [Commesse](subsidies.html)) | `deliver_cargo_town.script.tl:202-210`, `deliver_passengers.script.tl:113-114`, `towns.script.tl:331-333` |
| **Collegamenti principali interrotti** | **1/3** per ogni altra cittadina il cui collegamento principale è interrotto o troppo lungo | `town_util.tl:376-394`, `town_util.tl:1608` |

- Ogni motivo ha un tetto del 100 % (`town_util.tl:1611-1620`).
- Mentre costruisci, il tooltip mostra **Reputazione: −x %**, con il numero di cittadine colpite se sono più di una (`construction_react_util.tl:3818-3864`). Conta il costo partendo da una valutazione piena.
- Piantare alberi o posare rocce annulla solo **Alberi rimossi** o **Rocce rimosse**, con lo stesso 0,25 % ciascuno. Non fa nulla per gli altri motivi, né a reputazione piena (`town_util.tl:1228-1238`, `town_util.tl:1630-1641`).
- L'impostazione Reputazione di una nuova partita è **Mai** o **Sì** (Sì in ogni preimpostazione). Mai significa valutazione piena, sempre (`difficulty_util.tl:44`, `difficulty_util.tl:110`, `town_util.tl:396-399`).

```engine
Quanto in fretta cala il fattore di distanza tra una cittadina e un albero rimosso, quale volume di terreno riceve ogni cittadina, gli alberi rimossi automaticamente da un binario o una strada, e quali strade contano come collegamento principale di una cittadina (e quando un viaggio è «troppo lungo») sono valori del motore (getImpactFromDistance, getTerrainBrushVolumeImpact, getTerrainAlignmentImpact, getAutoRemovalEntityImpact, getTownProblems).
```

## Collegamenti principali interrotti

Un collegamento principale conta come interrotto quando il gioco segnala **Il collegamento stradale tra le città è stato interrotto** o **Il tempo di viaggio tra le città è troppo lungo** (`town_util.tl:378-380`, `town_warning.script.tl:7-22`). Ogni altra cittadina coinvolta costa 1/3, e la valutazione lo mostra **subito** (`town_util.tl:401-403`):

| Collegamenti interrotti | Reputazione al massimo | Valutazione | Fonte |
|---|---|---|---|
| 1 | 67 % | Ottima | `town_util.tl:983-985` |
| 2 | 33 % | Mediocre | `town_util.tl:983-985` |
| 3 | 0 % | Pessima: la cittadina smette di crescere | `town_util.tl:607-633` |

- Finché l'interruzione dura, la penalità viene scritta anche nel punteggio salvato, passo dopo passo, nell'arco di 3 mesi (`towns.script.tl:137-145`). Dopo aver riparato la strada, quella parte salvata torna solo alla velocità normale di recupero: un'interruzione lunga continua a costare reputazione per un po'.
- 67 % è proprio al limite di Ottima: qualsiasi altra piccola perdita porta la cittadina a Buona.

```tip scripts
**Costruisci la nuova strada prima di togliere la vecchia.** Ogni collegamento principale interrotto costa subito un terzo della reputazione, e più dura l'interruzione, più lungo è il recupero.
```

## Come torna

- **Da sola**: un livello (1/6) ogni 3 mesi di tempo di gioco (360 s), ogni mese (120 s) durante una campagna marketing (`towns.script.tl:121-135`). A velocità calendario ×1 sono circa **67 %** all'anno, **200 %** con una campagna: da 0 % al massimo in circa 1,5 anni. La finestra della cittadina mostra **Recupero annuale** 33 % e 100 %: testi fissi, metà della velocità reale (`town_react_util.tl:1066`). Misurato su una cittadina di prova: un livello ogni 358 s, ogni 120 s con una campagna.
- Il recupero ripartisce il guadagno su tutti i motivi; non supera mai i collegamenti ancora interrotti (`town_util.tl:1649-1687`).
- Le **celebrazioni** aggiungono **+50 %** per il primo passeggero che sale su una tua linea in una cittadina, +50 % per il primo carico consegnato a una cittadina, +50 % a ogni salita di livello della cittadina, e +20 % alla cittadina più vicina per il primo carico consegnato a ogni industria (`celebrations.script.tl:181-273`). Il messaggio termina allora con **Reputazione insediamento migliorata.** o **Reputazione … migliorata.** (`celebration_react_util.tl:63-75`). Contano solo se la reputazione è sotto quanto permettono ancora i collegamenti principali interrotti (piena meno 1/3 per collegamento interrotto) e l'impostazione Reputazione è su Sì, e non nelle missioni della campagna (`celebrations.script.tl:79-93`, `celebrations.script.tl:140-142`).
- **Fornitura urbana** può dare da +5 % a +20 % × il fattore di rischio all'accettazione (`deliver_cargo_town.script.tl:195-199`). Come ogni guadagno, toglie solo perdite esistenti (`towns.script.tl:324-330`).

## Campagna marketing

| Cosa | Valore | Fonte |
|---|---|---|
| Prezzo | 10 M × fattore dell'anno: 4 M nel 1900 fino a 25 M nel 2020, arrotondato a 1 M | `marketing_campaign_tool.script.tl:9-14` |
| Richiede | un permesso dei vantaggi dell'azienda | `marketing_campaign_tool.script.tl:83-95`, `company.script.tl:416-423` |
| Durata | un anno | `marketing_campaign_tool.script.tl:136` |
| Reputazione | recupero ×3 (≈ 200 % all'anno, la finestra mostra 100 %); **nessun** guadagno immediato | `towns.script.tl:126`, `town_util.tl:915-925` |
| Residenti | le tue linee in quella cittadina contano come costose la metà quando i residenti scelgono come spostarsi | `marketing_campaign_tool.script.tl:137`, `towns.script.tl:376-398` |

```engine
Lo script conta 360 secondi di tempo di gioco per livello (120 con una campagna), con un mese di 30 giorni da 4 secondi. Il recupero segue il tempo di gioco: con un calendario più lento un anno del calendario dura di più, quindi torna di più per anno mostrato. Quanto il costo di linea dimezzato porti i residenti verso le tue linee lo decide la scelta del percorso del motore.
```

## Buono a sapersi

- Guarda il tooltip di costruzione: se mostra **Reputazione: −x %**, un tunnel o un tracciato più dolce spesso costa meno della reputazione.
- Non lasciare mai interrotta una strada principale tra due cittadine: ognuna vale −33 % subito, e tre interruzioni fermano la cittadina.
- Una campagna marketing a reputazione piena aiuta solo le tue linee, non la valutazione. Lanciala subito dopo grandi lavori, quando il recupero ha qualcosa da recuperare.
- Il bonus **Recupero reputazione** del modulo grande della sede centrale (+1 %) compare nella scheda Bonus, ma negli script cambia solo un valore che nessuna valutazione legge (`hq_module_l.module.lua:171`, `towns.script.tl:157`, `town_util.tl:829`, `town_util.tl:857`).
- L'obiettivo **Non è colpa mia** chiede una cittadina con 0 % di reputazione in Gioco libero (`achievements.script.tl:261-267`).

```check
official: "Reputation reflects how the town and surrounding nature are treated. Landscaping, removing town buildings and breaking main connections to other towns can lower it, while celebrations and marketing campaigns can improve it. Reputation lost by removing trees can be recovered by planting new ones." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Le stesse cause, più rocce rimosse, tunnel, il terreno di binari e strade e le commesse non completate. Ogni collegamento principale interrotto o troppo lungo costa 1/3 subito; tre fermano la cittadina. Il recupero è di circa 67 % all'anno da solo e di circa 200 % con una campagna marketing, il doppio di quanto mostra la finestra (33 % e 100 %); la campagna non dà nulla subito. Piantare alberi annulla solo la perdita dovuta agli alberi. Il bonus Recupero reputazione della sede centrale non ha effetto negli script.
result: differs
```
