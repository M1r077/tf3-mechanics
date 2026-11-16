---
title: Industrie
summary: Regole di produzione, scorte, lotti ed espansione, perché un'industria non cresce o non è potenziata, quando chiude un'industria inutilizzata, e come compaiono nuove industrie.
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
game: 40425
fact: 5 anni | senza carico né consumo rendono un'industria candidata alla chiusura
fact: 1,1 % | di probabilità all'anno con Raramente (predefinito), poi 730 giorni di conto alla rovescia
fact: +50–150 % | di bonus dal carico booster, fisso per ogni industria
fact: 3 mesi | di bonus per lotto di carico booster
fact: ×2/3 – ×1,5 | Densità industrie obiettivo: le nuove industrie non si possono disattivare
---

Ogni industria funziona con **regole**: «prendi questo dalle scorte in entrata, metti quello nelle scorte in uscita», un numero fisso di volte all'anno. Le industrie primarie (miniere, fattorie, pozzi) non hanno bisogno di entrate; la loro dimensione viene dai **lotti**. Due bonus possono moltiplicare la produzione: il **carico booster** (solo industrie primarie) e i **lavoratori**.

## Regole di produzione

- Una regola indica il carico usato e prodotto per ciclo, e quanti cicli all'anno: un ciclo dura un anno ÷ quel numero, meno con i bonus nelle regole di produzione (`industry_react_util.tl:51-57`). La sezione Produzione della finestra dell'industria lo mostra con numeri piccoli.
- Il numero **Massimo** della finestra è: per ciclo × cicli all'anno × il fattore di dimensione (`rule.consumptionFactor`) × i bonus × l'impostazione **Produttività industrie**, gli ultimi due solo nelle regole di produzione (`industry_util.tl:310-379`, `industry_util.tl:357-362`).
- **Produttività industrie**: 50 %, 75 %, 100 %, 150 % o 200 %. Preimpostazioni: Facile 150 %, Normale 100 %, Difficile 75 %, Molto difficile 50 % (`difficulty_util.tl:41`, `difficulty_util.tl:93`, `difficulty_util.tl:120`, `difficulty_util.tl:148`, `difficulty_util.tl:175`, `mod.script.tl:196-197`).
- Esempio, Acciaieria: 6 minerale di ferro + 6 carbone → 3 acciaio + 4 lamine di metallo, 121,7 cicli all'anno: 730 minerale di ferro e 730 carbone → 365 acciaio e 487 lamine di metallo (`steel_mill.con.lua:43-71`). Se manca un'entrata, la regola si ferma.
- La Fabbrica di conserve ha due regole: pesce + lamine di metallo, oppure carne + lamine di metallo (`food_factory.con.lua:43-74`).

```engine
Il motore esegue le regole. Può allungare un ciclo: il tooltip del ciclo mostra allora «(+… per tempo di consegna)» (`industry_react_util.tl:61-76`). Quando e di quanto non è negli script, quindi la produzione reale può restare sotto il Massimo.
```

## Scorte

- Ogni carico ha la sua scorta con un limite: ad es. una Miniera di carbone tiene 100 strumenti e 400 carbone, un'Acciaieria 800 minerale di ferro, 800 carbone, 400 acciaio e 500 lamine di metallo (`coal_mine.con.lua:44-67`, `steel_mill.con.lua:43-71`).
- Le scorte non si deteriorano mai (`industryutil.lua:25-29`): il carico aspetta quanto serve.
- Una scorta in uscita piena non ferma la produzione: l'eccesso viene buttato (wiki ufficiale). Il grafico **Flusso di carichi** mostra **Consumato**, **Prodotto** e **Distrutto** (`industry_eow.script.tl:804-816`).
- Con il parametro di costruzione **Ingresso** su Disattivato, le regole perdono le entrate e l'industria non ha scorte in entrata (`industryutil.lua:280-287`, `industryutil.lua:383-387`, `industryutil.lua:432-441`).

## Lotti ed espansione

