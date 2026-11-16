---
title: Barcos y puertos
summary: Barcos pequeños y grandes, qué puerto admite cuál, terminales y costes de los puertos, y la lista de todos los barcos con su cargamento, capacidad y velocidad.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
game: 40425
fact: 2 | tamaños de barco: pequeño y grande
fact: 1, 2, 4 | terminales por puerto
fact: 27 | barcos en el juego base
fact: ×9 | precio y conservación de la variante de puerto de 1990
---

Cada barco es **pequeño** o **grande**. Un barco grande solo puede atracar en un **puerto grande**; un barco pequeño atraca en ambos. La guía del juego también lo dice: «Cabe destacar que los barcos grandes solo pueden atracar en puertos grandes.»

```diagram ship_access
```

## Puertos pequeños y grandes

- Dos puertos en el menú de construcción: **Puerto de carga/pasajeros pequeño** y **Puerto de carga/pasajeros grande**. Ambos admiten pasajeros y todo el cargamento (`harbor_modular.tl:92`, `harbor_modular.tl:122`).
- El puerto pequeño se construye con muelles pequeños, que solo admiten barcos pequeños (`small_pier.module.lua:7`). El puerto grande usa muelles medianos, que admiten ambos tamaños (`medium_pier.module.lua:6`, `harbor_modular.script.lua:35-39`).
- **Terminales**: 1, 2 o 4, a elegir al construir (`harbor_modular.tl:16`, `harbor_modular.script.lua:33`).
- Una terminal de muelle admite 100 pasajeros en espera en un muelle pequeño y 50 en un muelle mediano (`modules.script.lua:872`, `modules.script.lua:1004`).
- Los puertos deben colocarse a lo largo de una costa, en agua navegable (`harbor_modular.tl:29`).
- Cada barco fija su propio tamaño en su archivo de vehículo; el juego lo convierte en el modo de barco pequeño o grande (`model_metadata_util.lua:1411-1412`).

## Costes

Hay una variante de puerto por época: 1900, 1950 y 1990 (`harbor_modular.tl:71-73`). El precio y la conservación se multiplican por 3 para una variante desde 1940 y por 9 para una desde 1980 (`harbor_modular.tl:76`):

| Puerto | Precio (primera variante) | Conservación por año (primera variante) | Fuente |
|---|---|---|---|
| Puerto pequeño | 144.000 - 444.000 | 24.000 - 74.000 | `harbor_modular.tl:88-89` |
| Puerto grande | 228.000 - 678.000 | 38.000 - 113.000 | `harbor_modular.tl:118-119` |

- Los dos valores son la disposición más pequeña y la más grande.
- La conservación de los puertos también sigue el año del calendario, ×1 en 1900 hasta ×6 en 2020, como almacenes y aeropuertos ([Costes, conservación y préstamos](costs.html)).
- Los puertos son ruidosos y contaminantes: de 180 a 280 para ambos ([Contaminación y ruido](emission.html)).
- El precio y los costes de funcionamiento de un barco se calculan a partir de su velocidad y su capacidad, como los vehículos de carretera y los aviones ([Costes, conservación y préstamos](costs.html)).

## Todos los barcos

Velocidad en km/h, redondeada. «Cargamento» enumera las clases de cargamento del archivo de vehículo; «cualquier cargamento» significa todos los tipos de cargamento. La capacidad es el total que muestra la tienda de vehículos: la suma de los compartimentos, cada uno con su mayor configuración de carga (`vehicle_store_util.tl:70-95`).

