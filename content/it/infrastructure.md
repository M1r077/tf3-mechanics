---
title: Strade, binari, ponti e segnali
summary: Velocità, prezzo e manutenzione di ogni tipo di binario e di strada, quanto costano e cosa permettono ponti, gallerie, passaggi a livello e segnali, cosa cambiano davvero viali alberati e barriere antirumore, e dove si spiegano i depositi.
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40425
fact: 100 / 160 / 350 km/h | binario semplice, standard e ad alta velocità
fact: ×9 | prezzo e manutenzione del binario ad alta velocità rispetto a quello semplice
fact: +30% | prezzo della catenaria su un binario
fact: -65% | rumore di una strada o di un binario con barriera antirumore
---

Ogni tipo di strada e di binario ha una velocità massima, un prezzo al metro e una manutenzione al metro e all'anno, tutti scritti nel suo file. Ponti, passaggi a livello e alcune decorazioni stradali aggiungono un proprio limite di velocità. I costi qui sotto valgono con **Costi infrastrutture** e **Manutenzione infrastrutture** al 100% (vedi [Costi, manutenzione e prestiti](costs.html)).

## Binari

| Binario | Dal | Velocità massima | Costruzione per km | Manutenzione per km e anno | Fonte |
|---|---|---|---|---|---|
| Binari semplici | inizio | 100 km/h | 60.000 | 10.000 | `simple.street_template.lua:9`, `simple.street_template.lua:28`, `simple.street_template.lua:33` |
| Binari standard | 1930 | 160 km/h | 180.000 | 30.000 | `standard.street_template.lua:4`, `standard.street_template.lua:11`, `standard.street_template.lua:30`, `standard.street_template.lua:35` |
| Binari ad alta velocità | 1980 | 350 km/h | 540.000 | 90.000 | `high_speed.street_template.lua:4`, `high_speed.street_template.lua:11`, `high_speed.street_template.lua:30`, `high_speed.street_template.lua:35` |

- La **catenaria** costa il **30%** in più del binario (`mod.script.tl:24-25`). È disponibile dal 1921 sul binario semplice e dall'inizio di ogni tipo più recente (`simple_catenary.street_template.lua:4`). Nei file non costa nulla in più all'anno: la variante elettrica ha la stessa manutenzione (`simple_catenary.street_template.lua:34`).
- I tre tipi permettono la stessa pendenza e le stesse curve: **8,5%** quando costruisci (il cursore Inclina arriva fin lì), al massimo 13% per la forma del binario, e un raggio di curva di 55 m quando costruisci, almeno 40 m (`standard.street_template.lua:36-37`, `standard.street_template.lua:48-49`, `construction_react_util.tl:241-242`, `construction_react_util.tl:1821`).
- L'inquinamento del binario stesso cresce con il tipo: 2, 4 e 6 (`simple.street_template.lua:18`, `standard.street_template.lua:20`, `high_speed.street_template.lua:20`).

```engine
Quanto una curva riduce la velocità di un treno (gli speedCoeffs di ogni tipo di binario) e quale velocità lo strumento di costruzione mostra per una curva lo calcola il motore.
```

```tip scripts
Il binario ad alta velocità costa 9 volte quello semplice, in costruzione e ogni anno. Posalo solo dove i treni vanno davvero oltre i 160 km/h; altrove basta il binario standard, e quello semplice per le diramazioni merci lente.
```

## Strade

