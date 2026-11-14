---
title: Custos, manutenção e empréstimos
summary: O que as configurações de custos mudam, quais custos crescem com o ano do calendário, como o preço dos veículos é calculado e quanto um empréstimo custa de verdade.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: ×6 | fator de ano na manutenção de armazéns, portos e aeroportos em 2020
fact: 6 anos | de custos operacionais: o preço de um veículo
fact: uma vez | a taxa de um empréstimo é aplicada ao valor, não a cada ano
fact: 4 | empréstimos ao mesmo tempo
---

A configuração **Inflação** não aumenta nenhum custo: ela só baixa a sua renda conforme o ranque da empresa sobe (veja [Renda por carga](income.html)). Os custos crescem com o **ano do calendário**, e quatro controles deslizantes os escalam desde o início.

```diagram cost_years
```

## As configurações de custos

| Configuração | Valores | Predefinições Fácil · Normal · Difícil · Muito Difícil | Fonte |
|---|---|---|---|
| **Custos de Veículo**, **Manutenção de Veículos** | 50% · 75% · 100% · 125% · 150% | 50% · 100% · 125% · 150% | `difficulty_util.tl:39`, `difficulty_util.tl:98-99`, `difficulty_util.tl:125-126` |
| **Custos de Infraestrutura**, **Manutenção de Infraestrutura** | 50% · 75% · 100% · 125% · 150% | 50% · 100% · 125% · 150% | `difficulty_util.tl:100-101`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Efeito da Manutenção do Veículo** | Nenhum ×0 · Baixo ×0,5 · Médio ×1 · Alto ×1,5 · Muito Alto ×2 | Baixo · Médio · Alto · Muito Alto | `difficulty_util.tl:42`, `difficulty_util.tl:103`, `difficulty_util.tl:185` |
| **Inflação** | só a renda, veja [Renda por carga](income.html) | Baixa · Normal · Alta · Muito Alta | `difficulty_util.tl:50`, `mod.script.tl:694-697` |

- **Custos de Infraestrutura** escala o preço de ruas, trilhos, pontes, túneis, cruzamentos, prédios e módulos, e também das obras no terreno (`post_run_util.tl:23-52`, `post_run_util.tl:83-120`, `construction.script.tl:31-35`, `mod.script.tl:223-226`). **Manutenção de Infraestrutura** escala a manutenção deles (`post_run_util.tl:43-45`, `post_run_util.tl:105-112`, `entity_window_util.tl:186`).
- **Custos de Veículo** e **Manutenção de Veículos** escalam o preço de compra e os custos operacionais de cada veículo (`post_run_util.tl:54-81`).
- **Efeito da Manutenção do Veículo** define o quanto um veículo em mau estado perde velocidade, potência e conforto e ganha ruído, poluição e custos operacionais (`mod.script.tl:241-245`).

## O que cresce com o ano do calendário

- **Manutenção de prédios**: ×1 em 1900, ×1,5 em 1920, ×2,2 em 1940, ×3,2 em 1960, ×4 em 1980, ×5 em 2000, ×6 em 2020 (`mod.script.tl:92-100`). A janela do prédio e o menu de construção aplicam isso a cada prédio marcado para seguir o ano, e o menu de construção marca estes: armazéns, aeródromos, aeroportos e portos (`entity_window_util.tl:186-193`, `construction_react_util.tl:1149`, `warehouse.tl:7`, `harbor_modular.tl:24`).
- Os **módulos** adicionados a um prédio assim custam o preço do ano em que o prédio foi construído, e a manutenção deles segue o ano atual (`construction.tl:3720-3727`, `construction.tl:4364-4367`).
- **Variantes por era**: pátios, edifícios de manutenção, armazéns, estações, portos e aeroportos têm uma variante por era, e cada variante seguinte custa **×3** (era B) ou **×9** (era C) da primeira (`rail_depot.con.lua:7`, `warehouse.tl:48`, `modular_station.con.lua:71`, `harbor_modular.tl:76`, `airport.tl:8`).
- **Dinheiro dos subsídios**: ×1 em 1900 até ×4 a partir de 2000 (`finances_util.tl:87-90`). **Valor dos empréstimos**: ×0,4 em 1900 até ×2,4 em 2020 (`loan_util.tl:7-10`).
- A **renda** não tem nenhum fator de ano (`cargo_income.script.lua:10-13`).

