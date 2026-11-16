---
title: Tempo di gioco e calendario
summary: La velocità di gioco e la velocità del calendario sono due cose diverse. Quanto durano un giorno e un anno, cosa cambia un calendario più lento o in pausa, e cosa no.
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
game: 40425
fact: 4 s | un giorno di calendario a velocità calendario ×1, velocità di gioco x1
fact: ≈ 24 min | un anno di calendario alle stesse velocità
fact: 0 ×0,25 ×0,5 ×1 ×2 ×4 | livelli della velocità calendario
fact: 0 1x 2x 4x | livelli della velocità di gioco
---

Il gioco ha **due orologi**. La **velocità di gioco** (pausa, x1, x2, x4) fa andare tutto più veloce: veicoli, produzione, cittadine. La **Velocità calendario** stabilisce solo quanto velocemente avanza la data. Quasi ogni regola del gioco conta in tempo di gioco, non in giorni di calendario.

## Le due impostazioni

| Impostazione | Livelli | Cosa cambia | Fonte |
|---|---|---|---|
| **Velocità di gioco** | Pausa, x1, x2, x4 | quanto velocemente va tutta la simulazione | `game_bar_widgets.tl:199-203` |
| **Velocità calendario** | In pausa, ×0,25, ×0,5, ×1, ×2, ×4 | quanti secondi di gioco dura un giorno | `game_bar_widgets.tl:321-335`, `game_bar_widgets.tl:351` |

- A velocità calendario ×1 un giorno dura **4 secondi** di tempo di gioco (wiki ufficiale), quindi un mese dura circa 2 minuti e un anno circa **24 minuti** a x1. Misurato con [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard): 4,0 s al giorno a ×1, 1 s a ×4, 8 s a ×0,5, 16 s a ×0,25.
- ×4 fa avanzare la data quattro volte più veloce; **In pausa** ferma la data, la simulazione continua.
- x2 e x4 sono un massimo: il gioco li abbassa quando il computer non tiene il passo (`game.tl:636-642`). Misurato: x2 ha dato x1,9 e x4 ha dato x3,6 in media.
- L'**Ora del giorno** e il meteo sono un terzo orologio, visivo: di base cambiano da soli, qualunque sia il calendario (`game_time_config.res.lua:5`, `weather_config.res.lua:5`).

## Cosa segue il tempo di gioco, qualunque sia il calendario

Queste cose si contano in tempo di gioco, quindi un calendario più lento o in pausa non le rallenta:

- **Produzione**: il tempo di produzione di un'industria è una quota fissa di un anno standard (`industry_react_util.tl:51`). La finestra dell'industria lo mostra in giorni del calendario attuale (`industry_react_util.tl:23`): a ×0,25 lo stesso ritmo mostra un quarto dei giorni.
- **Rate dei prestiti**: una ogni mese standard di tempo di gioco, anche con il calendario in pausa (`loan.script.tl:83-88`).
- **Scadenze dei sussidi** e la durata del bonus, 5 anni standard (`subvention_util.tl:286`, `subvention_util.tl:290-292`).
- **Recupero della reputazione delle cittadine** (`towns.script.tl:121-130`), **effetti dei lavoratori**, contati su al massimo 2 anni standard (`industry_productivity_util.tl:3`), e **chiusura delle industrie** dopo anni senza servizio (`industries.script.tl:119-128`).
- **Valutazioni delle consegne** delle cittadine, sull'ultimo semestre (`town_util.tl:840`).
- **Nuove industrie**: con il calendario in pausa ne sono comparse 3 in 1809 s di tempo di gioco, a 760 s e 728 s l'una dall'altra, allo stesso ritmo del calendario in moto (circa 730 s). Misurato con [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard); vedi [Industrie](industries.html).

Con il calendario in moto, il gioco mostra queste durate in anni, mesi e giorni della velocità calendario attuale (`util.tl:40-49`).

## Cosa segue la data del calendario

- **Nuovi veicoli, stazioni ed edifici** compaiono in base all'anno (wiki ufficiale: "Different calendar speeds only affect the availability of vehicles and infrastructure").
- **Costi che crescono con l'anno**: la manutenzione degli edifici, le varianti d'epoca, il denaro dei sussidi e gli importi dei prestiti seguono la data. Vedi [Costi, manutenzione e prestiti](costs.html).

## Con il calendario in pausa

1. La data, e quindi l'anno, restano fissi: niente veicoli nuovi, e i costi legati all'anno restano dove sono.
2. Le durate sono mostrate in **minuti e secondi** invece che in giorni (`util.tl:41-43`, `industry_react_util.tl:16-21`).
3. Un prestito mostra la sua rata **per min** invece che per anno (`finances_loan_gui.tl:223-231`), e la carta del prestito personalizzato non si può prendere (`finances_loan_gui.tl:393`).
4. Produzione, rate, scadenze e reputazione mantengono il loro ritmo in tempo di gioco.

## Da sapere

- Vuoi più tempo per far crescere una rete prima che arrivino veicoli nuovi? Abbassa la velocità calendario: le tue entrate per minuto di gioco non cambiano.
- La produzione mostrata "all'anno" dipende dalla velocità calendario; confronta le industrie alla stessa velocità.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) mantiene grafici finanziari leggibili con il calendario in pausa.

```engine
La durata del giorno, del mese e dell'anno standard (getDefaultDayDuration e gli altri) viene dal motore. Lo script delle cittadine conta un mese come 30 × 4 secondi (`towns.script.tl:121`), il che corrisponde al giorno misurato di 4 secondi; alcune altre costanti presumono ancora un giorno di 2 secondi (`cargotype.script.lua:3`, `mod.script.tl:172`).
```

```check
official: "By default a day in the game lasts 4 seconds." "Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent." ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: Velocità calendario da ×0,25 a ×4 o in pausa, rispetto al giorno standard; produzione, prestiti, sussidi, reputazione e timer dei lavoratori vanno in tempo di gioco; un calendario in pausa mostra le durate in minuti e le rate al minuto, e blocca i nuovi prestiti; misurato: 4 s al giorno a ×1.
result: refines
```
