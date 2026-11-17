---
title: Notificaciones y avisos
summary: Cuándo aparece cada aviso y cuándo desaparece: vehículos atascados, estaciones no utilizables o abarrotadas, problemas de líneas y paradas, calificaciones de las localidades, condición de los vehículos, industrias que cierran, y qué avisos están ocultos en el registro por defecto.
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 5 min | de tiempo de juego parado antes de que un vehículo se dé por atascado
fact: 20 % | de condición que activa el aviso, hasta que el vehículo vuelve a superar el 30 %
fact: 11 | tipos de notificación desactivados en una partida nueva
fact: 75 días | entre dos comprobaciones de estaciones sin conexión de carretera
---

La mayoría de los avisos son **persistentes**: un script del juego comprueba la situación una y otra vez, el aviso se mantiene mientras el problema exista y termina solo cuando se resuelve. Las comprobaciones se reparten por turnos en 4 actualizaciones, así que un aviso puede tardar un momento en aparecer o desaparecer (`notifications.script.tl:13`, `notifications.script.tl:49`).

## Cuándo aparece cada aviso

| Aviso | Aparece cuando | Desaparece cuando | Fuente |
|---|---|---|---|
| **Vehículo atascado** | uno de tus vehículos está en camino, no lo has detenido tú, y lleva **5 minutos** de tiempo de juego a velocidad 0 | vuelve a moverse | `notifications.script.tl:557-580` |
| **Estación no operativa** | ningún terminal de la estación carga ni descarga pasajeros y **nada** está en su área de influencia (ni almacén, ni industria, ni edificio de la localidad), mientras una de tus líneas para allí | algo entra en el área de influencia | `notifications.script.tl:602-617`, `notifications.script.tl:630-647`, `station_useless.script.tl:39` |
| **Estación abarrotada** | la estación tiene más pasajeros o cargamento esperando de lo que admite (desbordamiento), mientras una de tus líneas para allí; los pasajeros se van | el desbordamiento termina | `notifications.script.tl:599`, `notifications.script.tl:649-661`, `overcrowding.script.tl:23` |
| **Condición del vehículo** | un vehículo tuyo está al **20 %** de condición o menos | vuelve a superar el **30 %** | `notifications.script.tl:310-318` |
| **Calificación de localidad muy baja** | una de las calificaciones de la localidad cae a Muy baja (menos de 1/6) | la calificación vuelve a Mediocre o mejor | `notifications.script.tl:230-238`, `town_util.tl:763-769`, `town_util.tl:983-985` |
| **Calificación de localidad en declive** | una calificación está en Baja o Mediocre (menos del 50 %) sin estar en el aviso de Muy baja | la calificación es Buena o mejor | `notifications.script.tl:240-248` |
| **Cierre de industria** | una industria empieza su cuenta atrás de cierre | cierra, o se vuelve a usar a tiempo | `notifications.script.tl:439-451`, `industry_close.script.tl:53-59` |
| **Sin conexión de carretera** | una estación no está conectada a una carretera; se comprueba cada **75 días** | la siguiente comprobación encuentra una carretera | `notifications.script.tl:16`, `notifications.script.tl:423-436` |
| **Problema de descarga de cargamento** | el cargamento de un vehículo nunca se descarga en su línea | se descarga | `notifications.script.tl:277-290`, `cargo_rtc_warning.script.tl:28-37` |

- Un vehículo **en el depósito** nunca cuenta como atascado: esa comprobación está desactivada en el script (`notifications.script.tl:563-564`). Un vehículo que has detenido tampoco cuenta nunca.
- La comprobación de Estación no operativa solo mira el área de influencia. Una estación que ya tiene pasajeros subiendo o bajando en un terminal nunca se señala (`notifications.script.tl:606-610`).
- Cómo subir una calificación de localidad: [Crecimiento de las localidades](towns.html) y [Reputación](reputation.html). Cómo funciona la cuenta atrás de cierre y cómo pararla: [Industrias](industries.html). Lo que la condición le hace a un vehículo: [Costes, mantenimiento y préstamos](costs.html).

```engine
Si una estación se desborda, si un vehículo tiene ruta, si una línea puede llegar a sus estaciones y cuánto puede durar el viaje entre dos localidades lo determina el motor (calculateStationGroupCargo, getVehicleProblems, getLineProblems, getTownProblems). Los scripts solo convierten sus respuestas en avisos.
```

