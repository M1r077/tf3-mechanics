---
title: Costes, conservación y préstamos
summary: Qué cambian los ajustes de costes, qué costes crecen con el año del calendario, cómo se calcula el precio de los vehículos y cuánto cuesta realmente un préstamo.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
game: 40444
fact: ×6 | factor de año sobre la conservación de almacenes, puertos y aeropuertos en 2020
fact: 6 años | de gastos de mantenimiento: el precio de un vehículo
fact: una vez | el interés de un préstamo se aplica al importe, no cada año
fact: 4 | préstamos a la vez
---

El ajuste **Inflación** no sube ningún coste: solo baja tus ingresos a medida que sube el rango de la empresa (ver [Ingresos por cargamento](income.html)). Los costes crecen con el **año del calendario**, y cuatro controles los escalan desde el principio.

```diagram cost_years
```

## Los ajustes de costes

| Ajuste | Valores | Niveles Fácil · Normal · Difícil · Muy difícil | Fuente |
|---|---|---|---|
| **Gastos de vehículos**, **Mantenimiento de vehículos** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:39`, `difficulty_util.tl:98-101`, `difficulty_util.tl:125-128`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Gastos de infraestructura**, **Conservación de infraestructura** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:98-101`, `difficulty_util.tl:125-128`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Efecto del mantenimiento de vehículos** | Ninguno ×0 · Bajo ×0,5 · Medio ×1 · Alto ×1,5 · Muy alto ×2 | Bajo · Medio · Alto · Muy alto | `difficulty_util.tl:42`, `difficulty_util.tl:103`, `difficulty_util.tl:185` |
| **Inflación** | solo ingresos, ver [Ingresos por cargamento](income.html) | Baja · Normal · Alta · Muy alta | `difficulty_util.tl:50`, `mod.script.tl:695-698` |

- **Gastos de infraestructura** escala el precio de calles, vías, puentes, túneles, cruces, edificios y módulos, y también de los trabajos de terreno (`post_run_util.tl:23-52`, `post_run_util.tl:83-120`, `construction.script.tl:31-35`, `mod.script.tl:224-227`). También escala el coste de demolición de los edificios (`construction.script.tl:39-44`). **Conservación de infraestructura** escala al cargar la conservación de calles, vías, puentes, túneles, cruces y módulos (`post_run_util.tl:43-45`, `post_run_util.tl:105-112`). En los edificios, los scripts solo la aplican en la ventana del edificio (`entity_window_util.tl:186`); lo que se cobra lo decide el motor.
- **Gastos de vehículos** y **Mantenimiento de vehículos** escalan el precio de compra y los gastos de mantenimiento de cada vehículo (`post_run_util.tl:54-81`).
- **Efecto del mantenimiento de vehículos** fija cuánto pierde un vehículo en mal estado en velocidad, potencia y comodidad, y cuánto gana en ruido, contaminación y gastos de mantenimiento (`mod.script.tl:242-246`).

## Qué crece con el año del calendario

- **Conservación de edificios**: ×1 en 1900, ×1,5 en 1920, ×2,2 en 1940, ×3,2 en 1960, ×4 en 1980, ×5 en 2000, ×6 en 2020 (`mod.script.tl:92-100`). La ventana del edificio y el menú de construcción lo aplican a cada edificio marcado para seguir el año, y el menú de construcción marca todas las metaconstrucciones (en el juego base: almacenes, aeródromos, aeropuertos y puertos) (`entity_window_util.tl:186-193`, `construction_react_util.tl:1152`, `warehouse.tl:7`, `harbor_modular.tl:24`).
- Los **módulos** añadidos a un edificio así se cobran según el año en que se construyó el edificio, y su conservación según el año actual (`construction.tl:3741-3748`, `construction.tl:4413-4416`).
- **Variantes por época**: depósitos, edificios de mantenimiento, almacenes, estaciones, puertos y aeropuertos tienen una variante por época, y cada variante posterior cuesta **×3** (época B) o **×9** (época C) de la primera (`rail_depot.con.lua:7`, `warehouse.tl:48`, `modular_station.con.lua:71`, `harbor_modular.tl:76`, `airport.tl:8`).
- **Dinero de las subvenciones**: ×1 en 1900 hasta ×4 desde 2000 (`finances_util.tl:87-90`). **Importe de los préstamos**: ×0,4 en 1900 hasta ×2,4 en 2020 (`loan_util.tl:7-10`).
- Los **ingresos** no tienen ningún factor de año (`cargo_income.script.lua:10-13`).

