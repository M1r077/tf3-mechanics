---
title: Crescita delle cittadine: XP, valutazioni e dimensioni
summary: Da dove arriva l'XP di una cittadina, come le sei valutazioni determinano il suo indice di crescita e di quanto la ingrandisce ogni livello.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
fact: 0% | di crescita quando una valutazione è Pessima
fact: ×1,5 | di XP per ogni livello successivo (1.000 per il livello 2)
fact: ×40 | di dimensioni dopo 17 livelli guadagnati
---

Una cittadina cresce solo grazie ai **tuoi** trasporti: i passeggeri che arrivano con le tue linee e le merci consegnate ai suoi edifici le danno XP. Le sue valutazioni decidono quanta parte di quell'XP conta, e ogni livello guadagnato rende la cittadina più grande.

```diagram town_xp
```

## Da dove arriva l'XP

| Origine | XP grezzo | Fonte |
|---|---|---|
| Passeggero che arriva **con le tue linee** a un edificio della cittadina | 5 · 10 · 20: casa e lavoro o negozio nella stessa cittadina, in una cittadina vicina, in una cittadina più lontana | `town_growth.script.tl:649-701`, `town_growth_config.res.lua:6` |
| Unità di merce consegnata a un edificio della cittadina | 10 · 20 · 40 per merci di livello 0 · 1 · 2 | `town_growth.script.tl:642`, `town_growth_config.res.lua:5` |
| Ricompensa di commessa "esperienza della cittadina" | una quota del livello attuale, anch'essa × indice di crescita | `subvention_util.tl:144-152`, `town_growth.script.tl:608` |

- L'XP va alla cittadina dell'edificio dove il passeggero o la merce **arriva**. Un pendolare tra due cittadine dà XP a entrambe: alla cittadina del lavoro all'andata, a quella di residenza al ritorno.
- I viaggi da o verso un'**industria** non danno XP (`town_growth.script.tl:680-683`). Nemmeno i viaggi a piedi o in auto: contano solo i viaggi fatti con le tue linee (`town_growth.script.tl:656`).
- Il solo passare del tempo non dà nulla: l'XP per tick è 0 (`town_cargo_util.tl:6`).
- Livelli delle merci: **0** mattoni, cemento, pesce, carburante, carne, assi, verdure; **1** bevande, libri, indumenti, mobili, macchinari, cibo in scatola, strumenti; **2** veicoli (`placementparamsutil.lua:506-616`).

Ogni XP grezzo viene moltiplicato per l'**indice di crescita** della cittadina (`town_growth.script.tl:60-63`). La finestra della cittadina lo mostra come **Indice di crescita:**.

## L'indice di crescita

L'indice di crescita deriva da due valutazioni della finestra della cittadina (`town_util.tl:607-633`, `town_util.tl:954-962`):

1. **Autorità cittadina**: la **più bassa** delle sue sei valutazioni, non la media (`town_util.tl:754-784`).
2. **Forniture**: la media dei livelli di fornitura di passeggeri e merci, arrotondata per eccesso (`town_util.tl:555-589`).

```diagram growth_matrix
```

- Ogni valutazione ha sei livelli: un valore tra 0 e 1 diviso in sesti (`town_util.tl:983-985`). **Eccellente** richiede 5/6 = 83% o più.
- Con **una sola** valutazione Pessima, l'autorità è Pessima e l'indice di crescita è **0%**: la cittadina si ferma, qualunque cosa tu consegni.
- Il 100% richiede un'autorità Eccellente con forniture Ottima o migliori, oppure un'autorità Ottima con forniture Eccellente.
- La tua **Sede centrale** aggiunge +5% alla cittadina più vicina, e la maggior parte delle sue estensioni aggiunge un altro +5% ciascuna (`headquarter.script.tl:510-515`, `landmark_util.tl:51-70`). Questo bonus moltiplica l'indice, quindi a 0% non fa nulla.

## Le sei valutazioni dell'autorità

