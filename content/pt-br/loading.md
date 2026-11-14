---
title: Velocidade de carga e descarga
summary: O que faz um veículo carregar rápido ou devagar em uma parada: o veículo, as seções da plataforma e o estoque que entrega ou recebe a carga.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-14
fact: ×2 | seção de plataforma especializada
fact: ×0,25 | seção errada ou trem longo demais
fact: ×4 | melhor caso: plataforma e armazém especializados
---

O tempo que um veículo passa carregando ou descarregando é a sua própria velocidade de carregamento multiplicada por dois fatores: um da **plataforma** e um do **estoque** do outro lado (armazém, indústria, município).

```diagram loading_factors
```

## 1. O veículo

Cada veículo tem uma velocidade de carregamento base, mostrada na Loja de Veículos e na janela do veículo ("2.0x"). Tudo o que vem abaixo multiplica esse valor.

## 2. O fator da plataforma

Para o jogo, uma plataforma não é uma fileira de módulos: é uma **lista de seções, uma por classe de carga**, com os comprimentos de todos os módulos daquela classe somados.

```diagram loading_sections
```

| Vagões… | Fator | Fonte |
|---|---|---|
| em uma seção da sua classe (vagões a granel, seção a granel) | **×2** | `modular_station.script.lua:1042` |
| em uma seção universal | ×1 | `modular_station.script.lua:1042` |
| sem nenhuma seção da sua classe na plataforma | **×0,25** | `cargo_react_util.tl:60` |
| além do comprimento da plataforma (trem longo demais) | **×0,25** | `cargo_react_util.tl:61` |

- O fator é uma **mistura pela fração do trem**: se 3/4 dos vagões combinam e 1/4 não, o fator é ¾ × 2 + ¼ × 0,25 ≈ ×1,56 (`cargo_react_util.tl:63-70`, a mesma divisão que o jogo mostra como "Terminal Parcialmente Especializado").
- **Onde** os vagões param na plataforma não importa, só os comprimentos somados (medido no jogo).
- Rodovias: terminais de caminhão especializados dão ×2 (`modular_terminal.script.lua:2956`); as pequenas paradas de rua são sempre ×1 (`small_stops.script.lua:19`).
- Plataformas de passageiros são ×1.

## 3. O fator do estoque

Na descarga, cada unidade vai para um destinatário: um módulo de armazém, uma indústria ou um prédio do município. O estoque do destinatário tem o seu próprio fator.

| Destinatário | Fator | Fonte |
|---|---|---|
| módulo de armazém **especializado** (líquidos, a granel, plataforma, mercadorias) | **×2** | `modules.script.lua:120`, `warehouse.script.lua:297-314` |
| armazém **universal** | ×1 | `warehouse.script.lua:272-285` |
| indústria | ×1 | medido no jogo |

- Todo módulo de armazém pede ×2, mas os módulos universais só aumentam a capacidade de **um estoque universal compartilhado**, que é criado com ×1. Só os módulos especializados têm estoque próprio com ×2.
- A dica do jogo chama esse fator de "Armazém especializado: +100%" (`cargo_react_util.tl:51-54`).
- Durante uma mesma descarga o jogo atende os destinatários **em rodízio**: por isso a velocidade muda enquanto o trem descarrega quando parte da carga vai para um armazém e parte para uma indústria (medido no jogo).

```engine
Qual destinatário recebe cada unidade, e a multiplicação final, são decididos no motor. Os fatores acima são os dados que os scripts entregam a ele; o resultado foi conferido com os valores que o motor expõe (sonda do [Detalhes das plataformas (Platform Details)](https://mod.io/g/transportfever3/m/platform-details), outubro de 2026).
```

## O que o jogo mostra

- O indicador de carregamento aparece como **acelerado** acima de ×1,5 e como **lento** abaixo de ×0,75 (`cargo_react_util.tl:119-122`).
- Passe o mouse sobre ele: a dica lista "Terminal Especializado", "As especializações não correspondem", "Terminal pequeno demais" e "Armazém especializado", cada um com a sua porcentagem (`cargo_react_util.tl:76-99`).

## Exemplo

Um trem de 8 vagões a granel, com 160 m, descarregando carvão.

| Estação | Plataforma | Destinatário | Fator |
|---|---|---|---|
| plataforma universal de 160 m | ×1 | usina siderúrgica | **×1** |
| plataforma a granel de 160 m | ×2 | usina siderúrgica | **×2** |
| plataforma a granel de 160 m | ×2 | armazém a granel especializado | **×4** |
| plataforma a granel de 160 m | ×2 | armazém universal | **×2** |
| plataforma universal de 120 m (trem 40 m longo demais) | ¾ × 1 + ¼ × 0,25 ≈ ×0,81 | usina siderúrgica | **×0,81** |

## Bom saber

- Estações dentro de uma indústria são sempre especializadas na carga de que a indústria precisa (wiki oficial).
- Módulos de armazém especializados também congelam o prazo de entrega da carga que guardam (wiki oficial); um armazém universal não.
- O [Detalhes das plataformas (Platform Details)](https://mod.io/g/transportfever3/m/platform-details) mostra os dois fatores de cada veículo na plataforma e para onde foi a carga descarregada.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Armazéns especializados "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Seção especializada ×2, universal ×1, nenhuma seção compatível ×0,25, além da plataforma ×0,25, misturados pela fração do trem; módulo de armazém especializado ×2, armazém universal ×1.
result: refines
```
