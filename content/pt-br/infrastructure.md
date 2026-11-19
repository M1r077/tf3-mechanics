---
title: Ruas, trilhos, pontes e sinais
summary: Velocidade, preço e manutenção de cada tipo de trilho e de rua, quanto custam e o que permitem pontes, túneis, cruzamentos e sinais, o que vielas e barreiras de som mudam de verdade, e onde os pátios são explicados.
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40444
fact: 100 / 160 / 350 km/h | trilhos simples, padrão e de alta velocidade
fact: ×9 | preço e manutenção dos trilhos de alta velocidade comparados com os trilhos simples
fact: +30% | no preço de um trilho com catenária
fact: -65% | de ruído de uma rua ou trilho com barreira de som
---

Cada tipo de rua e de trilho tem uma velocidade máxima, um preço por metro e uma manutenção por metro e ano, tudo escrito no seu arquivo. Pontes, cruzamentos e algumas decorações de rua somam o seu próprio limite de velocidade. Os custos abaixo valem com **Custos de Infraestrutura** e **Manutenção de Infraestrutura** em 100% (veja [Custos, manutenção e empréstimos](costs.html)).

## Trilhos

| Trilho | Desde | Velocidade máxima | Construção por km | Manutenção por km e ano | Fonte |
|---|---|---|---|---|---|
| Trilhos Simples | início | 100 km/h | 60.000 | 10.000 | `simple.street_template.lua:9`, `simple.street_template.lua:28`, `simple.street_template.lua:33` |
| Trilhos Padrão | 1930 | 160 km/h | 180.000 | 30.000 | `standard.street_template.lua:4`, `standard.street_template.lua:11`, `standard.street_template.lua:30`, `standard.street_template.lua:35` |
| Trilhos de Alta Velocidade | 1980 | 350 km/h | 540.000 | 90.000 | `high_speed.street_template.lua:4`, `high_speed.street_template.lua:11`, `high_speed.street_template.lua:30`, `high_speed.street_template.lua:35` |

- A **catenária** custa **30%** a mais que o trilho (`mod.script.tl:24-25`). Ela está disponível a partir de 1921 nos trilhos simples e desde o início de cada tipo mais novo (`simple_catenary.street_template.lua:4`). Nos arquivos, ela não custa nada a mais por ano: a variante elétrica tem a mesma manutenção (`simple_catenary.street_template.lua:34`).
- Os três tipos permitem a mesma inclinação e as mesmas curvas: **8,5%** ao construir (o controle Inclinação vai até esse valor), no máximo 13% para a forma do trilho, e um raio de curva de 55 m ao construir, 40 m no mínimo (`standard.street_template.lua:36-37`, `standard.street_template.lua:48-49`, `construction_react_util.tl:241-242`, `construction_react_util.tl:1824`).
- A poluição do próprio trilho cresce com o tipo: 2, 4 e 6 (`simple.street_template.lua:18`, `standard.street_template.lua:20`, `high_speed.street_template.lua:20`).

```engine
Quanto uma curva reduz a velocidade de um trem (os speedCoeffs de cada tipo de trilho) e qual velocidade a ferramenta de construção mostra para uma curva são calculados pelo motor.
```

```tip scripts
Os trilhos de alta velocidade custam 9 vezes os trilhos simples, na construção e todo ano. Use-os só onde os trens andam de verdade a mais de 160 km/h; no resto, os trilhos padrão bastam, e os simples para ramais lentos de carga.
```

## Ruas

