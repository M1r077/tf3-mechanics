---
title: 회사 등급, 특전과 본부
summary: 회사 등급을 올리는 것, 각 등급이 여는 것, 허가와 자원 탐사의 작동 방식, 본부가 실제로 주는 것, 그리고 높은 등급의 대가.
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40425
fact: 15 | 회사 등급, 주니어부터 거물까지
fact: ×12.5 | 등급 15에 필요한 세계 인구(시작 시와 비교)
fact: ×0.75 | 인플레이션 보통에서 등급 15의 수입
fact: 0 | 인구가 줄어도 잃는 등급
---

회사 등급은 돈이나 배송이 아니라 **맵 전체의 인구**에서 나온다. 새 등급마다 특전(랜드마크, 자원 탐사, 마케팅 캠페인, 산업 녹화, 본부 모듈)이 열리고, **인플레이션** 설정이 있으면 모든 수입도 조금씩 줄어든다.

## 등급을 올리는 것

- 게임은 **시작 시의 세계 인구**, 즉 모든 마을의 주민 수를 기억한다(`company.script.tl:392-396`, `company_util.tl:365-371`).
- 그리고 지금까지 도달한 **최대** 세계 인구를 그 시작 값과 비교한다(`company_growth.script.tl:25-27`). 이 값은 오르기만 하므로, 마을이 줄어도 등급을 잃지 않는다.
- 등급 1은 시작 값에서, 등급 15는 그 약 **12.5배**에서 도달한다(`company_progression_util.tl:6-14`, `company_progression_util.tl:95-120`, `town_growth_function.tl:13-20`).
- 캠페인 미션과 맵 편집기에는 등급이 없다(`company_growth.script.tl:74-79`).

| 등급 | 직책 | 세계 인구(시작 시와 비교) |
|---|---|---|
| 1 | 주니어 | ×1 |
| 2 | 정비공 | ×1.02 |
| 3 | 엔지니어 | ×1.08 |
| 4 | 담당자 | ×1.2 |
| 5 | 전문가 | ×1.4 |
| 6 | 팀장 | ×1.7 |
| 7 | 관리자 | ×2.1 |
| 8 | 경영자 | ×2.6 |
| 9 | 책임자 | ×3.3 |
| 10 | 수석 책임자 | ×4.2 |
| 11 | CEO | ×5.3 |
| 12 | 의장 | ×6.7 |
| 13 | 부사장 | ×8.3 |
| 14 | 회장 | ×10.2 |
| 15 | 거물 | ×12.5 |

비율은 시작 인구 50,000 이상일 때를 스크립트로 계산한 것이다(`company_progression_util.tl:6-14`, `company_static_util.tl:6-24`). 작은 맵에서는 중간 등급이 조금 더 높다(주민 5,000이면 등급 8에 ×2.85 필요). 등급 1과 15는 ×1과 ×12.5 그대로다.

- 따라서 등급은 **마을 성장**을 따른다. 마을은 당신의 승객과 화물로 성장한다. [마을 성장](towns.html)을 참조.
- 처음 등급은 빨리 오지만, 마지막 등급은 맵의 마을들이 몇 배나 커져야 한다.

## 새 등급은 회사 창에서 적용된다

인구가 기준을 넘으면 **등급 상승 알림**이 뜬다. 클릭하면 그 등급으로 회사 창이 열린다(`company_growth.script.tl:96-107`, `company_notification_rank_up.script.tl:8-9`).

- 새 특전은 그 등급이 **회사 창에서 선택될 때**에만 열린다. 그때 창이 해제를 보낸다(`company.tl:420-423`, `company_growth.script.tl:55-62`). 건설 메뉴는 이 적용된 등급을 확인한다(`company_util.tl:92`, `company_util.tl:171-178`).
- 다음 절의 수입 계수는 적용 여부와 관계없이 **도달한** 등급을 따른다(`company_growth.script.tl:47-48`).

```tip scripts
등급이 오르면 알림을 클릭하거나(또는 회사 창을 열고 새 등급을 선택해) 특전을 받자. 기다려도 얻는 것은 없다. 수입은 이미 줄었다.
```

## 높은 등급의 대가: 인플레이션 설정

**인플레이션**이 있으면 모든 화물과 승객 수입이 등급 1의 ×1에서 등급 15의 최솟값까지 고르게 줄어든다(`company_progression_util.tl:25-40`, `company_growth.script.tl:159-170`).

| 인플레이션 | 등급 15의 수입 | 출처 |
|---|---|---|
| 없음 | ×1(변화 없음) | `difficulty_util.tl:50`, `mod.script.tl:694-697` |
| 낮음 | ×0.9 | |
| 보통 | ×0.75 | |
| 높음 | ×0.6 | |
| 매우 높음 | ×0.5 | |

