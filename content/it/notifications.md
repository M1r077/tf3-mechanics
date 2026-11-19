---
title: Notifiche e avvisi
summary: Quando compare ogni avviso e quando sparisce: veicoli bloccati, stazioni non utilizzabili o sovraffollate, problemi di linee e fermate, valutazioni delle cittadine, condizione dei veicoli, industrie che chiudono, e quali avvisi sono nascosti nel registro per impostazione predefinita.
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40444
fact: 5 min | di tempo di gioco da fermo prima che un veicolo venga segnalato bloccato
fact: 20 % | di condizione che fa scattare l'avviso, finché il veicolo non torna sopra il 30 %
fact: 11 | tipi di notifica disattivati in una nuova partita
fact: 75 giorni | tra due controlli delle stazioni senza collegamento stradale
---

La maggior parte degli avvisi è **persistente**: uno script del gioco controlla la situazione più e più volte, l'avviso resta finché il problema c'è e finisce da solo quando è risolto. I controlli sono distribuiti a turno su 4 aggiornamenti, quindi un avviso può metterci un attimo a comparire o a sparire (`notifications.script.tl:13`, `notifications.script.tl:49`).

## Quando compare ogni avviso

| Avviso | Compare quando | Sparisce quando | Fonte |
|---|---|---|---|
| **Veicolo bloccato** | uno dei tuoi veicoli è in viaggio, non fermato da te, e ha velocità 0 da **5 minuti** di tempo di gioco | si muove di nuovo | `notifications.script.tl:557-580` |
| **Stazione non funzionante** | nessun terminal della stazione carica o scarica passeggeri e **nulla** è nella sua area di influenza (né magazzino, né industria, né edificio della cittadina), mentre una tua linea vi si ferma | qualcosa entra nell'area di influenza | `notifications.script.tl:602-617`, `notifications.script.tl:630-647`, `station_useless.script.tl:39` |
| **Stazione sovraffollata** | la stazione contiene più passeggeri o merci in attesa di quanti ne possa (traboccamento), mentre una tua linea vi si ferma; i passeggeri se ne vanno | il traboccamento finisce | `notifications.script.tl:599`, `notifications.script.tl:649-661`, `overcrowding.script.tl:23` |
| **Condizione veicolo** | un tuo veicolo è al **20 %** di condizione o meno | torna sopra il **30 %** | `notifications.script.tl:310-318` |
| **Valutazione cittadina molto scadente** | una delle valutazioni della cittadina scende a Pessima (sotto 1/6) | la valutazione torna a Mediocre o meglio | `notifications.script.tl:230-238`, `town_util.tl:763-769`, `town_util.tl:983-985` |
| **Valutazione cittadina in calo** | una valutazione è Scadente o Mediocre (sotto il 50 %) senza essere nell'avviso Pessima | la valutazione è Buona o meglio | `notifications.script.tl:240-248` |
| **Chiusura dell’industria** | un'industria avvia il conto alla rovescia di chiusura | chiude, o viene di nuovo usata in tempo | `notifications.script.tl:439-451`, `industry_close.script.tl:53-59` |
| **Nessun collegamento stradale** | una stazione non è collegata a una strada; controllato ogni **75 giorni** | il controllo successivo trova una strada | `notifications.script.tl:16`, `notifications.script.tl:423-436` |
| **Problema di scarico** | le merci di un veicolo non vengono mai scaricate sulla sua linea | vengono scaricate | `notifications.script.tl:277-290`, `cargo_rtc_warning.script.tl:28-37` |

- Un veicolo **nel deposito** non conta mai come bloccato: quel controllo è disattivato nello script (`notifications.script.tl:563-564`). Nemmeno un veicolo che hai fermato tu conta mai.
- Il controllo Stazione non funzionante guarda solo l'area di influenza. Una stazione che ha già passeggeri che salgono o scendono a un terminal non viene mai segnalata (`notifications.script.tl:606-610`).
- Come alzare una valutazione della cittadina: [Crescita delle cittadine](towns.html) e [Reputazione](reputation.html). Come funziona il conto alla rovescia di chiusura e come fermarlo: [Industrie](industries.html). Cosa fa la condizione a un veicolo: [Costi, manutenzione e prestiti](costs.html).

```engine
Se una stazione trabocca, se un veicolo ha un percorso, se una linea può raggiungere le sue stazioni e quanto può durare il viaggio tra due cittadine lo stabilisce il motore (calculateStationGroupCargo, getVehicleProblems, getLineProblems, getTownProblems). Gli script trasformano soltanto le sue risposte in avvisi.
```

