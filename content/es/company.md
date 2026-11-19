---
title: Rango de la empresa, ventajas y sede central
summary: Qué sube el rango de tu empresa, qué desbloquea cada rango, cómo funcionan los permisos y las prospecciones, qué aporta de verdad la sede central y qué te cuesta un rango más alto.
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40444
fact: 15 | rangos de empresa, de Júnior a Magnate
fact: ×12,5 | de población mundial necesaria para el rango 15, respecto al inicio
fact: ×0,75 | de ingresos en el rango 15 con Inflación Normal
fact: 0 | rangos perdidos cuando baja la población
---

El rango de tu empresa no viene del dinero ni de las entregas: viene de la **población de todo el mapa**. Cada nuevo rango desbloquea ventajas (monumentos, prospecciones, campañas de marketing, Ecologización industrial, módulos de la sede central) y, con el ajuste **Inflación**, también baja un poco todos tus ingresos.

## Qué sube el rango

- El juego recuerda la **población mundial al inicio** de la partida: los habitantes de todas las localidades (`company.script.tl:392-396`, `company_util.tl:365-371`).
- Después compara la población mundial **más alta** alcanzada con ese valor inicial (`company_growth.script.tl:25-27`). El valor solo sube: las localidades que encogen nunca te cuestan un rango.
- El rango 1 se alcanza con el valor inicial y el rango 15 con unas **12,5 veces** ese valor (`company_progression_util.tl:6-14`, `company_progression_util.tl:95-120`, `town_growth_function.tl:13-20`).
- No hay rango en las misiones de campaña ni en el editor de mapas (`company_growth.script.tl:74-79`).

| Rango | Rol | Población mundial, respecto al inicio |
|---|---|---|
| 1 | Júnior | ×1 |
| 2 | Mecánicas | ×1,02 |
| 3 | Ingeniería | ×1,08 |
| 4 | Coordinación | ×1,2 |
| 5 | Especialista | ×1,4 |
| 6 | Líder de equipo | ×1,7 |
| 7 | Supervisión | ×2,1 |
| 8 | Gerente | ×2,6 |
| 9 | Dirección | ×3,3 |
| 10 | Dirección sénior | ×4,2 |
| 11 | Dirección ejecutiva | ×5,3 |
| 12 | Presidencia del consejo | ×6,7 |
| 13 | Vicepresidencia | ×8,3 |
| 14 | Presidencia | ×10,2 |
| 15 | Magnate | ×12,5 |

Las proporciones se calculan a partir de los scripts para una población inicial de 50.000 o más (`company_progression_util.tl:6-14`, `company_static_util.tl:6-24`). En un mapa pequeño son algo más altas para los rangos intermedios (el rango 8 necesita ×2,85 con 5.000 habitantes); los rangos 1 y 15 se quedan en ×1 y ×12,5.

- Así que el rango sigue el **crecimiento de las localidades**: las localidades crecen con tus pasajeros y tu carga, ver [Crecimiento de las localidades](towns.html).
- Los primeros rangos llegan rápido; los últimos necesitan localidades muchas veces más grandes.

## Un nuevo rango se aplica en la ventana de la empresa

Cuando la población supera un umbral, aparece una **notificación de ascenso**; al hacer clic se abre la ventana de la empresa en ese rango (`company_growth.script.tl:96-107`, `company_notification_rank_up.script.tl:8-9`).

- Las nuevas ventajas solo se desbloquean cuando ese rango se **selecciona en la ventana de la empresa**: la ventana envía entonces el desbloqueo (`company.tl:420-423`, `company_growth.script.tl:55-62`). Los menús de construcción comprueban este rango aplicado (`company_util.tl:92`, `company_util.tl:171-178`).
- El multiplicador de ingresos de la sección siguiente sigue el rango **alcanzado**, aplicado o no (`company_growth.script.tl:47-48`).

```tip scripts
Tras un ascenso, haz clic en la notificación (o abre la ventana de la empresa y selecciona el nuevo rango) para obtener las ventajas. Esperar no te da nada: los ingresos ya han bajado.
```

## Lo que cuesta un rango más alto: el ajuste Inflación

Con **Inflación**, todos los ingresos de carga y pasajeros bajan de forma regular desde ×1 en el rango 1 hasta un mínimo en el rango 15 (`company_progression_util.tl:25-40`, `company_growth.script.tl:159-170`).

