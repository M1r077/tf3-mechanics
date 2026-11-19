---
title: 비용, 관리비, 대출
summary: 비용 설정이 무엇을 바꾸는지, 어떤 비용이 달력 연도에 따라 커지는지, 운송 수단 가격이 어떻게 계산되는지, 대출이 실제로 얼마나 드는지.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
game: 40444
fact: ×6 | 2020년까지 창고, 항구, 공항 관리비에 붙는 연도 계수
fact: 6년 | 치 운영 비용: 이것이 운송 수단의 가격
fact: 한 번 | 대출 이자율은 매년이 아니라 금액에 한 번만 붙음
fact: 4 | 동시에 받을 수 있는 대출 수
---

**인플레이션** 설정은 어떤 비용도 올리지 않는다. 회사 랭크가 오를수록 수입을 낮출 뿐이다([화물 수입과 배송 시간](income.html) 참조). 비용은 대신 **달력 연도**에 따라 커지며, 네 개의 슬라이더가 처음부터 그 배율을 정한다.

```diagram cost_years
```

## 비용 설정

| 설정 | 값 | 프리셋 쉬움 · 보통 · 어려움 · 매우 어려움 | 출처 |
|---|---|---|---|
| **운송 수단 비용**, **운송 수단 유지보수** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:39`, `difficulty_util.tl:98-101`, `difficulty_util.tl:125-128`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **기반 시설 비용**, **기반 시설 관리** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:98-101`, `difficulty_util.tl:125-128`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **운송 수단 유지보수 효과** | 없음 ×0 · 낮음 ×0.5 · 중간 ×1 · 높음 ×1.5 · 아주 높음 ×2 | 낮음 · 중간 · 높음 · 아주 높음 | `difficulty_util.tl:42`, `difficulty_util.tl:103`, `difficulty_util.tl:185` |
| **인플레이션** | 수입에만 적용, [화물 수입과 배송 시간](income.html) 참조 | 낮음 · 보통 · 높음 · 매우 높음 | `difficulty_util.tl:50`, `mod.script.tl:695-698` |

- **기반 시설 비용**은 도로, 선로, 다리, 터널, 건널목, 건물, 모듈의 가격과 지형 작업 비용을 바꾼다(`post_run_util.tl:23-52`, `post_run_util.tl:83-120`, `construction.script.tl:31-35`, `mod.script.tl:224-227`). 건물의 철거 비용도 바꾼다(`construction.script.tl:39-44`). **기반 시설 관리**는 불러올 때 도로, 선로, 다리, 터널, 건널목, 모듈의 관리비를 바꾼다(`post_run_util.tl:43-45`, `post_run_util.tl:105-112`). 건물의 경우 스크립트는 건물 창에서만 이를 적용한다(`entity_window_util.tl:186`). 실제로 청구되는 금액은 엔진이 정한다.
- **운송 수단 비용**과 **운송 수단 유지보수**는 모든 운송 수단의 구매 가격과 운영 비용을 바꾼다(`post_run_util.tl:54-81`).
- **운송 수단 유지보수 효과**는 상태가 나쁜 운송 수단이 속도, 출력, 편안함을 얼마나 잃고 소음, 오염, 운영 비용이 얼마나 늘어나는지 정한다(`mod.script.tl:242-246`).

## 달력 연도에 따라 커지는 것

- **건물 관리비**: 1900년 ×1, 1920년 ×1.5, 1940년 ×2.2, 1960년 ×3.2, 1980년 ×4, 2000년 ×5, 2020년 ×6(`mod.script.tl:92-100`). 건물 창과 건설 메뉴는 연도를 따르도록 표시된 모든 건물에 이를 적용하며, 건설 메뉴는 모든 메타 건설물을 이렇게 표시한다(기본 게임에서는 창고, 비행장, 공항, 항구)(`entity_window_util.tl:186-193`, `construction_react_util.tl:1152`, `warehouse.tl:7`, `harbor_modular.tl:24`).
- 이런 건물에 추가한 **모듈**은 가격은 건물을 지은 연도로, 관리비는 현재 연도로 정해진다(`construction.tl:3741-3748`, `construction.tl:4413-4416`).
- **시대별 종류**: 차량기지, 정비소, 창고, 역, 항구, 공항은 시대마다 종류가 하나씩 있고, 뒤의 종류는 첫 종류의 **×3**(시대 B) 또는 **×9**(시대 C)가 든다(`rail_depot.con.lua:7`, `warehouse.tl:48`, `modular_station.con.lua:71`, `harbor_modular.tl:76`, `airport.tl:8`).
- **보조금 현금**: 1900년 ×1에서 2000년 이후 ×4까지(`finances_util.tl:87-90`). **대출 금액**: 1900년 ×0.4에서 2020년 ×2.4까지(`loan_util.tl:7-10`).
- **수입**에는 연도 계수가 전혀 없다(`cargo_income.script.lua:10-13`).

