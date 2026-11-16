---
title: Industrias
summary: Reglas de producción, existencias, terrenos y expansión, por qué una industria no crece o no tiene refuerzo, cuándo cierra una industria sin uso y cómo aparecen industrias nuevas.
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
fact: 5 años | sin carga ni consumo convierten una industria en candidata al cierre
fact: 1,1 % | de probabilidad al año en Casi nunca (por defecto), luego 730 días de cuenta atrás
fact: +50–150 % | de refuerzo por carga de refuerzo, fijo por industria
fact: 3 meses | de refuerzo por lote de carga de refuerzo
fact: ×2/3 – ×1,5 | Densidad objetivo de la industria: las industrias nuevas no se pueden desactivar
---

Cada industria funciona con **reglas**: «toma esto de las existencias de entrada, pon aquello en las existencias de salida», un número fijo de veces al año. Las industrias primarias (minas, granjas, pozos) no necesitan entrada; su tamaño viene de sus **terrenos**. Dos refuerzos pueden multiplicar la producción: la **carga de refuerzo** (solo industrias primarias) y los **trabajadores**.

## Reglas de producción

- Una regla indica la carga usada y producida por ciclo, y cuántos ciclos al año: un ciclo dura un año ÷ ese número (`industry_react_util.tl:51-57`). La sección Producción de la ventana de la industria lo muestra con números pequeños.
- El número **Máx.** de la ventana es: por ciclo × ciclos al año × los refuerzos × el ajuste **Productividad de la industria** (`industry_util.tl:310-379`).
- **Productividad de la industria**: 50 %, 75 %, 100 %, 150 % o 200 %. Preajustes: Fácil 150 %, Normal 100 %, Difícil 75 %, Muy difícil 50 % (`difficulty_util.tl:41`, `difficulty_util.tl:93`, `difficulty_util.tl:120`, `difficulty_util.tl:148`, `difficulty_util.tl:175`, `mod.script.tl:196-197`).
- Ejemplo, Acería: 6 mineral de hierro + 6 carbón → 3 acero + 4 lámina de metal, 121,7 ciclos al año: 730 mineral de hierro y 730 carbón → 365 acero y 487 lámina de metal (`steel_mill.con.lua:43-71`). Si falta una entrada, la regla se para.
- La Fábrica de conservas tiene dos reglas: pescado + lámina de metal, o carne + lámina de metal (`food_factory.con.lua:43-74`).

```engine
El motor ejecuta las reglas. Puede alargar un ciclo: la descripción del ciclo muestra entonces «(+ … debido al tiempo de entrega)» (`industry_react_util.tl:61-76`). Cuándo y cuánto no está en los scripts, así que la producción real puede quedar por debajo del Máx.
```

## Existencias

- Cada carga tiene su propia existencia con un límite: p. ej. una Mina de carbón guarda 100 herramientas y 400 carbón, una Acería 800 mineral de hierro, 800 carbón, 400 acero y 500 lámina de metal (`coal_mine.con.lua:44-67`, `steel_mill.con.lua:43-71`).
- Las existencias nunca se degradan (`industryutil.lua:25-29`): la carga espera lo que haga falta.
- Una existencia de salida llena no para la producción: lo que sobra se tira (wiki oficial). El gráfico **Flujo de cargamento** muestra **Consumido**, **Producido** y **Destruido** (`industry_eow.script.tl:804-816`).
- Con el parámetro de construcción **Entrada** en Desactivado, las reglas pierden sus entradas y la industria no tiene existencias de entrada (`industryutil.lua:280-287`, `industryutil.lua:383-387`, `industryutil.lua:432-441`).

## Terrenos y expansión

