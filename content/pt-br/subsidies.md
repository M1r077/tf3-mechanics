---
title: Subsídios: ofertas, prazos e recompensas
summary: Os quatro tipos de contrato, o que realmente os cumpre, o que você ganha e o que arrisca, e com que frequência chegam novas ofertas.
domain: subsidies
official: gamemanual:management:subsidies
status: verified
updated: 2026-11-15
fact: 4 | tipos de contrato em um jogo livre
fact: 5 | contratos aceitos no máximo ao mesmo tempo
fact: ×2 | de renda por 5 anos nas linhas que entregaram
fact: 0 | de penalidade por recusar uma oferta
---

Um subsídio é um contrato: uma indústria ou um município oferece uma tarefa, você recebe algo ao aceitar, mais ao cumpri-la no prazo, e devolve o adiantamento mais uma penalidade quando perde o prazo. Recusar uma oferta, ou deixá-la expirar, não custa nada.

```diagram subsidy_life
```

## Os quatro tipos de contrato

```diagram subsidy_types
```

| Contrato | Alvo | O que o cumpre | Fonte |
|---|---|---|---|
| **Abastecer Indústria** | uma indústria que nunca produziu nada | o número exigido de entregas a ela, **de qualquer uma das suas cargas de entrada** | `deliver_cargo.script.tl:54-61`, `deliver_cargo.script.tl:230-234`, `deliver_cargo.script.tl:470-479` |
| **Abastecer Município** | uma carga que o município pede e não recebe de forma alguma | o número exigido de unidades **dessa carga** entregues a prédios do município | `deliver_cargo_town.script.tl:566-581` |
| **Conectar Municípios** | dois municípios | **um único** passageiro que começa uma viagem entre os dois municípios em uma linha que para nos dois | `deliver_passengers.script.tl:263-280`, `subvention_util.tl:561-592` |
| **Transportar Trabalhadores** | uma indústria que já envia ou recebe carga, ainda sem bônus | o seu bônus de trabalhadores fica ativo (metade dos seus postos de trabalho) | `deliver_workers.script.tl:121-131`, `deliver_workers.script.tl:152-156` |

- Cada nova oferta sorteia um dos tipos que podem aparecer no momento, com chances iguais (`subventions.script.tl:147-169`).
- **Abastecer Indústria** e **Abastecer Município** contam entregas, não viagens: cada unidade paga que chega ao alvo soma 1. Transferências são permitidas (`deliver_cargo.script.tl:470-479`).
- **Conectar Municípios** não exige um número de passageiros: o primeiro passageiro que embarca na sua linha entre os dois municípios o cumpre. "Sem transferência" significa que esse trecho é feito em uma única linha que atende os dois municípios. Nenhuma oferta aparece se uma linha já transporta passageiros entre eles (`deliver_passengers.script.tl:72-78`).
- Municípios próximos são bem mais prováveis: o peso do par cai de 1 a 1 km ou menos para 0,01 a 20 km, elevado à potência 7 (`deliver_passengers.script.tl:175-191`).
- **Abastecer Município** prefere cargas que já são produzidas em algum lugar do mapa: 16 vezes mais prováveis que as outras (`deliver_cargo_town.script.tl:277-280`).
- A quantidade a entregar depende da configuração **Risco dos Subsídios**:

| Risco dos Subsídios | Abastecer Indústria | Abastecer Município (no máximo a demanda do município) | Fonte |
|---|---|---|---|
| Nenhum | 10–50 | 10–30 | `deliver_cargo.script.tl:100-114`, `deliver_cargo_town.script.tl:165-188` |
| Justo | 50–100 | 30–100 | |
| Arriscado | 75–150 | 35–125 | |
| Muito Arriscado | 150–300 | 45–150 | |

## O que é uma conexão sem transferência?