| Rua | Anos | Velocidade máxima | Construção por km | Manutenção por km e ano | Fonte |
|---|---|---|---|---|---|
| Rua Estreita (antiga) | até 1940 | 20 km/h | 36.000 | 6.000 | `town_old_xsmall.street_template.lua:4-5`, `town_old_xsmall.street_template.lua:8`, `town_old_xsmall.street_template.lua:27`, `town_old_xsmall.street_template.lua:56` |
| Rua Pequena (antiga) | até 1940 | 40 km/h | 60.000 | 10.000 | `town_old_small.street_template.lua:8`, `town_old_small.street_template.lua:27`, `town_old_small.street_template.lua:56` |
| Rua Grande (antiga) | até 1940 | 60 km/h | 180.000 | 30.000 | `town_old_large.street_template.lua:8`, `town_old_large.street_template.lua:27`, `town_old_large.street_template.lua:88` |
| Rua Estreita (moderna) | desde 1940 | 30 km/h | 120.000 | 20.000 | `town_new_xsmall.street_template.lua:4`, `town_new_xsmall.street_template.lua:11`, `town_new_xsmall.street_template.lua:30`, `town_new_xsmall.street_template.lua:59` |
| Rua Pequena (moderna) | desde 1940 | 50 km/h | 180.000 | 30.000 | `town_new_small.street_template.lua:11`, `town_new_small.street_template.lua:30`, `town_new_small.street_template.lua:59` |
| Rua Média (moderna) | desde 1940 | 50 km/h | 360.000 | 60.000 | `town_new_medium.street_template.lua:11`, `town_new_medium.street_template.lua:30`, `town_new_medium.street_template.lua:75` |
| Rua Grande (moderna) | desde 1940 | 60 km/h | 540.000 | 90.000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:30`, `town_new_large.street_template.lua:91` |
| Via Rural Pequena (antiga) | até 1940 | 60 km/h | 60.000 | 10.000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:29`, `country_old_small.street_template.lua:58` |
| Via Rural Pequena (moderna) | desde 1940 | 80 km/h | 180.000 | 30.000 | `country_new_small.street_template.lua:10`, `country_new_small.street_template.lua:31`, `country_new_small.street_template.lua:60` |
| Rodovia com Uma Faixa | desde 1940 | 100 km/h | 180.000 | 30.000 | `highway_new_small.street_template.lua:10`, `highway_new_small.street_template.lua:32`, `highway_new_small.street_template.lua:53` |
| Rodovia com Duas Faixas | desde 1940 | 120 km/h | 360.000 | 60.000 | `highway_new_medium.street_template.lua:10`, `highway_new_medium.street_template.lua:32`, `highway_new_medium.street_template.lua:61` |
| Rodovia com Três Faixas | desde 1940 | 120 km/h | 540.000 | 90.000 | `highway_new_large.street_template.lua:10`, `highway_new_large.street_template.lua:32`, `highway_new_large.street_template.lua:69` |
| Trilhos de Bonde (antigos) | até 1910 | 40 km/h | 36.000 | 6.000 | `tram_old.street_template.lua:4-5`, `tram_old.street_template.lua:8`, `tram_old.street_template.lua:27`, `tram_old.street_template.lua:40` |
| Trilhos de Bonde (modernos) | desde 1925 | 100 km/h | 120.000 | 20.000 | `tram_new.street_template.lua:4`, `tram_new.street_template.lua:9`, `tram_new.street_template.lua:29`, `tram_new.street_template.lua:42` |

- A **mudança de 1940** deixa as ruas urbanas 10 km/h mais rápidas, mas **três vezes** mais caras, na construção e todo ano: uma rua pequena passa de 60.000 para 180.000 por km.
- As variantes média e grande das vias rurais custam 2 e 3 vezes a pequena, com a mesma velocidade (`country_new_large.street_template.lua:10`, `country_new_large.street_template.lua:31`).
- Acréscimos a uma rua: uma **faixa de ônibus** +10%, um **trilho de bonde** +20%, um **trilho de bonde elétrico** +40% do preço da rua (`mod.script.tl:24-28`).
- Em geral o jogador não é dono das ruas, nem das que ele mesmo construiu; as ferramentas de rua podem mudar o dono de uma rua (wiki oficial). Quem paga a manutenção de uma rua é decidido pelo motor.

## Vielas e barreiras de som

| Ferramenta | Ruído | Poluição | Velocidade máxima | Onde | Fonte |
|---|---|---|---|---|---|
| Ferramenta de Viela (árvores) | -10% | -50% | **-25%** | ruas com calçada, não em pontes nem em túneis | `alley.edge.lua:39-40`, `alley.edge.lua:53-56` |
| Ferramenta de Barreira de Som | -65% | sem mudança | sem mudança | ruas e trilhos, não em túneis | `barrier_b.edge.lua:43`, `barrier_b.edge.lua:47`, `barrier_track_b.edge.lua:43` |

- As duas custam 100 e 10 por ano nos seus arquivos, como uma rua por metro (`alley.edge.lua:8`, `alley.edge.lua:12`, `barrier_b.edge.lua:7`, `barrier_b.edge.lua:11`).
- Os tipos de rua "com árvores" e "com barreiras" do menu de construção são as mesmas ruas já com essas decorações (`town_new_medium_trees.street_template.lua:12-14`). O menu de construção soma os efeitos delas (`construction_react_util.tl:2119-2142`).
- Por isso uma rua com árvores fica **um quarto mais lenta**: uma rua média moderna com árvores permite cerca de 38 km/h em vez de 50.

```tip scripts
Contra o ruído, use a Barreira de Som: -65% e nenhuma perda de velocidade. As árvores são a ferramenta contra a poluição (-50%), mas deixam a rua um quarto mais lenta.
```

Como as cidades avaliam ruído e poluição: [Poluição e ruído](emission.html).

## Pontes e túneis