- Le industrie primarie e l'Allevamento di bestiame hanno **lotti** (campi, pozzi di miniera, torri). Il loro livello è il numero di lotti (`industryutil.lua:602-617`).
- La regola cresce con i lotti: produzione per ciclo × lotti ÷ **tutti i lotti di quel tipo di industria**, arrotondato, almeno 1. Le entrate calano della stessa quota, arrotondate per eccesso, almeno 1, ma per niente se una produzione mantiene la quantità piena (per esempio una produzione di 1, che non può scendere); le regole di potenziamento non vengono mai ridotte (`industryutil.lua:225-259`). Una Miniera di carbone (8 tipi di lotto) con 4 lotti fa 8 carbone per ciclo invece di 16.
- Ogni industria riceve un massimo: a caso tra metà dei lotti e tutti, oppure Piccola / Media / Grande (50 / 75 / 100 %) con il parametro **Dimensioni industria** (`industryutil.lua:519-537`). Una miniera con massimo 5 su 8 non raggiunge mai la regola completa.
- Con Media, se il 75 % arrotondato dà tutti i lotti, il massimo è tutti i lotti meno uno (`industryutil.lua:523-526`). Una nuova industria parte con i lotti che il motore costruisce al piazzamento; il suo livello viene da questi (`industryutil.lua:602-617`).
- Ogni sei mesi di **tempo di gioco** il gioco può aggiungere **un lotto** (`industries_config.res.lua:5`, `industries.script.tl:161-167`). Si usa mezzo anno standard, quindi la velocità del calendario non cambia la frequenza (vedi [Tempo di gioco e calendario](time.html)).
- La probabilità è (valutazione − 25 %) ÷ 50 %, con valutazione = valutazione di produzione × la quota della produzione che spedisci (al massimo 1): 25 % o meno mai, 75 % o più sempre (`industries.script.tl:168-179`).
- Quindi un'industria di cui non spedisci il carico **non cresce mai**. Le fabbriche non hanno lotti e non crescono mai.
- Al massimo la finestra dice **L'industria ha raggiunto il suo massimo potenziale.**; se edifici, binari o strade sono d'intralcio, **L'industria non può espandersi ulteriormente.** (`industry_react_util.tl:588-602`, `industries.script.tl:13-38`). Nessuno script toglie lotti; secondo la wiki ufficiale i lotti demoliti abbassano la produzione.
- Lo script di gioco salta le industrie di tua proprietà, quelle a sviluppo manuale e quelle in conto alla rovescia di chiusura: da lui non ricevono mai un lotto (`industries.script.tl:94-99`, `industries.script.tl:147-157`).

Esempio, **Campo di disboscamento**: 20 lotti, 8 tronchi per ciclo, 30,4 cicli all'anno (`forest.con.lua:54-66`, `forest.con.lua:75-98`). Per ciclo fa 8 × lotti ÷ 20, arrotondato, almeno 1 (`industryutil.lua:231-241`):

| Lotti (livello) | Tronchi per ciclo | Tronchi all'anno (Massimo, senza bonus, Produttività 100 %) |
|---|---|---|
| 1–3 | 1 | 30 |
| 4–6 | 2 | 61 |
| 7–8 | 3 | 91 |
| 9–11 | 4 | 122 |
| 12–13 | 5 | 152 |
| 14–16 | 6 | 183 |
| 17–18 | 7 | 213 |
| 19–20 | 8 | 243 |

La produzione cresce a gradini: un nuovo lotto non aumenta sempre la produzione.

## Perché la mia industria non cresce?

```diagram ind_growth
```

1. **Carico non spedito**: la valutazione conta la quota della produzione caricata sui tuoi veicoli. Con una valutazione di produzione del 100 %, spedire il 25 % o meno non dà alcuna probabilità, il 50 % una probabilità di metà, il 75 % o più un lotto ogni sei mesi.
2. **Al massimo**: **L'industria ha raggiunto il suo massimo potenziale.** Il massimo viene estratto alla costruzione (da metà a tutti i lotti) e non cambia mai.
3. **Bloccata**: **L'industria non può espandersi ulteriormente.** Togli strade, binari o edifici dal posto del prossimo lotto (mostrato nella finestra).
4. **Non è un'industria primaria**: le fabbriche non hanno lotti.
5. **Conto alla rovescia di chiusura**, di tua proprietà o a sviluppo manuale: nessuna crescita dallo script (sopra).
6. **Nessuna produzione**: un'industria che non produce nulla nell'anno viene saltata (`industries.script.tl:168-171`).

```tip scripts
**Per far crescere una miniera o una fattoria, spedisci almeno il 75 % della produzione e tieni alta la valutazione di produzione.** La probabilità usa valutazione di produzione × quota spedita: con il 25 % o meno nessun nuovo lotto; con il 75 % o più e una valutazione di produzione del 100 %, uno ogni sei mesi, fino al massimo.
```

```engine
La valutazione di produzione (getProductionRating), la produzione annua e la quantità spedita (getCargoOutputPerYear, getCargoShippedPerYear), e dove va un nuovo lotto (makeIndustryExtendProposal) sono valori del motore.
```