O cartão **Conectar Municípios** pede: "Crie uma conexão sem transferência entre {fromTownName} e {toTownName} e transporte passageiros entre os dois municípios." (`deliver_passengers.script.tl:14`).

- **Uma linha com uma parada em cada município.** O jogo percorre as paradas da linha e pega o município de cada uma; a linha conta quando pelo menos uma parada fica em cada um dos dois municípios. As outras paradas, a ordem delas e o tipo de veículo (ônibus, bonde, trem, navio, aeronave) não importam (`subvention_util.tl:561-592`).
- **Um passageiro o cumpre**: o primeiro passageiro que viaja nessa linha de uma parada em um município até uma parada no outro, em qualquer sentido (`deliver_passengers.script.tl:263-280`, `deliver_passengers.script.tl:210-218`). A verificação só olha para essa viagem, então trocar de linha antes ou depois dela não deve importar.
- **O município de uma parada** é o município da primeira estação do seu grupo de estações (`town_util.tl:1844-1873`). A qual município uma estação pertence é decidido pelo motor.
- **Nenhuma oferta** aparece quando uma linha já tem uma parada que embarca passageiros em cada município e um veículo que leva passageiros (`deliver_passengers.script.tl:72-78`). Uma linha só de carga entre eles não bloqueia a oferta.
- O contrato termina como **Subsídio Removido** quando um dos dois municípios, ou a linha que o cumpriu, muda de um jeito que o jogo conta como uma nova versão (`deliver_passengers.script.tl:232-240`).

```engine
A qual município uma estação pertence (stationSystem.getTown), quando exatamente um passageiro "começa a usar" uma linha (OnStartedLineUsage) e quais edições de uma linha contam como uma nova versão ficam do lado do motor. Não foi testado se uma edição da linha depois do cumprimento encerra o efeito Renda x2.
```

## Recompensas e penalidades

Cada contrato guarda três listas, mostradas no seu cartão como **Ao aceitar**, **Ao cumprir** e **Ao fracassar** (`subvention_util.tl:449-471`). Em caso de fracasso, o adiantamento é sempre devolvido, mais uma penalidade extra (`deliver_cargo.script.tl:134-136`).

| Contrato | Ao aceitar | Ao cumprir | Ao fracassar | Fonte |
|---|---|---|---|---|
| Abastecer Indústria | dinheiro | só o efeito **Renda x2** | adiantamento devolvido + multa | `deliver_cargo.script.tl:120-136` |
| Abastecer Município | dinheiro **ou** reputação no município | experiência do município **ou** dinheiro, mais Renda x2 | adiantamento devolvido + perda de reputação **ou** multa | `deliver_cargo_town.script.tl:194-229` |
| Conectar Municípios | dinheiro, mais para municípios distantes | experiência nos **dois** municípios, mais Renda x2 | adiantamento devolvido + perda de reputação nos **dois** municípios | `deliver_passengers.script.tl:105-119` |
| Transportar Trabalhadores | dinheiro | dinheiro | adiantamento devolvido + multa | `deliver_workers.script.tl:92-116` |

- **Dinheiro**, antes do ajuste pelo ano: adiantamento de 1,5 a 3,75 milhões × o fator de risco (Nenhum ×2, Justo ×1, Arriscado ×0,75, Muito Arriscado ×0,5); multa de 3 a 6 milhões; pagamento ao cumprir de 3,75 a 11,25 milhões (`deliver_cargo.script.tl:120-128`, `deliver_workers.script.tl:102-104`).
- O dinheiro cresce com o **ano do calendário**, não com a configuração Inflação: ×1 em 1900, subindo de forma regular até ×4 em 2000 e depois, arredondado para cima a 10.000 (`finances_util.tl:87-90`). Ele é lançado como **Subsídios** nas finanças (`subvention_util.tl:126-135`).
- **Abastecer Município** dá recompensas e multas em dinheiro só enquanto a sua conta bancária está abaixo de 100 milhões; acima disso, só 1 oferta em 10 ainda pode dar (`deliver_cargo_town.script.tl:206-217`).
- A **experiência do município** é uma parte do nível atual do município: de 20% a 100% do XP entre o seu nível e o seguinte (`deliver_cargo_town.script.tl:216`, `town_growth.script.tl:605-608`). Para **Conectar Municípios** ela é multiplicada pelo fator de distância, de 0,3 a 1 km até 3,0 a 20 km: municípios distantes podem ganhar vários níveis (`deliver_passengers.script.tl:94-96`, `deliver_passengers.script.tl:116-118`).
- A **reputação** perdida depois de um fracasso aparece na classificação Reputação do município como **Subsídio Fracassado** (`towns.script.tl:313-334`). A reputação ganha ao aceitar só remove penalidades existentes, não pode passar do máximo (`town_util.tl:1644-1647`).

