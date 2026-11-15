---
title: Configurações de partida: carga completa, Nível de Preenchimento e tempos de parada
summary: Quando um veículo deixa uma parada: os três modos de partida, o Nível de Preenchimento de cada carga e os tempos de parada mínimo, máximo e adicional.
domain: stations
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-15
fact: 600 s | Tempo de Parada Máx. padrão de uma parada nova
fact: 30 s / 60 s | Tempo Máximo de Espera Adicional padrão, rodovia / ferrovia
fact: 0–100 % | Nível de Preenchimento, por carga, da capacidade do veículo
---

Cada parada de uma linha tem as suas próprias configurações de partida, na janela "Filtro de Cargas" da parada (clique na parada na janela da linha). Elas decidem **quanto** o veículo carrega ali e **quanto tempo** ele pode esperar.

## As configurações

| Configuração | Valores | Parada nova | Fonte |
|---|---|---|---|
| "Carregar, se disponível", "Carga Completa (Qualquer)", "Carga Completa (Tudo)" | um dos três | Carregar, se disponível (medido) | `cargofilter_window.tl:798-821` |
| "Tempo de Parada Mín." | 0–600 s, passo 10 | 0 s (medido) | `cargofilter_window.tl:841-845` |
| "Tempo de Parada Máx." | 0–600 s, ou "---" (sem limite, controle deslizante no fim) | **600 s** (medido) | `cargofilter_window.tl:855-863` |
| "Tempo Máximo de Espera Adicional" | 0–600 s, passo 10 | 60 s; 30 s em uma estação rodoviária ou de bonde sem ferrovia | `cargofilter_window.tl:827-831`, `line_util.tl:478-490` |
| "Nível de Preenchimento", por carga carregada | 0–100 %, passo 1 | 100 % | `cargofilter_window.tl:698-704`, `line_util.tl:511` |

- Clicar em um tempo abre uma caixa numérica: valores acima de 600 s podem ser digitados ali (`cargofilter_window.tl:204-208`).
- Os três tempos se mantêm em ordem: subir o mínimo ou a espera adicional acima do máximo também sobe o máximo (`cargofilter_window.tl:834-835`, `cargofilter_window.tl:848-849`, `cargofilter_window.tl:865-869`).
- Mudar qualquer um deles marca a linha como personalizada: a configuração automática não mexe mais nas suas listas Volume (`cargofilter_window.tl:438`, veja [Velocidade de carga e descarga](loading.html)). A própria configuração automática nunca muda o modo nem os tempos (`line_util.tl:495-513`).

## Nível de Preenchimento: um limite por carga

O Nível de Preenchimento é o máximo daquela carga que o veículo pega nesta parada, como fração da capacidade do veículo, arredondado para a unidade mais próxima (medido no jogo).

| Veículo | Nível de Preenchimento | Sai com |
|---|---|---|
| caminhão, 15 lugares, troncos | 50 % | **8** (7,5 arredondado para cima) |
| caminhão, 22 lugares, tecido | 70 % | **15** todas as vezes (15,4) |
| trem, 18 lugares, vidro | 48 % | no máximo **9** (8,64) |
| bonde, 28 lugares, combustível | 66 % | no máximo **18** (18,48) |

- A carga já a bordo conta: um bonde que chegou com 14 de combustível saiu com 18, não 14 + 18.
- Acima do limite nada é carregado **e nada é descarregado** por causa dele: um caminhão que chegou com 22 de fertilizante (limite 11) saiu com 22.
- **0 %** significa: não carregar esta carga aqui.
- Com um modo de Carga Completa, o limite conta como cheio: caminhões de troncos com Nível de Preenchimento de 50 % esperaram cerca de 270 s e saíram com 8 de 15, não 15.
- Não existe porcentagem de descarga. A descarga é decidida pela lista Volume e por "Forçar descarregamento de todas as cargas na chegada" ([Velocidade de carga e descarga](loading.html)).

## Carga Completa e os tempos de parada

- **Carregar, se disponível**: o veículo pega o que há e sai.
- **Carga Completa (Tudo)**: o veículo espera até ficar cheio. Caminhões de troncos esperaram 460–566 s e saíram com 15 de 15.
- **Carga Completa (Qualquer)**: o veículo sai quando uma carga está cheia. Um trem de troncos e tábuas saiu com 143 e 144 troncos após 369–380 s; duas outras partidas após cerca de 30 s, com 57 e 118 troncos, não têm explicação.
- **Tempo de Parada Máx.** encerra a espera, mesmo sem nada carregado. Um trem de vegetais em Carga Completa (Tudo) com máximo de 120 s ou encheu (64 de 64) em cerca de 25 s, ou saiu após 116–120 s com 26 ou **0**. Com o padrão de 600 s ele saiu com 26 de 64 após 596–600 s.
- **Tempo de Parada Mín.** é a parada inteira, carregamento incluído, não tempo extra depois dele: com 60 s, trens de vidro pararam 55–61 s todas as vezes, independentemente do que carregaram.
- **Tempo Máximo de Espera Adicional**: "Maximum wait time after loading to improve vehicle distribution" (`cargofilter_window.tl:827`). A janela do veículo mostra "Garantindo distância segura" enquanto ele espera (`entity_window_util.tl:2279-2286`).
- **Vários veículos em uma parada carregam ao mesmo tempo**, não importa quando cada um chegou (visto no jogo). Dois caminhões de troncos que chegaram com cerca de 90 s de diferença saíram no mesmo segundo, cada um com 8. Como a carga é dividida entre eles não foi medido.

```engine
Os scripts só guardam as configurações; quando um veículo sai é decidido pelo motor.
```

As regras acima foram medidas com o banco de dados do [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) (instantâneos a cada 2 s, então os tempos de parada são ±2 s), novembro de 2026.

## Bom saber

- Uma espera longa com Carga Completa em uma parada onde chega pouca carga bloqueia a plataforma: outros veículos da linha fazem fila atrás.
- Um Tempo de Parada Máx. curto com Carga Completa pode mandar veículos embora vazios se eles voltarem antes de haver carga nova.
- Uma vez, um trem em Carga Completa (Tudo) parou 783–992 s com máximo de 600 s. A causa não foi encontrada.

```check
official: "Full load (any): The vehicle will stop and wait until one cargo type is fully loaded. Full load (all): The vehicle will stop and wait until it is fully loaded." "In the vanilla game "all" and "any" only applies to trains and ships […] Any other vehicle type will wait for full load in both cases." Each cargo is loaded "to what percentage of a vehicle's total capacity". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles#departure_configuration))
scripts: Três modos de partida, Tempo de Parada Mín. / Máx. 0–600 s (ou sem limite), Tempo Máximo de Espera Adicional 0–600 s (60 s, 30 s rodovia), Nível de Preenchimento 0–100 % por carga; medido: o Nível de Preenchimento limita a carga a bordo, arredondado para a unidade mais próxima, e conta como cheio para Carga Completa; o Tempo de Parada Máx. encerra uma carga completa, mesmo vazio; o Tempo de Parada Mín. inclui o carregamento; veículos em uma parada carregam juntos.
result: refines
```
