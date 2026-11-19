---
title: Grado azienda, vantaggi e sede centrale
summary: Cosa fa salire il grado della tua azienda, cosa sblocca ogni grado, come funzionano permessi e prospezioni, cosa dà davvero la sede centrale e quanto ti costa un grado più alto.
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40444
fact: 15 | gradi azienda, da Apprendista a Magnate
fact: ×12,5 | di popolazione mondiale necessaria per il grado 15, rispetto all'inizio
fact: ×0,75 | di entrate al grado 15 con Inflazione Normale
fact: 0 | gradi persi quando la popolazione cala
---

Il grado della tua azienda non viene dal denaro né dalle consegne: viene dalla **popolazione dell'intera mappa**. Ogni nuovo grado sblocca vantaggi (monumenti, prospezioni, campagne marketing, Inverdimento dell’industria, moduli della sede centrale) e, con l'impostazione **Inflazione**, abbassa anche un po' tutte le tue entrate.

## Cosa fa salire il grado

- Il gioco ricorda la **popolazione mondiale all'inizio** della partita: gli abitanti di tutte le cittadine (`company.script.tl:392-396`, `company_util.tl:365-371`).
- Poi confronta la popolazione mondiale **più alta** mai raggiunta con quel valore iniziale (`company_growth.script.tl:25-27`). Il valore sale soltanto: le cittadine che si riducono non ti costano mai un grado.
- Il grado 1 si raggiunge al valore iniziale, il grado 15 a circa **12,5 volte** tanto (`company_progression_util.tl:6-14`, `company_progression_util.tl:95-120`, `town_growth_function.tl:13-20`).
- Non c'è grado nelle missioni della campagna né nell'editor di mappe (`company_growth.script.tl:74-79`).

| Grado | Ruolo | Popolazione mondiale, rispetto all'inizio |
|---|---|---|
| 1 | Apprendista | ×1 |
| 2 | Meccanico | ×1,02 |
| 3 | Ingegnere | ×1,08 |
| 4 | Coordinatore | ×1,2 |
| 5 | Esperto | ×1,4 |
| 6 | Caposquadra | ×1,7 |
| 7 | Supervisore | ×2,1 |
| 8 | Responsabile | ×2,6 |
| 9 | Direttore | ×3,3 |
| 10 | Direttore senior | ×4,2 |
| 11 | AD | ×5,3 |
| 12 | Capo consiglio | ×6,7 |
| 13 | Vicepresidente | ×8,3 |
| 14 | Presidente | ×10,2 |
| 15 | Magnate | ×12,5 |

I rapporti sono calcolati dagli script per una popolazione iniziale di 50.000 o più (`company_progression_util.tl:6-14`, `company_static_util.tl:6-24`). Su una mappa piccola sono un po' più alti per i gradi intermedi (il grado 8 richiede ×2,85 con 5.000 abitanti); i gradi 1 e 15 restano a ×1 e ×12,5.

- Il grado segue quindi la **crescita delle cittadine**: le cittadine crescono grazie ai tuoi passeggeri e alle tue merci, vedi [Crescita delle cittadine](towns.html).
- I primi gradi arrivano in fretta, gli ultimi richiedono cittadine molte volte più grandi.

## Un nuovo grado si applica nella finestra dell'azienda

Quando la popolazione supera una soglia, compare una **notifica di promozione**; cliccandola si apre la finestra dell'azienda su quel grado (`company_growth.script.tl:96-107`, `company_notification_rank_up.script.tl:8-9`).

- I nuovi vantaggi si sbloccano solo quando quel grado viene **selezionato nella finestra dell'azienda**: la finestra invia allora lo sblocco (`company.tl:420-423`, `company_growth.script.tl:55-62`). I menu di costruzione controllano questo grado applicato (`company_util.tl:92`, `company_util.tl:171-178`).
- Il moltiplicatore delle entrate della sezione successiva segue il grado **raggiunto**, applicato o no (`company_growth.script.tl:47-48`).

```tip scripts
Dopo una promozione, clicca la notifica (o apri la finestra dell'azienda e seleziona il nuovo grado) per ottenere i vantaggi. Aspettare non ti dà nulla: le entrate sono già calate.
```

## Quanto costa un grado più alto: l'impostazione Inflazione

Con l'**Inflazione**, tutte le entrate da merci e passeggeri calano in modo uniforme da ×1 al grado 1 fino a un minimo al grado 15 (`company_progression_util.tl:25-40`, `company_growth.script.tl:159-170`).

