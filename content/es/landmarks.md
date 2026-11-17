---
title: Monumentos, celebraciones y elementos divertidos
summary: Lo que cuesta cada monumento en carga, cuándo se desbloquea y qué aporta a los vehículos de su localidad, cómo lo escala el ajuste Recursos necesarios para los monumentos, y qué hacen de verdad las celebraciones, los fuegos artificiales, los dirigibles y los ovnis.
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 9 | monumentos, uno por rango de empresa del 2 al 15
fact: +20 % / -20 % / +25 % | velocidad máxima, contaminación o comodidad para los vehículos de su localidad
fact: ×0 a ×4 | de carga necesaria, con el ajuste Recursos necesarios para los monumentos
fact: 2-4 años | entre dos ovnis
---

Un monumento se construye como una obra: lo desbloqueas con un rango de empresa, lo colocas y luego le **entregas carga**. Cuando la obra tiene toda su carga, el monumento está terminado y da una bonificación a los vehículos de **su localidad**. La sede central es un edificio aparte con sus propias reglas (ver [Rango de la empresa, ventajas y sede central](company.html)).

## Los monumentos

Carga con **Recursos necesarios para los monumentos** ×1 (Normal).

| Monumento | Rango | Carga que entregar | Bonificación para los vehículos de su localidad | Fuente |
|---|---|---|---|---|
| **Anfiteatro** | 2 | 800 piedra | vehículos de carretera: ruido **-25 %** | `arena.con.lua:10`, `arena.con.lua:20-26`, `arena.con.lua:39` |
| **Gran faro** | 5 | 1.200 piedra, 200 combustible | barcos: velocidad máxima **+20 %** | `lighthouse.con.lua:10`, `lighthouse.con.lua:14`, `lighthouse.con.lua:29`, `lighthouse.con.lua:48` |
| **Castillo de Himeji** | 7 | 1.200 piedra, 400 tablones | trenes: contaminación **-20 %** | `white_heron_castle.con.lua:10`, `white_heron_castle.con.lua:14`, `white_heron_castle.con.lua:28`, `white_heron_castle.con.lua:47` |
| **Barco museo** | 9 | 600 troncos, 600 tablones, 200 tejido | barcos: comodidad **+25 %** | `ship_museum.con.lua:10-18`, `ship_museum.con.lua:36`, `ship_museum.con.lua:55` |
| **Castillo de Neuschwanstein** | 10 | 1.000 piedra, 600 tablones, 200 tintes | vehículos de carretera: comodidad **+25 %** | `neuschwanstein.con.lua:10-18`, `neuschwanstein.con.lua:36`, `neuschwanstein.con.lua:55` |
| **Estatua de la Libertad** | 11 | 800 piedra, 400 acero, 400 lámina de metal | barcos: contaminación **-20 %** | `statue_of_liberty.con.lua:10-18`, `statue_of_liberty.con.lua:38`, `statue_of_liberty.con.lua:57` |
| **Palacio de Verano** | 13 | 600 piedra, 300 tablones, 300 tintes, 300 muebles | aviones: contaminación **-20 %** | `summer_palace.con.lua:10-22`, `summer_palace.con.lua:44`, `summer_palace.con.lua:63` |
| **Teatro de ópera** | 14 | 800 piedra, 400 vidrio, 400 lámina de metal, 400 tejido | trenes: comodidad **+25 %** | `opera_house.con.lua:10-22`, `opera_house.con.lua:44`, `opera_house.con.lua:63` |
| **Palacio de Westminster** | 15 | 800 piedra, 400 tablones, 400 vidrio, 400 muebles | vehículos de carretera, trenes, barcos y aviones: velocidad máxima **+20 %** | `westminster.con.lua:10-22`, `westminster.con.lua:45`, `westminster.con.lua:79` |

- Cada monumento se desbloquea una sola vez, por su rango; cómo sube el rango está en [Rango de la empresa, ventajas y sede central](company.html).
- Según sus archivos, los monumentos no cuestan nada al construirlos ni cada año: solo la carga (`arena.con.lua:59-64`).
- La obra almacena la mitad de cada carga a la vez, así que necesita al menos dos entregas de cada una (`arena.con.lua:13-18`).

## Construir un monumento