```engine
실제로 청구되는 관리비와, 도로, 선로, 운송 수단도 연도 표를 따르는지는 엔진이 정한다(getCostMultiplierForYear. 기본 설정은 chargeMaintenanceInterval = 60만 지정한다, `mod.script.tl:105`). 스크립트는 위의 표로 창과 건설 메뉴에 보이는 값만 계산한다. 다른 건물에 "연도를 따름" 표시를 붙이는 스크립트는 없다.
```

## 선로, 도로, 건물

도로와 선로 파일에는 미터당 가격과 연간 관리비가 적혀 있고, 건설 메뉴는 킬로미터당으로 보여 준다(`construction_react_util.tl:2466`, `construction_react_util.tl:2480-2488`). 대부분의 종류에서 관리비는 건설 가격의 **6분의 1**이다.

| 종류 | 등장 | km당 건설비 | km당 연간 관리비 | 출처 |
|---|---|---|---|---|
| 간소한 선로 | 시작 | 6만 | 1만 | `simple.street_template.lua:9`, `simple.street_template.lua:33` |
| 표준 선로 | 1930 | 18만 | 3만 | `standard.street_template.lua:11`, `standard.street_template.lua:35` |
| 고속 선로 | 1980 | 54만 | 9만 | `high_speed.street_template.lua:11`, `high_speed.street_template.lua:35` |
| 오래된 작은 시골길 | 시작 – 1940 | 6만 | 1만 | `country_old_small.street_template.lua:4-5`, `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:58` |
| 새로운 큰 시내 도로 | 1940 | 54만 | 9만 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:91` |

- 전차선은 선로 가격의 **30 %**를 더한다. 버스 전용 차로는 도로 가격의 10 %, 전차 선로는 20 %, 전기 전차 선로는 40 %를 더한다(`mod.script.tl:24-28`).
- 지형을 높이는 데는 m³당 4.5, 낮추는 데는 m³당 5.25(둘 다 기반 시설 비용을 곱한다), 밭을 없애는 데는 20만이 든다(`mod.script.tl:20-22`, `mod.script.tl:33`, `mod.script.tl:226-227`).
- 관리비를 지정하지 않은 건물은 해마다 **가격의 6분의 1**을 낸다(기반 시설 비용 설정을 곱하기 전의 가격에서 계산, `construction.script.tl:25-27`).
- 기본 설정은 철거 환불 계수 0.75, 환불 시간 60을 지정한다(`mod.script.tl:30-31`). 방금 지은 것을 철거하면 돈 대부분을 돌려받는다. 이를 적용하는 것은 엔진이다.

파일에 적힌 연간 관리비, 첫 종류(1940년 이전)와 뒤의 종류. 창고에는 위의 연도 계수가 추가로 붙는다.

| 건물 | 첫 종류 | ×3(1940년부터) | ×9(1980년부터) | 출처 |
|---|---|---|---|---|
| 열차 차량기지, 선박 차량기지 | 10만 | 30만 | 90만 | `rail_depot.con.lua:34`, `water_depot.con.lua:32` |
| 도로 차량기지 | 3만 | 9만 | 27만 | `road_depot.con.lua:32` |
| 전차 차량기지 | 2만 | 6만 | 18만 | `tram_depot.con.lua:34` |
| 열차 또는 선박 정비소 | 4만 | 12만 | 36만 | `rail_maint_station.con.lua:32`, `water_maint_station.con.lua:32` |
| 도로 정비소 | 1만 | 3만 | 9만 | `road_maint_station.con.lua:32` |
| 범용 창고 | 2.5만 | 7.5만 | 22.5만 | `warehouse.tl:48-52`, `warehouse.tl:75` |
| 특화된 창고 | 5만 | 15만 | 45만 | `warehouse.tl:51`, `warehouse.tl:75` |

이 건물들은 모두 관리비의 **6배**로 지어진다(`rail_depot.con.lua:35`, `warehouse.tl:76`). 마지막 시대의 특화된 창고라면 연도 계수 전에 270만이다.

- 첫 **비행장**(1950년까지)은 이미 두 번째 시대의 ×3을 쓴다. 판정이 종류의 시작 연도 대신 끝 연도를 읽기 때문이다(`airfield.tl:8`, `airfield_era_a.metacon.tl:3`).

## 운송 수단

기본 게임의 운송 수단에는 고정 가격이 없다. 게임은 모델을 불러올 때 운송 수단의 속도와 수용량으로 가격을 계산한다(`model_metadata_util.lua:488-552`).

1. **연간 운영 비용** = 약 675 × 평균 속도(m/s) × 수용량 ÷ 4(`model_metadata_util.lua:499-518`). 675는 km당 평균 수입에서 나온 값으로, 빈 차 귀환, 구매 비용, 떨어지는 운임을 감안해 줄인 것이다(`model_metadata_util.lua:500-508`).
2. **평균 속도**는 최고 속도보다 낮다(v는 km/h). 도로 운송 수단과 전차는 v^0.78 + 4, 열차는 v^0.86 + 10, 항공기는 −0.0000203 × v² + 0.17 × v + 28.36(v는 최대 4,000), 선박은 최고 속도의 65 %다(`model_metadata_util.lua:448-474`).
3. **열차**: 화차는 수용량의 절반으로 센다. 기관차는 출력 ÷ 최고 속도(km/h) × 12.5도 수용량으로 세며, 이것도 절반으로 한다(`model_metadata_util.lua:511-512`, `model_metadata_util.lua:526-540`). 힘세고 느린 기관차는 비싸다.
4. **가격** = 연간 운영 비용의 **6배**(`model_metadata_util.lua:548-549`).

100 %에서의 예: 승객 48명을 태우는 35 km/h 버스는 운영 비용이 연간 약 4.5만, 가격이 약 27만이다.

- 운송 수단의 상태는 다섯 단계로 나뉜다(100–80 %, 그다음 20 %마다)(`vehicle_store_util.tl:231-234`). **20 %**가 되면 게임이 경고하며, 30 %를 넘을 때까지 계속된다(`notifications.script.tl:310-318`).

```engine
운송 수단의 상태가 얼마나 빨리 떨어지는지, 그에 따라 운영 비용이 얼마나 오르는지, 운송 수단 가격이 연도에 따라 바뀌는지는 엔진 값이다(getMaintenanceRunningCostPenalty와 다른 페널티). 스크립트는 운송 수단 유지보수 효과로 그 값의 배율만 정한다.
```

## 대출

```diagram loan_interest
```

| 종류 | 1960년 무렵 금액(1900년 ×0.4, 2020년 ×2.4) | 기한 | 이율 | 출처 |
|---|---|---|---|---|
| 작음 | 500만–1000만 | 1–5년 | 3–5 % | `loan_util.tl:12-22` |
| 보통 | 1500만–2500만 | 3–8년 | 5–8 % | `loan_util.tl:24-34` |
| 큼 | 3000만–5000만 | 5–12년 | 8–10 % | `loan_util.tl:36-46` |
| 아주 큼 | 4000만–6000만 | 10–24년 | 10–12 % | `loan_util.tl:48-58` |

- 카드에는 **연이율**이라고 적혀 있지만, 이율은 금액에 **한 번만** 적용된다. 총이자는 기한과 상관없이 금액 × 이율이다. 원금과 함께 매달 같은 금액으로 낸다(`loan_util.tl:102-111`, `loan_util.tl:126-136`, `loan.script.tl:83-99`). 그래서 이율이 같다면 긴 대출이 짧은 대출보다 1년당 싸다.
- **상환**은 남은 원금만 낸다. 남은 이자는 사라진다(`loan.script.tl:171-190`). 버튼을 쓰려면 그 금액만큼 현금이 있어야 한다(`finances_loan_gui.tl:284-286`).
- 이율은 난이도에 따라 **달라지지 않는다**. 종류마다 고정된 범위가 있다(`loan_util.tl:12-58`).
- 동시에 최대 **4건**의 대출(`loan_util.tl:4`, `loan.script.tl:134`). 제안은 반년 뒤에 바뀌고, 받은 대출의 칸은 4–8개월 동안 비어 있다(`loan.script.tl:61-76`, `loan.script.tl:150`).
- 게임을 시작할 때 네 칸 각각에 무작위 종류의 값이 들어가므로, 첫 "작음" 제안이 큰 대출일 수도 있다. 제안이 한 번 갱신되면 각 칸은 자기 종류를 제안한다(`loan_util.tl:60-74`, `loan.script.tl:63-75`).

```tip scripts
**가장 긴 대출을 받고 일찍 상환한다.** 총이자는 기간과 상관없이 같고, 월 납입금은 더 적으며, 상환하면 남은 이자는 사라진다.
```

## 알아두면 좋은 점

- 받을 수 있는 **가장 긴** 대출을 고르자. 총이자는 같고 더 많은 달로 나뉘며, 일찍 상환하면 나머지를 내지 않는다.
- 시대별 종류가 있는 건물은 뒤 시대에 ×3, ×9가 들고 관리비도 연도에 따라 계속 커진다. 마지막 시대의 특화된 창고는 큰 고정 비용이다.
- 빠르고 수용량이 큰 운송 수단은 운영 비용이 많이 들지만 더 많이 나른다. 가격과 운영 비용은 벌 수 있는 수입처럼 속도 × 수용량을 따른다.

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: 대출 이율은 종류에 따라서만 정해지고(3–12 %) 난이도와는 상관없다. 금액에 한 번만 붙고 기한의 달들에 나뉘어 청구된다. 일찍 상환하면 남은 이자는 사라진다. 인플레이션은 수입만 바꾼다. 건물 관리비는 연도를 따른다(×1–×6). 운송 수단 가격 = 연간 운영 비용의 6배이며, 둘 다 속도와 수용량으로 정해진다.
result: differs
```
