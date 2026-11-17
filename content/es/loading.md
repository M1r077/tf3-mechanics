---
title: Velocidad de carga y descarga
summary: Qué hace que un vehículo cargue rápido o despacio en una parada: el vehículo, las secciones del andén y las existencias que entregan o reciben el cargamento.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-15
game: 40425
fact: ×2 | sección de andén especializada
fact: ×0,25 | sección incorrecta o tren demasiado largo
fact: ×4 | mejor caso: andén y almacén especializados
---

El tiempo que un vehículo pasa cargando o descargando es su propia velocidad de carga multiplicada por dos factores: uno del **andén** y otro de las **existencias** del otro lado (almacén, industria, localidad).

```diagram loading_factors
```

## 1. El vehículo

Cada vehículo tiene una velocidad de carga base, que se muestra en la Tienda de vehículos y en la ventana del vehículo ("x2,0"). Todo lo que sigue la multiplica.

## 2. El factor del andén

Para el juego, un andén no es una fila de módulos: es una **lista de secciones, una por clase de cargamento**, con la suma de las longitudes de todos los módulos de esa clase.

```diagram loading_sections
```

| Vagones… | Factor | Fuente |
|---|---|---|
| en una sección de su clase (vagones a granel, sección a granel) | **×2** | `modular_station.script.lua:1042` |
| en una sección universal | ×1 | `modular_station.script.lua:1042` |
| sin ninguna sección de su clase en el andén | **×0,25** (constante del tooltip de carga; el factor en sí lo aplica el motor) | `cargo_react_util.tl:60` |
| más allá de la longitud del andén (tren demasiado largo) | **×0,25** (constante del tooltip de carga; el factor en sí lo aplica el motor) | `cargo_react_util.tl:61` |

- El factor es una **mezcla según la proporción del tren**: si 3/4 de los vagones coinciden y 1/4 no, el factor es ¾ × 2 + ¼ × 0,25 ≈ ×1,56 (`cargo_react_util.tl:63-70`, el mismo reparto que el juego muestra como "Terminal parcialmente especializada").
- **Dónde** se detienen los vagones en el andén no importa, solo cuentan las longitudes sumadas (medido en el juego).
- Carretera: las terminales de camiones especializadas dan ×2 (`modular_terminal.script.lua:2956`); las pequeñas paradas de calle son siempre ×1 (`small_stops.script.lua:19`).
- Los andenes de pasajeros son ×1.

## 3. El factor de las existencias

Al descargar, cada unidad va a un receptor: un módulo de almacén, una industria o un edificio de la localidad. Las existencias del receptor tienen su propio factor.

| Receptor | Factor | Fuente |
|---|---|---|
| módulo de almacén **especializado** (líquidos, a granel, de plataforma, mercancías) | **×2** | `modules.script.lua:120`, `warehouse.script.lua:297-314` |
| almacén **universal** | ×1 | `warehouse.script.lua:272-285` |
| industria | ×1 | medido en el juego |

- Todo módulo de almacén pide ×2, pero los módulos universales solo añaden capacidad a **unas existencias universales compartidas**, que se crean con ×1. Solo los módulos especializados tienen existencias propias con ×2.
- La descripción emergente del juego llama a este factor "Almacén especializado: +100 %" (`cargo_react_util.tl:51-54`).
- Durante una misma descarga el juego atiende a los receptores **por turnos**, así que la velocidad cambia mientras el tren descarga cuando parte del cargamento va a un almacén y parte a una industria (medido en el juego).

```engine
Qué receptor recibe cada unidad, y la multiplicación final, se deciden en el motor. Los factores de arriba son los datos que le pasan los scripts; el resultado se comprobó con los valores que expone el motor (sonda de [Platform Details](https://mod.io/g/transportfever3/m/platform-details), octubre de 2026).
```

## Lo que muestra el juego

- El indicador de carga aparece como **acelerado** por encima de ×1,5 y como **ralentizado** por debajo de ×0,75 (`cargo_react_util.tl:119-122`).
- Pasa el ratón por encima: la descripción emergente enumera "Terminal especializada", "Las especializaciones no coinciden", "Terminal demasiado corta" y "Almacén especializado", cada una con su porcentaje (`cargo_react_util.tl:76-99`).

## Ejemplo

Un tren de 8 vagones a granel, de 160 m, descargando carbón.

| Estación | Andén | Receptor | Factor |
|---|---|---|---|
| andén universal de 160 m | ×1 | acería | **×1** |
| andén a granel de 160 m | ×2 | acería | **×2** |
| andén a granel de 160 m | ×2 | almacén a granel especializado | **×4** |
| andén a granel de 160 m | ×2 | almacén universal | **×2** |
| andén universal de 120 m (tren 40 m demasiado largo) | ¾ × 1 + ¼ × 0,25 ≈ ×0,81 | acería | **×0,81** |

## Dónde se descarga el cargamento

Cada parada de una línea tiene una lista **Carga**, en la ventana "Filtro de cargamento" de la parada. En la parada, el vehículo conserva a bordo el cargamento de esa lista; el resto se descarga en cualquier existencia de la zona de influencia que lo acepte, almacenes incluidos (medido en el juego).

- Así es como un tren acaba vaciándose en un almacén a mitad de su línea. En el juego: en una parada junto a un almacén, con solo plástico en su lista, las herramientas a bordo fueron al almacén, aunque estaba casi lleno.
- Un andén de pasajeros no transfiere mercancías: allí el cargamento se queda a bordo (medido en el juego).
- Para conservar el cargamento a bordo, añádelo a la lista Carga de esa parada.