| Inflación | Ingresos en el rango 15 | Fuente |
|---|---|---|
| Ninguna | ×1 (sin cambio) | `difficulty_util.tl:50`, `mod.script.tl:695-698` |
| Baja | ×0,9 | |
| Normal | ×0,75 | |
| Alta | ×0,6 | |
| Muy alta | ×0,5 | |

- En Normal, cada rango cuesta un 1,8 % de los ingresos: ×0,96 en el rango 3, ×0,875 en el rango 8, ×0,75 en el rango 15.
- La Inflación no sube ningún coste; los costes siguen el año del calendario (ver [Costes, mantenimiento y préstamos](costs.html)).
- Un rango más alto también hace más raras las nuevas ofertas de contratos (ver [Contratos](subsidies.html)).

## Permisos

La mayoría de las ventajas están limitadas por **permisos**. Un rango da permisos para una ventaja; cada edificio o uso gasta uno (`company_util.tl:33-80`, `company_util.tl:206`).

- Los permisos **se suman** a lo largo de los rangos: una ventaja que da 1 en el rango 3 y 1 en el rango 5 permite 2 desde el rango 5 (`company_util.tl:51-56`).
- Un edificio devuelve su permiso al ser demolido: el juego cuenta lo que está en pie (`company_util.tl:143-163`, `company_util.tl:203-206`).
- Las prospecciones, las campañas de marketing y la ecologización gastan un permiso al empezar (`company.script.tl:416-423`, `company.script.tl:459-462`, `company.script.tl:496-500`). El menú de construcción muestra entonces **Ya se ha usado** o **Tiempo de espera** (`company_util.tl:207-226`).
- El permiso de **Marketing** vuelve **5 años** después de cada campaña (`marketing.res.lua:6-7`, `company.script.tl:66-94`).

| Ventaja | Permisos | Fuente |
|---|---|---|
| Sede central | 1 en el rango 1 | `hq.res.lua:6` |
| Campaña de marketing | 1 en el rango 4, vuelve tras 5 años | `marketing.res.lua:6-7` |
| Ecologización industrial | 1 en los rangos 3, 6, 9, 12 y 15 | `industry_greenify_tool.script.tl:101-102` |
| Planta de limpieza | 15 en el rango 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Monumentos | uno de cada: Anfiteatro 2, Gran faro 5, Castillo de Himeji 7, Barco museo 9, Castillo de Neuschwanstein 10, Estatua de la Libertad 11, Palacio de Verano 13, Teatro de ópera 14, Palacio de Westminster 15 | `arena.con.lua:39`, `lighthouse.con.lua:48`, `white_heron_castle.con.lua:47`, `ship_museum.con.lua:55`, `neuschwanstein.con.lua:55`, `statue_of_liberty.con.lua:57`, `summer_palace.con.lua:63`, `opera_house.con.lua:63`, `westminster.con.lua:79` |

Qué hace cada ventaja: [Reputación](reputation.html) (campaña de marketing), [Contaminación y ruido](emission.html) (ecologización, Planta de limpieza).

## Prospecciones

Una prospección busca un recurso cerca de una localidad y, si tiene éxito, funda allí una nueva industria.

| Recurso | Rango | Fuente |
|---|---|---|
| Pescado | 2 | `exploration_fish.res.lua:9-11` |
| Arcilla | 3 | `exploration_clay.res.lua:9-11` |
| Crudo | 4 | `exploration_crude_oil.res.lua:9-11` |
| Grano, vegetales | 4, **un permiso compartido** (Industria) | `exploration_grain.res.lua:9`, `exploration_vegetables.res.lua:9`, `permit_key_farm.res.lua:6` |
| Troncos | 5 | `exploration_logs.res.lua:9-11` |
| Carbón, mineral de hierro | 6 | `exploration_coal.res.lua:9-11`, `exploration_iron_ore.res.lua:9-11` |
| Piedra, lana | 8 | `exploration_stone.res.lua:9-11`, `exploration_wool.res.lua:9-11` |
| Arena | 9 | `exploration_sand.res.lua:9-11` |
| Caucho | 12 | `exploration_rubber.res.lua:9-11` |

