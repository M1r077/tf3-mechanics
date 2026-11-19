---
title: Calles, vías, puentes y señales
summary: Velocidad, precio y conservación de cada tipo de vía y de calle, qué cuestan y permiten puentes, túneles, pasos a nivel y señales, qué cambian de verdad las travesías arboladas y las barreras acústicas, y dónde se explican los depósitos.
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40444
fact: 100 / 160 / 350 km/h | vía simple, estándar y de alta velocidad
fact: ×9 | precio y conservación de la vía de alta velocidad frente a la vía simple
fact: +30 % | precio de la catenaria sobre una vía
fact: -65 % | ruido de una calle o vía con barrera acústica
---

Cada tipo de calle y de vía tiene una velocidad máxima, un precio por metro y una conservación por metro y año, todo escrito en su archivo. Los puentes, los pasos a nivel y algunas decoraciones de calle añaden su propio límite de velocidad. Los costes de abajo son con **Gastos de infraestructura** y **Conservación de infraestructura** al 100 % (ver [Costes, conservación y préstamos](costs.html)).

## Vías

| Vía | Desde | Velocidad máxima | Construcción por km | Conservación por km y año | Fuente |
|---|---|---|---|---|---|
| Vías simples | inicio | 100 km/h | 60.000 | 10.000 | `simple.street_template.lua:9`, `simple.street_template.lua:28`, `simple.street_template.lua:33` |
| Vías estándar | 1930 | 160 km/h | 180.000 | 30.000 | `standard.street_template.lua:4`, `standard.street_template.lua:11`, `standard.street_template.lua:30`, `standard.street_template.lua:35` |
| Vías de alta velocidad | 1980 | 350 km/h | 540.000 | 90.000 | `high_speed.street_template.lua:4`, `high_speed.street_template.lua:11`, `high_speed.street_template.lua:30`, `high_speed.street_template.lua:35` |

- La **catenaria** cuesta un **30 %** más que la vía (`mod.script.tl:24-25`). Está disponible desde 1921 en la vía simple y desde el inicio de cada tipo más reciente (`simple_catenary.street_template.lua:4`). En los archivos no cuesta nada más al año: la variante eléctrica tiene la misma conservación (`simple_catenary.street_template.lua:34`).
- Los tres tipos permiten la misma pendiente y las mismas curvas: **8,5 %** al construir (el control Inclinación llega hasta ahí), 13 % como máximo para la forma de la vía, y un radio de curva de 55 m al construir, 40 m como mínimo (`standard.street_template.lua:36-37`, `standard.street_template.lua:48-49`, `construction_react_util.tl:241-242`, `construction_react_util.tl:1824`).
- La contaminación de la propia vía crece con su tipo: 2, 4 y 6 (`simple.street_template.lua:18`, `standard.street_template.lua:20`, `high_speed.street_template.lua:20`).

```engine
Cuánto reduce una curva la velocidad de un tren (los speedCoeffs de cada tipo de vía) y qué velocidad muestra la herramienta de construcción para una curva lo calcula el motor.
```

```tip scripts
La vía de alta velocidad cuesta 9 veces la vía simple, al construirla y cada año. Tiéndela solo donde los trenes vayan de verdad a más de 160 km/h; en el resto basta la vía estándar, y la vía simple para los ramales de mercancías lentos.
```

## Calles

