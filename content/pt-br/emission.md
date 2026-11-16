---
title: Poluição e barulho
summary: O que emite barulho e poluição, quando um edifício emite mais, como as cidades avaliam isso e o que a Ecologização industrial e a Estação de Limpeza fazem de verdade.
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
fact: 65–80 dB | barulho na cidade: avaliação máxima em 65, zero em 80
fact: 60–74 | poluição na cidade, na escala logarítmica dos scripts (não é um nível sonoro): avaliação máxima em 60, zero em 74
fact: −80 % | barulho e poluição de uma indústria ecologizada
fact: 700 m | alcance da Estação de Limpeza
---

Veículos, trilhos, ruas, estações, garagens, armazéns e indústrias emitem **barulho** e **poluição**. Duas avaliações da cidade, **Barulho** e **Poluição**, comparam o que chega à cidade com limites fixos. Uma avaliação ruim reduz a avaliação da **Autoridade do Município** e, assim, o crescimento (veja [Cidades](towns.html)).

## Quando um edifício emite mais

Um script do jogo define a emissão de quatro tipos de edifício a cada poucas atualizações, entre um nível calmo e um movimentado (`emissions.script.tl:12-18`):

| Edifício | Emite mais quando | Fonte |
|---|---|---|
| **Indústria** | produz, e de novo a cada impulso (carga ou trabalhadores); menos, em direção ao nível parado, quando seu estoque de saída está cheio | `emissions.script.tl:152-194` |
| **Estação** | está mais movimentada: pessoas e carga esperando em relação à capacidade | `emissions.script.tl:211-222` |
| **Garagem**, **estação de manutenção** | mais veículos usam sua manutenção | `emissions.script.tl:223-234` |
| **Armazém** | seus estoques estão mais cheios | `emissions.script.tl:237-250` |

- Cada indústria tem seus próprios quatro níveis: parada, produzindo, com um impulso, com dois impulsos (`industryutil.lua:464-475`; o padrão 0 / 78 / 84 / 88 só vale para uma indústria sem os seus). A maioria emite um pouco mesmo parada: uma mina de carvão vai de 2 → 10 → 20 → 30 de poluição, seus campos 2 → 30 → 60 → 90 (`coal_mine.con.lua:99-135`, veja [Indústrias](industries.html)).
- Uma indústria cuja produção não é recolhida volta ao nível parado: atendê-la aumenta sua poluição.
- Veículos e trilhos também emitem; um veículo em mau estado emite mais com a configuração **Efeito da Manutenção do Veículo** (veja [Custos, manutenção e empréstimos](costs.html)).

## O que o menu de construção mostra

| Edifício | Barulho | Poluição | Fonte |
|---|---|---|---|
| Porto | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| Aeroporto | 8–56 | 80–560 | `airport.tl:28-29` |
| Estação de trem | 25 | 45–350 | `modular_station.con.lua:97-98` |
| Garagem ferroviária | 50 | 100 | `rail_depot.con.lua:32-33` |
| Garagem rodoviária e de bonde | 40 | 80 | `road_depot.con.lua:30-31`, `tram_depot.con.lua:32-33` |
| Estação de metrô | 40 | 80 | `underground_station.con.lua:75-76` |
| Estação de caminhões e ônibus | 1–10 | 12–76 | `modular_terminal.con.lua:67-68` |
| Estações de manutenção | 20 | 40–50 | `road_maint_station.con.lua:30-31`, `rail_maint_station.con.lua:30-31` |
| Armazém | 20 | 50 (universal) ou 100 (especializado) | `warehouses/warehouse.tl:51`, `warehouses/warehouse.tl:73-74` |

Dois valores são a faixa mostrada pelo menu, do mais baixo ao mais alto, como a faixa de preço ao lado (`construction_desc_react_util.tl:733-746`); um valor é um número único. Em funcionamento, cada prédio emite mais quanto mais movimentado está (tabela acima). Mantenha portos, aeroportos e grandes estações de carga longe das casas.

## Como uma cidade avalia

| Avaliação | Medido | Avaliação máxima | Zero | Fonte |
|---|---|---|---|---|
| **Barulho** | barulho nos edifícios da cidade | 65 dB ou menos | 80 dB | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Poluição** | poluição média por célula de 16 m da área da cidade (área contada entre 5 e 10 km²), convertida para a escala logarítmica dos scripts ("dB") | 60 ou menos | 74 | `town_util.tl:413-431`, `emission_config.tl:23-30` |

