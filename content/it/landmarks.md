---
title: Monumenti, celebrazioni ed elementi divertenti
summary: Quanto costa ogni monumento in merci, quando si sblocca e cosa dà ai veicoli della sua città, come l'impostazione Livello risorse per luoghi di riferimento lo scala, e cosa fanno davvero celebrazioni, fuochi d'artificio, dirigibili e UFO.
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40444
fact: 9 + 3 | monumenti: 9 nel gioco base (gradi dal 2 al 15), altri 3 con i pacchetti DLC (grado 1)
fact: +20 % / +25 % / -20 % / -25 % | velocità massima, inquinamento o comfort per i veicoli della sua città
fact: ×0 a ×4 | di merci necessarie, con l'impostazione Livello risorse per luoghi di riferimento
fact: 2-4 anni | tra due UFO
---

Un monumento si costruisce come un cantiere: lo sblocchi con un grado aziendale, lo piazzi e poi gli **consegni merci**. Quando il cantiere ha tutte le sue merci, il monumento è finito e dà un bonus ai veicoli della **sua città**. La sede centrale è un edificio a parte con regole proprie (vedi [Grado aziendale, vantaggi e sede centrale](company.html)).

## I monumenti

Merci con **Livello risorse per luoghi di riferimento** ×1 (Normale).

| Monumento | Grado | Merci da consegnare | Bonus per i veicoli della sua città | Fonte |
|---|---|---|---|---|
| **Anfiteatro** | 2 | 800 pietra | veicoli stradali: rumore **-25 %** | `arena.con.lua:10`, `arena.con.lua:20-26`, `arena.con.lua:39` |
| **Grande faro** | 5 | 1.200 pietra, 200 carburante | navi: velocità massima **+20 %** | `lighthouse.con.lua:10`, `lighthouse.con.lua:14`, `lighthouse.con.lua:29`, `lighthouse.con.lua:48` |
| **Castello dell'airone bianco** | 7 | 1.200 pietra, 400 assi | treni: inquinamento **-20 %** | `white_heron_castle.con.lua:10`, `white_heron_castle.con.lua:14`, `white_heron_castle.con.lua:28`, `white_heron_castle.con.lua:47` |
| **Museo navale** | 9 | 600 tronchi, 600 assi, 200 tessuti | navi: comfort **+25 %** | `ship_museum.con.lua:10-18`, `ship_museum.con.lua:36`, `ship_museum.con.lua:55` |
| **Castello di Neuschwanstein** | 10 | 1.000 pietra, 600 assi, 200 tinture | veicoli stradali: comfort **+25 %** | `neuschwanstein.con.lua:10-18`, `neuschwanstein.con.lua:36`, `neuschwanstein.con.lua:55` |
| **Statua della Libertà** | 11 | 800 pietra, 400 acciaio, 400 lamine di metallo | navi: inquinamento **-20 %** | `statue_of_liberty.con.lua:10-18`, `statue_of_liberty.con.lua:38`, `statue_of_liberty.con.lua:57` |
| **Palazzo d'estate** | 13 | 600 pietra, 300 assi, 300 tinture, 300 mobili | aerei: inquinamento **-20 %** | `summer_palace.con.lua:10-22`, `summer_palace.con.lua:44`, `summer_palace.con.lua:63` |
| **Teatro dell'opera** | 14 | 800 pietra, 400 vetro, 400 lamine di metallo, 400 tessuti | treni: comfort **+25 %** | `opera_house.con.lua:10-22`, `opera_house.con.lua:44`, `opera_house.con.lua:63` |
| **Parlamento** | 15 | 800 pietra, 400 assi, 400 vetro, 400 mobili | veicoli stradali, treni, navi e aerei: velocità massima **+20 %** | `westminster.con.lua:10-22`, `westminster.con.lua:45`, `westminster.con.lua:79` |

**Monumenti DLC.** Due pacchetti DLC ne aggiungono altri tre, sbloccati dal grado 1. I loro file sono nelle cartelle DLC del gioco (Deluxe Upgrade Pack e Pre-order Pack), fuori dai file base indicizzati da questo wiki, quindi qui non hanno link alle fonti.

| Monumento | DLC | Grado | Merci da consegnare | Bonus per i veicoli della sua città |
|---|---|---|---|---|
| **Torre Eiffel** | Deluxe Upgrade Pack | 1 | 400 acciaio | veicoli stradali: velocità massima **+25 %** |
| **Taj Mahal** | Deluxe Upgrade Pack | 1 | 800 pietra | aerei: rumore **-25 %** |
| **Grande piramide** | Pre-order Pack | 1 | 800 pietra | treni: velocità massima **+25 %** |

- Ogni monumento si sblocca una sola volta, con il suo grado; come sale il grado è spiegato in [Grado aziendale, vantaggi e sede centrale](company.html).
- Nei loro file i monumenti non costano nulla da costruire né all'anno: solo le merci (`arena.con.lua:59-64`).
- Il cantiere immagazzina metà di ogni merce alla volta, quindi servono almeno due consegne di ciascuna (`arena.con.lua:13-18`).

