---
title: Subvenciones: ofertas, plazos y recompensas
summary: Los cuatro tipos de contrato, qué los cumple de verdad, qué ganas y qué arriesgas, y con qué frecuencia llegan nuevas ofertas.
domain: subsidies
official: gamemanual:management:subsidies
status: verified
updated: 2026-11-15
fact: 4 | tipos de contrato en una partida libre
fact: 5 | contratos aceptados como máximo a la vez
fact: ×2 | de ingresos durante 5 años en las líneas que entregaron
fact: 0 | penalización por rechazar una oferta
---

Una subvención es un contrato: una industria o una localidad propone una tarea, recibes algo al aceptarla, más si la cumples a tiempo, y devuelves el anticipo más una penalización si se te pasa el plazo. Rechazar una oferta, o dejar que caduque, no cuesta nada.

```diagram subsidy_life
```

## Los cuatro tipos de contrato

```diagram subsidy_types
```

| Contrato | Objetivo | Qué lo cumple | Fuente |
|---|---|---|---|
| **Suministrar a industria** | una industria que nunca ha producido nada | el número exigido de entregas a ella, **de cualquiera de sus cargamentos de entrada** | `deliver_cargo.script.tl:54-61`, `deliver_cargo.script.tl:230-234`, `deliver_cargo.script.tl:470-479` |
| **Suministrar a localidad** | un cargamento que la localidad pide y no recibe en absoluto | el número exigido de unidades **de ese cargamento** entregadas a edificios de la localidad | `deliver_cargo_town.script.tl:566-581` |
| **Conectar localidades** | dos localidades | **un solo** pasajero que empieza un viaje entre las dos localidades en una línea que para en ambas | `deliver_passengers.script.tl:263-280`, `subvention_util.tl:561-592` |
| **Transportar trabajadores** | una industria que ya envía o recibe cargamento, aún sin refuerzo | su refuerzo de trabajadores se activa (la mitad de sus puestos de trabajo) | `deliver_workers.script.tl:121-131`, `deliver_workers.script.tl:152-156` |

- Cada nueva oferta elige uno de los tipos que pueden aparecer en ese momento, con la misma probabilidad (`subventions.script.tl:147-169`).
- **Suministrar a industria** y **Suministrar a localidad** cuentan entregas, no viajes: cada unidad pagada que llega al objetivo suma 1. Se permiten transbordos (`deliver_cargo.script.tl:470-479`).
- **Conectar localidades** no exige ningún número de pasajeros: el primer pasajero que sube a tu línea entre las dos localidades lo cumple. "Sin escalas" significa que ese tramo se hace en una sola línea que da servicio a ambas localidades. No aparece ninguna oferta si una línea ya transporta pasajeros entre ellas (`deliver_passengers.script.tl:72-78`).
- Las localidades cercanas son mucho más probables: el peso de una pareja baja de 1 a 1 km o menos a 0,01 a 20 km, elevado a la potencia 7 (`deliver_passengers.script.tl:175-191`).
- **Suministrar a localidad** prefiere cargamentos que ya se producen en algún lugar del mapa: 16 veces más probables que los demás (`deliver_cargo_town.script.tl:277-280`).
- La cantidad que hay que entregar depende del ajuste **Riesgo de las subvenciones**:

| Riesgo de las subvenciones | Suministrar a industria | Suministrar a localidad (como máximo la demanda de la localidad) | Fuente |
|---|---|---|---|
| Ninguno | 10–50 | 10–30 | `deliver_cargo.script.tl:100-114`, `deliver_cargo_town.script.tl:165-188` |
| Considerable | 50–100 | 30–100 | |
| Arriesgado | 75–150 | 35–125 | |
| Muy arriesgado | 150–300 | 45–150 | |

## ¿Qué es una conexión sin escalas?

La tarjeta **Conectar localidades** pide: "Crea una conexión sin escalas entre {fromTownName} y {toTownName} y transporta pasajeros entre ambas localidades." (`deliver_passengers.script.tl:14`).

