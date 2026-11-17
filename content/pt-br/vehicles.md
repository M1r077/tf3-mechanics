---
title: Veículos: condição, idade e velocidade de carga
summary: O que significam os atributos dos veículos, como funcionam condição e idade, o que fazem pátios e estações de manutenção, de onde vêm o preço e os custos operacionais, e quando substituir um veículo.
domain: vehicles
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-16
game: 40425
fact: 5 | níveis de condição, de Muito Ruim a Muito Bom, 20 % cada
fact: 20 % | de condição dispara o aviso Condição do Veículo
fact: 6 × | o custo operacional anual base: o preço de um veículo
fact: 4 a 16 | veículos nos recursos de manutenção de um pátio ou estação de manutenção
---

Todo veículo tem atributos fixos (velocidade, capacidade, velocidade de carga, preço, custos operacionais, vida útil) e dois valores que mudam: sua **condição** e sua **idade**. A condição cai enquanto ele roda e é restaurada pela manutenção. A idade só aumenta.

## Os atributos na loja de veículos

- A loja mostra cada atributo como uma barra. A barra usa uma escala fixa por tipo de transporte, que muda com o ano (por exemplo velocidade de carga dos navios: 10 a 45 a partir de 2003). Ela não compara o veículo com outros veículos (`vehicle_util.tl:210-245`, `vehicle_util.tl:259-268`).
- Para um trem, a loja mostra a **maior** velocidade de carga entre todas as suas partes (`vehicle_store_util.tl:333`).
- Um veículo cujo arquivo não define velocidade de carga, ruído, poluição ou conforto recebe um valor calculado a partir dos outros atributos (ano, velocidade, potência, peso, tamanho) (`model_metadata_util.lua:395-417`, `vehicle_metadata_util.lua:233-256`). A velocidade de carga calculada é arredondada para 0,5 e nunca fica abaixo de 1 (`vehicle_metadata_util.lua:267-269`).

## Qual veículo carrega mais rápido?

A velocidade de carga do veículo é só o primeiro fator; a plataforma e o estoque a multiplicam (veja [Velocidade de carga e descarga](loading.html)).

| Tipo de transporte | Velocidade de carga mostrada como barra cheia (última era) | Fonte |
|---|---|---|
| Navios | 10 a 45 (a partir de 2003) | `vehicle_util.tl:219-223` |
| Veículos rodoviários, bondes | 0,5 a 10 (a partir de 1995) | `vehicle_util.tl:232-243` |
| Trens | 0,1 a 10 (a partir de 1981) | `vehicle_util.tl:226-229` |
| Aeronaves | 1 a 4 (a partir de 1978) | `vehicle_util.tl:212-216` |

- Os navios têm de longe as maiores velocidades de carga, as aeronaves a menor escala.
- Compare veículos de um mesmo tipo de transporte na loja pela coluna de velocidade de carga; modelos mais novos costumam ficar mais altos na barra.
- Toda carga tem fator de carga 0,0625, passageiros 1 (`coal.cargo.lua:29`, `passengers.cargo.lua:23`).

```engine
Como a velocidade de carga do veículo, o fator de carga da carga e os fatores de plataforma e estoque se combinam no tempo real de carga é calculado pelo motor. Os scripts só fornecem as entradas.
```

## Condição

| Condição | Nível | Fonte |
|---|---|---|
| acima de 80 % | **Muito Bom** | `vehicle_util.tl:159-172` |
| 60–80 % | **Bom** | `vehicle_util.tl:159-172` |
| 40–60 % | **Medíocre** | `vehicle_util.tl:159-172` |
| 20–40 % | **Ruim** | `vehicle_util.tl:159-172` |
| até 20 % | **Muito Ruim** | `vehicle_util.tl:159-172` |

