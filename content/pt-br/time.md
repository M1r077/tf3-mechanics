---
title: Tempo de jogo e calendário
summary: Velocidade do jogo e velocidade do calendário são duas coisas diferentes. Quanto duram um dia e um ano, o que um calendário mais lento ou pausado muda, e o que não muda.
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
fact: 4 s | um dia do calendário com velocidade do calendário ×1 e velocidade do jogo 1x
fact: ≈ 24 min | um ano do calendário com as mesmas velocidades
fact: 0 ×0,25 ×0,5 ×1 ×2 ×4 | níveis da velocidade do calendário
fact: 0 1x 2x 4x | níveis da velocidade do jogo
---

O jogo tem **dois relógios**. A **velocidade do jogo** (pausa, 1x, 2x, 4x) acelera tudo: veículos, produção, cidades. A **velocidade do calendário** só define a rapidez com que a data avança. Quase toda regra do jogo conta em tempo de jogo, não em dias do calendário.

## As duas configurações

| Configuração | Níveis | O que muda | Fonte |
|---|---|---|---|
| **Velocidade do jogo** | Pausar, 1x, 2x, 4x | a rapidez de toda a simulação | `game_bar_widgets.tl:199-203` |
| **Velocidade do Calendário** | Pausado, ×0.25, ×0.5, ×1, ×2, ×4 | quantos segundos de jogo dura um dia | `game_bar_widgets.tl:321-335`, `game_bar_widgets.tl:351` |

- Com velocidade do calendário ×1, um dia dura **4 segundos** de tempo de jogo (wiki oficial), então um mês dura cerca de 2 minutos e um ano cerca de **24 minutos** em 1x. Medido com o [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard): 4,0 s por dia em ×1, 1 s em ×4, 8 s em ×0.5, 16 s em ×0.25.
- ×4 faz a data avançar quatro vezes mais rápido; **Pausado** para a data, e a simulação continua.
- 2x e 4x são um máximo: o jogo os reduz quando o computador não acompanha (`game.tl:636-642`). Medido: 2x deu 1,9x e 4x deu 3,6x em média.
- A **Hora do Dia** e o clima são um terceiro relógio, visual: por padrão mudam sozinhos, independentemente do calendário (`game_time_config.res.lua:5`, `weather_config.res.lua:5`).

## O que segue o tempo de jogo, independentemente do calendário

Estes são contados em tempo de jogo, então um calendário mais lento ou pausado não os desacelera:

- **Produção**: o tempo de produção de uma indústria é uma fração fixa de um ano padrão (`industry_react_util.tl:51`). A janela da indústria o mostra em dias do calendário atual (`industry_react_util.tl:23`): em ×0.25 o mesmo ritmo mostra um quarto dos dias.
- **Parcelas de empréstimos**: uma a cada mês padrão de tempo de jogo, também com o calendário pausado (`loan.script.tl:83-88`).
- **Prazos de subsídios** e o bônus ×2 de renda (`subvention_util.tl:290-292`).
- **Recuperação da reputação das cidades** (`towns.script.tl:121-130`), **bônus de trabalhadores** (`industry_productivity_util.tl:3`) e **fechamento de indústrias** após anos sem atendimento (`industries.script.tl:119-128`).
- **Avaliações de entrega** das cidades, no último semestre (`town_util.tl:840`).

Com o calendário rodando, o jogo mostra essas durações em anos, meses e dias da velocidade do calendário atual (`util.tl:40-49`).

## O que segue a data do calendário

- **Novos veículos, estações e edifícios** aparecem conforme o ano (wiki oficial: "Different calendar speeds only affect the availability of vehicles and infrastructure").
- **Custos que crescem com o ano**: manutenção de edifícios, variantes de era, valores de subsídios e de empréstimos seguem a data. Detalhes: [Custos, manutenção e empréstimos](costs.html).

## Com o calendário pausado

1. A data, e portanto o ano, ficam fixos: nenhum veículo novo, e os custos baseados no ano não mudam.
2. As durações são mostradas em **minutos e segundos** em vez de dias (`util.tl:41-43`, `industry_react_util.tl:16-21`).
3. Um empréstimo mostra sua parcela **por minuto** em vez de por ano (`finances_loan_gui.tl:223-231`), e o empréstimo personalizado não pode ser contratado (`finances_loan_gui.tl:393`).
4. Produção, pagamentos, prazos e reputação mantêm seu ritmo em tempo de jogo.

## Bom saber

- Quer mais tempo para expandir uma rede antes de chegarem novos veículos? Diminua a velocidade do calendário: sua renda por minuto de jogo não muda.
- A produção mostrada "por ano" depende da velocidade do calendário; compare indústrias na mesma velocidade.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) mantém gráficos de finanças legíveis com o calendário pausado.

```engine
A duração do dia, mês e ano padrão (getDefaultDayDuration e os outros) vem do motor. O script das cidades conta um mês como 30 × 4 segundos (`towns.script.tl:121`), o que combina com o dia medido de 4 segundos; algumas outras constantes ainda supõem um dia de 2 segundos (`cargotype.script.lua:3`, `mod.script.tl:172`).
```

```check
official: "By default a day in the game lasts 4 seconds." "Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent." ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: Velocidade do calendário de ×0.25 a ×4 ou pausado, em relação ao dia padrão; produção, empréstimos, subsídios, reputação e temporizadores de trabalhadores rodam em tempo de jogo; um calendário pausado mostra durações em minutos, pagamentos por minuto e bloqueia novos empréstimos; medido: 4 s por dia em ×1.
result: refines
```
