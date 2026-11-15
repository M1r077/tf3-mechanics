---
title: Industrias
summary: Reglas de producción, existencias, terrenos y expansión, carga de refuerzo, por qué una industria no tiene refuerzo, y cuándo cierra de verdad una industria sin uso.
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
fact: 5 años | sin carga ni consumo convierten una industria en candidata al cierre
fact: 1,1 % | de probabilidad al año en Casi nunca (por defecto), luego 730 días de cuenta atrás
fact: +50–150 % | de refuerzo por carga de refuerzo, fijo por industria
fact: 3 meses | de refuerzo por lote de carga de refuerzo
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
- Cada medio año el juego puede añadir **un terreno** (`industries_config.res.lua:5`, `industries.script.tl:158-183`). La probabilidad es (nota − 25 %) ÷ 50 %, con nota = nota de producción × la parte de la producción que transportas (como mucho 1): 25 % o menos nunca, 75 % o más siempre (`industries.script.tl:172-176`).
- Así que una industria cuya carga no transportas **nunca crece**. Las fábricas no tienen terrenos y nunca crecen.
- En el máximo la ventana dice **Esta industria ha alcanzado todo su potencial.**; si edificios, vías o carreteras estorban, **La expansión de la industria está bloqueada.** (`industry_react_util.tl:588-602`, `industries.script.tl:13-38`). Ningún script quita terrenos; según la wiki oficial, los terrenos demolidos bajan la producción.

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

## ¿Cuándo cierra una industria sin uso?

```diagram ind_closure
```

La comprobación se hace cada 100 actualizaciones para cada industria (`industries.script.tl:84-85`):

1. **Candidata**: ninguna carga **cargada** en un vehículo y ninguna **consumida** durante **5 años** (desde su construcción si nunca) (`industries.script.tl:104-119`, `industries_config.res.lua:6`). Producir no basta.
2. **Azar**: cada año una candidata se marca con la probabilidad del ajuste **Frecuencia de cierre de industrias** (tabla abajo) (`industries.script.tl:120-131`).
3. **Cuenta atrás**: aparece la notificación **Cierre de industria**, con 2 años (730 días) de plazo (`industries_config.res.lua:7`, `industry_close.script.tl:53-67`). Después la industria se elimina con sus propios tramos de carretera (`industries.script.tl:147-155`, `industry_util.tl:560-601`).
4. **Salvada**: una sola carga o un consumo durante la cuenta atrás la cancela (`industries.script.tl:134-137`). Aceptar un subsidio **Suministrar a industria** o **Transportar trabajadores** para ella también la cancela (`subvention_util.tl:473-484`).

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

- El motor añade industrias con el tiempo; los scripts solo le dan un tiempo objetivo de 50 años, un exponente de 3 y ninguna industria nueva en el editor de mapas (`mod.script.tl:166-168`). El ajuste **Densidad objetivo de la industria** lo escala (`mod.script.tl:194-195`). La notificación es **Industria fundada** (`industry_spawn.res.lua:6`).
- La ventaja de empresa **Prospección de recursos** busca una industria nueva de ese recurso cerca de una localidad: un intento al mes con una probabilidad del 20 % al 60 %, durante 6 meses; si falla, el permiso vuelve (`company_util.tl:14-17`, `company.script.tl:96-142`, `company.script.tl:299-307`).

```engine
Dónde y cuándo aparece una industria nueva, y de qué tipo, lo decide el motor (makeIndustrySpawnProposal).
```

## Bueno saber

- Transporta desde cada industria primaria que quieras hacer crecer: la producción no transportada bloquea la expansión, sean cuales sean los refuerzos.
- Lleva la carga de refuerzo a las minas y granjas más grandes: el lote cuesta igual, el bonus sigue a los terrenos.
- Las existencias no se degradan: puedes entregar carga de refuerzo por adelantado, hasta el límite de la existencia (100).
- Los refuerzos suben ruido y contaminación: una Mina de carbón pasa de 10 de contaminación a 20 con un refuerzo y 30 con dos (`coal_mine.con.lua:99-117`).
- Con el ajuste por defecto una industria sin uso cierra rara vez; en Con mucha frecuencia, carga algo de vez en cuando.

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 5 años, no 10, y la producción no cuenta: solo la carga cargada en un vehículo o consumida. Tras los 5 años la industria solo es candidata: cada año se marca con una probabilidad del 1,1 % (Casi nunca) al 8,8 % (Con mucha frecuencia). La cuenta atrás dura 730 días, como se dice. La carga de refuerzo da +50 % a +150 % por industria, en lotes que duran 3 meses.
result: differs
```
