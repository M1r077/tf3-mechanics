---
title: Obiettivi
summary: Cosa controlla lo script del gioco per ogni obiettivo della partita libera e quando, quali contano solo veicoli, merci e animali del gioco base, e quali controlli sono lasciati al motore.
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-17
game: 40425
fact: 17 | obiettivi sbloccati dallo script del gioco stesso
fact: 500 m | altezza del primo vagone di un treno a una fermata per Fermata in vetta
fact: < 1 % | di Reputazione della cittadina per Non è colpa mia
fact: 10 | monumenti che devono avere la stessa cittadina più vicina per L'ombelico del mondo
---

La wiki ufficiale elenca 41 obiettivi. Lo script del gioco (`achievements.script.tl`) ne sblocca **17** da solo e alimenta **9 contatori tra le partite**; gli altri (campagna, meteo, dimensione delle cittadine, magazzino, interessi, potenziamenti, auto, 1900-2000, vapore negli anni 2000) sono controllati altrove, dal motore o dalla piattaforma. Ogni controllo chiede prima al motore se l'obiettivo può ancora essere sbloccato; è lì che si decide se mod o impostazioni lo bloccano (`achievements.script.tl:632`, `achievements.script.tl:510`).

## Obiettivi controllati dallo script

| Obiettivo | Cosa controlla lo script | Fonte |
|---|---|---|
| **C'è posta per te** | un'unità di merce arriva a destinazione | `achievements.script.tl:221-225`, `achievements.script.tl:632-636` |
| **Liberati dal giogo** | una sovvenzione completata | `achievements.script.tl:241-244`, `achievements.script.tl:638-642` |
| **Raffica di commesse** | 10 sovvenzioni completate senza nessuna fallita in mezzo; una sovvenzione fallita riporta il conteggio a 0 | `achievements.script.tl:243-249`, `achievements.script.tl:644-648` |
| **Custode** | la valutazione delle consegne di una cittadina passa a **Eccellente** | `achievements.script.tl:270-276`, `towns.script.tl:30-33`, `achievements.script.tl:650-654` |
| **Sviluppo urbano** | una cittadina sale di livello | `achievements.script.tl:253-255`, `town_growth.script.tl:92` |
| **Incremento della domanda** | una cittadina ottiene la domanda di un nuovo tipo di merce | `achievements.script.tl:257-259`, `achievements.script.tl:668-672` |
| **Non è colpa mia** | la Reputazione di una cittadina **scende** sotto l'**1 %** | `achievements.script.tl:261-267`, `towns.script.tl:36-39` |
| **Promozione** | l'azienda sale di grado | `achievements.script.tl:280-282`, `achievements.script.tl:680-684` |
| **Scalata sociale** | l'azienda raggiunge il grado più alto | `achievements.script.tl:284-290`, `achievements.script.tl:686-690` |
| **Paesaggista** | piazzi alberi, e solo alberi, in una costruzione (niente rimosso, non con il rimboschimento) | `achievements.script.tl:346-377` |
| **Perfezionista** | la stessa stazione viene demolita, ricostruita, demolita e ricostruita, in quest'ordine, senza che un'altra stazione venga costruita o rimossa nel frattempo | `achievements.script.tl:304-341`, `achievements.script.tl:694-710` |
| **L'ombelico del mondo** | esattamente 10 monumenti completati hanno la stessa cittadina più vicina | `achievements.script.tl:382-395`, `achievements.script.tl:713-721` |
| **Fermata in vetta** | uno dei tuoi treni arriva a una fermata con il primo vagone a più di **500 m** | `achievements.script.tl:407-417`, `achievements.script.tl:723-727` |
| **Gioco di piattaforme** | uno dei tuoi elicotteri arriva a una fermata di una piattaforma petrolifera | `achievements.script.tl:420-450`, `achievements.script.tl:729-733` |
| **Storia della nautica** | ogni modello di nave del gioco base è in servizio nello stesso momento su una delle tue linee di navi | `achievements.script.tl:735-776` |
| **Incontri ravvicinati** | fai clic su un UFO | `achievements.script.tl:793-806` |
| **Custode del tempo** | cambi l'ora del giorno a mano | `achievements.script.tl:839-844` |

