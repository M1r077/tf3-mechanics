---
title: Ingresos por cargamento y tiempo de entrega
summary: Cuánto paga una entrega (distancia en línea recta, desnivel, rango de la empresa, subvenciones) y cuánto cuesta realmente un retraso.
domain: economy
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
game: 40425
fact: 3,8 | el mismo factor de ingresos para todos los cargamentos
fact: +8 × desnivel | metros de subida sumados a la distancia
fact: 100 % | se paga aunque la entrega llegue tarde
---

Una entrega paga por la **distancia en línea recta**, y nada más del viaje. La velocidad importa por otro motivo: cada cargamento tiene un **plazo**, y las entregas con retraso bajan la calificación **Entrega** de la localidad, no tus ingresos.

```diagram income_formula
```

## La fórmula de los ingresos

La fórmula completa es un breve script del juego (`cargo_income.script.lua:10-13`):

1. **Factor de ingresos** del cargamento. Todos los cargamentos del juego base usan la misma función y los mismos precios (`initialPrice = 4`, `finalPrice = 3.2`), lo que da **3,8 para los 36 cargamentos** (`cargotype.script.lua:7-13`, `coal.cargo.lua:21-22`). El carbón paga exactamente lo mismo que las mercancías en la misma distancia.
2. Ajuste **Ingresos por el cargamento**: 50 %, 75 %, 100 %, 125 % o 150 % (`difficulty_util.tl:38`, `mod.script.tl:211`). Los cuatro niveles de dificultad predefinidos usan 100 % (`difficulty_util.tl:97`).
3. **Distancia**, ver más abajo.

La función recibe el tiempo de viaje pero **no lo usa** (`cargotype.script.lua:7-13`): una entrega lenta o con retraso paga lo mismo.

## Distancia: línea recta más desnivel

```diagram income_distance
```

- La distancia es la **línea recta en 3D** entre los dos puntos, no la longitud de tu ruta (`cargo_income.script.lua:3-7`).
- Cuando la diferencia de altura es positiva, se suma **8 × esa altura** (`cargo_income.script.lua:5`): 100 m de subida pagan como 800 m más. En sentido contrario no se resta nada.
- Así, una línea llena de curvas rinde lo mismo que una recta, pero pagas el mantenimiento de cada metro de vía o carretera que construiste.

```engine
El motor elige los dos puntos y se los pasa al script. Medido en el juego (ver abajo): son el **origen** del cargamento (la industria o el edificio de la localidad que lo produjo) y el **consumidor** que lo recibe, tal como dice la wiki oficial ("between the source and the final destination").
```

## Cargamento que cambia de línea

Cuando un artículo viaja en varias líneas, por ejemplo barco → almacén → tren, el juego lo sigue pagando **una sola vez**:

```diagram income_split
```

1. Descargar en un almacén o en una estación de transbordo no paga **nada**. De unos 17.000 pagos medidos, solo 43 fueron a un destino que no era un consumidor.
2. Cuando el último vehículo entrega al consumidor, el artículo se paga con la fórmula de arriba, por la línea recta **desde el origen hasta el consumidor**. Los tramos y la ruta real no cuentan, así que un rodeo por un almacén no rinde nada más.
3. Ese dinero se reparte entre las líneas de la cadena **en proporción a la longitud en línea recta de cada tramo**: de un punto de recogida al siguiente, y del último punto de recogida al consumidor. La bonificación por desnivel no cuenta en este reparto.
4. El vehículo que entrega retiene primero el importe completo, con una parte por tramo. Se contabiliza unos segundos de tiempo de juego más tarde (mediana de unos 6 s), y cada línea y cada vehículo recibe su propia parte. Por eso el saldo de una línea cambia poco después de la entrega, no en el almacén.

Así, una línea corta de alimentación hacia un almacén rinde poco, aunque haga toda la recogida; el tramo largo se lleva la mayor parte. Cada línea sigue mostrando su parte real en su propio saldo.

```engine
Los scripts solo calculan el total (`economy/cargo_income.script.lua`); el reparto lo hace el motor y no es visible en los scripts. Las reglas de arriba se midieron con un mod de prueba de solo lectura: unos 1.700 pagos de artículos con 2 o 3 tramos, y los cambios de cuenta de cada línea y vehículo implicados. En 769 casos limpios (un artículo, un pago) el reparto coincidió con las longitudes de los tramos con un margen del 1 % todas las veces; un reparto con la bonificación por desnivel coincidió solo en el 59 % de ellos, y un reparto a partes iguales en ninguno.
```

## Qué más cambia el importe

| Qué | Efecto | Fuente |
|---|---|---|
| **Rango de la empresa** con el ajuste Inflación | rango 1: ×1, bajando de forma regular hasta el rango 15: ×0,9 (Baja), **×0,75 (Normal)**, ×0,6 (Alta), ×0,5 (Muy alta); Ninguna: siempre ×1 | `company_progression_util.tl:25-40`, `difficulty_util.tl:50`, `mod.script.tl:694-697` |
| **Subvención cumplida** | ×2 para entregas a la industria o localidad del contrato, en las líneas que entregaron para el contrato | `deliver_cargo.script.tl:463-469`, `deliver_cargo_town.script.tl:554-565` |
| **Entrega con retraso** | ningún efecto en los ingresos | `cargotype.script.lua:7-13` |

