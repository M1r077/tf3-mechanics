---
title: Улицы, пути, мосты и сигналы
summary: Скорость, цена и обслуживание каждого типа путей и улиц, сколько стоят и что позволяют мосты, туннели, переезды и сигналы, что на самом деле меняют аллеи и шумозащитные экраны, и где описаны депо.
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40425
fact: 100 / 160 / 350 км/ч | простые, обычные и скоростные пути
fact: ×9 | цена и обслуживание скоростных путей по сравнению с простыми
fact: +30 % | к цене путей за контактную сеть
fact: -65 % | шума улицы или путей с шумозащитным экраном
---

У каждого типа улиц и путей есть максимальная скорость, цена за метр и обслуживание за метр в год, всё записано в его файле. Мосты, переезды и некоторые украшения улиц добавляют собственное ограничение скорости. Расходы ниже указаны при **Стоимость инфраструктуры** и **Обслуживание инфраструктуры** 100 % (см. [Расходы, обслуживание и займы](costs.html)).

## Пути

| Пути | С | Максимальная скорость | Постройка за км | Обслуживание за км в год | Источник |
|---|---|---|---|---|---|
| Простые пути | начало | 100 км/ч | 60 000 | 10 000 | `simple.street_template.lua:9`, `simple.street_template.lua:28`, `simple.street_template.lua:33` |
| Обычные пути | 1930 | 160 км/ч | 180 000 | 30 000 | `standard.street_template.lua:4`, `standard.street_template.lua:11`, `standard.street_template.lua:30`, `standard.street_template.lua:35` |
| Скоростные пути | 1980 | 350 км/ч | 540 000 | 90 000 | `high_speed.street_template.lua:4`, `high_speed.street_template.lua:11`, `high_speed.street_template.lua:30`, `high_speed.street_template.lua:35` |

- **Контактная сеть** стоит на **30 %** больше путей (`mod.script.tl:24-25`). Она доступна с 1921 года на простых путях и с самого появления каждого более нового типа (`simple_catenary.street_template.lua:4`). По файлам она ничего не добавляет в год: у электрифицированного варианта то же обслуживание (`simple_catenary.street_template.lua:34`).
- Все три типа допускают одинаковые уклоны и кривые: **8,5 %** при строительстве (ползунок «Наклон» доходит до этого значения), не более 13 % для формы путей, и радиус кривой 55 м при строительстве, не менее 40 м (`standard.street_template.lua:36-37`, `standard.street_template.lua:48-49`, `construction_react_util.tl:241-242`, `construction_react_util.tl:1821`).
- Загрязнение от самих путей растёт с типом: 2, 4 и 6 (`simple.street_template.lua:18`, `standard.street_template.lua:20`, `high_speed.street_template.lua:20`).

```engine
Насколько кривая снижает скорость поезда (speedCoeffs каждого типа путей) и какую скорость инструмент строительства показывает для кривой, вычисляет движок.
```

```tip scripts
Скоростные пути стоят в 9 раз дороже простых, и при постройке, и каждый год. Прокладывайте их только там, где поезда действительно идут быстрее 160 км/ч; в остальных местах хватит обычных путей, а для медленных грузовых веток - простых.
```

## Улицы

