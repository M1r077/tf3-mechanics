---
title: 알림과 경고
summary: 각 경고가 언제 나타나고 언제 사라지는지: 멈춘 운송 수단, 사용할 수 없거나 혼잡한 역, 노선과 정류장 문제, 마을 평가, 운송 수단 상태, 폐쇄되는 산업, 그리고 기본적으로 기록에서 숨겨지는 경고.
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 5분 | 운송 수단이 멈춘 것으로 보고되기까지 서 있는 게임 시간
fact: 20 % | 경고가 나타나는 상태, 운송 수단이 30 %를 넘을 때까지 유지
fact: 11 | 새 게임에서 꺼져 있는 알림 종류
fact: 75일 | 도로 연결이 없는 역을 두 번 확인하는 간격
---

대부분의 경고는 **지속형**이다. 게임 스크립트가 상황을 계속 다시 확인하며, 문제가 있는 동안 경고가 남고 해결되면 저절로 끝난다. 확인은 4번의 업데이트에 차례로 나뉘어 이루어지므로, 경고가 나타나거나 사라지기까지 잠시 걸릴 수 있다(`notifications.script.tl:13`, `notifications.script.tl:49`).

## 각 경고가 나타나는 때

| 경고 | 나타나는 때 | 사라지는 때 | 출처 |
|---|---|---|---|
| **차량이 멈췄습니다** | 플레이어의 운송 수단이 운행 중이고, 플레이어가 멈춘 것이 아니며, 게임 시간 **5분** 동안 속도가 0 | 다시 움직인다 | `notifications.script.tl:557-580` |
| **역이 작동하지 않음** | 역의 어느 터미널에서도 승객이 타거나 내리지 않고 집객 범위에 **아무것도** 없으며(창고, 산업, 마을 건물 없음), 플레이어의 노선이 그곳에 정차한다 | 집객 범위에 무언가 들어온다 | `notifications.script.tl:602-617`, `notifications.script.tl:630-647`, `station_useless.script.tl:39` |
| **역이 혼잡합니다** | 역에 기다리는 승객이나 화물이 수용량보다 많고(넘침), 플레이어의 노선이 그곳에 정차한다. 승객은 떠난다 | 넘침이 끝난다 | `notifications.script.tl:599`, `notifications.script.tl:649-661`, `overcrowding.script.tl:23` |
| **운송 수단 상태** | 플레이어의 운송 수단 상태가 **20 %** 이하 | 다시 **30 %**를 넘는다 | `notifications.script.tl:310-318` |
| **마을 평가 매우 형편없음** | 마을 평가 중 하나가 매우 형편없음(1/6 미만)으로 떨어진다 | 평가가 그저 그럼 이상으로 돌아온다 | `notifications.script.tl:230-238`, `town_util.tl:763-769`, `town_util.tl:983-985` |
| **마을 평가 악화 중** | 평가가 형편없음 또는 그저 그럼(50 % 미만)이고 매우 형편없음 경고에는 해당하지 않는다 | 평가가 좋음 이상이 된다 | `notifications.script.tl:240-248` |
| **산업 폐쇄** | 산업이 폐쇄 카운트다운을 시작한다 | 폐쇄되거나, 제때 다시 이용된다 | `notifications.script.tl:439-451`, `industry_close.script.tl:53-59` |
| **도로 연결 없음** | 역이 도로에 연결되어 있지 않다. **75일**마다 확인 | 다음 확인에서 도로가 발견된다 | `notifications.script.tl:16`, `notifications.script.tl:423-436` |
| **화물 하차 문제** | 운송 수단의 화물이 노선 어디에서도 하차되지 않는다 | 하차된다 | `notifications.script.tl:277-290`, `cargo_rtc_warning.script.tl:28-37` |

- **차량기지에 있는** 운송 수단은 멈춘 것으로 치지 않는다. 그 확인은 스크립트에서 꺼져 있다(`notifications.script.tl:563-564`). 플레이어가 멈춘 운송 수단도 마찬가지다.
- 역이 작동하지 않음 확인은 집객 범위만 본다. 터미널에서 이미 승객이 타고 내리는 역은 보고되지 않는다(`notifications.script.tl:606-610`).
- 마을 평가를 올리는 방법은 [마을 성장](towns.html)과 [평판](reputation.html), 폐쇄 카운트다운의 작동과 막는 방법은 [산업](industries.html), 상태가 운송 수단에 미치는 영향은 [비용, 유지비와 대출](costs.html)을 보라.

```engine
역이 넘치는지, 운송 수단에 경로가 있는지, 노선이 역에 닿을 수 있는지, 두 마을 사이 이동이 얼마나 걸려도 되는지는 엔진이 판단한다(calculateStationGroupCargo, getVehicleProblems, getLineProblems, getTownProblems). 스크립트는 그 답을 경고로 바꿀 뿐이다.
```

