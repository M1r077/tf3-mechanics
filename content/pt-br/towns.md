---
title: Crescimento dos municípios: XP, classificações e tamanho
summary: De onde vem o XP de um município, como as seis classificações definem a sua taxa de crescimento e quanto cada nível o aumenta.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-14
fact: 0% | de crescimento quando uma classificação está Muito Ruim
fact: ×1,5 | de XP para cada nível seguinte (1.000 para o nível 2)
fact: ×40 | de tamanho após 17 níveis ganhos
---

Um município só cresce com o **seu** transporte: os passageiros que chegam pelas suas linhas e a carga entregue aos seus prédios dão XP a ele. As classificações decidem quanto desse XP conta, e cada nível ganho deixa o município maior.

```diagram town_xp
```

## De onde vem o XP

| Origem | XP bruto | Fonte |
|---|---|---|
| Passageiro que chega **pelas suas linhas** a um prédio do município | 5 · 10 · 20: casa e emprego ou loja no mesmo município, em um município vizinho, em um município mais distante | `town_growth.script.tl:649-701`, `town_growth_config.res.lua:6` |
| Unidade de carga entregue a um prédio do município | 10 · 20 · 40 para carga de nível 0 · 1 · 2 | `town_growth.script.tl:642`, `town_growth_config.res.lua:5` |
| Recompensa de subsídio "experiência do município" | uma parte do nível atual, também × taxa de crescimento | `subvention_util.tl:144-152`, `town_growth.script.tl:608` |

- O XP vai para o município do prédio onde o passageiro ou a carga **chega**. Quem viaja todo dia entre dois municípios dá XP aos dois: ao município do emprego na ida e ao município da casa na volta.
- Viagens de ou para uma **indústria** não dão XP (`town_growth.script.tl:680-683`). Viagens a pé ou de carro também não: só contam as viagens feitas com as suas linhas (`town_growth.script.tl:656`).
- O tempo sozinho não dá nada: o XP por tick é 0 (`town_cargo_util.tl:6`).
- Níveis de carga: **0** tijolos, cimento, peixes, combustível, carne, tábuas, vegetais; **1** bebidas, livros, roupas, móveis, máquinas, comida enlatada, ferramentas; **2** veículos (`placementparamsutil.lua:506-616`).

Todo XP bruto é multiplicado pela **taxa de crescimento** do município (`town_growth.script.tl:60-63`). A janela do município mostra esse valor como **Taxa de Crescimento:**.

## A taxa de crescimento

A taxa de crescimento vem de duas classificações da janela do município (`town_util.tl:607-633`, `town_util.tl:954-962`):

1. **Autoridade do Município**: a **mais baixa** das suas seis classificações, não a média (`town_util.tl:754-784`).
2. **Suprimentos**: a média dos níveis de suprimento de passageiros e de carga, arredondada para cima (`town_util.tl:555-589`).

```diagram growth_matrix
```

- Cada classificação tem seis níveis: um valor de 0 a 1 dividido em sextos (`town_util.tl:983-985`). **Excelente** exige 5/6 = 83% ou mais.
- Com **uma única** classificação em Muito Ruim, a autoridade fica Muito Ruim e a taxa de crescimento é **0%**: o município para, não importa o que você entregue.
- 100% exige autoridade Excelente com suprimentos Muito Boa ou melhor, ou autoridade Muito Boa com suprimentos Excelente.
- A sua **Sede** soma +5% ao município mais próximo dela, e a maioria das suas extensões soma mais +5% cada (`headquarter.script.tl:510-515`, `landmark_util.tl:51-70`). Esse bônus multiplica a taxa, então não faz nada em 0%.

## As seis classificações da autoridade

| Classificação | O que a reduz | Fonte |
|---|---|---|
| **Reputação** | terraplenagem, demolição de prédios do município, remoção de árvores; cada ligação principal cortada com outro município −1/3 | `town_util.tl:396-404`, `town_util.tl:1608` |
| **Tráfego** | ruas congestionadas no município | `town_util.tl:445-456` |
| **Felicidade** | fração de viajantes insatisfeitos (no mínimo 15 pessoas consideradas) | `town_util.tl:479-503` |
| **Entrega** | fração de entregas de carga atrasadas (veja [Renda por carga](income.html)) | `town_util.tl:505-519` |
| **Barulho** | barulho do município: 65 dB ou menos → classificação cheia, 80 dB → 0 | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Poluição** | poluição média da área do município: 60 dB → cheia, 74 dB → 0 | `town_util.tl:413-431`, `emission_config.tl:23-24` |

