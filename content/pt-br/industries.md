---
title: Indústrias
summary: Regras de produção, estoques, lotes e expansão, por que uma indústria não cresce ou não tem reforço, quando uma indústria sem uso fecha e como surgem novas indústrias.
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
fact: 5 anos | sem carregamento nem consumo tornam uma indústria candidata ao fechamento
fact: 1,1 % | de chance por ano em Raramente (padrão), depois 730 dias de contagem regressiva
fact: +50–150 % | de reforço pela carga de reforço, fixo por indústria
fact: 3 meses | de reforço por lote de carga de reforço
fact: ×2/3 – ×1,5 | Densidade-Alvo da Indústria: não é possível desligar as novas indústrias
---

Cada indústria funciona por **regras**: “pegue isto da entrada dos estoques, coloque aquilo na saída dos estoques”, um número fixo de vezes por ano. As indústrias primárias (minas, fazendas, poços) não precisam de entrada; o tamanho delas vem dos **lotes**. Dois reforços podem multiplicar a produção: a **carga de reforço** (só indústrias primárias) e os **trabalhadores**.

## Regras de produção

- Uma regra dá a carga usada e produzida por ciclo, e quantos ciclos por ano: um ciclo dura um ano ÷ esse número (`industry_react_util.tl:51-57`). A seção Produção da janela da indústria mostra isso em números pequenos.
- O número **Máx.** da janela é: por ciclo × ciclos por ano × os reforços × a configuração **Produtividade da Indústria** (`industry_util.tl:310-379`).
- **Produtividade da Indústria**: 50 %, 75 %, 100 %, 150 % ou 200 %. Predefinições: Fácil 150 %, Normal 100 %, Difícil 75 %, Muito Difícil 50 % (`difficulty_util.tl:41`, `difficulty_util.tl:93`, `difficulty_util.tl:120`, `difficulty_util.tl:148`, `difficulty_util.tl:175`, `mod.script.tl:196-197`).
- Exemplo, Usina Siderúrgica: 6 minério de ferro + 6 carvão → 3 aço + 4 chapas metálicas, 121,7 ciclos por ano: 730 minério de ferro e 730 carvão → 365 aço e 487 chapas metálicas (`steel_mill.con.lua:43-71`). Faltando uma entrada, a regra para.
- A Fábrica de Conservas tem duas regras: peixes + chapas metálicas, ou carne + chapas metálicas (`food_factory.con.lua:43-74`).

```engine
O motor executa as regras. Ele pode alongar um ciclo: a dica do ciclo mostra então “(+ … devido ao tempo de entrega)” (`industry_react_util.tl:61-76`). Quando e quanto não está nos scripts, então a produção real pode ficar abaixo do Máx.
```

## Estoques

- Cada carga tem seu próprio estoque com limite: p. ex. uma Mina de Carvão guarda 100 ferramentas e 400 carvão, uma Usina Siderúrgica 800 minério de ferro, 800 carvão, 400 aço e 500 chapas metálicas (`coal_mine.con.lua:44-67`, `steel_mill.con.lua:43-71`).
- Os estoques nunca se estragam (`industryutil.lua:25-29`): a carga espera o tempo que for preciso.
- Um estoque de saída cheio não para a produção: o excesso é jogado fora (wiki oficial). O gráfico **Fluxo de Carga** mostra **Consumido**, **Produzido** e **Destruído** (`industry_eow.script.tl:804-816`).
- Com o parâmetro de construção **Entrada** em Desligado, as regras perdem as entradas e a indústria não tem estoques de entrada (`industryutil.lua:280-287`, `industryutil.lua:383-387`, `industryutil.lua:432-441`).

## Lotes e expansão

