---
title: 랜드마크, 축하 행사, 재미 요소
summary: 각 랜드마크에 필요한 화물, 해제되는 랭크, 그 마을 운송 수단에 주는 효과, 랜드마크 필요 자원 설정의 배율, 그리고 축하 행사, 불꽃놀이, 비행선, UFO가 실제로 하는 일.
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40444
fact: 9 + 3 | 랜드마크: 기본 게임에 9개(랭크 2~15), DLC 팩으로 3개 더(랭크 1)
fact: +20 % / +25 % / -20 % / -25 % | 그 마을 운송 수단의 최고 속도, 오염 또는 편안함
fact: ×0 ~ ×4 | 랜드마크 필요 자원 설정에 따른 필요 화물 배율
fact: 2–4년 | UFO 두 대 사이의 간격
---

랜드마크는 공사 현장처럼 짓는다: 회사 랭크로 해제하고, 배치한 다음 **화물을 배달**한다. 현장에 필요한 화물이 모두 모이면 랜드마크가 완성되고 **그 마을**의 운송 수단에 보너스를 준다. 본사는 별개의 건물이며 고유한 규칙이 있다([회사 랭크, 특전, 본사](company.html) 참고).

## 랜드마크 목록

화물량은 **랜드마크 필요 자원** ×1(보통) 기준.

| 랜드마크 | 랭크 | 배달할 화물 | 그 마을 운송 수단의 보너스 | 출처 |
|---|---|---|---|---|
| **원형극장** | 2 | 석재 800 | 도로 차량: 소음 **-25 %** | `arena.con.lua:10`, `arena.con.lua:20-26`, `arena.con.lua:39` |
| **알렉산드리아 등대** | 5 | 석재 1,200, 연료 200 | 선박: 최고 속도 **+20 %** | `lighthouse.con.lua:10`, `lighthouse.con.lua:14`, `lighthouse.con.lua:29`, `lighthouse.con.lua:48` |
| **히메지성** | 7 | 석재 1,200, 널빤지 400 | 열차: 오염 **-20 %** | `white_heron_castle.con.lua:10`, `white_heron_castle.con.lua:14`, `white_heron_castle.con.lua:28`, `white_heron_castle.con.lua:47` |
| **선박 박물관** | 9 | 통나무 600, 널빤지 600, 천 200 | 선박: 편안함 **+25 %** | `ship_museum.con.lua:10-18`, `ship_museum.con.lua:36`, `ship_museum.con.lua:55` |
| **노이슈반슈타인 성** | 10 | 석재 1,000, 널빤지 600, 염료 200 | 도로 차량: 편안함 **+25 %** | `neuschwanstein.con.lua:10-18`, `neuschwanstein.con.lua:36`, `neuschwanstein.con.lua:55` |
| **자유의 여신상** | 11 | 석재 800, 강철 400, 판금 400 | 선박: 오염 **-20 %** | `statue_of_liberty.con.lua:10-18`, `statue_of_liberty.con.lua:38`, `statue_of_liberty.con.lua:57` |
| **이화원** | 13 | 석재 600, 널빤지 300, 염료 300, 가구 300 | 항공기: 오염 **-20 %** | `summer_palace.con.lua:10-22`, `summer_palace.con.lua:44`, `summer_palace.con.lua:63` |
| **오페라 하우스** | 14 | 석재 800, 유리 400, 판금 400, 천 400 | 열차: 편안함 **+25 %** | `opera_house.con.lua:10-22`, `opera_house.con.lua:44`, `opera_house.con.lua:63` |
| **국회의사당** | 15 | 석재 800, 널빤지 400, 유리 400, 가구 400 | 도로 차량, 열차, 선박, 항공기: 최고 속도 **+20 %** | `westminster.con.lua:10-22`, `westminster.con.lua:45`, `westminster.con.lua:79` |

**DLC 랜드마크.** DLC 팩 두 개가 세 개를 더 추가하며, 랭크 1부터 해제된다. 그 파일은 게임의 DLC 폴더(Deluxe Upgrade Pack, Pre-order Pack)에 있어 이 위키가 색인하는 기본 파일 밖에 있으므로, 여기에는 출처 링크가 없다.

| 랜드마크 | DLC | 랭크 | 배달할 화물 | 그 마을 운송 수단의 보너스 |
|---|---|---|---|---|
| **에펠탑** | Deluxe Upgrade Pack | 1 | 강철 400 | 도로 차량: 최고 속도 **+25 %** |
| **타지마할** | Deluxe Upgrade Pack | 1 | 석재 800 | 항공기: 소음 **-25 %** |
| **대피라미드** | Pre-order Pack | 1 | 석재 800 | 열차: 최고 속도 **+25 %** |

- 각 랜드마크는 해당 랭크에서 한 번만 해제된다. 랭크가 오르는 방식은 [회사 랭크, 특전, 본사](company.html)에 있다.
- 파일상 랜드마크는 건설비도 연간 비용도 없고, 화물만 필요하다(`arena.con.lua:59-64`).
- 현장은 각 화물의 절반씩만 보관하므로, 화물마다 최소 두 번은 배달해야 한다(`arena.con.lua:13-18`).

## 랜드마크 건설