| Calle | Años | Velocidad máxima | Construcción por km | Conservación por km y año | Fuente |
|---|---|---|---|---|---|
| Calle estrecha (antigua) | hasta 1940 | 20 km/h | 36.000 | 6.000 | `town_old_xsmall.street_template.lua:4-5`, `town_old_xsmall.street_template.lua:8`, `town_old_xsmall.street_template.lua:27`, `town_old_xsmall.street_template.lua:56` |
| Calle pequeña (antigua) | hasta 1940 | 40 km/h | 60.000 | 10.000 | `town_old_small.street_template.lua:8`, `town_old_small.street_template.lua:27`, `town_old_small.street_template.lua:56` |
| Calle grande (antigua) | hasta 1940 | 60 km/h | 180.000 | 30.000 | `town_old_large.street_template.lua:8`, `town_old_large.street_template.lua:27`, `town_old_large.street_template.lua:88` |
| Calle estrecha (moderna) | desde 1940 | 30 km/h | 120.000 | 20.000 | `town_new_xsmall.street_template.lua:4`, `town_new_xsmall.street_template.lua:11`, `town_new_xsmall.street_template.lua:30`, `town_new_xsmall.street_template.lua:59` |
| Calle pequeña (moderna) | desde 1940 | 50 km/h | 180.000 | 30.000 | `town_new_small.street_template.lua:11`, `town_new_small.street_template.lua:30`, `town_new_small.street_template.lua:59` |
| Calle mediana (moderna) | desde 1940 | 50 km/h | 360.000 | 60.000 | `town_new_medium.street_template.lua:11`, `town_new_medium.street_template.lua:30`, `town_new_medium.street_template.lua:75` |
| Calle grande (moderna) | desde 1940 | 60 km/h | 540.000 | 90.000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:30`, `town_new_large.street_template.lua:91` |
| Carretera rural pequeña (antigua) | hasta 1940 | 60 km/h | 60.000 | 10.000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:29`, `country_old_small.street_template.lua:58` |
| Carretera rural pequeña (moderna) | desde 1940 | 80 km/h | 180.000 | 30.000 | `country_new_small.street_template.lua:10`, `country_new_small.street_template.lua:31`, `country_new_small.street_template.lua:60` |
| Autopista de un carril | desde 1940 | 100 km/h | 180.000 | 30.000 | `highway_new_small.street_template.lua:10`, `highway_new_small.street_template.lua:32`, `highway_new_small.street_template.lua:53` |
| Autopista de dos carriles | desde 1940 | 120 km/h | 360.000 | 60.000 | `highway_new_medium.street_template.lua:10`, `highway_new_medium.street_template.lua:32`, `highway_new_medium.street_template.lua:61` |
| Autopista de tres carriles | desde 1940 | 120 km/h | 540.000 | 90.000 | `highway_new_large.street_template.lua:10`, `highway_new_large.street_template.lua:32`, `highway_new_large.street_template.lua:69` |
| Vías del tranvía (antiguas) | hasta 1910 | 40 km/h | 36.000 | 6.000 | `tram_old.street_template.lua:4-5`, `tram_old.street_template.lua:8`, `tram_old.street_template.lua:27`, `tram_old.street_template.lua:40` |
| Vías del tranvía (modernas) | desde 1925 | 100 km/h | 120.000 | 20.000 | `tram_new.street_template.lua:4`, `tram_new.street_template.lua:9`, `tram_new.street_template.lua:29`, `tram_new.street_template.lua:42` |

- El **cambio de 1940** hace las calles urbanas 10 km/h más rápidas pero **tres veces** más caras, al construirlas y cada año: una calle pequeña pasa de 60.000 a 180.000 por km.
- Las variantes mediana y grande de las carreteras rurales cuestan 2 y 3 veces la pequeña, a la misma velocidad (`country_new_large.street_template.lua:10`, `country_new_large.street_template.lua:31`).
- Añadidos a una calle: un **carril bus** +10 %, una **vía de tranvía** +20 %, una **vía de tranvía eléctrico** +40 % del precio de la calle (`mod.script.tl:24-28`).
- Normalmente el jugador no es dueño de las calles, ni siquiera de las que construye; las herramientas de calle pueden cambiar el dueño de una calle (wiki oficial). Quién paga la conservación de una calle lo decide el motor.

## Travesías arboladas y barreras acústicas

| Herramienta | Ruido | Contaminación | Velocidad máxima | Dónde | Fuente |
|---|---|---|---|---|---|
| Herramienta de travesía (árboles) | -10 % | -50 % | **-25 %** | calles con acera, no en puentes ni en túneles | `alley.edge.lua:39-40`, `alley.edge.lua:53-56` |
| Herramienta de barrera acústica | -65 % | sin cambio | sin cambio | calles y vías, no en túneles | `barrier_b.edge.lua:43`, `barrier_b.edge.lua:47`, `barrier_track_b.edge.lua:43` |

- Ambas cuestan 100 y 10 al año en sus archivos, como una calle por metro (`alley.edge.lua:8`, `alley.edge.lua:12`, `barrier_b.edge.lua:7`, `barrier_b.edge.lua:11`).
- Los tipos de calle «con árboles» y «con barreras» del menú de construcción son las mismas calles con estas decoraciones ya puestas (`town_new_medium_trees.street_template.lua:12-14`). El menú de construcción suma sus efectos (`construction_react_util.tl:2119-2142`).
- Así que una calle con árboles es **un cuarto más lenta**: una calle mediana moderna con árboles permite unos 38 km/h en lugar de 50.

```tip scripts
Contra el ruido, usa la barrera acústica: -65 % y sin pérdida de velocidad. Los árboles son la herramienta contra la contaminación (-50 %), pero frenan la calle un cuarto.
```

Cómo valoran las localidades el ruido y la contaminación: [Contaminación y ruido](emission.html).

## Puentes y túneles