- **Perfezionista** conta solo una costruzione che aggiunge o rimuove una stazione intera: aggiungere un binario o un modulo a una stazione non conta (`achievements.script.tl:301-302`).
- **L'ombelico del mondo** conta ogni monumento quando è completato, per la cittadina più vicina in quel momento (`achievements.script.tl:386`).
- **Storia della nautica** viene controllato solo quando un modello di nave che non si è mai fermato arriva a una fermata; guarda i veicoli delle tue linee di navi, non le navi in un deposito (`achievements.script.tl:736`, `achievements.script.tl:750-766`).
- **Non è colpa mia** richiede la Reputazione, non un'altra valutazione: vedi [Reputazione delle cittadine](reputation.html).

```tip scripts
Fermata in vetta controlla l'altezza del primo vagone quando il treno si ferma, non l'altezza dell'edificio della stazione. Costruisci la stazione su una montagna sopra i 500 m e fai arrivare lì un treno.
```

## Contatori tra le partite

Continuano da una partita all'altra (la piattaforma li salva). Lo script invia solo ciò che è cambiato dall'ultimo controllo.

| Contatore | Obiettivo | Cosa conta | Fonte |
|---|---|---|---|
| Lunghezza dei binari | **Attorno al globo** | l'aumento della lunghezza totale del registro (in km); non viene tolto nulla quando demolisci | `achievements.script.tl:511-523` |
| Popolazione | **Popolazione mondiale** | l'aumento della popolazione della mappa, dalla popolazione al caricamento della partita | `achievements.script.tl:512`, `achievements.script.tl:525-533` |
| Passeggeri | **Al servizio del passeggero** | passeggeri che hanno finito un viaggio su una delle tue linee | `achievements.script.tl:236-238`, `achievements.script.tl:535-541` |
| Merci | **Dal mittente al destinatario** | unità di merce consegnate | `achievements.script.tl:543-549` |
| Climi | **Magnate senza rivali** | il clima della mappa, quando l'azienda vi raggiunge il grado più alto | `achievements.script.tl:551-567` |
| Entrate | **Dottor Male** | le tue entrate sommate, in miliardi | `achievements.script.tl:202-204`, `achievements.script.tl:569-590` |
| Tipi di merce | **Boss delle consegne** | ogni tipo di merce del gioco base consegnato una volta | `achievements.script.tl:20-22`, `achievements.script.tl:230-232`, `achievements.script.tl:592-607` |
| Veicoli | **Amante dei viaggi** | ogni modello di veicolo del gioco base che arriva una volta a una fermata | `achievements.script.tl:16-18`, `achievements.script.tl:469-481`, `achievements.script.tl:609-625` |
| Animali | **Amante degli animali** | ogni animale del gioco base su cui fai clic una volta | `achievements.script.tl:24-26`, `achievements.script.tl:809-834` |

- Veicoli, merci e animali delle mod non contano mai per questi contatori: vengono presi solo i file del gioco base (`::/vehicle`, `::/cargos`, `::/animal`) (`achievements.script.tl:16-26`).
- Per Amante dei viaggi un veicolo deve **arrivare a una fermata** di una linea; comprarlo non basta.

```engine
Se un obiettivo può ancora essere sbloccato (isAchievementUnlockable), se i contatori sono disattivati (areStatsDisabled), i traguardi di ogni contatore e i 24 obiettivi che non sono nello script sono gestiti dal motore e dalla piattaforma. La wiki ufficiale dice che gli obiettivi in genere non sono disponibili con mod non cosmetiche o con impostazioni di gioco diverse dai valori standard.
```

## Da sapere

- Ogni obiettivo da «prima volta» è controllato rispetto al controllo precedente: serve un **nuovo** evento in una partita in cui l'obiettivo è ancora aperto; una vecchia sovvenzione o un vecchio grado di un salvataggio non contano di nuovo (`achievements.script.tl:633`, `achievements.script.tl:779`).
- Il tuo grado, le sovvenzioni e la Reputazione sono spiegati in [Grado dell'azienda, vantaggi e sede centrale](company.html), [Sovvenzioni](subsidies.html) e [Reputazione delle cittadine](reputation.html).

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: 17 obiettivi e 9 contatori sono nello script. Precisa i testi ufficiali: Custode significa la valutazione delle consegne che raggiunge Eccellente, Non è colpa mia una Reputazione sotto l'1 %, Fermata in vetta il primo vagone sopra i 500 m, Perfezionista demolire-ricostruire-demolire-ricostruire la stessa stazione, e Storia della nautica tutti i modelli di nave del gioco base su linee nello stesso momento. Solo veicoli, merci e animali del gioco base contano per i contatori.
result: refines
```
