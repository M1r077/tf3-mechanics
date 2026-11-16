---
title: Aviones, aeropuertos y helicópteros
summary: Aeródromo o aeropuerto, qué avión aterriza dónde, terminales, la segunda pista, helipuertos, y la lista de todas las aeronaves con su cargamento, capacidad y velocidad.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
fact: 2 | tamaños de avión: pequeño y grande
fact: 1950 | primer aeropuerto y primeros helicópteros
fact: 1980 | segunda pista
fact: 5 | aeronaves por hangar
---

Cada avión es **pequeño** o **grande**. Un **aeródromo** solo admite aviones pequeños; un **aeropuerto** admite ambos, y helicópteros en su edificio principal. Los helicópteros también tienen estaciones propias.

```diagram air_access
```

## Aeródromo y aeropuerto

- **Aeródromo**: «Pueden usarlo los aviones pequeños.» Variantes de 1920, 1950 y 1980; 1, 2 o 3 terminales y un depósito opcional (`airfield.tl:49`, `airfield.tl:76`, `airfield_era_a.metacon.tl:3`).
- **Aeropuerto**: «Pueden usarlo los aviones pequeños y grandes.» Variantes de 1950 y 1980; 2, 3 o 4 terminales y una dirección de aterrizaje (`airport.tl:24`, `airport.tl:80`, `airport1950.metacon.tl:3-4`).
- Las terminales de aeródromo solo admiten aviones pequeños; las de aeropuerto admiten ambos tamaños (`af_terminal.module.lua:715`, `ap_terminal.module.lua:897`).
- El edificio principal del aeropuerto tiene plataformas para helicópteros (`ap_main.module.lua:532`), y desde 1950 un aeropuerto puede tener una terminal de helicópteros (`ap_terminal_heli.module.lua:897`, `ap_terminal_heli.module.lua:971`).
- **Segunda pista**: un módulo de aeropuerto desde 1980 (`airport_2nd_runway.module.lua:5`). Algunos módulos de aeropuerto la necesitan y sin ella muestran «Necesitas una segunda pista» (`airport.script.lua:261`).
- Todas las estaciones aéreas admiten pasajeros y todo el cargamento (`airfield.tl:59`, `airport.tl:34`).

| Edificio | Pasajeros en espera | Fuente |
|---|---|---|
| Terminal de aeródromo | hasta 250 | `af_terminal.module.lua:773` |
| Edificio principal del aeropuerto | hasta 400 | `ap_main.module.lua:667` |
| Terminal de aeropuerto | hasta 850 | `ap_terminal.module.lua:951` |
| Terminal de helicópteros del aeropuerto | hasta 450 | `ap_terminal_heli.module.lua:990` |

## Hangares y estaciones de helicópteros

- Un **hangar** de aeródromo o aeropuerto admite 5 aeronaves y mantiene las aeronaves en un radio de 550 m (`af_hangar.module.lua:273-278`, `ap_hangar.module.lua:456-461`).
- **Helipuerto** (desde 1950): compra y mantiene helicópteros, depósito de 5, radio de mantenimiento de 800 m (`heliport.script.lua:301-306`).
- **Helisuperficie** (desde 1950): una pequeña plataforma de aterrizaje para pasajeros y cargamento, sin depósito (`helipad.con.lua:29-33`).

## Costes

Precio y conservación de la primera variante. Las variantes posteriores cuestan ×3 o ×9 ([Costes, conservación y préstamos](costs.html)); el primer aeródromo ya usa ×3 (`airfield.tl:8`).

| Edificio | Precio | Conservación por año | Fuente |
|---|---|---|---|
| Aeródromo | 1.200.000 - 3.000.000 | 50.000 - 200.000 | `airfield.tl:55-56` |
| Aeropuerto | 1.800.000 - 4.500.000 | 300.000 - 750.000 | `airport.tl:30-31` |
| Módulo de aeródromo (edificio principal, terminal, hangar) | 600.000 | 100.000 | `af_main.module.lua:316-317`, `af_hangar.module.lua:326-327` |
| Módulo de aeropuerto (terminal, hangar, segunda pista) | 900.000 | 150.000 | `ap_main.module.lua:672-673`, `ap_hangar.module.lua:508-509`, `airport_2nd_runway.module.lua:27-28` |

- La conservación de aeropuertos y aeródromos también sigue el año del calendario, ×1 en 1900 hasta ×6 en 2020 ([Costes, conservación y préstamos](costs.html)).
- El precio y los costes de funcionamiento de una aeronave se calculan a partir de su velocidad y su capacidad, como los barcos y los vehículos de carretera ([Costes, conservación y préstamos](costs.html)).

## Todos los aviones

Velocidad en km/h, redondeada. «Cualquier cargamento» significa todos los tipos de cargamento. La capacidad es el total que muestra la tienda de vehículos: la suma de los compartimentos, cada uno con su mayor configuración de carga (`vehicle_store_util.tl:70-95`).