- Las industrias primarias y la Granja de ganado tienen **terrenos** (campos, pozos de mina, torres). Su nivel es su número de terrenos (`industryutil.lua:602-617`).
- La regla crece con los terrenos: producción por ciclo × terrenos ÷ **todos los terrenos de ese tipo de industria**, redondeado, al menos 1. Las entradas bajan en la misma proporción (`industryutil.lua:225-259`). Una Mina de carbón (8 tipos de terreno) con 4 terrenos hace 8 carbón por ciclo en vez de 16.
- Cada industria recibe un máximo: al azar entre la mitad de los terrenos y todos, o Pequeña / Mediana / Grande (50 / 75 / 100 %) con el parámetro **Tamaño de la industria** (`industryutil.lua:519-537`). Una mina con máximo 5 de 8 nunca llega a la regla completa.
- Con Mediana, si el 75 % redondeado da todos los terrenos, el máximo es todos los terrenos menos uno (`industryutil.lua:523-526`). Una industria nueva empieza con los terrenos que el motor construye al colocarla; su nivel se fija a partir de ellos (`industryutil.lua:602-617`).
- Cada medio año de **tiempo de juego** el juego puede añadir **un terreno** (`industries_config.res.lua:5`, `industries.script.tl:161-167`). Se usa medio año estándar, así que la velocidad del calendario no cambia la frecuencia (ver [Tiempo de juego y calendario](time.html)).
- La probabilidad es (nota − 25 %) ÷ 50 %, con nota = nota de producción × la parte de la producción que transportas (como mucho 1): 25 % o menos nunca, 75 % o más siempre (`industries.script.tl:168-179`).
- Así que una industria cuya carga no transportas **nunca crece**. Las fábricas no tienen terrenos y nunca crecen.
- En el máximo la ventana dice **Esta industria ha alcanzado todo su potencial.**; si edificios, vías o carreteras estorban, **La expansión de la industria está bloqueada.** (`industry_react_util.tl:588-602`, `industries.script.tl:13-38`). Ningún script quita terrenos; según la wiki oficial, los terrenos demolidos bajan la producción.
- El script del juego se salta las industrias que te pertenecen, las de desarrollo manual y las que están en cuenta atrás de cierre: nunca reciben un terreno de él (`industries.script.tl:94-99`, `industries.script.tl:147-157`).

Ejemplo, **Campamento maderero**: 20 terrenos, 8 troncos por ciclo, 30,4 ciclos al año (`forest.con.lua:54-66`, `forest.con.lua:75-98`). Por ciclo hace 8 × terrenos ÷ 20, redondeado, al menos 1 (`industryutil.lua:231-241`):

| Terrenos (nivel) | Troncos por ciclo | Troncos al año (Máx., sin refuerzo, Productividad 100 %) |
|---|---|---|
| 1–3 | 1 | 30 |
| 4–6 | 2 | 61 |
| 7–8 | 3 | 91 |
| 9–11 | 4 | 122 |
| 12–13 | 5 | 152 |
| 14–16 | 6 | 183 |
| 17–18 | 7 | 213 |
| 19–20 | 8 | 243 |

La producción sube por escalones: un terreno nuevo no siempre aumenta la producción.

## ¿Por qué mi industria no crece?

```diagram ind_growth
```

1. **Carga no transportada**: la nota cuenta la parte de la producción cargada en tus vehículos. Con una nota de producción del 100 %, transportar el 25 % o menos no da ninguna probabilidad, el 50 % una probabilidad de la mitad, el 75 % o más un terreno cada medio año.
2. **En su máximo**: **Esta industria ha alcanzado todo su potencial.** El máximo se sortea al construirla (de la mitad a todos los terrenos) y nunca cambia.
3. **Bloqueada**: **La expansión de la industria está bloqueada.** Quita las carreteras, vías o edificios del lugar del siguiente terreno (mostrado en la ventana).
4. **No es una industria primaria**: las fábricas no tienen terrenos.
5. **Cuenta atrás de cierre**, industria tuya o desarrollo manual: el script no la hace crecer (arriba).
6. **Sin producción**: una industria que no produce nada en el año se salta (`industries.script.tl:168-171`).

```tip scripts
**Para que una mina o una granja crezca, transporta al menos el 75 % de su producción y mantén alta su valoración de producción.** La probabilidad usa valoración de producción × parte transportada: con el 25 % o menos no hay terreno nuevo; con el 75 % o más y una valoración de producción del 100 %, uno cada medio año, hasta su máximo.
```

```engine
La nota de producción (getProductionRating), la producción anual y la cantidad transportada (getCargoOutputPerYear, getCargoShippedPerYear), y dónde va un terreno nuevo (makeIndustryExtendProposal) son valores del motor.
```