```tip
**¿Desaparece cargamento en una parada junto a un almacén? Añádelo a la lista Carga de esa parada.** Todo lo que no está en la lista se descarga en cualquier existencia al alcance, y el almacén no paga nada.
```

| Opción de "Filtro de cargamento" | Qué hace | Fuente |
|---|---|---|
| "Forzar la descarga de todo el cargamento al llegar" | tooltip: "Descargar el cargamento aunque las existencias estén llenas"; el cargamento que no cabe se destruye: el juego indica la estación como destino, y una estación nunca consume cargamento (medido en el juego). Desactivada en una parada nueva. | `cargofilter_window.tl:757`, `line_util.tl:476` |
| "Destruir el cargamento al llegar cuando cambie la configuración" | descarga o destruye el cargamento a bordo cuando en esta parada espera carga para otra configuración de carga del vehículo; cuál de las dos cosas pasa lo decide el motor | `cargofilter_window.tl:767` |
| "Sustituir por cargamento nuevo si hay disponibilidad" | destruye el cargamento que volvió a la parada donde se cargó, cuando espera cargamento más nuevo del mismo tipo | `cargofilter_window.tl:778` |

- Con la primera opción desactivada, el icono del cargamento muestra "≤" y la descripción emergente "Descargar si no se ha alcanzado el límite de existencias" (`cargofilter_window.tl:124`, `cargofilter_window.tl:158`).

## Varios cargamentos en una línea

- La lista **Carga** de una parada es un sí/no por tipo de cargamento, **sin orden**: el jugador no puede decidir qué cargamento se carga primero. Los iconos solo se dibujan en el orden de cargamentos del juego (`line_util.tl:471-475`, `line_util.tl:510`, `cargofilter_window.tl:533-535`).
- Un vagón o camión que admite varios cargamentos tiene, por compartimento, varias **configuraciones de carga**; la capacidad del compartimento es la mayor de ellas, no su suma (`model_metadata_util.lua:682-733`, `vehicle_metadata_util.lua:27-37`). Por eso lleva solo una de ellas a la vez.
- Los vehículos nuevos tienen activada la elección automática de configuración en cada compartimento (`vehicle_react_util.tl:339`), y el juego no tiene ninguna ventana para elegir a mano el cargamento de un vehículo.
- Pasajeros y cargamento pueden compartir una línea: los scripts nunca rechazan cargamento en una parada porque también admita pasajeros (`line_util.tl:1381-1386`). El cargamento solo se quita de una parada cuya terminal no puede cargar ni descargar cargamento (`line_util.tl:554-559`).
- Con varios cargamentos, **Capacidad máxima (cualquiera)** y **Capacidad máxima (todo)** se comportan de forma distinta: ver [Ajustes de salida: capacidad máxima, nivel de llenado y tiempos de parada](departure.html).
- Cuando la configuración no encaja, la línea muestra **Algunas configuraciones de tipos de carga de esta línea entran en conflicto**, por ejemplo "Ningún vehículo de la línea puede transportar parte del cargamento configurado para su carga." (`line_warning.script.tl:10-36`).

```engine
El orden en que se cargan varios cargamentos, cómo se reparten unas existencias compartidas entre los vehículos que esperan y cómo elige un vehículo su configuración de carga lo decide el motor.
```

## La configuración automática

Mientras nadie haya guardado un cambio en la ventana "Filtro de cargamento" de una parada, lo que la desactiva para siempre en esa línea (`line_util.tl:495-498`, `cargofilter_window.tl:438`), el juego rellena él mismo las listas Carga cada vez que se crea la línea, se añade o quita una parada, se reordenan las paradas o se añade un punto de paso (`manager_window.tl:6712`, `:6786`, `:6845`, `:6879`, `:6963`). Mover una parada a otra estación o andén, y quitar o mover un punto de paso, no la ejecutan (`manager_window.tl:6851-6868`, `manager_window.tl:6968-6992`).

- Empieza de nuevo con listas vacías, con pasajeros en las estaciones de pasajeros (`line_util.tl:542-588`).
- Busca productores y consumidores solo entre industrias y edificios de la ciudad: los almacenes no cuentan (`cargo_util.tl:518-526`).
- Pone un cargamento en la lista Carga de una parada cuando hace falta más adelante y nada en la parada lo acepta. Un almacén cuenta como si aceptara todo lo que almacena (`line_util.tl:676-693`): en una parada junto a un almacén que guarda ese cargamento, el cargamento queda fuera de la lista y el tren lo descarga allí.
- En cuanto se cambia un filtro a mano, la línea queda marcada como personalizada (`cargofilter_window.tl:438`) y la configuración automática ya no la toca nunca, ni siquiera cuando después se añaden paradas (`line_util.tl:496`).

```engine
Los scripts solo escriben las listas Carga; la descarga en sí la hace el motor. La regla anterior (lo que no está en la lista se descarga en cualquier existencia que lo acepte) se observó en el juego con [Platform Details](https://mod.io/g/transportfever3/m/platform-details), noviembre de 2026.
```

## Conviene saber

- Las estaciones dentro de una industria están siempre especializadas en el cargamento que necesita esa industria (wiki oficial).
- Los módulos de almacén especializados también congelan el plazo de entrega del cargamento que guardan (wiki oficial); un almacén universal no.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) muestra ambos factores para cada vehículo en un andén, y adónde fue el cargamento descargado.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Los almacenes especializados "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Sección especializada ×2, universal ×1, ninguna sección compatible ×0,25, más allá del andén ×0,25, mezclados según la proporción del tren; módulo de almacén especializado ×2, almacén universal ×1.
result: refines
```