| Inflazione | Entrate al grado 15 | Fonte |
|---|---|---|
| Nessuna | ×1 (nessun cambiamento) | `difficulty_util.tl:50`, `mod.script.tl:695-698` |
| Ridotta | ×0,9 | |
| Normale | ×0,75 | |
| Elevata | ×0,6 | |
| Molto elevata | ×0,5 | |

- A Normale, ogni grado costa circa l'1,8 % delle entrate: ×0,96 al grado 3, ×0,875 al grado 8, ×0,75 al grado 15.
- L'Inflazione non aumenta alcun costo; i costi seguono l'anno del calendario (vedi [Costi, manutenzione e prestiti](costs.html)).
- Un grado più alto rende anche più rare le nuove offerte di contratti (vedi [Contratti](subsidies.html)).

## Permessi

La maggior parte dei vantaggi è limitata da **permessi**. Un grado dà permessi per un vantaggio; ogni edificio o utilizzo ne consuma uno (`company_util.tl:33-80`, `company_util.tl:206`).

- I permessi **si sommano** di grado in grado: un vantaggio che ne dà 1 al grado 3 e 1 al grado 5 ne consente 2 dal grado 5 in poi (`company_util.tl:51-56`).
- Un edificio restituisce il suo permesso quando viene demolito: il gioco conta ciò che è in piedi (`company_util.tl:143-163`, `company_util.tl:203-206`).
- Prospezioni, campagne marketing e inverdimento consumano un permesso all'avvio (`company.script.tl:416-423`, `company.script.tl:459-462`, `company.script.tl:496-500`). Il menu di costruzione mostra allora **Già utilizzato** o **Ricarica** (`company_util.tl:207-226`).
- Il permesso **Marketing** torna **5 anni** dopo ogni campagna (`marketing.res.lua:6-7`, `company.script.tl:66-94`).

| Vantaggio | Permessi | Fonte |
|---|---|---|
| Sede centrale | 1 al grado 1 | `hq.res.lua:6` |
| Campagna marketing | 1 al grado 4, torna dopo 5 anni | `marketing.res.lua:6-7` |
| Inverdimento dell’industria | 1 ai gradi 3, 6, 9, 12 e 15 | `industry_greenify_tool.script.tl:101-102` |
| Impianto di bonifica | 15 al grado 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Monumenti | uno ciascuno: Anfiteatro 2, Grande faro 5, Castello dell'airone bianco 7, Museo navale 9, Castello di Neuschwanstein 10, Statua della Libertà 11, Palazzo d'estate 13, Teatro dell'opera 14, Parlamento 15 | `arena.con.lua:39`, `lighthouse.con.lua:48`, `white_heron_castle.con.lua:47`, `ship_museum.con.lua:55`, `neuschwanstein.con.lua:55`, `statue_of_liberty.con.lua:57`, `summer_palace.con.lua:63`, `opera_house.con.lua:63`, `westminster.con.lua:79` |

Cosa fa ogni vantaggio: [Reputazione](reputation.html) (campagna marketing), [Inquinamento e rumore](emission.html) (inverdimento, Impianto di bonifica).

## Prospezioni

Una prospezione cerca una risorsa vicino a una cittadina e, se riesce, vi fonda una nuova industria.

| Risorsa | Grado | Fonte |
|---|---|---|
| Pesce | 2 | `exploration_fish.res.lua:9-11` |
| Argilla | 3 | `exploration_clay.res.lua:9-11` |
| Petrolio grezzo | 4 | `exploration_crude_oil.res.lua:9-11` |
| Cereali, verdure | 4, **un solo permesso condiviso** (Industria) | `exploration_grain.res.lua:9`, `exploration_vegetables.res.lua:9`, `permit_key_farm.res.lua:6` |
| Tronchi | 5 | `exploration_logs.res.lua:9-11` |
| Carbone, minerale di ferro | 6 | `exploration_coal.res.lua:9-11`, `exploration_iron_ore.res.lua:9-11` |
| Pietra, lana | 8 | `exploration_stone.res.lua:9-11`, `exploration_wool.res.lua:9-11` |
| Sabbia | 9 | `exploration_sand.res.lua:9-11` |
| Gomma | 12 | `exploration_rubber.res.lua:9-11` |

