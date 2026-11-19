---
title: Velocità di carico e scarico
summary: Che cosa fa caricare un veicolo velocemente o lentamente a una fermata: il veicolo, le sezioni della piattaforma e le scorte che cedono o ricevono il carico.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-15
game: 40444
fact: ×2 | sezione di piattaforma specializzata
fact: ×0,25 | sezione sbagliata o treno troppo lungo
fact: ×4 | caso migliore: piattaforma e magazzino specializzati
---

Il tempo che un veicolo impiega a caricare o scaricare è la sua velocità di caricamento moltiplicata per due fattori: uno per la **piattaforma**, uno per le **scorte** dall'altra parte (magazzino, industria, cittadina).

```diagram loading_factors
```

## 1. Il veicolo

Ogni veicolo ha una velocità di caricamento di base, mostrata nel Negozio veicoli e nella finestra del veicolo ("2.0x"). Tutto ciò che segue la moltiplica.

## 2. Il fattore della piattaforma

Per il gioco una piattaforma non è una fila di moduli: è un **elenco di sezioni, una per classe di carico**, con le lunghezze di tutti i moduli di quella classe sommate.

```diagram loading_sections
```

| Vagoni… | Fattore | Fonte |
|---|---|---|
| su una sezione della loro classe (vagoni per merci sfuse, sezione per merci sfuse) | **×2** | `modular_station.script.lua:1042` |
| su una sezione universale | ×1 | `modular_station.script.lua:1042` |
| senza alcuna sezione della loro classe sulla piattaforma | **×0,25** (costante del tooltip di carico; il fattore in sé lo applica il motore) | `cargo_react_util.tl:60` |
| oltre la lunghezza della piattaforma (treno troppo lungo) | **×0,25** (costante del tooltip di carico; il fattore in sé lo applica il motore) | `cargo_react_util.tl:61` |

- Il fattore è una **media pesata sulla quota del treno**: se 3/4 dei vagoni corrispondono e 1/4 no, il fattore è ¾ × 2 + ¼ × 0,25 ≈ ×1,56 (`cargo_react_util.tl:63-70`, la stessa suddivisione che il gioco mostra come "Terminal parzialmente specializzato").
- **Dove** si fermano i vagoni sulla piattaforma non conta, contano solo le lunghezze sommate (misurato in gioco).
- Strada: i terminal per camion specializzati danno ×2 (`modular_terminal.script.lua:2956`); le piccole fermate su strada sono sempre ×1 (`small_stops.script.lua:19`).
- Le piattaforme per passeggeri sono ×1.

## 3. Il fattore delle scorte

Allo scarico, ogni unità va a un destinatario: un modulo di magazzino, un'industria o un edificio della cittadina. Le scorte del destinatario hanno il loro fattore.

| Destinatario | Fattore | Fonte |
|---|---|---|
| modulo di magazzino **specializzato** (liquidi, merci sfuse, merci ingombranti, merci generiche) | **×2** | `modules.script.lua:120`, `warehouse.script.lua:297-314` |
| magazzino **universale** | ×1 | `warehouse.script.lua:272-285` |
| industria | ×1 | misurato in gioco |

- Ogni modulo di magazzino chiede ×2, ma i moduli universali aggiungono solo capacità a **un'unica scorta universale condivisa**, che viene creata con ×1. Solo i moduli specializzati hanno una scorta propria con ×2.
- Il tooltip del gioco chiama questo fattore "Magazzino specializzato: +100%" (`cargo_react_util.tl:51-54`).
- Durante uno stesso scarico il gioco serve i destinatari **a turno**: per questo la velocità cambia mentre il treno scarica, quando parte del carico va a un magazzino e parte a un'industria (misurato in gioco).

```engine
Quale destinatario riceve ogni unità, e la moltiplicazione finale, sono decisi dal motore. I fattori qui sopra sono i dati che gli script gli forniscono; il risultato è stato verificato con i valori che il motore espone (sonda di [Platform Details](https://mod.io/g/transportfever3/m/platform-details), ottobre 2026).
```