- As indústrias primárias e a Fazenda Pecuária têm **lotes** (campos, poços de mina, torres). O nível delas é o número de lotes (`industryutil.lua:602-617`).
- A regra cresce com os lotes: produção por ciclo × lotes ÷ **todos os lotes desse tipo de indústria**, arredondado, no mínimo 1. As entradas caem na mesma proporção (`industryutil.lua:225-259`). Uma Mina de Carvão (8 tipos de lote) com 4 lotes faz 8 carvão por ciclo em vez de 16.
- Cada indústria recebe um máximo: ao acaso entre metade dos lotes e todos, ou Pequena / Média / Grande (50 / 75 / 100 %) com o parâmetro **Tamanho da Indústria** (`industryutil.lua:519-537`). Uma mina com máximo de 5 de 8 nunca chega à regra completa.
- Com Média, se 75 % arredonda para todos os lotes, o máximo é todos os lotes menos um (`industryutil.lua:523-526`). Uma indústria nova começa com os lotes que o motor constrói na colocação; o nível dela vem deles (`industryutil.lua:602-617`).
- A cada meio ano de **tempo de jogo** o jogo pode adicionar **um lote** (`industries_config.res.lua:5`, `industries.script.tl:161-167`). Usa-se meio ano padrão, então a velocidade do calendário não muda a frequência (veja [Tempo de jogo e calendário](time.html)).
- A chance é (nota − 25 %) ÷ 50 %, com nota = nota de produção × a parte da produção que você transporta (no máximo 1): 25 % ou menos nunca, 75 % ou mais sempre (`industries.script.tl:168-179`).
- Então uma indústria cuja carga você não transporta **nunca cresce**. Fábricas não têm lotes e nunca crescem.
- No máximo a janela diz **A indústria está expandida ao seu potencial máximo.**; quando prédios, trilhos ou estradas atrapalham, **A indústria está bloqueada de expansão adicional.** (`industry_react_util.tl:588-602`, `industries.script.tl:13-38`). Nenhum script remove lotes; segundo a wiki oficial, lotes demolidos reduzem a produção.
- O script do jogo pula as indústrias que pertencem a você, as de desenvolvimento manual e as que estão em contagem regressiva de fechamento: elas nunca recebem lote dele (`industries.script.tl:94-99`, `industries.script.tl:147-157`).

Exemplo, **Acampamento de Madeireira**: 20 lotes, 8 troncos por ciclo, 30,4 ciclos por ano (`forest.con.lua:54-66`, `forest.con.lua:75-98`). Por ciclo ele faz 8 × lotes ÷ 20, arredondado, no mínimo 1 (`industryutil.lua:231-241`):

| Lotes (nível) | Troncos por ciclo | Troncos por ano (Máx., sem reforço, Produtividade 100 %) |
|---|---|---|
| 1–3 | 1 | 30 |
| 4–6 | 2 | 61 |
| 7–8 | 3 | 91 |
| 9–11 | 4 | 122 |
| 12–13 | 5 | 152 |
| 14–16 | 6 | 183 |
| 17–18 | 7 | 213 |
| 19–20 | 8 | 243 |

A produção cresce em degraus: um lote novo nem sempre aumenta a produção.

## Por que minha indústria não cresce?

```diagram ind_growth
```

1. **Carga não transportada**: a nota conta a parte da produção carregada nos seus veículos. Com nota de produção de 100 %, transportar 25 % ou menos não dá chance, 50 % dá chance de metade, 75 % ou mais dá um lote a cada meio ano.
2. **No máximo**: **A indústria está expandida ao seu potencial máximo.** O máximo é sorteado na construção (de metade a todos os lotes) e nunca muda.
3. **Bloqueada**: **A indústria está bloqueada de expansão adicional.** Remova as estradas, trilhos ou prédios no lugar do próximo lote (mostrado na janela).
4. **Não é uma indústria primária**: fábricas não têm lotes.
5. **Contagem regressiva de fechamento**, indústria sua ou desenvolvimento manual: o script não faz crescer (acima).
6. **Sem produção**: uma indústria que não produz nada no ano é pulada (`industries.script.tl:168-171`).

```tip scripts
**Para uma mina ou fazenda crescer, transporte pelo menos 75 % da produção.** Com 25 % ou menos ela nunca ganha um lote novo; com 75 % ou mais ganha um a cada meio ano, até o máximo.
```

```engine
A nota de produção (getProductionRating), a produção anual e a quantidade transportada (getCargoOutputPerYear, getCargoShippedPerYear), e onde vai um novo lote (makeIndustryExtendProposal) são valores do motor.
```

