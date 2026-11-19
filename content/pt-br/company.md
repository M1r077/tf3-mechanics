---
title: Nível da empresa, vantagens e sede
summary: O que aumenta o nível da sua empresa, o que cada nível desbloqueia, como funcionam licenças e prospecções, o que a sede dá de verdade e quanto um nível mais alto custa para você.
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40444
fact: 15 | níveis de empresa, de Júnior a Magnata
fact: ×12,5 | população mundial necessária para o nível 15, comparada com o início
fact: ×0,75 | de receita no nível 15 com Inflação Normal
fact: 0 | níveis perdidos quando a população cai
---

O nível da sua empresa não vem do dinheiro nem das entregas: vem da **população do mapa inteiro**. Cada novo nível desbloqueia vantagens (pontos de referência, prospecções, Campanhas de Marketing, Ecologização industrial, módulos da sede) e, com a opção **Inflação**, também baixa um pouco toda a sua receita.

## O que aumenta o nível

- O jogo guarda a **população mundial no início** do jogo: os habitantes de todos os municípios (`company.script.tl:392-396`, `company_util.tl:365-371`).
- Depois compara a **maior** população mundial já alcançada com esse valor inicial (`company_growth.script.tl:25-27`). O valor só sobe: municípios que encolhem nunca custam um nível.
- O nível 1 é alcançado no valor inicial, o nível 15 em cerca de **12,5 vezes** esse valor (`company_progression_util.tl:6-14`, `company_progression_util.tl:95-120`, `town_growth_function.tl:13-20`).
- Não há nível nas missões de campanha nem no editor de mapas (`company_growth.script.tl:74-79`).

| Nível | Cargo | População mundial, comparada com o início |
|---|---|---|
| 1 | Júnior | ×1 |
| 2 | Mecânico | ×1,02 |
| 3 | Engenheiro | ×1,08 |
| 4 | Coordenador | ×1,2 |
| 5 | Perito | ×1,4 |
| 6 | Líder de Equipe | ×1,7 |
| 7 | Supervisor | ×2,1 |
| 8 | Gerente | ×2,6 |
| 9 | Diretor | ×3,3 |
| 10 | Diretor Sênior | ×4,2 |
| 11 | CEO | ×5,3 |
| 12 | Presidente Executivo | ×6,7 |
| 13 | Vice-Presidente | ×8,3 |
| 14 | Presidente | ×10,2 |
| 15 | Magnata | ×12,5 |

As proporções foram calculadas a partir dos scripts para uma população inicial de 50.000 ou mais (`company_progression_util.tl:6-14`, `company_static_util.tl:6-24`). Num mapa pequeno elas são um pouco maiores nos níveis do meio (o nível 8 pede ×2,85 com 5.000 habitantes); os níveis 1 e 15 ficam em ×1 e ×12,5.

- O nível segue, portanto, o **crescimento dos municípios**: eles crescem com seus passageiros e cargas, veja [Crescimento dos municípios](towns.html).
- Os primeiros níveis chegam rápido; os últimos exigem municípios muitas vezes maiores.

## Um novo nível é aplicado na janela da empresa

Quando a população passa de um limite, aparece uma **notificação de subida de nível**; clicar nela abre a janela da empresa nesse nível (`company_growth.script.tl:96-107`, `company_notification_rank_up.script.tl:8-9`).

- As novas vantagens só são desbloqueadas quando esse nível é **selecionado na janela da empresa**: a janela então envia o desbloqueio (`company.tl:420-423`, `company_growth.script.tl:55-62`). Os menus de construção verificam esse nível aplicado (`company_util.tl:92`, `company_util.tl:171-178`).
- O multiplicador de receita da próxima seção segue o nível **alcançado**, aplicado ou não (`company_growth.script.tl:47-48`).

```tip scripts
Depois de subir de nível, clique na notificação (ou abra a janela da empresa e selecione o novo nível) para receber as vantagens. Esperar não dá nada: a receita já foi reduzida.
```

## Quanto custa um nível mais alto: a opção Inflação

Com **Inflação**, toda a receita de cargas e passageiros cai de forma uniforme de ×1 no nível 1 até um mínimo no nível 15 (`company_progression_util.tl:25-40`, `company_growth.script.tl:159-170`).