- **Una línea con una parada en cada localidad.** El juego recorre las paradas de la línea y toma la localidad de cada una; la línea cuenta cuando al menos una parada está en cada una de las dos localidades. Las demás paradas, su orden y el tipo de vehículo (autobús, tranvía, tren, barco, avión) no importan (`subvention_util.tl:561-592`).
- **Un solo pasajero lo cumple**: el primer pasajero que viaja en esa línea desde una parada de una localidad hasta una parada de la otra, en cualquier sentido (`deliver_passengers.script.tl:263-280`, `deliver_passengers.script.tl:210-218`). La comprobación solo mira ese viaje, así que cambiar de línea antes o después no debería importar.
- **La localidad de una parada** es la localidad de la primera estación de su grupo de estaciones (`town_util.tl:1844-1873`). A qué localidad pertenece una estación lo decide el motor.
- **No hay oferta** cuando una línea ya tiene en cada localidad una parada que carga pasajeros y un vehículo que lleva pasajeros (`deliver_passengers.script.tl:72-78`). Una línea solo de mercancías entre ellas no bloquea la oferta.
- El contrato termina como **Subvención eliminada** cuando una de las dos localidades, o la línea que lo cumplió, cambia de una forma que el juego cuenta como una nueva versión (`deliver_passengers.script.tl:232-240`).

```engine
A qué localidad pertenece una estación (stationSystem.getTown), cuándo exactamente un pasajero "empieza a usar" una línea (OnStartedLineUsage) y qué cambios de una línea cuentan como una nueva versión depende del motor. No se ha probado si un cambio de la línea después de cumplir el contrato pone fin al efecto Ingresos x2.
```

## Recompensas y penalizaciones

Cada contrato guarda tres listas, que su tarjeta muestra como **Tras la aceptación**, **Tras el cumplimiento** y **Tras fallar** (`subvention_util.tl:449-471`). Si falla, el anticipo siempre se devuelve, más una penalización adicional (`deliver_cargo.script.tl:134-136`).

| Contrato | Tras la aceptación | Tras el cumplimiento | Tras fallar | Fuente |
|---|---|---|---|---|
| Suministrar a industria | dinero | solo el efecto **Ingresos x2** | devolución del anticipo + multa | `deliver_cargo.script.tl:120-136` |
| Suministrar a localidad | dinero **o** reputación en la localidad | experiencia de la localidad **o** dinero, más Ingresos x2 | devolución del anticipo + pérdida de reputación **o** multa | `deliver_cargo_town.script.tl:194-229` |
| Conectar localidades | dinero, más para localidades lejanas | experiencia en **ambas** localidades, más Ingresos x2 | devolución del anticipo + pérdida de reputación en **ambas** localidades | `deliver_passengers.script.tl:105-119` |
| Transportar trabajadores | dinero | dinero | devolución del anticipo + multa | `deliver_workers.script.tl:92-116` |

- **Dinero**, antes del ajuste por año: anticipo de 1,5 M a 3,75 M × el factor de riesgo (Ninguno ×2, Considerable ×1, Arriesgado ×0,75, Muy arriesgado ×0,5); multa de 3 M a 6 M; pago al cumplir de 3,75 M a 11,25 M (`deliver_cargo.script.tl:120-128`, `deliver_workers.script.tl:102-104`).
- El dinero crece con el **año del calendario**, no con el ajuste Inflación: ×1 en 1900, subiendo de forma regular hasta ×4 en 2000 y después, redondeado hacia arriba a 10.000 (`finances_util.tl:87-90`). Se contabiliza como **Subvenciones** en las finanzas (`subvention_util.tl:126-135`).
- **Suministrar a localidad** da recompensas en dinero y multas solo mientras tu cuenta bancaria esté por debajo de 100 M; por encima, solo 1 de cada 10 ofertas puede darlas todavía (`deliver_cargo_town.script.tl:206-217`).
- La **experiencia de la localidad** es una parte de su nivel actual: del 20 % al 100 % de la XP entre su nivel y el siguiente (`deliver_cargo_town.script.tl:216`, `town_growth.script.tl:605-608`). En **Conectar localidades** se multiplica por el factor de distancia, de 0,3 a 1 km hasta 3,0 a 20 km: las localidades lejanas pueden ganar varios niveles (`deliver_passengers.script.tl:94-96`, `deliver_passengers.script.tl:116-118`).
- La **reputación** perdida tras un fallo aparece en la calificación Reputación de la localidad como **Subvención fallida** (`towns.script.tl:313-334`). La reputación ganada al aceptar solo elimina penalizaciones existentes, no puede superar el máximo (`town_util.tl:1644-1647`).

