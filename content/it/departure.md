---
title: Impostazioni di partenza: carico completo, Riempi livello e tempi di sosta
summary: Quando un veicolo lascia una fermata: le tre modalità di partenza, il livello di riempimento di ogni carico e i tempi di sosta minimo, massimo e aggiuntivo.
domain: stations
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-15
fact: 600 s | Tempo arresto massimo predefinito di una nuova fermata
fact: 30 s / 60 s | Attesa aggiuntiva massima predefinita, strada / ferrovia
fact: 0–100 % | Riempi livello, per carico, della capacità del veicolo
---

Ogni fermata di una linea ha le sue impostazioni di partenza, nella finestra "Filtro carico" della fermata (clicca la fermata nella finestra della linea). Decidono **quanto** carica lì il veicolo e **quanto a lungo** può aspettare.

## Le impostazioni

| Impostazione | Valori | Nuova fermata | Fonte |
|---|---|---|---|
| "Carica se disponibile", "Carico completo (qualsiasi)", "Carico completo (tutto)" | una delle tre | Carica se disponibile (misurato) | `cargofilter_window.tl:798-821` |
| "Tempo arresto minimo" | 0–600 s, passo 10 | 0 s (misurato) | `cargofilter_window.tl:841-845` |
| "Tempo arresto massimo" | 0–600 s, oppure "---" (nessun limite, cursore in fondo) | **600 s** (misurato) | `cargofilter_window.tl:855-863` |
| "Attesa aggiuntiva massima" | 0–600 s, passo 10 | 60 s; 30 s a una stazione stradale o del tram senza ferrovia | `cargofilter_window.tl:827-831`, `line_util.tl:478-490` |
| "Riempi livello", per ogni carico caricato | 0–100 %, passo 1 | 100 % | `cargofilter_window.tl:698-704`, `line_util.tl:472` |

- Cliccando un tempo si apre un campo numerico: lì si possono digitare valori oltre 600 s (`cargofilter_window.tl:204-208`).
- I tre tempi restano in ordine tra loro: alzare il minimo o l'attesa aggiuntiva sopra il massimo alza anche il massimo (`cargofilter_window.tl:834-835`, `cargofilter_window.tl:848-849`, `cargofilter_window.tl:865-869`).
- Cambiarne uno qualsiasi segna la linea come personalizzata: la configurazione automatica non tocca più le sue liste Carico (`cargofilter_window.tl:438`, vedi [Velocità di carico e scarico](loading.html)). La configurazione automatica non cambia mai la modalità né i tempi (`line_util.tl:495-513`).

## Riempi livello: un limite per carico

Riempi livello è la quantità massima di quel carico che il veicolo prende a questa fermata, come quota della capacità del veicolo, arrotondata all'unità più vicina (misurato in gioco).

| Veicolo | Riempi livello | Parte con |
|---|---|---|
| camion, 15 posti, tronchi | 50 % | **8** (7,5 arrotondato per eccesso) |
| camion, 22 posti, tessuti | 70 % | **15** ogni volta (15,4) |
| treno, 18 posti, vetro | 48 % | al massimo **9** (8,64) |
| tram, 28 posti, carburante | 66 % | al massimo **18** (18,48) |

- Il carico già a bordo conta: un tram arrivato con 14 di carburante è partito con 18, non 14 + 18.
- Sopra il limite non viene caricato niente **e non viene scaricato niente** a causa sua: un camion arrivato con 22 di fertilizzanti (limite 11) è partito con 22.
- **0 %** significa: non caricare questo carico qui.
- Con una modalità di carico completo, il limite conta come pieno: camion di tronchi con Riempi livello al 50 % hanno aspettato circa 270 s e sono partiti con 8 su 15, non 15.
- Non esiste una percentuale di scarico. Lo scarico dipende dalla lista Carico e da "Forza scarico di tutte le merci all'arrivo" ([Velocità di carico e scarico](loading.html)).

## Carico completo e tempi di sosta

- **Carica se disponibile**: il veicolo prende ciò che c'è e parte.
- **Carico completo (tutto)**: il veicolo aspetta di essere pieno. Camion di tronchi hanno aspettato 460–566 s e sono partiti con 15 su 15.
- **Carico completo (qualsiasi)**: il veicolo parte quando un carico è pieno. Un treno per tronchi e assi è partito con 143 e 144 tronchi dopo 369–380 s; altre due partenze dopo circa 30 s con 57 e 118 tronchi non sono spiegate.
- **Tempo arresto massimo** termina l'attesa, anche senza niente caricato. Un treno di verdure in Carico completo (tutto) con un massimo di 120 s si è riempito (64 su 64) in circa 25 s, oppure è partito dopo 116–120 s con 26 o **0**. Con i 600 s predefiniti è partito con 26 su 64 dopo 596–600 s.
- **Tempo arresto minimo** è l'intera sosta, carico compreso, non tempo extra dopo di esso: con 60 s, i treni del vetro si sono fermati 55–61 s ogni volta, qualunque cosa caricassero.
- **Attesa aggiuntiva massima**: "Maximum wait time after loading to improve vehicle distribution" (`cargofilter_window.tl:828`). La finestra del veicolo mostra "Mantenimento distanza di sicurezza" mentre aspetta (`entity_window_util.tl:2279-2286`).
- **Più veicoli a una stessa fermata caricano contemporaneamente**, indipendentemente da quando è arrivato ciascuno (visto in gioco). Due camion di tronchi arrivati a circa 90 s di distanza sono partiti nello stesso secondo, ciascuno con 8. Come il carico venga diviso tra loro non è stato misurato.

```engine
Gli script memorizzano solo le impostazioni; quando un veicolo parte lo decide il motore.
```

Le regole qui sopra sono state misurate con il database di [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) (istantanee ogni 2 s, quindi i tempi di sosta sono ±2 s), novembre 2026.

## Da sapere

- Una lunga attesa con carico completo a una fermata dove arriva poco carico blocca la piattaforma: gli altri veicoli della linea si mettono in coda dietro.
- Un Tempo arresto massimo breve con carico completo può far partire i veicoli vuoti se tornano prima che arrivi nuovo carico.
- Una volta un treno in Carico completo (tutto) si è fermato 783–992 s con un massimo di 600 s. La causa non è stata trovata.

```check
official: "Full load (any): The vehicle will stop and wait until one cargo type is fully loaded. Full load (all): The vehicle will stop and wait until it is fully loaded." "In the vanilla game "all" and "any" only applies to trains and ships […] Any other vehicle type will wait for full load in both cases." Each cargo is loaded "to what percentage of a vehicle's total capacity". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles#departure_configuration))
scripts: Tre modalità di partenza, Tempo arresto minimo / massimo 0–600 s (o nessun limite), Attesa aggiuntiva massima 0–600 s (60 s, 30 s strada), Riempi livello 0–100 % per carico; misurato: Riempi livello limita il carico a bordo, arrotondato all'unità più vicina, e conta come pieno per il carico completo; Tempo arresto massimo termina un carico completo, anche vuoto; Tempo arresto minimo include il carico; i veicoli a una stessa fermata caricano insieme.
result: refines
```