| Puente | Años | Velocidad máxima | Para | Precio base | Fuente |
|---|---|---|---|---|---|
| Puente de piedra | desde el inicio | 90 km/h | vías, calles | 200 | `stone.bridge.lua:169-170`, `stone.bridge.lua:181-183`, `stone.bridge.lua:193` |
| Puente de caballetes | hasta 1970 | 60 km/h | un tipo para vías, otro para calles | 100 | `trestle.bridge.lua:200-201`, `trestle.bridge.lua:212-214`, `trestle.bridge.lua:226`, `trestle_s.bridge.lua:212` |
| Puente de acero | desde 1940 | 140 km/h | vías, calles | 200 | `steel.bridge.lua:243`, `steel.bridge.lua:259`, `steel.bridge.lua:269` |
| Puente colgante | desde 1940 | 180 km/h | vías, calles | 600 | `suspension.bridge.lua:277`, `suspension.bridge.lua:294`, `suspension.bridge.lua:304` |
| Puente de hormigón | desde 1970 | 280 km/h | vías, calles | 200 | `concrete.bridge.lua:162`, `concrete.bridge.lua:176`, `concrete.bridge.lua:187` |
| Puente atirantado | desde 2000 | 220 km/h | vías, calles | 750 | `cable.bridge.lua:214`, `cable.bridge.lua:231`, `cable.bridge.lua:240` |
| Puente de arco tensado | desde 2010 | 350 km/h | vías, calles | 650 | `tarch.bridge.lua:253`, `tarch.bridge.lua:270`, `tarch.bridge.lua:280` |

- El límite del puente se aplica **además** del de la vía: una línea de alta velocidad sobre un puente de acero va ahí a 140 km/h. Antes de 1970 ningún puente permite más de 180 km/h, antes de 2010 ninguno permite 350 km/h.
- Los **túneles** (Túnel de piedra, Túnel de hormigón desde 1970) **no tienen límite de velocidad** en sus archivos, y el mismo precio base de 600 (`tunnel_a.tunnel.lua:187-188`, `tunnel_a_car.tunnel.lua:185`, `tunnel_b.tunnel.lua:191-194`).
- Los precios de puentes y túneles siguen Gastos de infraestructura (`post_run_util.tl:50-51`).

```engine
El motor convierte el precio base de un puente o túnel en un precio por metro, con la altura o la profundidad (costFactors); la wiki oficial dice que depende de la longitud y de la altura sobre el suelo o la profundidad bajo él. El mismo precio base puede dar facturas muy distintas. Los túneles cuestan Reputación ante la localidad (ver [Reputación de las localidades](reputation.html)).
```

```tip scripts
Para una línea rápida que cruce un valle antes de 1970, el puente colgante (180 km/h) es el único puente más rápido que 140 km/h; un túnel no tiene ningún límite.
```

## Pasos a nivel y señales

| Qué | Años | Velocidad máxima de la vía | Precio | Fuente |
|---|---|---|---|---|
| Cruce simple | 1850 - 1925 | 120 km/h | 4.000 | `era_a_eu.rcr.lua:14-17`, `era_a_eu.rcr.lua:26` |
| Cruce con media barrera | 1925 - 1975 | 160 km/h | 16.000 | `era_b_eu.rcr.lua:15-18`, `era_b_eu.rcr.lua:27` |
| Cruce con media barrera moderno | desde 1975 | 160 km/h | 16.000 | `era_c_eu.rcr.lua:15-17`, `era_c_eu.rcr.lua:26` |
| Señal de ruta (semáforo hasta 1950, luminosa desde 1950) | todos | - | 9.000, conservación 1.500 al año | `signal_path_a.con.lua:4-5`, `signal_path_a.con.lua:10-11`, `signal_path_c.con.lua:4-5` |

- Un paso a nivel limita la vía a 160 km/h como máximo: las líneas de alta velocidad necesitan puentes o túneles para cruzar las calles.
- Cada señal puede ponerse en **Sentido único** (`signal_path_a.con.lua:51-52`). Cómo dividen las señales la vía en bloques se explica en la página Railway Signals de la wiki oficial.

## Depósitos y edificios de mantenimiento

Lo que cuestan los depósitos y los edificios de mantenimiento, cuántos vehículos atienden y en qué radio: [Vehículos](vehicles.html) y [Costes, conservación y préstamos](costs.html).

## Conviene saber

- Antes de 1940, mejorar las calles urbanas es barato; después de 1940 cada calle urbana nueva o reconstruida cuesta el triple y el triple de conservación.
- En una línea rápida, revisa cada puente y cada paso a nivel: el más lento fija ahí la velocidad.
- La velocidad solo compensa si da más viajes (ver [¿Por qué pierdo dinero?](money.html)).

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: Mismas velocidades que las tablas oficiales para vías, calles y puentes. En los archivos los límites de los puentes también se aplican a las calles, los túneles no tienen ninguno, los pasos a nivel limitan las vías a 120 o 160 km/h, los árboles frenan una calle un 25 % y reducen la contaminación un 50 % pero el ruido solo un 10 %, mientras que las barreras acústicas reducen el ruido un 65 % sin frenar.
result: refines
```