```tip scripts
차량이 멈췄습니다, 운송 수단 문제, 운송 수단 상태, 역이 혼잡합니다, 역을 사용할 수 없음은 새 게임의 기록에서 꺼져 있다. 알림 설정에서 켜 두자. 정체, 경로 없음, 낡은 차량들을 알려 주는 경고들이다.
```

## 노선, 정류장, 운송 수단 문제

이 경고들은 엔진의 노선과 운송 수단 확인에서 바로 나오며, 스크립트가 각각에 제목을 붙인다.

| 경고 | 경우 | 출처 |
|---|---|---|
| **노선 문제** | 역이 너무 적음, 같은 역이 연달아 두 번, 서로 호환되지 않는 역, 역을 연결할 수 없음, 대체 터미널을 연결할 수 없음 | `line_warning.script.tl:46-128` |
| **노선이 잘못 구성되었습니다** | 어디에서도 실을 수 없거나 내릴 수 없는 화물 종류, 싣도록 설정한 화물을 나를 수 있는 운송 수단이 없음, 설정한 화물을 하나도 나르지 않는 운송 수단이나 승객 노선의 화물 전용 운송 수단, 화물이 전혀 설정되지 않음 | `line_warning.script.tl:15-36`, `line_warning.script.tl:133` |
| **정류장 문제** | 현재 운송 수단이 쓸 수 없는 정류장, 화물 운송 수단(일부 또는 전부)이 쓰는 승객 정류장, 승객 운송 수단이 쓰는 화물 정류장, 그 정류장에서 싣거나 내릴 수 없는 설정된 화물 종류 | `line_station_warning.script.tl:6-87` |
| **운송 수단 문제** | 전철화된 경로 없음, 대형 항공기용 경로 없음, 대형 선박용 경로 없음, 경로가 전혀 없음, 두 열차가 서로 막음 | `vehicle_warning.script.tl:6-58` |
| **도시가 연결되지 않았습니다** | 두 마을 사이의 도로가 끊김, 두 마을 사이 이동이 너무 오래 걸림 | `town_warning.script.tl:7-19` |

- "대형 항공기용 경로가 없습니다"와 "대형 선박용 경로가 없습니다"는 운송 수단이 노선의 활주로, 부두, 수로에 비해 너무 크다는 뜻이다. [항공기](aircraft.html)와 [선박](ships.html)을 보라.

## 기록, 팝업, 설정

- 각 경고 종류는 알림 설정("알림 기록 설정")에서 끌 수 있다. 꺼진 종류는 팝업이 뜨지 않고 기록에도 남지 않는다(`notification_util.tl:145-146`, `notification_log.tl:480`).
- **새 게임**에서는 11가지 종류가 처음부터 꺼져 있다: **차량이 멈췄습니다**, **운송 수단 문제**, **운송 수단 상태**, **역이 혼잡합니다**, **역을 사용할 수 없음**, **역이 연결되지 않았습니다**, **도시가 연결되지 않았습니다**, **화물 하차되지 않음**, 그리고 회사의 조사, 마케팅 캠페인, 산업 녹화 진행 메시지(`stuck_vehicle.res.lua:7`, `vehicle_warning.res.lua:8`, `noroadconnection.res.lua:8`, `vehiclecondition.res.lua:8`, `overcrowding.res.lua:8`, `station_useless.res.lua:7`, `town_warning.res.lua:8`, `cargo_rtc_warning.res.lua:8`, `notification_util.tl:32-39`).
- 일회성 메시지(새 운송 수단, 새 건설, 등급 상승, 보조금)는 게임 시간 **60초** 후 팝업이 사라지며, 기록에는 남는다(`notification_util.tl:10`, `notifications.script.tl:85-94`).
- 알림이 가리키는 모든 것이 철거되거나 다시 지어져도 알림은 끝난다(`notifications.script.tl:95-107`).
- 미션에서는 알림이 일시 정지된 상태로 시작하며, 미션이 켤 때까지 그대로다(`notifications.script.tl:700-704`).

## 알아 두면 좋은 점

- 5분 뒤의 멈춤 경고는 이유를 말해 주지 않는다. 운송 수단을 살펴보자: 빨간 신호, 반대 방향의 일방 신호, 또는 같은 운송 수단의 운송 수단 문제 경고.
- "역이 작동하지 않음"은 "집객 범위에 아직 아무것도 없음"이라는 뜻일 뿐이다. 역을 집, 산업, 창고 가까이 옮기거나 역을 넓히자.
- 혼잡한 역은 승객을 잃는다. 운송 수단을 늘리거나 간격을 줄이자([출발과 대기](departure.html) 참고).

```check
official: The official wiki's User Interface page describes the notification button, the log and its filters, without the conditions of each warning. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: 위의 조건: 운행 중 속도 0으로 5분이면 멈춤, 운송 수단 상태 20 %에서 30 %까지, 마을 평가 매우 형편없음은 1/6 미만, 도로 연결은 75일마다 확인, 기본으로 11가지 종류가 꺼짐.
result: adds
```
