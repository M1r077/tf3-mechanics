---
title: Tiempo de juego y calendario
summary: La velocidad del juego y la velocidad del calendario son dos cosas distintas. Cuánto duran un día y un año, qué cambia un calendario más lento o en pausa, y qué no cambia.
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
fact: 4 s | un día del calendario a velocidad del calendario ×1, velocidad del juego x1
fact: ≈ 24 min | un año del calendario a las mismas velocidades
fact: 0 ×0,25 ×0,5 ×1 ×2 ×4 | niveles de la velocidad del calendario
fact: 0 1x 2x 4x | niveles de la velocidad del juego
---

El juego tiene **dos relojes**. La **velocidad del juego** (pausa, x1, x2, x4) hace que todo vaya más rápido: vehículos, producción, localidades. La **Velocidad del calendario** solo fija lo rápido que avanza la fecha. Casi todas las reglas del juego cuentan en tiempo de juego, no en días del calendario.

## Los dos ajustes

| Ajuste | Niveles | Qué cambia | Fuente |
|---|---|---|---|
| **Velocidad del juego** | Pausa, x1, x2, x4 | lo rápido que va toda la simulación | `game_bar_widgets.tl:199-203` |
| **Velocidad del calendario** | En pausa, ×0,25, ×0,5, ×1, ×2, ×4 | cuántos segundos de juego dura un día | `game_bar_widgets.tl:321-335`, `game_bar_widgets.tl:351` |

- A velocidad del calendario ×1, un día dura **4 segundos** de tiempo de juego (wiki oficial), así que un mes dura unos 2 minutos y un año unos **24 minutos** a x1. Medido con [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard): 4,0 s por día a ×1, 1 s a ×4, 8 s a ×0,5, 16 s a ×0,25.
- ×4 hace que la fecha avance cuatro veces más rápido; **En pausa** detiene la fecha, la simulación sigue.
- x2 y x4 son un máximo: el juego los baja cuando el ordenador no da abasto (`game.tl:636-642`). Medido: x2 dio x1,9 y x4 dio x3,6 de media.
- La **Hora del día** y el clima son un tercer reloj, visual: por defecto cambian solos, sea cual sea el calendario (`game_time_config.res.lua:5`, `weather_config.res.lua:5`).

## Qué sigue el tiempo de juego, sea cual sea el calendario

Estas cosas se cuentan en tiempo de juego, así que un calendario más lento o en pausa no las frena:

- **Producción**: el tiempo de producción de una industria es una parte fija de un año estándar (`industry_react_util.tl:51`). La ventana de la industria lo muestra en días del calendario actual (`industry_react_util.tl:23`): a ×0,25, el mismo ritmo muestra una cuarta parte de los días.
- **Pagos de préstamos**: uno por cada mes estándar de tiempo de juego, también con el calendario en pausa (`loan.script.tl:83-88`).
- **Plazos de las subvenciones** y el bono de ingresos ×2 (`subvention_util.tl:290-292`).
- **Recuperación de la reputación de las localidades** (`towns.script.tl:121-130`), **bonificaciones de trabajadores** (`industry_productivity_util.tl:3`) y **cierre de industrias** tras años sin servicio (`industries.script.tl:119-128`).
- **Valoraciones de entrega** de las localidades, sobre el último medio año (`town_util.tl:840`).
- **Industrias nuevas**: con el calendario en pausa aparecieron 3 en 1809 s de tiempo de juego, con 760 s y 728 s de separación, al mismo ritmo que con el calendario en marcha (unos 730 s). Medido con [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard); ver [Industrias](industries.html).

Con el calendario en marcha, el juego muestra estas duraciones en años, meses y días de la velocidad del calendario actual (`util.tl:40-49`).

## Qué sigue la fecha del calendario

- **Nuevos vehículos, estaciones y edificios** aparecen según el año (wiki oficial: "Different calendar speeds only affect the availability of vehicles and infrastructure").
- **Costes que crecen con el año**: la conservación de los edificios, las variantes de época, el dinero de las subvenciones y los importes de los préstamos siguen la fecha. Ver [Costes, conservación y préstamos](costs.html).

## Con el calendario en pausa

1. La fecha, y por tanto el año, quedan fijos: no hay vehículos nuevos y los costes ligados al año no se mueven.
2. Las duraciones se muestran en **minutos y segundos** en lugar de días (`util.tl:41-43`, `industry_react_util.tl:16-21`).
3. Un préstamo muestra su pago **por min** en lugar de por año (`finances_loan_gui.tl:223-231`), y la tarjeta de préstamo personalizado no se puede tomar (`finances_loan_gui.tl:393`).
4. La producción, los pagos, los plazos y la reputación mantienen su ritmo de tiempo de juego.

## Conviene saber

- ¿Quieres más tiempo para hacer crecer una red antes de que lleguen vehículos nuevos? Baja la velocidad del calendario: tus ingresos por minuto de juego no cambian.
- La producción mostrada "por año" depende de la velocidad del calendario; compara las industrias a la misma velocidad.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) mantiene gráficos financieros legibles con el calendario en pausa.

```engine
La duración del día, el mes y el año estándar (getDefaultDayDuration y los demás) viene del motor. El script de las localidades cuenta un mes como 30 × 4 segundos (`towns.script.tl:121`), lo que encaja con el día medido de 4 segundos; algunas otras constantes aún suponen un día de 2 segundos (`cargotype.script.lua:3`, `mod.script.tl:172`).
```

```check
official: "By default a day in the game lasts 4 seconds." "Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent." ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: Velocidad del calendario de ×0,25 a ×4 o en pausa, relativa al día estándar; la producción, los préstamos, las subvenciones, la reputación y los temporizadores de trabajadores van en tiempo de juego; un calendario en pausa muestra las duraciones en minutos y los pagos por minuto, y bloquea los préstamos nuevos; medido: 4 s por día a ×1.
result: refines
```