- La obra tiene **4 fases**. Avanza a medida que llega la carga: fase 2 con un tercio de toda la carga, fase 3 con dos tercios, terminado al 100 %. Cada carga solo cuenta hasta su propia cantidad, así que la piedra de más no compensa los tablones que faltan (`landmarks.script.tl:34-46`).
- La bonificación solo funciona cuando el monumento está **terminado** (`landmark_util_serialized.tl:393-395`). Entonces aparece el mensaje «Construcción terminada» (`landmarks.script.tl:49-61`).
- El ajuste **Recursos necesarios para los monumentos** multiplica toda la carga: Ninguno ×0, Bajo ×0,5, Normal ×1, Alto ×2 o Muy alto ×4. Los niveles son Fácil ×0,5, Normal ×1, Difícil ×2, Muy difícil ×4. Con ×0 un monumento queda terminado en cuanto se coloca (`difficulty_util.tl:40`, `difficulty_util.tl:107`, `difficulty_util.tl:135`, `difficulty_util.tl:162`, `difficulty_util.tl:189`, `landmarks.script.tl:38`, `landmarks.script.tl:46`).

## Quién recibe la bonificación

- La bonificación va a la localidad **más cercana al monumento**, y a los vehículos del medio de transporte indicado cuya localidad más cercana es esa (`landmark_util.tl:6-47`, `landmarks.script.tl:208-236`).
- Cuando un vehículo entra en la zona de otra localidad, toma las bonificaciones de esa localidad y pierde las anteriores (`landmarks.script.tl:279-299`).
- Las bonificaciones de varios monumentos en la misma localidad **se suman**: dos +20 % de velocidad máxima dan +40 % (`landmark_util.tl:46`, `vehicle_modifier.script.tl:3-16`).

```engine
Qué localidad es la «localidad más cercana» de un monumento o de un vehículo en marcha lo decide el motor (getConstructionClosestTown, closestTown). Cómo convierte el motor +25 % de comodidad o +20 % de velocidad máxima en viajes e ingresos también es cosa del motor.
```

```tip scripts
Pon el Palacio de Westminster en la localidad donde circulan la mayoría de tus vehículos: +20 % de velocidad máxima para todos los medios de transporte. Otro +20 % lo da el Gran faro para los barcos de la misma localidad. El logro Centralizado pide 10 monumentos terminados con la misma localidad más cercana, mientras que los archivos del juego contienen 9 monumentos además de la sede central (contada); no se sabe si puede conseguirse en esta versión (ver [Logros](achievements.html)).
```

## Celebraciones

Una celebración es la pequeña fiesta que aparece sobre una localidad cuando algo ocurre por primera vez. También sube la **Reputación** de la localidad, pero solo cuando la Reputación no está ya llena.

| Evento | Reputación | Fuente |
|---|---|---|
| el primer pasajero sube a una de tus líneas en la localidad | +50 % | `celebrations.script.tl:228-252` |
| la primera carga entregada a la localidad | +50 % | `celebrations.script.tl:187-198` |
| la localidad sube de nivel | +50 % | `celebrations.script.tl:260-272` |
| la primera carga entregada a una industria | +20 % para la localidad más cercana | `celebrations.script.tl:202-219` |

- Una localidad que sube de nivel también tiene **fuegos artificiales**, salvo que estén desactivados (`town_growth.script.tl:108-112`).
- Cómo funciona la Reputación: [Reputación](reputation.html).

## Elementos divertidos

- Un **dirigible** sobrevuela una localidad cuando inicias allí una Campaña de marketing (`fun_elements.script.tl:112-117`).
- Un **ovni** aparece cada **2 a 4 años** de tiempo de juego, elegido al azar, cuando no hay ninguno en el mapa (`fun_elements.script.tl:10`, `fun_elements.script.tl:79-91`). Haz clic en él para el logro Encuentros en la tercera fase.
- Ninguno de ellos cambia la economía.

## Conviene saber

- Elige la localidad antes de construir: la bonificación no sigue a tus líneas, solo a los vehículos cerca de esa localidad.
- En Muy difícil un monumento necesita cuatro veces la carga: el Palacio de Westminster pide entonces 3.200 de piedra y 1.600 de cada una de las otras cargas.

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: Nueve monumentos, uno por rango del 2 al 15, cada uno construido con carga entregada en 4 fases, escalada por Recursos necesarios para los monumentos ×0 a ×4. Una vez terminado, cada uno da una bonificación (+20 % de velocidad máxima, -20 % de contaminación, -25 % de ruido o +25 % de comodidad) a los vehículos de un medio de transporte en su localidad más cercana; las bonificaciones se suman. Las celebraciones añaden 50 % o 20 % de Reputación; un ovni llega cada 2 a 4 años.
result: adds
```
