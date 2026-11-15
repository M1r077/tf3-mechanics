---
title: Vehículos: condición, edad y velocidad de carga
summary: Qué significan las estadísticas de los vehículos, cómo funcionan la condición y la edad, qué hacen los depósitos y las estaciones de mantenimiento, de dónde salen el precio y los costes de funcionamiento, y cuándo sustituir un vehículo.
domain: vehicles
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-16
fact: 5 | niveles de condición, de Muy mala a Muy buena, 20 % cada uno
fact: 20 % | condición que activa el aviso Condición del vehículo
fact: 6 años | de costes de funcionamiento: el precio de un vehículo
fact: 4 a 16 | vehículos en los recursos de mantenimiento de un depósito o estación de mantenimiento
---

Cada vehículo tiene estadísticas fijas (velocidad, capacidad, velocidad de carga, precio, costes de funcionamiento, vida útil) y dos valores que cambian: su **condición** y su **edad**. La condición baja mientras circula y el mantenimiento la restablece. La edad solo crece.

## Las estadísticas en la tienda de vehículos

- La tienda muestra cada estadística como una barra. La barra compara el vehículo con los demás del mismo medio de transporte y la misma época, no con una escala fija (`vehicle_util.tl:210-245`, `vehicle_util.tl:248-270`).
- Para un tren, la tienda muestra la velocidad de carga **más alta** de todas sus partes (`vehicle_store_util.tl:333`).
- Un vehículo cuyo archivo no fija velocidad de carga, ruido, contaminación o comodidad recibe un valor calculado a partir de sus otras estadísticas (año, velocidad, potencia, peso, tamaño) (`model_metadata_util.lua:395-417`, `vehicle_metadata_util.lua:233-256`). La velocidad de carga calculada se redondea a 0,5 y nunca es inferior a 1 (`vehicle_metadata_util.lua:267-269`).

## ¿Qué vehículo carga más rápido?

La velocidad de carga del vehículo es solo el primer factor; el andén y las existencias la multiplican (ver [Velocidad de carga y descarga](loading.html)).

| Medio de transporte | Velocidad de carga mostrada como barra llena (última época) | Source |
|---|---|---|
| Barcos | 10 a 45 (desde 2003) | `vehicle_util.tl:219-223` |
| Vehículos de carretera, tranvías | 0,5 a 10 (desde 1995) | `vehicle_util.tl:232-243` |
| Trenes | 0,1 a 10 (desde 1981) | `vehicle_util.tl:226-229` |
| Aviones | 1 a 4 (desde 1978) | `vehicle_util.tl:212-216` |

- Los barcos tienen con diferencia las velocidades de carga más altas; los aviones, la escala más baja.
- Compara los vehículos de un mismo medio de transporte en la tienda con la columna de velocidad de carga; los modelos más nuevos suelen estar más arriba en la barra.
- Todo cargamento tiene un factor de carga de 0,0625; los pasajeros, 1 (`coal.cargo.lua:29`, `passengers.cargo.lua:23`).

```engine
Cómo se combinan la velocidad de carga del vehículo, el factor de carga del cargamento y los factores del andén y de las existencias en el tiempo de carga real lo calcula el motor. Los scripts solo dan los datos de entrada.
```

## Condición

| Condición | Nivel | Source |
|---|---|---|
| más del 80 % | **Muy buena** | `vehicle_util.tl:159-172` |
| 60–80 % | **Buena** | `vehicle_util.tl:159-172` |
| 40–60 % | **Mediocre** | `vehicle_util.tl:159-172` |
| 20–40 % | **Mala** | `vehicle_util.tl:159-172` |
| hasta el 20 % | **Muy mala** | `vehicle_util.tl:159-172` |

- La condición de un tren es la **media** de todos sus vagones y locomotoras (`vehicle_util.tl:285-295`).
- Por debajo del 80 %, un vehículo empieza a perder velocidad máxima, potencia y comodidad, y a ganar ruido, contaminación y costes de funcionamiento (`vehicle_store_util.tl:230-259`). La ventana del vehículo enumera estas penalizaciones en **Condición**.
- La intensidad de estas penalizaciones la fija **Efecto del mantenimiento de vehículos** (Ninguno, Bajo, Medio, Alto, Muy alto); con Ninguno, la condición no tiene efecto (`mod.script.tl:241-245`, `vehicle_store_util.tl:211-228`). Detalles: [Costes, conservación y préstamos](costs.html).
- Con un **20 %** o menos recibes el aviso **Condición del vehículo**. Se mantiene hasta que el vehículo vuelve a superar el **30 %** (`notifications.script.tl:310-318`).
- Un vehículo clonado es una compra nueva: condición 100 %, nueva fecha de compra (`manager_window.tl:8502-8506`).

```engine
La rapidez con que baja la condición, cuánto restablece una visita a una estación de mantenimiento y el tamaño de cada penalización (getMaintenanceTopSpeedPenalty y las demás) son valores del motor. Cada modelo de vehículo también puede fijar su propia penalización de velocidad máxima por nivel (`vehicle_store_util.tl:250-253`).
```

## Depósitos y estaciones de mantenimiento