| Улица | Годы | Максимальная скорость | Постройка за км | Обслуживание за км в год | Источник |
|---|---|---|---|---|---|
| Узкая улица (старая) | до 1940 | 20 км/ч | 36 000 | 6 000 | `town_old_xsmall.street_template.lua:4-5`, `town_old_xsmall.street_template.lua:8`, `town_old_xsmall.street_template.lua:27`, `town_old_xsmall.street_template.lua:56` |
| Небольшая улица (старая) | до 1940 | 40 км/ч | 60 000 | 10 000 | `town_old_small.street_template.lua:8`, `town_old_small.street_template.lua:27`, `town_old_small.street_template.lua:56` |
| Широкая улица (старая) | до 1940 | 60 км/ч | 180 000 | 30 000 | `town_old_large.street_template.lua:8`, `town_old_large.street_template.lua:27`, `town_old_large.street_template.lua:88` |
| Узкая улица (новая) | с 1940 | 30 км/ч | 120 000 | 20 000 | `town_new_xsmall.street_template.lua:4`, `town_new_xsmall.street_template.lua:11`, `town_new_xsmall.street_template.lua:30`, `town_new_xsmall.street_template.lua:59` |
| Небольшая улица (новая) | с 1940 | 50 км/ч | 180 000 | 30 000 | `town_new_small.street_template.lua:11`, `town_new_small.street_template.lua:30`, `town_new_small.street_template.lua:59` |
| Средняя улица (новая) | с 1940 | 50 км/ч | 360 000 | 60 000 | `town_new_medium.street_template.lua:11`, `town_new_medium.street_template.lua:30`, `town_new_medium.street_template.lua:75` |
| Широкая улица (новая) | с 1940 | 60 км/ч | 540 000 | 90 000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:30`, `town_new_large.street_template.lua:91` |
| Маленькая проселочная дорога (старая) | до 1940 | 60 км/ч | 60 000 | 10 000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:29`, `country_old_small.street_template.lua:58` |
| Маленькая проселочная дорога (новая) | с 1940 | 80 км/ч | 180 000 | 30 000 | `country_new_small.street_template.lua:10`, `country_new_small.street_template.lua:31`, `country_new_small.street_template.lua:60` |
| Однополосное шоссе | с 1940 | 100 км/ч | 180 000 | 30 000 | `highway_new_small.street_template.lua:10`, `highway_new_small.street_template.lua:32`, `highway_new_small.street_template.lua:53` |
| Двухполосное шоссе | с 1940 | 120 км/ч | 360 000 | 60 000 | `highway_new_medium.street_template.lua:10`, `highway_new_medium.street_template.lua:32`, `highway_new_medium.street_template.lua:61` |
| Трехполосное шоссе | с 1940 | 120 км/ч | 540 000 | 90 000 | `highway_new_large.street_template.lua:10`, `highway_new_large.street_template.lua:32`, `highway_new_large.street_template.lua:69` |
| Трамвайные пути (старые) | до 1910 | 40 км/ч | 36 000 | 6 000 | `tram_old.street_template.lua:4-5`, `tram_old.street_template.lua:8`, `tram_old.street_template.lua:27`, `tram_old.street_template.lua:40` |
| Трамвайные пути (новые) | с 1925 | 100 км/ч | 120 000 | 20 000 | `tram_new.street_template.lua:4`, `tram_new.street_template.lua:9`, `tram_new.street_template.lua:29`, `tram_new.street_template.lua:42` |

- **Смена 1940 года** делает городские улицы на 10 км/ч быстрее, но **втрое** дороже, и при постройке, и каждый год: небольшая улица дорожает с 60 000 до 180 000 за км.
- Средний и широкий варианты проселочных дорог стоят в 2 и 3 раза больше маленькой при той же скорости (`country_new_large.street_template.lua:10`, `country_new_large.street_template.lua:31`).
- Добавки к улице: **автобусная полоса** +10 %, **трамвайные пути** +20 %, **электрифицированные трамвайные пути** +40 % цены улицы (`mod.script.tl:24-28`).
- Обычно игрок не владеет улицами, даже построенными им самим; инструменты улиц могут сменить владельца улицы (официальная вики). Кто платит за обслуживание улицы, решает движок.

## Аллеи и шумозащитные экраны

| Инструмент | Шум | Загрязнение | Максимальная скорость | Где | Источник |
|---|---|---|---|---|---|
| Аллея (деревья) | -10 % | -50 % | **-25 %** | улицы с тротуаром, не на мостах и не в туннелях | `alley.edge.lua:39-40`, `alley.edge.lua:53-56` |
| Шумозащитные экраны | -65 % | без изменений | без изменений | улицы и пути, не в туннелях | `barrier_b.edge.lua:43`, `barrier_b.edge.lua:47`, `barrier_track_b.edge.lua:43` |

- Оба стоят в своих файлах 100 и 10 в год, как улица за метр (`alley.edge.lua:8`, `alley.edge.lua:12`, `barrier_b.edge.lua:7`, `barrier_b.edge.lua:11`).
- Типы улиц «с деревьями» и «с экранами» в меню строительства - это те же улицы с уже нанесёнными украшениями (`town_new_medium_trees.street_template.lua:12-14`). Меню строительства суммирует их эффекты (`construction_react_util.tl:2116-2139`).
- Поэтому улица с деревьями **на четверть медленнее**: новая средняя улица с деревьями допускает около 38 км/ч вместо 50.

```tip scripts
Против шума используйте шумозащитные экраны: -65 % и никакой потери скорости. Деревья - средство против загрязнения (-50 %), но они замедляют улицу на четверть.
```

Как города оценивают шум и загрязнение: [Загрязнение и шум](emission.html).

## Мосты и туннели