| Ponte | Anos | Velocidade máxima | Para | Preço base | Fonte |
|---|---|---|---|---|---|
| Ponte de Pedra | desde o início | 90 km/h | trilhos, ruas | 200 | `stone.bridge.lua:169-170`, `stone.bridge.lua:181-183`, `stone.bridge.lua:193` |
| Ponte de Cavaletes | até 1970 | 60 km/h | um tipo para trilhos, um para ruas | 100 | `trestle.bridge.lua:200-201`, `trestle.bridge.lua:212-214`, `trestle.bridge.lua:226`, `trestle_s.bridge.lua:212` |
| Ponte de Aço | desde 1940 | 140 km/h | trilhos, ruas | 200 | `steel.bridge.lua:243`, `steel.bridge.lua:259`, `steel.bridge.lua:269` |
| Ponte Suspensa | desde 1940 | 180 km/h | trilhos, ruas | 600 | `suspension.bridge.lua:277`, `suspension.bridge.lua:294`, `suspension.bridge.lua:304` |
| Ponte de Concreto | desde 1970 | 280 km/h | trilhos, ruas | 200 | `concrete.bridge.lua:162`, `concrete.bridge.lua:176`, `concrete.bridge.lua:187` |
| Ponte Estaiada | desde 2000 | 220 km/h | trilhos, ruas | 750 | `cable.bridge.lua:214`, `cable.bridge.lua:231`, `cable.bridge.lua:240` |
| Ponte em Arco com Tirante | desde 2010 | 350 km/h | trilhos, ruas | 650 | `tarch.bridge.lua:253`, `tarch.bridge.lua:270`, `tarch.bridge.lua:280` |

- O limite da ponte vale **além** do limite do trilho: uma linha de alta velocidade sobre uma ponte de aço anda a 140 km/h ali. Antes de 1970 nenhuma ponte permite mais de 180 km/h, antes de 2010 nenhuma permite 350 km/h.
- Os **túneis** (Túnel de Pedra, Túnel de Concreto desde 1970) **não têm limite de velocidade** nos seus arquivos, e têm o mesmo preço base de 600 (`tunnel_a.tunnel.lua:187-188`, `tunnel_a_car.tunnel.lua:185`, `tunnel_b.tunnel.lua:191-194`).
- Os preços de pontes e túneis seguem Custos de Infraestrutura (`post_run_util.tl:50-51`).

```engine
O preço base de uma ponte ou túnel é convertido pelo motor em um preço por metro, com a altura ou a profundidade (costFactors); a wiki oficial diz que ele depende do comprimento e da altura acima do solo ou da profundidade abaixo dele. O mesmo preço base pode, portanto, dar contas muito diferentes. Túneis custam Reputação na cidade (veja [Reputação](reputation.html)).
```

```tip scripts
Para uma linha rápida atravessando um vale antes de 1970, a ponte suspensa (180 km/h) é a única ponte mais rápida que 140 km/h; um túnel não tem limite nenhum.
```

## Passagens de nível e sinais

| O quê | Anos | Velocidade máxima do trilho | Preço | Fonte |
|---|---|---|---|---|
| Cruzamento Simples | 1850 - 1925 | 120 km/h | 4.000 | `era_a_eu.rcr.lua:14-17`, `era_a_eu.rcr.lua:26` |
| Cruzamento Rodoferroviário | 1925 - 1975 | 160 km/h | 16.000 | `era_b_eu.rcr.lua:15-18`, `era_b_eu.rcr.lua:27` |
| Cruzamento Rodoferroviário Moderno | desde 1975 | 160 km/h | 16.000 | `era_c_eu.rcr.lua:15-17`, `era_c_eu.rcr.lua:26` |
| Sinalização de Caminho (semáforo até 1950, luminoso desde 1950) | todos | - | 9.000, manutenção 1.500 por ano | `signal_path_a.con.lua:4-5`, `signal_path_a.con.lua:10-11`, `signal_path_c.con.lua:4-5` |

- Uma passagem de nível limita o trilho a no máximo 160 km/h: linhas de alta velocidade precisam de pontes ou túneis sobre as ruas.
- Todo sinal pode ser posto em **Sentido Único** (`signal_path_a.con.lua:51-52`). Como os sinais dividem o trilho em blocos é explicado na página Railway Signals da wiki oficial.

## Pátios e edifícios de manutenção

Quanto custam pátios e edifícios de manutenção, quantos veículos atendem e em que raio: [Linhas e veículos](vehicles.html) e [Custos, manutenção e empréstimos](costs.html).

## Bom saber

- Antes de 1940, melhorar ruas urbanas é barato; depois de 1940, cada rua urbana nova ou reconstruída custa três vezes mais e tem três vezes a manutenção.
- Numa linha rápida, confira cada ponte e cada passagem de nível: a mais lenta define a velocidade ali.
- Velocidade só compensa quando gera mais viagens (veja [Por que estou perdendo dinheiro?](money.html)).

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: As mesmas velocidades das tabelas oficiais para trilhos, ruas e pontes. Nos arquivos, os limites das pontes também valem para ruas, os túneis não têm nenhum, as passagens de nível limitam os trilhos a 120 ou 160 km/h, as árvores deixam a rua 25% mais lenta e cortam a poluição em 50%, mas o ruído só em 10%, enquanto as barreiras de som cortam o ruído em 65% sem reduzir a velocidade.
result: refines
```