- Só o distrito **residencial** sofre com o barulho; edifícios comerciais e industriais não (wiki oficial). A janela de uma casa mostra o barulho na sua posição (`town_building.tl:165-183`).
- A poluição é tirada como média de toda a área, então uma fonte longe do centro pesa menos numa cidade grande do que numa pequena.
- As configurações **Sensibilidade de Barulho** e **Sensibilidade de Poluição** deslocam os limites: o dobro da sensibilidade conta como +3 dB (`town_util.tl:426-428`, `town_util.tl:439-441`). A poluição usa a mesma escala logarítmica do barulho (10·log10): +3 "dB" significa o dobro de poluição. Não é um nível sonoro.

| Nível | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Fonte |
|---|---|---|---|---|---|---|---|---|
| Barulho | Desligado (sempre máxima) | ×¼ | ×½ | ×1 | ×1,4 | ×1,8 | ×3,5 | `difficulty_util.tl:48` |
| Poluição | Desligado (sempre máxima) | ×¼ | ×½ | ×1 | ×1,7 | ×3 | ×5 | `difficulty_util.tl:49` |

As predefinições Fácil, Médio, Difícil e Muito difícil usam os níveis 3, 4, 5 e 6 (`difficulty_util.tl:114-115`, `difficulty_util.tl:142-143`, `difficulty_util.tl:169-170`, `difficulty_util.tl:196-197`).

## Ecologização industrial

| | | Fonte |
|---|---|---|
| Efeito | barulho e poluição da indústria ×0,2 (−80 %), para sempre | `emission_config.tl:32`, `emissions.script.tl:184-192` |
| Usos | um na classificação da empresa 3, 6, 9, 12 e 15 | `industry_greenify_tool.script.tl:99-104` |
| Limite | uma vez por indústria; uma segunda tentativa não gasta licença | `company.script.tl:489-494` |

- O efeito está ligado àquela versão da indústria: quando a indústria é reconstruída, ele se perde (`emissions.script.tl:187-190`).
- Melhor uso: a indústria mais movimentada bem ao lado de uma cidade, já que uma indústria impulsionada emite mais.

## A Estação de Limpeza

Uma vantagem da empresa que remove a poluição ao seu redor.

| | | Fonte |
|---|---|---|
| Preço | 100.000.000 | `pollution_cleanup_facility.script.lua:560` |
| Manutenção por ano | 10.000.000 | `pollution_cleanup_facility.script.lua:561` |
| Disponível | 15 na classificação da empresa 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Precisa de | **Máquinas**: 8 por ciclo, dois ciclos por ano; 20 trabalhadores | `pollution_cleanup_facility.con.lua:43-60` |
| Alcance | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| Estado | Poluição | Barulho | Fonte |
|---|---|---|---|
| parada (sem máquinas) | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| funcionando | −10.000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| impulsionada uma vez | −20.000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| impulsionada duas vezes | −40.000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

- Sem máquinas ela quase não faz nada: precisa ser abastecida como uma indústria.
- Ela é barulhenta: construa-a fora do distrito residencial, a até 700 m da área poluída.
- Seu fator de impulso por trabalhadores é ×2 (`pollution_cleanup_facility.script.lua:549`). Veja [Trabalhadores](workers.html).

## Bom saber

- Abra a janela da cidade ou as camadas de barulho e poluição para ver a avaliação e os pontos críticos.
- Um estoque de saída cheio baixa a emissão de uma indústria em direção ao nível parado, mas custa a sua carga: é melhor mover a cidade do que deixar a indústria sem atendimento.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) e [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) ajudam a encontrar as estações mais movimentadas.

```engine
O motor calcula os mapas de barulho e poluição, como os valores se espalham, as emissões de veículos e trilhos e quando uma indústria é reconstruída. O script só define o nível de cada edifício e os limites da cidade.
```

```check
official: "Noise reflects noise levels in residential areas." "Pollution reflects pollution levels across the town area." O distrito residencial "is sensitive to noise"; o distrito comercial "is robust against the influence of noise". ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Avaliação de barulho 65 → 80 dB, poluição 60 → 74 dB em média sobre 5–10 km²; a sensibilidade soma 10·log10 dB; indústrias, estações, garagens e armazéns emitem mais quando movimentados; um estoque de saída cheio baixa a emissão de uma indústria em direção ao nível parado; ecologização −80 %, uma vez por indústria; a Estação de Limpeza remove até 40.000 de poluição num raio de 700 m e precisa de máquinas.
result: refines
```
