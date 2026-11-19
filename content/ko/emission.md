---
title: 오염과 소음
summary: 무엇이 소음과 오염을 내는지, 건물이 언제 더 많이 내는지, 마을이 이를 어떻게 평가하는지, 그리고 산업 녹화와 정화 시설이 실제로 하는 일.
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
game: 40444
fact: 65–80 dB | 마을 소음: 65에서 만점, 80에서 0
fact: 60–74 | 마을 오염, 스크립트의 로그 척도(소리 크기가 아님): 60에서 만점, 74에서 0
fact: −80 % | 녹화된 산업의 소음과 오염
fact: 700 m | 정화 시설의 범위
---

운송 수단, 선로, 도로, 역, 차고, 창고, 산업은 모두 **소음**과 **공해**를 낸다. 마을의 두 평가, **소음**과 **공해**는 마을에 닿는 양을 고정된 한계와 비교한다. 나쁜 평가는 마을 권한 평가를 낮추고, 따라서 성장도 낮춘다([마을](towns.html) 참조).

## 건물이 더 많이 내는 때

게임 스크립트는 몇 번의 업데이트마다 네 종류 건물의 배출을 조용한 수준과 바쁜 수준 사이에서 설정한다(`emissions.script.tl:12-18`).

| 건물 | 더 많이 내는 때 | 출처 |
|---|---|---|
| **산업** | 생산할 때, 그리고 부스트(화물 또는 노동자)마다 더. 모든 출력 재고가 동시에 가득 차면 수준이 절반이 됨(생산 → 유휴, 부스트 2회 → 생산) | `emissions.script.tl:152-194` |
| **역** | 바쁠수록. 기다리는 사람과 화물을 수용량과 비교 | `emissions.script.tl:211-222` |
| **차고**, **정비소** | 그 정비를 쓰는 운송 수단이 많을수록 | `emissions.script.tl:223-234` |
| **창고** | 재고가 많을수록 | `emissions.script.tl:237-250` |

- 산업마다 고유한 4단계(유휴, 생산 중, 부스트 1회, 부스트 2회)가 있다(`industryutil.lua:464-475`. 기본값 0 / 78 / 84 / 88은 고유 값이 없는 산업에만 쓰인다). 대부분은 유휴 상태에서도 조금 낸다. 탄광은 오염 2 → 10 → 20 → 30, 그 밭은 2 → 30 → 60 → 90이다(`coal_mine.con.lua:99-135`, [산업](industries.html) 참조).
- 출력 재고가 모두 가득 찬 산업은 수준이 절반으로 떨어진다(`emissions.script.tl:172-182`). 즉, 운송하면 그 오염이 올라간다.
- 운송 수단과 선로도 배출한다. **운송 수단 유지보수 효과** 설정에서는 상태가 나쁜 운송 수단이 더 많이 낸다([비용, 관리비, 대출](costs.html) 참조).

## 건설 메뉴에 표시되는 것

| 건물 | 소음 | 오염 | 출처 |
|---|---|---|---|
| 항구 | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| 공항 | 8–56 | 80–560 | `airport.tl:28-29` |
| 기차역 | 25 | 45–350 | `modular_station.con.lua:97-98` |
| 철도 차고 | 50 | 100 | `rail_depot.con.lua:32-33` |
| 도로 및 트램 차고 | 40 | 80 | `road_depot.con.lua:30-31`, `tram_depot.con.lua:32-33` |
| 지하역 | 40 | 80 | `underground_station.con.lua:75-76` |
| 트럭 및 버스 정류장 | 1–10 | 12–76 | `modular_terminal.con.lua:67-68`, `modular_terminal.con.lua:121-122` |
| 정비소 | 20 | 40–50 | `road_maint_station.con.lua:30-31`, `rail_maint_station.con.lua:30-31` |
| 창고 | 20 | 50(범용) 또는 100(전용) | `warehouses/warehouse.tl:51`, `warehouses/warehouse.tl:73-74` |

두 값은 메뉴가 보여 주는 범위로, 가장 낮은 값에서 가장 높은 값까지이며 옆의 가격 범위와 같다(`construction_desc_react_util.tl:733-746`). 값이 하나면 단일 수치다. 가동 중에는 모든 건물이 바쁠수록 더 많이 낸다(위 표). 항구, 공항, 큰 화물역은 집에서 멀리 둔다.

## 마을이 평가하는 방법

| 평가 | 측정 대상 | 만점 | 0 | 출처 |
|---|---|---|---|---|
| **소음** | 마을 건물에서의 소음 | 65 dB 이하 | 80 dB | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **공해** | 마을 면적의 16 m 칸당 평균 공해(면적은 최소 5, 최대 10 km²로 계산)를 스크립트의 로그 척도("dB")로 환산 | 60 이하 | 74 | `town_util.tl:413-431`, `emission_config.tl:23-30` |

