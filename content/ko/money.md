---
title: 왜 돈을 잃고 있을까?
summary: 무엇이 돈을 벌고 무엇이 돈이 드는지, 그리고 돈을 잃는 노선과 그 이유를 찾는 6단계 점검과 각 항목을 설명하는 페이지 링크.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-15
fact: 1 | 화물 1개당 지급, 소비처에서, 직선 거리에 대해
fact: 0 | 창고나 환승에서의 지급
fact: 100 % | 늦어도 지급
fact: ×6 | 2020년까지 창고, 항구, 공항 관리비의 연도 계수
---

배송은 **하나의 직선**에 대해 지급된다. 화물이 만들어진 곳에서 쓰이는 곳까지이며, 그곳에 도착했을 때만 지급된다. 짓고 사는 모든 것은 매년 돈이 들고, 그중 일부는 연도가 지날수록 점점 더 든다. 노선이 돈을 잃는 것은 그 노선의 지급 몫이 그 노선이 만드는 비용보다 작을 때다.

```diagram money_flow
```

## 무엇이 돈을 버는가

- 공급처에서 소비처까지의 **직선 거리**에 8 × 오르막을 더한 값. 경로의 길이는 세지 않는다(`cargo_income.script.lua:3-7`, `cargo_income.script.lua:5`).
- **모든 화물은 km당 같은 금액**을 낸다: 수입 계수는 모두 3.8이다(`cargotype.script.lua:7-13`).
- **소비처에서 한 번만.** 창고나 환승역에서 하차하면 아무것도 지급되지 않는다. 지급액은 그 뒤 각 구간의 직선 길이에 따라 체인의 노선들에 나뉜다(게임 내 측정).
- **늦은 화물도 전액 지급된다**: 이동 시간은 쓰이지 않는다(`cargotype.script.lua:7-13`). 대신 늦으면 마을의 배송 평가가 내려간다.
- **회사 랭크**는 **인플레이션** 설정에 따라 모든 수입을 낮춘다: 랭크 15에서 보통이면 ×0.75(`company_progression_util.tl:25-40`).
- **완료한 보조금**은 배송한 노선의 수입을 5년 동안 두 배로 만든다(`subvention_util.tl:286`).

자세히: [화물 수입과 배송 시간](income.html).

## 무엇이 돈이 드는가

- **운송 수단**: 운행비는 평균 속도 × 수용량을 따르고, 가격은 운행비 6년분이다(`model_metadata_util.lua:499-518`, `model_metadata_util.lua:548-549`).
- **선로와 도로**: km당 1년에 건설 가격의 약 6분의 1. 고속 선로는 일반 선로의 9배가 든다(`simple.street_template.lua:33`, `high_speed.street_template.lua:35`).
- **차량기지, 역, 창고, 항구, 공항**: 후기 시대 변형은 ×3과 ×9가 든다(`rail_depot.con.lua:7`, `warehouse.tl:48`). 또 창고, 항구, 공항의 관리비는 연도도 따라서, 1900년 ×1에서 2020년 ×6이 된다(`mod.script.tl:92-100`).
- **대출**: 이율은 금액에 한 번만 부과되고 기간 전체에 나뉜다(`loan_util.tl:102-111`).
- **인플레이션은 어떤 비용도 올리지 않는다**. 수입만 낮춘다.

자세히: [비용, 관리비, 대출](costs.html).

## 순서대로 6가지 점검

```diagram money_check
```

1. **어떤 노선이 돈을 잃는가?** 회사 전체가 아니라 노선별 수지를 본다. [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) 모드는 각 노선의 최근 12개월 수지와 몇 년간의 평균을 보여 준다.
2. **화물이 멀리 가는가?** 공급처에서 소비처까지의 직선만 지급된다. 창고로 가는 짧은 지선은 자기 짧은 구간의 몫만 받는다([화물 수입과 배송 시간](income.html)).
3. **가득 차서 달리는가?** 운송 수단의 비용은 가득 차든 비어 있든 같다. 빈 귀환 운행, 각 정류장의 **충전 수위**와 **가득 실음**을 본다([출발 설정: 가득 실음, 충전 수위, 정지 시간](departure.html)).
4. **돈이 지급되는 곳에서 하차하는가?** 정류장의 상차 목록에 없는 것은 근처의 아무 재고에나 하차된다. 창고도 포함되며, 창고는 아무것도 지급하지 않는다([상차 및 하차 속도](loading.html), [창고](warehouses.html)). 가득 찬 마을 재고에 들어가지 않는 화물은 차량에 남는다([마을 성장: 경험치, 평가, 규모](towns.html)).
5. **운송 수단이 과한가?** 속도와 수용량은 돈이 들지만 속도 자체는 지급되지 않는다. 1년 운행 횟수가 늘 때만 도움이 된다. 마을 안에서는 오래되고 느린 버스가 새롭고 빠른 버스보다 수익이 좋을 수 있다([비용, 관리비, 대출](costs.html)).
6. **고정비.** 차량기지, 여분의 창고 모듈, 고속 선로, 후기 시대 건물은 쓰든 안 쓰든 매년 돈이 든다([비용, 관리비, 대출](costs.html)).

## 알아두면 좋은 점

- 화물은 가격이 아니라 **양과 거리로 고른다**: 모든 화물은 km당 같은 금액을 낸다.
- 짧은 노선들이 화물을 대 주는 **긴 간선**이 돈의 대부분을 번다. 지선의 수지는 작아 보이지만, 중요한 것은 체인 전체다.
- **운반할 것을 늘린다**: 부스트한 산업은 더 많이 생산하고([근로자와 근로자 부스트](workers.html), [산업](industries.html)), 큰 마을은 더 많은 화물을 원한다.
- 노선을 빠르게 해도 화물 1개당 지급액은 오르지 않는다. 같은 운송 수단이 더 많이 운행할 때만 도움이 된다.

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks))
scripts: 같다: 직선에 8 × 오르막, 모든 화물에 같은 계수, 이동 시간은 쓰이지 않음. 게임 내 측정: 소비처에서 한 번만 지급되고 구간 길이로 나뉜다. 비용은 운송 수단이 속도 × 수용량, 선로가 가격의 1/6, 건물은 시대 변형 ×3 / ×9와 연도 계수 ×1에서 ×6. 인플레이션은 수입만 낮춘다.
result: refines
```