- El multiplicador de rango se aplica a **todos** los pagos de cargamento y de pasajeros (`company_growth.script.tl:159-170`). Los niveles de dificultad usan Inflación Baja (Fácil), Normal (Normal), Alta (Difícil), Muy alta (Muy difícil) (`difficulty_util.tl:108`).
- El ×2 de las subvenciones solo se aplica a las líneas que entregaron durante el contrato, durante un tiempo limitado (wiki oficial, Subsidies).

## Pasajeros

Los pasajeros usan la misma distancia y un factor de ingresos fijo de unos 3,61 (`cargotype.script.lua:50-53`), multiplicado por **0,5 + el factor de precio del billete del vehículo** (`cargo_income.script.lua:14-17`). Cuando un modelo de vehículo no define su factor de comodidad, el juego fija el factor de precio en 0,3 para autobuses y tranvías, 0,9 para aeronaves, 0,1 para barcos y 0,5 para trenes (`base_mod.lua:46-61`); para los demás modelos es un valor del motor, no visible en los scripts. Una subvención de pasajeros solo duplica los pasajeros que viajan entre sus dos localidades, en su única línea (`deliver_passengers.script.tl:292-296`).

## Plazos de entrega

Cada cargamento tiene su propio plazo (`meat.cargo.lua:30`, `coal.cargo.lua:30`). Los alimentos frescos tienen el más corto; las materias primas pesadas, uno cinco veces más largo:

```diagram delivery_times
```

- **Finanzas › Tiempo de entrega** muestra el plazo de cada cargamento en tu mapa; la capa de satisfacción de cargamento colorea las rutas de verde a rojo.
- Una entrega cuenta como **retrasada** cuando llega después de su plazo (`towns.script.tl:425`).
- Los módulos de almacén especializados **congelan** el plazo del cargamento que guardan (wiki oficial, Warehouses).

```engine
El motor convierte el tiempo base en el plazo que se muestra en Finanzas (los scripts lo leen con getAdjustedDeliveryTime) y decide cuándo un artículo va con retraso. Solo los valores relativos de arriba proceden de los archivos de cargamento.
```

## Lo que cuesta un retraso: la calificación Entrega

El cargamento con retraso se paga entero, pero cada localidad lleva una calificación **Entrega** (`town_util.tl:505-519`):

1. El juego cuenta las entregas a la localidad durante el **último medio año**, y cuántas llegaron tarde (se suponen al menos 10, para que las primeras entregas no la hagan oscilar).
2. Proporción a tiempo → calificación: por debajo de un límite inferior la calificación es 0, por encima de un límite superior es 1, y lineal entre ambos. Con la susceptibilidad por defecto (**Normal**): **30 % a tiempo → 0, 100 % → 1**, así que un 90 % a tiempo da 0,86.
3. El ajuste **Susceptibilidad a las entregas** desplaza los límites (`difficulty_util.tl:47`). No: siempre 1. Niveles predefinidos: Fácil Baja, Normal Normal, Difícil Alta, Muy difícil Muy alta (`difficulty_util.tl:113`).

```diagram delivery_rating
```

Entrega es una de las seis calificaciones cuya más baja fija la tasa de crecimiento de la localidad: una sola calificación Muy baja detiene la localidad (ver [Crecimiento de las localidades](towns.html)).

## Ejemplo

La misma entrega de carbón, a 5 km en línea recta.

| Situación | Pagado |
|---|---|
| terreno llano, cualquier longitud de ruta | **100 %** |
| a 10 km | **200 %** |
| destino 100 m más alto | **116 %** |
| entregado con retraso | **100 %** (baja la calificación Entrega) |
| rango de la empresa 15, Inflación Normal | **75 %** |
| entrega cubierta por una subvención cumplida | **200 %** |

## Conviene saber

- Como todos los cargamentos pagan lo mismo por kilómetro, **elige los cargamentos por volumen, distancia y plazo**, no por precio.
- Los plazos importan sobre todo para la carne, el pescado, los vegetales y las bebidas: líneas cortas, o almacenes que congelan el plazo.
- Cada unidad entregada a un edificio de la localidad también da experiencia a esa localidad (`town_growth.script.tl:642`, `town_growth_config.res.lua:5`).

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks), [Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Mismo factor 3,8 para todos los cargamentos; distancia en 3D más 8 × el desnivel; el rango de la empresa reduce los ingresos hasta ×0,75 en el rango 15 (Inflación Normal); ×2 tras una subvención; el tiempo no se usa para los ingresos; medido en el juego: un artículo que cambia de línea se paga una sola vez, en el consumidor, y se reparte entre las líneas según la longitud de los tramos; calificación Entrega según la proporción a tiempo del último medio año (Normal: 30 % → 0, 100 % → 1).
result: refines
```
