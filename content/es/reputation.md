---
title: Reputación de las localidades
summary: Qué baja la calificación Reputación de una localidad, a qué ritmo vuelve, qué hacen de verdad las celebraciones y las campañas de marketing, y por qué una carretera cortada entre dos localidades cuesta tanto.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
game: 40425
fact: −33 % | por conexión principal interrumpida con otra localidad
fact: ≈ 67 % | recuperado al año a velocidad de calendario ×1 (≈ 200 % durante una campaña de marketing); la ventana de la localidad muestra 33 % y 100 %
fact: 0,25 % | por árbol adulto eliminado junto a la localidad
fact: 2 M m³ | de obras de terreno cuestan toda la reputación
---

La **Reputación** es una de las seis calificaciones de la ventana de la localidad, y la Autoridad municipal toma la **más baja** de ellas (ver [Crecimiento de las localidades](towns.html)). Empieza en 100 % y solo baja por lo que **tú** construyes o fallas: obras de terreno, árboles y rocas eliminados, edificios de la localidad demolidos, subvenciones fallidas y conexiones principales cortadas. El tiempo, las celebraciones y las campañas de marketing la recuperan.

```diagram rep_recovery
```

## Qué la baja

Cada construcción que confirmas se revisa antes de aplicarla; el coste se asigna a la localidad afectada (`towns.script.tl:271-291`, `town_util.tl:1062-1080`). Solo cuentan tus propias construcciones, y en el editor de mapas no cuenta nada (`town_util.tl:1078-1080`, `towns.script.tl:233`, `towns.script.tl:271`).

| Motivo en la ventana de la localidad | Qué cuesta reputación | Fuente |
|---|---|---|
| **Árboles eliminados** | 0,25 % por árbol, × el factor de distancia a la localidad más cercana, × el tamaño del árbol (los árboles pequeños cuentan menos) | `town_util.tl:1144-1150`, `town_util.tl:865`, `model_metadata_util.lua:655-680` |
| **Rocas eliminadas** | 0,25 % por roca, × el factor de distancia | `town_util.tl:1148-1149`, `town_util.tl:884-885` |
| **Paisajismo** | 0,00005 % por m³ de terreno elevado **o** hundido: 2 millones de m³ = 100 %. También cuenta el terreno que forman vías, carreteras y edificios (reducido a partir de 10.000 m², a la mitad desde 50.000 m²), y el volumen neto de los túneles nuevos | `town_util.tl:873-886`, `town_util.tl:1245-1269`, `town_util.tl:1403-1436` |
| **Edificios demolidos** | 100 % por el 40,5 % de la capacidad de un distrito eliminada (viviendas, comercios o empleos de esa localidad) | `town_util.tl:867-869`, `town_util.tl:1165-1184` |
| **Subvención fallida** | Suministrar a localidad: una penalización elegida al azar, la pérdida de reputación (del 10 % hasta 60–90 % según el riesgo) o una multa; siempre la pérdida de reputación si no se ofrece multa. Conectar localidades: 10–100 % × el factor de distancia, en **ambas** localidades (ver [Subvenciones](subsidies.html)) | `deliver_cargo_town.script.tl:202-210`, `deliver_cargo_town.script.tl:209-211`, `deliver_cargo_town.script.tl:225`, `deliver_passengers.script.tl:113-114`, `towns.script.tl:331-333` |
| **Conexiones principales interrumpidas** | **1/3** por cada otra localidad cuya conexión principal está cortada o es demasiado larga | `town_util.tl:376-394`, `town_util.tl:1608` |

- Cada motivo tiene un tope del 100 % (`town_util.tl:1611-1620`).
- Mientras construyes, la ayuda emergente muestra **Reputación: −x %**, con el número de localidades afectadas si son varias (`construction_react_util.tl:3818-3864`). Cuenta el coste desde una calificación completa.
- Plantar árboles o colocar rocas solo anula **Árboles eliminados** o **Rocas eliminadas**, con el mismo 0,25 % por unidad. No hace nada por los otros motivos, ni con la reputación completa (`town_util.tl:1228-1238`, `town_util.tl:1630-1641`).
- El ajuste Reputación de una partida nueva es **No** o **Sí** (Sí en todos los preajustes). No significa calificación completa, siempre (`difficulty_util.tl:44`, `difficulty_util.tl:110`, `town_util.tl:396-399`).

```engine
La rapidez con la que baja el factor de distancia entre una localidad y un árbol eliminado, el volumen de terreno que recibe cada localidad, los árboles que una vía o carretera elimina automáticamente, y qué carreteras cuentan como conexión principal de una localidad (y cuándo un trayecto es «demasiado largo») son valores del motor (getImpactFromDistance, getTerrainBrushVolumeImpact, getTerrainAlignmentImpact, getAutoRemovalEntityImpact, getTownProblems).
```

## Conexiones principales cortadas

Una conexión principal cuenta como cortada cuando el juego avisa **Se corto la conexión por carretera entre las ciudades.** o **El tiempo de viaje entre las ciudades es demasiado largo** (`town_util.tl:378-380`, `town_warning.script.tl:7-22`). Cada otra localidad afectada cuesta 1/3, y la calificación lo muestra **al instante** (`town_util.tl:401-403`):

| Conexiones cortadas | Reputación como máximo | Calificación | Fuente |
|---|---|---|---|
| 1 | 67 % | Muy buena | `town_util.tl:983-985` |
| 2 | 33 % | Mediocre | `town_util.tl:983-985` |
| 3 | 0 % | Muy baja: la localidad deja de crecer | `town_util.tl:607-633` |

