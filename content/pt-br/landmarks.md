---
title: Pontos de referência, celebrações e elementos divertidos
summary: Quanto cada ponto de referência custa em carga, quando é desbloqueado e o que faz pelos veículos da sua cidade, como a configuração Recursos Necessários para Marcos o escala, e o que celebrações, fogos de artifício, dirigíveis e OVNIs realmente fazem.
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 9 | pontos de referência, um por nível de empresa de 2 a 15
fact: +20 % / −20 % / +25 % | velocidade máxima, poluição ou conforto para os veículos da sua cidade
fact: ×0 a ×4 | de carga necessária, com a configuração Recursos Necessários para Marcos
fact: 2-4 anos | entre dois OVNIs
---

Um ponto de referência é construído como um canteiro de obras: você o desbloqueia com um nível de empresa, o posiciona e depois **entrega carga** a ele. Quando o canteiro tem toda a sua carga, o ponto de referência fica pronto e dá um bônus aos veículos da **sua cidade**. A sede é um prédio separado com regras próprias (veja [Nível da empresa, vantagens e sede](company.html)).

## Os pontos de referência

Carga com **Recursos Necessários para Marcos** ×1 (Normal).

| Ponto de referência | Nível | Carga a entregar | Bônus para os veículos da sua cidade | Fonte |
|---|---|---|---|---|
| **Anfiteatro** | 2 | 800 de pedra | veículos rodoviários: ruído **−25 %** | `arena.con.lua:10`, `arena.con.lua:20-26`, `arena.con.lua:39` |
| **Grande Farol** | 5 | 1.200 de pedra, 200 de combustível | navios: velocidade máxima **+20 %** | `lighthouse.con.lua:10`, `lighthouse.con.lua:14`, `lighthouse.con.lua:29`, `lighthouse.con.lua:48` |
| **Castelo de Himeji** | 7 | 1.200 de pedra, 400 tábuas | trens: poluição **−20 %** | `white_heron_castle.con.lua:10`, `white_heron_castle.con.lua:14`, `white_heron_castle.con.lua:28`, `white_heron_castle.con.lua:47` |
| **Museu Naval** | 9 | 600 troncos, 600 tábuas, 200 de tecido | navios: conforto **+25 %** | `ship_museum.con.lua:10-18`, `ship_museum.con.lua:36`, `ship_museum.con.lua:55` |
| **Castelo Neuschwanstein** | 10 | 1.000 de pedra, 600 tábuas, 200 corantes | veículos rodoviários: conforto **+25 %** | `neuschwanstein.con.lua:10-18`, `neuschwanstein.con.lua:36`, `neuschwanstein.con.lua:55` |
| **Estátua da Liberdade** | 11 | 800 de pedra, 400 de aço, 400 chapas metálicas | navios: poluição **−20 %** | `statue_of_liberty.con.lua:10-18`, `statue_of_liberty.con.lua:38`, `statue_of_liberty.con.lua:57` |
| **Palácio de Verão** | 13 | 600 de pedra, 300 tábuas, 300 corantes, 300 móveis | aeronaves: poluição **−20 %** | `summer_palace.con.lua:10-22`, `summer_palace.con.lua:44`, `summer_palace.con.lua:63` |
| **Teatro de Ópera** | 14 | 800 de pedra, 400 de vidro, 400 chapas metálicas, 400 de tecido | trens: conforto **+25 %** | `opera_house.con.lua:10-22`, `opera_house.con.lua:44`, `opera_house.con.lua:63` |
| **Palácio de Westminster** | 15 | 800 de pedra, 400 tábuas, 400 de vidro, 400 móveis | veículos rodoviários, trens, navios e aeronaves: velocidade máxima **+20 %** | `westminster.con.lua:10-22`, `westminster.con.lua:45`, `westminster.con.lua:79` |

- Cada ponto de referência é desbloqueado uma vez, pelo seu nível; como o nível cresce está em [Nível da empresa, vantagens e sede](company.html).
- Nos seus arquivos, os pontos de referência não custam nada para construir nem por ano: só a carga (`arena.con.lua:59-64`).
- O canteiro armazena metade de cada carga por vez, então precisa de pelo menos duas entregas de cada (`arena.con.lua:13-18`).

## Construindo um ponto de referência