## Che cosa mostra il gioco

- L'indicatore di caricamento appare come **accelerato** sopra ×1,5 e come **rallentato** sotto ×0,75 (`cargo_react_util.tl:119-122`).
- Passaci sopra con il mouse: il tooltip elenca "Terminal specializzato", "Specializzazioni non corrispondenti", "Terminal troppo corto" e "Magazzino specializzato", ciascuno con la sua percentuale (`cargo_react_util.tl:76-99`).

## Esempio

Un treno di 8 vagoni per merci sfuse, lungo 160 m, che scarica carbone.

| Stazione | Piattaforma | Destinatario | Fattore |
|---|---|---|---|
| piattaforma universale di 160 m | ×1 | acciaieria | **×1** |
| piattaforma per merci sfuse di 160 m | ×2 | acciaieria | **×2** |
| piattaforma per merci sfuse di 160 m | ×2 | magazzino specializzato per merci sfuse | **×4** |
| piattaforma per merci sfuse di 160 m | ×2 | magazzino universale | **×2** |
| piattaforma universale di 120 m (treno più lungo di 40 m) | ¾ × 1 + ¼ × 0,25 ≈ ×0,81 | acciaieria | **×0,81** |

## Dove viene scaricato il carico

Ogni fermata di una linea ha una lista **Carico**, nella finestra "Filtro carico" della fermata. Alla fermata il veicolo tiene a bordo le merci di quella lista; il resto viene scaricato in qualsiasi scorta del bacino d'utenza che lo accetti, magazzini compresi (misurato in gioco).

- È così che un treno finisce per svuotarsi in un magazzino a metà della sua linea. In gioco: a una fermata accanto a un magazzino, con solo plastica nella lista, gli attrezzi a bordo sono finiti nel magazzino, anche se era quasi pieno.
- Una piattaforma passeggeri non trasferisce merci: lì le merci restano a bordo (misurato in gioco).
- Per tenere le merci a bordo, aggiungile alla lista Carico di quella fermata.

```tip
**Le merci spariscono a una fermata vicino a un magazzino? Aggiungile alla lista Carico di quella fermata.** Tutto ciò che non è nella lista viene scaricato in una scorta a portata, e il magazzino non paga nulla.
```

| Opzione di "Filtro carico" | Che cosa fa | Fonte |
|---|---|---|
| "Forza scarico di tutte le merci all'arrivo" | tooltip: "Scarica le merci anche se le scorte sono piene"; le merci che non entrano vengono distrutte: il gioco indica la stazione come destinazione, e una stazione non consuma mai merci (misurato in gioco). Disattivata per una nuova fermata. | `cargofilter_window.tl:757`, `line_util.tl:477` |
| "Distrugge il carico all'arrivo se la configurazione cambia" | scarica o distrugge il carico a bordo quando a questa fermata aspetta merce per un'altra configurazione di carico del veicolo; quale delle due lo decide il motore | `cargofilter_window.tl:767` |
| "Sostituisci con nuovo carico se disponibile" | distrugge il carico tornato alla fermata dove era stato caricato, quando aspetta un carico più recente dello stesso tipo | `cargofilter_window.tl:778` |

- Con la prima opzione disattivata, l'icona della merce mostra "≤" e il tooltip "Scarica solo se scorte hanno capacità" (`cargofilter_window.tl:124`, `cargofilter_window.tl:158`).

## Più merci su una linea