- A condição de um trem é a **média** de todos os seus vagões e locomotivas (`vehicle_util.tl:285-295`).
- Um veículo desgastado perde velocidade máxima, potência e conforto, e ganha ruído, poluição e custos operacionais (`vehicle_store_util.tl:236-258`). Quanto, e a partir de qual condição, são valores do motor do jogo. A janela do veículo lista essas penalidades em **Condição**.
- A força dessas penalidades é definida por **Efeito da Manutenção do Veículo** (Nenhum, Baixo, Médio, Alto, Muito Alto); com Nenhum, a condição não tem efeito (`difficulty_util.tl:42`, `mod.script.tl:241-245`, `vehicle_store_util.tl:166-168`, `vehicle_store_util.tl:216-228`). Detalhes: [Custos, manutenção e empréstimos](costs.html).
- Com **20 %** ou menos você recebe o aviso **Condição do Veículo**. Ele fica até o veículo voltar acima de **30 %** (`notifications.script.tl:310-318`).
- Um veículo clonado é uma compra nova: condição 100 %, nova data de compra (`manager_window.tl:8502-8506`).

```engine
A rapidez com que a condição cai, quanto uma visita a uma estação de manutenção restaura e o tamanho de cada penalidade (getMaintenanceTopSpeedPenalty e as outras) são valores do motor. Cada modelo de veículo também pode definir sua própria penalidade de velocidade máxima por nível (`vehicle_store_util.tl:250-253`).
```

## Pátios e estações de manutenção

Os veículos recebem manutenção de um pátio ou estação de manutenção próxima. Cada um atende um número limitado de veículos: seus **Recursos de Manutenção**.

| Edifício | Recursos de manutenção | Raio | Veículos guardados | Fonte |
|---|---|---|---|---|
| Pátio ferroviário | 6 | 800 m | 5 | `rail_depot.script.lua:341-349` |
| Estação de manutenção ferroviária | 12 | 800 m | – | `rail_maint_station.script.lua:151-157` |
| Pátio rodoviário, pátio de bondes | 12 | 400 m | 10 / 8 | `road_depot.script.lua:189-198`, `tram_depot.script.lua:217-226` |
| Estação de manutenção rodoviária | 16 | 600 m | – | `road_maint_station.script.lua:234-240` |
| Estaleiro | 8 | 1000 m | 5 | `water_depot.script.lua:370-379` |
| Estação de manutenção de navios | 12 | 1400 m | – | `water_maint_station.script.lua:256-262` |
| Hangar de aeródromo ou aeroporto | 16 | 550 m | 5 | `af_hangar.module.lua:272-280`, `ap_hangar.module.lua:455-463` |
| Heliporto | 4 | 800 m | 5 | `heliport.script.lua:300-309` |

- A janela do edifício mostra "usados / recursos" (por exemplo 14 / 12) e a lista de veículos atendidos, com sua condição (`entity_window_util.tl:2010-2039`, `maintenance_station_eow.script.tl:188-215`).
- Recursos mais ocupados deixam o edifício mais barulhento e mais poluente: as emissões sobem com a parcela em uso (`emissions.script.tl:223-234`).
- Uma estação de manutenção ferroviária atende o dobro de trens de um pátio ferroviário: 12 contra 6.
- As estações de manutenção não compram nem guardam veículos, mas seu raio costuma ser maior que o do pátio: 600 m contra 400 m nas estradas, 1400 m contra 1000 m para navios. Os bondes recebem manutenção do pátio de bondes e da estação de manutenção rodoviária; o pátio rodoviário não faz a manutenção dos bondes (`tram_depot.script.lua:209`, `tram_depot.script.lua:226`).
- A wiki oficial sugere pontos de passagem para fazer os veículos passarem por um edifício de manutenção.

```engine
A qual estação um veículo é atribuído, o que acontece quando mais veículos usam uma estação do que seus recursos e o raio de cobertura usado são decididos pelo motor.
```

## Preço e custos operacionais