## Carico booster

Le 13 industrie primarie hanno una seconda regola, il **booster**: prende un lotto di carico booster dalla scorta in entrata 4 volte all'anno e dà un bonus finché dura.

| Industria | Lotti | A piena dimensione, all'anno | Lotto booster (4 all'anno) | Fonte |
|---|---|---|---|---|
| Cava di argilla | 8 | 365 argilla | 12 strumenti | `clay_pit.con.lua:42-82` |
| Miniera di carbone | 8 | 320 carbone | 13 strumenti | `coal_mine.con.lua:44-85` |
| Piantagione di cotone | 21 | 274 lana | 17 fertilizzanti | `cotton_farm.con.lua:42-98` |
| Azienda agricola | 20 | 274 cereali + 183 verdure | 17 fertilizzanti | `farm.con.lua:44-106` |
| Area di pesca | 18 | 263 pesce | 12 strumenti | `fishing_grounds.con.lua:44-101` |
| Campo di disboscamento | 20 | 243 tronchi | 15 macchinari | `forest.con.lua:44-99` |
| Miniera di ferro | 8 | 365 minerale di ferro | 15 macchinari | `iron_ore_mine.con.lua:44-84` |
| Piattaforma petrolifera | 9 | 365 petrolio grezzo | 12 macchinari | `oil_platform.con.lua:45-96` |
| Pozzo petrolifero | 14 | 548 petrolio grezzo | 15 macchinari | `oil_well.con.lua:44-94` |
| Cava | 7 | 365 pietra | 12 strumenti | `quarry.con.lua:44-83` |
| Piantagione di gomma | 23 | 365 gomma | 17 fertilizzanti | `rubber_farm.con.lua:41-102` |
| Dragatore di sabbia | 9 | 365 sabbia | 15 macchinari | `sand_excavator.con.lua:44-92` |
| Cava di sabbia | 8 | 365 sabbia | 12 strumenti | `sand_pit.con.lua:44-84` |

- Il bonus viene estratto una volta per industria: **da +50 % a +150 %**, arrotondato all'1 % (`industryutil.lua:394-405`). La sezione Booster lo mostra come «+X %» (`industry_util.tl:428-434`). Con il parametro **Fattore incremento** vale invece +50 %, +75 %, +100 %, +125 % o +150 % (`industryutil.lua:289-299`).
- La finestra mostra il booster attivo finché dura il suo ultimo lotto (3 mesi), o appena la scorta contiene un lotto completo (`industry_util.tl:55-91`).
- Il lotto **non** cala con i lotti di terreno: una miniera piccola chiede tanti strumenti quanto una grande (`industryutil.lua:227-229`).
- I due bonus si moltiplicano: produzione × fattore lavoratori × (1 + bonus booster) (`industry_util.tl:42-104`).

## Il booster dei lavoratori

Metà dei posti (per esempio 10 su 20) deve essere occupata da abitanti **arrivati con le tue linee passeggeri** negli ultimi 2 anni (`industry_productivity_util.tl:3`, `industry_productivity_util.tl:35-48`, `industry_productivity_util.tl:74`). Il fattore è casuale tra ×1,5 e ×2,5, fisso per ogni industria; un edificio può fissarne uno proprio (`industry_productivity_util.tl:58-72`). I lavoratori solo assegnati non contano. Dettagli: [I lavoratori e il booster dei lavoratori](workers.html).

## Perché la mia industria non è potenziata?

1. **Non è un'industria primaria**: le fabbriche non hanno regola booster, solo il booster dei lavoratori (`steel_mill.con.lua:61-70`).
2. **Lotto incompleto**: la scorta deve contenere un lotto completo, ad es. 13 strumenti per una Miniera di carbone. Sotto i 4 lotti all'anno (52 strumenti) il bonus si ferma tra una consegna e l'altra.
3. **Carico sbagliato**: strumenti, macchinari o fertilizzanti a seconda dell'industria (tabella sopra).
4. **Lavoratori**: assegnati non basta; la sezione Booster conta gli arrivi («12/10») (`industry_react_util.tl:617-654`). Vedi [I lavoratori e il booster dei lavoratori](workers.html).

```tip scripts
**Per un potenziamento che non si ferma mai, consegna almeno 4 lotti completi l'anno** (52 attrezzi per una miniera di carbone). Ogni lotto mantiene il bonus 3 mesi.
```

## Quando chiude un'industria inutilizzata?

```diagram ind_closure
```

