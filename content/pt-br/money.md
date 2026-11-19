---
title: Por que estou perdendo dinheiro?
summary: O que paga, o que custa, e uma verificação em seis passos para achar as linhas que perdem dinheiro e por quê, com links para as páginas que explicam cada ponto.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-15
game: 40444
fact: 1 | pagamento por item, no consumidor, pela linha reta
fact: 0 | pago num armazém ou numa transferência
fact: 100 % | pago mesmo atrasado
fact: ×6 | fator de ano exibido na manutenção de armazéns, aeródromos, aeroportos e portos em 2020
---

Uma entrega paga por **uma única linha reta**, de onde a carga foi produzida até onde ela é usada, e só quando chega lá. Tudo o que você constrói e compra custa dinheiro todo ano, uma parte cada vez mais com o ano do calendário. Uma linha perde dinheiro quando a sua parte dos pagamentos é menor que os custos que ela traz.

```diagram money_flow
```

## O que paga

- **A distância em linha reta** da fonte ao consumidor, mais 8 × a subida. O comprimento da sua rota não conta (`cargo_income.script.lua:3-7`, `cargo_income.script.lua:5`).
- **Toda carga paga o mesmo** por quilômetro: o fator de renda é 3,8 para todas (`cargotype.script.lua:7-13`).
- **Uma vez, no consumidor.** Descarregar num armazém ou numa estação de transferência não paga nada. O pagamento é depois dividido entre as linhas da cadeia pelo comprimento em linha reta de cada trecho (medido no jogo).
- **Carga atrasada é paga por inteiro**: o tempo de viagem não é usado (`cargotype.script.lua:7-13`). O atraso baixa em vez disso a classificação **Entrega** do município.
- **O ranque da empresa** baixa toda a renda com a configuração **Inflação**: no ranque 15, ×0,75 em Normal (`company_progression_util.tl:25-40`).
- Um **subsídio cumprido** dobra, por 5 anos, a renda das entregas que cobre: para a sua indústria, para o seu município ou passageiros entre os seus dois municípios, só nas suas linhas (`subvention_util.tl:286`). Veja [Subsídios: ofertas, prazos e recompensas](subsidies.html).

Detalhes: [Renda por carga e tempo de entrega](income.html).

## O que custa

- **Veículos**: os custos operacionais seguem a velocidade média × a capacidade, e o preço vale 6 anos de custos operacionais (`model_metadata_util.lua:499-518`, `model_metadata_util.lua:548-549`).
- **Trilhos e estradas**: cerca de um sexto do preço de construção por km e por ano; trilho de alta velocidade custa 9 vezes o trilho simples (`simple.street_template.lua:33`, `high_speed.street_template.lua:35`).
- **Garagens, estações, armazéns, portos, aeroportos**: as variantes de eras posteriores custam ×3 e ×9 (`rail_depot.con.lua:7`, `warehouse.tl:48`), e para armazéns, aeródromos, aeroportos e portos a janela do prédio mostra uma manutenção que segue o ano, de ×1 em 1900 a ×6 em 2020 (`mod.script.tl:92-100`, `entity_window_util.tl:188-192`). O que é cobrado é decidido pelo motor.
- **Empréstimos**: a taxa é cobrada uma vez sobre o valor, distribuída ao longo do prazo (`loan_util.tl:102-111`).
- **A Inflação não aumenta nenhum custo**. Ela só baixa a renda.

Detalhes: [Custos, manutenção e empréstimos](costs.html).

## Seis verificações, em ordem

```diagram money_check
```

1. **Quais linhas perdem dinheiro?** Olhe o saldo de cada linha, não o total da empresa. O mod [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) mostra o saldo de cada linha nos últimos 12 meses e a sua média de vários anos.
2. **A carga vai longe?** Só a linha reta da fonte ao consumidor paga. Uma linha alimentadora curta até um armazém recebe só a parte do seu próprio trecho curto ([Renda por carga e tempo de entrega](income.html)).
3. **Ela anda cheia?** Um veículo custa o mesmo cheio ou vazio. Olhe as voltas vazias, o **Nível de Preenchimento** e a **carga completa** de cada parada ([Configurações de partida: carga completa, Nível de Preenchimento e tempos de parada](departure.html)).
4. **É descarregada onde paga?** O que não está na lista Volume de uma parada é descarregado em qualquer estoque próximo, armazéns incluídos, e um armazém não paga nada ([Velocidade de carga e descarga](loading.html), [Armazéns](warehouses.html)). A carga que não cabe em estoques cheios do município fica a bordo ([Crescimento dos municípios: XP, classificações e tamanho](towns.html)).
5. **Veículo demais?** Velocidade e capacidade custam dinheiro, mas velocidade não paga: só ajuda quando dá mais viagens por ano. Na cidade, um ônibus velho e lento pode ser mais lucrativo que um novo e rápido ([Custos, manutenção e empréstimos](costs.html)).
6. **Custos fixos.** Garagens, módulos extras de armazém, trilhos rápidos e prédios de uma era posterior custam todo ano, usados ou não ([Custos, manutenção e empréstimos](costs.html)).

## Bom saber

- **Escolha as cargas por volume e distância**, não por preço: toda carga paga o mesmo por km.
- Uma **linha principal longa** alimentada por linhas curtas ganha a maior parte do dinheiro; as alimentadoras mostram saldos pequenos, mas o que conta é a cadeia inteira.
- **Mais para transportar**: uma indústria reforçada produz mais ([Trabalhadores e o reforço de trabalhadores](workers.html), [Indústrias](industries.html)), e um município maior pede mais carga.
- Acelerar uma linha não aumenta o pagamento por item. Só ajuda se os mesmos veículos fizerem mais viagens.

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks))
scripts: Igual: linha reta mais 8 × subida, o mesmo fator para toda carga, tempo de viagem não usado; medido no jogo: pago uma vez no consumidor e dividido pelo comprimento do trecho; os custos seguem velocidade × capacidade nos veículos, 1/6 do preço nos trilhos, variantes de era ×3 / ×9 e fator de ano de ×1 a ×6 nos prédios; a Inflação só baixa a renda.
result: refines
```
