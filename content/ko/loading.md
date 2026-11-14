---
title: 상차 및 하차 속도
summary: 정류장에서 운송 수단의 상차를 빠르거나 느리게 만드는 요소: 운송 수단, 플랫폼 구간, 그리고 화물을 내주거나 받는 재고.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-14
fact: ×2 | 특화된 플랫폼 구간
fact: ×0.25 | 맞지 않는 구간 또는 너무 긴 열차
fact: ×4 | 최선의 경우: 특화된 플랫폼과 특화된 창고
---

운송 수단이 상차나 하차에 쓰는 시간은 자체 상차 속도에 두 계수를 곱한 값으로 정해진다. 하나는 **플랫폼**의 계수, 다른 하나는 반대편 **재고**(창고, 산업, 마을)의 계수다.

```diagram loading_factors
```

## 1. 운송 수단

모든 운송 수단에는 기본 상차 속도가 있으며, 운송 수단 상점과 운송 수단 창에 표시된다("2.0x"). 아래의 모든 계수가 이 값에 곱해진다.

## 2. 플랫폼 계수

게임에게 플랫폼은 모듈의 나열이 아니다. **화물 분류마다 하나씩 있는 구간의 목록**이며, 같은 분류에 속한 모든 모듈의 길이를 합산한 것이다.

```diagram loading_sections
```

| 화차가… | 계수 | 출처 |
|---|---|---|
| 자기 분류의 구간에 있을 때(벌크 화차, 벌크 구간) | **×2** | `modular_station.script.lua:1042` |
| 범용 구간에 있을 때 | ×1 | `modular_station.script.lua:1042` |
| 플랫폼에 자기 분류의 구간이 없을 때 | **×0.25** | `cargo_react_util.tl:60` |
| 플랫폼 길이를 벗어난 부분(열차가 너무 김) | **×0.25** | `cargo_react_util.tl:61` |

- 계수는 **열차에서 차지하는 비율에 따라 섞인다**. 화차의 3/4이 맞고 1/4이 맞지 않으면 계수는 ¾ × 2 + ¼ × 0.25 ≈ ×1.56이다(`cargo_react_util.tl:63-70`, 게임이 "부분 특화된 터미널"로 표시하는 것과 같은 분할).
- 화차가 플랫폼의 **어디에** 서 있는지는 상관없고, 합산된 길이만 중요하다(게임 내 측정).
- 도로: 특화된 트럭 터미널은 ×2(`modular_terminal.script.lua:2956`), 작은 도로 역은 항상 ×1이다(`small_stops.script.lua:19`).
- 승객 플랫폼은 ×1이다.

## 3. 재고 계수

화물을 하차할 때 각 단위는 수령처 하나로 간다. 창고 모듈, 산업, 또는 마을 건물이다. 수령처의 재고에는 고유한 계수가 있다.

| 수령처 | 계수 | 출처 |
|---|---|---|
| **특화된** 창고 모듈(액체, 벌크, 평상식, 상품) | **×2** | `modules.script.lua:120`, `warehouse.script.lua:297-314` |
| **범용** 창고 | ×1 | `warehouse.script.lua:272-285` |
| 산업 | ×1 | 게임 내 측정 |

- 모든 창고 모듈이 ×2를 요청하지만, 범용 모듈은 **하나의 공용 범용 재고**에 수용량만 더하며, 이 재고는 ×1로 생성된다. 특화된 모듈만 ×2인 자체 재고를 가진다.
- 게임의 툴팁은 이 계수를 "특화된 창고: +100 %"라고 부른다(`cargo_react_util.tl:51-54`).
- 한 번의 하차 동안 게임은 수령처들을 **번갈아** 처리한다. 그래서 화물 일부는 창고로, 일부는 산업으로 갈 때 열차가 하차하는 도중에 속도가 바뀐다(게임 내 측정).

```engine
각 단위가 어느 수령처로 가는지, 그리고 최종 곱셈은 엔진에서 처리된다. 위의 계수는 스크립트가 엔진에 주는 입력값이며, 결과는 엔진이 노출하는 값으로 확인했다([Platform Details](https://mod.io/g/transportfever3/m/platform-details) 프로브, 2026년 10월).
```

## 게임에 표시되는 내용

- 상차 표시기는 ×1.5를 넘으면 **가속**으로, ×0.75 미만이면 **감속**으로 그려진다(`cargo_react_util.tl:119-122`).
- 마우스를 올리면 툴팁에 "특화된 터미널", "특화 종류 불일치", "터미널 너무 짧음", "특화된 창고"가 각각의 백분율과 함께 표시된다(`cargo_react_util.tl:76-99`).

## 예시

벌크 화차 8량, 길이 160 m의 열차가 석탄을 하차한다.

| 정류장 | 플랫폼 | 수령처 | 계수 |
|---|---|---|---|
| 범용 플랫폼 160 m | ×1 | 제철소 | **×1** |
| 벌크 플랫폼 160 m | ×2 | 제철소 | **×2** |
| 벌크 플랫폼 160 m | ×2 | 특화된 벌크 창고 | **×4** |
| 벌크 플랫폼 160 m | ×2 | 범용 창고 | **×2** |
| 범용 플랫폼 120 m(열차가 40 m 초과) | ¾ × 1 + ¼ × 0.25 ≈ ×0.81 | 제철소 | **×0.81** |

## 알아두면 좋은 점

- 산업 내부의 정류장은 항상 그 산업이 필요로 하는 화물에 특화되어 있다(공식 위키).
- 특화된 창고 모듈은 보관 중인 화물의 배송 타이머도 멈춘다(공식 위키). 범용 창고는 그렇지 않다.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details)는 플랫폼에 있는 모든 운송 수단의 두 계수와, 하차한 화물이 어디로 갔는지를 보여준다.

```check
official: "Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization." Specialized warehouses "enable faster loading / unloading speeds". ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: 특화된 구간 ×2, 범용 ×1, 맞는 구간 없음 ×0.25, 플랫폼을 벗어난 부분 ×0.25, 열차에서 차지하는 비율로 혼합. 특화된 창고 모듈 ×2, 범용 창고 ×1.
result: refines
```