## Carga de reforço

As 13 indústrias primárias têm uma segunda regra, o **reforço**: ele tira um lote de carga de reforço do estoque de entrada 4 vezes por ano e dá um bônus enquanto dura.

| Indústria | Lotes | Em tamanho cheio, por ano | Lote de reforço (4 por ano) | Fonte |
|---|---|---|---|---|
| Poço de Argila | 8 | 365 argila | 12 ferramentas | `clay_pit.con.lua:42-82` |
| Mina de Carvão | 8 | 320 carvão | 13 ferramentas | `coal_mine.con.lua:44-85` |
| Fazenda de Algodão | 21 | 274 lã | 17 fertilizante | `cotton_farm.con.lua:42-98` |
| Fazenda Agrícola | 20 | 274 grãos + 183 vegetais | 17 fertilizante | `farm.con.lua:44-106` |
| Áreas de Pesca | 18 | 263 peixes | 12 ferramentas | `fishing_grounds.con.lua:44-101` |
| Acampamento de Madeireira | 20 | 243 troncos | 15 máquinas | `forest.con.lua:44-99` |
| Mina de Minério de Ferro | 8 | 365 minério de ferro | 15 máquinas | `iron_ore_mine.con.lua:44-84` |
| Plataforma Petrolífera | 9 | 365 petróleo bruto | 12 máquinas | `oil_platform.con.lua:45-96` |
| Poço de Petróleo | 14 | 548 petróleo bruto | 15 máquinas | `oil_well.con.lua:44-94` |
| Pedreira | 7 | 365 pedra | 12 ferramentas | `quarry.con.lua:44-83` |
| Fazenda de Borracha | 23 | 365 borracha | 17 fertilizante | `rubber_farm.con.lua:41-102` |
| Barco Escavador | 9 | 365 areia | 15 máquinas | `sand_excavator.con.lua:44-92` |
| Areal | 8 | 365 areia | 12 ferramentas | `sand_pit.con.lua:44-84` |

- O bônus é sorteado uma vez por indústria: **+50 % a +150 %**, arredondado a 1 % (`industryutil.lua:394-405`). A seção Reforço mostra como “+X %” (`industry_util.tl:428-434`). Com o parâmetro **Fator de Reforço** ele vale +50 %, +75 %, +100 %, +125 % ou +150 % (`industryutil.lua:289-299`).
- A janela mostra o reforço ativo enquanto dura o último lote (3 meses), ou assim que o estoque tem um lote completo (`industry_util.tl:55-91`).
- O lote **não** diminui com os lotes de terreno: uma mina pequena pede tantas ferramentas quanto uma grande (`industryutil.lua:227-229`).
- Os dois reforços se multiplicam: produção × fator de trabalhadores × (1 + bônus de reforço) (`industry_util.tl:42-104`).

## O reforço de trabalhadores

Metade dos postos (10 de 20) precisa ser ocupada por moradores que **chegaram pelas suas linhas de passageiros** nos últimos 2 anos; o fator é ×1,5 a ×2,5, fixo por indústria (`industry_productivity_util.tl:35-72`). Trabalhadores só designados não contam. Detalhes: [Trabalhadores e o reforço de trabalhadores](workers.html).

## Por que minha indústria não tem reforço?

1. **Não é uma indústria primária**: fábricas não têm regra de reforço, só o reforço de trabalhadores (`steel_mill.con.lua:61-70`).
2. **Lote incompleto**: o estoque precisa ter um lote completo, p. ex. 13 ferramentas para uma Mina de Carvão. Abaixo de 4 lotes por ano (52 ferramentas) o reforço para entre as entregas.
3. **Carga errada**: ferramentas, máquinas ou fertilizante conforme a indústria (tabela acima).
4. **Trabalhadores**: designados não basta; a seção Reforço conta chegadas (“12/10”) (`industry_react_util.tl:617-654`). Veja [Trabalhadores e o reforço de trabalhadores](workers.html).

```tip scripts
**Para um bônus que nunca para, entregue pelo menos 4 lotes completos por ano** (52 ferramentas para uma mina de carvão). O estoque não se perde, então dá para entregar adiantado.
```