## O efeito Renda x2

- Ele dura **60 meses** (5 anos) depois que o contrato é cumprido (`subvention_util.tl:286`, `subvention_util.tl:292`).
- **Abastecer Indústria**: entregas a essa indústria, nas linhas que entregaram a ela durante o contrato (`deliver_cargo.script.tl:463-469`).
- **Abastecer Município**: entregas a qualquer prédio desse município, **de qualquer carga**, nas linhas que entregaram a carga do contrato (`deliver_cargo_town.script.tl:554-565`).
- **Conectar Municípios**: passageiros entre os dois municípios na linha que o cumpriu (`deliver_passengers.script.tl:281-304`).
- **Transportar Trabalhadores** não tem efeito na renda (`deliver_workers.script.tl:90`).
- Uma linha que só começou a entregar depois que o contrato foi cumprido não ganha nada: a lista de linhas só é preenchida durante o contrato.
- Dois contratos nunca dobram o mesmo pagamento duas vezes: quando vários se aplicam, só a última resposta é usada (`subventions.script.tl:570-583`).

```tip scripts
**Quer a renda dobrada de Abastecer Indústria ou Abastecer Município em várias linhas? Faça todas entregarem antes de o contrato ser cumprido.** Uma linha adicionada depois não ganha nada. Conectar Municípios dobra só uma linha.
```

```engine
Como o ×2 de um subsídio se combina com o multiplicador do ranque da empresa (configuração Inflação) é decidido pelo motor: os dois scripts só devolvem um multiplicador para cada pagamento. O que é uma entrada de pagamento (provavelmente uma unidade de carga ou um passageiro) também é decidido pelo motor.
```

## Prazos

O prazo começa quando você aceita. Ele é mais longo quando a carga precisa viajar longe e mais curto com um risco maior (fator de risco Nenhum ×2, Justo ×1, Arriscado ×0,75, Muito Arriscado ×0,5, ou ×0,625 para os contratos de passageiros e de trabalhadores):

| Contrato | Prazo em meses | Distância usada | Fonte |
|---|---|---|---|
| Abastecer Indústria, Abastecer Município | (6 + 32 × E) × fator de risco | até a indústria mais próxima que produz a carga | `deliver_cargo.script.tl:116-117` |
| Conectar Municípios | (9 + 4 × E) × fator de risco | entre os dois municípios | `deliver_passengers.script.tl:98-99` |
| Transportar Trabalhadores | (6 + 15 × E) × fator de risco × fator de época (×1,75 antes de 1940, ×1,25 antes de 1980) | até o município mais próximo | `deliver_workers.script.tl:75-87` |

E é o tempo que um trem na velocidade máxima da época (120 km/h a partir de 1900 até 300 km/h a partir de 1981) leva para essa distância, arredondado para cima, no mínimo 1 (`subvention_util.tl:486-489`, `vehicle_util.tl:225-230`).