| Valutazione | Che cosa la abbassa | Fonte |
|---|---|---|
| **Reputazione** | modifiche del terreno, demolizione di edifici della cittadina, rimozione di alberi; ogni collegamento principale interrotto con un'altra cittadina −1/3 | `town_util.tl:396-404`, `town_util.tl:1608` |
| **Traffico** | strade congestionate nella cittadina | `town_util.tl:445-456` |
| **Felicità** | quota di viaggiatori insoddisfatti (si presumono almeno 15 persone) | `town_util.tl:479-503` |
| **Consegna** | quota di consegne di merci in ritardo (vedi [Entrate dalle merci](income.html)) | `town_util.tl:505-519` |
| **Rumore** | rumore della cittadina: 65 dB o meno → valutazione piena, 80 dB → 0 | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Inquinamento** | inquinamento medio dell'area della cittadina: 60 dB → piena, 74 dB → 0 | `town_util.tl:413-431`, `emission_config.tl:23-24` |

Le impostazioni di **sensibilità** di ogni valutazione (sette livelli, il primo è No) spostano questi limiti; No significa valutazione sempre piena (`difficulty_util.tl:44-49`).

## Forniture

- **Passeggeri**: utilizzo linea della cittadina × 2, quindi **un utilizzo linea del 50% dà la valutazione piena** (`town_util.tl:546-553`).
- **Merci**: offerta ÷ domanda di ogni quartiere (commerciale, industriale); conta il quartiere **migliore**, non la media (`town_util.tl:521-529`).
- Una cittadina senza nulla da rifornire conta come forniture piene. Una cittadina che non riceve da te né passeggeri né merci conta come "nessuna consegna": indice di crescita 0% (`town_util.tl:565-588`).

Le nuove richieste di merci arrivano con i livelli (`placementparamsutil.lua:618-660`): una commerciale e una industriale all'inizio, una seconda commerciale al livello 5, una seconda industriale al livello 7, una terza commerciale al livello 9, una terza industriale al livello 11. Vengono aggiunte solo dopo che la cittadina ha ricevuto almeno una consegna di merci (`town_growth.script.tl:286-288`). Il gioco preferisce merci che poche altre cittadine richiedono già (`town_growth.script.tl:258-266`).

## Livelli e dimensioni