| Мост | Годы | Максимальная скорость | Для | Базовая цена | Источник |
|---|---|---|---|---|---|
| Каменный мост | с начала | 90 км/ч | пути, улицы | 200 | `stone.bridge.lua:169-170`, `stone.bridge.lua:181-183`, `stone.bridge.lua:193` |
| Мост-эстакада | до 1970 | 60 км/ч | один тип для путей, один для улиц | 100 | `trestle.bridge.lua:200-201`, `trestle.bridge.lua:212-214`, `trestle.bridge.lua:226`, `trestle_s.bridge.lua:212` |
| Стальной мост | с 1940 | 140 км/ч | пути, улицы | 200 | `steel.bridge.lua:243`, `steel.bridge.lua:259`, `steel.bridge.lua:269` |
| Висячий мост | с 1940 | 180 км/ч | пути, улицы | 600 | `suspension.bridge.lua:277`, `suspension.bridge.lua:294`, `suspension.bridge.lua:304` |
| Железобетонный мост | с 1970 | 280 км/ч | пути, улицы | 200 | `concrete.bridge.lua:162`, `concrete.bridge.lua:176`, `concrete.bridge.lua:187` |
| Вантовый мост | с 2000 | 220 км/ч | пути, улицы | 750 | `cable.bridge.lua:214`, `cable.bridge.lua:231`, `cable.bridge.lua:240` |
| Арочный мост | с 2010 | 350 км/ч | пути, улицы | 650 | `tarch.bridge.lua:253`, `tarch.bridge.lua:270`, `tarch.bridge.lua:280` |

- Ограничение моста действует **поверх** ограничения путей: скоростная линия на стальном мосту идёт там 140 км/ч. До 1970 года ни один мост не допускает больше 180 км/ч, до 2010 года ни один не допускает 350 км/ч.
- У **туннелей** (Туннель в скале, Железобетонный туннель с 1970) в файлах **нет ограничения скорости**, и базовая цена у них одинаковая, 600 (`tunnel_a.tunnel.lua:187-188`, `tunnel_a_car.tunnel.lua:185`, `tunnel_b.tunnel.lua:191-194`).
- Цены мостов и туннелей следуют настройке «Стоимость инфраструктуры» (`post_run_util.tl:50-51`).

```engine
Базовую цену моста или туннеля движок переводит в цену за метр с учётом высоты или глубины (costFactors); официальная вики говорит, что она зависит от длины и высоты над землёй или глубины под ней. Поэтому одна и та же базовая цена может дать очень разные счета. Туннели стоят городу репутации (см. [Репутация](reputation.html)).
```

```tip scripts
Для быстрой линии через долину до 1970 года висячий мост (180 км/ч) - единственный мост быстрее 140 км/ч; у туннеля ограничения нет вовсе.
```

## Железнодорожные переезды и сигналы

| Что | Годы | Максимальная скорость путей | Цена | Источник |
|---|---|---|---|---|
| Простой железнодорожный переезд | 1850 - 1925 | 120 км/ч | 4 000 | `era_a_eu.rcr.lua:14-17`, `era_a_eu.rcr.lua:26` |
| Переезд со шлагбаумом | 1925 - 1975 | 160 км/ч | 16 000 | `era_b_eu.rcr.lua:15-18`, `era_b_eu.rcr.lua:27` |
| Современный переезд со шлагбаумом | с 1975 | 160 км/ч | 16 000 | `era_c_eu.rcr.lua:15-17`, `era_c_eu.rcr.lua:26` |
| Семафор (механический до 1950, светофор с 1950) | все | - | 9 000, обслуживание 1 500 в год | `signal_path_a.con.lua:4-5`, `signal_path_a.con.lua:10-11`, `signal_path_c.con.lua:4-5` |

- Переезд ограничивает путь не более чем 160 км/ч: скоростным линиям нужны мосты или туннели над улицами.
- Любой сигнал можно переключить в режим **В одну сторону** (`signal_path_a.con.lua:51-52`). Как сигналы делят путь на блоки, объясняет страница Railway Signals официальной вики.

## Депо и станции техобслуживания

Сколько стоят депо и станции техобслуживания, сколько транспорта они обслуживают и в каком радиусе: [Линии и транспорт](vehicles.html) и [Расходы, обслуживание и займы](costs.html).

## Полезно знать

- До 1940 года модернизация городских улиц дешёвая; после 1940 года каждая новая или перестроенная городская улица стоит втрое дороже и втрое дороже в обслуживании.
- На быстрой линии проверьте каждый мост и каждый переезд: самый медленный задаёт скорость на этом участке.
- Скорость окупается, только если даёт больше рейсов (см. [Почему я теряю деньги?](money.html)).

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: Те же скорости, что в официальных таблицах для путей, улиц и мостов. По файлам ограничения мостов действуют и на улицы, у туннелей их нет, переезды ограничивают пути 120 или 160 км/ч, деревья замедляют улицу на 25 % и снижают загрязнение на 50 %, но шум лишь на 10 %, а шумозащитные экраны снижают шум на 65 % без замедления.
result: refines
```