- O canteiro tem **4 estágios**. Ele avança conforme a carga chega: estágio 2 com um terço de toda a carga, estágio 3 com dois terços, pronto com 100 %. Cada carga só conta até a sua própria quantidade, então pedra extra não compensa tábuas faltando (`landmarks.script.tl:34-46`).
- O bônus só funciona quando o ponto de referência está **pronto** (`landmark_util_serialized.tl:393-395`). A mensagem "Construção finalizada" aparece nesse momento (`landmarks.script.tl:49-61`).
- A configuração **Recursos Necessários para Marcos** multiplica toda a carga: Nenhum ×0, Baixo ×0,5, Normal ×1, Alto ×2 ou Muito Alto ×4. As predefinições são Fácil ×0,5, Normal ×1, Difícil ×2, Muito Difícil ×4. Com ×0 um ponto de referência fica pronto assim que é posicionado (`difficulty_util.tl:40`, `difficulty_util.tl:107`, `difficulty_util.tl:135`, `difficulty_util.tl:162`, `difficulty_util.tl:189`, `landmarks.script.tl:38`, `landmarks.script.tl:46`).

## Quem recebe o bônus

- O bônus vai para a cidade **mais próxima do ponto de referência**, e para os veículos do tipo de transporte indicado cuja cidade mais próxima é essa cidade (`landmark_util.tl:6-47`, `landmarks.script.tl:208-236`).
- Quando um veículo entra na área de outra cidade, ele recebe os bônus dessa cidade e perde os antigos (`landmarks.script.tl:279-299`).
- Os bônus de vários pontos de referência na mesma cidade **se somam**: duas velocidades máximas de +20 % dão +40 % (`landmark_util.tl:46`, `vehicle_modifier.script.tl:3-16`).

```engine
Qual cidade é a "cidade mais próxima" de um ponto de referência ou de um veículo em movimento é decidido pelo motor (getConstructionClosestTown, closestTown). Como o motor transforma +25 % de conforto ou +20 % de velocidade máxima em viagens e receita também é trabalho do motor.
```

```tip scripts
Coloque o Palácio de Westminster na cidade onde roda a maioria dos seus veículos: +20 % de velocidade máxima para todo tipo de transporte. Um segundo +20 % vem do Grande Farol para navios na mesma cidade. A conquista Centralização pede 10 pontos de referência prontos com a mesma cidade mais próxima, enquanto os arquivos do jogo têm 9 pontos de referência além da sede (contados); se ela pode ser obtida nesta versão é desconhecido (veja [Conquistas](achievements.html)).
```

## Celebrações

Uma celebração é a pequena festa mostrada sobre uma cidade quando algo acontece pela primeira vez. Ela também aumenta a **Reputação** da cidade, mas só quando a Reputação ainda não está cheia.

| Evento | Reputação | Fonte |
|---|---|---|
| primeiro passageiro embarca em uma das suas linhas na cidade | +50 % | `celebrations.script.tl:228-252` |
| primeira carga entregue à cidade | +50 % | `celebrations.script.tl:187-198` |
| a cidade sobe de nível | +50 % | `celebrations.script.tl:260-272` |
| primeira carga entregue a uma indústria | +20 % para a cidade mais próxima dela | `celebrations.script.tl:202-219` |

- Uma cidade que sobe de nível também ganha **fogos de artifício**, a menos que estejam desativados (`town_growth.script.tl:108-112`).
- Como a Reputação funciona: [Reputação](reputation.html).

## Elementos divertidos

- Um **dirigível** sobrevoa uma cidade quando você inicia uma Campanha de Marketing lá (`fun_elements.script.tl:112-117`).
- Um **OVNI** aparece a cada **2 a 4 anos** de tempo de jogo, escolhidos ao acaso, quando não há nenhum no mapa (`fun_elements.script.tl:10`, `fun_elements.script.tl:79-91`). Clique nele para a conquista Contato do Terceiro Grau.
- Nenhum deles muda a economia.

## Bom saber

- Escolha a cidade antes de construir: o bônus não segue suas linhas, só os veículos perto daquela cidade.
- No Muito Difícil um ponto de referência precisa de quatro vezes a carga: o Palácio de Westminster pede então 3.200 de pedra e 1.600 de cada uma das outras cargas.

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: Nove pontos de referência, um por nível de 2 a 15, cada um construído com carga entregue em 4 estágios, escalada por Recursos Necessários para Marcos de ×0 a ×4. Depois de pronto, cada um dá um bônus (+20 % de velocidade máxima, −20 % de poluição, −25 % de ruído ou +25 % de conforto) aos veículos de um tipo de transporte na cidade mais próxima; os bônus se somam. Celebrações dão 50 % ou 20 % de Reputação; um OVNI vem a cada 2 a 4 anos.
result: adds
```