## Quando fecha uma indústria sem uso?

```diagram ind_closure
```

A verificação roda a cada 100 atualizações para cada indústria (`industries.script.tl:84-85`):

1. **Candidata**: nenhuma carga **carregada** num veículo e nenhuma **consumida** por **5 anos** (desde a construção, se nunca) (`industries.script.tl:104-119`, `industries_config.res.lua:6`). Só produzir não conta.
2. **Sorte**: a cada ano uma candidata é marcada com a chance da configuração **Frequência de fechamento de indústrias** (tabela abaixo) (`industries.script.tl:120-131`).
3. **Contagem regressiva**: aparece a notificação **Fechamento da indústria**, com 2 anos (730 dias) de prazo (`industries_config.res.lua:7`, `industry_close.script.tl:53-67`). Depois a indústria é removida com seus próprios trechos de estrada (`industries.script.tl:147-155`, `industry_util.tl:560-601`).
4. **Salva**: um único carregamento ou consumo durante a contagem a cancela (`industries.script.tl:134-137`). Aceitar um subsídio **Abastecer Indústria** ou **Transportar Trabalhadores** para ela também cancela (`subvention_util.tl:473-484`).

```tip scripts
**Notificação Fechamento da indústria? Um único carregamento ou entrega durante os 730 dias a cancela.** Aceitar um subsídio Abastecer Indústria ou Transportar Trabalhadores para essa indústria também cancela.
```

| Frequência de fechamento de indústrias | Chance por ano como candidata | Metade das candidatas marcadas após | Predefinição | Fonte |
|---|---|---|---|---|
| Nunca | 0 | nunca | Fácil | `difficulty_util.tl:94` |
| Raramente (padrão) | 1,1 % | cerca de 63 anos | Normal | `difficulty_util.tl:121` |
| Às Vezes | 2,2 % | cerca de 32 anos | Difícil | `difficulty_util.tl:149` |
| Frequentemente | 4,4 % | cerca de 16 anos | – | `difficulty_util.tl:37` |
| Muito Frequentemente | 8,8 % | cerca de 8 anos | Muito Difícil | `difficulty_util.tl:176` |

A chance é 0,011 por ano × 0, 1, 2, 4 ou 8 (`mod.script.tl:171`, `mod.script.tl:202-203`, `difficulty_util.tl:37`). Indústrias que pertencem a você nunca fecham, nem as de desenvolvimento manual, nem nenhuma durante o tutorial (`industries.script.tl:94-102`).

```engine
O que conta como “carregado” e “consumido” (os registros itemsLoaded e itemsConsumed, p. ex. se a carga de reforço conta), o indicador manualDevelopment, e por que indústrias com depósito ficam de fora (`industries.script.tl:140-146`) dependem do motor. Também o que o motor faz com uma regra de reforço que perdeu a entrada (Entrada desligada).
```

## Novas indústrias

O motor adiciona novas indústrias durante o jogo. A notificação é **Nova Indústria Fundada**: “Um empreendedor visionário identificou uma possibilidade de lucro e fundou: {industry}.” (`industry_spawn.script.tl:34-36`, `industry_spawn.res.lua:6`). Nenhum script do jogo escolhe o lugar, o tipo ou o momento, e nenhum filtra o que o motor propõe.

O que os scripts dão ao motor (`mod.script.tl:128-133`, `mod.script.tl:166-168`, `mod.script.tl:194-195`):

| Valor de configuração | Valor | Significado |
|---|---|---|
| spawnTargetTimeSpan | 50 × 365,25 dias padrão | chamado de “tempo-alvo”: 50 anos padrão de tempo de jogo |
| spawnProbabilityExponent | 3,0 | expoente da chance de surgimento (fórmula no motor) |
| spawnIndustries | desligado no editor de mapas, ligado num jogo | nenhuma indústria nova no editor de mapas |
| industryDensity | 1 × **Densidade-Alvo da Indústria** | o número-alvo de indústrias |
| maxNumberPerArea, absoluteMinimum | 0,8 por km² (0,64 em consoles), 24 | também usados pelo gerador de mapas |

