---
title: Velocidade de carga e descarga
summary: O que faz um veículo carregar rápido ou devagar em uma parada: o veículo, as seções da plataforma e o estoque que entrega ou recebe a carga.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-15
fact: ×2 | seção de plataforma especializada
fact: ×0,25 | seção errada ou trem longo demais
fact: ×4 | melhor caso: plataforma e armazém especializados
---

O tempo que um veículo passa carregando ou descarregando é a sua própria velocidade de carregamento multiplicada por dois fatores: um da **plataforma** e um do **estoque** do outro lado (armazém, indústria, município).

```diagram loading_factors
```

## 1. O veículo

Cada veículo tem uma velocidade de carregamento base, mostrada na Loja de Veículos e na janela do veículo ("2.0x"). Tudo o que vem abaixo multiplica esse valor.

## 2. O fator da plataforma

Para o jogo, uma plataforma não é uma fileira de módulos: é uma **lista de seções, uma por classe de carga**, com os comprimentos de todos os módulos daquela classe somados.

```diagram loading_sections
```

| Vagões… | Fator | Fonte |
|---|---|---|
| em uma seção da sua classe (vagões a granel, seção a granel) | **×2** | `modular_station.script.lua:1042` |
| em uma seção universal | ×1 | `modular_station.script.lua:1042` |
| sem nenhuma seção da sua classe na plataforma | **×0,25** | `cargo_react_util.tl:60` |
| além do comprimento da plataforma (trem longo demais) | **×0,25** | `cargo_react_util.tl:61` |

- O fator é uma **mistura pela fração do trem**: se 3/4 dos vagões combinam e 1/4 não, o fator é ¾ × 2 + ¼ × 0,25 ≈ ×1,56 (`cargo_react_util.tl:63-70`, a mesma divisão que o jogo mostra como "Terminal Parcialmente Especializado").
- **Onde** os vagões param na plataforma não importa, só os comprimentos somados (medido no jogo).
- Rodovias: terminais de caminhão especializados dão ×2 (`modular_terminal.script.lua:2956`); as pequenas paradas de rua são sempre ×1 (`small_stops.script.lua:19`).
- Plataformas de passageiros são ×1.

## 3. O fator do estoque

Na descarga, cada unidade vai para um destinatário: um módulo de armazém, uma indústria ou um prédio do município. O estoque do destinatário tem o seu próprio fator.

| Destinatário | Fator | Fonte |
|---|---|---|
| módulo de armazém **especializado** (líquidos, a granel, plataforma, mercadorias) | **×2** | `modules.script.lua:120`, `warehouse.script.lua:297-314` |
| armazém **universal** | ×1 | `warehouse.script.lua:272-285` |
| indústria | ×1 | medido no jogo |

- Todo módulo de armazém pede ×2, mas os módulos universais só aumentam a capacidade de **um estoque universal compartilhado**, que é criado com ×1. Só os módulos especializados têm estoque próprio com ×2.
- A dica do jogo chama esse fator de "Armazém especializado: +100%" (`cargo_react_util.tl:51-54`).
- Durante uma mesma descarga o jogo atende os destinatários **em rodízio**: por isso a velocidade muda enquanto o trem descarrega quando parte da carga vai para um armazém e parte para uma indústria (medido no jogo).

```engine
Qual destinatário recebe cada unidade, e a multiplicação final, são decididos no motor. Os fatores acima são os dados que os scripts entregam a ele; o resultado foi conferido com os valores que o motor expõe (sonda do [Detalhes das plataformas (Platform Details)](https://mod.io/g/transportfever3/m/platform-details), outubro de 2026).
```

## O que o jogo mostra

- O indicador de carregamento aparece como **acelerado** acima de ×1,5 e como **lento** abaixo de ×0,75 (`cargo_react_util.tl:119-122`).
- Passe o mouse sobre ele: a dica lista "Terminal Especializado", "As especializações não correspondem", "Terminal pequeno demais" e "Armazém especializado", cada um com a sua porcentagem (`cargo_react_util.tl:76-99`).

## Exemplo

Um trem de 8 vagões a granel, com 160 m, descarregando carvão.

| Estação | Plataforma | Destinatário | Fator |
|---|---|---|---|
| plataforma universal de 160 m | ×1 | usina siderúrgica | **×1** |
| plataforma a granel de 160 m | ×2 | usina siderúrgica | **×2** |
| plataforma a granel de 160 m | ×2 | armazém a granel especializado | **×4** |
| plataforma a granel de 160 m | ×2 | armazém universal | **×2** |
| plataforma universal de 120 m (trem 40 m longo demais) | ¾ × 1 + ¼ × 0,25 ≈ ×0,81 | usina siderúrgica | **×0,81** |

## Onde a carga é descarregada

Cada parada de uma linha tem uma lista **Volume**, na janela "Filtro de Cargas" da parada. Na parada, o veículo mantém a bordo a carga dessa lista; o resto é descarregado em qualquer estoque da área de cobertura que o aceite, armazéns incluídos (medido no jogo).

- É assim que um trem acaba se esvaziando num armazém no meio da linha. No jogo: numa parada ao lado de um armazém, com só plástico na lista, as ferramentas a bordo foram para o armazém, embora ele estivesse quase cheio.
- Uma plataforma de passageiros não transfere carga: ali a carga fica a bordo (medido no jogo).
- Para manter a carga a bordo, adicione-a à lista Volume dessa parada.

