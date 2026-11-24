---
title: Conquistas
summary: O que o script do jogo verifica para cada conquista do Jogo Livre e quando, quais contam só veículos, cargas e animais do jogo base, e quais verificações ficam com o motor.
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-24
game: 40444
fact: 17 | conquistas desbloqueadas pelo próprio script do jogo
fact: 500 m | altura do primeiro vagão de um trem numa parada para Chegada ao Topo
fact: < 1 % | reputação do município para Vexame
fact: 10 | marcos que precisam ter o mesmo município mais próximo para Centralização
---

A wiki oficial lista 41 conquistas. O script do jogo (`achievements.script.tl`) desbloqueia **17** delas sozinho e alimenta **9 contadores entre jogos**; as outras (campanha, clima, tamanho do município, armazém, juros, boosters, carros, 1900-2000, vapor nos anos 2000) são verificadas em outro lugar, pelo motor ou pela plataforma. Cada verificação primeiro pergunta ao motor se a conquista ainda pode ser desbloqueada; se mods ou configurações a bloqueiam é decidido lá (`achievements.script.tl:632`, `achievements.script.tl:510`).

## Conquistas verificadas pelo script

| Conquista | O que o script verifica | Fonte |
|---|---|---|
| **Pacote Entregue** | um item de carga chega ao destino | `achievements.script.tl:221-225`, `achievements.script.tl:632-636` |
| **Em Nome do Povo** | um subsídio concluído | `achievements.script.tl:241-244`, `achievements.script.tl:638-642` |
| **Sequência de Subsídios** | 10 subsídios concluídos sem nenhum fracassado entre eles; um subsídio fracassado zera a contagem | `achievements.script.tl:243-249`, `achievements.script.tl:644-648` |
| **Protegendo o Município** | a avaliação de entregas de um município passa a **Excelente** | `achievements.script.tl:270-276`, `towns.script.tl:27-30`, `achievements.script.tl:650-654` |
| **Desenvolvimento Urbano** | um município sobe de nível | `achievements.script.tl:253-255`, `town_growth.script.tl:92` |
| **Demanda em Ascensão** | um município ganha demanda por um novo tipo de carga | `achievements.script.tl:257-259`, `achievements.script.tl:668-672` |
| **Vexame** | a Reputação de um município **cai** para menos de **1 %** | `achievements.script.tl:261-267`, `towns.script.tl:33-36` |
| **Promoção** | a empresa sobe de nível | `achievements.script.tl:280-282`, `achievements.script.tl:680-684` |
| **Degraus da Carreira** | a empresa chega ao nível mais alto | `achievements.script.tl:284-290`, `achievements.script.tl:686-690` |
| **Paisagismo Perfeito** | você coloca árvores, e só árvores, numa construção (nada removido, não por reflorestamento) | `achievements.script.tl:346-377` |
| **Perfeccionismo** | a mesma estação é demolida, reconstruída, demolida e reconstruída, nessa ordem, sem outra estação construída ou removida entre elas | `achievements.script.tl:304-341`, `achievements.script.tl:694-710` |
| **Centralização** | exatamente 10 marcos concluídos têm o mesmo município mais próximo | `achievements.script.tl:382-395`, `achievements.script.tl:713-721` |
| **Chegada ao Topo** | um dos seus trens chega a uma parada com o primeiro vagão acima de **500 m** | `achievements.script.tl:407-417`, `achievements.script.tl:723-727` |
| **Offshore** | um dos seus helicópteros chega a uma parada de uma plataforma de petróleo | `achievements.script.tl:420-450`, `achievements.script.tl:729-733` |
| **Frota Patrimonial** | todos os modelos de navio do jogo base estão rodando ao mesmo tempo nas suas linhas de navio | `achievements.script.tl:735-776` |
| **Contato do Terceiro Grau** | você clica num OVNI | `achievements.script.tl:793-806` |
| **Tempo Marcado** | você muda a hora do dia manualmente | `achievements.script.tl:839-844` |

- **Perfeccionismo** só conta uma construção que adiciona ou remove uma estação inteira: adicionar uma plataforma ou um módulo a uma estação não conta (`achievements.script.tl:301-302`).
- **Centralização** conta cada marco quando ele fica pronto, para o município mais próximo dele naquele momento (`achievements.script.tl:386`).
- **Frota Patrimonial** só é verificada quando um modelo de navio que nunca parou antes chega a uma parada; ela olha os veículos das suas linhas de navio, não os navios no depósito (`achievements.script.tl:736`, `achievements.script.tl:750-766`).
- **Vexame** exige a Reputação, não outra avaliação: veja [Reputação dos municípios](reputation.html).

```tip scripts
Chegada ao Topo verifica a altura do primeiro vagão quando o trem para, não a altura do prédio da estação. Construa a estação numa montanha acima de 500 m e faça um trem chegar lá.
```

## Contadores entre jogos

Estes continuam de um jogo para outro (a plataforma os guarda). O script só envia o que mudou desde a última verificação.

