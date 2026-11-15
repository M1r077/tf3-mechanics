---
title: ¿Por qué pierdo dinero?
summary: Qué paga, qué cuesta, y una comprobación en seis pasos para encontrar las líneas que pierden dinero y por qué, con enlaces a las páginas que explican cada punto.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-15
fact: 1 | pago por artículo, en el consumidor, por la línea recta
fact: 0 | pagado en un almacén o en un transbordo
fact: 100 % | pagado incluso con retraso
fact: ×6 | factor de año sobre la conservación de almacenes, puertos y aeropuertos en 2020
---

Una entrega paga por **una sola línea recta**, desde donde se produjo el cargamento hasta donde se usa, y solo cuando llega allí. Todo lo que construyes y compras cuesta dinero cada año, y una parte cada vez más con el año del calendario. Una línea pierde dinero cuando su parte de los pagos es menor que los costes que genera.

```diagram money_flow
```

## Qué paga

- **La distancia en línea recta** de la fuente al consumidor, más 8 × el desnivel. La longitud de tu ruta no cuenta (`cargo_income.script.lua:3-7`, `cargo_income.script.lua:5`).
- **Todos los cargamentos pagan lo mismo** por kilómetro: el factor de ingresos es 3,8 para todos (`cargotype.script.lua:7-13`).
- **Una vez, en el consumidor.** Descargar en un almacén o en una estación de transbordo no paga nada. El pago se reparte después entre las líneas de la cadena según la longitud en línea recta de cada tramo (medido en el juego).
- **El cargamento con retraso se paga entero**: el tiempo de viaje no se usa (`cargotype.script.lua:7-13`). El retraso baja en cambio la calificación **Entrega** de la localidad.
- **El rango de la empresa** baja todos los ingresos con el ajuste **Inflación**: en el rango 15, ×0,75 en Normal (`company_progression_util.tl:25-40`).
- Una **subvención cumplida** duplica los ingresos de las líneas que entregaron, durante 5 años (`subvention_util.tl:286`).

Detalles: [Ingresos por cargamento y tiempo de entrega](income.html).

## Qué cuesta

- **Vehículos**: los costes de funcionamiento siguen la velocidad media × la capacidad, y el precio equivale a 6 años de costes de funcionamiento (`model_metadata_util.lua:499-518`, `model_metadata_util.lua:548-549`).
- **Vías y carreteras**: alrededor de una sexta parte del precio de construcción por km y año; la vía de alta velocidad cuesta 9 veces la vía simple (`simple.street_template.lua:33`, `high_speed.street_template.lua:35`).
- **Depósitos, estaciones, almacenes, puertos, aeropuertos**: las variantes de épocas posteriores cuestan ×3 y ×9 (`rail_depot.con.lua:7`, `warehouse.tl:48`), y la conservación de almacenes, puertos y aeropuertos también sigue el año, de ×1 en 1900 a ×6 en 2020 (`mod.script.tl:92-100`).
- **Préstamos**: el tipo se cobra una vez sobre el importe, repartido a lo largo del plazo (`loan_util.tl:102-111`).
- **La Inflación no sube ningún coste**. Solo baja los ingresos.

Detalles: [Costes, conservación y préstamos](costs.html).

## Seis comprobaciones, en orden

```diagram money_check
```

1. **¿Qué líneas pierden dinero?** Mira el balance de cada línea, no el total de la empresa. El mod [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) muestra el balance de cada línea en los últimos 12 meses y su media de varios años.
2. **¿Va lejos el cargamento?** Solo paga la línea recta de la fuente al consumidor. Una línea de aporte corta hacia un almacén solo recibe la parte de su propio tramo corto ([Ingresos por cargamento y tiempo de entrega](income.html)).
3. **¿Va lleno?** Un vehículo cuesta lo mismo lleno o vacío. Mira los viajes de vuelta vacíos, el **nivel de llenado** y la **capacidad máxima** de cada parada ([Ajustes de salida: capacidad máxima, nivel de llenado y tiempos de parada](departure.html)).
4. **¿Se descarga donde paga?** Lo que no está en la lista Carga de una parada se descarga en cualquier existencia cercana, almacenes incluidos, y un almacén no paga nada ([Velocidad de carga y descarga](loading.html), [Almacenes](warehouses.html)). El cargamento que no cabe en existencias llenas de la localidad se queda a bordo ([Crecimiento de las localidades: XP, calificaciones y tamaño](towns.html)).
5. **¿Demasiado vehículo?** La velocidad y la capacidad cuestan dinero, pero la velocidad no paga: solo ayuda cuando da más viajes al año. En la ciudad, un autobús viejo y lento puede ser más rentable que uno nuevo y rápido ([Costes, conservación y préstamos](costs.html)).
6. **Costes fijos.** Los depósitos, los módulos de almacén extra, las vías rápidas y los edificios de una época posterior cuestan cada año, se usen o no ([Costes, conservación y préstamos](costs.html)).

## Bueno saber

- **Elige los cargamentos por volumen y distancia**, no por precio: todos pagan lo mismo por km.
- Una **línea principal larga** alimentada por líneas cortas gana la mayor parte del dinero; las líneas de aporte muestran balances pequeños, pero lo que cuenta es la cadena entera.
- **Más que transportar**: una industria reforzada produce más ([Trabajadores y el refuerzo de trabajadores](workers.html), [Industrias](industries.html)), y una localidad más grande pide más cargamento.
- Hacer más rápida una línea no sube el pago por artículo. Solo ayuda si los mismos vehículos hacen más viajes.

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks))
scripts: Igual: línea recta más 8 × desnivel, el mismo factor para todos los cargamentos, tiempo de viaje no usado; medido en el juego: pagado una vez en el consumidor y repartido por longitud de tramo; los costes siguen velocidad × capacidad en vehículos, 1/6 del precio en vías, variantes de época ×3 / ×9 y factor de año ×1 a ×6 en edificios; la Inflación solo baja los ingresos.
result: refines
```