| Inflação | Receita no nível 15 | Fonte |
|---|---|---|
| Nenhuma | ×1 (sem mudança) | `difficulty_util.tl:50`, `mod.script.tl:695-698` |
| Baixa | ×0,9 | |
| Normal | ×0,75 | |
| Alta | ×0,6 | |
| Muito Alta | ×0,5 | |

- Em Normal, cada nível custa cerca de 1,8 % da receita: ×0,96 no nível 3, ×0,875 no nível 8, ×0,75 no nível 15.
- A Inflação não aumenta nenhum custo; os custos seguem o ano do calendário (veja [Custos, manutenção e empréstimos](costs.html)).
- Um nível mais alto também torna as novas ofertas de subsídio mais raras (veja [Subsídios](subsidies.html)).

## Licenças

A maioria das vantagens é limitada por **licenças**. Um nível dá licenças para uma vantagem; cada edifício ou uso consome uma (`company_util.tl:33-80`, `company_util.tl:206`).

- As licenças **se somam** ao longo dos níveis: uma vantagem que dá 1 no nível 3 e 1 no nível 5 permite 2 a partir do nível 5 (`company_util.tl:51-56`).
- Um edifício devolve sua licença quando é demolido: o jogo conta o que está de pé (`company_util.tl:143-163`, `company_util.tl:203-206`).
- Prospecções, Campanhas de Marketing e Ecologização consomem uma licença ao começar (`company.script.tl:416-423`, `company.script.tl:459-462`, `company.script.tl:496-500`). O menu de construção mostra então **Já utilizado** ou **Recarga** (`company_util.tl:207-226`).
- A licença de **Marketing** volta **5 anos** depois de cada campanha (`marketing.res.lua:6-7`, `company.script.tl:66-94`).

| Vantagem | Licenças | Fonte |
|---|---|---|
| Sede | 1 no nível 1 | `hq.res.lua:6` |
| Campanha de Marketing | 1 no nível 4, volta após 5 anos | `marketing.res.lua:6-7` |
| Ecologização industrial | 1 nos níveis 3, 6, 9, 12 e 15 | `industry_greenify_tool.script.tl:101-102` |
| Estação de Limpeza | 15 no nível 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Pontos de referência | um de cada: Anfiteatro 2, Grande Farol 5, Castelo de Himeji 7, Museu Naval 9, Castelo Neuschwanstein 10, Estátua da Liberdade 11, Palácio de Verão 13, Teatro de Ópera 14, Palácio de Westminster 15 | `arena.con.lua:39`, `lighthouse.con.lua:48`, `white_heron_castle.con.lua:47`, `ship_museum.con.lua:55`, `neuschwanstein.con.lua:55`, `statue_of_liberty.con.lua:57`, `summer_palace.con.lua:63`, `opera_house.con.lua:63`, `westminster.con.lua:79` |

O que cada vantagem faz: [Reputação](reputation.html) (Campanha de Marketing), [Poluição e ruído](emission.html) (Ecologização, Estação de Limpeza).

## Prospecções

Uma prospecção procura um recurso perto de um município e, se tiver sucesso, funda ali uma nova indústria.

| Recurso | Nível | Fonte |
|---|---|---|
| Peixes | 2 | `exploration_fish.res.lua:9-11` |
| Argila | 3 | `exploration_clay.res.lua:9-11` |
| Petróleo Bruto | 4 | `exploration_crude_oil.res.lua:9-11` |
| Grãos, vegetais | 4, **uma licença compartilhada** (Indústria) | `exploration_grain.res.lua:9`, `exploration_vegetables.res.lua:9`, `permit_key_farm.res.lua:6` |
| Troncos | 5 | `exploration_logs.res.lua:9-11` |
| Carvão, minério de ferro | 6 | `exploration_coal.res.lua:9-11`, `exploration_iron_ore.res.lua:9-11` |
| Pedra, lã | 8 | `exploration_stone.res.lua:9-11`, `exploration_wool.res.lua:9-11` |
| Areia | 9 | `exploration_sand.res.lua:9-11` |
| Borracha | 12 | `exploration_rubber.res.lua:9-11` |

