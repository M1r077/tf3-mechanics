---
title: Aviões, aeroportos e helicópteros
summary: Aeródromo ou aeroporto, qual avião pousa onde, terminais, a segunda pista, heliportos, e a lista de todas as aeronaves com sua carga, capacidade e velocidade.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
fact: 2 | tamanhos de avião: pequeno e grande
fact: 1950 | primeiro aeroporto e primeiros helicópteros
fact: 1980 | segunda pista
fact: 5 | aeronaves por hangar
---

Todo avião é **pequeno** ou **grande**. Um **aeródromo** recebe só aviões pequenos; um **aeroporto** recebe os dois, e helicópteros no prédio principal. Helicópteros também têm estações próprias.

```diagram air_access
```

## Aeródromo e aeroporto

- **Aeródromo**: "pode ser usado por aviões pequenos." Variantes a partir de 1920, 1950 e 1980; 1, 2 ou 3 terminais e um depósito opcional (`airfield.tl:49`, `airfield.tl:76`, `airfield_era_a.metacon.tl:3`).
- **Aeroporto**: "pode ser usado por aviões pequenos e grandes." Variantes a partir de 1950 e 1980; 2, 3 ou 4 terminais e uma direção de pouso (`airport.tl:24`, `airport.tl:80`, `airport1950.metacon.tl:3-4`).
- Terminais de aeródromo aceitam só aviões pequenos; terminais de aeroporto aceitam os dois tamanhos (`af_terminal.module.lua:715`, `ap_terminal.module.lua:897`).
- O prédio principal do aeroporto tem helipontos (`ap_main.module.lua:532`), e a partir de 1950 um aeroporto pode ganhar um terminal de helicópteros (`ap_terminal_heli.module.lua:897`, `ap_terminal_heli.module.lua:971`).
- **Segunda pista**: um módulo de aeroporto a partir de 1980 (`airport_2nd_runway.module.lua:5`). Alguns módulos de aeroporto precisam dela e mostram "2ª Pista Necessária" sem ela (`airport.script.lua:261`).
- Todas as estações aéreas recebem passageiros e todas as cargas (`airfield.tl:59`, `airport.tl:34`).

| Prédio | Passageiros esperando | Fonte |
|---|---|---|
| Terminal de aeródromo | até 250 | `af_terminal.module.lua:773` |
| Prédio principal do aeroporto | até 400 | `ap_main.module.lua:667` |
| Terminal de aeroporto | até 850 | `ap_terminal.module.lua:951` |
| Terminal de helicópteros do aeroporto | até 450 | `ap_terminal_heli.module.lua:990` |

## Hangares e estações de helicópteros

- Um **hangar** de aeródromo ou aeroporto comporta 5 aeronaves e faz a manutenção de aeronaves em um raio de 550 m (`af_hangar.module.lua:273-278`, `ap_hangar.module.lua:456-461`).
- **Heliporto** (a partir de 1950): compra e mantém helicópteros, depósito para 5, raio de manutenção de 800 m (`heliport.script.lua:301-306`).
- **Heliponto** (a partir de 1950): uma pequena plataforma de pouso para passageiros e carga, sem depósito (`helipad.con.lua:29-33`).

## Custos

Preço e manutenção da primeira variante. Variantes posteriores custam ×3 ou ×9 ([Custos, manutenção e empréstimos](costs.html)); o primeiro aeródromo já usa ×3 (`airfield.tl:8`).

| Prédio | Preço | Manutenção por ano | Fonte |
|---|---|---|---|
| Aeródromo | 1.200.000 - 3.000.000 | 50.000 - 200.000 | `airfield.tl:55-56` |
| Aeroporto | 1.800.000 - 4.500.000 | 300.000 - 750.000 | `airport.tl:30-31` |
| Módulo de aeródromo (prédio principal, terminal, hangar) | 600.000 | 100.000 | `af_main.module.lua:316-317`, `af_hangar.module.lua:326-327` |
| Módulo de aeroporto (terminal, hangar, segunda pista) | 900.000 | 150.000 | `ap_main.module.lua:672-673`, `ap_hangar.module.lua:508-509`, `airport_2nd_runway.module.lua:27-28` |

- A manutenção de aeroportos e aeródromos também segue o ano do calendário, ×1 em 1900 até ×6 em 2020 ([Custos, manutenção e empréstimos](costs.html)).
- O preço e os custos operacionais de uma aeronave são calculados a partir de sua velocidade e capacidade, como navios e veículos rodoviários ([Custos, manutenção e empréstimos](costs.html)).

## Todos os aviões

Velocidade em km/h, arredondada. "Qualquer carga" significa todo tipo de carga. A capacidade é o total mostrado na loja de veículos: a soma dos compartimentos, cada um com sua maior configuração de carga (`vehicle_store_util.tl:70-95`).

