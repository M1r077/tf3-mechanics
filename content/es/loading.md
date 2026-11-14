---
title: Velocidad de carga y descarga
summary: Qué hace que un vehículo cargue rápido o despacio en una parada: el vehículo, las secciones del andén y las existencias que entregan o reciben el cargamento.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-14
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
| sin ninguna sección de su clase en el andén | **×0,25** | `cargo_react_util.tl:60` |
| más allá de la longitud del andén (tren demasiado largo) | **×0,25** | `cargo_react_util.tl:61` |

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

## Conviene saber

- Las estaciones dentro de una industria están siempre especializadas en el cargamento que necesita esa industria (wiki oficial).
- Los módulos de almacén especializados también congelan el plazo de entrega del cargamento que guardan (wiki oficial); un almacén universal no.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) muestra ambos factores para cada vehículo en un andén, y adónde fue el cargamento descargado.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Los almacenes especializados "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Sección especializada ×2, universal ×1, ninguna sección compatible ×0,25, más allá del andén ×0,25, mezclados según la proporción del tren; módulo de almacén especializado ×2, almacén universal ×1.
result: refines
```
