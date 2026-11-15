---
title: Trabalhadores e o reforço de trabalhadores
summary: Como os moradores conseguem emprego em uma indústria, quais contam para o reforço e qual é o tamanho do reforço.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-15
fact: 10 / 20 | trabalhadores necessários para o reforço
fact: 2 anos | tempo durante o qual uma chegada conta
fact: ×1,5–2,5 | fator de reforço, fixo para cada indústria
---

Toda indústria oferece locais de trabalho. Quando trabalhadores suficientes **chegam pelas suas linhas de passageiros**, a indústria produz mais. A janela da indústria mostra dois números diferentes, e confundir os dois é a causa mais comum de mal-entendidos.

```diagram workers_flow
```

## Quem pode trabalhar em uma indústria

- Toda indústria do jogo base tem **20 locais de trabalho** (`industrialCapacity = 20`).
- Os locais de trabalho são configurados para que os moradores **não possam ir a pé nem de carro**: só as suas linhas podem levá-los (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Cada morador tem uma casa, uma loja e um emprego. O jogo escolhe o emprego entre os lugares que o morador consegue alcançar; uma indústria tem peso de destino 2,0 (`industryutil.lua:455`).

```engine
Como um morador escolhe um emprego entre todos os lugares que consegue alcançar (tempo de viagem, custo, o peso de 2,0) é calculado pelo motor. Os scripts só fornecem os dados de entrada.
```

## Trabalhadores atribuídos

São os moradores cujo emprego é esta indústria. É a barra de locais de trabalho da janela da indústria e a coluna **Locais de Trabalho** das estatísticas de indústrias ("12/20") (`entity_window_util.tl:1238`, `statistic_industries.tl:305`). Estar atribuído **não** basta para o reforço: o trabalhador precisa de fato fazer a viagem.

## Trabalhadores contados para o reforço

Um pequeno script do jogo acompanha cada chegada (`industry_workers.script.tl`):

1. Quando um morador chega a uma indústria e o seu **último trajeto foi pelas suas linhas**, a chegada é registrada com o horário do jogo (`industry_workers.script.tl:86-118`).
2. Só ficam guardadas as chegadas dos **últimos 2 anos de jogo** (`industry_productivity_util.tl:3`: `2 * getDefaultYearDuration()`).
3. Ficam guardadas no máximo as **20 chegadas mais recentes** (`industry_workers.script.tl:4`, `KeepHistoryCount = 20`).
4. Quando a mesma pessoa chega de novo, a nova chegada substitui a antiga: cada morador conta **uma única vez** (`industry_workers.script.tl:56-70`).

```diagram workers_window
```

## Quando o reforço começa e termina

- A indústria recebe o reforço quando os trabalhadores contados chegam à **metade dos locais de trabalho**: `contados ≥ locais × 0,5` (`industry_productivity_util.tl:35-48`, `RequiredWorkersFractionForBoost = 0.5`). Com 20 locais de trabalho: **10 trabalhadores**.
- A seção Reforço da janela da indústria mostra exatamente isso: "contados / necessários", com o necessário arredondado para cima (`industry_react_util.tl:627`).
- A verificação é refeita sempre que chegam novos trabalhadores ou quando a chegada mais antiga passa de 2 anos (`industry_workers.script.tl:40-43`). Por isso o reforço **termina sozinho** cerca de 2 anos depois que os trabalhadores param de chegar.

## Tamanho do reforço

- A produção é multiplicada pelo **fator de reforço** da indústria, mostrado na janela como "+X %" (`industry_react_util.tl:716`).
- O fator é sorteado uma vez a partir da semente aleatória da indústria: **entre ×1,5 e ×2,5**, e nunca muda para aquela indústria (`industry_productivity_util.tl:58-72`). Uma indústria sem semente usa ×2.
- Então duas minas idênticas podem ter reforços diferentes: confira o "+X %" antes de escolher qual atender.

## Exemplo

Uma mina de carvão com 20 locais de trabalho e "+84 %".

| Situação | Contados | Reforçada? | Produção |
|---|---|---|---|
| Nova linha de ônibus: 14 moradores atribuídos, nenhum chegou ainda | 0 | não | ×1 |
| 12 moradores diferentes chegaram de ônibus este ano | 12 | sim (≥ 10) | ×1,84 |
| Linha de ônibus removida; ninguém chega por 2 anos | cai para 0 | termina | ×1 |

## Levar trabalhadores a uma indústria

```diagram workers_trip
```

- Um trabalhador é contado quando **chega à própria indústria**, o destino da viagem (`targetOrAtEntity`) é a indústria e o último modo de deslocamento é **Linhas** (`industry_workers.script.tl:86-94`). Descer numa parada não basta: a pessoa precisa chegar à indústria.
- Cada morador tem um modo de deslocamento por destino (casa, loja, emprego). A janela da indústria lista os trabalhadores atribuídos com um ícone desse modo: **Andar**, **Carro** ou **Linhas** (`entity_window_util.tl:1400-1435`). Para uma indústria deve ser sempre Linhas, porque Andar e Carro não são permitidos ali (`industryutil.lua:451-457`).
- Então "sem ir a pé" quer dizer que a viagem inteira não pode ser a pé nem de carro. Não quer dizer "nada a pé": uma viagem por Linhas ainda começa e termina a pé entre as paradas e os prédios (veja a nota do motor abaixo).
- **Baldeações contam.** O script só olha o modo da viagem, não quantas linhas foram usadas (`industry_workers.script.tl:91`). Um trabalhador de um município a quatro linhas de distância conta igual a um vizinho, mas pode demorar muito mais para chegar.
- **Qualquer uma das suas linhas pode trazê-los**, também uma linha que leva carga, desde que os veículos levem passageiros e a parada carregue passageiros. O script não verifica o tipo de veículo (`industry_workers.script.tl:86-118`). Jogadores relatam menos problemas com linhas de passageiros separadas.
- Algumas indústrias (por exemplo plataformas de petróleo) têm uma parada própria embutida, que aceita passageiros e carga (`industryutil.lua:156-165`).
- A janela da indústria mostra, para cada trabalhador atribuído, se está **Aqui** ou **A caminho** (`entity_window_util.tl:1371-1384`). A seção Reforço lista os trabalhadores contados com o **Tempo Restante** dos 2 anos (`entity_window_util.tl:1579-1630`, `industry_eow.script.tl:644-649`).
- Uma indústria ainda sem trabalhador mostra: "Conecte este local ao transporte público para que os habitantes possam trabalhar aqui." (`entity_window_util.tl:1650-1652`).

```engine
Qual parada atende uma indústria, quanto um trabalhador anda de uma parada até a entrada da indústria e os moradores de quais municípios pegam o emprego são decididos pelo motor (áreas de captação, busca de caminho, escolha de emprego). Os scripts não definem limite de distância para trabalhadores. Jogadores relatam que uma estação cuja área de captação cobria a indústria para carga não trouxe trabalhadores até um ônibus ir à entrada da indústria (tópico do Steam "Problem getting workers to site").
```

```tip
**Consiga rápido o bônus de trabalhadores (e o contrato Transportar trabalhadores): comece com uma linha simples.**

1. Crie uma **nova linha de passageiros** de uma parada na indústria até **uma só cidade**.
2. Posicione a parada na cidade de forma que sua área de cobertura **não toque nenhuma das suas outras estações de passageiros**.
3. Um só veículo basta para começar.

Os empregos são distribuídos quando a linha abre: em dois testes **os 20 empregos foram para essa única cidade**, e o bônus começou após **346 s e 925 s** de tempo de jogo (uma vez com um único veículo). Quando a parada na cidade tocava a área de uma estação da rede, alguns empregos foram para uma cidade distante e os últimos trabalhadores demoraram muito mais (964 s). Medido com [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) e o [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard); quem fica com um emprego continua sendo decidido pelo motor.
```

## Subsídio Transportar Trabalhadores

- Só é oferecido para uma indústria que envia ou recebe carga e ainda não tem reforço (`deliver_workers.script.tl:121-131`, `industry_util.tl:541-553`).
- É cumprido quando o reforço de trabalhadores fica ativo: as mesmas 10 de 20 chegadas diferentes pelas suas linhas (`deliver_workers.script.tl:152-156`). Nada mais é contado; não há regra escondida.
- A barra de progresso no cartão do contrato é "trabalhadores contados ÷ metade dos locais de trabalho" (`deliver_workers.script.tl:267-272`, `industry_util.tl:11-18`).
- As setas no mapa do contrato vêm dos **5 municípios mais próximos**. São só uma dica: o script as desenha pela distância, não por quem tem o emprego (`deliver_workers.script.tl:297-317`).
- Veja [Subsídios: ofertas, prazos e recompensas](subsidies.html) para dinheiro e prazo.

## Por que meus trabalhadores não chegam?

| Verificação | Onde olhar | Por quê |
|---|---|---|
| Alguém tem o emprego? | Barra de locais de trabalho ("12/20") | Sem trabalhadores atribuídos ninguém viaja. A escolha de emprego depende do motor. |
| Ícone de modo dos trabalhadores | Lista de trabalhadores: Andar / Carro / Linhas | Só viagens por Linhas podem contar (`industry_workers.script.tl:91`). |
| Eles estão se movendo? | **A caminho** / **Aqui** | "A caminho" por muito tempo: baldeações lentas ou lotadas, ou nenhum caminho desde a última parada. |
| A última parada alcança a entrada da indústria? | Captação da parada, estrada da entrada | Relatado por jogadores; depende do motor. Um ônibus curto até a entrada ajudou. |
| A parada carrega passageiros? | Parada da linha, Filtro de Cargas | Os passageiros precisam ser carregados e descarregados nas duas pontas da viagem. |
| 10 pessoas **diferentes** em 2 anos? | Seção Reforço, **Tempo Restante** | A mesma pessoa conta uma vez; chegadas antigas saem (`industry_workers.script.tl:56-70`). |
| Mais de 40 locais de trabalho (mods)? | Barra de locais de trabalho | Nunca chega à metade com 20 chegadas guardadas. |

## Bom saber

- O limite de 20 chegadas guardadas e a regra dos 50 % fazem com que uma indústria com **mais de 40 locais de trabalho** (possível com mods) nunca possa ser reforçada por trabalhadores.
- O subsídio **Transportar Trabalhadores** é cumprido quando este reforço é ativado (`deliver_workers.script.tl:152-156`).
- A carga de reforço (fertilizante, máquinas, ferramentas) é um reforço **separado** das indústrias de matéria-prima, que não é tratado aqui.
- O mod [Origem dos trabalhadores (Worker Origins)](https://mod.io/g/transportfever3/m/worker-origins) mostra, na janela da indústria, de quais municípios vêm os trabalhadores atribuídos e os do reforço, com setas no mapa.

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: "Suficiente" = metade dos locais de trabalho (10 de 20); "recentemente" = os últimos 2 anos de jogo, as 20 chegadas mais recentes, uma por pessoa, só pelas suas linhas; fator de reforço de ×1,5 a ×2,5 conforme a indústria. Baldeações contam; o modo da viagem precisa ser Linhas, e andar a partir de uma parada faz parte dessa viagem.
result: refines
```