| Avião | Anos | Tamanho | Carga | Capacidade | Velocidade | Velocidade de carga |
|---|---|---|---|---|---|---|
| F 13 Herta da Junkers | 1920-1950 | pequeno | passageiros | 16 | 135 | - |
| J6860 Victoria da Vickers | 1922-1960 | pequeno | qualquer carga | 32 | 150 | 2,5 |
| Fokker F.VII | 1925-1960 | pequeno | passageiros | 32 | 175 | 2 |
| JU-52 "Iron Annie" da Junkers | 1933-1982 | pequeno | passageiros, qualquer carga | **48** (2 × 24) | 200 | 3 |
| DC-3 da Douglas | 1935-1995 | pequeno | passageiros | 56 | 300 | 2,5 |
| C-46 Commando da Curtiss | 1942-1980 | pequeno | qualquer carga | 80 | 280 | - |
| DC-4 da Douglas | 1944-1998 | pequeno | passageiros | 100 | 365 | 3 |
| Type 170 Freighter da Bristol | 1949-2005 | pequeno | passageiros, qualquer carga | **80** (2 × 40) | 350 | 1,5 |
| L-1049 Super Connie da Lockheed | 1952-1986 | grande | passageiros | 120 | 486 | 3 |
| L-1049D/H Super Connie da Lockheed | 1959-2000 | grande | qualquer carga | **120** (2 × 60) | 486 | 2,5 |
| DH.106 Comet da De Havilland | 1960-2000 | grande | passageiros | 160 | 724 | 3 |
| CL-44 Freighter da Canadair | 1962-2005 | grande | qualquer carga | **144** (3 × 48) | 645 | 2 |
| CV 990 Coronado da Convair | 1962-2020 | grande | passageiros | 200 | 917 | 2 |
| L-100 Hercules da Lockheed | 1976-2000 | pequeno | qualquer carga | **132** (3 × 44) | 400 | 3 |
| DC-10-30 da McDonnell Douglas | 1978- | grande | passageiros | 400 | 960 | 2,5 |
| DC-10-30CF da McDonnell Douglas | 1978- | grande | qualquer carga | **396** (3 × 132) | 960 | 4 |
| A310 300F Freighter da Airbus | 1982- | grande | qualquer carga | 160 | 850 | 3 |
| Short 330 Sherpa | 1984- | pequeno | passageiros, qualquer carga | **80** (2 × 40) | 455 | 2,5 |
| A320 da Airbus | 1985- | grande | passageiros | 180 | 753 | 3 |
| 146 da British Aerospace | 1985- | pequeno | passageiros | 112 | 753 | 3 |
| 146 Freighter da British Aerospace | 1985- | pequeno | qualquer carga | **96** (2 × 48) | 753 | 2 |
| Fokker 100 | 1988- | grande | passageiros | 160 | 845 | 3,5 |
| Tu-204 da Tupolev | 1995- | grande | passageiros | 280 | 850 | 4 |
| Tu-204C Freighter da Tupolev | 1995- | grande | qualquer carga | **204** (3 × 68) | 850 | 2 |
| 737-700 da Boeing | 1998- | grande | passageiros | 200 | 974 | 2,5 |
| 737-700-C Freighter da Boeing | 1998- | grande | qualquer carga | **160** (2 × 80) | 974 | 3 |
| DHC-8 da Bombardier | 2000- | pequeno | passageiros | 120 | 648 | 3 |
| DHC-8 Freighter da Bombardier | 2008- | pequeno | qualquer carga | 120 | 648 | 2 |
| Superjet 100 da Sukhoi | 2011- | pequeno | passageiros | 160 | 870 | 3 |
| Canada A220 da Airbus | 2013- | grande | passageiros | 180 | 830 | 5 |

## Todos os helicópteros

| Helicóptero | Anos | Carga | Capacidade | Velocidade | Velocidade de carga |
|---|---|---|---|---|---|
| Bell 47 | 1950-1990 | passageiros, qualquer carga | 8 | 150 | 2 |
| H-21 Workhorse da Piasecki | 1952-1985 | passageiros, qualquer carga | 80 (48 carga) | 210 | 3 |
| S-64 Skycrane da Sikorsky | 1962-2017 | qualquer carga | 40 | 213 | 4 |
| Bell 206 Long Ranger | 1965-2025 | passageiros | 32 | 241 | 2,5 |
| Vertol 234 Chinook da Boeing | 1980- | passageiros, qualquer carga | 80 | 269 | 2 |
| AW101 "Merlin" da AgustaWestland | 1990- | passageiros | 60 | 278 | 3 |
| Mil Mi-26TC | 1993- | qualquer carga | 120 | 295 | 4 |
| Eurocopter 120B Colibri | 1998- | passageiros | 48 | 210 | 3 |
| K-MAX da Kaman | 2005- | qualquer carga | 60 | 190 | 3 |
| H225 "Super Puma" da Airbus | 2013- | passageiros | 48 | 288 | 3 |
| VTOL NextGen | 2030- | passageiros | 56 | 610 | 4 |

## Bom saber

- **Aviões pequenos continuam úteis até o fim.** O DHC-8, sua versão de carga e o Superjet 100 da Sukhoi são pequenos, então um aeródromo basta para eles.
- **Antes de 1952 não há avião grande**, então um aeroporto antigo ainda não dá acesso a aeronaves maiores.
- Aviões voam em linha reta, e o pagamento conta só a distância em linha reta, então um desvio não lhes custa nada a mais ([Renda por carga e tempo de entrega](income.html)).
- O comprimento mínimo da pista, as rotas de voo e o pouso são decididos pelo motor do jogo; os scripts não os mostram.

```check
official: "It can be used by small airplanes." (Airfield) "It can be used by small and large airplanes." (Airport), build menu descriptions.
scripts: Igual: terminais de aeródromo aceitam só SMALL_AIRCRAFT, terminais de aeroporto AIRCRAFT e SMALL_AIRCRAFT, helicópteros no prédio principal do aeroporto, heliporto e heliponto a partir de 1950, segunda pista a partir de 1980, hangares para 5; 15 aviões pequenos, 15 grandes e 11 helicópteros no jogo base.
result: agrees
```
