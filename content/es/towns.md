---
title: Crecimiento de las localidades: XP, calificaciones y tamaño
summary: De dónde viene la XP de una localidad, cómo sus seis calificaciones fijan su tasa de crecimiento y cuánto la agranda cada nivel.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
fact: 0 % | de crecimiento cuando una calificación está en Muy baja
fact: ×1,5 | de XP para cada nivel siguiente (1.000 para el nivel 2)
fact: ×40 | de tamaño tras ganar 17 niveles
---

Una localidad solo crece con **tu** transporte: los pasajeros que llegan con tus líneas y el cargamento entregado a sus edificios le dan XP. Sus calificaciones deciden cuánta de esa XP cuenta, y cada nivel ganado agranda la localidad.

```diagram town_xp
```

## De dónde viene la XP

| Origen | XP bruta | Fuente |
|---|---|---|
| Pasajero que llega **con tus líneas** a un edificio de la localidad | 5 · 10 · 20: vivienda y empleo o tienda en la misma localidad, en una localidad vecina, en una localidad más lejana | `town_growth.script.tl:649-701`, `town_growth_config.res.lua:6` |
| Unidad de cargamento entregada a un edificio de la localidad | 10 · 20 · 40 para cargamento de nivel 0 · 1 · 2 | `town_growth.script.tl:642`, `town_growth_config.res.lua:5` |
| Recompensa de subvención "experiencia de la localidad" | una parte del nivel actual, también × tasa de crecimiento | `subvention_util.tl:144-152`, `town_growth.script.tl:608` |

- La XP va a la localidad del edificio al que **llega** el pasajero o el cargamento. Quien va y viene a diario entre dos localidades da XP a ambas: a la del empleo a la ida y a la de la vivienda a la vuelta.
- Los viajes desde o hacia una **industria** no dan XP (`town_growth.script.tl:680-683`). Los viajes a pie o en coche tampoco: solo cuentan los viajes hechos con tus líneas (`town_growth.script.tl:656`).
- El tiempo por sí solo no da nada: la XP por tick es 0 (`town_cargo_util.tl:6`).
- Niveles de cargamento: **0** ladrillos, cemento, pescado, combustible, carne, tablones, vegetales; **1** bebidas, libros, ropa, muebles, máquinas, comida enlatada, herramientas; **2** vehículos (`placementparamsutil.lua:506-616`).

Toda XP bruta se multiplica por la **tasa de crecimiento** de la localidad (`town_growth.script.tl:60-63`). La ventana de la localidad la muestra como **Tasa de crecimiento:**.

## La tasa de crecimiento

La tasa de crecimiento sale de dos calificaciones de la ventana de la localidad (`town_util.tl:607-633`, `town_util.tl:954-962`):

1. **Autoridad municipal**: la **más baja** de sus seis calificaciones, no la media (`town_util.tl:754-784`).
2. **Suministros**: la media de los niveles de suministro de pasajeros y de cargamento, redondeada hacia arriba (`town_util.tl:555-589`).

```diagram growth_matrix
```

- Cada calificación tiene seis niveles: un valor de 0 a 1 dividido en sextos (`town_util.tl:983-985`). **Excelente** exige 5/6 = 83 % o más.
- Con **una sola** calificación en Muy baja, la autoridad queda en Muy baja y la tasa de crecimiento es **0 %**: la localidad se detiene, entregues lo que entregues.
- El 100 % exige autoridad Excelente con suministros Muy buena o mejor, o autoridad Muy buena con suministros Excelente.
- Tu **sede central** añade +5 % a la localidad más cercana, y la mayoría de sus ampliaciones añaden otro +5 % cada una (`headquarter.script.tl:510-515`, `landmark_util.tl:51-70`). Esta bonificación multiplica la tasa, así que no hace nada con 0 %.

## Las seis calificaciones de la autoridad