- Ogni risorsa ha **un** permesso, consumato all'avvio della prospezione (`company.script.tl:451-462`).
- Dura fino a **6 mesi**. Una volta al mese prova a piazzare l'industria, con una probabilità che sale dal 20 % al 60 % nei 6 mesi (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`).
- Un tentativo fallisce anche quando il gioco non trova posto per quell'industria vicino alla cittadina (`company.script.tl:199-210`).
- Se l'ultimo tentativo fallisce, **il permesso torna** e una notifica lo segnala (`company.script.tl:106-126`, `company.script.tl:170-181`).
- Può essere attiva una sola prospezione alla volta per cittadina e risorsa (`company.script.tl:442-447`).

```engine
Dove può sorgere la nuova industria (makeIndustrySpawnProposal vicino alla cittadina) lo decide il motore: una prospezione di pesce lontana dall'acqua, o una cittadina senza terreno libero intorno, semplicemente fallisce e restituisce il permesso.
```

## La sede centrale

| Cosa | Valore | Fonte |
|---|---|---|
| Prezzo e manutenzione | gratis, nessuna manutenzione | `headquarter.script.tl:526-527` |
| Permesso | 1, al grado 1 | `headquarter.con.lua:6-7`, `hq.res.lua:6` |
| Crescita della cittadina | +5 % alla cittadina più vicina | `headquarter.script.tl:510-515`, `landmark_util.tl:51-70` |
| Posti di lavoro | 24 | `headquarter.con.lua:16`, `headquarter.script.tl:505-508` |

- Il +5 % è un bonus sul tasso di crescita di quella cittadina, quindi non fa nulla quando il tasso è 0 % (vedi [Crescita delle cittadine](towns.html)).
- I **moduli** costano 50.000 ciascuno e sono limitati da permessi che crescono con il grado (`hq_module_m.module.lua:83`, `hq_module_m.module.lua:137`).
- Solo due moduli hanno un bonus nei file: **Edificio medio** +1 % di crescita della cittadina (`hq_module_m.module.lua:139-142`) ed **Edificio grande** +1 % di Recupero reputazione (`hq_module_l.module.lua:169-172`). Il bonus di recupero non viene letto da nessuna valutazione della cittadina (vedi [Reputazione](reputation.html)). Gli altri moduli sono decorativi.
- Ogni file di modulo inizia anche con una tabella che dà +5 % di crescita, ma niente nel file la usa (`hq_corner_l.module.lua:148-159`, `hq_statue.module.lua:46-57`). Viene sommato solo il bonus nei `metadata` del modulo (`headquarter_addon.script.tl:18-29`).

| Modulo | Permessi ottenuti al grado (×2 = due) | Totale al grado 15 |
|---|---|---|
| Bandiera da terreno | 1 ×2, 6, 7, 8, 9, 11, 12, 13, 14 | 10 |
| Edificio angolare | 3, 5, 7 ×2, 9, 11, 13, 15 | 8 |
| Edificio medio | 2, 4, 10 ×2, 15 ×2 | 6 |
| Edificio grande | 5, 6, 10, 12 | 4 |
| Balconata | 8 ×2, 14 ×2 | 4 |
| Fontana grande | 10 ×2, 14 ×2 | 4 |
| Cupola | 6, 15 ×2 | 3 |
| Bandiera da tetto | 7, 10, 13 | 3 |
| Campo da tennis | 11, 12, 14 | 3 |
| Albero secolare | 13, 15 ×2 | 3 |
| Statua | 14 ×2 | 2 |
| Piscina | 15 | 1 |

Fonti: la riga `rankAndPermits` di ogni file di modulo (`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`).

```tip scripts
Metti la sede centrale nella cittadina che vuoi far crescere più in fretta e aggiungici Edifici medi: sono gli unici moduli con un bonus di crescita.
```

## Da sapere

- Per salire di grado, fai crescere le cittadine: più passeggeri e merci verso più cittadine, con buone valutazioni. Il denaro in banca non conta.
- Pianifica monumenti e prospezioni: ognuno arriva una sola volta, a un grado fisso.
- Su una mappa con Inflazione, una promozione è buona per i vantaggi e cattiva per le entrate. A Normale, tutta la strada fino al grado 15 costa un quarto di tutte le entrate.

```check
official: "The company rank depends on the population of the map. … Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Stessa regola: la popolazione mondiale più alta raggiunta, confrontata con quella iniziale, ×12,5 per il grado 15; mai persa. Un nuovo grado va selezionato nella finestra dell'azienda per sbloccarne i vantaggi, mentre l'Inflazione abbassa subito le entrate. Solo due moduli hanno un bonus (Edificio medio +1 % di crescita, Edificio grande +1 % di Recupero reputazione, che nessuna valutazione legge); gli altri sono decorativi.
result: refines
```