```engine
A manutenção cobrada de verdade, e se ruas, trilhos e veículos também seguem a tabela de anos, é decidida pelo motor (getCostMultiplierForYear; a configuração base só define chargeMaintenanceInterval = 60, mod.script.tl:105). Os scripts só calculam os valores mostrados nas janelas e no menu de construção, com a tabela acima. Nenhum script liga a marca "seguir o ano" dos outros prédios.
```

## Trilhos, estradas e prédios

Os arquivos de ruas e trilhos dão o preço e a manutenção anual por metro; o menu de construção os mostra por quilômetro (`construction_react_util.tl:2463`, `construction_react_util.tl:2477-2485`). Na maioria dos tipos, a manutenção é **um sexto** do preço de construção:

| Tipo | Disponível desde | Construção por km | Manutenção por km e ano | Fonte |
|---|---|---|---|---|
| Trilho simples | início | 60.000 | 10.000 | `simple.street_template.lua:9`, `simple.street_template.lua:33` |
| Trilho padrão | 1930 | 180.000 | 30.000 | `standard.street_template.lua:11`, `standard.street_template.lua:35` |
| Trilho de alta velocidade | 1980 | 540.000 | 90.000 | `high_speed.street_template.lua:11`, `high_speed.street_template.lua:35` |
| Estrada rural antiga pequena | início | 60.000 | 10.000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:58` |
| Rua urbana moderna grande | 1940 | 540.000 | 90.000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:91` |

- A catenária soma **30%** do preço do trilho; uma faixa de ônibus, 10%; um trilho de bonde, 20%; um trilho de bonde elétrico, 40% do preço da rua (`mod.script.tl:24-28`).
- Subir o terreno custa 4,5 por m³, baixá-lo 5,25 por m³, remover um campo 200.000 (`mod.script.tl:20-22`, `mod.script.tl:33`).
- Um prédio que não define manutenção paga **um sexto do seu preço** por ano (`construction.script.tl:25-27`).
- A configuração base define um fator de reembolso na demolição de 0,75 e um tempo de reembolso de 60 (`mod.script.tl:30-31`): demolir o que você acabou de construir devolve a maior parte do dinheiro. Quem aplica isso é o motor.

Manutenção anual escrita nos arquivos, para a primeira variante (antes de 1940) e as seguintes; os armazéns recebem ainda o fator de ano acima:

| Prédio | Primeira variante | ×3 (desde 1940) | ×9 (desde 1980) | Fonte |
|---|---|---|---|---|
| Pátio de Trens, Pátio de Navios | 100.000 | 300.000 | 900.000 | `rail_depot.con.lua:34`, `water_depot.con.lua:32` |
| Pátio Viário | 30.000 | 90.000 | 270.000 | `road_depot.con.lua:32` |
| Pátio de Bondes | 20.000 | 60.000 | 180.000 | `tram_depot.con.lua:34` |
| Edifício de Manutenção de Trens ou de Navios | 40.000 | 120.000 | 360.000 | `rail_maint_station.con.lua:32`, `water_maint_station.con.lua:32` |
| Edifício de Manutenção Viária | 10.000 | 30.000 | 90.000 | `road_maint_station.con.lua:32` |
| Armazém universal | 25.000 | 75.000 | 225.000 | `warehouse.tl:48-52`, `warehouse.tl:75` |
| Armazém especializado | 50.000 | 150.000 | 450.000 | `warehouse.tl:51`, `warehouse.tl:75` |

Construir cada um desses prédios custa **6 ×** a sua manutenção (`rail_depot.con.lua:35`, `warehouse.tl:76`): 2,7 M para um armazém especializado da última era, antes do fator de ano.

- O primeiro **aeródromo** (até 1950) já usa o ×3 da segunda era: o teste dele lê o ano final da variante em vez do ano inicial (`airfield.tl:8`, `airfield_era_a.metacon.tl:3`).

## Veículos

Nenhum veículo do jogo base tem preço fixo: o jogo o calcula a partir da velocidade e da capacidade do veículo quando carrega o modelo (`model_metadata_util.lua:488-552`):