| Calificación | Qué la baja | Fuente |
|---|---|---|
| **Reputación** | modificar el terreno, demoler edificios de la localidad, talar árboles; cada conexión principal cortada con otra localidad −1/3 | `town_util.tl:396-404`, `town_util.tl:1608` |
| **Tráfico** | calles congestionadas en la localidad | `town_util.tl:445-456` |
| **Felicidad** | proporción de viajeros descontentos (se suponen al menos 15 personas) | `town_util.tl:479-503` |
| **Entrega** | proporción de entregas de cargamento con retraso (ver [Ingresos por cargamento](income.html)) | `town_util.tl:505-519` |
| **Ruido** | ruido de la localidad: 65 dB o menos → calificación máxima, 80 dB → 0 | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Polución** | polución media del área de la localidad: 60 dB → máxima, 74 dB → 0 | `town_util.tl:413-431`, `emission_config.tl:23-24` |

Los ajustes de **susceptibilidad** de cada calificación (siete niveles, el primero es No) desplazan estos límites; No significa calificación siempre máxima (`difficulty_util.tl:44-49`).

## Suministros

- **Pasajeros**: uso de línea de la localidad × 2, así que **un 50 % de uso de línea da la calificación máxima** (`town_util.tl:546-553`).
- **Cargamento**: suministro ÷ demanda de cada distrito (comercial, industrial); cuenta el **mejor** distrito, no la media (`town_util.tl:521-529`).
- Una localidad sin nada que suministrar cuenta como suministros completos. Una localidad que no recibe de ti ni pasajeros ni cargamento cuenta como "sin entregas": tasa de crecimiento 0 % (`town_util.tl:565-588`).

Las nuevas demandas de cargamento llegan con los niveles (`placementparamsutil.lua:618-660`): una comercial y una industrial al principio, una segunda comercial en el nivel 5, una segunda industrial en el nivel 7, una tercera comercial en el nivel 9 y una tercera industrial en el nivel 11. Solo se añaden cuando la localidad ha recibido al menos una entrega de cargamento (`town_growth.script.tl:286-288`). El juego prefiere cargamentos que pocas otras localidades piden ya (`town_growth.script.tl:258-266`).

## Niveles y tamaño

- El nivel 2 exige 1.000 XP, y cada nivel siguiente 1,5 veces más que el anterior (`town_cargo_util.tl:81-97`, `town_growth_config.res.lua:7`): nivel 5 con 8.125 XP en total, nivel 10 con unos 75.000, nivel 18 (Metrópolis grande, el último) con unos 2 millones.
- Las localidades colocadas con más viviendas empiezan más arriba: nivel 2, 3 o 4 (`town_cargo_util.tl:43-54`).
- El **tamaño objetivo** depende de los niveles ganados desde el inicio, incluido el progreso hacia el siguiente (`town_cargo_util.tl:100-110`, `town_growth_function.tl:4-11`):

```diagram town_size
```

- El tamaño adicional se reparte entre los distritos residencial, comercial e industrial según lo bien atendido que esté cada uno: uso de pasajeros para las viviendas, suministro de cargamento para los demás (`town_growth.script.tl:404-421`). Cuando un distrito alcanza el 40 % de la localidad, la parte máxima que puede llevarse del nuevo tamaño baja del 100 % al 50 % a medida que llega al 50 % de la localidad (se aplican límites parecidos en todo el mapa) (`town_growth.script.tl:509-522`). Si no se atiende ningún distrito, la localidad no crece, aunque tenga XP (`town_growth.script.tl:415`).

```engine
El motor calcula el uso de línea, la velocidad del tráfico, los mapas de ruido y polución y la lista de entregas con retraso, y construye las nuevas casas y calles. La parte mínima que siempre recibe un distrito (townGrowthMinDistrictFraction) es un valor del motor.
```

## Demanda de cargamento y existencias de los edificios

