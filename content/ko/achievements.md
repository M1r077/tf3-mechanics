---
title: 업적
summary: 게임 스크립트가 자유 게임의 각 업적에서 무엇을 언제 확인하는지, 어떤 업적이 기본 게임의 운송 수단, 화물, 동물만 세는지, 그리고 엔진에 맡겨진 확인.
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-24
game: 40444
fact: 17 | 게임 스크립트가 직접 해제하는 업적
fact: 500 m | 꼭대기 체류에서 정류장에 선 열차의 첫 차량 높이
fact: < 1 % | 내가 안 그랬어를 위한 마을 평판
fact: 10 | 중앙 집중을 위해 가장 가까운 마을이 같아야 하는 랜드마크
---

공식 위키에는 41개의 업적이 있다. 게임 스크립트 (`achievements.script.tl`)은 그중 **17개**를 직접 해제하고 **게임 간 카운터 9개**에 값을 보낸다. 나머지(캠페인, 날씨, 마을 크기, 창고, 이자, 부스터, 자동차, 1900-2000, 2000년대의 증기)는 엔진이나 플랫폼 등 다른 곳에서 확인한다. 모든 확인은 먼저 업적을 아직 해제할 수 있는지 엔진에 묻는다. 모드나 설정 때문에 막히는지는 그쪽에서 정해진다(`achievements.script.tl:632`, `achievements.script.tl:510`).

## 스크립트가 확인하는 업적

| 업적 | 스크립트가 확인하는 것 | 출처 |
|---|---|---|
| **택배 도착** | 화물 하나가 목적지에 도착한다 | `achievements.script.tl:221-225`, `achievements.script.tl:632-636` |
| **당신을 대신하여** | 보조금 하나를 완료한다 | `achievements.script.tl:241-244`, `achievements.script.tl:638-642` |
| **보조금 연속 기록** | 중간에 실패 없이 보조금 10개를 완료한다. 실패하면 횟수가 0으로 돌아간다 | `achievements.script.tl:243-249`, `achievements.script.tl:644-648` |
| **관리인** | 마을의 배송 평가가 **탁월함**으로 바뀐다 | `achievements.script.tl:270-276`, `towns.script.tl:27-30`, `achievements.script.tl:650-654` |
| **도시 개발** | 마을 레벨이 오른다 | `achievements.script.tl:253-255`, `town_growth.script.tl:92` |
| **수요 증가** | 마을에 새 화물 종류 수요가 생긴다 | `achievements.script.tl:257-259`, `achievements.script.tl:668-672` |
| **내가 안 그랬어** | 마을 평판이 **내려가서** **1 %** 미만이 된다 | `achievements.script.tl:261-267`, `towns.script.tl:33-36` |
| **승진** | 회사 등급이 오른다 | `achievements.script.tl:280-282`, `achievements.script.tl:680-684` |
| **출세 가도** | 회사가 최고 등급에 도달한다 | `achievements.script.tl:284-290`, `achievements.script.tl:686-690` |
| **조경사** | 한 번의 건설에서 나무만 놓는다(아무것도 제거하지 않고, 재조림으로도 아님) | `achievements.script.tl:346-377` |
| **완벽주의자** | 같은 역을 철거, 재건, 철거, 재건 순서로 하고, 그사이 다른 역을 짓거나 제거하지 않는다 | `achievements.script.tl:304-341`, `achievements.script.tl:694-710` |
| **중앙 집중** | 완성된 랜드마크 정확히 10개의 가장 가까운 마을이 같다 | `achievements.script.tl:382-395`, `achievements.script.tl:713-721` |
| **꼭대기 체류** | 플레이어의 열차가 첫 차량이 **500 m**보다 높은 상태로 정류장에 도착한다 | `achievements.script.tl:407-417`, `achievements.script.tl:723-727` |
| **바다로** | 플레이어의 헬리콥터가 석유 플랫폼의 정류장에 도착한다 | `achievements.script.tl:420-450`, `achievements.script.tl:729-733` |
| **유산 함대** | 기본 게임의 모든 선박 모델이 동시에 플레이어의 선박 노선에서 운행 중이다 | `achievements.script.tl:735-776` |
| **외계와의 조우** | UFO를 클릭한다 | `achievements.script.tl:793-806` |
| **시간 능력자** | 시간대를 직접 바꾼다 | `achievements.script.tl:839-844` |

- **완벽주의자**는 역 전체 하나를 추가하거나 제거하는 건설만 센다. 역에 승강장이나 모듈을 추가하는 것은 세지 않는다(`achievements.script.tl:301-302`).
- **중앙 집중**은 각 랜드마크를 완성된 순간 그때 가장 가까운 마을의 것으로 센다(`achievements.script.tl:386`).
- **유산 함대**는 한 번도 정차한 적 없는 선박 모델이 정류장에 도착할 때만 확인된다. 차량기지의 배가 아니라 선박 노선의 운송 수단을 본다(`achievements.script.tl:736`, `achievements.script.tl:750-766`).
- **내가 안 그랬어**에는 다른 평가가 아닌 평판이 필요하다. [마을 평판](reputation.html)을 보라.

```tip scripts
꼭대기 체류는 역 건물의 높이가 아니라 열차가 설 때 첫 차량의 높이를 확인한다. 500 m가 넘는 산 위에 역을 짓고 열차 하나를 운행하자.
```

## 게임 간 카운터

이 카운터들은 게임에서 게임으로 이어진다(플랫폼이 저장한다). 스크립트는 지난 확인 이후 바뀐 만큼만 보낸다.