**Densidade-Alvo da Indústria** (“Ajusta a densidade-alvo das indústrias no mapa.”): 5 níveis, ×2/3, ×5/6, ×1, ×1,2, ×1,5 (`difficulty_util.tl:55`, `difficulty_util.tl:85`).

- Fica nas configurações avançadas, parte de economia (`advanced_settings.tl:287-291`), e não faz parte das predefinições Fácil … Muito Difícil (`difficulty_util.tl:90-199`).
- No menu de novo jogo, **Densidade de Indústrias** (as indústrias no início, mesmos 5 fatores) põe **Densidade-Alvo da Indústria** no mesmo nível (`new_game_or_map_settings_page.tl:159-166`, `new_game_react_util.tl:288-296`). Mude o alvo depois nas configurações avançadas se quiser valores diferentes.
- **Nenhuma configuração desliga isso**: o nível mais baixo é ×2/3. Só o editor de mapas não tem indústrias novas. Mods podem.
- Velocidade: o tempo-alvo está em dias padrão, como todas as regras de tempo de jogo, então a velocidade do calendário e um calendário pausado não deveriam atrasá-lo. Medido com o calendário pausado: em 1809 s de tempo de jogo surgiram 3 indústrias novas, a 760 s e 728 s uma da outra, então um calendário pausado não as impede. Medido com o [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) em 3 jogos (cerca de 500 indústrias novas): as indústrias novas surgiram a cerca de **730 s** de tempo de jogo uma da outra em todas as velocidades do calendário (×4, ×1, ×0,5, ×0,25). São cerca de 45 dias do calendário em ×0,25 e 2 anos em ×4.
- A Prospecção por recursos (abaixo) usa a mesma chamada do motor com um município, então um surgimento “perto de um município” existe no motor (`company.script.tl:202`). O tutorial também a usa (`tutorial_init.tl:23-24`).

```engine
A fórmula por trás dos 50 anos e do expoente 3, como a densidade-alvo é contada (por área do mapa, por município?), qual tipo é escolhido e onde ele vai (makeIndustrySpawnProposal) dependem do motor. Nenhum script explica por que várias indústrias de um tipo podem aparecer juntas (“nove minas de carvão lado a lado”), nem por que algumas aparecem do outro lado do mapa.
```

### Prospecção por recursos

A vantagem de empresa **Prospecção por recursos** procura uma nova indústria desse recurso perto de um município que você escolhe: uma tentativa por mês, com chance subindo de 20 % a 60 %, por 6 meses (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`). Se o recurso tem vários tipos de indústria, eles são tentados em ordem aleatória (`company.script.tl:185-206`). Se todas as tentativas falharem, a licença volta (`company.script.tl:106-110`).

## Bom saber

- Transporte de cada indústria primária que você quer fazer crescer: produção não transportada bloqueia a expansão, quaisquer que sejam os reforços.
- Leve carga de reforço às maiores minas e fazendas: o lote custa o mesmo, o bônus acompanha os lotes de terreno.
- Os estoques não se estragam: você pode entregar carga de reforço adiantada, até o limite do estoque (100).
- Os reforços aumentam ruído e poluição: uma Mina de Carvão vai de 10 de poluição para 20 com um reforço e 30 com dois (`coal_mine.con.lua:99-117`).
- Menos indústrias novas: ponha **Densidade-Alvo da Indústria** no nível mais baixo nas configurações avançadas; não dá para zerar.
- Na configuração padrão uma indústria sem uso fecha raramente; em Muito Frequentemente, carregue algo de vez em quando.

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 5 anos, não 10, e a produção não conta: só a carga carregada num veículo ou consumida. Depois dos 5 anos a indústria é só candidata: a cada ano é marcada com chance de 1,1 % (Raramente) a 8,8 % (Muito Frequentemente). A contagem dura 730 dias, como dito. A carga de reforço dá +50 % a +150 % por indústria, em lotes que duram 3 meses. Novas indústrias: nenhuma configuração liga/desliga, só Densidade-Alvo da Indústria de ×2/3 a ×1,5; nenhuma no editor de mapas.
result: differs
```
