---
title: Reputação dos municípios
summary: O que baixa a avaliação Reputação de um município, com que rapidez ela volta, o que celebrações e campanhas de marketing fazem de verdade, e por que uma estrada cortada entre dois municípios custa tanto.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
fact: −33 % | por conexão principal interrompida com outro município
fact: 33 % | recuperados por ano (100 % durante uma campanha de marketing)
fact: 0,25 % | por árvore adulta removida perto do município
fact: 2 mi m³ | de obras no terreno custam toda a reputação
---

A **Reputação** é uma das seis avaliações da janela do município, e a Autoridade do Município usa a **mais baixa** delas (veja [Crescimento dos municípios](towns.html)). Ela começa em 100 % e só cai pelo que **você** constrói ou falha: obras no terreno, árvores e rochas removidas, edifícios do município demolidos, subsídios fracassados e conexões principais cortadas. O tempo, as celebrações e as campanhas de marketing a trazem de volta.

```diagram rep_recovery
```

## O que a baixa

Cada construção que você confirma é verificada antes de ser aplicada; o custo vai para o município afetado (`towns.script.tl:271-291`, `town_util.tl:1062-1080`). Só as suas construções contam, e no editor de mapas nada conta (`town_util.tl:1078-1080`, `towns.script.tl:58`).

| Motivo na janela do município | O que custa reputação | Fonte |
|---|---|---|
| **Árvores Removidas** | 0,25 % por árvore, × o fator de distância até o município mais próximo, × o tamanho da árvore (árvores pequenas contam menos) | `town_util.tl:1144-1150`, `town_util.tl:865`, `model_metadata_util.lua:655-680` |
| **Rochas Removidas** | 0,25 % por rocha, × o fator de distância | `town_util.tl:1148-1149`, `town_util.tl:884-885` |
| **Paisagismo** | 0,00005 % por m³ de terreno elevado **ou** rebaixado: 2 milhões de m³ = 100 %. Também conta o terreno moldado por trilhos, estradas e edifícios (até metade a menos em obras acima de 50.000 m²), e o volume de túneis novos | `town_util.tl:873-886`, `town_util.tl:1245-1269`, `town_util.tl:1403-1436` |
| **Edifícios Demolidos** | 100 % para 40,5 % da capacidade de um distrito removida (moradias, lojas ou empregos daquele município) | `town_util.tl:867-869`, `town_util.tl:1165-1184` |
| **Subsídio Fracassado** | Abastecer Município: de 10 % até 60–90 % (conforme o risco); Conectar Municípios: 10–100 % × o fator de distância, nos **dois** municípios (veja [Subsídios](subsidies.html)) | `deliver_cargo_town.script.tl:202-210`, `deliver_passengers.script.tl:113-114`, `towns.script.tl:331-333` |
| **Conexões Principais Interrompidas** | **1/3** por outro município cuja conexão principal está cortada ou longa demais | `town_util.tl:376-394`, `town_util.tl:1608` |

- Cada motivo tem limite de 100 % (`town_util.tl:1611-1620`).
- Durante a construção, a dica mostra **Reputação: −x %**, com o número de municípios atingidos quando são vários (`construction_react_util.tl:3818-3864`). Ela conta o custo a partir de uma avaliação cheia.
- Plantar árvores ou colocar rochas só anula **Árvores Removidas** ou **Rochas Removidas**, com os mesmos 0,25 % por unidade. Não faz nada pelos outros motivos, nem com a reputação cheia (`town_util.tl:1228-1238`, `town_util.tl:1630-1641`).
- A opção Reputação de um novo jogo é **Desligado** ou **Ligado** (Ligado em todas as predefinições). Desligado significa avaliação cheia, sempre (`difficulty_util.tl:44`, `difficulty_util.tl:110`, `town_util.tl:396-399`).

```engine
Com que rapidez o fator de distância cai entre um município e uma árvore removida, que volume de terreno cada município recebe, as árvores removidas automaticamente por um trilho ou uma estrada, e quais estradas contam como conexão principal de um município (e quando uma viagem é "longa demais") são valores do motor (getImpactFromDistance, getTerrainBrushVolumeImpact, getTerrainAlignmentImpact, getAutoRemovalEntityImpact, getTownProblems).
```

## Conexões principais cortadas

Uma conexão principal conta como cortada quando o jogo avisa **A conexão rodoviária entre as cidades foi interrompida** ou **O tempo de viagem entre as cidades é muito longo** (`town_util.tl:378-380`, `town_warning.script.tl:7-22`). Cada outro município envolvido custa 1/3, e a avaliação mostra isso **na hora** (`town_util.tl:401-403`):