- Os veículos do jogo base não têm preço fixo: os custos operacionais vêm da velocidade e da capacidade, e o preço é **6 ×** o custo operacional anual base, antes das configurações Custos de Veículo e Manutenção de Veículos (`model_metadata_util.lua:548-549`). Dá exatamente 6 anos de custos operacionais só quando as duas configurações são iguais. Fórmula completa: [Custos, manutenção e empréstimos](costs.html).
- **Custos de Veículo** escala os preços de 50 % a 150 % (`post_run_util.tl:54-81`), e **Manutenção de Veículos** escala os custos operacionais do mesmo jeito. Medido no jogo nos 921 veículos de um jogo salvo, carregado a 75 %, 100 % e 125 %: os custos operacionais seguem o controle deslizante (mediana ×0,75 e ×1,25; veículos cujo estado mudou entre os carregamentos variam um pouco).
- Um veículo em má condição paga mais custos operacionais, além do valor base (`vehicle_store_util.tl:256-259`).

## Idade e vida útil

- Cada modelo tem uma **vida útil** (`vehicle_util.tl:31-34`). A coluna **Idade** da janela da linha mostra a idade; sua dica mostra o tempo restante, ou **Vida útil alcançada** (`line_eow.script.tl:133-147`). A parcela da vida útil nessa dica mostra **0%** até a vida útil ser alcançada: o script arredonda a fração para baixo antes de mostrá-la (`line_eow.script.tl:139`), enquanto a mesma parcela é calculada por inteiro em outro lugar (`vehicle_util.tl:311`). Use o tempo restante.
- Para um trem, conta a parte **mais antiga** (`vehicle_util.tl:36-52`). Um vagão velho faz o trem inteiro aparecer como velho.

```engine
O que muda ao atingir a vida útil (por exemplo perda de condição mais rápida ou menor valor de venda) não está nos scripts. Os scripts só exibem idade e vida útil.
```

## Quando devo substituir veículos velhos?

1. **A condição continua baixa** mesmo com uma estação de manutenção por perto: o veículo perde velocidade e paga mais custos operacionais. Verifique primeiro os recursos da estação: podem estar cheios.
2. **Vida útil alcançada** na dica de Idade: o modelo passou da vida planejada.
3. **Existe um modelo melhor**: veículos mais rápidos ou maiores custam mais para operar, mas transportam mais (o preço segue velocidade × capacidade).
4. Use **Substituir Veículos** no gerenciador de linhas. Ele abre a loja com uma comparação com o veículo atual (`vehicle_store_window.tl:4893-4928`, `vehicle_store_window.tl:2611`).

```tip scripts
**Veículos continuam em mau estado perto de um pátio? Abra a janela dele e veja "usado / capacidade".** Um pátio ferroviário atende 6 trens; uma estação de manutenção ferroviária, 12. O que o motor faz com os veículos acima da capacidade não está nos scripts; um segundo prédio é a resposta segura.
```

## Bom saber

- Construa capacidade de manutenção suficiente: um pátio ferroviário atende só 6 trens.
- Com **Efeito da Manutenção do Veículo** em Nenhum, a condição não importa.
- **Enviar ao Pátio** manda um veículo para o pátio alcançável mais próximo, não para aquele onde foi comprado (wiki oficial).
- [Vehicle Comparison](https://mod.io/g/transportfever3/m/vehicle-comparison) ajuda a comparar modelos antes de substituí-los.

```check
official: "This section shows how well the vehicle is maintained and how the maintenance state affects the vehicle properties." "Loading speed modifies a vehicle's base loading speed which can be seen in the vehicle window or in the vehicle store." ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles))
scripts: Cinco níveis de condição de 20 %; penalidades de velocidade, potência, conforto, emissões e custos operacionais abaixo de 80 %, escaladas por Efeito da Manutenção do Veículo; aviso em 20 %, removido acima de 30 %. Recursos de manutenção de 4 a 16 veículos por edifício. Preço = 6 anos de custos operacionais. Idade de um trem = sua parte mais antiga. Velocidades de carga ausentes são calculadas a partir dos outros atributos, arredondadas para 0,5, no mínimo 1.
result: refines
```