- Cada recurso tiene **un** permiso, que se gasta al empezar la prospección (`company.script.tl:451-462`).
- Dura hasta **6 meses**. Una vez al mes intenta colocar la industria, con una probabilidad que sube del 20 % al 60 % a lo largo de los 6 meses (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`).
- Un intento también falla cuando el juego no encuentra sitio para esa industria cerca de la localidad (`company.script.tl:199-210`).
- Si el último intento falla, **el permiso vuelve** y una notificación lo indica (`company.script.tl:106-126`, `company.script.tl:170-181`).
- Solo puede haber una prospección a la vez por localidad y recurso (`company.script.tl:442-447`).

```engine
Dónde puede situarse la nueva industria (makeIndustrySpawnProposal cerca de la localidad) lo decide el motor: una prospección de pescado lejos del agua, o una localidad sin terreno libre alrededor, simplemente falla y devuelve el permiso.
```

## La sede central

| Qué | Valor | Fuente |
|---|---|---|
| Precio y mantenimiento | gratis, sin mantenimiento | `headquarter.script.tl:526-527` |
| Permiso | 1, en el rango 1 | `headquarter.con.lua:6-7`, `hq.res.lua:6` |
| Crecimiento de la localidad | +5 % para la localidad más cercana | `headquarter.script.tl:510-515`, `landmark_util.tl:51-70` |
| Puestos de trabajo | 24 | `headquarter.con.lua:16`, `headquarter.script.tl:505-508` |

- El +5 % es una bonificación sobre la tasa de crecimiento de esa localidad, así que no hace nada cuando esa tasa es 0 % (ver [Crecimiento de las localidades](towns.html)).
- Los **módulos** cuestan 50.000 cada uno y están limitados por permisos que aumentan con el rango (`hq_module_m.module.lua:83`, `hq_module_m.module.lua:137`).
- Solo dos módulos tienen bonificación en los archivos: **Edificio mediano** +1 % de crecimiento de la localidad (`hq_module_m.module.lua:139-142`) y **Edificio grande** +1 % de Recuperación de la reputación (`hq_module_l.module.lua:169-172`). Ninguna calificación de localidad lee la bonificación de recuperación (ver [Reputación](reputation.html)). Los demás módulos son decorativos.
- Cada archivo de módulo empieza también con una tabla que da +5 % de crecimiento, pero nada en el archivo la usa (`hq_corner_l.module.lua:148-159`, `hq_statue.module.lua:46-57`). Solo se suma la bonificación dentro de los `metadata` del módulo (`headquarter_addon.script.tl:18-29`).

| Módulo | Permisos ganados en el rango (×2 = dos) | Total en el rango 15 |
|---|---|---|
| Bandera de suelo | 1 ×2, 6, 7, 8, 9, 11, 12, 13, 14 | 10 |
| Edificio de esquina | 3, 5, 7 ×2, 9, 11, 13, 15 | 8 |
| Edificio mediano | 2, 4, 10 ×2, 15 ×2 | 6 |
| Edificio grande | 5, 6, 10, 12 | 4 |
| Balcón | 8 ×2, 14 ×2 | 4 |
| Fuente grande | 10 ×2, 14 ×2 | 4 |
| Cúpula | 6, 15 ×2 | 3 |
| Bandera de techo | 7, 10, 13 | 3 |
| Pista de tenis | 11, 12, 14 | 3 |
| Árbol antiguo | 13, 15 ×2 | 3 |
| Estatua | 14 ×2 | 2 |
| Piscina | 15 | 1 |

Fuentes: la línea `rankAndPermits` de cada archivo de módulo (`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`).

```tip scripts
Pon la sede central en la localidad que quieras hacer crecer más rápido y añade allí Edificios medianos: son los únicos módulos con bonificación de crecimiento.
```

## Conviene saber

- Para subir de rango, haz crecer las localidades: más pasajeros y carga hacia más localidades, con buenas calificaciones. El dinero en el banco no cuenta.
- Planifica tus monumentos y prospecciones: cada uno llega una sola vez, en un rango fijo.
- En un mapa con Inflación, un ascenso es bueno para las ventajas y malo para los ingresos. En Normal, todo el camino hasta el rango 15 cuesta una cuarta parte de todos los ingresos.

```check
official: "The company rank depends on the population of the map. … Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Misma regla: la población mundial más alta alcanzada, comparada con la población inicial, ×12,5 para el rango 15; nunca se pierde. Un nuevo rango debe seleccionarse en la ventana de la empresa para desbloquear sus ventajas, mientras que la Inflación baja los ingresos de inmediato. Solo dos módulos tienen bonificación (Edificio mediano +1 % de crecimiento, Edificio grande +1 % de Recuperación de la reputación, que ninguna calificación lee); los demás son decorativos.
result: refines
```
