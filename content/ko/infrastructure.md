---
title: 도로, 선로, 교량, 신호기
summary: 선로와 도로 종류별 속도, 가격, 관리비, 교량, 터널, 건널목, 신호기의 비용과 가능한 것, 가로수와 소음 장벽이 실제로 바꾸는 것, 그리고 차량기지 설명이 있는 곳.
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40425
fact: 100 / 160 / 350 km/h | 간소한 선로, 표준 선로, 고속 선로
fact: ×9 | 간소한 선로와 비교한 고속 선로의 가격과 관리비
fact: +30 % | 선로에 전차선을 놓는 가격
fact: -65 % | 소음 장벽이 있는 도로나 선로의 소음
---

도로와 선로의 종류마다 최고 속도, 미터당 가격, 미터당 연간 관리비가 있으며 모두 파일에 적혀 있다. 교량, 건널목, 일부 도로 장식은 자체 속도 제한을 더한다. 아래 비용은 **기반 시설 비용**과 **기반 시설 관리**가 100 %일 때의 값이다([비용, 관리비, 대출](costs.html) 참조).

## 선로

| 선로 | 등장 | 최고 속도 | km당 건설비 | km당 연간 관리비 | 출처 |
|---|---|---|---|---|---|
| 간소한 선로 | 시작 | 100 km/h | 6만 | 1만 | `simple.street_template.lua:9`, `simple.street_template.lua:28`, `simple.street_template.lua:33` |
| 표준 선로 | 1930 | 160 km/h | 18만 | 3만 | `standard.street_template.lua:4`, `standard.street_template.lua:11`, `standard.street_template.lua:30`, `standard.street_template.lua:35` |
| 고속 선로 | 1980 | 350 km/h | 54만 | 9만 | `high_speed.street_template.lua:4`, `high_speed.street_template.lua:11`, `high_speed.street_template.lua:30`, `high_speed.street_template.lua:35` |

- **전차선**은 선로보다 **30 %** 비싸다(`mod.script.tl:24-25`). 간소한 선로에서는 1921년부터, 더 새로운 종류에서는 등장할 때부터 쓸 수 있다(`simple_catenary.street_template.lua:4`). 파일상 연간 추가 비용은 없으며, 전기 버전의 관리비는 같다(`simple_catenary.street_template.lua:34`).
- 세 종류 모두 경사와 곡선 조건이 같다. 건설할 때 **8.5 %**(**경사** 슬라이더의 최대값), 선로 형태로는 최대 13 %, 곡선 반경은 건설할 때 55 m, 최소 40 m다(`standard.street_template.lua:36-37`, `standard.street_template.lua:48-49`, `construction_react_util.tl:241-242`, `construction_react_util.tl:1821`).
- 선로 자체의 오염은 종류에 따라 커진다. 2, 4, 6(`simple.street_template.lua:18`, `standard.street_template.lua:20`, `high_speed.street_template.lua:20`).

```engine
곡선이 열차 속도를 얼마나 낮추는지(선로 종류별 speedCoeffs)와 건설 도구가 곡선에 표시하는 속도는 엔진이 계산한다.
```

```tip scripts
고속 선로는 건설도 연간 관리도 간소한 선로의 9배가 든다. 열차가 실제로 160 km/h보다 빠르게 달리는 곳에만 깔자. 다른 곳은 표준 선로면 충분하고, 느린 화물 지선은 간소한 선로로 된다.
```

## 도로