| Strada | Anni | Velocità massima | Costruzione per km | Manutenzione per km e anno | Fonte |
|---|---|---|---|---|---|
| Strada stretta (vecchia) | fino al 1940 | 20 km/h | 36.000 | 6.000 | `town_old_xsmall.street_template.lua:4-5`, `town_old_xsmall.street_template.lua:8`, `town_old_xsmall.street_template.lua:27`, `town_old_xsmall.street_template.lua:56` |
| Strada piccola (vecchia) | fino al 1940 | 40 km/h | 60.000 | 10.000 | `town_old_small.street_template.lua:8`, `town_old_small.street_template.lua:27`, `town_old_small.street_template.lua:56` |
| Strada grande (vecchia) | fino al 1940 | 60 km/h | 180.000 | 30.000 | `town_old_large.street_template.lua:8`, `town_old_large.street_template.lua:27`, `town_old_large.street_template.lua:88` |
| Strada stretta (nuova) | dal 1940 | 30 km/h | 120.000 | 20.000 | `town_new_xsmall.street_template.lua:4`, `town_new_xsmall.street_template.lua:11`, `town_new_xsmall.street_template.lua:30`, `town_new_xsmall.street_template.lua:59` |
| Strada piccola (nuova) | dal 1940 | 50 km/h | 180.000 | 30.000 | `town_new_small.street_template.lua:11`, `town_new_small.street_template.lua:30`, `town_new_small.street_template.lua:59` |
| Strada media (nuova) | dal 1940 | 50 km/h | 360.000 | 60.000 | `town_new_medium.street_template.lua:11`, `town_new_medium.street_template.lua:30`, `town_new_medium.street_template.lua:75` |
| Strada grande (nuova) | dal 1940 | 60 km/h | 540.000 | 90.000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:30`, `town_new_large.street_template.lua:91` |
| Strada extraurbana piccola (vecchia) | fino al 1940 | 60 km/h | 60.000 | 10.000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:29`, `country_old_small.street_template.lua:58` |
| Strada extraurbana piccola (nuova) | dal 1940 | 80 km/h | 180.000 | 30.000 | `country_new_small.street_template.lua:10`, `country_new_small.street_template.lua:31`, `country_new_small.street_template.lua:60` |
| Autostrada a corsia singola | dal 1940 | 100 km/h | 180.000 | 30.000 | `highway_new_small.street_template.lua:10`, `highway_new_small.street_template.lua:32`, `highway_new_small.street_template.lua:53` |
| Autostrada a due corsie | dal 1940 | 120 km/h | 360.000 | 60.000 | `highway_new_medium.street_template.lua:10`, `highway_new_medium.street_template.lua:32`, `highway_new_medium.street_template.lua:61` |
| Autostrada a tre corsie | dal 1940 | 120 km/h | 540.000 | 90.000 | `highway_new_large.street_template.lua:10`, `highway_new_large.street_template.lua:32`, `highway_new_large.street_template.lua:69` |
| Binari da tram (vecchi) | fino al 1910 | 40 km/h | 36.000 | 6.000 | `tram_old.street_template.lua:4-5`, `tram_old.street_template.lua:8`, `tram_old.street_template.lua:27`, `tram_old.street_template.lua:40` |
| Binari da tram (nuovi) | dal 1925 | 100 km/h | 120.000 | 20.000 | `tram_new.street_template.lua:4`, `tram_new.street_template.lua:9`, `tram_new.street_template.lua:29`, `tram_new.street_template.lua:42` |

- Il **cambio del 1940** rende le strade cittadine 10 km/h più veloci ma **tre volte** più care, in costruzione e ogni anno: una strada piccola passa da 60.000 a 180.000 per km.
- Le varianti media e grande delle strade extraurbane costano 2 e 3 volte quella piccola, alla stessa velocità (`country_new_large.street_template.lua:10`, `country_new_large.street_template.lua:31`).
- Aggiunte a una strada: una **corsia per autobus** +10%, un **binario del tram** +20%, un **binario del tram elettrico** +40% del prezzo della strada (`mod.script.tl:24-28`).
- Di solito il giocatore non possiede le strade, nemmeno quelle che ha costruito; gli strumenti stradali possono cambiare il proprietario di una strada (wiki ufficiale). Chi paga la manutenzione di una strada lo decide il motore.

## Viali alberati e barriere antirumore

| Strumento | Rumore | Inquinamento | Velocità massima | Dove | Fonte |
|---|---|---|---|---|---|
| Strumento viale (alberi) | -10% | -50% | **-25%** | strade con marciapiede, non su ponti né in galleria | `alley.edge.lua:39-40`, `alley.edge.lua:53-56` |
| Strumento barriera antirumore | -65% | nessun cambiamento | nessun cambiamento | strade e binari, non in galleria | `barrier_b.edge.lua:43`, `barrier_b.edge.lua:47`, `barrier_track_b.edge.lua:43` |

- Entrambi costano 100 e 10 all'anno nei loro file, come una strada al metro (`alley.edge.lua:8`, `alley.edge.lua:12`, `barrier_b.edge.lua:7`, `barrier_b.edge.lua:11`).
- I tipi di strada «con alberi» e «con barriere» del menu di costruzione sono le stesse strade con queste decorazioni già applicate (`town_new_medium_trees.street_template.lua:12-14`). Il menu di costruzione somma i loro effetti (`construction_react_util.tl:2116-2139`).
- Quindi una strada con alberi è **più lenta di un quarto**: una strada media nuova con alberi permette circa 38 km/h invece di 50.

```tip scripts
Contro il rumore usa la barriera antirumore: -65% e nessuna perdita di velocità. Gli alberi sono lo strumento contro l'inquinamento (-50%), ma rallentano la strada di un quarto.
```

Come le cittadine valutano rumore e inquinamento: [Inquinamento e rumore](emission.html).

## Ponti e gallerie