```tip scripts
Veicolo bloccato, Inconveniente veicolo, Condizione veicolo, Stazione sovraffollata e Stazione non utilizzabile sono disattivati nel registro di una nuova partita. Attivali nelle impostazioni delle notifiche: sono gli avvisi che ti segnalano un ingorgo, un percorso mancante o una flotta usurata.
```

## Problemi di linee, fermate e veicoli

Arrivano direttamente dai controlli del motore sulle tue linee e sui tuoi veicoli; lo script dà un titolo a ciascuno.

| Avviso | Casi | Fonte |
|---|---|---|
| **Inconveniente di linea** | troppo poche stazioni; una stazione due volte di fila; stazioni incompatibili tra loro; non è stato possibile collegare delle stazioni; non è stato possibile collegare dei terminal alternativi | `line_warning.script.tl:46-128` |
| **La linea è configurata in modo errato** | un tipo di merce che non può essere caricato da nessuna parte, o scaricato da nessuna parte; nessun veicolo può trasportare una merce impostata per il carico; veicoli che non trasportano nessuna delle merci configurate, o veicoli solo merci su una linea passeggeri; nessuna merce configurata | `line_warning.script.tl:15-36`, `line_warning.script.tl:133` |
| **Inconveniente di stazione** | una fermata che i veicoli attuali non possono usare; una fermata passeggeri usata da veicoli merci (uno o tutti); una fermata merci usata da veicoli passeggeri; un tipo di merce configurato che non può essere caricato o scaricato a quella fermata | `line_station_warning.script.tl:6-87` |
| **Inconveniente veicolo** | nessun percorso elettrificato; nessun percorso per aerei di grandi dimensioni; nessun percorso per grandi navi; nessun percorso; due treni che si bloccano a vicenda | `vehicle_warning.script.tl:6-58` |
| **Città non collegata** | la strada tra due cittadine è interrotta; il viaggio tra due cittadine dura troppo | `town_warning.script.tl:7-19` |

- "Nessun percorso per aerei di grandi dimensioni" e "Nessun percorso per grandi navi" significano che il veicolo è troppo grande per una pista, un molo o una via navigabile della sua linea: vedi [Aerei](aircraft.html) e [Navi](ships.html).

## Registro, pop-up e impostazioni

- Ogni tipo di avviso si può disattivare nelle impostazioni delle notifiche ("Configura registro delle notifiche"). Un tipo disattivato non ha pop-up e non viene tenuto nel registro (`notification_util.tl:145-146`, `notification_log.tl:480`).
- In una **nuova partita**, 11 tipi sono disattivati fin dall'inizio: **Veicolo bloccato**, **Inconveniente veicolo**, **Condizione veicolo**, **Stazione sovraffollata**, **Stazione non utilizzabile**, **Stazione non collegata**, **Città non collegata**, **Merci non scaricate**, e i messaggi di avanzamento Prospezione, Campagna marketing e Inverdimento dell’industria dell'azienda (`stuck_vehicle.res.lua:7`, `vehicle_warning.res.lua:8`, `noroadconnection.res.lua:8`, `vehiclecondition.res.lua:8`, `overcrowding.res.lua:8`, `station_useless.res.lua:7`, `town_warning.res.lua:8`, `cargo_rtc_warning.res.lua:8`, `notification_util.tl:32-39`).
- I messaggi una tantum (nuovo veicolo, nuova costruzione, salita di grado, sovvenzioni) nascondono il pop-up dopo **60 secondi** di tempo di gioco; restano nella cronologia (`notification_util.tl:10`, `notifications.script.tl:85-94`).
- Una notifica finisce anche quando tutto ciò a cui punta è stato rimosso o ricostruito (`notifications.script.tl:95-107`).
- In una missione le notifiche partono in pausa, finché la missione non le attiva (`notifications.script.tl:700-704`).

## Da sapere

- Un avviso di blocco dopo 5 minuti non dice il perché. Guarda il veicolo: un segnale rosso, un segnale a senso unico nel verso sbagliato, o un avviso Inconveniente veicolo per lo stesso veicolo.
- "Stazione non funzionante" significa solo "ancora niente nell'area di influenza". Avvicina la stazione alle case, a un'industria o a un magazzino, oppure ingrandiscila.
- Una stazione sovraffollata perde passeggeri: aggiungi veicoli o accorcia l'intervallo (vedi [Partenza e attesa](departure.html)).

```check
official: La pagina User Interface del wiki ufficiale descrive il pulsante delle notifiche, il registro e i suoi filtri, senza le condizioni di ciascun avviso. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: Le condizioni sopra: bloccato dopo 5 minuti a velocità 0 in viaggio, condizione veicolo al 20 % fino al 30 %, valutazione cittadina Pessima sotto 1/6, collegamento stradale controllato ogni 75 giorni, 11 tipi disattivati per impostazione predefinita.
result: adds
```