## El efecto Ingresos x2

- Dura **60 meses** (5 años) tras cumplir el contrato (`subvention_util.tl:286`, `subvention_util.tl:292`).
- **Suministrar a industria**: las entregas a esa industria, en las líneas que le entregaron durante el contrato (`deliver_cargo.script.tl:463-469`).
- **Suministrar a localidad**: las entregas a cualquier edificio de esa localidad, **cualquier cargamento**, en las líneas que entregaron el cargamento del contrato (`deliver_cargo_town.script.tl:554-565`).
- **Conectar localidades**: los pasajeros entre las dos localidades, en **una** sola línea directa: la última línea directa a la que subió un pasajero entre ellas. Se sigue actualizando después del contrato, así que con dos líneas directas el ×2 puede pasar de una a otra (`deliver_passengers.script.tl:263-296`).
- **Transportar trabajadores** no tiene efecto en los ingresos (`deliver_workers.script.tl:90`).
- En Suministrar a industria y Suministrar a localidad, una línea que solo empezó a entregar después de cumplirse el contrato no recibe nada: la lista de líneas solo se llena durante el contrato.
- Dos contratos nunca duplican dos veces el mismo pago: cuando coinciden varios, solo se usa la última respuesta (`subventions.script.tl:570-583`).

```tip scripts
**¿Quieres los ingresos dobles de Suministrar a industria o Suministrar a localidad en varias líneas? Haz que todas entreguen antes de que se cumpla el contrato.** Una línea añadida después no recibe nada. Conectar localidades solo dobla una línea, la última directa a la que subieron pasajeros: mantén una sola línea directa entre las dos localidades.
```

```engine
Cómo se combina el ×2 de una subvención con el multiplicador de rango de la empresa (ajuste Inflación) lo decide el motor: ambos scripts solo devuelven un multiplicador para cada pago. Qué es una entrada de pago (probablemente una unidad de cargamento o un pasajero) también lo decide el motor.
```

## Plazos

El plazo empieza cuando aceptas. Es más largo cuando el cargamento tiene que viajar lejos y más corto con un riesgo más alto (factor de riesgo Ninguno ×2, Considerable ×1, Arriesgado ×0,75, Muy arriesgado ×0,5, o ×0,625 para los contratos de pasajeros y de trabajadores):

| Contrato | Plazo en meses | Distancia usada | Fuente |
|---|---|---|---|
| Suministrar a industria, Suministrar a localidad | (6 + 32 × E) × factor de riesgo | hasta la industria más cercana que produce el cargamento | `deliver_cargo.script.tl:116-117` |
| Conectar localidades | (9 + 4 × E) × factor de riesgo | entre las dos localidades | `deliver_passengers.script.tl:98-99` |
| Transportar trabajadores | (6 + 15 × E) × factor de riesgo × factor de época (×1,75 antes de 1940, ×1,25 antes de 1980) | hasta la localidad más cercana | `deliver_workers.script.tl:75-87` |

E es el tiempo que necesita un tren a la velocidad máxima de la época (120 km/h desde 1900 hasta 300 km/h desde 1981) para esa distancia, redondeado hacia arriba, como mínimo 1 (`subvention_util.tl:486-489`, `vehicle_util.tl:225-230`).

