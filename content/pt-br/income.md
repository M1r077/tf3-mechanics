---
title: Renda por carga e tempo de entrega
summary: Quanto uma entrega paga (distância em linha reta, subida, ranque da empresa, subsídios) e quanto um atraso custa de verdade.
domain: economy
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: 3,8 | o mesmo fator de renda para todas as cargas
fact: +8 × subida | metros de subida somados à distância
fact: 100% | pago mesmo quando a entrega atrasa
---

Uma entrega paga pela **distância em linha reta**, e nada mais da viagem. A velocidade importa por outro motivo: cada carga tem um **prazo**, e as entregas atrasadas baixam a classificação **Entrega** do município, não a sua renda.

```diagram income_formula
```

## A fórmula da renda

A fórmula inteira é um script curto do jogo (`cargo_income.script.lua:10-13`):

1. **Fator de renda** da carga. Todas as cargas do jogo base usam a mesma função e os mesmos preços (`initialPrice = 4`, `finalPrice = 3.2`), o que dá **3,8 para as 36 cargas** (`cargotype.script.lua:7-13`, `coal.cargo.lua:21-22`). O carvão paga exatamente o mesmo que as mercadorias na mesma distância.
2. Configuração **Renda por Carga**: 50%, 75%, 100%, 125% ou 150% (`difficulty_util.tl:38`, `mod.script.tl:211`). As quatro predefinições de dificuldade usam 100% (`difficulty_util.tl:97`).
3. **Distância**, veja abaixo.

A função recebe o tempo de viagem, mas **não o usa** (`cargotype.script.lua:7-13`): uma entrega lenta ou atrasada paga o mesmo.

## Distância: linha reta mais subida

```diagram income_distance
```

- A distância é a **linha reta em 3D** entre os dois pontos, não o comprimento da sua rota (`cargo_income.script.lua:3-7`).
- Quando a diferença de altura é positiva, **8 × essa altura** é somado (`cargo_income.script.lua:5`): 100 m de subida pagam como 800 m a mais. No sentido contrário, nada é descontado.
- Então uma linha cheia de curvas rende o mesmo que uma reta, mas você paga a manutenção de cada metro de trilho ou estrada que construiu.

```engine
O motor escolhe os dois pontos e os passa ao script. Medido no jogo (veja abaixo): são a **origem** da carga (a indústria ou o prédio do município que a produziu) e o **consumidor** que a recebe, como diz a wiki oficial ("between the source and the final destination").
```

## Carga que muda de linha

Quando um item viaja em várias linhas, por exemplo navio → armazém → trem, o jogo ainda o paga **uma única vez**:

```diagram income_split
```

1. Descarregar em um armazém ou em uma estação de transbordo não paga **nada**. De cerca de 17.000 pagamentos medidos, só 43 foram para um destino que não era um consumidor.
2. Quando o último veículo entrega ao consumidor, o item é pago com a fórmula acima, pela linha reta **da origem até o consumidor**. Os trechos e a rota real não contam, então um desvio por um armazém não rende nada a mais.
3. Esse dinheiro é dividido entre as linhas da cadeia **em proporção ao comprimento em linha reta de cada trecho**: de um ponto de coleta ao seguinte, e do último ponto de coleta ao consumidor. O bônus de subida não conta nessa divisão.
4. O veículo que entrega primeiro retém o valor inteiro, com uma parte por trecho. Ele é lançado alguns segundos de tempo de jogo depois (mediana de cerca de 6 s), e cada linha e cada veículo recebe a sua própria parte. Por isso o saldo de uma linha muda logo depois da entrega, não no armazém.

Então uma linha alimentadora curta até um armazém rende pouco, mesmo fazendo toda a coleta; o trecho longo fica com a maior parte. Cada linha continua mostrando a sua parte real no próprio saldo.

```engine
Os scripts só calculam o total (`economy/cargo_income.script.lua`); a divisão é feita pelo motor e não é visível nos scripts. As regras acima foram medidas com um mod de teste somente leitura: cerca de 1.700 pagamentos de itens com 2 ou 3 trechos, e as mudanças de conta de cada linha e veículo envolvidos. Em 769 casos limpos (um item, um pagamento) a divisão bateu com os comprimentos dos trechos com margem de 1% todas as vezes; uma divisão com o bônus de subida bateu em só 59% deles, e uma divisão igual em nenhum.
```

## O que mais muda o valor

| O quê | Efeito | Fonte |
|---|---|---|
| **Ranque da Empresa** com a configuração Inflação | ranque 1: ×1, caindo de forma regular até o ranque 15: ×0,9 (Baixa), **×0,75 (Normal)**, ×0,6 (Alta), ×0,5 (Muito Alta); Nenhuma: sempre ×1 | `company_progression_util.tl:25-40`, `difficulty_util.tl:50`, `mod.script.tl:694-697` |
| **Subsídio cumprido** | ×2 para entregas à indústria ou ao município do contrato, nas linhas que entregaram para o contrato | `deliver_cargo.script.tl:463-469`, `deliver_cargo_town.script.tl:554-565` |
| **Entrega atrasada** | nenhum efeito na renda | `cargotype.script.lua:7-13` |