Los vehículos reciben mantenimiento de un depósito o una estación de mantenimiento cercanos. Cada uno atiende a un número limitado de vehículos: sus **Recursos de mantenimiento**.

| Edificio | Recursos de mantenimiento | Source |
|---|---|---|
| Depósito de trenes | 6 | `rail_depot.script.lua:349` |
| Estación de mantenimiento de trenes | 12 | `rail_maint_station.script.lua:157` |
| Depósito de carretera, depósito de tranvías | 12 | `road_depot.script.lua:198`, `tram_depot.script.lua:226` |
| Estación de mantenimiento de carretera | 16 | `road_maint_station.script.lua:240` |
| Depósito de barcos | 8 | `water_depot.script.lua:379` |
| Estación de mantenimiento de barcos | 12 | `water_maint_station.script.lua:262` |
| Hangar de aeródromo o aeropuerto | 16 | `af_hangar.module.lua:280`, `ap_hangar.module.lua:463` |
| Helipuerto | 4 | `heliport.script.lua:309` |

- La ventana del edificio muestra "usados / recursos" (por ejemplo 14 / 12) y la lista de vehículos que atiende, con su condición (`entity_window_util.tl:2010-2039`, `maintenance_station_eow.script.tl:188-215`).
- Cuanto más lleno está, más ruidoso y contaminante es el edificio: las emisiones suben con la parte de los recursos en uso (`emissions.script.tl:223-234`).
- Una estación de mantenimiento de trenes atiende el doble de trenes que un depósito de trenes: 12 frente a 6.
- La wiki oficial sugiere puntos de paso para hacer pasar los vehículos por un edificio de mantenimiento.

```engine
A qué estación se asigna un vehículo, qué pasa cuando más vehículos usan una estación de los que admiten sus recursos, y el radio de influencia usado, lo decide el motor.
```

## Precio y costes de funcionamiento

- Los vehículos del juego base no tienen precio fijo: los costes de funcionamiento salen de la velocidad y la capacidad, y el precio equivale a **6 años** de costes de funcionamiento (`model_metadata_util.lua:548-549`). Fórmula completa: [Costes, conservación y préstamos](costs.html).
- **Gastos de vehículos** y **Mantenimiento de vehículos** los escalan ambos del 50 % al 150 % (`post_run_util.tl:54-81`).
- Un vehículo en mal estado paga más costes de funcionamiento, además del valor base (`vehicle_store_util.tl:256-259`).

## Edad y vida útil

- Cada modelo tiene una **vida útil** en años (`vehicle_metadata_util.lua:79-83`). La columna **Edad** de la ventana de la línea muestra la edad; su descripción emergente muestra la parte de la vida útil consumida y el tiempo restante, o **Vida útil cumplida** (`line_eow.script.tl:133-147`).
- Para un tren, cuenta la parte **más antigua** (`vehicle_util.tl:36-52`). Un solo vagón viejo hace que todo el tren aparezca como viejo.

```engine
Qué cambia al alcanzar la vida útil (por ejemplo, una pérdida de condición más rápida o un valor de venta más bajo) no está en los scripts. Los scripts solo muestran la edad y la vida útil.
```

## ¿Cuándo debo sustituir los vehículos viejos?

1. **La condición sigue baja** aunque haya una estación de mantenimiento cerca: el vehículo pierde velocidad y paga más costes de funcionamiento. Revisa primero los recursos de la estación: pueden estar llenos.
2. **Vida útil cumplida** en la descripción emergente de Edad: el modelo ha superado su vida prevista.
3. **Existe un modelo mejor**: los vehículos más rápidos o más grandes cuestan más de mantener en servicio, pero transportan más (el precio sigue a velocidad × capacidad).
4. Usa **Sustituir vehículos** en el gestor de líneas. Abre la tienda con una comparación con el vehículo actual (`vehicle_store_window.tl:4893-4928`, `vehicle_store_window.tl:2611`).

## Conviene saber

- Construye suficiente capacidad de mantenimiento: un depósito de trenes solo atiende 6 trenes.
- Con **Efecto del mantenimiento de vehículos** en Ninguno, la condición no importa.
- **Enviar al depósito** envía un vehículo al depósito alcanzable más cercano, no al que se compró (wiki oficial).
- [Vehicle Comparison](https://mod.io/g/transportfever3/m/vehicle-comparison) ayuda a comparar modelos antes de sustituirlos.

```check
official: "This section shows how well the vehicle is maintained and how the maintenance state affects the vehicle properties." "Loading speed modifies a vehicle's base loading speed which can be seen in the vehicle window or in the vehicle store." ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles))
scripts: Cinco niveles de condición del 20 %; penalizaciones de velocidad, potencia, comodidad, emisiones y costes de funcionamiento por debajo del 80 %, escaladas por Efecto del mantenimiento de vehículos; aviso al 20 %, retirado por encima del 30 %. Recursos de mantenimiento de 4 a 16 vehículos por edificio. Precio = 6 años de costes de funcionamiento. Edad de un tren = su parte más antigua. Las velocidades de carga que faltan se calculan a partir de las otras estadísticas, redondeadas a 0,5, como mínimo 1.
result: refines
```
