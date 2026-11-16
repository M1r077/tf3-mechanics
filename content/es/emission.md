---
title: Contaminación y ruido
summary: Qué emite ruido y contaminación, cuándo un edificio emite más, cómo lo valoran las ciudades y qué hacen de verdad la Ecologización industrial y la Planta de limpieza.
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
fact: 65–80 dB | ruido en la ciudad: valoración completa a 65, cero a 80
fact: 60–74 | contaminación en la ciudad, en la escala logarítmica de los scripts (no es un nivel sonoro): valoración completa a 60, cero a 74
fact: −80 % | ruido y contaminación de una industria ecologizada
fact: 700 m | alcance de la Planta de limpieza
---

Vehículos, vías, calles, estaciones, cocheras, almacenes e industrias emiten **Ruido** y **Polución**. Dos valoraciones de la ciudad, **Ruido** y **Polución**, comparan lo que llega a la ciudad con límites fijos. Una mala baja la valoración de la **Autoridad municipal** y, con ella, el crecimiento (ver [Ciudades](towns.html)).

## Cuándo un edificio emite más

Un script del juego fija la emisión de cuatro tipos de edificios cada pocas actualizaciones, entre un nivel tranquilo y uno ajetreado (`emissions.script.tl:12-18`):

| Edificio | Emite más cuando | Fuente |
|---|---|---|
| **Industria** | produce, y más con cada impulso (carga o trabajadores); menos, hacia su nivel parado, cuando su existencia de salida está llena | `emissions.script.tl:152-194` |
| **Estación** | está más concurrida: personas y carga en espera frente a su capacidad | `emissions.script.tl:211-222` |
| **Cochera**, **estación de mantenimiento** | más vehículos usan su mantenimiento | `emissions.script.tl:223-234` |
| **Almacén** | sus existencias están más llenas | `emissions.script.tl:237-250` |

- Cada industria tiene sus propios cuatro niveles: parada, produciendo, impulsada una vez, impulsada dos veces (`industryutil.lua:464-475`; el valor por defecto 0 / 78 / 84 / 88 solo se aplica a una industria sin los suyos). La mayoría emite algo incluso parada: una mina de carbón pasa de 2 → 10 → 20 → 30 de contaminación, sus campos 2 → 30 → 60 → 90 (`coal_mine.con.lua:99-135`, ver [Industrias](industries.html)).
- Una industria cuya producción no se recoge vuelve hacia su nivel parado: darle servicio aumenta su contaminación.
- Vehículos y vías también emiten; un vehículo en mal estado emite más con el ajuste **Efecto del mantenimiento de vehículos** (ver [Costes, mantenimiento y préstamos](costs.html)).

## Lo que muestra el menú de construcción

| Edificio | Ruido | Contaminación | Fuente |
|---|---|---|---|
| Puerto | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| Aeropuerto | 8–56 | 80–560 | `airport.tl:28-29` |
| Estación de tren | 25 | 45–350 | `modular_station.con.lua:97-98` |
| Cochera ferroviaria | 50 | 100 | `rail_depot.con.lua:32-33` |
| Cochera de carretera y tranvía | 40 | 80 | `road_depot.con.lua:30-31`, `tram_depot.con.lua:32-33` |
| Estación subterránea | 40 | 80 | `underground_station.con.lua:75-76` |
| Estación de camiones y autobuses | 1–10 | 12–76 | `modular_terminal.con.lua:67-68` |
| Estaciones de mantenimiento | 20 | 40–50 | `road_maint_station.con.lua:30-31`, `rail_maint_station.con.lua:30-31` |
| Almacén | 20 | 50 (universal) o 100 (especializado) | `warehouses/warehouse.tl:51`, `warehouses/warehouse.tl:73-74` |

Dos valores son el rango que muestra el menú, del más bajo al más alto, como el rango de precio a su lado (`construction_desc_react_util.tl:733-746`); un valor es una cifra única. En funcionamiento, cada edificio emite más cuanto más ocupado está (tabla de arriba). Mantén puertos, aeropuertos y grandes estaciones de mercancías lejos de las casas.

## Cómo lo valora una ciudad

| Valoración | Medida | Valoración completa | Cero | Fuente |
|---|---|---|---|---|
| **Ruido** | ruido en los edificios de la ciudad | 65 dB o menos | 80 dB | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Polución** | polución media por celda de 16 m del área de la ciudad (área contada entre 5 y 10 km²), convertida a la escala logarítmica de los scripts («dB») | 60 o menos | 74 | `town_util.tl:413-431`, `emission_config.tl:23-30` |

