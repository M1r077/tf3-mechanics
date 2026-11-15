---
title: Trabajadores y el refuerzo de trabajadores
summary: Cómo los residentes consiguen empleo en una industria, cuáles cuentan para el refuerzo y de cuánto es el refuerzo.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-14
fact: 10 / 20 | trabajadores necesarios para el refuerzo
fact: 2 años | tiempo durante el que cuenta una llegada
fact: ×1,5–2,5 | factor de refuerzo, fijo para cada industria
---

Toda industria ofrece puestos de trabajo. Cuando llegan suficientes trabajadores **a través de tus líneas de pasajeros**, la industria produce más. La ventana de la industria muestra dos números distintos, y confundirlos es la causa más habitual de malentendidos.

```diagram workers_flow
```

## Quién puede trabajar en una industria

- Toda industria del juego base tiene **20 puestos de trabajo** (`industrialCapacity = 20`).
- Los puestos de trabajo están configurados para que los residentes **no puedan ir a pie ni en coche**: solo tus líneas pueden llevarlos (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Cada residente tiene una vivienda, una tienda y un empleo. El juego elige el empleo entre los lugares que el residente puede alcanzar; una industria tiene un peso de destino de 2,0 (`industryutil.lua:455`).

```engine
Cómo elige un residente un empleo entre todos los lugares que puede alcanzar (tiempo de viaje, coste, el peso de 2,0) lo calcula el motor. Los scripts solo proporcionan los datos de entrada.
```

## Trabajadores asignados

Son los residentes cuyo empleo es esta industria. Es la barra de puestos de trabajo de la ventana de la industria y la columna **Zonas de trabajo** de las estadísticas de las industrias ("12/20") (`entity_window_util.tl:1238`, `statistic_industries.tl:305`). Estar asignado **no** basta para el refuerzo: el trabajador tiene que hacer realmente el viaje.

## Trabajadores contados para el refuerzo

Un pequeño script del juego vigila cada llegada (`industry_workers.script.tl`):

1. Cuando un residente llega a una industria y su **último desplazamiento fue con tus líneas**, la llegada se anota con la hora del juego (`industry_workers.script.tl:86-118`).
2. Solo se conservan las llegadas de los **últimos 2 años de juego** (`industry_productivity_util.tl:3`: `2 * getDefaultYearDuration()`).
3. Se conservan como máximo las **20 llegadas más recientes** (`industry_workers.script.tl:4`, `KeepHistoryCount = 20`).
4. Cuando la misma persona vuelve a llegar, la nueva llegada sustituye a la anterior: cada residente cuenta **una sola vez** (`industry_workers.script.tl:56-70`).

```diagram workers_window
```

## Cuándo empieza y termina el refuerzo

- La industria recibe el refuerzo cuando los trabajadores contados alcanzan **la mitad de los puestos de trabajo**: `contados ≥ puestos × 0,5` (`industry_productivity_util.tl:35-48`, `RequiredWorkersFractionForBoost = 0.5`). Con 20 puestos de trabajo: **10 trabajadores**.
- La sección **Refuerzos** de la ventana de la industria muestra exactamente esto: "contados / necesarios", con los necesarios redondeados hacia arriba (`industry_react_util.tl:627`).
- La comprobación se repite cada vez que llegan nuevos trabajadores o la llegada más antigua supera los 2 años (`industry_workers.script.tl:40-43`). Por eso el refuerzo **termina por sí solo** unos 2 años después de que los trabajadores dejen de llegar.

## De cuánto es el refuerzo

- La producción se multiplica por el **factor de refuerzo** de la industria, que la ventana muestra como "+X %" (`industry_react_util.tl:716`).
- El factor se sortea una sola vez a partir de la semilla aleatoria de la industria: **entre ×1,5 y ×2,5**, y nunca cambia para esa industria (`industry_productivity_util.tl:58-72`). Una industria sin semilla usa ×2.
- Así, dos minas idénticas pueden tener refuerzos de trabajadores distintos: mira el "+X %" antes de decidir a cuál dar servicio.

## Ejemplo

Una mina de carbón con 20 puestos de trabajo y "+84 %".

| Situación | Contados | ¿Reforzada? | Producción |
|---|---|---|---|
| Nueva línea de autobús: 14 residentes asignados, aún no ha llegado ninguno | 0 | no | ×1 |
| 12 residentes distintos han llegado en autobús este año | 12 | sí (≥ 10) | ×1,84 |
| Línea de autobús eliminada; nadie llega durante 2 años | baja a 0 | termina | ×1 |

## Conviene saber

- El límite de 20 llegadas conservadas y la regla del 50 % hacen que una industria con **más de 40 puestos de trabajo** (posible con mods) nunca pueda recibir el refuerzo de trabajadores.
- La subvención "Transportar trabajadores" se cumple cuando se activa este refuerzo (wiki oficial, Subsidies).
- El cargamento de refuerzo (fertilizante, máquinas, herramientas) es un refuerzo **distinto** de las industrias de materias primas, que no se trata aquí.
- El mod [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) muestra, en la ventana de la industria, de qué localidades vienen los trabajadores asignados y los del refuerzo, con flechas en el mapa.

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: "Suficiente" = la mitad de los puestos de trabajo (10 de 20); "recientemente" = los últimos 2 años de juego, las 20 llegadas más recientes, una por persona, solo con tus líneas; factor de refuerzo de ×1,5 a ×2,5 según la industria.
result: refines
```