| Avión | Años | Tamaño | Cargamento | Capacidad | Velocidad | Velocidad de carga |
|---|---|---|---|---|---|---|
| Junkers F 13 Herta | 1920-1950 | pequeño | pasajeros | 16 | 135 | - |
| Vickers J6860 Victoria | 1922-1960 | pequeño | cualquier cargamento | 32 | 150 | 2,5 |
| Fokker F VII A | 1925-1960 | pequeño | pasajeros | 32 | 175 | 2 |
| Junkers JU-52 Iron Annie | 1933-1982 | pequeño | pasajeros, cualquier cargamento | **48** (2 × 24) | 200 | 3 |
| Douglas DC-3 | 1935-1995 | pequeño | pasajeros | 56 | 300 | 2,5 |
| Curtiss C-46 Commando | 1942-1980 | pequeño | cualquier cargamento | 80 | 280 | - |
| Douglas DC-4 | 1944-1998 | pequeño | pasajeros | 100 | 365 | 3 |
| Bristol tipo 170 Freighter | 1949-2005 | pequeño | pasajeros, cualquier cargamento | **80** (2 × 40) | 350 | 1,5 |
| Lockheed L-1049 Super Connie | 1952-1986 | grande | pasajeros | 120 | 486 | 3 |
| Lockheed L-1049D/H Super Connie | 1959-2000 | grande | cualquier cargamento | **120** (2 × 60) | 486 | 2,5 |
| De Havilland DH.106 Comet | 1960-2000 | grande | pasajeros | 160 | 724 | 3 |
| Canadair CL-44 Freighter | 1962-2005 | grande | cualquier cargamento | **144** (3 × 48) | 645 | 2 |
| Convair CV 990 Coronado | 1962-2020 | grande | pasajeros | 200 | 917 | 2 |
| Lockheed L-100 Hercules | 1976-2000 | pequeño | cualquier cargamento | **132** (3 × 44) | 400 | 3 |
| McDonnell Douglas DC-10-30 | 1978- | grande | pasajeros | 400 | 960 | 2,5 |
| McDonnell Douglas DC-10-30CF | 1978- | grande | cualquier cargamento | **396** (3 × 132) | 960 | 4 |
| Airbus A310 300F Freighter | 1982- | grande | cualquier cargamento | 160 | 850 | 3 |
| Short 330 Sherpa | 1984- | pequeño | pasajeros, cualquier cargamento | **80** (2 × 40) | 455 | 2,5 |
| Airbus A320 | 1985- | grande | pasajeros | 180 | 753 | 3 |
| Br. Aerospace 146 | 1985- | pequeño | pasajeros | 112 | 753 | 3 |
| Br. Aerospace 146 Freighter | 1985- | pequeño | cualquier cargamento | **96** (2 × 48) | 753 | 2 |
| Fokker 100 | 1988- | grande | pasajeros | 160 | 845 | 3,5 |
| Tupolev Tu-204 | 1995- | grande | pasajeros | 280 | 850 | 4 |
| Tupolev Tu-204C Freighter | 1995- | grande | cualquier cargamento | **204** (3 × 68) | 850 | 2 |
| Boeing 737-700 | 1998- | grande | pasajeros | 200 | 974 | 2,5 |
| Boeing 737-700-C Freighter | 1998- | grande | cualquier cargamento | **160** (2 × 80) | 974 | 3 |
| Bombardier DHC-8 | 2000- | pequeño | pasajeros | 120 | 648 | 3 |
| Bombardier DHC-8 Freighter | 2008- | pequeño | cualquier cargamento | 120 | 648 | 2 |
| Sukhoi Superjet 100 | 2011- | pequeño | pasajeros | 160 | 870 | 3 |
| Airbus Canada A220 | 2013- | grande | pasajeros | 180 | 830 | 5 |

## Todos los helicópteros

| Helicóptero | Años | Cargamento | Capacidad | Velocidad | Velocidad de carga |
|---|---|---|---|---|---|
| Bell 47 | 1950-1990 | pasajeros, cualquier cargamento | 8 | 150 | 2 |
| Piasecki H-21 Workhorse | 1952-1985 | pasajeros, cualquier cargamento | 80 (48 cargamento) | 210 | 3 |
| Sikorsky S-64 Skycrane | 1962-2017 | cualquier cargamento | 40 | 213 | 4 |
| Bell 206 Long Ranger | 1965-2025 | pasajeros | 32 | 241 | 2,5 |
| Boeing Vertol 234 Chinook | 1980- | pasajeros, cualquier cargamento | 80 | 269 | 2 |
| AgustaWestland AW101 Merlin | 1990- | pasajeros | 60 | 278 | 3 |
| Mil Mi-26TC | 1993- | cualquier cargamento | 120 | 295 | 4 |
| Eurocopter 120B Colibri | 1998- | pasajeros | 48 | 210 | 3 |
| Kaman K-MAX | 2005- | cualquier cargamento | 60 | 190 | 3 |
| Airbus H225 Super Puma | 2013- | pasajeros | 48 | 288 | 3 |
| NextGen VTOL | 2030- | pasajeros | 56 | 610 | 4 |

## Conviene saber

- **Los aviones pequeños siguen siendo útiles hasta el final.** El DHC-8, su versión de carga y el Sukhoi Superjet 100 son pequeños, así que les basta un aeródromo.
- **Antes de 1952 no hay ningún avión grande**, así que un aeropuerto temprano todavía no da acceso a aeronaves mayores.
- Los aviones vuelan en línea recta y el pago solo cuenta la distancia en línea recta, así que un desvío no les cuesta nada más ([Ingresos por cargamento y tiempo de entrega](income.html)).
- La longitud mínima de pista, las rutas de vuelo y el aterrizaje los decide el motor del juego; los scripts no los muestran.

```check
official: "It can be used by small airplanes." (Airfield) "It can be used by small and large airplanes." (Airport), build menu descriptions.
scripts: Igual: las terminales de aeródromo solo admiten SMALL_AIRCRAFT, las de aeropuerto AIRCRAFT y SMALL_AIRCRAFT, helicópteros en el edificio principal del aeropuerto, helipuerto y helisuperficie desde 1950, segunda pista desde 1980, hangares de 5; 15 aviones pequeños y 15 grandes y 11 helicópteros en el juego base.
result: agrees
```