Il controllo passa ogni 100 aggiornamenti per ogni industria (`industries.script.tl:84-85`):

1. **Candidata**: nessun carico **caricato** su un veicolo e nessuno **consumato** per **5 anni** (dalla costruzione se mai) (`industries.script.tl:104-119`, `industries_config.res.lua:6`). Produrre non basta.
2. **Caso**: una candidata viene estratta a ogni controllo con una parte della probabilità annua dell'impostazione **Frequenza di chiusura delle industrie** (tabella sotto), così che in un anno si arriva a quella probabilità (`industries.script.tl:84-85`, `industries.script.tl:120-131`).
3. **Conto alla rovescia**: compare la notifica **Chiusura dell'industria**, con 2 anni (730 giorni) di tempo (`industries_config.res.lua:7`, `industry_close.script.tl:53-67`). Poi l'industria viene rimossa con i suoi tratti di strada (`industries.script.tl:147-155`, `industries.script.tl:193-222`, `industry_util.tl:560-601`).
4. **Salvata**: un solo carico o un consumo durante il conto alla rovescia lo annulla (`industries.script.tl:134-137`). Accettare un sussidio **Fornitura industriale** o **Trasporto di forza lavoro** per lei annulla il conto alla rovescia finché il sussidio è in corso (`subvention_util.tl:473-484`, `subvention_util.tl:478-483`). Non azzera il test dei 5 anni (`industries.script.tl:119`): se nulla viene caricato o consumato, l'industria può essere segnata di nuovo più tardi.

```tip scripts
**Notifica Chiusura dell'industria? Un solo carico o una sola consegna durante i 730 giorni la annulla.** Accettare un sussidio Fornitura industriale o Trasporto di forza lavoro per quell'industria la annulla finché il sussidio è in corso, ma continua a caricare qualcosa: il test dei 5 anni non viene azzerato.
```

| Frequenza di chiusura delle industrie | Probabilità all'anno da candidata | Metà delle candidate segnate dopo | Preimpostazione | Fonte |
|---|---|---|---|---|
| Mai | 0 | mai | Facile | `difficulty_util.tl:94` |
| Raramente (predefinito) | 1,1 % | circa 63 anni | Normale | `difficulty_util.tl:121` |
| Occasionalmente | 2,2 % | circa 32 anni | Difficile | `difficulty_util.tl:149` |
| Frequentemente | 4,4 % | circa 16 anni | – | `difficulty_util.tl:37` |
| Regolarmente | 8,8 % | circa 8 anni | Molto difficile | `difficulty_util.tl:176` |

La probabilità è 0,011 all'anno × 0, 1, 2, 4 o 8 (`mod.script.tl:171`, `mod.script.tl:202-203`, `difficulty_util.tl:37`). Le industrie di tua proprietà non chiudono mai, né quelle a sviluppo manuale; finché le chiusure sono in pausa (nel gioco base, solo durante il tutorial) non ne inizia nessuna e un conto alla rovescia in corso viene annullato (`industries.script.tl:94-102`, `mission_sim.script.tl:814`, `mission_sim.script.tl:850`).

```engine
Cosa conta come «caricato» e «consumato» (i registri itemsLoaded e itemsConsumed, ad es. se il carico booster conta), il flag manualDevelopment, e perché le industrie con un deposito sono escluse (`industries.script.tl:140-146`) dipendono dal motore. Così come cosa fa il motore di una regola booster che ha perso l'entrata (Ingresso disattivato).
```

## Nuove industrie

Il motore aggiunge nuove industrie durante la partita. La notifica è **Nuova industria fondata**: «Una stella dell'imprenditoria ha intravisto un'opportunità di profitto e ha fondato {industry}.» (`industry_spawn.script.tl:34-36`); la sua etichetta di tipo è **Industria fondata** (`industry_spawn.res.lua:6`). Nessuno script di gioco sceglie il posto, il tipo o il momento, e nessuno filtra ciò che il motore propone.

Cosa danno gli script al motore (`mod.script.tl:128-133`, `mod.script.tl:166-168`, `mod.script.tl:194-195`):

| Valore di configurazione | Valore | Significato |
|---|---|---|
| spawnTargetTimeSpan | 50 × 365,25 giorni standard | chiamato «tempo obiettivo»: 50 anni standard di tempo di gioco |
| spawnProbabilityExponent | 3,0 | esponente della probabilità di comparsa (formula nel motore) |
| spawnIndustries | spento nell'editor di mappe, acceso in partita | nessuna nuova industria nell'editor di mappe |
| industryDensity | 1 × **Densità industrie obiettivo** | il numero obiettivo di industrie |
| maxNumberPerArea, absoluteMinimum | 0,8 per km² (0,64 su console), 24 | un limite per superficie e un minimo (il loro uso è nel motore) |

