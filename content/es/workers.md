---
title: Trabajadores y el refuerzo de trabajadores
summary: Cómo los residentes consiguen empleo en una industria, cuáles cuentan para el refuerzo y de cuánto es el refuerzo.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-15
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

## Llevar trabajadores a una industria

```diagram workers_trip
```

- Un trabajador se cuenta cuando **llega a la propia industria**, el destino de su viaje (`targetOrAtEntity`) es la industria y su último modo de desplazamiento es **Líneas** (`industry_workers.script.tl:86-94`). Bajarse en una parada no basta: la persona tiene que llegar a la industria.
- Cada residente tiene un modo de desplazamiento por destino (vivienda, tienda, empleo). La ventana de la industria lista los trabajadores asignados con un icono para ese modo: **Caminar**, **Coche** o **Líneas** (`entity_window_util.tl:1400-1435`). Para una industria siempre debería ser Líneas, porque Caminar y Coche no están permitidos allí (`industryutil.lua:451-457`).
- Así que "sin ir a pie" significa que el viaje entero no puede ser a pie ni en coche. No significa "sin caminar nada": un viaje en Líneas empieza y termina a pie entre las paradas y los edificios (ver la nota del motor abajo).
- **Los transbordos cuentan.** El script solo mira el modo del viaje, no cuántas líneas se usaron (`industry_workers.script.tl:91`). Un trabajador de una localidad a cuatro líneas de distancia cuenta igual que uno de al lado, pero puede tardar mucho más en llegar.
- **Cualquiera de tus líneas puede llevarlos**, incluso una línea de carga, siempre que sus vehículos lleven pasajeros y la parada cargue pasajeros. El script no comprueba el tipo de vehículo (`industry_workers.script.tl:86-118`). Los jugadores dicen tener menos problemas con líneas de pasajeros separadas.
- Algunas industrias (por ejemplo las plataformas petrolíferas) tienen su propia parada integrada, que acepta pasajeros y carga (`industryutil.lua:156-165`).
- La ventana de la industria indica, para cada trabajador asignado, si está en **Ubicación actual** o **De camino** (`entity_window_util.tl:1371-1384`). La sección Refuerzos lista los trabajadores contados con su **Tiempo restante** de los 2 años (`entity_window_util.tl:1579-1630`, `industry_eow.script.tl:644-649`).
- Una industria todavía sin trabajadores muestra: "Conecta esta ubicación con el transporte público para permitir que los residentes trabajen aquí." (`entity_window_util.tl:1650-1652`).

```engine
Qué parada sirve a una industria, cuánto camina un trabajador desde una parada hasta la entrada de la industria y los residentes de qué localidades toman el empleo lo decide el motor (áreas de influencia, búsqueda de ruta, elección de empleo). Los scripts no fijan ningún límite de distancia para los trabajadores. Algunos jugadores cuentan que una estación cuya área de influencia cubría la industria para la carga no llevó trabajadores hasta que un autobús fue a la entrada de la industria (hilo de Steam "Problem getting workers to site").
```

```tip
**Consigue rápido el refuerzo de trabajadores (y el contrato Transportar trabajadores): empieza con una línea simple.**

1. Crea una **nueva línea de pasajeros** desde una parada en la industria hasta **una sola localidad**.
2. Coloca la parada de la localidad de modo que su área de influencia **no toque ninguna de tus otras estaciones de pasajeros**.
3. Un solo vehículo basta para empezar.

Los empleos se reparten cuando abre la línea: en dos pruebas los **20 empleos fueron a esa única localidad**, y el refuerzo empezó tras **346 s y 925 s** de tiempo de juego (una vez con un solo vehículo). Cuando la parada de la localidad tocaba el área de una estación de la red, algunos empleos fueron a una localidad lejana y los últimos trabajadores tardaron mucho más (964 s). Medido con [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) y el [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard); quién obtiene un empleo lo sigue decidiendo el motor.
```

## Subsidio Transportar trabajadores

- Solo se ofrece para una industria con puestos de trabajo cuyo refuerzo de trabajadores aún no está activo y que envió o recibió carga en el último año, según las cifras anuales del motor (`deliver_workers.script.tl:121-131`, `industry_util.tl:541-558`). Si basta con recibir depende de cómo el motor rellena las reglas de producción; no está en los scripts.
- Se cumple cuando se activa el refuerzo de trabajadores: las mismas 10 de 20 llegadas distintas con tus líneas (`deliver_workers.script.tl:152-156`). No se cuenta nada más; no hay ninguna regla oculta.
- La barra de progreso de la tarjeta del contrato es "trabajadores contados ÷ la mitad de los puestos" (`deliver_workers.script.tl:267-272`, `industry_util.tl:11-18`).
- Las flechas del mapa del contrato salen de las **5 localidades más cercanas**. Son solo una pista: el script las dibuja por distancia, no según quién tiene el empleo (`deliver_workers.script.tl:297-317`).
- Ver [Subvenciones: ofertas, plazos y recompensas](subsidies.html) para el dinero y el plazo.

## ¿Por qué no llegan mis trabajadores?

| Comprobación | Dónde mirar | Por qué |
|---|---|---|
| ¿Alguien tiene el empleo? | Barra de puestos ("12/20") | Sin trabajadores asignados nadie viaja. La elección de empleo depende del motor. |
| Icono de modo de los trabajadores | Lista de trabajadores: Caminar / Coche / Líneas | Solo cuentan los viajes en Líneas (`industry_workers.script.tl:91`). |
| ¿Se están moviendo? | **De camino** / **Ubicación actual** | "De camino" durante mucho tiempo: transbordos lentos o saturados, o sin ruta desde la última parada. |
| ¿La última parada llega a la entrada de la industria? | Área de influencia de la parada, carretera de entrada | Lo cuentan los jugadores; depende del motor. Un autobús corto hasta la entrada ayudó. |
| ¿La parada carga pasajeros? | Parada de la línea, Filtro de cargamento | Los pasajeros deben cargarse y descargarse en los dos extremos del viaje. |
| ¿10 personas **distintas** en 2 años? | Sección Refuerzos, **Tiempo restante** | La misma persona cuenta una vez; las llegadas más antiguas salen (`industry_workers.script.tl:56-70`). |
| ¿Más de 40 puestos (mods)? | Barra de puestos | Nunca puede llegar a la mitad con 20 llegadas conservadas. |

## Conviene saber

- El límite de 20 llegadas conservadas y la regla del 50 % hacen que una industria con **más de 40 puestos de trabajo** (posible con mods) nunca pueda recibir el refuerzo de trabajadores.
- La subvención **Transportar trabajadores** se cumple cuando se activa este refuerzo (`deliver_workers.script.tl:152-156`).
- El cargamento de refuerzo (fertilizante, máquinas, herramientas) es un refuerzo **distinto** de las industrias de materias primas, que no se trata aquí.
- El mod [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) muestra, en la ventana de la industria, de qué localidades vienen los trabajadores asignados y los del refuerzo, con flechas en el mapa.

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: "Suficiente" = la mitad de los puestos de trabajo (10 de 20); "recientemente" = los últimos 2 años de juego, las 20 llegadas más recientes, una por persona, solo con tus líneas; factor de refuerzo de ×1,5 a ×2,5 según la industria. Los transbordos cuentan; el modo del viaje debe ser Líneas, caminar desde una parada forma parte de ese viaje.
result: refines
```