| Barco | Años | Tamaño | Cargamento | Capacidad | Velocidad | Velocidad de carga |
|---|---|---|---|---|---|---|
| Dunara Castle | 1875-1930 | grande | pasajeros, cualquier cargamento | **160** (2 × 80) | 20 | 20 |
| Arrastrero canadiense | 1884-1948 | pequeño | cualquier cargamento | 40 | 35 | 10 |
| Waimarie | 1889-1940 | pequeño | pasajeros | 80 | 30 | 15 |
| Sydfart | 1900-1930 | pequeño | líquidos, de plataforma, mercancías, a granel | 80 | 30 | 20 |
| PS Trillium | 1910-1955 | grande | pasajeros | 200 | 35 | 15 |
| Barco de vapor de ruedas | 1915-1960 | pequeño | pasajeros, cualquier cargamento | **120** (2 × 60) | 40 | 10 |
| Terra Nova | 1925-1975 | grande | a granel, de plataforma, mercancías | **200** (2 × 100) | 45 | 30 |
| Remolcador petrolero Votrans | 1935-1990 | pequeño | líquidos | 120 | 33 | 20 |
| Remolcador de cargamento Votrans | 1935-1990 | pequeño | a granel, de plataforma, mercancías | 120 | 33 | 20 |
| MS Stadt Kiel | 1943-1990 | pequeño | pasajeros | 80 | 30 | 20 |
| Borealis | 1948-1994 | pequeño | cualquier cargamento | 60 | 38 | 20 |
| Wopper | 1950-2005 | pequeño | líquidos, de plataforma, mercancías, a granel | 160 | 30 | 25 |
| Ferri Meridian | 1956-2011 | pequeño | pasajeros | 240 | 30 | 15 |
| Cap Arkona | 1965-2010 | grande | pasajeros | 200 | 40 | 20 |
| Barco costero Tora | 1970-2020 | grande | líquidos, de plataforma, mercancías, a granel | 320 | 40 | 25 |
| Aerodeslizador AP1-88 | 1980- | pequeño | pasajeros | 240 | 90 | 15 |
| Remolcador Hercules XI | 1990- | grande | de plataforma, mercancías, a granel | **240** (2 × 120) | 32 | 20 |
| Baltica | 1994- | pequeño | cualquier cargamento | 80 | 40 | 20 |
| HADAG tipo 2000 | 1995- | pequeño | pasajeros | 100 | 35 | 25 |
| Damen Tanker 800 | 1996- | pequeño | líquidos | **320** (2 × 160) | 28 | 30 |
| Damen Fast Ferry | 2003- | grande | pasajeros | 220 | 75 | 20 |
| Luise Deymann | 2013- | grande | líquidos | **480** (2 × 240) | 30 | 35 |
| MS Diamant | 2013- | grande | pasajeros | 280 | 45 | 35 |
| Remolcador Virgo | 2015- | grande | de plataforma, mercancías, a granel | **320** (2 × 160) | 40 | 15 |
| GHL Oita Hovercraft | 2023- | pequeño | pasajeros | 320 | 100 | 20 |
| Yara Birkeland | 2030- | grande | de plataforma, mercancías, a granel | 480 | 42 | 10 |
| Transbordador solar | 2035- | pequeño | pasajeros | 80 | 30 | 30 |

## Conviene saber

- **Comprueba el tamaño antes de construir un puerto pequeño.** Varios de los mayores buques de carga (Tora, Virgo, Yara Birkeland) son grandes y no atracarán allí.
- **«No hay ruta para barcos grandes»** es un aviso aparte para barcos grandes: el juego no encontró ninguna ruta por agua que pueda usar un barco grande. Qué agua está abierta a qué tamaño lo decide el motor del juego, no los scripts, que solo muestran el aviso (`vehicle_warning.script.tl:28-36`).
- **Los puntos de ruta de los barcos** deben colocarse en el agua («Los puntos de ruta de navegación deben estar en el agua.»).
- El depósito de barcos y la estación de mantenimiento de barcos son edificios distintos; el mantenimiento actúa en un radio a su alrededor ([Vehículos: condición, edad y velocidad de carga](vehicles.html)).

```check
official: "Passenger and cargo ships are available in two sizes: small and large. Large ships can only dock at large harbors, so make sure the harbor matches the size of the ships assigned to the line." (in-game guide "Water Infrastructure")
scripts: Igual: los muelles pequeños solo admiten SMALL_SHIP, los medianos SHIP y SMALL_SHIP; ambos puertos admiten pasajeros y todo el cargamento; 1, 2 o 4 terminales; tres variantes de época a ×1 / ×3 / ×9; 16 barcos pequeños y 11 grandes en el juego base.
result: refines
```