- La demanda de una localidad es la suma de sus **edificios**. Cada edificio comercial o industrial tiene una pequeña reserva de entrada por cada cargamento que pide la localidad: capacidad ÷ 4, redondeada hacia arriba (`townbuildingutil.lua:226-251`). El juego anota que este tamaño de reserva "is currently nowhere shown in the UI" (de momento no se muestra en ninguna parte de la interfaz) (`townbuildingutil.lua:249`).
- La demanda de la ventana de la localidad es el límite total de estas reservas; el suministro que cuenta para la calificación está limitado a la demanda (`town_util.tl:95-99`, `town_util.tl:194-198`). Las localidades más grandes piden más porque tienen más edificios.
- La ventana del edificio muestra una **Calificación de consumo**: lo rápido que el edificio usa su cargamento en comparación con su máximo (`town_building.tl:103-132`).
- La XP y el pago llegan cuando una unidad entra en la reserva de un edificio (`town_growth.script.tl:620-642`).
- Una parada solo alcanza los edificios de su área de captación. Sus reservas pueden estar llenas mientras a la localidad en conjunto aún le falta cargamento: entonces el cargamento que no cabe **se queda en el vehículo**, salvo que esté marcado **Forzar la descarga de todo el cargamento al llegar** ("Descargar cargamento aunque se haya alcanzado el límite de existencias.") (`cargofilter_window.tl:757-763`), que destruye lo que no cabe (ver [Velocidad de carga y descarga](loading.html)).
- El cargamento que se queda a bordo genera la notificación **Cargamento sin descargar**: "Número de cargamentos del vehículo {vehicle} no descargados en la línea: {cargoCount}." (`cargo_rtc_warning.res.lua:6`, `cargo_rtc_warning.script.tl:28-41`).
- **Demandas de cargamento de localidades** ("Elige el límite de demandas de cargamento por cada localidad."): 2, 4 o 6, 2 por defecto (`difficulty_util.tl:54`, `difficulty_util.tl:83`, `mod.script.tl:173`, `mod.script.tl:205`). Los scripts añaden demandas según el nivel (ver arriba) y pasan este valor al motor.

```engine
La velocidad a la que un edificio consume su reserva (consumeFrequency), qué edificio de un área de captación recibe cada unidad, qué pasa con el cargamento que se lleva de un lado a otro y cómo usa el motor Demandas de cargamento de localidades se deciden en el motor.
```

## ¿Puedo impedir que una localidad crezca?

- En una partida normal **no hay ningún ajuste** de tamaño máximo de las localidades (`difficulty_util.tl:90-199`).
- En el **modo sandbox** y en el editor de mapas, la ventana de la localidad tiene una tarjeta **Capacidades del distrito objetivo** con **Activar desarrollo de la localidad** (`town_eow.script.tl:1041-1052`, `town_eow.script.tl:1170-1171`, `town_eow_editor_initial_capacity.res.lua:6`). Si se desmarca, la localidad no recibe XP y no cambia de tamaño; la ventana muestra **Desarrollo de la localidad inactivo** (`town_growth.script.tl:28`, `town_growth.script.tl:345`, `town_eow.script.tl:107`).
- Sin sandbox, las únicas formas son indirectas: una localidad solo crece con tus pasajeros y tu cargamento, y una sola calificación en Muy baja la detiene (ver arriba).

## Conviene saber

- **Corrige primero la peor calificación**: la autoridad es el mínimo, así que mejorar las demás no sirve de nada.
- Los pasajeros entre **dos localidades** dan 2 veces (vecinas) o 4 veces (más lejanas) la XP de los viajes dentro de una misma localidad, y a ambas localidades.
- Los cargamentos comerciales son solo de nivel 0–1; solo los **vehículos** (industriales) dan 40 XP por unidad, y normalmente una localidad solo los pide a partir de su tercera demanda industrial (nivel 11).
- Una localidad lejos de tu sede central no recibe su bonificación: solo la recibe la localidad más cercana.

```check
official: "A town needs 1,000 total XP to reach level 2. The XP required for each following level-up is 1.5 times the amount required for the previous level-up." Pasajeros 5 / 10 / 20 XP, cargamento 10 / 20 / 40 XP. "The Town Authority rating is determined by the lowest of six ratings." "A line usage of 50% gives the maximum rating." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Mismos números. Tasa de crecimiento de 0 a 100 % en pasos del 20 % según autoridad × suministros; una calificación Muy baja detiene el crecimiento; ninguna XP por viajes a industrias; demandas de cargamento añadidas solo tras una primera entrega de cargamento; la tercera demanda comercial no puede ser de nivel 2 en el juego base (no hay cargamento comercial de nivel 2); tamaño ×40 tras ganar 17 niveles.
result: refines
```
