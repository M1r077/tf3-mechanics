---
title: Logros
summary: Qué comprueba el script del juego para cada logro de la partida libre y cuándo, cuáles cuentan solo vehículos, carga y animales del juego base, y qué comprobaciones se dejan al motor.
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-17
game: 40425
fact: 17 | logros que desbloquea el propio script del juego
fact: 500 m | altura del primer vagón de un tren en una parada para Escala en la cima
fact: < 1 % | de Reputación de la localidad para Yo no he sido
fact: 10 | monumentos que deben tener la misma localidad más cercana para Centralizado
---

La wiki oficial lista 41 logros. El script del juego (`achievements.script.tl`) desbloquea **17** de ellos por sí mismo y alimenta **9 contadores entre partidas**; los demás (campaña, clima, tamaño de las localidades, almacén, intereses, potenciadores, coches, 1900-2000, vapor en los años 2000) se comprueban en otro sitio, en el motor o en la plataforma. Cada comprobación pregunta primero al motor si el logro aún puede desbloquearse; allí se decide si los mods o los ajustes lo bloquean (`achievements.script.tl:632`, `achievements.script.tl:510`).

## Logros comprobados por el script

| Logro | Qué comprueba el script | Fuente |
|---|---|---|
| **Paquete entregado** | una unidad de carga llega a su destino | `achievements.script.tl:221-225`, `achievements.script.tl:632-636` |
| **En nombre de...** | una subvención completada | `achievements.script.tl:241-244`, `achievements.script.tl:638-642` |
| **Racha de subvenciones** | 10 subvenciones completadas sin ninguna fallida entre ellas; una subvención fallida pone la cuenta a 0 | `achievements.script.tl:243-249`, `achievements.script.tl:644-648` |
| **Que no falte de nada** | la valoración de entregas de una localidad pasa a **Excelente** | `achievements.script.tl:270-276`, `towns.script.tl:30-33`, `achievements.script.tl:650-654` |
| **Desarrollo urbano** | una localidad sube de nivel | `achievements.script.tl:253-255`, `town_growth.script.tl:92` |
| **Demanda en aumento** | una localidad obtiene la demanda de un nuevo tipo de carga | `achievements.script.tl:257-259`, `achievements.script.tl:668-672` |
| **Yo no he sido** | la Reputación de una localidad **baja** por debajo del **1 %** | `achievements.script.tl:261-267`, `towns.script.tl:36-39` |
| **Ascenso** | la empresa sube un rango | `achievements.script.tl:280-282`, `achievements.script.tl:680-684` |
| **La cima del escalafón** | la empresa alcanza el rango más alto | `achievements.script.tl:284-290`, `achievements.script.tl:686-690` |
| **Paisajista** | colocas árboles, y solo árboles, en una construcción (nada retirado, no por reforestación) | `achievements.script.tl:346-377` |
| **Perfeccionista** | la misma estación se derriba, se reconstruye, se derriba y se reconstruye, en ese orden, sin que se construya o retire otra estación entre medias | `achievements.script.tl:304-341`, `achievements.script.tl:694-710` |
| **Centralizado** | exactamente 10 monumentos terminados tienen la misma localidad más cercana | `achievements.script.tl:382-395`, `achievements.script.tl:713-721` |
| **Escala en la cima** | uno de tus trenes llega a una parada con su primer vagón a más de **500 m** | `achievements.script.tl:407-417`, `achievements.script.tl:723-727` |
| **Alta mar** | uno de tus helicópteros llega a una parada de una plataforma petrolífera | `achievements.script.tl:420-450`, `achievements.script.tl:729-733` |
| **Flota patrimonial** | todos los modelos de barco del juego base circulan a la vez en tus líneas de barcos | `achievements.script.tl:735-776` |
| **Encuentros en la tercera fase** | haces clic en un ovni | `achievements.script.tl:793-806` |
| **Cronometrista** | cambias la hora del día a mano | `achievements.script.tl:839-844` |