## Carga de refuerzo

Las 13 industrias primarias tienen una segunda regla, el **refuerzo**: toma un lote de carga de refuerzo de la existencia de entrada 4 veces al año y da un bonus mientras dura.

| Industria | Terrenos | A tamaño completo, por año | Lote de refuerzo (4 al año) | Fuente |
|---|---|---|---|---|
| Cantera de arcilla | 8 | 365 arcilla | 12 herramientas | `clay_pit.con.lua:42-82` |
| Mina de carbón | 8 | 320 carbón | 13 herramientas | `coal_mine.con.lua:44-85` |
| Granja de algodón | 21 | 274 lana | 17 fertilizante | `cotton_farm.con.lua:42-98` |
| Granja de cultivos | 20 | 274 grano + 183 vegetales | 17 fertilizante | `farm.con.lua:44-106` |
| Caladeros | 18 | 263 pescado | 12 herramientas | `fishing_grounds.con.lua:44-101` |
| Campamento maderero | 20 | 243 troncos | 15 máquinas | `forest.con.lua:44-99` |
| Mina de mineral de hierro | 8 | 365 mineral de hierro | 15 máquinas | `iron_ore_mine.con.lua:44-84` |
| Plataforma petrolífera | 9 | 365 crudo | 12 máquinas | `oil_platform.con.lua:45-96` |
| Pozo petrolífero | 14 | 548 crudo | 15 máquinas | `oil_well.con.lua:44-94` |
| Cantera | 7 | 365 piedra | 12 herramientas | `quarry.con.lua:44-83` |
| Granja de caucho | 23 | 365 caucho | 17 fertilizante | `rubber_farm.con.lua:41-102` |
| Draga de arena | 9 | 365 arena | 15 máquinas | `sand_excavator.con.lua:44-92` |
| Cantera de arena | 8 | 365 arena | 12 herramientas | `sand_pit.con.lua:44-84` |

- El bonus se sortea una vez por industria: **+50 % a +150 %**, redondeado al 1 % (`industryutil.lua:394-405`). La sección Refuerzo lo muestra como «+X %» (`industry_util.tl:428-434`). Con el parámetro **Factor de refuerzo** vale en cambio +50 %, +75 %, +100 %, +125 % o +150 % (`industryutil.lua:289-299`).
- La ventana muestra el refuerzo activo mientras dura su último lote (3 meses), o en cuanto la existencia tiene un lote completo (`industry_util.tl:55-91`).
- El lote **no** baja con los terrenos: una mina pequeña pide tantas herramientas como una grande (`industryutil.lua:227-229`).
- Los dos refuerzos se multiplican: producción × factor de trabajadores × (1 + bonus de refuerzo) (`industry_util.tl:42-104`).

## El refuerzo de trabajadores

La mitad de los puestos (10 de 20) debe estar ocupada por residentes que **llegaron con tus líneas de pasajeros** en los últimos 2 años; el factor es ×1,5 a ×2,5, fijo por industria (`industry_productivity_util.tl:35-72`). Los trabajadores solo asignados no cuentan. Detalles: [Trabajadores y el refuerzo de trabajadores](workers.html).

## ¿Por qué mi industria no tiene refuerzo?

1. **No es una industria primaria**: las fábricas no tienen regla de refuerzo, solo el refuerzo de trabajadores (`steel_mill.con.lua:61-70`).
2. **Lote incompleto**: la existencia debe tener un lote completo, p. ej. 13 herramientas para una Mina de carbón. Por debajo de 4 lotes al año (52 herramientas) el refuerzo se para entre entregas.
3. **Carga equivocada**: herramientas, máquinas o fertilizante según la industria (tabla de arriba).
4. **Trabajadores**: asignados no basta; la sección Refuerzo cuenta llegadas («12/10») (`industry_react_util.tl:617-654`). Ver [Trabajadores y el refuerzo de trabajadores](workers.html).

```tip scripts
**Para un potenciador que nunca se detenga, entrega al menos 4 lotes completos al año** (52 herramientas para una mina de carbón). Cada lote mantiene el bonus 3 meses.
```

