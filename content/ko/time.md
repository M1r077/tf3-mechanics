---
title: 게임 시간과 달력
summary: 게임 속도와 달력 속도는 서로 다르다. 하루와 1년의 길이, 달력을 느리게 하거나 멈추면 무엇이 바뀌고 무엇이 바뀌지 않는지.
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
game: 40425
fact: 4 s | 달력 속도 ×1, 게임 속도 1x에서 달력의 하루
fact: ≈ 24 min | 같은 속도에서 달력의 1년
fact: 0 ×0.25 ×0.5 ×1 ×2 ×4 | 달력 속도 단계
fact: 0 1x 2x 4x | 게임 속도 단계
---

게임에는 **시계가 두 개** 있다. **게임 속도**(일시 정지, 1x, 2x, 4x)는 모든 것을 빠르게 돌린다. 운송 수단, 생산, 마을도 마찬가지다. **달력 속도**는 날짜가 흐르는 속도만 정한다. 게임의 거의 모든 규칙은 달력의 날짜가 아니라 게임 시간으로 센다.

## 두 가지 설정

| 설정 | 단계 | 바꾸는 것 | 출처 |
|---|---|---|---|
| **게임 속도** | 일시 정지, 1x, 2x, 4x | 시뮬레이션 전체가 도는 속도 | `game_bar_widgets.tl:199-203` |
| **달력 속도** | 일시 정지됨, ×0.25, ×0.5, ×1, ×2, ×4 | 하루가 게임 시간으로 몇 초인지 | `game_bar_widgets.tl:321-335`, `game_bar_widgets.tl:351` |

- 달력 속도 ×1에서 하루는 게임 시간으로 **4초**다(공식 위키). 그래서 1x에서 한 달은 약 2분, 1년은 약 **24분**이다. [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard)로 측정: ×1에서 하루 4.0초, ×4에서 1초, ×0.5에서 8초, ×0.25에서 16초.
- ×4는 날짜를 네 배 빠르게 흐르게 한다. **일시 정지됨**은 날짜를 멈추지만 시뮬레이션은 계속된다.
- 2x와 4x는 최댓값이다. 컴퓨터가 따라가지 못하면 게임이 이를 낮춘다(`game.tl:636-642`). 측정 결과 2x는 평균 1.9x, 4x는 평균 3.6x였다.
- **시각**과 날씨는 세 번째의, 보이기만 하는 시계다. 기본적으로 달력과 상관없이 스스로 바뀐다(`game_time_config.res.lua:5`, `weather_config.res.lua:5`).

## 달력과 상관없이 게임 시간을 따르는 것

이것들은 게임 시간으로 센다. 그래서 달력을 느리게 하거나 멈춰도 느려지지 않는다.

- **생산**: 산업의 생산 시간은 표준 1년의 일정한 비율이다(`industry_react_util.tl:51`). 산업 창은 이를 현재 달력의 날짜 수로 보여준다(`industry_react_util.tl:23`). ×0.25에서는 같은 속도라도 날짜 수가 4분의 1로 보인다.
- **대출 상환**: 게임 시간으로 표준 한 달마다 한 번이며, 달력이 멈춰도 같다(`loan.script.tl:83-88`).
- **보조금 기한**과 ×2 수입 보너스(`subvention_util.tl:290-292`).
- **마을 평판 회복**(`towns.script.tl:121-130`), **노동자 부스트**(`industry_productivity_util.tl:3`), 몇 년 동안 운송이 없을 때의 **산업 폐쇄**(`industries.script.tl:119-128`).
- 최근 반년 동안의 마을 **배송 평가**(`town_util.tl:840`).
- **새 산업**: 달력을 멈춘 상태에서도 게임 시간 1809초 동안 3개가 760초와 728초 간격으로 생겼다. 달력이 흐를 때(약 730초)와 같은 리듬이다. [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard)로 측정. [산업](industries.html) 참고.

달력이 흐르는 동안 게임은 이 기간들을 현재 달력 속도의 년, 월, 일로 보여준다(`util.tl:40-49`).

## 달력 날짜를 따르는 것

- **새 운송 수단, 역, 건물**은 연도에 따라 나온다(공식 위키: "Different calendar speeds only affect the availability of vehicles and infrastructure").
- **연도에 따라 커지는 비용**: 건물 관리비, 시대별 종류, 보조금 액수, 대출 금액은 날짜를 따른다. 자세한 내용: [비용, 관리비, 대출](costs.html).

## 달력이 일시 정지됐을 때

1. 날짜, 곧 연도가 그대로다. 새 운송 수단이 나오지 않고, 연도에 따른 비용도 그대로다.
2. 기간이 날짜 대신 **분과 초**로 표시된다(`util.tl:41-43`, `industry_react_util.tl:16-21`).
3. 대출은 상환액을 연간이 아니라 **분당**으로 보여준다(`finances_loan_gui.tl:223-231`). 맞춤 대출 카드는 받을 수 없다(`finances_loan_gui.tl:393`).
4. 생산, 상환, 기한, 평판은 게임 시간의 속도대로 계속된다.

## 알아두면 좋은 점

- 새 운송 수단이 나오기 전에 노선망을 키울 시간이 더 필요한가? 달력 속도를 낮추자. 게임 시간 1분당 수입은 바뀌지 않는다.
- "연간"으로 표시되는 생산은 달력 속도에 따라 달라진다. 산업은 같은 속도에서 비교하자.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard)는 달력이 멈춰도 읽기 쉬운 재무 그래프를 보여준다.

```engine
표준 하루, 한 달, 1년의 길이(getDefaultDayDuration 등)는 엔진에서 온다. 마을 스크립트는 한 달을 30 × 4초로 센다(`towns.script.tl:121`). 이는 측정한 하루 4초와 맞는다. 다른 몇몇 상수는 아직 하루를 2초로 가정한다(`cargotype.script.lua:3`, `mod.script.tl:172`).
```

```check
official: "By default a day in the game lasts 4 seconds." "Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent." ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: 달력 속도는 표준 하루를 기준으로 ×0.25에서 ×4, 또는 일시 정지다. 생산, 대출, 보조금, 평판, 노동자 타이머는 게임 시간으로 돈다. 달력이 멈추면 기간은 분으로, 상환은 분당으로 표시되고 새 대출은 막힌다. 측정: ×1에서 하루 4초.
result: refines
```
