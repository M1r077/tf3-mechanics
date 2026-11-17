---
title: Notificações e avisos
summary: Quando cada aviso aparece e quando some: veículos presos, estações inutilizáveis ou superlotadas, problemas de linha e de parada, classificações dos municípios, condição dos veículos, indústrias fechando, e quais avisos ficam fora do registro por padrão.
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 5 min | de tempo de jogo parado antes de um veículo ser dado como preso
fact: 20% | de condição que dispara o aviso, até o veículo voltar acima de 30%
fact: 11 | tipos de notificação desligados num jogo novo
fact: 75 dias | entre duas verificações de estações sem conexão viária
---

A maioria dos avisos é **persistente**: um script do jogo verifica a situação várias vezes, o aviso fica enquanto o problema existir e termina sozinho quando ele é resolvido. As verificações se revezam em 4 atualizações, então um aviso pode demorar um pouco para aparecer ou sumir (`notifications.script.tl:13`, `notifications.script.tl:49`).

## Quando cada aviso aparece

| Aviso | Aparece quando | Some quando | Fonte |
|---|---|---|---|
| **Veículo preso** | um dos seus veículos está a caminho, não foi parado por você e está com velocidade 0 há **5 minutos** de tempo de jogo | ele volta a andar | `notifications.script.tl:557-580` |
| **Estação fora de serviço** | nenhum terminal da estação embarca ou desembarca passageiros e **nada** está na área de cobertura (nenhum armazém, indústria ou prédio do município), enquanto uma das suas linhas para lá | algo entra na área de cobertura | `notifications.script.tl:602-617`, `notifications.script.tl:630-647`, `station_useless.script.tl:39` |
| **Estação superlotada** | a estação tem mais passageiros ou carga esperando do que comporta (excesso), enquanto uma das suas linhas para lá; passageiros vão embora | o excesso acaba | `notifications.script.tl:599`, `notifications.script.tl:649-661`, `overcrowding.script.tl:23` |
| **Condição do Veículo** | um veículo seu está com **20%** de condição ou menos | ele volta acima de **30%** | `notifications.script.tl:310-318` |
| **Classificação do Município: Muito Ruim** | uma das classificações do município cai para Muito Ruim (abaixo de 1/6) | a classificação volta a Medíocre ou melhor | `notifications.script.tl:230-238`, `town_util.tl:763-769`, `town_util.tl:983-985` |
| **Classificação do Município Caindo** | uma classificação está Ruim ou Medíocre (abaixo de 50%) sem estar no aviso Muito Ruim | a classificação está Boa ou melhor | `notifications.script.tl:240-248` |
| **Fechamento da indústria** | uma indústria começa a contagem regressiva para fechar | ela fecha, ou volta a ser usada a tempo | `notifications.script.tl:439-451`, `industry_close.script.tl:53-59` |
| **Não Há Conexão Viária** | uma estação não está conectada a uma rua; verificado a cada **75 dias** | a próxima verificação encontra uma rua | `notifications.script.tl:16`, `notifications.script.tl:423-436` |
| **Problema com o Descarregamento de Carga** | a carga de um veículo nunca é descarregada na sua linha | ela é descarregada | `notifications.script.tl:277-290`, `cargo_rtc_warning.script.tl:28-37` |

- Um veículo **no pátio** nunca conta como preso: essa verificação está desligada no script (`notifications.script.tl:563-564`). Um veículo que você parou também não.
- A verificação de Estação fora de serviço olha só a área de cobertura. Uma estação que já tem passageiros embarcando ou desembarcando num terminal nunca é avisada (`notifications.script.tl:606-610`).
- Como subir uma classificação do município: [Crescimento dos municípios](towns.html) e [Reputação](reputation.html). Como funciona a contagem para fechar e como pará-la: [Indústrias](industries.html). O que a condição faz com um veículo: [Custos, manutenção e empréstimos](costs.html).

```engine
Se uma estação transborda, se um veículo tem caminho, se uma linha alcança suas estações e quanto tempo a viagem entre dois municípios pode durar, quem decide é o motor (calculateStationGroupCargo, getVehicleProblems, getLineProblems, getTownProblems). Os scripts só transformam as respostas dele em avisos.
```