## ¿Cuándo cierra una industria sin uso?

```diagram ind_closure
```

La comprobación se hace cada 100 actualizaciones para cada industria (`industries.script.tl:84-85`):

1. **Candidata**: ninguna carga **cargada** en un vehículo y ninguna **consumida** durante **5 años** (desde su construcción si nunca) (`industries.script.tl:104-119`, `industries_config.res.lua:6`). Producir no basta.
2. **Azar**: cada año una candidata se marca con la probabilidad del ajuste **Frecuencia de cierre de industrias** (tabla abajo) (`industries.script.tl:120-131`).
3. **Cuenta atrás**: aparece la notificación **Cierre de industria**, con 2 años (730 días) de plazo (`industries_config.res.lua:7`, `industry_close.script.tl:53-67`). Después la industria se elimina con sus propios tramos de carretera (`industries.script.tl:147-155`, `industry_util.tl:560-601`).
4. **Salvada**: una sola carga o un consumo durante la cuenta atrás la cancela (`industries.script.tl:134-137`). Aceptar un subsidio **Suministrar a industria** o **Transportar trabajadores** para ella también la cancela (`subvention_util.tl:473-484`).

```tip scripts
**¿Aviso de Cierre de industria? Una sola carga o una sola entrega durante los 730 días lo cancela.** Aceptar un subsidio Suministrar a industria o Transportar trabajadores para esa industria también lo cancela.
```

| Frecuencia de cierre de industrias | Probabilidad al año como candidata | Mitad de las candidatas marcadas tras | Preajuste | Fuente |
|---|---|---|---|---|
| Nunca | 0 | nunca | Fácil | `difficulty_util.tl:94` |
| Casi nunca (por defecto) | 1,1 % | unos 63 años | Normal | `difficulty_util.tl:121` |
| A veces | 2,2 % | unos 32 años | Difícil | `difficulty_util.tl:149` |
| Con frecuencia | 4,4 % | unos 16 años | – | `difficulty_util.tl:37` |
| Con mucha frecuencia | 8,8 % | unos 8 años | Muy difícil | `difficulty_util.tl:176` |

La probabilidad es 0,011 al año × 0, 1, 2, 4 u 8 (`mod.script.tl:171`, `mod.script.tl:202-203`, `difficulty_util.tl:37`). Las industrias que te pertenecen nunca cierran, ni las de desarrollo manual, ni ninguna durante el tutorial (`industries.script.tl:94-102`).

```engine
Qué cuenta como «cargado» y «consumido» (los registros itemsLoaded e itemsConsumed, p. ej. si cuenta la carga de refuerzo), el indicador manualDevelopment, y por qué se excluyen las industrias con depósito (`industries.script.tl:140-146`) dependen del motor. También qué hace el motor con una regla de refuerzo que perdió su entrada (Entrada desactivada).
```

## Industrias nuevas

El motor añade industrias nuevas durante la partida. La notificación es **Nueva industria fundada**: «Un emprendedor visionario ha descubierto una oportunidad para sacar beneficio y ha fundado {industry}.» (`industry_spawn.script.tl:34-36`, `industry_spawn.res.lua:6`). Ningún script del juego elige el lugar, el tipo ni el momento, y ninguno filtra lo que propone el motor.

Lo que los scripts dan al motor (`mod.script.tl:128-133`, `mod.script.tl:166-168`, `mod.script.tl:194-195`):

| Valor de config | Valor | Significado |
|---|---|---|
| spawnTargetTimeSpan | 50 × 365,25 días estándar | llamado «tiempo objetivo»: 50 años estándar de tiempo de juego |
| spawnProbabilityExponent | 3,0 | exponente de la probabilidad de aparición (fórmula en el motor) |
| spawnIndustries | desactivado en el editor de mapas, activado en partida | ninguna industria nueva en el editor de mapas |
| industryDensity | 1 × **Densidad objetivo de la industria** | el número objetivo de industrias |
| maxNumberPerArea, absoluteMinimum | 0,8 por km² (0,64 en consolas), 24 | también lo usa el generador de mapas |

