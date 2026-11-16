---
title: Ajustes de salida: capacidad máxima, nivel de llenado y tiempos de parada
summary: Cuándo sale un vehículo de una parada: los tres modos de salida, el nivel de llenado de cada cargamento y los tiempos de parada mínimo, máximo y adicional.
domain: stations
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-15
fact: 600 s | tiempo de parada máx. por defecto de una parada nueva
fact: 30 s / 60 s | espera adicional máxima por defecto, carretera / ferrocarril
fact: 0–100 % | nivel de llenado, por cargamento, de la capacidad del vehículo
---

Cada parada de una línea tiene sus propios ajustes de salida, en la ventana "Filtro de cargamento" de la parada (haz clic en la parada en la ventana de la línea). Deciden **cuánto** carga allí el vehículo y **cuánto tiempo** puede esperar.

## Los ajustes

| Ajuste | Valores | Parada nueva | Fuente |
|---|---|---|---|
| "Cargar si hay disponibilidad", "Capacidad máxima (cualquiera)", "Capacidad máxima (todo)" | uno de los tres | Cargar si hay disponibilidad (medido) | `cargofilter_window.tl:798-821` |
| "Tiempo de parada mín." | 0–600 s, de 10 en 10 | 0 s (medido) | `cargofilter_window.tl:841-845` |
| "Tiempo de parada máx." | 0–600 s, o "---" (sin límite, control deslizante al final) | **600 s** (medido) | `cargofilter_window.tl:855-863` |
| "Espera adicional máxima" | 0–600 s, de 10 en 10 | 60 s; 30 s en una estación de carretera o de tranvía sin ferrocarril | `cargofilter_window.tl:827-831`, `line_util.tl:478-490` |
| "Cubrir nivel", por cargamento cargado | 0–100 %, de 1 en 1 | 100 % | `cargofilter_window.tl:698-704`, `line_util.tl:472` |

- Al hacer clic en un tiempo se abre una casilla numérica: allí se pueden escribir valores por encima de 600 s (`cargofilter_window.tl:204-208`).
- Los tres tiempos se mantienen en orden: subir el mínimo o la espera adicional por encima del máximo también sube el máximo (`cargofilter_window.tl:834-835`, `cargofilter_window.tl:848-849`, `cargofilter_window.tl:865-869`).
- Cambiar cualquiera de ellos marca la línea como personalizada: la configuración automática ya no toca sus listas Carga (`cargofilter_window.tl:438`, ver [Velocidad de carga y descarga](loading.html)). La configuración automática en sí nunca cambia el modo ni los tiempos (`line_util.tl:495-513`).

## Nivel de llenado: un tope por cargamento

El nivel de llenado es lo máximo de ese cargamento que el vehículo toma en esta parada, como proporción de la capacidad del vehículo, redondeado a la unidad más cercana (medido en el juego).

| Vehículo | Nivel de llenado | Sale con |
|---|---|---|
| camión, 15 plazas, troncos | 50 % | **8** (7,5 redondeado hacia arriba) |
| camión, 22 plazas, tejido | 70 % | **15** cada vez (15,4) |
| tren, 18 plazas, vidrio | 48 % | como mucho **9** (8,64) |
| tranvía, 28 plazas, combustible | 66 % | como mucho **18** (18,48) |

- El cargamento que ya va a bordo cuenta: un tranvía que llegó con 14 de combustible salió con 18, no con 14 + 18.
- Por encima del tope no se carga nada **y no se descarga nada** por su causa: un camión que llegó con 22 de fertilizante (tope 11) salió con 22.
- **0 %** significa: no cargar aquí este cargamento.
- Con un modo de capacidad máxima, el tope cuenta como lleno: camiones de troncos con un nivel de llenado del 50 % esperaron unos 270 s y salieron con 8 de 15, no con 15.
- No hay porcentaje de descarga. La descarga la deciden la lista Carga y "Forzar la descarga de todo el cargamento al llegar" ([Velocidad de carga y descarga](loading.html)).

## Capacidad máxima y los tiempos de parada

- **Cargar si hay disponibilidad**: el vehículo toma lo que hay y sale.
- **Capacidad máxima (todo)**: el vehículo espera hasta estar lleno. Camiones de troncos esperaron 460–566 s y salieron con 15 de 15.
- **Capacidad máxima (cualquiera)**: el vehículo sale cuando un cargamento está lleno. Un tren de troncos y tablones salió con 143 y 144 troncos tras 369–380 s; otras dos salidas tras unos 30 s con 57 y 118 troncos no tienen explicación.
- **Tiempo de parada máx.** termina la espera, aunque no se haya cargado nada. Un tren de vegetales en Capacidad máxima (todo) con un máximo de 120 s o bien se llenó (64 de 64) en unos 25 s, o bien salió tras 116–120 s con 26 o **0**. Con los 600 s por defecto salió con 26 de 64 tras 596–600 s.
- **Tiempo de parada mín.** es la parada entera, carga incluida, no tiempo extra después: con 60 s, los trenes de vidrio pararon 55–61 s cada vez, cargaran lo que cargaran.
- **Espera adicional máxima**: "Maximum wait time after loading to improve vehicle distribution" (`cargofilter_window.tl:828`). La ventana del vehículo muestra "Garantizando una distancia segura" mientras espera (`entity_window_util.tl:2279-2286`).
- **Varios vehículos en una misma parada cargan a la vez**, llegara cuando llegara cada uno (visto en el juego). Dos camiones de troncos que llegaron con unos 90 s de diferencia salieron en el mismo segundo, cada uno con 8. No se midió cómo se reparte el cargamento entre ellos.

```engine
Los scripts solo guardan los ajustes; cuándo sale un vehículo lo decide el motor.
```

Las reglas anteriores se midieron con la base de datos de [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) (capturas cada 2 s, así que los tiempos de parada son ±2 s), noviembre de 2026.

## Conviene saber

- Una espera larga con capacidad máxima en una parada donde llega poco cargamento bloquea el andén: los demás vehículos de la línea hacen cola detrás.
- Un tiempo de parada máx. corto con capacidad máxima puede hacer salir vehículos vacíos si vuelven antes de que haya cargamento nuevo.
- Una vez, un tren en Capacidad máxima (todo) paró 783–992 s con un máximo de 600 s. No se encontró la causa.

```check
official: "Full load (any): The vehicle will stop and wait until one cargo type is fully loaded. Full load (all): The vehicle will stop and wait until it is fully loaded." "In the vanilla game "all" and "any" only applies to trains and ships […] Any other vehicle type will wait for full load in both cases." Cada cargamento se carga "to what percentage of a vehicle's total capacity". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles#departure_configuration))
scripts: Tres modos de salida, tiempo de parada mín. / máx. 0–600 s (o sin límite), espera adicional máxima 0–600 s (60 s, 30 s carretera), nivel de llenado 0–100 % por cargamento; medido: el nivel de llenado limita el cargamento a bordo, redondeado a la unidad más cercana, y cuenta como lleno para la capacidad máxima; el tiempo de parada máx. termina una carga completa, aunque esté vacío; el tiempo de parada mín. incluye la carga; los vehículos de una misma parada cargan juntos.
result: refines
```
