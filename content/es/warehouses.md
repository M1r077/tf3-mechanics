---
title: Almacenes
summary: Módulos universales o especializados, qué guarda cada existencia, fijar un tipo de cargamento, velocidad de carga, costes y contaminación, y lo que un almacén no hace.
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
game: 40425
fact: 500 | unidades de cargamento por módulo, sea del tipo que sea
fact: ×2 | velocidad de carga en un módulo especializado, ×1 en uno universal
fact: 150.000 / 300.000 | precio de un módulo universal / especializado
fact: 0 | ingresos por el cargamento descargado en un almacén
---

Un almacén es una entrada y un conjunto de **módulos**. Guarda cargamento entre dos líneas: una línea lo descarga y otra lo vuelve a cargar. Las estaciones llegan a él a través de su zona de influencia; las localidades y las industrias nunca toman nada de él (wiki oficial).

## Módulos universales o especializados

| Módulo | Existencias | Guarda | Factor de carga | Fuente |
|---|---|---|---|---|
| **Almacén universal** | todos los módulos universales comparten **unas** existencias | cualquier cargamento, mezclado | ×1 | `warehouse.script.lua:272-295`, `modules.script.lua:49` |
| **Almacén de líquidos**, **Almacén para cargamento a granel**, **Almacén para cargamento de plataforma**, **Almacén de mercancías** | **unas existencias por módulo** | un tipo de cargamento a la vez, de su clase | ×2 | `warehouse.script.lua:296-314`, `modules.script.lua:120`, `modules.script.lua:165`, `modules.script.lua:247`, `modules.script.lua:296` |

- Cada módulo añade **500** unidades (`modules.script.lua:49`, `modules.script.lua:120`). Cinco módulos universales forman unas existencias de 2.500; cinco módulos de líquidos forman cinco existencias de 500.
- Los pasajeros nunca se almacenan (`warehouse.script.lua:279`, `warehouse.script.lua:304`).
- Un módulo especializado acepta un solo tipo de cargamento a la vez: para guardar petróleo crudo y combustible necesitas dos módulos de líquidos (wiki oficial).
- El ×2 de un módulo especializado se multiplica por el factor del andén: un andén a granel y un módulo a granel dan ×4. Detalles: [Velocidad de carga y descarga](loading.html).

## ¿Universal o especializado?

1. **Muchos tipos de cargamento, cantidades pequeñas**: universal. Unas existencias compartidas, la mitad de precio y la mitad de contaminación.
2. **Un cargamento en grandes cantidades** (carbón, petróleo crudo, troncos): especializado. Los vehículos descargan y cargan allí el doble de rápido, pero necesitas un módulo por tipo de cargamento.
3. **Alimentos y otro cargamento con tiempo de entrega corto**: especializado; la wiki oficial dice que estos módulos congelan el plazo de entrega (ver más abajo).
4. Ambos tipos se pueden mezclar en un almacén: los módulos universales siguen formando unas existencias, y cada módulo especializado las suyas.

## ¿Un almacén acelera la descarga?

- **Módulo especializado**: sí, ×2 para el cargamento que acepta. La descripción emergente de carga del vehículo muestra "Almacén especializado: +100 %" (`cargo_react_util.tl:51-54`).
- **Módulo universal**: no. Sus existencias se crean con ×1; el ×2 que pide el módulo se ignora (`warehouse.script.lua:284`, `warehouse.script.lua:288-289`).
- Cuando parte del cargamento va a un almacén y parte a una industria, el vehículo los atiende por turnos, así que la velocidad cambia durante una misma parada (medido en el juego, ver [Velocidad de carga y descarga](loading.html)).

## La sección Existencias

- Una fila por existencia: el cargamento que acepta, la cantidad y, al pasar el ratón, la **Media de tiempo de entrega restante** (`entity_window_util.tl:408-410`).
- **Fijar un tipo de cargamento**: en un módulo especializado, haz clic en un icono de cargamento. El juego reconstruye el almacén con ese módulo reservado a ese cargamento (`entity_window_util.tl:339-367`, `warehouse.script.lua:308`). Quitar o sustituir el módulo borra su fijación (`warehouse.script.lua:403-405`).
- **Descartar todo el cargamento**: vacía esa fila de una vez (`entity_window_util.tl:423-434`). El cargamento se pierde.
- Ambos botones solo faltan en un almacén que pertenece a otro jugador; los tuyos y los almacenes sin dueño los tienen (`warehouse_eow.script.tl:127-137`, `gui/entity_window/warehouse/warehouse.tl:38`, `entity_util.tl:83-86`).
- El gráfico **Estadísticas** muestra **Entrante** (descargado) y **Saliente** (cargado) por año (`warehouse_eow.script.tl:159-160`).