- 보통에서는 등급마다 수입의 약 1.8 %를 잃는다. 등급 3에서 ×0.96, 등급 8에서 ×0.875, 등급 15에서 ×0.75.
- 인플레이션은 어떤 비용도 올리지 않는다. 비용은 달력의 연도를 따른다([비용, 유지비와 대출](costs.html) 참조).
- 등급이 높으면 새 보조금 제안도 드물어진다([보조금](subsidies.html) 참조).

## 허가

대부분의 특전은 **허가**로 제한된다. 등급이 특전의 허가를 주고, 건물 하나나 사용 한 번마다 하나를 쓴다(`company_util.tl:33-80`, `company_util.tl:206`).

- 허가는 등급을 거치며 **합산된다**. 등급 3에서 1, 등급 5에서 1을 주는 특전은 등급 5부터 2개를 허용한다(`company_util.tl:51-56`).
- 건물은 철거하면 허가를 돌려준다. 게임은 서 있는 것을 센다(`company_util.tl:143-163`, `company_util.tl:203-206`).
- 자원 탐사, 마케팅 캠페인, 녹화는 시작할 때 허가를 소모한다(`company.script.tl:416-423`, `company.script.tl:459-462`, `company.script.tl:496-500`). 그 뒤 건설 메뉴에 **이미 사용됨** 또는 **쿨타임**이 표시된다(`company_util.tl:207-226`).
- **마케팅** 허가는 각 캠페인 **5년** 뒤에 돌아온다(`marketing.res.lua:6-7`, `company.script.tl:66-94`).

| 특전 | 허가 | 출처 |
|---|---|---|
| 본부 | 등급 1에서 1 | `hq.res.lua:6` |
| 마케팅 캠페인 | 등급 4에서 1, 5년 뒤 돌아옴 | `marketing.res.lua:6-7` |
| 산업 녹화 | 등급 3, 6, 9, 12, 15에서 1 | `industry_greenify_tool.script.tl:101-102` |
| 정화 시설 | 등급 10에서 15 | `pollution_cleanup_facility.con.lua:106-108` |
| 랜드마크 | 각각 하나: 원형극장 2, 알렉산드리아 등대 5, 히메지성 7, 선박 박물관 9, 노이슈반슈타인 성 10, 자유의 여신상 11, 이화원 13, 오페라 하우스 14, 국회의사당 15 | `arena.con.lua:39`, `lighthouse.con.lua:48`, `white_heron_castle.con.lua:47`, `ship_museum.con.lua:55`, `neuschwanstein.con.lua:55`, `statue_of_liberty.con.lua:57`, `summer_palace.con.lua:63`, `opera_house.con.lua:63`, `westminster.con.lua:79` |

각 특전의 효과: [마을 평판](reputation.html)(마케팅 캠페인), [오염과 소음](emission.html)(녹화, 정화 시설).

## 자원 탐사

자원 탐사는 마을 근처에서 자원을 찾고, 성공하면 그곳에 새 산업을 세운다.

| 자원 | 등급 | 출처 |
|---|---|---|
| 어류 | 2 | `exploration_fish.res.lua:9-11` |
| 찰흙 | 3 | `exploration_clay.res.lua:9-11` |
| 원유 | 4 | `exploration_crude_oil.res.lua:9-11` |
| 곡물, 채소 | 4, **공유 허가 하나**(산업) | `exploration_grain.res.lua:9`, `exploration_vegetables.res.lua:9`, `permit_key_farm.res.lua:6` |
| 통나무 | 5 | `exploration_logs.res.lua:9-11` |
| 석탄, 철광석 | 6 | `exploration_coal.res.lua:9-11`, `exploration_iron_ore.res.lua:9-11` |
| 석재, 모직 | 8 | `exploration_stone.res.lua:9-11`, `exploration_wool.res.lua:9-11` |
| 모래 | 9 | `exploration_sand.res.lua:9-11` |
| 고무 | 12 | `exploration_rubber.res.lua:9-11` |

- 자원마다 허가는 **하나**이며, 자원 탐사를 시작할 때 쓴다(`company.script.tl:451-462`).
- 최대 **6개월** 동안 진행된다. 한 달에 한 번 산업 배치를 시도하며, 확률은 6개월에 걸쳐 20 %에서 60 %로 오른다(`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`).
- 게임이 마을 근처에서 그 산업을 둘 곳을 찾지 못해도 시도는 실패한다(`company.script.tl:199-210`).
- 마지막 시도가 실패하면 **허가가 돌아오고** 알림이 그렇게 알려 준다(`company.script.tl:106-126`, `company.script.tl:170-181`).
- 마을과 자원 조합마다 한 번에 하나의 자원 탐사만 진행할 수 있다(`company.script.tl:442-447`).