| 카운터 | 업적 | 세는 것 | 출처 |
|---|---|---|---|
| 선로 길이 | **세계 곳곳** | 기록부 총 길이(km)의 증가분. 제거해도 빼지 않는다 | `achievements.script.tl:511-523` |
| 인구 | **지구 인구** | 게임을 불러왔을 때의 인구에서 늘어난 맵 인구 | `achievements.script.tl:512`, `achievements.script.tl:525-533` |
| 승객 | **승객의 개척자** | 플레이어의 노선에서 이동을 마친 승객 | `achievements.script.tl:236-238`, `achievements.script.tl:535-541` |
| 화물 | **화물의 개척자** | 배송된 화물 | `achievements.script.tl:543-549` |
| 기후 | **타이쿤의 거물** | 회사가 최고 등급에 도달했을 때 맵의 기후 | `achievements.script.tl:551-567` |
| 수입 | **사악한 돈** | 수입 합계(10억 단위) | `achievements.script.tl:202-204`, `achievements.script.tl:569-590` |
| 화물 종류 | **마스터 판매원** | 기본 게임의 각 화물 종류를 한 번씩 배송 | `achievements.script.tl:20-22`, `achievements.script.tl:230-232`, `achievements.script.tl:592-607` |
| 운송 수단 | **전문가** | 기본 게임의 각 운송 수단 모델이 한 번씩 정류장에 도착 | `achievements.script.tl:16-18`, `achievements.script.tl:469-481`, `achievements.script.tl:609-625` |
| 동물 | **동물 사랑꾼** | 기본 게임의 각 동물을 한 번씩 클릭 | `achievements.script.tl:24-26`, `achievements.script.tl:809-834` |

- 모드의 운송 수단, 화물, 동물은 이 카운터에 절대 세지 않는다. 기본 게임의 파일(`::/vehicle`, `::/cargos`, `::/animal`)만 쓴다(`achievements.script.tl:16-26`).
- 전문가에서는 운송 수단이 노선의 **정류장에 도착**해야 한다. 구매만으로는 부족하다.

```engine
업적을 아직 해제할 수 있는지(isAchievementUnlockable), 카운터가 꺼져 있는지(areStatsDisabled), 각 카운터의 목표, 그리고 스크립트에 없는 24개 업적은 엔진과 플랫폼이 처리한다. 공식 위키에 따르면 외형용이 아닌 모드를 쓰거나 게임플레이 설정을 표준값에서 바꾸면 업적은 대체로 얻을 수 없다.
```

## 모드와 업적

모드를 쓴다고 해서 업적이 저절로 꺼지는 것은 **아니다**. 중요한 것은 활성화된 각 모드가 **cosmetic**(외형용)으로 표시되어 있는지다.

- 모든 모드는 `mod.json`에 `cosmetic` 플래그가 있다. 게임 자체의 API 문서(폴더 `api/tealdef`, 필드 `ModDesc.cosmetic`)에는 "If the mod is purely cosmetic, cosmetic mods still allow achievement from being earned while playing"(모드가 순수하게 외형용이면, 외형용 모드를 써도 플레이 중 업적을 얻을 수 있다)라고 적혀 있다.
- 엔진은 활성화된 모드 목록을 확인하고(`ModRep.couldAchievementsBeEarned`) 그 결과를 각 세이브 파일에 저장한다(`achievementsEarnable`). 같은 폴더에 있다.
- 공식 DLC와 캠페인 미션도 모드이며, 모두 cosmetic으로 표시되어 있다(`dlcs/*/mod.json`, `mods/release/urbangames_campaign*/mod.json`).
- 업적이 막히면 게임이 알려 준다. "Achievements Disabled!"(업적 비활성화!)와 "Achievements cannot be earned."(업적을 얻을 수 없습니다.) 메시지가 있다(`base/strings`).

따라서 외형용 모드만 쓰는 게임에서는 업적을 계속 얻을 수 있다. 외형용이 아닌 모드가 하나라도 있거나 게임플레이 설정이 표준값에서 벗어나면 업적이 막힌다(공식 위키).

```engine
정확한 규칙(어떤 설정이 해당되는지, 한 번 막힌 세이브 파일이 모드를 제거한 뒤에도 계속 막혀 있는지)은 엔진에서 결정되며 읽을 수 있는 파일에는 없다: 알 수 없음.
```

```tip scripts
플래그는 모드 제작자가 정한다. 모드의 `mod.json`에서 `cosmetic` 줄을 확인하거나 제작자에게 물어보자. 게임플레이(비용, 생산, 규칙)를 바꾸는 모드는 대개 외형용이 아니다.
```

## 알아 두면 좋은 점

- "처음" 업적은 지난 확인과 비교해서 확인된다. 업적이 아직 열려 있는 게임에서 **새** 사건이 필요하며, 저장 파일에 있던 예전 보조금이나 등급은 다시 세지 않는다(`achievements.script.tl:633`, `achievements.script.tl:779`).
- 등급, 보조금, 평판은 [회사 등급, 혜택과 본사](company.html), [보조금](subsidies.html), [마을 평판](reputation.html)에서 설명한다.

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: 스크립트에는 업적 17개와 카운터 9개가 있다. 공식 설명을 구체화한다: 관리인은 배송 평가가 탁월함에 이르는 것, 내가 안 그랬어는 평판 1 % 미만, 꼭대기 체류는 첫 차량이 500 m 위, 완벽주의자는 같은 역의 철거-재건-철거-재건, 유산 함대는 기본 게임의 모든 선박 모델이 동시에 노선에 있는 것. 카운터에는 기본 게임의 운송 수단, 화물, 동물만 센다.
result: refines
```