- Il livello 2 richiede 1.000 XP, ogni livello successivo 1,5 volte più del precedente (`town_cargo_util.tl:81-97`, `town_growth_config.res.lua:7`): livello 5 a 8.125 XP in totale, livello 10 a circa 75.000, livello 18 (Metropoli grande, l'ultimo) a circa 2 milioni.
- Le cittadine posizionate con più case partono più in alto: livello 2, 3 o 4 (`town_cargo_util.tl:43-54`).
- La **dimensione obiettivo** dipende dai livelli guadagnati dall'inizio, compreso il progresso verso il successivo (`town_cargo_util.tl:100-110`, `town_growth_function.tl:4-11`):

```diagram town_size
```

- La dimensione in più viene ripartita tra i quartieri residenziale, commerciale e industriale in base a quanto ciascuno è servito: utilizzo dei passeggeri per le case, fornitura di merci per gli altri (`town_growth.script.tl:404-421`). Quando un quartiere raggiunge il 40% della cittadina, la quota massima che può prendere della nuova dimensione scende dal 100% al 50% man mano che arriva al 50% della cittadina (limiti simili valgono su tutta la mappa) (`town_growth.script.tl:509-522`). Se nessun quartiere è servito, la cittadina non cresce, anche con XP (`town_growth.script.tl:415`).

```engine
Il motore calcola l'utilizzo delle linee, la velocità del traffico, le mappe del rumore e dell'inquinamento e l'elenco delle consegne in ritardo, e costruisce le nuove case e strade. La quota minima che un quartiere riceve sempre (townGrowthMinDistrictFraction) è un valore del motore.
```

## Domanda di merci e scorte degli edifici

- La domanda di una cittadina è la somma dei suoi **edifici**. Ogni edificio commerciale o industriale ha una piccola scorta in entrata per ogni merce richiesta dalla cittadina: capacità ÷ 4, arrotondata per eccesso (`townbuildingutil.lua:226-251`). Il gioco annota che questa dimensione della scorta "is currently nowhere shown in the UI" (per ora non è mostrata da nessuna parte nell'interfaccia) (`townbuildingutil.lua:249`).
- La domanda nella finestra della cittadina è il limite totale di queste scorte; l'offerta contata per la valutazione è limitata alla domanda (`town_util.tl:95-99`, `town_util.tl:194-198`). Le cittadine più grandi chiedono di più perché hanno più edifici.
- La finestra dell'edificio mostra una **Valutazione consumo**: quanto velocemente l'edificio usa le sue merci rispetto al suo massimo (`town_building.tl:103-132`).
- XP e pagamento arrivano quando un'unità entra nella scorta di un edificio (`town_growth.script.tl:620-642`).
- Una fermata raggiunge solo gli edifici nella sua area di influenza. Le loro scorte possono essere piene mentre alla cittadina nel complesso mancano ancora merci: allora le merci che non entrano **restano sul veicolo**, a meno che non sia spuntato **Forza scarico di tutte le merci all'arrivo** ("Scarica anche con scorte al completo.") (`cargofilter_window.tl:757-763`), che distrugge ciò che non entra (vedi [Velocità di carico e scarico](loading.html)).
- Le merci rimaste a bordo generano la notifica **Merci non scaricate**: "Unità del carico di {vehicle} non scaricate sulla linea: {cargoCount}" (`cargo_rtc_warning.res.lua:6`, `cargo_rtc_warning.script.tl:28-41`).
- **Richiesta di carico delle cittadine** ("Seleziona il numero massimo di carichi richiesti dalle cittadine."): 2, 4 o 6, predefinito 2 (`difficulty_util.tl:54`, `difficulty_util.tl:83`, `mod.script.tl:173`, `mod.script.tl:205`). Gli script aggiungono le richieste in base al livello (vedi sopra) e passano questo valore al motore.

```engine
La velocità con cui un edificio consuma la sua scorta (consumeFrequency), quale edificio di un'area di influenza riceve ogni unità, che cosa succede alle merci portate in giro e come il motore usa Richiesta di carico delle cittadine sono gestiti dal motore.
```

## Posso impedire a una cittadina di crescere?

- In una partita normale **non c'è nessuna impostazione** per una dimensione massima delle cittadine (`difficulty_util.tl:90-199`).
- In **modalità sandbox** e nell'editor di mappe, la finestra della cittadina ha una scheda **Capacità quartiere obiettivo** con **Attiva sviluppo cittadina** (`town_eow.script.tl:1041-1052`, `town_eow.script.tl:1170-1171`, `town_eow_editor_initial_capacity.res.lua:6`). Se non è spuntata, la cittadina non riceve XP e non viene ridimensionata; la finestra mostra **Sviluppo cittadina non attivo** (`town_growth.script.tl:28`, `town_growth.script.tl:345`, `town_eow.script.tl:107`).
- Senza sandbox, gli unici modi sono indiretti: una cittadina cresce solo con i tuoi passeggeri e le tue merci, e una sola valutazione Pessima la ferma (vedi sopra).

## Da sapere

- **Correggi prima la valutazione peggiore**: l'autorità è il minimo, quindi migliorare le altre non serve a nulla.
- I passeggeri tra **due cittadine** danno 2 volte (vicine) o 4 volte (più lontane) l'XP dei viaggi all'interno di una sola cittadina, e a entrambe le cittadine.
- Le merci commerciali sono solo di livello 0–1; solo i **veicoli** (industriali) danno 40 XP per unità, e di norma una cittadina li richiede solo dalla sua terza richiesta industriale (livello 11).
- Una cittadina lontana dalla tua Sede centrale non riceve il suo bonus: lo riceve solo la cittadina più vicina.

```check
official: "A town needs 1,000 total XP to reach level 2. The XP required for each following level-up is 1.5 times the amount required for the previous level-up." Passeggeri 5 / 10 / 20 XP, merci 10 / 20 / 40 XP. "The Town Authority rating is determined by the lowest of six ratings." "A line usage of 50% gives the maximum rating." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Stessi numeri. Indice di crescita 0–100% a passi del 20% da autorità × forniture; una valutazione Pessima ferma la crescita; nessun XP dai viaggi verso le industrie; richieste di merci aggiunte solo dopo una prima consegna di merci; la terza richiesta commerciale non può essere di livello 2 nel gioco base (non esiste una merce commerciale di livello 2); dimensioni ×40 dopo 17 livelli guadagnati.
result: refines
```