```tip scripts
Veículo preso, Problema com Veículo, Condição do Veículo, Estação superlotada e Estação indisponível vêm desligados no registro de um jogo novo. Ligue-os nas configurações de notificação: são eles que avisam de um congestionamento, de um caminho faltando ou de uma frota desgastada.
```

## Problemas de linha, parada e veículo

Estes vêm direto das verificações do motor sobre suas linhas e veículos; o script dá um título a cada um.

| Aviso | Casos | Fonte |
|---|---|---|
| **Problema com a Linha** | poucas estações; uma estação duas vezes seguidas; estações incompatíveis entre si; não foi possível conectar as estações; não foi possível conectar terminais alternativos | `line_warning.script.tl:46-128` |
| **A linha está configurada incorretamente** | um tipo de carga que não pode ser carregado em lugar nenhum, ou descarregado em lugar nenhum; nenhum veículo leva uma carga marcada para carregar; veículos que não levam nenhuma das cargas configuradas, ou veículos só de carga numa linha de passageiros; nenhuma carga configurada | `line_warning.script.tl:15-36`, `line_warning.script.tl:133` |
| **Problema com a Estação** | uma parada que os veículos atuais não podem usar; uma parada de passageiros usada por veículos de carga (um ou todos); uma parada de carga usada por veículos de passageiros; um tipo de carga configurado que não pode ser carregado ou descarregado naquela parada | `line_station_warning.script.tl:6-87` |
| **Problema com Veículo** | sem caminho eletrificado; sem caminho para aeronaves grandes; sem caminho para navios grandes; nenhum caminho; dois trens bloqueando um ao outro | `vehicle_warning.script.tl:6-58` |
| **Cidade não conectada** | a rua entre dois municípios está interrompida; a viagem entre dois municípios demora demais | `town_warning.script.tl:7-19` |

- "Não há caminho para aeronaves grandes" e "Não há caminho para navios grandes" significam que o veículo é grande demais para uma pista, cais ou via navegável da sua linha: veja [Aeronaves](aircraft.html) e [Navios](ships.html).

## Registro, pop-ups e configurações

- Cada tipo de aviso pode ser desligado nas configurações de notificação ("Configurar registro de notificações"). Um tipo desligado não tem pop-up e não fica no registro (`notification_util.tl:145-146`, `notification_log.tl:480`).
- Num **jogo novo**, 11 tipos começam desligados: **Veículo preso**, **Problema com Veículo**, **Condição do Veículo**, **Estação superlotada**, **Estação indisponível**, **Estação não conectada**, **Cidade não conectada**, **Carga Não Descarregada**, e as mensagens de progresso da empresa de Prospecção, Campanha de Marketing e Ecologização industrial (`stuck_vehicle.res.lua:7`, `vehicle_warning.res.lua:8`, `noroadconnection.res.lua:8`, `vehiclecondition.res.lua:8`, `overcrowding.res.lua:8`, `station_useless.res.lua:7`, `town_warning.res.lua:8`, `cargo_rtc_warning.res.lua:8`, `notification_util.tl:32-39`).
- Mensagens únicas (veículo novo, construção nova, subida de nível, subsídios) escondem o pop-up após **60 segundos** de tempo de jogo; elas ficam no histórico (`notification_util.tl:10`, `notifications.script.tl:85-94`).
- Uma notificação também termina quando tudo o que ela aponta foi removido ou reconstruído (`notifications.script.tl:95-107`).
- Numa missão as notificações começam pausadas, até a missão ligá-las (`notifications.script.tl:700-704`).

## Bom saber

- Um aviso de veículo preso após 5 minutos não diz o motivo. Olhe o veículo: um sinal vermelho, um sinal de mão única virado ao contrário, ou um aviso Problema com Veículo para o mesmo veículo.
- "Estação fora de serviço" só quer dizer "nada na área de cobertura ainda". Aproxime a estação de casas, de uma indústria ou de um armazém, ou aumente-a.
- Uma estação superlotada perde passageiros: adicione veículos ou encurte o intervalo (veja [Partida e espera](departure.html)).

```check
official: The official wiki's User Interface page describes the notification button, the log and its filters, without the conditions of each warning. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: As condições acima: preso após 5 minutos com velocidade 0 a caminho, condição do veículo de 20% até 30%, classificação Muito Ruim abaixo de 1/6, conexão viária verificada a cada 75 dias, 11 tipos desligados por padrão.
result: adds
```