| Ponte | Anni | Velocità massima | Per | Prezzo base | Fonte |
|---|---|---|---|---|---|
| Ponte in pietra | dall'inizio | 90 km/h | binari, strade | 200 | `stone.bridge.lua:169-170`, `stone.bridge.lua:181-183`, `stone.bridge.lua:193` |
| Ponte a cavalletto | fino al 1970 | 60 km/h | un tipo per i binari, uno per le strade | 100 | `trestle.bridge.lua:200-201`, `trestle.bridge.lua:212-214`, `trestle.bridge.lua:226`, `trestle_s.bridge.lua:212` |
| Ponte in acciaio | dal 1940 | 140 km/h | binari, strade | 200 | `steel.bridge.lua:243`, `steel.bridge.lua:259`, `steel.bridge.lua:269` |
| Ponte sospeso | dal 1940 | 180 km/h | binari, strade | 600 | `suspension.bridge.lua:277`, `suspension.bridge.lua:294`, `suspension.bridge.lua:304` |
| Ponte in cemento | dal 1970 | 280 km/h | binari, strade | 200 | `concrete.bridge.lua:162`, `concrete.bridge.lua:176`, `concrete.bridge.lua:187` |
| Ponte strallato | dal 2000 | 220 km/h | binari, strade | 750 | `cable.bridge.lua:214`, `cable.bridge.lua:231`, `cable.bridge.lua:240` |
| Ponte ad arco tirante | dal 2010 | 350 km/h | binari, strade | 650 | `tarch.bridge.lua:253`, `tarch.bridge.lua:270`, `tarch.bridge.lua:280` |

- Il limite del ponte si applica **in aggiunta** a quello del binario: una linea ad alta velocità su un ponte in acciaio lì va a 140 km/h. Prima del 1970 nessun ponte permette più di 180 km/h, prima del 2010 nessuno permette 350 km/h.
- Le **gallerie** (Tunnel in pietra, Tunnel in cemento dal 1970) **non hanno limiti di velocità** nei loro file, e lo stesso prezzo base di 600 (`tunnel_a.tunnel.lua:187-188`, `tunnel_a_car.tunnel.lua:185`, `tunnel_b.tunnel.lua:191-194`).
- I prezzi di ponti e gallerie seguono Costi infrastrutture (`post_run_util.tl:50-51`).

```engine
Il prezzo base di un ponte o di una galleria viene trasformato dal motore in un prezzo al metro, con l'altezza o la profondità (costFactors); la wiki ufficiale dice che dipende dalla lunghezza e dall'altezza dal suolo o dalla profondità sotto di esso. Lo stesso prezzo base può quindi dare conti molto diversi. Le gallerie costano Reputazione presso la cittadina (vedi [Reputazione delle cittadine](reputation.html)).
```

```tip scripts
Per una linea veloce che attraversa una valle prima del 1970, il ponte sospeso (180 km/h) è l'unico ponte più veloce di 140 km/h; una galleria non ha alcun limite.
```

## Passaggi a livello e segnali

| Cosa | Anni | Velocità massima del binario | Prezzo | Fonte |
|---|---|---|---|---|
| Incrocio semplice | 1850 - 1925 | 120 km/h | 4.000 | `era_a_eu.rcr.lua:14-17`, `era_a_eu.rcr.lua:26` |
| Incrocio con semibarriera | 1925 - 1975 | 160 km/h | 16.000 | `era_b_eu.rcr.lua:15-18`, `era_b_eu.rcr.lua:27` |
| Incrocio con semibarriera moderno | dal 1975 | 160 km/h | 16.000 | `era_c_eu.rcr.lua:15-17`, `era_c_eu.rcr.lua:26` |
| Segnale di percorso (semaforico fino al 1950, luminoso dal 1950) | tutti | - | 9.000, manutenzione 1.500 all'anno | `signal_path_a.con.lua:4-5`, `signal_path_a.con.lua:10-11`, `signal_path_c.con.lua:4-5` |

- Un passaggio a livello limita il binario a 160 km/h al massimo: le linee ad alta velocità hanno bisogno di ponti o gallerie per superare le strade.
- Ogni segnale può essere impostato a **Senso unico** (`signal_path_a.con.lua:51-52`). Come i segnali dividono il binario in blocchi è spiegato nella pagina Railway Signals della wiki ufficiale.

## Depositi e edifici di manutenzione

Quanto costano depositi ed edifici di manutenzione, quanti veicoli servono e in che raggio: [Veicoli](vehicles.html) e [Costi, manutenzione e prestiti](costs.html).

## Buono a sapersi

- Prima del 1940 migliorare le strade cittadine costa poco; dopo il 1940 ogni strada cittadina nuova o ricostruita costa il triplo e il triplo di manutenzione.
- Su una linea veloce controlla ogni ponte e ogni passaggio a livello: il più lento fissa lì la velocità.
- La velocità conviene solo se porta più viaggi (vedi [Perché perdo soldi?](money.html)).

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: Stesse velocità delle tabelle ufficiali per binari, strade e ponti. Nei file i limiti dei ponti valgono anche per le strade, le gallerie non ne hanno, i passaggi a livello limitano i binari a 120 o 160 km/h, gli alberi rallentano una strada del 25% e riducono l'inquinamento del 50% ma il rumore solo del 10%, mentre le barriere antirumore riducono il rumore del 65% senza rallentare.
result: refines
```