## Costruire un monumento

- Il cantiere ha **4 fasi**. Avanza man mano che arrivano le merci: fase 2 a un terzo di tutte le merci, fase 3 a due terzi, finito al 100 %. Ogni merce conta solo fino alla sua quantità, quindi la pietra in più non compensa le assi mancanti (`landmarks.script.tl:34-46`).
- Il bonus funziona solo quando il monumento è **finito** (`landmark_util_serialized.tl:393-395`). Appare allora il messaggio «Costruzione ultimata» (`landmarks.script.tl:49-61`).
- L'impostazione **Livello risorse per luoghi di riferimento** moltiplica tutte le merci: Nessuno ×0, Ridotto ×0,5, Normale ×1, Elevato ×2 o Molto elevato ×4. I livelli sono Facile ×0,5, Normale ×1, Difficile ×2, Molto difficile ×4. A ×0 un monumento è finito appena piazzato (`difficulty_util.tl:40`, `difficulty_util.tl:107`, `difficulty_util.tl:135`, `difficulty_util.tl:162`, `difficulty_util.tl:189`, `landmarks.script.tl:38`, `landmarks.script.tl:46`).

## Chi riceve il bonus

- Il bonus va alla città **più vicina al monumento**, e ai veicoli del tipo di trasporto indicato la cui città più vicina è quella città (`landmark_util.tl:6-47`, `landmarks.script.tl:208-236`).
- Quando un veicolo entra nell'area di un'altra città, prende i bonus di quella città e perde i vecchi (`landmarks.script.tl:279-299`).
- I bonus di più monumenti nella stessa città **si sommano**: due +20 % di velocità massima danno +40 % (`landmark_util.tl:46`, `vehicle_modifier.script.tl:3-16`).

```engine
Quale città sia la «città più vicina» di un monumento o di un veicolo in movimento lo decide il motore (getConstructionClosestTown, closestTown). Anche il modo in cui il motore trasforma +25 % di comfort o +20 % di velocità massima in viaggi ed entrate è compito del motore.
```

```tip scripts
Metti il Parlamento nella città dove circola la maggior parte dei tuoi veicoli: +20 % di velocità massima per ogni tipo di trasporto. Un secondo +20 % viene dal Grande faro per le navi nella stessa città. L'obiettivo L'ombelico del mondo chiede 10 monumenti finiti con la stessa città più vicina; la sede centrale non conta, perché non ha merci da consegnare. Il gioco base contiene 9 monumenti e i pacchetti DLC ne aggiungono 3 (contati); non si sa se L'ombelico del mondo sia raggiungibile senza un DLC (vedi [Obiettivi](achievements.html)).
```

## Celebrazioni

Una celebrazione è la piccola festa mostrata sopra una città quando qualcosa accade per la prima volta. Aumenta anche la **Reputazione** della città, ma solo quando la Reputazione non è già piena.

| Evento | Reputazione | Fonte |
|---|---|---|
| il primo passeggero sale su una delle tue linee nella città | +50 % | `celebrations.script.tl:228-252` |
| le prime merci consegnate alla città | +50 % | `celebrations.script.tl:187-198` |
| la città sale di livello | +50 % | `celebrations.script.tl:260-272` |
| le prime merci consegnate a un'industria | +20 % alla città più vicina | `celebrations.script.tl:202-219` |

- Una città che sale di livello riceve anche i **fuochi d'artificio**, a meno che non siano disattivati (`town_growth.script.tl:108-112`).
- Come funziona la Reputazione: [Reputazione](reputation.html).

## Elementi divertenti

- Un **dirigibile** sorvola una città quando vi avvii una Campagna marketing (`fun_elements.script.tl:112-117`).
- Un **UFO** appare ogni **2-4 anni** di tempo di gioco, scelto a caso, quando non ce n'è nessuno sulla mappa (`fun_elements.script.tl:10`, `fun_elements.script.tl:79-91`). Cliccalo per l'obiettivo Incontri ravvicinati.
- Nessuno di essi cambia l'economia.

## Da sapere

- Scegli la città prima di costruire: il bonus non segue le tue linee, solo i veicoli vicini a quella città.
- A Molto difficile un monumento richiede quattro volte le merci: il Parlamento chiede allora 3.200 pietra e 1.600 di ciascuna delle altre merci.

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: Nove monumenti base, uno per grado dal 2 al 15, più tre monumenti DLC al grado 1, ciascuno costruito con merci consegnate in 4 fasi, scalate da Livello risorse per luoghi di riferimento ×0 a ×4. Una volta finito, ognuno dà un bonus (+20 % o +25 % di velocità massima, -20 % di inquinamento, -25 % di rumore o +25 % di comfort) ai veicoli di un tipo di trasporto nella sua città più vicina; i bonus si sommano. Le celebrazioni aggiungono il 50 % o il 20 % di Reputazione; un UFO arriva ogni 2-4 anni.
result: adds
```