- Solo el distrito **Residencial** sufre el ruido; los edificios comerciales e industriales no (wiki oficial). La ventana de una casa muestra el ruido en su posición (`town_building.tl:165-183`).
- La contaminación se promedia sobre toda el área: una fuente lejos del centro pesa menos en una ciudad grande que en una pequeña.
- Los ajustes **Susceptibilidad al ruido** y **Susceptibilidad a la polución** desplazan los límites: el doble de susceptibilidad cuenta como +3 dB (`town_util.tl:426-428`, `town_util.tl:439-441`). La polución usa la misma escala logarítmica que el ruido (10·log10): +3 «dB» significa el doble de polución. No es un nivel sonoro.

| Nivel | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Fuente |
|---|---|---|---|---|---|---|---|---|
| Ruido | No (siempre completa) | ×¼ | ×½ | ×1 | ×1,4 | ×1,8 | ×3,5 | `difficulty_util.tl:48` |
| Polución | No (siempre completa) | ×¼ | ×½ | ×1 | ×1,7 | ×3 | ×5 | `difficulty_util.tl:49` |

Los preajustes Fácil, Medio, Difícil y Muy difícil usan los niveles 3, 4, 5 y 6 (`difficulty_util.tl:114-115`, `difficulty_util.tl:142-143`, `difficulty_util.tl:169-170`, `difficulty_util.tl:196-197`).

## Ecologización industrial

| | | Fuente |
|---|---|---|
| Efecto | ruido y contaminación de la industria ×0,2 (−80 %), para siempre | `emission_config.tl:32`, `emissions.script.tl:184-192` |
| Usos | uno en el rango de empresa 3, 6, 9, 12 y 15 | `industry_greenify_tool.script.tl:99-104` |
| Límite | una vez por industria; un segundo intento no gasta permiso | `company.script.tl:489-494` |

- El efecto va ligado a esa versión de la industria: cuando la industria se reconstruye, se pierde (`emissions.script.tl:187-190`).
- Mejor uso: la industria más activa justo al lado de una ciudad, porque una industria impulsada es la que más emite.

## La Planta de limpieza

Una ventaja de empresa que elimina la contaminación a su alrededor.

| | | Fuente |
|---|---|---|
| Precio | 100.000.000 | `pollution_cleanup_facility.script.lua:560` |
| Mantenimiento por año | 10.000.000 | `pollution_cleanup_facility.script.lua:561` |
| Disponible | 15 en el rango de empresa 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Necesita | **Máquinas**: 8 por ciclo, dos ciclos al año; 20 trabajadores | `pollution_cleanup_facility.con.lua:43-60` |
| Alcance | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| Estado | Contaminación | Ruido | Fuente |
|---|---|---|---|
| parada (sin máquinas) | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| en marcha | −10.000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| impulsada una vez | −20.000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| impulsada dos veces | −40.000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

- Sin máquinas casi no hace nada: hay que abastecerla como a una industria.
- Es ruidosa: constrúyela fuera del distrito residencial, a menos de 700 m de la zona contaminada.
- Su factor de impulso por trabajadores es ×2 (`pollution_cleanup_facility.script.lua:549`). Ver [Trabajadores](workers.html).

## Conviene saber

- Abre la ventana de la ciudad o las capas de ruido y contaminación para ver la valoración y los puntos críticos.
- Una existencia de salida llena baja la emisión de una industria hacia su nivel parado, pero te cuesta su carga: mejor alejar la ciudad que dejar sin servicio a la industria.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) y [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) ayudan a encontrar las estaciones más concurridas.

```engine
El motor calcula los mapas de ruido y contaminación, cómo se propagan los valores, las emisiones de vehículos y vías, y cuándo se reconstruye una industria. El script solo fija el nivel de cada edificio y los límites de las ciudades.
```

```check
official: "Noise reflects noise levels in residential areas." "Pollution reflects pollution levels across the town area." El distrito residencial "is sensitive to noise"; el distrito comercial "is robust against the influence of noise". ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Valoración de ruido 65 → 80 dB, contaminación 60 → 74 dB promediada sobre 5–10 km²; la susceptibilidad suma 10·log10 dB; industrias, estaciones, cocheras y almacenes emiten más cuando están ocupados; una existencia de salida llena baja la emisión de una industria hacia su nivel parado; ecologización −80 % una vez por industria; la Planta de limpieza elimina hasta 40.000 de contaminación en 700 m y necesita máquinas.
result: refines
```