| 도로 | 연도 | 최고 속도 | km당 건설비 | km당 연간 관리비 | 출처 |
|---|---|---|---|---|---|
| 좁은 거리(옛) | 1940년까지 | 20 km/h | 3.6만 | 6,000 | `town_old_xsmall.street_template.lua:4-5`, `town_old_xsmall.street_template.lua:8`, `town_old_xsmall.street_template.lua:27`, `town_old_xsmall.street_template.lua:56` |
| 소형 거리(옛) | 1940년까지 | 40 km/h | 6만 | 1만 | `town_old_small.street_template.lua:8`, `town_old_small.street_template.lua:27`, `town_old_small.street_template.lua:56` |
| 대형 거리(옛) | 1940년까지 | 60 km/h | 18만 | 3만 | `town_old_large.street_template.lua:8`, `town_old_large.street_template.lua:27`, `town_old_large.street_template.lua:88` |
| 좁은 거리(새) | 1940년부터 | 30 km/h | 12만 | 2만 | `town_new_xsmall.street_template.lua:4`, `town_new_xsmall.street_template.lua:11`, `town_new_xsmall.street_template.lua:30`, `town_new_xsmall.street_template.lua:59` |
| 소형 거리(새) | 1940년부터 | 50 km/h | 18만 | 3만 | `town_new_small.street_template.lua:11`, `town_new_small.street_template.lua:30`, `town_new_small.street_template.lua:59` |
| 중형 거리(새) | 1940년부터 | 50 km/h | 36만 | 6만 | `town_new_medium.street_template.lua:11`, `town_new_medium.street_template.lua:30`, `town_new_medium.street_template.lua:75` |
| 대형 거리(새) | 1940년부터 | 60 km/h | 54만 | 9만 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:30`, `town_new_large.street_template.lua:91` |
| 소형 시골 도로(옛) | 1940년까지 | 60 km/h | 6만 | 1만 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:29`, `country_old_small.street_template.lua:58` |
| 소형 시골 도로(새) | 1940년부터 | 80 km/h | 18만 | 3만 | `country_new_small.street_template.lua:10`, `country_new_small.street_template.lua:31`, `country_new_small.street_template.lua:60` |
| 1차선 고속도로 | 1940년부터 | 100 km/h | 18만 | 3만 | `highway_new_small.street_template.lua:10`, `highway_new_small.street_template.lua:32`, `highway_new_small.street_template.lua:53` |
| 2차선 고속도로 | 1940년부터 | 120 km/h | 36만 | 6만 | `highway_new_medium.street_template.lua:10`, `highway_new_medium.street_template.lua:32`, `highway_new_medium.street_template.lua:61` |
| 3차선 고속도로 | 1940년부터 | 120 km/h | 54만 | 9만 | `highway_new_large.street_template.lua:10`, `highway_new_large.street_template.lua:32`, `highway_new_large.street_template.lua:69` |
| 전차 선로(옛) | 1910년까지 | 40 km/h | 3.6만 | 6,000 | `tram_old.street_template.lua:4-5`, `tram_old.street_template.lua:8`, `tram_old.street_template.lua:27`, `tram_old.street_template.lua:40` |
| 전차 선로(새) | 1925년부터 | 100 km/h | 12만 | 2만 | `tram_new.street_template.lua:4`, `tram_new.street_template.lua:9`, `tram_new.street_template.lua:29`, `tram_new.street_template.lua:42` |

- **1940년의 전환**으로 시내 도로는 10 km/h 빨라지지만, 건설도 연간 관리도 **3배** 비싸진다. 소형 거리는 km당 6만에서 18만이 된다.
- 시골 도로의 중형과 대형은 같은 속도에서 소형의 2배와 3배가 든다(`country_new_large.street_template.lua:10`, `country_new_large.street_template.lua:31`).
- 도로에 추가하기: **버스 전용 차로**는 도로 가격의 +10 %, **전차 선로**는 +20 %, **전기 전차 선로**는 +40 %(`mod.script.tl:24-28`).
- 플레이어는 보통 도로를 소유하지 않으며, 플레이어가 지은 도로도 마찬가지다. 도로 도구로 도로의 소유자를 바꿀 수 있다(공식 위키). 도로 관리비를 누가 내는지는 엔진이 정한다.

## 가로수와 소음 장벽

| 도구 | 소음 | 오염 | 최고 속도 | 장소 | 출처 |
|---|---|---|---|---|---|
| 골목 도구(나무) | -10 % | -50 % | **-25 %** | 보도가 있는 도로. 교량 위나 터널 안은 안 됨 | `alley.edge.lua:39-40`, `alley.edge.lua:53-56` |
| 소음 장벽 도구 | -65 % | 변화 없음 | 변화 없음 | 도로와 선로. 터널 안은 안 됨 | `barrier_b.edge.lua:43`, `barrier_b.edge.lua:47`, `barrier_track_b.edge.lua:43` |

- 둘 다 파일상 100, 연간 10으로, 도로의 미터당 값과 같다(`alley.edge.lua:8`, `alley.edge.lua:12`, `barrier_b.edge.lua:7`, `barrier_b.edge.lua:11`).
- 건설 메뉴의 "가로수 있음", "장벽 있음" 도로는 이 장식이 이미 붙은 같은 도로다(`town_new_medium_trees.street_template.lua:12-14`). 건설 메뉴는 그 효과를 합산한다(`construction_react_util.tl:2116-2139`).
- 그래서 가로수가 있는 도로는 **4분의 1 느리다**. 가로수가 있는 새 중형 거리는 50 km/h 대신 약 38 km/h다.

```tip scripts
소음에는 소음 장벽을 쓰자. -65 %에 속도 손실도 없다. 나무는 오염 대책(-50 %)이지만 도로를 4분의 1 느리게 만든다.
```

도시가 소음과 오염을 어떻게 평가하는지: [오염과 소음](emission.html).

## 교량과 터널

