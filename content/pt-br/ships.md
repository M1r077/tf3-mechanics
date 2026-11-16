---
title: Navios e portos
summary: Navios pequenos e grandes, qual porto recebe quais, terminais e custos dos portos, e a lista de todos os navios com sua carga, capacidade e velocidade.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
fact: 2 | tamanhos de navio: pequeno e grande
fact: 1, 2, 4 | terminais por porto
fact: 27 | navios no jogo base
fact: ×9 | preço e manutenção da variante de porto de 1990
---

Todo navio é **pequeno** ou **grande**. Um navio grande só pode atracar em um **porto grande**; um navio pequeno atraca nos dois. O guia do jogo também diz: "Atenção: navios grandes só podem atracar em portos amplos."

```diagram ship_access
```

## Portos pequenos e grandes

- Dois portos no menu de construção: **Porto de Passageiros/Carga Pequeno** e **Porto de Passageiros/Carga Grande**. Ambos recebem passageiros e todas as cargas (`harbor_modular.tl:92`, `harbor_modular.tl:122`).
- O porto pequeno é feito de píeres pequenos, que aceitam apenas navios pequenos (`small_pier.module.lua:7`). O porto grande usa píeres médios, que aceitam os dois tamanhos (`medium_pier.module.lua:6`, `harbor_modular.script.lua:35-39`).
- **Terminais**: 1, 2 ou 4, escolhidos na construção (`harbor_modular.tl:16`, `harbor_modular.script.lua:33`).
- Um terminal de píer comporta 100 passageiros esperando em um píer pequeno e 50 em um píer médio (`modules.script.lua:872`, `modules.script.lua:1004`).
- Portos devem ser colocados ao longo de uma costa, em água navegável (`harbor_modular.tl:29`).
- Cada navio define seu tamanho no próprio arquivo de veículo; o jogo o converte no modo navio pequeno ou grande (`model_metadata_util.lua:1411-1412`).

## Custos

Há uma variante de porto por era: 1900, 1950 e 1990 (`harbor_modular.tl:71-73`). Preço e manutenção são multiplicados por 3 para uma variante a partir de 1940 e por 9 para uma a partir de 1980 (`harbor_modular.tl:76`):

| Porto | Preço (primeira variante) | Manutenção por ano (primeira variante) | Fonte |
|---|---|---|---|
| Porto pequeno | 144.000 - 444.000 | 24.000 - 74.000 | `harbor_modular.tl:88-89` |
| Porto grande | 228.000 - 678.000 | 38.000 - 113.000 | `harbor_modular.tl:118-119` |

- Os dois valores são o menor e o maior layout.
- A manutenção dos portos também segue o ano do calendário, ×1 em 1900 até ×6 em 2020, como armazéns e aeroportos ([Custos, manutenção e empréstimos](costs.html)).
- Portos são barulhentos e sujos: 180 a 280 para ambos ([Poluição e barulho](emission.html)).
- O preço e os custos operacionais de um navio são calculados a partir de sua velocidade e capacidade, como veículos rodoviários e aeronaves ([Custos, manutenção e empréstimos](costs.html)).

## Todos os navios

Velocidade em km/h, arredondada. "Carga" lista as classes de carga do arquivo de veículo; "qualquer carga" significa todo tipo de carga. A capacidade é o total mostrado na loja de veículos: a soma dos compartimentos, cada um com sua maior configuração de carga (`vehicle_store_util.tl:70-95`).