```tip
**A carga some numa parada ao lado de um armazém? Adicione-a à lista Volume dessa parada.** Tudo o que não está na lista é descarregado em um estoque ao alcance, e o armazém não paga nada.
```

| Opção de "Filtro de Cargas" | O que faz | Fonte |
|---|---|---|
| "Forçar descarregamento de todas as cargas na chegada" | descarrega nos estoques compatíveis mesmo cheios; o que não cabe é destruído. Desligada numa parada nova. | `cargofilter_window.tl:757`, `line_util.tl:476` |
| "Destruir cargas na chegada quando a configuração mudar" | destrói a carga a bordo quando outra carga espera para ser carregada nesta parada | `cargofilter_window.tl:767` |
| "Substituir com carga mais nova, se disponível" | destrói a carga que voltou à parada onde foi carregada, quando há carga mais nova do mesmo tipo esperando | `cargofilter_window.tl:778` |

- Com a primeira opção desligada, o ícone da carga mostra "≤" e a dica "Descarregar somente se os estoques tiverem capacidade" (`cargofilter_window.tl:124`, `cargofilter_window.tl:158`).

## Várias cargas na mesma linha

- A lista Volume de uma parada é um sim/não por tipo de carga, **sem ordem**: o jogador não pode definir qual carga é carregada primeiro. Os ícones são apenas desenhados na ordem de cargas do jogo (`line_util.tl:471-475`, `line_util.tl:510`, `cargofilter_window.tl:533-535`).
- Um vagão ou caminhão que leva várias cargas tem, por compartimento, várias **configurações de carga**; a capacidade do compartimento é a maior delas, não a soma (`model_metadata_util.lua:682-733`, `vehicle_metadata_util.lua:27-37`). Por isso ele leva uma delas de cada vez.
- Veículos novos têm a escolha automática de configuração ligada em todos os compartimentos (`vehicle_react_util.tl:339`), e o jogo não tem janela para escolher à mão a carga de um veículo.
- Passageiros e carga podem dividir uma linha: os scripts nunca recusam carga numa parada por ela também receber passageiros (`line_util.tl:1381-1386`). A carga só é retirada de uma parada cujo terminal não pode carregar nem descarregar carga (`line_util.tl:554-559`).
- Com várias cargas, **Carga Completa (Qualquer)** e **Carga Completa (Tudo)** se comportam de forma diferente: veja [Configurações de partida: carga completa, Nível de Preenchimento e tempos de parada](departure.html).
- Quando a configuração não serve, a linha mostra **Algumas configurações de tipos de carga desta linha estão em conflito**, por exemplo "Nenhum veículo na linha pode transportar parte da carga configurada para transporte." (`line_warning.script.tl:10-36`).

```engine
A ordem em que várias cargas são carregadas, como um estoque compartilhado é dividido entre os veículos que esperam e como um veículo escolhe a sua configuração de carga são decididos pelo motor.
```

## A configuração automática

Enquanto ninguém salvar uma mudança na janela "Filtro de Cargas" de uma parada, o que a desliga de vez nessa linha (`line_util.tl:495-498`, `cargofilter_window.tl:438`), o próprio jogo preenche as listas Volume cada vez que a linha é criada, uma parada é adicionada ou removida, as paradas são reordenadas ou um ponto de passagem é adicionado (`manager_window.tl:6712`, `:6786`, `:6845`, `:6879`, `:6963`). Mover uma parada para outra estação ou plataforma, e remover ou mover um ponto de passagem, não a executam (`manager_window.tl:6851-6868`, `manager_window.tl:6968-6987`).

- Ela recomeça de listas vazias, com passageiros nas estações de passageiros (`line_util.tl:542-588`).
- Ela procura produtores e consumidores só entre indústrias e prédios da cidade: armazéns não contam (`cargo_util.tl:518-526`).
- Ela coloca uma carga na lista Volume de uma parada quando a carga é necessária mais adiante e nada na parada a aceita. Um armazém conta como se aceitasse tudo o que armazena (`line_util.tl:676-693`): numa parada ao lado de um armazém que guarda essa carga, a carga fica fora da lista e o trem a descarrega ali.
- Assim que um filtro é mudado à mão, a linha fica marcada como personalizada (`cargofilter_window.tl:438`) e a configuração automática nunca mais mexe nela, nem quando paradas são adicionadas depois (`line_util.tl:496`).

```engine
Os scripts só escrevem as listas Volume; a descarga em si é feita pelo motor. A regra acima (o que não está na lista é descarregado em qualquer estoque que o aceite) foi observada no jogo com [Platform Details](https://mod.io/g/transportfever3/m/platform-details), novembro de 2026.
```

## Bom saber

- Estações dentro de uma indústria são sempre especializadas na carga de que a indústria precisa (wiki oficial).
- Módulos de armazém especializados também congelam o prazo de entrega da carga que guardam (wiki oficial); um armazém universal não.
- O [Detalhes das plataformas (Platform Details)](https://mod.io/g/transportfever3/m/platform-details) mostra os dois fatores de cada veículo na plataforma e para onde foi a carga descarregada.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Armazéns especializados "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Seção especializada ×2, universal ×1, nenhuma seção compatível ×0,25, além da plataforma ×0,25, misturados pela fração do trem; módulo de armazém especializado ×2, armazém universal ×1.
result: refines
```