## Costes y contaminación

| | Módulo universal | Módulo especializado | Fuente |
|---|---|---|---|
| Precio | 150.000 | 300.000 | `wh_universal.module.lua:18`, `wh_liquid.module.lua:22` |
| Conservación por año | 25.000 | 50.000 | `wh_universal.module.lua:19`, `wh_liquid.module.lua:23` |
| Ruido | 20 | 20 | `wh_universal.module.lua:33`, `wh_liquid.module.lua:37` |
| Contaminación | 25 | 50 | `wh_universal.module.lua:34`, `wh_liquid.module.lua:38` |

- El almacén añade su propia contaminación: **25**, o **50** en cuanto se construye un módulo especializado (`warehouse.script.lua:327`, `warehouse.script.lua:338-345`).
- El menú de construcción tiene una entrada por clase y época (desde 1900, 1940 y 1980) (`warehouses/warehouse.tl:3-5`); las épocas posteriores muestran ×3 y ×9 (`warehouses/warehouse.tl:48`, `warehouses/warehouse.tl:75-76`), y la conservación de los almacenes también crece con el año. Detalles: [Costes, conservación y préstamos](costs.html).
- Los módulos a granel, de plataforma y de mercancías cuestan lo mismo que los de líquidos (`wh_bulk.module.lua:22-23`, `wh_flatbed.module.lua:22-23`, `wh_goods.module.lua:18-19`).

```engine
Los scripts dan dos niveles de emisión, el segundo el doble del primero (`warehouse.script.lua:342-343`); el almacén pasa del primero al segundo a medida que se llenan sus existencias, existencias llenas = el doble (`emissions.script.tl:237-249`). El precio que se cobra de verdad por los módulos lo calcula el motor.
```

## Lo que un almacén no hace

- **No paga nada.** Descargar en un almacén no da ingresos; la unidad se paga una sola vez, cuando llega a su consumidor, por la distancia en línea recta desde su origen (medido en el juego, ver [Ingresos por cargamento y tiempo de entrega](income.html)).
- **No abastece a localidades ni industrias** cercanas: solo toman cargamento de los vehículos (wiki oficial).
- **No es un destino para la configuración automática de líneas**, que solo busca productores y consumidores; pero una parada junto a un almacén que guarda un cargamento deja ese cargamento fuera de la lista Carga, así que los trenes lo descargan allí (ver [Velocidad de carga y descarga](loading.html)).
- **No necesita carretera.** La entrada se ajusta a una calle, pero el cargamento solo se mueve a través de las zonas de influencia de las estaciones (`warehouse.script.lua:386-389`, wiki oficial). La ventana del almacén muestra su zona de influencia (`gui/entity_window/warehouse/warehouse.tl:88-96`).

```engine
Adónde va el cargamento descargado, y si se detiene el plazo de entrega de una unidad almacenada, lo decide el motor. Ningún script congela el plazo: la wiki oficial dice que los módulos especializados lo hacen y uno universal no.
```

## Conviene saber

- Revisa la lista Carga de cada parada cerca de un almacén: lo que no está en ella se descarga en el almacén, incluso a mitad de la línea.
- Unas existencias llenas rechazan más cargamento, salvo que la parada use "Forzar la descarga de todo el cargamento al llegar" ("Descargar el cargamento aunque las existencias estén llenas"); el cargamento que no cabe se destruye: el juego indica la estación como destino, y una estación nunca consume cargamento (medido en el juego, ver [Velocidad de carga y descarga](loading.html)).
- Para reservar un módulo especializado a un cargamento, fija su tipo de cargamento en la sección Existencias.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) enumera, por estación, los almacenes a su alcance con sus existencias; [Platform Details](https://mod.io/g/transportfever3/m/platform-details) muestra adónde fue el cargamento descargado.

```check
official: "Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types." Los almacenes especializados "freeze the cargo item's delivery timer" y "enable faster loading / unloading speeds". "In specialized warehouses, only one cargo type can be stored at a time for a given module." ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Los módulos universales forman unas existencias compartidas con factor de carga ×1; cada módulo especializado, unas existencias propias de 500 con ×2 y un tipo de cargamento. Un módulo especializado cuesta el doble (300.000, conservación 50.000) y contamina el doble (50). La congelación del plazo no está en los scripts.
result: refines
```