| Navio | Anos | Tamanho | Carga | Capacidade | Velocidade | Velocidade de carga |
|---|---|---|---|---|---|---|
| Dunara Castle | 1875-1930 | grande | passageiros, qualquer carga | **160** (2 × 80) | 20 | 20 |
| Barco Canadense | 1884-1948 | pequeno | qualquer carga | 40 | 35 | 10 |
| Waimarie | 1889-1940 | pequeno | passageiros | 80 | 30 | 15 |
| Sydfart | 1900-1930 | pequeno | líquido, plataforma, mercadorias, granel | 80 | 30 | 20 |
| PS Trillium | 1910-1955 | grande | passageiros | 200 | 35 | 15 |
| Barco a Vapor com Rodas de Pás | 1915-1960 | pequeno | passageiros, qualquer carga | **120** (2 × 60) | 40 | 10 |
| Terra Nova | 1925-1975 | grande | granel, plataforma, mercadorias | **200** (2 × 100) | 45 | 30 |
| Rebocador de Petroleiro Votrans | 1935-1990 | pequeno | líquido | 120 | 33 | 20 |
| Rebocador Votrans | 1935-1990 | pequeno | granel, plataforma, mercadorias | 120 | 33 | 20 |
| MS Stadt Kiel | 1943-1990 | pequeno | passageiros | 80 | 30 | 20 |
| Borealis | 1948-1994 | pequeno | qualquer carga | 60 | 38 | 20 |
| Wopper | 1950-2005 | pequeno | líquido, plataforma, mercadorias, granel | 160 | 30 | 25 |
| Balsa da Meridian | 1956-2011 | pequeno | passageiros | 240 | 30 | 15 |
| Cap Arcona | 1965-2010 | grande | passageiros | 200 | 40 | 20 |
| Navio Costeiro Tora | 1970-2020 | grande | líquido, plataforma, mercadorias, granel | 320 | 40 | 25 |
| Aerodeslizador AP1-88 | 1980- | pequeno | passageiros | 240 | 90 | 15 |
| Rebocador Hercules XI | 1990- | grande | plataforma, mercadorias, granel | **240** (2 × 120) | 32 | 20 |
| Baltica | 1994- | pequeno | qualquer carga | 80 | 40 | 20 |
| Type 2000 da HADAG | 1995- | pequeno | passageiros | 100 | 35 | 25 |
| Tanker 800 da Damen | 1996- | pequeno | líquido | **320** (2 × 160) | 28 | 30 |
| Balsa Rápida da Damen | 2003- | grande | passageiros | 220 | 75 | 20 |
| Luise Deymann | 2013- | grande | líquido | **480** (2 × 240) | 30 | 35 |
| MS Diamant | 2013- | grande | passageiros | 280 | 45 | 35 |
| Rebocador Virgo | 2015- | grande | plataforma, mercadorias, granel | **320** (2 × 160) | 40 | 15 |
| Aerodeslizador GHL Oita | 2023- | pequeno | passageiros | 320 | 100 | 20 |
| Yara Birkeland | 2030- | grande | plataforma, mercadorias, granel | 480 | 42 | 10 |
| Transporte Naval Solar | 2035- | pequeno | passageiros | 80 | 30 | 30 |

## Bom saber

- **Confira o tamanho antes de construir um porto pequeno.** Vários dos maiores navios de carga (Tora, Virgo, Yara Birkeland) são grandes e não vão atracar lá.
- **"Não há caminho para navios grandes"** é um aviso separado para navios grandes: o jogo não encontrou um caminho na água que um navio grande possa usar. Qual água está aberta para qual tamanho é decidido pelo motor do jogo, não pelos scripts, que só mostram o aviso (`vehicle_warning.script.tl:28-36`).
- **Pontos de referência de navios** devem ser colocados na água ("Pontos de Referência de navios devem estar na água.").
- O estaleiro e a estação de manutenção de navios são prédios separados; a manutenção funciona em um raio ao redor deles ([Veículos: condição, idade e velocidade de carga](vehicles.html)).

```check
official: "Passenger and cargo ships are available in two sizes: small and large. Large ships can only dock at large harbors, so make sure the harbor matches the size of the ships assigned to the line." (in-game guide "Water Infrastructure")
scripts: Igual: píeres pequenos aceitam só SMALL_SHIP, píeres médios SHIP e SMALL_SHIP; ambos os portos recebem passageiros e todas as cargas; 1, 2 ou 4 terminais; três variantes de era com ×1 / ×3 / ×9; 16 navios pequenos e 11 grandes no jogo base.
result: refines
```