As configurações de **sensibilidade** de cada classificação (sete níveis, o primeiro é Desligado) movem esses limites; Desligado significa classificação sempre cheia (`difficulty_util.tl:44-49`).

## Suprimentos

- **Passageiros**: uso das linhas do município × 2, então **50% de uso das linhas dá a classificação cheia** (`town_util.tl:546-553`).
- **Carga**: oferta ÷ demanda de cada distrito (comercial, industrial); conta o **melhor** distrito, não a média (`town_util.tl:521-529`).
- Um município sem nada a ser abastecido conta como suprimentos cheios. Um município que não recebe de você nem passageiros nem carga conta como "sem entregas": taxa de crescimento 0% (`town_util.tl:565-588`).

Novas demandas de carga chegam com os níveis (`placementparamsutil.lua:618-660`): uma comercial e uma industrial no início, uma segunda comercial no nível 5, uma segunda industrial no nível 7, uma terceira comercial no nível 9 e uma terceira industrial no nível 11. Elas só são adicionadas depois que o município recebe pelo menos uma entrega de carga (`town_growth.script.tl:286-288`). O jogo prefere cargas que poucos outros municípios já pedem (`town_growth.script.tl:258-266`).

## Níveis e tamanho

- O nível 2 exige 1.000 XP, e cada nível seguinte 1,5 vez mais que o anterior (`town_cargo_util.tl:81-97`, `town_growth_config.res.lua:7`): nível 5 com 8.125 XP no total, nível 10 com cerca de 75.000, nível 18 (Metrópole Grande, o último) com cerca de 2 milhões.
- Municípios posicionados com mais casas começam mais alto: nível 2, 3 ou 4 (`town_cargo_util.tl:43-54`).
- O **tamanho-alvo** depende dos níveis ganhos desde o início, incluindo o progresso rumo ao próximo (`town_cargo_util.tl:100-110`, `town_growth_function.tl:4-11`):

```diagram town_size
```

- O tamanho extra é dividido entre os distritos residencial, comercial e industrial conforme o atendimento de cada um: uso de passageiros para as casas, oferta de carga para os outros (`town_growth.script.tl:404-421`). Quando um distrito chega a 40% do município, a parte máxima que ele pode levar do novo tamanho cai de 100% para 50% à medida que ele chega a 50% do município (limites parecidos valem para o mapa inteiro) (`town_growth.script.tl:509-522`). Se nenhum distrito for atendido, o município não cresce, mesmo com XP (`town_growth.script.tl:415`).

```engine
O motor calcula o uso das linhas, a velocidade do tráfego, os mapas de barulho e poluição e a lista de entregas atrasadas, e constrói as novas casas e ruas. A menor parte que um distrito sempre recebe (townGrowthMinDistrictFraction) é um valor do motor.
```

## Bom saber

- **Corrija primeiro a pior classificação**: a autoridade é o mínimo, então melhorar as outras não adianta nada.
- Passageiros entre **dois municípios** dão 2 vezes (vizinhos) ou 4 vezes (mais distantes) o XP das viagens dentro de um só município, e para os dois municípios.
- As cargas comerciais são só de nível 0–1; só os **veículos** (industriais) dão 40 XP por unidade, e normalmente um município só os pede a partir da sua terceira demanda industrial (nível 11).
- Um município longe da sua Sede não recebe o bônus dela: só o município mais próximo recebe.

```check
official: "A town needs 1,000 total XP to reach level 2. The XP required for each following level-up is 1.5 times the amount required for the previous level-up." Passageiros 5 / 10 / 20 XP, carga 10 / 20 / 40 XP. "The Town Authority rating is determined by the lowest of six ratings." "A line usage of 50% gives the maximum rating." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Mesmos números. Taxa de crescimento de 0 a 100% em degraus de 20% conforme autoridade × suprimentos; uma classificação Muito Ruim para o crescimento; nenhum XP por viagens a indústrias; demandas de carga adicionadas só depois de uma primeira entrega de carga; a terceira demanda comercial não pode ser de nível 2 no jogo base (não há carga comercial de nível 2); tamanho ×40 após 17 níveis ganhos.
result: refines
```