- **Perfeccionista** solo cuenta una construcción que añade o retira una estación entera: añadir un andén o un módulo a una estación no cuenta (`achievements.script.tl:301-302`).
- **Centralizado** cuenta cada monumento cuando se termina, para la localidad más cercana en ese momento (`achievements.script.tl:386`).
- **Flota patrimonial** solo se comprueba cuando un modelo de barco que nunca ha parado llega a una parada; mira los vehículos de tus líneas de barcos, no los barcos en un depósito (`achievements.script.tl:736`, `achievements.script.tl:750-766`).
- **Yo no he sido** necesita la Reputación, no otra valoración: ver [Reputación de las localidades](reputation.html).

```tip scripts
Escala en la cima comprueba la altura del primer vagón cuando el tren se detiene, no la altura del edificio de la estación. Construye la estación en una montaña por encima de 500 m y haz que un tren llegue allí.
```

## Contadores entre partidas

Continúan de una partida a otra (la plataforma los guarda). El script solo envía lo que ha cambiado desde la última comprobación.

| Contador | Logro | Qué cuenta | Fuente |
|---|---|---|---|
| Longitud de vías | **Vuelta al mundo** | el aumento de la longitud total del registro (en km); no se resta nada al derribar | `achievements.script.tl:511-523` |
| Población | **Población global** | el aumento de la población del mapa, desde la población al cargar la partida | `achievements.script.tl:512`, `achievements.script.tl:525-533` |
| Pasajeros | **Líder de los pasajeros** | pasajeros que terminaron un viaje en una de tus líneas | `achievements.script.tl:236-238`, `achievements.script.tl:535-541` |
| Carga | **Líder del cargamento** | unidades de carga entregadas | `achievements.script.tl:543-549` |
| Climas | **Magnate de magnates** | el clima del mapa, cuando la empresa alcanza allí el rango más alto | `achievements.script.tl:551-567` |
| Ingresos | **Dinero por doquier** | tus ingresos sumados, en miles de millones | `achievements.script.tl:202-204`, `achievements.script.tl:569-590` |
| Tipos de carga | **Líder en ventas** | cada tipo de carga del juego base entregado una vez | `achievements.script.tl:20-22`, `achievements.script.tl:230-232`, `achievements.script.tl:592-607` |
| Vehículos | **Derroche de conocimiento** | cada modelo de vehículo del juego base que llega una vez a una parada | `achievements.script.tl:16-18`, `achievements.script.tl:469-481`, `achievements.script.tl:609-625` |
| Animales | **Amante de los animales** | cada animal del juego base en el que haces clic una vez | `achievements.script.tl:24-26`, `achievements.script.tl:809-834` |

- Los vehículos, la carga y los animales de mods nunca cuentan para estos contadores: solo se toman archivos del juego base (`::/vehicle`, `::/cargos`, `::/animal`) (`achievements.script.tl:16-26`).
- Para Derroche de conocimiento un vehículo debe **llegar a una parada** de una línea; comprarlo no basta.

```engine
Si un logro aún puede desbloquearse (isAchievementUnlockable), si los contadores están desactivados (areStatsDisabled), los objetivos de cada contador y los 24 logros que no están en el script los gestionan el motor y la plataforma. La wiki oficial dice que los logros en general no están disponibles con mods no cosméticos o con ajustes de juego distintos de los valores estándar.
```

## Conviene saber

- Cada logro de «primera vez» se comprueba respecto a la comprobación anterior: necesita un evento **nuevo** en una partida en la que el logro sigue abierto; una subvención o un rango antiguos de una partida guardada no cuentan otra vez (`achievements.script.tl:633`, `achievements.script.tl:779`).
- Tu rango, las subvenciones y la Reputación se explican en [Rango de la empresa, ventajas y sede central](company.html), [Subvenciones](subsidies.html) y [Reputación de las localidades](reputation.html).

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: 17 logros y 9 contadores están en el script. Precisa los textos oficiales: Que no falte de nada significa que la valoración de entregas llega a Excelente, Yo no he sido una Reputación por debajo del 1 %, Escala en la cima el primer vagón por encima de 500 m, Perfeccionista derribar-reconstruir-derribar-reconstruir la misma estación, y Flota patrimonial todos los modelos de barco del juego base en líneas a la vez. Solo los vehículos, la carga y los animales del juego base cuentan para los contadores.
result: refines
```
