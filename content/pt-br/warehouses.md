---
title: Armazéns
summary: Módulos universais ou especializados, o que cada estoque guarda, fixar um tipo de carga, velocidade de carregamento, custos e poluição, e o que um armazém não faz.
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
fact: 500 | unidades de carga por módulo, qualquer que seja o tipo
fact: ×2 | velocidade de carregamento num módulo especializado, ×1 num universal
fact: 150.000 / 300.000 | preço de um módulo universal / especializado
fact: 0 | de renda pela carga descarregada num armazém
---

Um armazém é uma entrada e um conjunto de **módulos**. Ele guarda carga entre duas linhas: uma linha a descarrega, outra a carrega de novo. As estações chegam até ele pela sua área de cobertura; municípios e indústrias nunca tiram nada dele (wiki oficial).

## Módulos universais ou especializados

| Módulo | Estoque | Guarda | Fator de carregamento | Fonte |
|---|---|---|---|---|
| **Armazém Universal** | todos os módulos universais dividem **um** estoque | qualquer carga, misturada | ×1 | `warehouse.script.lua:272-295`, `modules.script.lua:49` |
| **Armazém de Líquidos**, **Armazém de Mercadorias a Granel**, **Armazém de Plataforma**, **Armazém de Mercadorias** | **um estoque por módulo** | um tipo de carga por vez, da sua classe | ×2 | `warehouse.script.lua:296-314`, `modules.script.lua:120`, `modules.script.lua:165`, `modules.script.lua:247`, `modules.script.lua:296` |

- Cada módulo soma **500** unidades (`modules.script.lua:49`, `modules.script.lua:120`). Cinco módulos universais formam um estoque de 2.500; cinco módulos de líquidos formam cinco estoques de 500.
- Passageiros nunca são armazenados (`warehouse.script.lua:279`, `warehouse.script.lua:304`).
- Um módulo especializado aceita um tipo de carga por vez: para guardar petróleo bruto e combustível você precisa de dois módulos de líquidos (wiki oficial).
- O ×2 de um módulo especializado se multiplica pelo fator da plataforma: uma plataforma a granel e um módulo a granel dão ×4. Detalhes: [Velocidade de carga e descarga](loading.html).

## Universal ou especializado?

1. **Muitos tipos de carga, pequenas quantidades**: universal. Um estoque compartilhado, metade do preço e metade da poluição.
2. **Uma carga em grandes quantidades** (carvão, petróleo bruto, toras): especializado. Os veículos descarregam e carregam ali duas vezes mais rápido, mas você precisa de um módulo por tipo de carga.
3. **Alimentos e outras cargas com prazo de entrega curto**: especializado; a wiki oficial diz que esses módulos congelam o prazo de entrega (veja abaixo).
4. Os dois tipos podem ser misturados num armazém: os módulos universais continuam formando um estoque, cada módulo especializado o seu próprio.

## Um armazém acelera a descarga?

- **Módulo especializado**: sim, ×2 para a carga que ele aceita. A dica de carregamento do veículo mostra "Armazém especializado: +100%" (`cargo_react_util.tl:51-54`).
- **Módulo universal**: não. O estoque dele é criado com ×1; o ×2 pedido pelo módulo é ignorado (`warehouse.script.lua:284`, `warehouse.script.lua:288-289`).
- Quando parte da carga vai para um armazém e parte para uma indústria, o veículo os atende em rodízio, então a velocidade muda durante uma mesma parada (medido no jogo, veja [Velocidade de carga e descarga](loading.html)).

## A seção Estoques

- Uma linha por estoque: a carga que ele aceita, a quantidade e, ao passar o mouse, o **Tempo médio restante de entrega** (`entity_window_util.tl:408-410`).
- **Fixar um tipo de carga**: num módulo especializado, clique num ícone de carga. O jogo reconstrói o armazém com esse módulo reservado a essa carga (`entity_window_util.tl:339-367`, `warehouse.script.lua:308`). Remover ou substituir o módulo apaga a fixação (`warehouse.script.lua:403-405`).
- **Descartar Toda a Carga**: esvazia essa linha de uma vez (`entity_window_util.tl:423-434`). A carga é perdida.
- Os dois botões só existem nos seus próprios armazéns (`warehouse_eow.script.tl:127-137`, `gui/entity_window/warehouse/warehouse.tl:38`).
- O gráfico **Estatísticas** mostra **Entrada** (descarregado) e **Saída** (carregado) por ano (`warehouse_eow.script.tl:159-160`).