- Una oferta no aceptada desaparece tras unos **6 meses** (de 150 a 210 días), sin ninguna penalización (`subvention_util.tl:284`, `subvention_util.tl:290`).
- Mientras corre un contrato **Suministrar a industria** o **Transportar trabajadores**, la industria objetivo no puede cerrar: un cierre previsto se anula (`subvention_util.tl:473-484`).
- Si el objetivo desaparece o se reconstruye durante el contrato, el juego muestra **Subvención eliminada**, pero las penalizaciones por fallo se aplican como si se hubiera pasado el plazo (`subventions.script.tl:172-190`, `subvention_util.tl:406-412`).
- No hay ningún botón para cancelar un contrato aceptado.

```engine
Cuánto dura un mes de juego, y por tanto la duración real de los plazos, lo fija el motor (getDefaultMonthDuration). Las fórmulas de arriba están en meses del calendario del juego.
```

## Con qué frecuencia llegan nuevas ofertas

- **Disponibilidad de las subvenciones**: Casi nunca, A veces (por defecto), Con frecuencia, Con mucha frecuencia dan una nueva oferta cada 12, 6, 3 o 1 meses; **Nunca** desactiva las subvenciones (`subvention_util.tl:13-38`, `mod.script.tl:247-248`).
- El intervalo crece con el **rango de la empresa**: ×1 en el rango 1 hasta ×2 en el rango 15 (`subvention_util.tl:19-22`).
- **Rechazar** una oferta reduce a la mitad el siguiente intervalo; aceptar o una nueva oferta lo restablece (`subventions.script.tl:429`, `subventions.script.tl:395`, `subventions.script.tl:118`).
- No llega ninguna oferta nueva mientras haya **5 contratos** aceptados en curso (`subventions.script.tl:23`, `subventions.script.tl:256-262`). La primera oferta llega tras medio mes.
- El mismo objetivo (industria, localidad y cargamento, pareja de localidades) se ofrece **solo una vez por partida**, incluso tras un contrato perdido o fallido (`subventions.script.tl:107-113`, `subventions.script.tl:186`).
- Niveles de dificultad predefinidos, disponibilidad / riesgo (`difficulty_util.tl:104-105`, `difficulty_util.tl:132-133`, `difficulty_util.tl:159-160`, `difficulty_util.tl:186-187`): Fácil Con frecuencia / Ninguno, Normal A veces / Considerable, Difícil Casi nunca / Arriesgado, **Muy difícil Nunca**: ninguna subvención.
- La comprobación de calificación que solo permitiría subvenciones en localidades calificadas como Muy buena existe, pero está desactivada (`town_util.tl:1574-1580`, `deliver_cargo_town.script.tl:272-275`).

## Conviene saber

- Acepta sin miedo cuando el objetivo es fácil: rechazar o ignorar no cuesta nada, pero **fallar** cuesta la devolución del anticipo más una multa que puede ser mayor que el anticipo.
- En **Suministrar a localidad** y **Suministrar a industria**, empieza a entregar con todas las líneas que quieras beneficiar: solo las líneas que entregaron durante el contrato reciben los Ingresos x2 durante 5 años.
- **Conectar localidades** con localidades muy separadas da la mayor experiencia, y basta con un solo pasajero.
- **Suministrar a industria** no paga nada más al cumplirse: su recompensa son solo los Ingresos x2.

```check
official: "Accept an offer to begin the contract; declining it has no penalty." "Possible rewards include town experience, an additional payment, or a limited-time 2x income effect on eligible transport lines." "The upfront reward is reversed, and an additional fine or loss of town reputation may apply." ([Subsidies](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:subsidies))
scripts: Cuatro tipos; un solo pasajero cumple Conectar localidades; el ×2 dura 60 meses en las líneas que entregaron durante el contrato; Suministrar a industria solo da el ×2; dinero escalado según el año (×1 a ×4); una nueva oferta cada 1–12 meses, más espaciadas con un rango alto de la empresa; como máximo 5 aceptados; cada objetivo se ofrece una vez por partida.
result: refines
```