- Mientras dura el corte, la penalización también se escribe en la puntuación guardada, paso a paso, durante 3 meses (`towns.script.tl:137-145`). Tras reparar la carretera, esa parte guardada solo vuelve a la velocidad normal de recuperación: un corte largo sigue costando reputación un tiempo.
- 67 % está justo en el límite de Muy buena: cualquier otra pequeña pérdida baja la localidad a Buena.

```tip scripts
**Construye la carretera nueva antes de quitar la vieja.** Cada conexión principal cortada cuesta un tercio de la reputación de golpe, y cuanto más dura el corte, más tarda en volver.
```

## Cómo vuelve

- **Sola**: un nivel (1/6) cada 3 meses de tiempo de juego (360 s), cada mes (120 s) durante una campaña de marketing (`towns.script.tl:121-135`). A velocidad de calendario ×1 son unos **67 %** al año, **200 %** con campaña: de 0 % al máximo en 1,5 años aproximadamente. La ventana de la localidad muestra **Recuperación anual** 33 % y 100 %: textos fijos, la mitad de la velocidad real (`town_react_util.tl:1066`). Medido en una localidad de prueba: un nivel cada 358 s, cada 120 s con campaña.
- La recuperación reparte la ganancia entre todos los motivos; nunca supera las conexiones cortadas que siguen abiertas (`town_util.tl:1649-1687`).
- Las **celebraciones** añaden **+50 %** por el primer pasajero que sube a una de tus líneas en una localidad, +50 % por la primera carga entregada a una localidad, +50 % en cada subida de nivel de la localidad, y +20 % a la localidad más cercana por la primera carga entregada a cada industria (`celebrations.script.tl:181-273`). El mensaje termina entonces con **Ha mejorado la reputación del asentamiento.** o **Reputación mejorada en …** (`celebration_react_util.tl:63-75`). Solo cuentan si la reputación está por debajo de lo que permiten las conexiones principales cortadas (completa menos 1/3 por conexión cortada) y el ajuste Reputación está en Sí, y no en las misiones de campaña (`celebrations.script.tl:79-93`, `celebrations.script.tl:140-142`).
- **Suministrar a localidad** da al aceptar un adelanto en efectivo o de +5 % a +20 % × el factor de riesgo, elegido al azar (`deliver_cargo_town.script.tl:197-200`, `deliver_cargo_town.script.tl:220-222`). Como toda ganancia, solo quita pérdidas existentes (`towns.script.tl:324-330`).

## Campaña de marketing

| Qué | Valor | Fuente |
|---|---|---|
| Precio | 10 M × factor de año: 4 M en 1900 hasta 25 M en 2020, redondeado a 1 M | `marketing_campaign_tool.script.tl:9-14` |
| Requiere | un permiso de las ventajas de la empresa | `marketing_campaign_tool.script.tl:83-95`, `company.script.tl:416-423` |
| Duración | un año | `marketing_campaign_tool.script.tl:136` |
| Reputación | recuperación ×3 (≈ 200 % al año, la ventana muestra 100 %); **ninguna** ganancia inmediata | `towns.script.tl:126`, `town_util.tl:915-925` |
| Vecinos | tus líneas en esa localidad cuentan como la mitad de costosas cuando los vecinos eligen cómo viajar | `marketing_campaign_tool.script.tl:137`, `towns.script.tl:376-398` |

```engine
El script cuenta 360 segundos de tiempo de juego por nivel (120 con campaña), con un mes de 30 días de 4 segundos. La recuperación sigue el tiempo de juego: con un calendario más lento, un año del calendario dura más, así que vuelve más por año mostrado. Cuánto atrae a los vecinos hacia tus líneas el coste de línea a la mitad lo decide la elección de ruta del motor.
```

## Bueno saber

- Mira la ayuda emergente al construir: si muestra **Reputación: −x %**, un túnel o un trazado más suave suele costar menos que la reputación.
- No dejes nunca cortada una carretera principal entre dos localidades: cada una es −33 % al instante, y tres cortes detienen la localidad.
- Una campaña de marketing con la reputación completa solo ayuda a tus líneas, no a la calificación. Lánzala justo después de grandes obras, cuando la recuperación tiene algo que recuperar.
- La bonificación **Recuperación de la reputación** del módulo grande de la sede central (+1 %) aparece en la pestaña Bonificaciones, pero en los scripts solo cambia un valor que ninguna calificación lee (`hq_module_l.module.lua:171`, `towns.script.tl:157`, `town_util.tl:829`, `town_util.tl:857`).
- El logro **Yo no he sido** pide una localidad cuya reputación baje de 1 % (`achievements.script.tl:261-267`).

```check
official: "Reputation reflects how the town and surrounding nature are treated. Landscaping, removing town buildings and breaking main connections to other towns can lower it, while celebrations and marketing campaigns can improve it. Reputation lost by removing trees can be recovered by planting new ones." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Las mismas causas, más rocas eliminadas, túneles, el terreno de vías y carreteras y las subvenciones fallidas. Cada conexión principal cortada o demasiado larga cuesta 1/3 al instante; tres detienen la localidad. La recuperación es de unos 67 % al año sola y de unos 200 % con una campaña de marketing, el doble de lo que muestra la ventana (33 % y 100 %); la campaña no da nada al instante. Plantar árboles solo anula la pérdida por árboles. La bonificación Recuperación de la reputación de la sede central no tiene efecto en los scripts.
result: differs
```