```engine
새 산업이 설 수 있는 곳(마을 근처의 makeIndustrySpawnProposal)은 엔진이 정한다. 물에서 먼 어류 자원 탐사나 주변에 빈 땅이 없는 마을에서는 그냥 실패하고 허가가 돌아온다.
```

## 본부

| 항목 | 값 | 출처 |
|---|---|---|
| 가격과 유지비 | 무료, 유지비 없음 | `headquarter.script.tl:526-527` |
| 허가 | 1, 등급 1에서 | `headquarter.con.lua:6-7`, `hq.res.lua:6` |
| 마을 성장 | 가장 가까운 마을에 +5 % | `headquarter.script.tl:510-515`, `landmark_util.tl:51-70` |
| 일자리 | 24 | `headquarter.con.lua:16`, `headquarter.script.tl:505-508` |

- +5 %는 그 마을 성장률에 대한 보너스이므로, 마을의 성장률이 0 %이면 아무것도 하지 않는다([마을 성장](towns.html) 참조).
- **모듈**은 하나에 50,000이며, 등급과 함께 늘어나는 허가로 제한된다(`hq_module_m.module.lua:83`, `hq_module_m.module.lua:137`).
- 파일에서 보너스가 있는 모듈은 둘뿐이다: **중형 건물** 마을 성장 +1 %(`hq_module_m.module.lua:139-142`)와 **대형 건물** **평판 복구** +1 %(`hq_module_l.module.lua:169-172`). 복구 보너스는 어떤 마을 평가도 읽지 않는다([마을 평판](reputation.html) 참조). 다른 모듈은 장식이다.
- 각 모듈 파일은 마을 성장 +5 %를 주는 표로 시작하지만, 파일 안에서 그것을 쓰는 곳은 없다(`hq_corner_l.module.lua:148-159`, `hq_statue.module.lua:46-57`). 합산되는 것은 모듈의 `metadata` 안에 있는 보너스뿐이다(`headquarter_addon.script.tl:18-29`).

| 모듈 | 허가를 얻는 등급(×2 = 두 개) | 등급 15의 합계 |
|---|---|---|
| 바닥용 깃발 | 1 ×2, 6, 7, 8, 9, 11, 12, 13, 14 | 10 |
| 코너 건물 | 3, 5, 7 ×2, 9, 11, 13, 15 | 8 |
| 중형 건물 | 2, 4, 10 ×2, 15 ×2 | 6 |
| 대형 건물 | 5, 6, 10, 12 | 4 |
| 발코니 | 8 ×2, 14 ×2 | 4 |
| 대형 분수 | 10 ×2, 14 ×2 | 4 |
| 돔 | 6, 15 ×2 | 3 |
| 지붕용 깃발 | 7, 10, 13 | 3 |
| 테니스 코트 | 11, 12, 14 | 3 |
| 고목 | 13, 15 ×2 | 3 |
| 조각상 | 14 ×2 | 2 |
| 수영장 | 15 | 1 |

출처: 각 모듈 파일의 `rankAndPermits` 줄 (`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`).

```tip scripts
본부는 가장 빨리 키우고 싶은 마을에 두고, 그곳에 중형 건물을 추가하자. 성장 보너스가 있는 모듈은 이것뿐이다.
```

## 알아 두면 좋은 것

- 등급을 올리려면 마을을 키우자. 더 많은 마을로 더 많은 승객과 화물을, 좋은 평가로. 은행의 돈은 세지 않는다.
- 랜드마크와 자원 탐사를 계획하자. 각각 정해진 등급에서 한 번만 온다.
- 인플레이션이 있는 맵에서 등급 상승은 특전에는 좋고 수입에는 나쁘다. 보통에서는 등급 15까지 가는 동안 전체 수입의 4분의 1을 잃는다.

```check
official: "The company rank depends on the population of the map. . Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: 같은 규칙이다. 지금까지 도달한 최대 세계 인구를 시작 시 인구와 비교하며, 등급 15는 ×12.5이고 잃지 않는다. 새 등급은 회사 창에서 선택해야 특전이 열리지만, 인플레이션은 바로 수입을 줄인다. 보너스가 있는 모듈은 둘뿐이고(중형 건물 성장 +1 %, 대형 건물 평판 복구 +1 %, 후자는 어떤 평가도 읽지 않음) 나머지는 장식이다.
result: refines
```