- Cada recurso tem **uma** licença, consumida quando a prospecção começa (`company.script.tl:451-462`).
- Ela dura até **6 meses**. Uma vez por mês tenta colocar a indústria, com uma chance que sobe de 20 % a 60 % ao longo dos 6 meses (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`).
- Uma tentativa também falha quando o jogo não encontra lugar para essa indústria perto do município (`company.script.tl:199-210`).
- Se a última tentativa falhar, **a licença volta** e uma notificação avisa (`company.script.tl:106-126`, `company.script.tl:170-181`).
- Só pode haver uma prospecção por vez por município e recurso (`company.script.tl:442-447`).

```engine
Onde a nova indústria pode ficar (makeIndustrySpawnProposal perto do município) é decidido pelo motor: uma prospecção de peixes longe da água, ou um município sem terreno livre ao redor, simplesmente falha e devolve a licença.
```

## A sede

| O quê | Valor | Fonte |
|---|---|---|
| Preço e manutenção | grátis, sem manutenção | `headquarter.script.tl:526-527` |
| Licença | 1, no nível 1 | `headquarter.con.lua:6-7`, `hq.res.lua:6` |
| Crescimento do município | +5 % para o município mais próximo | `headquarter.script.tl:510-515`, `landmark_util.tl:51-70` |
| Empregos | 24 | `headquarter.con.lua:16`, `headquarter.script.tl:505-508` |

- Os +5 % são um bônus sobre a taxa de crescimento desse município, então não fazem nada quando a taxa é 0 % (veja [Crescimento dos municípios](towns.html)).
- Os **módulos** custam 50.000 cada e são limitados por licenças que aumentam com o nível (`hq_module_m.module.lua:83`, `hq_module_m.module.lua:137`).
- Só dois módulos têm bônus nos arquivos: **Edifício Médio** +1 % de crescimento do município (`hq_module_m.module.lua:139-142`) e **Edifício Grande** +1 % de Recuperação da Reputação (`hq_module_l.module.lua:169-172`). O bônus de recuperação não é lido por nenhuma avaliação do município (veja [Reputação](reputation.html)). Os outros módulos são decorativos.
- Cada arquivo de módulo também começa com uma tabela que dá +5 % de crescimento, mas nada no arquivo a usa (`hq_corner_l.module.lua:148-159`, `hq_statue.module.lua:46-57`). Só o bônus dentro do `metadata` do módulo é somado (`headquarter_addon.script.tl:18-29`).

| Módulo | Licenças ganhas no nível (×2 = duas) | Total no nível 15 |
|---|---|---|
| Bandeira de Chão | 1 ×2, 6, 7, 8, 9, 11, 12, 13, 14 | 10 |
| Edifício de Esquina | 3, 5, 7 ×2, 9, 11, 13, 15 | 8 |
| Edifício Médio | 2, 4, 10 ×2, 15 ×2 | 6 |
| Edifício Grande | 5, 6, 10, 12 | 4 |
| Varanda | 8 ×2, 14 ×2 | 4 |
| Fonte Grande | 10 ×2, 14 ×2 | 4 |
| Cúpula | 6, 15 ×2 | 3 |
| Bandeira de Telhado | 7, 10, 13 | 3 |
| Quadra de Tênis | 11, 12, 14 | 3 |
| Árvore Antiga | 13, 15 ×2 | 3 |
| Estátua | 14 ×2 | 2 |
| Piscina | 15 | 1 |

Fontes: a linha `rankAndPermits` de cada arquivo de módulo (`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`).

```tip scripts
Coloque a sede no município que você quer fazer crescer mais rápido e adicione Edifícios Médios ali: são os únicos módulos com bônus de crescimento.
```

## Bom saber

- Para subir de nível, faça os municípios crescerem: mais passageiros e cargas para mais municípios, com boas avaliações. Dinheiro no banco não conta.
- Planeje seus pontos de referência e prospecções: cada um vem uma vez, num nível fixo.
- Num mapa com Inflação, subir de nível é bom para as vantagens e ruim para a receita. Em Normal, o caminho inteiro até o nível 15 custa um quarto de toda a receita.

```check
official: "The company rank depends on the population of the map. … Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Mesma regra: a maior população mundial alcançada, comparada com a população no início, ×12,5 para o nível 15; nunca perdida. Um novo nível precisa ser selecionado na janela da empresa para desbloquear suas vantagens, enquanto a Inflação reduz a receita na hora. Só dois módulos têm bônus (Edifício Médio +1 % de crescimento, Edifício Grande +1 % de Recuperação da Reputação, que nenhuma avaliação lê); os outros são decorativos.
result: refines
```