- 소음에 시달리는 것은 **주거** 지구뿐이며, 상업 및 산업 건물은 그렇지 않다(공식 위키). 집의 창은 그 위치의 소음을 보여준다(`town_building.tl:165-183`).
- 오염은 면적 전체에서 평균되므로, 중심에서 먼 발생원 하나는 작은 마을보다 큰 마을에서 덜 무겁다.
- **소음 민감도**와 **공해 민감도** 설정은 한계를 옮긴다. 민감도 두 배는 +3 dB로 계산된다(`town_util.tl:426-428`, `town_util.tl:439-441`). 공해는 소음과 같은 로그 척도(10·log10)를 쓴다. +3 "dB"는 공해가 두 배라는 뜻이며, 소리 크기가 아니다.

| 단계 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 출처 |
|---|---|---|---|---|---|---|---|---|
| 소음 | 끄기(항상 만점) | ×¼ | ×½ | ×1 | ×1.4 | ×1.8 | ×3.5 | `difficulty_util.tl:48` |
| 오염 | 끄기(항상 만점) | ×¼ | ×½ | ×1 | ×1.7 | ×3 | ×5 | `difficulty_util.tl:49` |

프리셋 쉬움, 보통, 어려움, 매우 어려움은 단계 3, 4, 5, 6을 쓴다(`difficulty_util.tl:114-115`, `difficulty_util.tl:142-143`, `difficulty_util.tl:169-170`, `difficulty_util.tl:196-197`).

## 산업 녹화

| | | 출처 |
|---|---|---|
| 효과 | 산업의 소음과 오염 ×0.2(−80 %), 영구 | `emission_config.tl:32`, `emissions.script.tl:184-192` |
| 사용 횟수 | 회사 등급 3, 6, 9, 12, 15에서 하나씩 | `industry_greenify_tool.script.tl:99-104` |
| 제한 | 산업마다 한 번. 두 번째 시도는 허가를 쓰지 않는다 | `company.script.tl:489-494` |

- 효과는 그 버전의 산업에 묶여 있다. 산업이 다시 지어지면 사라진다(`emissions.script.tl:187-190`).
- 가장 좋은 사용법: 마을 바로 옆의 가장 바쁜 산업. 부스트된 산업이 가장 많이 내기 때문이다.

## 정화 시설

주변의 오염을 없애는 회사 특전.

| | | 출처 |
|---|---|---|
| 가격 | 1억 | `pollution_cleanup_facility.script.lua:560` |
| 연간 관리비 | 1000만 | `pollution_cleanup_facility.script.lua:561` |
| 이용 가능 | 회사 등급 10에서 15개 | `pollution_cleanup_facility.con.lua:106-108` |
| 필요한 것 | **기계**: 주기당 8, 연 2주기. 노동자 20명 | `pollution_cleanup_facility.con.lua:43-60` |
| 범위 | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| 상태 | 오염 | 소음 | 출처 |
|---|---|---|---|
| 유휴(기계 없음) | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| 가동 중 | −10,000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| 부스트 1회 | −20,000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| 부스트 2회 | −40,000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

마지막 수준에는 부스터 규칙이 필요하지만 정화 시설에는 없다. 노동자가 있으면 −20,000에 이른다(`pollution_cleanup_facility.con.lua:51-58`, `emissions.script.tl:158-166`).

- 기계가 없으면 거의 아무것도 하지 않는다. 산업처럼 공급해야 한다.
- 시끄럽다. 주거 지구 밖, 오염된 지역에서 700 m 이내에 짓는다.
- 노동자 부스트 계수는 ×2다(`pollution_cleanup_facility.script.lua:549`). [노동자](workers.html) 참조.

## 알아두면 좋은 점

- 마을 창이나 소음 및 오염 레이어를 열면 평가와 발생 지점을 볼 수 있다.
- 산업의 출력 재고가 모두 가득 차면 배출 수준이 절반이 되지만, 그 화물을 잃는다. 산업을 굶기기보다 마을을 옮기는 편이 낫다.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details)와 [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard)는 가장 바쁜 역을 찾는 데 도움이 된다.

```engine
소음 및 오염 지도, 값이 퍼지는 방식, 운송 수단과 선로의 배출, 산업이 언제 다시 지어지는지는 엔진이 계산한다. 스크립트는 각 건물의 수준과 마을의 한계만 설정한다.
```

```check
official: "Noise reflects noise levels in residential areas." "Pollution reflects pollution levels across the town area." 주거 지구는 "is sensitive to noise", 상업 지구는 "is robust against the influence of noise". ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: 소음 평가 65 → 80 dB, 오염 60 → 74 dB, 5~10 km²에서 평균. 민감도는 10·log10 dB를 더한다. 산업, 역, 차고, 창고는 바쁠 때 더 많이 낸다. 출력 재고가 모두 가득 차면 산업의 배출 수준이 절반이 된다. 녹화는 산업마다 한 번 −80 %. 정화 시설은 700 m 이내에서 최대 20,000의 오염을 없애며(40,000은 정의되어 있지만 부스터 규칙이 필요) 기계가 필요하다.
result: refines
```