```engine
La conservación que se cobra de verdad, y si calles, vías y vehículos también siguen la tabla de años, lo decide el motor (getCostMultiplierForYear; la configuración base solo fija chargeMaintenanceInterval = 60, `mod.script.tl:105`). Los scripts solo calculan los valores que se muestran en las ventanas y en el menú de construcción, con la tabla de arriba. Ningún script activa la marca «seguir el año» de los demás edificios.
```

## Vías, carreteras y edificios

Los archivos de calles y vías dan el precio y la conservación anual por metro; el menú de construcción los muestra por kilómetro (`construction_react_util.tl:2466`, `construction_react_util.tl:2480-2488`). En la mayoría de los tipos, la conservación es **un sexto** del precio de construcción:

| Tipo | Disponible desde | Construcción por km | Conservación por km y año | Fuente |
|---|---|---|---|---|
| Vía simple | inicio | 60.000 | 10.000 | `simple.street_template.lua:9`, `simple.street_template.lua:33` |
| Vía estándar | 1930 | 180.000 | 30.000 | `standard.street_template.lua:11`, `standard.street_template.lua:35` |
| Vía de alta velocidad | 1980 | 540.000 | 90.000 | `high_speed.street_template.lua:11`, `high_speed.street_template.lua:35` |
| Carretera rural antigua pequeña | inicio – 1940 | 60.000 | 10.000 | `country_old_small.street_template.lua:4-5`, `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:58` |
| Calle urbana moderna grande | 1940 | 540.000 | 90.000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:91` |

- La catenaria suma un **30 %** del precio de la vía; un carril bus, un 10 %; una vía de tranvía, un 20 %; una vía de tranvía eléctrico, un 40 % del precio de la calle (`mod.script.tl:24-28`).
- Subir el terreno cuesta 4,5 por m³, bajarlo 5,25 por m³, ambos × Gastos de infraestructura; y quitar un campo 200.000 (`mod.script.tl:20-22`, `mod.script.tl:33`, `mod.script.tl:226-227`).
- Un edificio que no fija conservación paga **un sexto de su precio** al año, calculado sobre el precio antes del ajuste Gastos de infraestructura (`construction.script.tl:25-27`).
- La configuración base fija un factor de reembolso al demoler de 0,75 y un tiempo de reembolso de 60 (`mod.script.tl:30-31`): si demueles lo que acabas de construir, recuperas la mayor parte del dinero. Lo aplica el motor.

Conservación anual escrita en los archivos, para la primera variante (antes de 1940) y las siguientes; los almacenes reciben además el factor de año de arriba:

| Edificio | Primera variante | ×3 (desde 1940) | ×9 (desde 1980) | Fuente |
|---|---|---|---|---|
| Depósito de trenes, depósito de barcos | 100.000 | 300.000 | 900.000 | `rail_depot.con.lua:34`, `water_depot.con.lua:32` |
| Depósito de carretera | 30.000 | 90.000 | 270.000 | `road_depot.con.lua:32` |
| Depósito de tranvías | 20.000 | 60.000 | 180.000 | `tram_depot.con.lua:34` |
| Edificio de mantenimiento de trenes o barcos | 40.000 | 120.000 | 360.000 | `rail_maint_station.con.lua:32`, `water_maint_station.con.lua:32` |
| Edificio de mantenimiento de carretera | 10.000 | 30.000 | 90.000 | `road_maint_station.con.lua:32` |
| Almacén universal | 25.000 | 75.000 | 225.000 | `warehouse.tl:48-52`, `warehouse.tl:75` |
| Almacén especializado | 50.000 | 150.000 | 450.000 | `warehouse.tl:51`, `warehouse.tl:75` |

Construir cada uno de estos edificios cuesta **6 ×** su conservación (`rail_depot.con.lua:35`, `warehouse.tl:76`): 2,7 M para un almacén especializado de la última época, antes del factor de año.

- El primer **aeródromo** (hasta 1950) ya usa el ×3 de la segunda época: su comprobación lee el año final de la variante en lugar del año inicial (`airfield.tl:8`, `airfield_era_a.metacon.tl:3`).

## Vehículos

Ningún vehículo del juego base tiene un precio fijo: el juego lo calcula a partir de la velocidad y la capacidad del vehículo al cargar el modelo (`model_metadata_util.lua:488-552`):

1. **Gastos de mantenimiento al año** = unos 675 × velocidad media (m/s) × capacidad / 4 (`model_metadata_util.lua:499-518`). El 675 sale de los ingresos medios por km, reducidos para dejar margen a los viajes de vuelta vacíos, la compra y la bajada del precio de los billetes (`model_metadata_util.lua:500-508`).
2. La **velocidad media** es menor que la velocidad máxima (v en km/h): vehículos de carretera y tranvías v^0,78 + 4, trenes v^0,86 + 10, aeronaves −0,0000203 × v² + 0,17 × v + 28,36 (v como máximo 4.000), barcos el 65 % de la velocidad máxima (`model_metadata_util.lua:448-474`).
3. **Trenes**: un vagón cuenta la mitad de su capacidad; una locomotora cuenta además potencia ÷ velocidad máxima (km/h) × 12,5 como capacidad, también a la mitad (`model_metadata_util.lua:511-512`, `model_metadata_util.lua:526-540`). Una locomotora potente y lenta es cara.
4. **Precio** = **6 ×** los gastos de mantenimiento anuales (`model_metadata_util.lua:548-549`).

Ejemplo al 100 %: un autobús de 35 km/h para 48 pasajeros gasta unos 45.000 al año y cuesta unos 270.000.

- El estado de un vehículo tiene cinco niveles (100–80 %, y luego cada 20 %) (`vehicle_store_util.tl:231-234`); al **20 %** el juego avisa hasta que vuelve a superar el 30 % (`notifications.script.tl:310-318`).

```engine
La rapidez con que baja el estado de un vehículo, cuánto suben con ello los gastos de mantenimiento y si los precios de los vehículos cambian con el año son valores del motor (getMaintenanceRunningCostPenalty y las demás penalizaciones); los scripts solo los escalan con el Efecto del mantenimiento de vehículos.
```

## Préstamos

```diagram loan_interest
```

| Tipo | Importe hacia 1960 (×0,4 en 1900, ×2,4 en 2020) | Plazo | Tasa | Fuente |
|---|---|---|---|---|
| Pequeño | 5–10 M | 1–5 años | 3–5 % | `loan_util.tl:12-22` |
| Mediano | 15–25 M | 3–8 años | 5–8 % | `loan_util.tl:24-34` |
| Grande | 30–50 M | 5–12 años | 8–10 % | `loan_util.tl:36-46` |
| Muy grande | 40–60 M | 10–24 años | 10–12 % | `loan_util.tl:48-58` |

- La tarjeta lo llama **Tasa de interés anual**, pero la tasa se aplica **una sola vez** al importe: el interés total es importe × tasa, sea cual sea el plazo. Se paga en partes iguales cada mes junto con el capital (`loan_util.tl:102-111`, `loan_util.tl:126-136`, `loan.script.tl:83-99`). Por eso un préstamo largo cuesta menos al año que uno corto con la misma tasa.
- **Reembolsar** paga solo el resto del capital: los intereses restantes se anulan (`loan.script.tl:171-190`). El botón necesita ese importe en efectivo (`finances_loan_gui.tl:284-286`).
- Las tasas **no** dependen de la dificultad: cada tipo tiene su propio rango fijo (`loan_util.tl:12-58`).
- Como máximo **4 préstamos** a la vez (`loan_util.tl:4`, `loan.script.tl:134`). Una oferta se sustituye al cabo de medio año; la casilla de un préstamo que has pedido se queda vacía de 4 a 8 meses (`loan.script.tl:61-76`, `loan.script.tl:150`).
- Al empezar una partida, cada una de las cuatro casillas recibe los valores de un tipo al azar, así que la primera oferta «pequeña» puede ser un préstamo grande; cuando se renueva una oferta, cada casilla ofrece su propio tipo (`loan_util.tl:60-74`, `loan.script.tl:63-75`).

```tip scripts
**Pide el préstamo más largo y reembolsa pronto.** Los intereses totales son los mismos con cualquier plazo, las cuotas mensuales son menores, y Reembolsar anula los intereses restantes.
```

## Conviene saber

- Pide el préstamo **más largo** que puedas: el interés total es el mismo, repartido en más meses, y puedes reembolsarlo antes sin pagar el resto.
- Los edificios con variantes por época cuestan ×3 y ×9 en las épocas posteriores, y su conservación sigue creciendo con el año: un almacén especializado de la última época es un gran coste fijo.
- Un vehículo rápido y de gran capacidad cuesta más de mantener, pero también transporta más: el precio y los gastos de mantenimiento siguen a velocidad × capacidad, igual que los ingresos que puede generar.

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: La tasa de un préstamo depende solo de su tipo (3–12 %), no de la dificultad, y se aplica una vez al importe, repartida entre los meses del plazo; reembolsar antes anula los intereses restantes. La Inflación solo cambia los ingresos; la conservación de los edificios sigue el año (×1 a ×6); precio de un vehículo = 6 × sus gastos de mantenimiento anuales, ambos a partir de la velocidad y la capacidad.
result: differs
```