| Contador | Conquista | O que conta | Fonte |
|---|---|---|---|
| Comprimento de vias | **Ao Redor do Mundo** | o crescimento do comprimento total do registro (em km); nada é descontado quando você remove | `achievements.script.tl:511-523` |
| População | **População Global** | o crescimento da população do mapa, a partir da população quando o jogo foi carregado | `achievements.script.tl:512`, `achievements.script.tl:525-533` |
| Passageiros | **Pioneirismo em Viagens** | passageiros que terminaram uma viagem numa das suas linhas | `achievements.script.tl:236-238`, `achievements.script.tl:535-541` |
| Carga | **Pioneirismo em Cargas** | itens de carga entregues | `achievements.script.tl:543-549` |
| Climas | **Magnata dos Magnatas** | o clima do mapa, quando a empresa chega ao nível mais alto nele | `achievements.script.tl:551-567` |
| Receita | **Dinheiro Maligno** | sua receita somada, em bilhões | `achievements.script.tl:202-204`, `achievements.script.tl:569-590` |
| Tipos de carga | **Mestre das Vendas** | cada tipo de carga do jogo base entregue uma vez | `achievements.script.tl:20-22`, `achievements.script.tl:230-232`, `achievements.script.tl:592-607` |
| Veículos | **Conhecimento é Tudo** | cada modelo de veículo do jogo base que chega a uma parada uma vez | `achievements.script.tl:16-18`, `achievements.script.tl:469-481`, `achievements.script.tl:609-625` |
| Animais | **Amor aos Animais** | cada animal do jogo base em que você clica uma vez | `achievements.script.tl:24-26`, `achievements.script.tl:809-834` |

- Veículos, cargas e animais de mods nunca contam para esses contadores: só arquivos do jogo base (`::/vehicle`, `::/cargos`, `::/animal`) são considerados (`achievements.script.tl:16-26`).
- Para Conhecimento é Tudo um veículo precisa **chegar a uma parada** de uma linha; comprá-lo não basta.

```engine
Se uma conquista ainda pode ser desbloqueada (isAchievementUnlockable), se os contadores estão desligados (areStatsDisabled), as metas de cada contador e as 24 conquistas fora do script ficam a cargo do motor e da plataforma. A wiki oficial diz que as conquistas geralmente ficam indisponíveis com mods não cosméticos ou com configurações de jogo diferentes dos valores padrão.
```

## Mods e conquistas

Usar mods **não** desliga as conquistas por si só. O que conta é se cada mod ativo está marcado como **cosmético**.

- Todo mod tem uma flag `cosmetic` no seu `mod.json`. A própria documentação da API do jogo (pasta `api/tealdef`, campo `ModDesc.cosmetic`) diz: "If the mod is purely cosmetic, cosmetic mods still allow achievement from being earned while playing" (se o mod é puramente cosmético, ainda é possível ganhar conquistas).
- O motor verifica a lista de mods ativos (`ModRep.couldAchievementsBeEarned`) e guarda o resultado em cada jogo salvo (`achievementsEarnable`), mesma pasta.
- As DLCs oficiais e as missões da campanha também são mods, e todas estão marcadas como cosméticas (`dlcs/*/mod.json`, `mods/release/urbangames_campaign*/mod.json`).
- Quando as conquistas estão bloqueadas, o jogo avisa: ele tem as mensagens "Achievements Disabled!" (conquistas desativadas) e "Achievements cannot be earned." (conquistas não podem ser ganhas) (`base/strings`).

Então um jogo só com mods cosméticos ainda pode ganhar conquistas. Um único mod não cosmético, ou configurações de jogo diferentes dos valores padrão, basta para bloqueá-las (wiki oficial).

```engine
A regra exata (quais configurações contam, e se um jogo salvo que já foi bloqueado continua bloqueado depois que o mod é removido) é decidida no motor e não está nos arquivos legíveis: desconhecido.
```

```tip scripts
O autor do mod escolhe a flag. Confira a linha `cosmetic` no `mod.json` do mod, ou pergunte ao autor. Um mod que muda a jogabilidade (custos, produção, regras) normalmente não é cosmético.
```

## Bom saber

- Cada conquista de "primeira vez" é comparada com a verificação anterior: ela precisa de um evento **novo** num jogo em que a conquista ainda está aberta; um subsídio ou nível antigo de um save não conta de novo (`achievements.script.tl:633`, `achievements.script.tl:779`).
- Seu nível, os subsídios e a Reputação são explicados em [Nível da empresa, vantagens e sede](company.html), [Subsídios](subsidies.html) e [Reputação dos municípios](reputation.html).

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: 17 conquistas e 9 contadores estão no script. Ele detalha os textos oficiais: Protegendo o Município significa a avaliação de entregas chegar a Excelente, Vexame uma Reputação abaixo de 1 %, Chegada ao Topo o primeiro vagão acima de 500 m, Perfeccionismo demolir-reconstruir-demolir-reconstruir a mesma estação, e Frota Patrimonial todos os modelos de navio do jogo base em linhas ao mesmo tempo. Só veículos, cargas e animais do jogo base contam para os contadores.
result: refines
```
