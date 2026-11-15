---
title: Trabalhadores e o reforço de trabalhadores
summary: Como os moradores conseguem emprego em uma indústria, quais contam para o reforço e qual é o tamanho do reforço.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-14
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
- A seção Reforços da janela da indústria mostra exatamente isso: "contados / necessários", com o necessário arredondado para cima (`industry_react_util.tl:627`).
- A verificação é refeita sempre que chegam novos trabalhadores ou quando a chegada mais antiga passa de 2 anos (`industry_workers.script.tl:40-43`). Por isso o reforço **termina sozinho** cerca de 2 anos depois que os trabalhadores param de chegar.

## Tamanho do reforço

- A produção é multiplicada pelo **fator de reforço** da indústria, mostrado na janela como "+X%" (`industry_react_util.tl:716`).
- O fator é sorteado uma vez a partir da semente aleatória da indústria: **entre ×1,5 e ×2,5**, e nunca muda para aquela indústria (`industry_productivity_util.tl:58-72`). Uma indústria sem semente usa ×2.
- Então duas minas idênticas podem ter reforços diferentes: confira o "+X%" antes de escolher qual atender.

## Exemplo

Uma mina de carvão com 20 locais de trabalho e "+84%".

| Situação | Contados | Reforçada? | Produção |
|---|---|---|---|
| Nova linha de ônibus: 14 moradores atribuídos, nenhum chegou ainda | 0 | não | ×1 |
| 12 moradores diferentes chegaram de ônibus este ano | 12 | sim (≥ 10) | ×1,84 |
| Linha de ônibus removida; ninguém chega por 2 anos | cai para 0 | termina | ×1 |

## Bom saber

- O limite de 20 chegadas guardadas e a regra dos 50% fazem com que uma indústria com **mais de 40 locais de trabalho** (possível com mods) nunca possa ser reforçada por trabalhadores.
- O subsídio "Transportar Trabalhadores" é cumprido quando este reforço é ativado (wiki oficial, Subsidies).
- A carga de reforço (fertilizante, máquinas, ferramentas) é um reforço **separado** das indústrias de matéria-prima, que não é tratado aqui.
- O mod [Origem dos trabalhadores (Worker Origins)](https://mod.io/g/transportfever3/m/worker-origins) mostra, na janela da indústria, de quais municípios vêm os trabalhadores atribuídos e os do reforço, com setas no mapa.

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: "Suficiente" = metade dos locais de trabalho (10 de 20); "recentemente" = os últimos 2 anos de jogo, as 20 chegadas mais recentes, uma por pessoa, só pelas suas linhas; fator de reforço de ×1,5 a ×2,5 conforme a indústria.
result: refines
```