- 현장에는 **4단계**가 있다. 화물이 도착하면서 올라간다: 전체 화물의 3분의 1에서 2단계, 3분의 2에서 3단계, 100 %에서 완성. 각 화물은 자기 양까지만 세므로, 남는 석재로 모자란 널빤지를 채울 수 없다(`landmarks.script.tl:34-46`).
- 보너스는 랜드마크가 **완성**되었을 때만 작동한다(`landmark_util_serialized.tl:393-395`). 그때 "건축 완료됨" 메시지가 나온다(`landmarks.script.tl:49-61`).
- **랜드마크 필요 자원** 설정은 모든 화물에 배율을 곱한다: 없음 ×0, 낮음 ×0.5, 보통 ×1, 높음 ×2, 아주 높음 ×4. 프리셋은 쉬움 ×0.5, 보통 ×1, 어려움 ×2, 매우 어려움 ×4. ×0에서는 배치하자마자 랜드마크가 완성된다(`difficulty_util.tl:40`, `difficulty_util.tl:107`, `difficulty_util.tl:135`, `difficulty_util.tl:162`, `difficulty_util.tl:189`, `landmarks.script.tl:38`, `landmarks.script.tl:46`).

## 누가 보너스를 받나

- 보너스는 **랜드마크에서 가장 가까운 마을**과, 가장 가까운 마을이 그 마을인 해당 운송 수단의 차량에 간다(`landmark_util.tl:6-47`, `landmarks.script.tl:208-236`).
- 운송 수단이 다른 마을의 영역으로 들어가면 그 마을의 보너스를 받고 이전 보너스는 잃는다(`landmarks.script.tl:279-299`).
- 같은 마을에 있는 여러 랜드마크의 보너스는 **합산된다**: 최고 속도 +20 % 두 개면 +40 %(`landmark_util.tl:46`, `vehicle_modifier.script.tl:3-16`).

```engine
랜드마크나 움직이는 운송 수단의 "가장 가까운 마을"이 어디인지는 엔진이 정한다(getConstructionClosestTown, closestTown). 편안함 +25 %나 최고 속도 +20 %가 이동과 수입에 어떻게 반영되는지도 엔진의 일이다.
```

```tip scripts
국회의사당은 운송 수단이 가장 많이 다니는 마을에 지어라: 모든 운송 수단의 최고 속도 +20 %. 같은 마을의 선박은 알렉산드리아 등대에서 +20 %를 더 받는다. 중앙 집중 업적은 가장 가까운 마을이 같은 완성된 랜드마크 10개를 요구한다. 본사는 배달할 화물이 없으므로 세지 않는다. 기본 게임에는 랜드마크가 9개 있고 DLC 팩이 3개를 더한다(직접 셈). DLC 없이 중앙 집중을 달성할 수 있는지는 알 수 없다([업적](achievements.html) 참고).
```

## 축하 행사

축하 행사는 어떤 일이 처음 일어났을 때 마을 위에 표시되는 작은 파티다. 마을의 **평판**도 올리지만, 평판이 이미 가득 차 있지 않을 때만이다.

| 이벤트 | 평판 | 출처 |
|---|---|---|
| 마을에서 처음으로 승객이 당신의 노선에 탐 | +50 % | `celebrations.script.tl:228-252` |
| 마을에 처음으로 화물을 배달 | +50 % | `celebrations.script.tl:187-198` |
| 마을 레벨이 오름 | +50 % | `celebrations.script.tl:260-272` |
| 산업에 처음으로 화물을 배달 | 가장 가까운 마을에 +20 % | `celebrations.script.tl:202-219` |

- 마을 레벨이 오르면 꺼 두지 않은 한 **불꽃놀이**도 터진다(`town_growth.script.tl:108-112`).
- 평판의 원리: [평판](reputation.html).

## 재미 요소

- 마을에서 마케팅 캠페인을 시작하면 그 마을 위로 **비행선**이 난다(`fun_elements.script.tl:112-117`).
- 맵에 없을 때 **UFO**가 게임 시간으로 **2~4년**마다(무작위) 나타난다(`fun_elements.script.tl:10`, `fun_elements.script.tl:79-91`). 클릭하면 외계와의 조우 업적을 얻는다.
- 어느 것도 경제를 바꾸지 않는다.

## 알아 두면 좋은 점

- 짓기 전에 마을을 골라라: 보너스는 노선을 따라가지 않고, 그 마을 근처의 운송 수단에만 적용된다.
- 매우 어려움에서는 랜드마크에 화물이 4배 필요하다: 국회의사당은 석재 3,200과 나머지 화물 각 1,600.

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: 기본 랜드마크 9개, 랭크 2부터 15까지 하나씩, 그리고 랭크 1의 DLC 랜드마크 3개. 모두 배달된 화물로 4단계에 걸쳐 지어지며 랜드마크 필요 자원 ×0~×4로 배율이 붙는다. 완성되면 가장 가까운 마을에서 한 운송 수단의 차량에 보너스 하나(최고 속도 +20 % 또는 +25 %, 오염 -20 %, 소음 -25 %, 편안함 +25 %)를 주며, 보너스는 합산된다. 축하 행사는 평판을 50 % 또는 20 % 올리고, UFO는 2~4년마다 온다.
result: adds
```