## Custos e poluição

| | Módulo universal | Módulo especializado | Fonte |
|---|---|---|---|
| Preço | 150.000 | 300.000 | `wh_universal.module.lua:18`, `wh_liquid.module.lua:22` |
| Manutenção por ano | 25.000 | 50.000 | `wh_universal.module.lua:19`, `wh_liquid.module.lua:23` |
| Ruído | 20 | 20 | `wh_universal.module.lua:33`, `wh_liquid.module.lua:37` |
| Poluição | 25 | 50 | `wh_universal.module.lua:34`, `wh_liquid.module.lua:38` |

- O armazém soma a sua própria poluição: **25**, ou **50** assim que um módulo especializado é construído (`warehouse.script.lua:327`, `warehouse.script.lua:338-345`).
- O menu de construção tem uma entrada por classe e era (a partir de 1900, 1940 e 1980) (`warehouses/warehouse.tl:3-5`); as eras seguintes mostram ×3 e ×9, e a manutenção dos armazéns também cresce com o ano. Detalhes: [Custos, manutenção e empréstimos](costs.html).
- Módulos a granel, de plataforma e de mercadorias custam o mesmo que os de líquidos (`wh_bulk.module.lua:22-23`, `wh_flatbed.module.lua:22-23`, `wh_goods.module.lua:18-19`).

```engine
Os scripts dão dois níveis de emissão, o segundo o dobro do primeiro (`warehouse.script.lua:342-343`); o armazém passa do primeiro ao segundo à medida que os estoques enchem, estoques cheios = o dobro (`emissions.script.tl:237-249`). O preço realmente cobrado pelos módulos é calculado pelo motor.
```

## O que um armazém não faz

- **Ele não paga nada.** Descarregar num armazém não dá renda; a carga é paga uma vez, quando chega ao consumidor, pela distância em linha reta desde a origem (medido no jogo, veja [Renda por carga e tempo de entrega](income.html)).
- **Ele não abastece municípios nem indústrias** próximos: eles só recebem carga de veículos (wiki oficial).
- **Ele não é destino para a configuração automática da linha**, que só procura produtores e consumidores; mas uma parada ao lado de um armazém que guarda uma carga deixa essa carga fora da lista Volume, então os trens a descarregam ali (veja [Velocidade de carga e descarga](loading.html)).
- **Ele não precisa de estrada.** A entrada se encaixa numa rua, mas a carga só se move pelas áreas de cobertura das estações (`warehouse.script.lua:386-389`, wiki oficial). A janela do armazém mostra a área de cobertura dele (`gui/entity_window/warehouse/warehouse.tl:88-96`).

```engine
Para onde vai a carga descarregada, e se o prazo de entrega de uma carga armazenada para, é decidido pelo motor. Nenhum script congela o prazo: a wiki oficial diz que os módulos especializados congelam, e um universal não.
```

## Bom saber

- Confira a lista Volume de cada parada perto de um armazém: o que não está nela é descarregado no armazém, mesmo no meio da linha.
- Um estoque cheio recusa mais carga, a menos que a parada use "Forçar descarregamento de todas as cargas na chegada", que destrói o que não cabe (veja [Velocidade de carga e descarga](loading.html)).
- Para manter um módulo especializado para uma carga, fixe o tipo de carga dele na seção Estoques.
- O [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) lista, por estação, os armazéns ao alcance com os seus estoques; o [Detalhes das plataformas (Platform Details)](https://mod.io/g/transportfever3/m/platform-details) mostra para onde foi a carga descarregada.

```check
official: "Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types." Armazéns especializados "freeze the cargo item's delivery timer" e "enable faster loading / unloading speeds". "In specialized warehouses, only one cargo type can be stored at a time for a given module." ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Módulos universais formam um estoque compartilhado com fator de carregamento ×1, cada módulo especializado um estoque próprio de 500 com ×2 e um tipo de carga. Um módulo especializado custa o dobro (300.000, manutenção 50.000) e polui o dobro (50). O congelamento do prazo não está nos scripts.
result: refines
```