- La lista **Carico** di una fermata è un sì/no per tipo di merce, **senza ordine**: il giocatore non può decidere quale merce viene caricata per prima. Le icone sono solo disegnate nell'ordine delle merci del gioco (`line_util.tl:472-476`, `line_util.tl:512`, `cargofilter_window.tl:533-535`).
- Un vagone o un camion che accetta più merci ha, per scomparto, più **configurazioni di carico**; la capacità dello scomparto è la più grande di esse, non la loro somma (`model_metadata_util.lua:682-733`, `vehicle_metadata_util.lua:27-37`). Quindi ne trasporta una sola alla volta.
- I nuovi veicoli hanno la scelta automatica della configurazione attivata per ogni scomparto (`vehicle_react_util.tl:339`), e il gioco non ha alcuna finestra per scegliere a mano la merce di un veicolo.
- Passeggeri e merci possono condividere una linea: gli script non rifiutano mai merci a una fermata perché accetta anche passeggeri (`line_util.tl:1383-1388`). Le merci vengono tolte solo da una fermata il cui terminal non può caricare né scaricare merci (`line_util.tl:556-561`).
- Con più merci, **Carico completo (qualsiasi)** e **Carico completo (tutto)** si comportano in modo diverso: vedi [Impostazioni di partenza: carico completo, Riempi livello e tempi di sosta](departure.html).
- Quando la configurazione non va bene, la linea mostra **Alcune configurazioni dei tipi di merce di questa linea sono in conflitto**, per esempio "Nessun veicolo sulla linea può trasportare parte delle merci configurate per il carico." (`line_warning.script.tl:10-36`).

```engine
L'ordine in cui vengono caricate più merci, come una scorta condivisa viene ripartita tra i veicoli in attesa e come un veicolo sceglie la sua configurazione di carico sono decisi dal motore.
```

## La configurazione automatica

Finché nessuno ha salvato una modifica nella finestra "Filtro carico" di una fermata, cosa che la disattiva per sempre su quella linea (`line_util.tl:497-500`, `cargofilter_window.tl:438`), il gioco riempie da solo le liste Carico ogni volta che la linea viene creata, una fermata viene aggiunta o tolta, le fermate vengono riordinate o viene aggiunto un punto di passaggio (`manager_window.tl:6938`, `:6786`, `:6845`, `:6879`, `:6963`). Spostare una fermata su un'altra stazione o piattaforma, e togliere o spostare un punto di passaggio, non la riavviano (`manager_window.tl:7077-7094`, `manager_window.tl:7194-7218`).

- Riparte da liste vuote, con i passeggeri nelle stazioni passeggeri (`line_util.tl:544-590`).
- Cerca produttori e consumatori solo tra industrie ed edifici della città: i magazzini non contano (`cargo_util.tl:518-526`).
- Mette una merce nella lista Carico di una fermata quando serve più avanti e alla fermata niente la accetta. Un magazzino conta come se accettasse tutto ciò che immagazzina (`line_util.tl:678-695`): a una fermata accanto a un magazzino che conserva quella merce, la merce resta fuori dalla lista e il treno la scarica lì.
- Non appena un filtro viene cambiato a mano, la linea è segnata come personalizzata (`cargofilter_window.tl:438`) e la configurazione automatica non la tocca più, nemmeno quando in seguito si aggiungono fermate (`line_util.tl:498`).

```engine
Gli script scrivono solo le liste Carico; lo scarico vero e proprio lo fa il motore. La regola qui sopra (ciò che non è nella lista viene scaricato in qualsiasi scorta che lo accetti) è stata osservata in gioco con [Platform Details](https://mod.io/g/transportfever3/m/platform-details), novembre 2026.
```

## Da sapere

- Le stazioni all'interno di un'industria sono sempre specializzate per il carico di cui quell'industria ha bisogno (wiki ufficiale).
- I moduli di magazzino specializzati congelano anche il tempo di consegna del carico che conservano (wiki ufficiale); un magazzino universale no.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) mostra entrambi i fattori per ogni veicolo a una piattaforma, e dove è finito il carico scaricato.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Specialized warehouses "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Sezione specializzata ×2, universale ×1, nessuna sezione corrispondente ×0,25, oltre la piattaforma ×0,25, media pesata sulla quota del treno; modulo di magazzino specializzato ×2, magazzino universale ×1.
result: refines
```