1. **Custos operacionais por ano** = cerca de 675 × velocidade média (m/s) × capacidade / 4 (`model_metadata_util.lua:499-518`). O 675 vem da renda média por km, reduzida para deixar margem às viagens de volta vazias, à compra e à queda do preço das passagens (`model_metadata_util.lua:500-508`).
2. A **velocidade média** é menor que a velocidade máxima: para veículos viários (velocidade máxima em km/h)^0,78 + 4, para trens ^0,86 + 10, para navios 65% da velocidade máxima (`model_metadata_util.lua:448-474`).
3. **Trens**: um vagão conta metade da sua capacidade; uma locomotiva conta também potência ÷ velocidade máxima (km/h) × 12,5 como capacidade, também pela metade (`model_metadata_util.lua:511-512`, `model_metadata_util.lua:526-540`). Uma locomotiva forte e lenta é cara.
4. **Preço** = **6 ×** os custos operacionais anuais (`model_metadata_util.lua:548-549`).

Exemplo a 100%: um ônibus de 35 km/h para 48 passageiros custa cerca de 45.000 por ano para rodar e cerca de 270.000 para comprar.

- O estado de um veículo tem cinco níveis (100–80%, depois a cada 20%) (`vehicle_store_util.tl:231-234`); a **20%** o jogo avisa até ele voltar para acima de 30% (`notifications.script.tl:310-318`).

```engine
A velocidade com que o estado de um veículo cai, o quanto os custos operacionais sobem com isso e se os preços dos veículos mudam com o ano são valores do motor (getMaintenanceRunningCostPenalty e as outras penalidades); os scripts só os escalam com o Efeito da Manutenção do Veículo.
```

## Empréstimos

```diagram loan_interest
```

| Tipo | Valor por volta de 1960 (×0,4 em 1900, ×2,4 em 2020) | Prazo | Taxa | Fonte |
|---|---|---|---|---|
| Pequeno | 5–10 M | 1–5 anos | 3–5% | `loan_util.tl:12-22` |
| Médio | 15–25 M | 3–8 anos | 5–8% | `loan_util.tl:24-34` |
| Grande | 30–50 M | 5–12 anos | 8–10% | `loan_util.tl:36-46` |
| Muito grande | 40–60 M | 10–24 anos | 10–12% | `loan_util.tl:48-58` |

- O cartão chama de **Taxa de Juros Anual**, mas a taxa é aplicada **uma vez só** ao valor: o total de juros é valor × taxa, seja qual for o prazo. Ele é pago em partes iguais todo mês junto com o principal (`loan_util.tl:102-111`, `loan_util.tl:126-136`, `loan.script.tl:83-99`). Por isso um empréstimo longo custa menos por ano que um curto com a mesma taxa.
- **Pagar** quita só o resto do principal: os juros restantes são cancelados (`loan.script.tl:171-190`). O botão exige esse valor em caixa (`finances_loan_gui.tl:284-286`).
- As taxas **não** dependem da dificuldade: cada tipo tem a sua própria faixa fixa (`loan_util.tl:12-58`).
- No máximo **4 empréstimos** ao mesmo tempo (`loan_util.tl:4`, `loan.script.tl:134`). Uma oferta é trocada depois de meio ano; o espaço de um empréstimo que você pegou fica vazio de 4 a 8 meses (`loan.script.tl:61-76`, `loan.script.tl:150`).
- No começo de uma partida, cada um dos quatro espaços recebe os valores de um tipo sorteado, então a primeira oferta "pequena" pode ser um empréstimo grande; quando uma oferta é renovada, cada espaço oferece o seu próprio tipo (`loan_util.tl:60-74`, `loan.script.tl:63-75`).

## Bom saber

- Pegue o empréstimo **mais longo** que puder: o total de juros é o mesmo, dividido em mais meses, e você pode quitar antes sem pagar o resto.
- Prédios com variantes por era custam ×3 e ×9 nas eras seguintes, e a manutenção deles continua crescendo com o ano: um armazém especializado da última era é um custo fixo alto.
- Um veículo rápido e de grande capacidade custa mais para rodar, mas também transporta mais: preço e custos operacionais seguem velocidade × capacidade, como a renda que ele pode gerar.

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: A taxa de um empréstimo depende só do tipo (3–12%), não da dificuldade, e é aplicada uma vez ao valor, dividida pelos meses do prazo; quitar antes cancela os juros restantes. A Inflação só muda a renda; a manutenção de prédios segue o ano (×1 a ×6); preço de um veículo = 6 × os seus custos operacionais anuais, ambos a partir da velocidade e da capacidade.
result: differs
```