- Uma oferta que não é aceita desaparece depois de cerca de **6 meses** (150 a 210 dias), sem nenhuma penalidade (`subvention_util.tl:284`, `subvention_util.tl:290`).
- Enquanto um contrato **Abastecer Indústria** ou **Transportar Trabalhadores** está em andamento, a indústria alvo não pode fechar: um fechamento planejado é cancelado (`subvention_util.tl:473-484`).
- Se o alvo desaparece ou é reconstruído durante o contrato, o jogo mostra **Subsídio Removido**, mas as penalidades de fracasso são aplicadas como em um prazo perdido (`subventions.script.tl:172-190`, `subvention_util.tl:406-412`).
- Não há botão para cancelar um contrato aceito.

```engine
A duração de um mês de jogo, e portanto a duração real dos prazos, é definida pelo motor (getDefaultMonthDuration). As fórmulas acima estão em meses do calendário do jogo.
```

## Com que frequência chegam novas ofertas

- **Disponibilidade de Subsídios**: Raramente, Às Vezes (o padrão), Frequentemente, Muito Frequentemente dão uma nova oferta a cada 12, 6, 3 ou 1 mês; **Nunca** desliga os subsídios (`subvention_util.tl:13-38`, `mod.script.tl:247-248`).
- O intervalo cresce com o **ranque da empresa**: ×1 no ranque 1 até ×2 no ranque 15 (`subvention_util.tl:19-22`).
- **Recusar** uma oferta corta o próximo intervalo pela metade; aceitar ou uma nova oferta o restaura (`subventions.script.tl:429`, `subventions.script.tl:395`, `subventions.script.tl:118`).
- Nenhuma nova oferta enquanto **5 contratos** aceitos estão em andamento (`subventions.script.tl:23`, `subventions.script.tl:256-262`). A primeira oferta chega depois de meio mês.
- O mesmo alvo (indústria, município e carga, par de municípios) é oferecido **só uma vez por jogo**, mesmo depois de um contrato perdido ou fracassado (`subventions.script.tl:107-113`, `subventions.script.tl:186`).
- Predefinições de dificuldade, disponibilidade / risco (`difficulty_util.tl:104-105`, `difficulty_util.tl:132-133`, `difficulty_util.tl:159-160`, `difficulty_util.tl:186-187`): Fácil Frequentemente / Nenhum, Normal Às Vezes / Justo, Difícil Raramente / Arriscado, **Muito Difícil Nunca**: nenhum subsídio.
- A verificação da classificação do município que só permitiria subsídios em municípios com classificação Muito Boa existe, mas está desligada (`town_util.tl:1574-1580`, `deliver_cargo_town.script.tl:272-275`).

## Bom saber

- Aceite sem medo quando o alvo é fácil: recusar ou ignorar não custa nada, mas **fracassar** custa a devolução do adiantamento mais uma multa que pode ser maior que o adiantamento.
- Para **Abastecer Município** e **Abastecer Indústria**, comece a entregar com todas as linhas que você quer beneficiar: só as linhas que entregaram durante o contrato ganham a Renda x2 por 5 anos.
- **Conectar Municípios** com municípios distantes dá a maior experiência ao município, e exige um único passageiro.
- **Abastecer Indústria** não paga nada a mais ao ser cumprido: a sua recompensa é só a Renda x2.

```check
official: "Accept an offer to begin the contract; declining it has no penalty." "Possible rewards include town experience, an additional payment, or a limited-time 2x income effect on eligible transport lines." "The upfront reward is reversed, and an additional fine or loss of town reputation may apply." ([Subsidies](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:subsidies))
scripts: Quatro tipos; um único passageiro cumpre Conectar Municípios; o ×2 dura 60 meses nas linhas que entregaram durante o contrato; Abastecer Indústria dá só o ×2; dinheiro ajustado pelo ano (×1 a ×4); uma nova oferta a cada 1–12 meses, mais espaçadas em ranque alto da empresa; no máximo 5 aceitos; cada alvo oferecido uma vez por jogo.
result: refines
```