| Conexões cortadas | Reputação no máximo | Avaliação | Fonte |
|---|---|---|---|
| 1 | 67 % | Muito Boa | `town_util.tl:983-985` |
| 2 | 33 % | Medíocre | `town_util.tl:983-985` |
| 3 | 0 % | Muito Ruim: o município para de crescer | `town_util.tl:607-633` |

- Enquanto o corte dura, a penalidade também é gravada na pontuação salva, passo a passo, ao longo de meio ano (`towns.script.tl:137-145`). Depois que você conserta a estrada, essa parte gravada só volta na velocidade normal de recuperação: um corte longo continua custando reputação por um tempo.
- 67 % fica exatamente no limite de Muito Boa: qualquer outra pequena perda leva o município a Boa.

## Como ela volta

- **Sozinha**: a janela do município mostra **Recuperação Anual** 33 %, 100 % com uma campanha de marketing (`town_react_util.tl:1061-1067`). É um nível (1/6) a cada meio ano, ou a cada 2 meses durante uma campanha (`towns.script.tl:121-135`).
- A recuperação divide o ganho entre todos os motivos; ela nunca passa das conexões cortadas ainda abertas (`town_util.tl:1649-1687`).
- As **celebrações** somam **+50 %** pelo primeiro passageiro que embarca numa das suas linhas num município, +50 % pela primeira carga entregue a um município, +50 % a cada subida de nível do município, e +20 % ao município mais próximo pela primeira carga entregue a cada indústria (`celebrations.script.tl:181-273`). A mensagem termina então com **Reputação da aldeia melhorada.** ou **Reputação melhorada em …** (`celebration_react_util.tl:63-75`). Elas só contam se a reputação não estiver cheia, e não nas missões de campanha (`celebrations.script.tl:79-93`, `celebrations.script.tl:140-142`).
- **Abastecer Município** pode dar de +5 % a +20 % × o fator de risco ao aceitar (`deliver_cargo_town.script.tl:195-199`). Como todo ganho, só remove perdas existentes (`towns.script.tl:324-330`).

## Campanha de marketing

| O quê | Valor | Fonte |
|---|---|---|
| Preço | 10 M × fator do ano: 4 M em 1900 até 25 M em 2020, arredondado a 1 M | `marketing_campaign_tool.script.tl:9-14` |
| Exige | uma licença das vantagens da empresa | `marketing_campaign_tool.script.tl:83-95`, `company.script.tl:416-423` |
| Duração | um ano | `marketing_campaign_tool.script.tl:136` |
| Reputação | recuperação ×3 (100 % por ano); **nenhum** ganho imediato | `towns.script.tl:126`, `town_util.tl:915-925` |
| Habitantes | suas linhas naquele município contam como metade do custo quando os habitantes escolhem como viajar | `marketing_campaign_tool.script.tl:137`, `towns.script.tl:376-398` |

```engine
O script conta 360 segundos de tempo de jogo por nível (120 com campanha). O calendário por trás é a duração do ano do motor (getDefaultYearDuration); os 33 % e 100 % mostrados na janela do município correspondem a um ano de 720 segundos (um dia de 2 segundos, como em `cargotype.script.lua:3`). O quanto o custo de linha pela metade leva os habitantes às suas linhas é decidido pela escolha de rota do motor.
```

## Bom saber

- Olhe a dica de construção: se ela mostrar **Reputação: −x %**, um túnel ou um traçado mais suave muitas vezes custa menos que a reputação.
- Nunca deixe cortada uma estrada principal entre dois municípios: cada uma vale −33 % na hora, e três cortes param o município.
- Uma campanha de marketing com a reputação cheia só ajuda suas linhas, não a avaliação. Lance-a logo depois de grandes obras, quando a recuperação tem algo a recuperar.
- O bônus **Recuperação da Reputação** do módulo grande da sede (+1 %) aparece na aba Bônus, mas nos scripts só muda um valor que nenhuma avaliação lê (`hq_module_l.module.lua:171`, `towns.script.tl:157`, `town_util.tl:829`, `town_util.tl:857`).
- A conquista **Vexame** pede um município com 0 % de reputação no Jogo Livre (`achievements.script.tl:261-267`).

```check
official: "Reputation reflects how the town and surrounding nature are treated. Landscaping, removing town buildings and breaking main connections to other towns can lower it, while celebrations and marketing campaigns can improve it. Reputation lost by removing trees can be recovered by planting new ones." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: As mesmas causas, mais rochas removidas, túneis, o terreno de trilhos e estradas e subsídios fracassados. Cada conexão principal cortada ou longa demais custa 1/3 na hora; três param o município. A recuperação é de 33 % por ano sozinha; uma campanha de marketing a leva a 100 % por ano, mas não dá nada na hora. Plantar árvores só anula a perda por árvores. O bônus Recuperação da Reputação da sede não tem efeito nos scripts.
result: refines
```