**Densità industrie obiettivo** («Imposta l'obiettivo di densità delle industrie presenti sulla mappa.»): 5 gradini, ×2/3, ×5/6, ×1, ×1,2, ×1,5 (`difficulty_util.tl:55`, `difficulty_util.tl:85`).

- Si trova nelle impostazioni avanzate, parte economia (`advanced_settings.tl:287-291`), e non fa parte delle preimpostazioni da Facile a Molto difficile (`difficulty_util.tl:90-199`).
- Nel menu nuova partita, **Densità industrie** (le industrie all'inizio, stessi 5 fattori) imposta **Densità industrie obiettivo** allo stesso gradino (`new_game_or_map_settings_page.tl:159-166`, `new_game_react_util.tl:288-296`). Se le vuoi diverse, cambia poi l'obiettivo nelle impostazioni avanzate.
- **Nessuna impostazione la disattiva**: il gradino più basso è ×2/3. Solo l'editor di mappe non ha nuove industrie. Le mod possono farlo.
- Velocità: il tempo obiettivo è in giorni standard, come tutte le regole del tempo di gioco, quindi la velocità del calendario e un calendario in pausa non dovrebbero rallentarlo. Misurato con il calendario in pausa: in 1809 s di tempo di gioco sono comparse 3 nuove industrie, a 760 s e 728 s l'una dall'altra, quindi un calendario in pausa non le ferma. Misurato con [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) su 3 partite (circa 500 nuove industrie): le nuove industrie sono arrivate a circa **730 s** di tempo di gioco l'una dall'altra a ogni velocità del calendario (×4, ×1, ×0,5, ×0,25). Sono circa 45 giorni di calendario a ×0,25 e 2 anni a ×4.
- Prospezione risorse (sotto) usa la stessa chiamata del motore con una città, quindi nel motore esiste una comparsa «vicino a una città» (`company.script.tl:202`). Anche il tutorial la usa (`tutorial_init.tl:23-24`).

```engine
La formula dietro i 50 anni e l'esponente 3, come si conta la densità obiettivo (per area della mappa, per città?), quale tipo viene scelto e dove va (makeIndustrySpawnProposal) dipendono dal motore. Nessuno script spiega perché più industrie dello stesso tipo possono comparire vicine («nove miniere di carbone una accanto all'altra»), o perché alcune compaiono all'altro capo della mappa.
```

### Prospezione risorse

Il vantaggio aziendale **Prospezione risorse** cerca una nuova industria di quella risorsa vicino a una città che scegli: un tentativo al mese, con probabilità che sale dal 20 % al 60 %, per 6 mesi (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`). Se la risorsa ha più tipi di industria, vengono provati in ordine casuale (`company.script.tl:185-206`). Se tutti i tentativi falliscono, il permesso torna (`company.script.tl:106-110`).

## Buono a sapersi

- Spedisci da ogni industria primaria che vuoi far crescere: la produzione non spedita blocca l'espansione, qualunque siano i bonus.
- Porta il carico booster alle miniere e fattorie più grandi: il lotto costa uguale, il bonus segue i lotti di terreno.
- Le scorte non si deteriorano: puoi consegnare carico booster in anticipo, fino al limite della scorta (100).
- I bonus aumentano rumore e inquinamento: una Miniera di carbone passa da 10 di inquinamento a 20 con un bonus e 30 con due (`coal_mine.con.lua:99-117`).
- Meno nuove industrie: metti **Densità industrie obiettivo** al gradino più basso nelle impostazioni avanzate; non si può mettere a zero.
- Con l'impostazione predefinita un'industria inutilizzata chiude di rado; con Regolarmente, carica qualcosa ogni tanto.

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 5 anni, non 10, e la produzione non conta: solo il carico caricato su un veicolo o consumato. Dopo i 5 anni l'industria è solo candidata: ogni anno viene segnata con probabilità dall'1,1 % (Raramente) all'8,8 % (Regolarmente). Il conto alla rovescia dura 730 giorni, come detto. Il carico booster dà da +50 % a +150 % per industria, in lotti che durano 3 mesi. Nuove industrie: nessuna impostazione on/off, solo Densità industrie obiettivo da ×2/3 a ×1,5; nessuna nell'editor di mappe.
result: differs
```
