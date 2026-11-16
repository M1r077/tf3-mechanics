---
title: Inquinamento e rumore
summary: Che cosa emette rumore e inquinamento, quando un edificio emette di più, come lo valutano le città e che cosa fanno davvero l'Inverdimento dell’industria e l'Impianto di bonifica.
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
game: 40425
fact: 65–80 dB | rumore in città: valutazione piena a 65, zero a 80
fact: 60–74 | inquinamento in città, sulla scala logaritmica degli script (non un livello sonoro): valutazione piena a 60, zero a 74
fact: −80 % | rumore e inquinamento di un'industria inverdita
fact: 700 m | raggio dell'Impianto di bonifica
---

Veicoli, binari, strade, stazioni, depositi, magazzini e industrie emettono tutti **Rumore** e **Inquinamento**. Due valutazioni della città, **Rumore** e **Inquinamento**, confrontano ciò che raggiunge la città con limiti fissi. Una cattiva abbassa la valutazione dell'**Autorità cittadina** e quindi la crescita (vedi [Città](towns.html)).

## Quando un edificio emette di più

Uno script del gioco imposta l'emissione di quattro tipi di edifici ogni pochi aggiornamenti, tra un livello tranquillo e uno intenso (`emissions.script.tl:12-18`):

| Edificio | Emette di più quando | Fonte |
|---|---|---|
| **Industria** | produce, e ancora con ogni potenziamento (merci o lavoratori); quando tutte le sue scorte in uscita sono piene insieme, il suo livello si dimezza: in produzione → ferma, potenziato due volte → in produzione | `emissions.script.tl:152-194` |
| **Stazione** | è più affollata: persone e merci in attesa rispetto alla capacità | `emissions.script.tl:211-222` |
| **Deposito**, **stazione di manutenzione** | più veicoli usano la sua manutenzione | `emissions.script.tl:223-234` |
| **Magazzino** | le sue scorte sono più piene | `emissions.script.tl:237-250` |