- O multiplicador de ranque vale para **todos** os pagamentos de carga e de passageiros (`company_growth.script.tl:159-170`). As predefinições de dificuldade usam Inflação Baixa (Fácil), Normal (Normal), Alta (Difícil), Muito Alta (Muito Difícil) (`difficulty_util.tl:108`).
- O ×2 dos subsídios vale só para as linhas que entregaram durante o contrato, por um tempo limitado (wiki oficial, Subsidies).

## Passageiros

Os passageiros usam a mesma distância e um fator de renda fixo de cerca de 3,61 (`cargotype.script.lua:50-53`), multiplicado por **0,5 + o fator de preço da passagem do veículo** (`cargo_income.script.lua:14-17`). Quando um modelo de veículo não define o seu fator de conforto, o jogo define o fator de preço como 0,3 para ônibus e bondes, 0,9 para aeronaves, 0,1 para navios e 0,5 para trens (`base_mod.lua:46-61`); para os outros modelos é um valor do motor, não visível nos scripts. Um subsídio de passageiros dobra só os passageiros que viajam entre os seus dois municípios, na sua única linha (`deliver_passengers.script.tl:292-296`).

## Prazos de entrega

Cada carga tem o seu próprio prazo (`meat.cargo.lua:30`, `coal.cargo.lua:30`). Os alimentos frescos têm o mais curto, e as matérias-primas pesadas, um cinco vezes mais longo:

```diagram delivery_times
```

- **Finanças › Tempo de Entrega** mostra o prazo de cada carga no seu mapa; a Camada de Satisfação de Carga colore as rotas de verde a vermelho.
- Uma entrega conta como **atrasada** quando chega depois do prazo (`towns.script.tl:425`).
- Módulos de armazém especializados **congelam** o prazo da carga que guardam (wiki oficial, Warehouses).

```engine
O motor transforma o tempo base no prazo mostrado em Finanças (os scripts o leem com getAdjustedDeliveryTime) e decide quando um item está atrasado. Só os valores relativos acima vêm dos arquivos de carga.
```

## Quanto custa um atraso: a classificação Entrega

A carga atrasada é paga por inteiro, mas cada município mantém uma classificação **Entrega** (`town_util.tl:505-519`):

1. O jogo conta as entregas ao município no **último meio ano**, e quantas atrasaram (no mínimo 10 são consideradas, para que as primeiras entregas não a façam oscilar demais).
2. Fração no prazo → classificação: abaixo de um limite inferior a classificação é 0, acima de um limite superior é 1, linear entre os dois. Com a sensibilidade padrão (**Normal**): **30% no prazo → 0, 100% → 1**, então 90% no prazo dá 0,86.
3. A configuração **Sensibilidade de Entrega** move os limites (`difficulty_util.tl:47`). Desligado: sempre 1. Predefinições: Fácil Baixo, Normal Normal, Difícil Alto, Muito Difícil Muito Alto (`difficulty_util.tl:113`).

```diagram delivery_rating
```

Entrega é uma das seis classificações cuja mais baixa define a taxa de crescimento do município: uma única classificação Muito Ruim para o município (veja [Crescimento dos municípios](towns.html)).

## Exemplo

A mesma entrega de carvão, a 5 km em linha reta.

| Situação | Pago |
|---|---|
| terreno plano, qualquer comprimento de rota | **100%** |
| a 10 km | **200%** |
| destino 100 m mais alto | **116%** |
| entregue com atraso | **100%** (a classificação Entrega cai) |
| ranque da empresa 15, Inflação Normal | **75%** |
| entrega coberta por um subsídio cumprido | **200%** |

## Bom saber

- Como todas as cargas pagam o mesmo por quilômetro, **escolha as cargas pelo volume, pela distância e pelo prazo**, não pelo preço.
- Os prazos pesam mais para carne, peixes, vegetais e bebidas: linhas curtas, ou armazéns que congelam o prazo.
- Cada unidade entregue a um prédio do município também dá experiência a esse município (`town_growth.script.tl:642`, `town_growth_config.res.lua:5`).

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks), [Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Mesmo fator 3,8 para todas as cargas; distância em 3D mais 8 × a subida; o ranque da empresa reduz a renda até ×0,75 no ranque 15 (Inflação Normal); ×2 depois de um subsídio; o tempo não é usado na renda; medido no jogo: um item que muda de linha é pago uma única vez, no consumidor, e dividido entre as linhas pelo comprimento dos trechos; classificação Entrega pela fração no prazo do último meio ano (Normal: 30% → 0, 100% → 1).
result: refines
```