| 교량 | 연도 | 최고 속도 | 용도 | 기본 가격 | 출처 |
|---|---|---|---|---|---|
| 돌 교량 | 시작부터 | 90 km/h | 선로, 도로 | 200 | `stone.bridge.lua:169-170`, `stone.bridge.lua:181-183`, `stone.bridge.lua:193` |
| 구각교 | 1970년까지 | 60 km/h | 선로용과 도로용이 따로 있음 | 100 | `trestle.bridge.lua:200-201`, `trestle.bridge.lua:212-214`, `trestle.bridge.lua:226`, `trestle_s.bridge.lua:212` |
| 강철 교량 | 1940년부터 | 140 km/h | 선로, 도로 | 200 | `steel.bridge.lua:243`, `steel.bridge.lua:259`, `steel.bridge.lua:269` |
| 현수교 | 1940년부터 | 180 km/h | 선로, 도로 | 600 | `suspension.bridge.lua:277`, `suspension.bridge.lua:294`, `suspension.bridge.lua:304` |
| 콘크리트 교량 | 1970년부터 | 280 km/h | 선로, 도로 | 200 | `concrete.bridge.lua:162`, `concrete.bridge.lua:176`, `concrete.bridge.lua:187` |
| 사장교 | 2000년부터 | 220 km/h | 선로, 도로 | 750 | `cable.bridge.lua:214`, `cable.bridge.lua:231`, `cable.bridge.lua:240` |
| 타이드 아치 교량 | 2010년부터 | 350 km/h | 선로, 도로 | 650 | `tarch.bridge.lua:253`, `tarch.bridge.lua:270`, `tarch.bridge.lua:280` |

- 교량 제한은 선로 제한에 **더해서** 적용된다. 강철 교량을 건너는 고속 노선은 그곳에서 140 km/h로 달린다. 1970년 이전에는 180 km/h를 넘는 교량이 없고, 2010년 이전에는 350 km/h를 허용하는 교량이 없다.
- **터널**(바위 터널, 1970년부터 콘크리트 터널)은 파일상 **속도 제한이 없고**, 기본 가격은 똑같이 600이다(`tunnel_a.tunnel.lua:187-188`, `tunnel_a_car.tunnel.lua:185`, `tunnel_b.tunnel.lua:191-194`).
- 교량과 터널 가격은 기반 시설 비용을 따른다(`post_run_util.tl:50-51`).

```engine
교량이나 터널의 기본 가격은 엔진이 높이나 깊이(costFactors)를 써서 미터당 가격으로 바꾼다. 공식 위키에 따르면 가격은 길이와 지면 위 높이, 또는 지하 깊이에 따라 달라진다. 따라서 같은 기본 가격이라도 청구액은 크게 다를 수 있다. 터널은 도시의 평판을 떨어뜨린다([평판](reputation.html) 참조).
```

```tip scripts
1970년 이전에 골짜기를 건너는 빠른 노선이라면, 140 km/h보다 빠른 교량은 현수교(180 km/h)뿐이다. 터널에는 제한이 전혀 없다.
```

## 건널목과 신호기

| 종류 | 연도 | 선로 최고 속도 | 가격 | 출처 |
|---|---|---|---|---|
| 간소한 건널목 | 1850 - 1925 | 120 km/h | 4,000 | `era_a_eu.rcr.lua:14-17`, `era_a_eu.rcr.lua:26` |
| 반 장벽 건널목 | 1925 - 1975 | 160 km/h | 1.6만 | `era_b_eu.rcr.lua:15-18`, `era_b_eu.rcr.lua:27` |
| 현대 반 장벽 건널목 | 1975년부터 | 160 km/h | 1.6만 | `era_c_eu.rcr.lua:15-17`, `era_c_eu.rcr.lua:26` |
| 길 신호기(1950년까지 완목식, 1950년부터 색등식) | 전체 | - | 9,000, 연간 관리비 1,500 | `signal_path_a.con.lua:4-5`, `signal_path_a.con.lua:10-11`, `signal_path_c.con.lua:4-5` |

- 건널목은 선로를 최대 160 km/h로 제한한다. 고속 노선은 도로를 교량이나 터널로 넘어야 한다.
- 모든 신호기는 **일방통행**으로 설정할 수 있다(`signal_path_a.con.lua:51-52`). 신호기가 선로를 어떻게 블록으로 나누는지는 공식 위키의 철도 신호 페이지에 설명되어 있다.

## 차량기지와 정비소

차량기지와 정비소의 비용, 담당하는 운송 수단 수와 반경: [노선과 운송 수단](vehicles.html), [비용, 관리비, 대출](costs.html).

## 알아두면 좋은 점

- 1940년 이전에는 시내 도로 개량이 싸다. 1940년 이후에는 새로 짓거나 다시 짓는 시내 도로마다 가격과 관리비가 3배다.
- 빠른 노선에서는 모든 교량과 건널목을 확인하자. 가장 느린 것이 그곳의 속도를 정한다.
- 속도는 운행 횟수가 늘어날 때만 이득이다([왜 돈을 잃고 있을까?](money.html) 참조).

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: 선로, 도로, 교량 속도는 공식 표와 같다. 파일에서는 교량 제한이 도로에도 적용되고, 터널에는 제한이 없으며, 건널목은 선로를 120 또는 160 km/h로 제한하고, 나무는 도로를 25 % 느리게 하고 오염을 50 % 줄이지만 소음은 10 %만 줄인다. 반면 소음 장벽은 속도를 낮추지 않고 소음을 65 % 줄인다.
result: refines
```