- Ogni industria ha i suoi quattro livelli: ferma, in produzione, potenziata una volta, potenziata due volte (`industryutil.lua:464-475`; il valore predefinito 0 / 78 / 84 / 88 vale solo per un'industria senza i propri). La maggior parte emette un po' anche da ferma: una miniera di carbone va da 2 → 10 → 20 → 30 di inquinamento, i suoi campi 2 → 30 → 60 → 90 (`coal_mine.con.lua:99-135`, vedi [Industrie](industries.html)).
- Un'industria con tutte le scorte in uscita piene scende a metà del suo livello (`emissions.script.tl:172-182`): servirla ne aumenta l'inquinamento.
- Anche veicoli e binari emettono; un veicolo in cattivo stato emette di più con l'impostazione **Effetto manutenzione veicoli** (vedi [Costi, manutenzione e prestiti](costs.html)).

## Che cosa mostra il menu di costruzione

| Edificio | Rumore | Inquinamento | Fonte |
|---|---|---|---|
| Porto | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| Aeroporto | 8–56 | 80–560 | `airport.tl:28-29` |
| Stazione ferroviaria | 25 | 45–350 | `modular_station.con.lua:97-98` |
| Deposito ferroviario | 50 | 100 | `rail_depot.con.lua:32-33` |
| Deposito stradale e tram | 40 | 80 | `road_depot.con.lua:30-31`, `tram_depot.con.lua:32-33` |
| Stazione sotterranea | 40 | 80 | `underground_station.con.lua:75-76` |
| Stazione camion e autobus | 1–10 | 12–76 | `modular_terminal.con.lua:67-68`, `modular_terminal.con.lua:121-122` |
| Stazioni di manutenzione | 20 | 40–50 | `road_maint_station.con.lua:30-31`, `rail_maint_station.con.lua:30-31` |
| Magazzino | 20 | 50 (universale) o 100 (specializzato) | `warehouses/warehouse.tl:51`, `warehouses/warehouse.tl:73-74` |

Due valori sono l'intervallo mostrato dal menu, dal più basso al più alto, come l'intervallo di prezzo accanto (`construction_desc_react_util.tl:733-746`); un valore è una cifra unica. In funzione, ogni edificio emette di più quanto più è attivo (tabella sopra). Tieni porti, aeroporti e grandi stazioni merci lontano dalle case.

## Come lo valuta una città

| Valutazione | Misura | Valutazione piena | Zero | Fonte |
|---|---|---|---|---|
| **Rumore** | rumore agli edifici della città | 65 dB o meno | 80 dB | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Inquinamento** | inquinamento medio per cella di 16 m dell'area della città (area contata tra 5 e 10 km²), convertito sulla scala logaritmica degli script («dB») | 60 o meno | 74 | `town_util.tl:413-431`, `emission_config.tl:23-30` |

- Solo il quartiere **Residenziale** soffre il rumore; gli edifici commerciali e industriali no (wiki ufficiale). La finestra di una casa mostra il rumore nella sua posizione (`town_building.tl:165-183`).
- L'inquinamento è mediato su tutta l'area: una fonte lontana dal centro pesa meno in una città grande che in una piccola.
- Le impostazioni **Sensibilità rumore** e **Sensibilità inquinamento** spostano i limiti: una sensibilità doppia conta come +3 dB (`town_util.tl:426-428`, `town_util.tl:439-441`). L'inquinamento usa la stessa scala logaritmica del rumore (10·log10): +3 «dB» significa il doppio dell'inquinamento. Non è un livello sonoro.

| Livello | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Fonte |
|---|---|---|---|---|---|---|---|---|
| Rumore | Mai (sempre piena) | ×¼ | ×½ | ×1 | ×1,4 | ×1,8 | ×3,5 | `difficulty_util.tl:48` |
| Inquinamento | Mai (sempre piena) | ×¼ | ×½ | ×1 | ×1,7 | ×3 | ×5 | `difficulty_util.tl:49` |

Le preimpostazioni Facile, Media, Difficile e Molto difficile usano i livelli 3, 4, 5 e 6 (`difficulty_util.tl:114-115`, `difficulty_util.tl:142-143`, `difficulty_util.tl:169-170`, `difficulty_util.tl:196-197`).

## Inverdimento dell’industria

| | | Fonte |
|---|---|---|
| Effetto | rumore e inquinamento dell'industria ×0,2 (−80 %), per sempre | `emission_config.tl:32`, `emissions.script.tl:184-192` |
| Utilizzi | uno al grado aziendale 3, 6, 9, 12 e 15 | `industry_greenify_tool.script.tl:99-104` |
| Limite | una volta per industria; un secondo tentativo non consuma permessi | `company.script.tl:489-494` |

- L'effetto è legato a quella versione dell'industria: quando l'industria viene ricostruita, si perde (`emissions.script.tl:187-190`).
- Uso migliore: l'industria più attiva proprio accanto a una città, perché un'industria potenziata è quella che emette di più.

## L'Impianto di bonifica

Un vantaggio aziendale che rimuove l'inquinamento intorno a sé.

| | | Fonte |
|---|---|---|
| Prezzo | 100.000.000 | `pollution_cleanup_facility.script.lua:560` |
| Manutenzione annua | 10.000.000 | `pollution_cleanup_facility.script.lua:561` |
| Disponibili | 15 al grado aziendale 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Richiede | **Macchinari**: 8 per ciclo, due cicli all'anno; 20 lavoratori | `pollution_cleanup_facility.con.lua:43-60` |
| Raggio | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| Stato | Inquinamento | Rumore | Fonte |
|---|---|---|---|
| fermo (senza macchinari) | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| in funzione | −10.000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| potenziato una volta | −20.000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| potenziato due volte | −40.000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

L'ultimo livello richiede una regola di potenziamento, che l'Impianto di bonifica non ha: con i lavoratori arriva a −20.000 (`pollution_cleanup_facility.con.lua:51-58`, `emissions.script.tl:158-166`).

- Senza macchinari non fa quasi nulla: va rifornito come un'industria.
- È rumoroso: costruiscilo fuori dal quartiere residenziale, entro 700 m dalla zona inquinata.
- Il suo fattore di potenziamento dei lavoratori è ×2 (`pollution_cleanup_facility.script.lua:549`). Vedi [Lavoratori](workers.html).

## Da sapere

- Apri la finestra della città o i livelli rumore e inquinamento per vedere la valutazione e i punti critici.
- Quando tutte le scorte in uscita di un'industria sono piene, il suo livello di emissione si dimezza, ma perdi le sue merci: meglio spostare la città che affamare l'industria.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) e [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) aiutano a trovare le stazioni più affollate.

```engine
Il motore calcola le mappe di rumore e inquinamento, come si diffondono i valori, le emissioni di veicoli e binari, e quando un'industria viene ricostruita. Lo script imposta solo il livello di ogni edificio e i limiti delle città.
```

```check
official: "Noise reflects noise levels in residential areas." "Pollution reflects pollution levels across the town area." Il quartiere residenziale "is sensitive to noise"; il quartiere commerciale "is robust against the influence of noise". ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Valutazione del rumore 65 → 80 dB, inquinamento 60 → 74 dB mediato su 5–10 km²; la sensibilità aggiunge 10·log10 dB; industrie, stazioni, depositi e magazzini emettono di più quando sono attivi; con tutte le scorte in uscita piene, il livello di emissione di un'industria si dimezza; inverdimento −80 % una volta per industria; l'Impianto di bonifica rimuove fino a 20.000 di inquinamento (40.000 è definito ma richiede una regola di potenziamento) entro 700 m e richiede macchinari.
result: refines
```