**Densidad objetivo de la industria** («Establece la densidad objetivo de las industrias del mapa.»): 5 niveles, ×2/3, ×5/6, ×1, ×1,2, ×1,5 (`difficulty_util.tl:55`, `difficulty_util.tl:85`).

- Está en los ajustes avanzados, parte de economía (`advanced_settings.tl:287-291`), y no forma parte de los preajustes Fácil … Muy difícil (`difficulty_util.tl:90-199`).
- En el menú de partida nueva, **Densidad de la industria** (las industrias al inicio, los mismos 5 factores) pone **Densidad objetivo de la industria** en el mismo nivel (`new_game_or_map_settings_page.tl:159-166`, `new_game_react_util.tl:288-296`). Cambia el objetivo después en los ajustes avanzados si quieres que sean distintos.
- **Ningún ajuste lo desactiva**: el nivel más bajo es ×2/3. Solo el editor de mapas no tiene industrias nuevas. Los mods sí pueden.
- Velocidad: el tiempo objetivo va en días estándar, como todas las reglas de tiempo de juego, así que la velocidad del calendario y un calendario en pausa no deberían frenarlo. Medido con el calendario en pausa: en 1809 s de tiempo de juego aparecieron 3 industrias nuevas, con 760 s y 728 s de separación, así que un calendario en pausa no las detiene. Medido con [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) en 3 partidas (unas 500 industrias nuevas): las industrias nuevas llegaron con unos **730 s** de tiempo de juego de separación a todas las velocidades del calendario (×4, ×1, ×0,5, ×0,25). Son unos 45 días del calendario a ×0,25 y 2 años a ×4.
- Prospección de recursos (abajo) usa la misma llamada del motor con una localidad, así que una aparición «cerca de una localidad» existe en el motor (`company.script.tl:202`). El tutorial también la usa (`tutorial_init.tl:23-24`).

```engine
La fórmula detrás de los 50 años y el exponente 3, cómo se cuenta la densidad objetivo (¿por superficie del mapa, por localidad?), qué tipo se elige y dónde va (makeIndustrySpawnProposal) dependen del motor. Ningún script explica por qué pueden aparecer varias industrias de un tipo muy juntas («nueve minas de carbón una al lado de otra»), ni por qué algunas aparecen en el otro extremo del mapa.
```

### Prospección de recursos

La ventaja de empresa **Prospección de recursos** busca una industria nueva de ese recurso cerca de una localidad que eliges: un intento al mes, con una probabilidad que sube del 20 % al 60 %, durante 6 meses (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`). Si el recurso tiene varios tipos de industria, se prueban en orden aleatorio (`company.script.tl:185-206`). Si todos los intentos fallan, el permiso vuelve (`company.script.tl:106-110`).

## Bueno saber

- Transporta desde cada industria primaria que quieras hacer crecer: la producción no transportada bloquea la expansión, sean cuales sean los refuerzos.
- Lleva la carga de refuerzo a las minas y granjas más grandes: el lote cuesta igual, el bonus sigue a los terrenos.
- Las existencias no se degradan: puedes entregar carga de refuerzo por adelantado, hasta el límite de la existencia (100).
- Los refuerzos suben ruido y contaminación: una Mina de carbón pasa de 10 de contaminación a 20 con un refuerzo y 30 con dos (`coal_mine.con.lua:99-117`).
- Menos industrias nuevas: pon **Densidad objetivo de la industria** en su nivel más bajo en los ajustes avanzados; no se puede poner a cero.
- Con el ajuste por defecto una industria sin uso cierra rara vez; en Con mucha frecuencia, carga algo de vez en cuando.

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 5 años, no 10, y la producción no cuenta: solo la carga cargada en un vehículo o consumida. Tras los 5 años la industria solo es candidata: cada año se marca con una probabilidad del 1,1 % (Casi nunca) al 8,8 % (Con mucha frecuencia). La cuenta atrás dura 730 días, como se dice. La carga de refuerzo da +50 % a +150 % por industria, en lotes que duran 3 meses. Industrias nuevas: ningún ajuste de activar/desactivar, solo Densidad objetivo de la industria de ×2/3 a ×1,5; ninguna en el editor de mapas.
result: differs
```