```tip scripts
Vehículo atascado, Problema de vehículo, Condición del vehículo, Estación abarrotada y Estación no utilizable están desactivados en el registro de una partida nueva. Actívalos en los ajustes de notificaciones: son los avisos que te informan de un atasco, una ruta que falta o una flota desgastada.
```

## Problemas de líneas, paradas y vehículos

Vienen directamente de las comprobaciones del motor sobre tus líneas y vehículos; el script da un título a cada uno.

| Aviso | Casos | Fuente |
|---|---|---|
| **Problema de línea** | muy pocas estaciones; una estación dos veces seguidas; estaciones incompatibles entre sí; no se pudieron conectar estaciones; no se pudieron conectar terminales alternativos | `line_warning.script.tl:46-128` |
| **La línea está mal configurada** | un tipo de cargamento que no se puede cargar en ningún sitio, o descargar en ningún sitio; ningún vehículo puede llevar un cargamento configurado para cargarse; vehículos que no llevan ninguno de los cargamentos configurados, o vehículos solo de carga en una línea de pasajeros; ningún cargamento configurado | `line_warning.script.tl:15-36`, `line_warning.script.tl:133` |
| **Problema de estación** | una parada que los vehículos actuales no pueden usar; una parada de pasajeros usada por vehículos de carga (uno o todos); una parada de carga usada por vehículos de pasajeros; un tipo de cargamento configurado que no se puede cargar o descargar en esa parada | `line_station_warning.script.tl:6-87` |
| **Problema de vehículo** | no hay ruta electrificada; no hay ruta para aviones grandes; no hay ruta para barcos grandes; no hay ninguna ruta; dos trenes que se bloquean entre sí | `vehicle_warning.script.tl:6-58` |
| **La ciudad no está conectada** | la carretera entre dos localidades está cortada; el viaje entre dos localidades dura demasiado | `town_warning.script.tl:7-19` |

- «No hay ruta para aviones grandes» y «No hay ruta para barcos grandes» significan que el vehículo es demasiado grande para una pista, un muelle o una vía navegable de su línea: consulta [Aviones](aircraft.html) y [Barcos](ships.html).

## Registro, ventanas emergentes y ajustes

- Cada tipo de aviso se puede desactivar en los ajustes de notificaciones («Configurar el registro de notificaciones»). Un tipo desactivado no muestra ventana emergente y no se guarda en el registro (`notification_util.tl:145-146`, `notification_log.tl:480`).
- En una **partida nueva**, 11 tipos están desactivados desde el principio: **Vehículo atascado**, **Problema de vehículo**, **Condición del vehículo**, **Estación abarrotada**, **Estación no utilizable**, **Estación no conectada**, **La ciudad no está conectada**, **Cargamento sin descargar**, y los mensajes de progreso de Prospección, Campaña de marketing y Ecologización industrial de la empresa (`stuck_vehicle.res.lua:7`, `vehicle_warning.res.lua:8`, `noroadconnection.res.lua:8`, `vehiclecondition.res.lua:8`, `overcrowding.res.lua:8`, `station_useless.res.lua:7`, `town_warning.res.lua:8`, `cargo_rtc_warning.res.lua:8`, `notification_util.tl:32-39`).
- Los mensajes puntuales (vehículo nuevo, construcción nueva, subida de rango, subvenciones) ocultan su ventana emergente tras **60 segundos** de tiempo de juego; se quedan en el historial (`notification_util.tl:10`, `notifications.script.tl:85-94`).
- Una notificación también termina cuando todo lo que señala se ha eliminado o reconstruido (`notifications.script.tl:95-107`).
- En una misión las notificaciones empiezan en pausa, hasta que la misión las activa (`notifications.script.tl:700-704`).

## Conviene saber

- Un aviso de atasco tras 5 minutos no dice por qué. Mira el vehículo: una señal en rojo, una señal de sentido único al revés, o un aviso Problema de vehículo para el mismo vehículo.
- «Estación no operativa» solo significa «todavía nada en el área de influencia». Acerca la estación a las casas, a una industria o a un almacén, o amplíala.
- Una estación abarrotada pierde pasajeros: añade vehículos o acorta el intervalo (consulta [Salida y espera](departure.html)).

```check
official: La página User Interface de la wiki oficial describe el botón de notificaciones, el registro y sus filtros, sin las condiciones de cada aviso. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: Las condiciones de arriba: atascado tras 5 minutos a velocidad 0 en camino, condición del vehículo al 20 % hasta el 30 %, calificación de localidad Muy baja por debajo de 1/6, conexión de carretera comprobada cada 75 días, 11 tipos desactivados por defecto.
result: adds
```
