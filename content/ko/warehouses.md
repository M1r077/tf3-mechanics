---
title: 창고
summary: 범용 모듈과 특화된 모듈, 각 재고에 들어가는 것, 화물 종류 고정, 상차 속도, 비용과 오염, 그리고 창고가 하지 않는 일.
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
game: 40425
fact: 500 | 단위: 종류와 상관없이 모듈 하나당 화물
fact: ×2 | 특화된 모듈의 상차 속도, 범용 모듈은 ×1
fact: 15만 / 30만 | 범용 / 특화된 모듈의 가격
fact: 0 | 창고에 하차한 화물의 수입
---

창고는 입구 하나와 여러 **모듈**로 이루어진다. 창고는 두 노선 사이에서 화물을 보관한다. 한 노선이 하차하고, 다른 노선이 다시 상차한다. 역은 집객 범위를 통해 창고에 닿는다. 마을과 산업은 창고에서 아무것도 가져가지 않는다(공식 위키).

## 범용 모듈과 특화된 모듈

| 모듈 | 재고 | 보관하는 것 | 계수 | 출처 |
|---|---|---|---|---|
| **범용** | 모든 범용 모듈이 **하나의** 재고를 공유 | 어떤 화물이든, 섞어서 | ×1 | `warehouse.script.lua:272-295`, `modules.script.lua:49` |
| **액체**, **벌크**, **평상식**, **상품** | **모듈마다 재고 하나** | 한 번에 한 종류의 화물, 그 분류의 것 | ×2 | `warehouse.script.lua:296-314`, `modules.script.lua:120`, `modules.script.lua:165`, `modules.script.lua:247`, `modules.script.lua:296` |

- 모든 모듈은 **500** 단위를 더한다(`modules.script.lua:49`, `modules.script.lua:120`). 범용 모듈 다섯 개는 2500짜리 재고 하나를, 액체 모듈 다섯 개는 500짜리 재고 다섯 개를 만든다.
- 승객은 보관되지 않는다(`warehouse.script.lua:279`, `warehouse.script.lua:304`).
- 특화된 모듈은 한 번에 한 종류의 화물만 받는다. 원유와 연료를 보관하려면 액체 모듈이 두 개 필요하다(공식 위키).
- 특화된 모듈의 ×2는 플랫폼 계수와 곱해진다. 벌크 플랫폼과 벌크 모듈이면 ×4다. 자세한 내용: [상차 및 하차 속도](loading.html).

## 범용인가 특화인가?

1. **여러 종류의 화물을 조금씩**: 범용. 공유 재고 하나에, 가격도 오염도 절반이다.
2. **한 화물을 대량으로**(석탄, 원유, 통나무): 특화. 운송 수단이 그곳에서 두 배 빠르게 하차하고 상차하지만, 화물 종류마다 모듈이 하나씩 필요하다.
3. **식품처럼 배송 시간이 짧은 화물**: 특화. 공식 위키에 따르면 이 모듈은 배송 타이머를 멈춘다(아래 참조).
4. 한 창고에 두 종류를 섞을 수 있다. 범용 모듈은 여전히 재고 하나를 이루고, 특화된 모듈은 각각 자체 재고를 가진다.

## 창고가 하차를 빠르게 하는가?

- **특화된 모듈**: 그렇다. 받는 화물에 대해 ×2. 운송 수단의 상차 툴팁에 "특화된 창고: +100 %"가 표시된다(`cargo_react_util.tl:51-54`).
- **범용 모듈**: 아니다. 그 재고는 ×1로 생성되고, 모듈이 요청하는 ×2는 무시된다(`warehouse.script.lua:284`, `warehouse.script.lua:288-289`).
- 화물 일부는 창고로, 일부는 산업으로 갈 때 운송 수단은 이들을 번갈아 처리하므로, 한 번 정차하는 동안 속도가 바뀐다(게임 내 측정, [상차 및 하차 속도](loading.html) 참조).

## 재고 섹션

- 재고마다 한 줄: 받는 화물, 양, 그리고 마우스를 올리면 **남은 배송 시간 평균**(`entity_window_util.tl:408-410`).
- **화물 종류 고정**: 특화된 모듈에서 화물 아이콘을 클릭한다. 게임은 그 모듈을 이 화물 전용으로 하여 창고를 다시 짓는다(`entity_window_util.tl:339-367`, `warehouse.script.lua:308`). 모듈을 제거하거나 교체하면 고정이 풀린다(`warehouse.script.lua:403-405`).
- **모든 화물 버리기**: 그 줄을 즉시 비운다(`entity_window_util.tl:423-434`). 화물은 사라진다.
- 두 버튼은 다른 플레이어가 소유한 창고에만 없다. 자신의 창고와 소유자가 없는 창고에는 있다(`warehouse_eow.script.tl:127-137`, `gui/entity_window/warehouse/warehouse.tl:38`, `entity_util.tl:83-86`).
- **통계** 차트는 연도별 **수신**(하차한 양)과 **발신**(상차한 양)을 보여준다(`warehouse_eow.script.tl:159-160`).

## 비용과 오염

| | 범용 모듈 | 특화된 모듈 | 출처 |
|---|---|---|---|
| 가격 | 15만 | 30만 | `wh_universal.module.lua:18`, `wh_liquid.module.lua:22` |
| 연간 관리비 | 2.5만 | 5만 | `wh_universal.module.lua:19`, `wh_liquid.module.lua:23` |
| 소음 | 20 | 20 | `wh_universal.module.lua:33`, `wh_liquid.module.lua:37` |
| 오염 | 25 | 50 | `wh_universal.module.lua:34`, `wh_liquid.module.lua:38` |

- 창고 자체도 오염을 더한다. **25**, 특화된 모듈을 하나라도 지으면 **50**이다(`warehouse.script.lua:327`, `warehouse.script.lua:338-345`).
- 건설 메뉴에는 분류와 시대(1900년, 1940년, 1980년부터)마다 항목이 하나씩 있다(`warehouses/warehouse.tl:3-5`). 뒤의 시대는 ×3과 ×9를 보여주며, 창고 관리비도 연도에 따라 커진다. 자세한 내용: [비용, 관리비, 대출](costs.html).
- 벌크, 평상식, 상품 모듈은 액체 모듈과 비용이 같다(`wh_bulk.module.lua:22-23`, `wh_flatbed.module.lua:22-23`, `wh_goods.module.lua:18-19`).

```engine
스크립트는 두 가지 배출 수준을 주며, 두 번째는 첫 번째의 두 배다(`warehouse.script.lua:342-343`). 창고는 재고가 찰수록 첫 번째에서 두 번째로 옮겨 가며, 재고가 가득 차면 두 배다(`emissions.script.tl:237-249`). 모듈에 실제로 청구되는 가격은 엔진이 계산한다.
```

## 창고가 하지 않는 일

- **아무것도 지불하지 않는다.** 창고에 하차해도 수입이 없다. 화물은 소비처에 도착할 때 한 번만, 출발지로부터의 직선 거리에 대해 지불된다(게임 내 측정, [화물 수입과 배송 시간](income.html) 참조).
- **근처의 마을이나 산업에 공급하지 않는다**: 그들은 운송 수단에서만 화물을 받는다(공식 위키).
- **노선 자동 구성의 목적지가 아니다.** 자동 구성은 생산자와 소비자만 찾는다. 하지만 어떤 화물을 보관하는 창고 옆 정류장에서는 그 화물이 상차 목록에서 빠지므로, 열차는 거기서 그 화물을 하차한다([상차 및 하차 속도](loading.html) 참조).
- **도로가 필요 없다.** 입구는 도로에 붙지만, 화물은 역의 집객 범위를 통해서만 이동한다(`warehouse.script.lua:386-389`, 공식 위키). 창고 창은 집객 범위를 보여준다(`gui/entity_window/warehouse/warehouse.tl:88-96`).

```engine
하차한 화물이 어디로 가는지, 그리고 보관된 화물의 배송 타이머가 멈추는지는 엔진이 정한다. 타이머를 멈추는 스크립트는 없다. 공식 위키에 따르면 특화된 모듈은 멈추고, 범용 모듈은 멈추지 않는다.
```

## 알아두면 좋은 점

- 창고 근처의 모든 정류장의 상차 목록을 확인하자. 목록에 없는 것은 노선 중간이라도 창고에 하차된다.
- 가득 찬 재고는 더 이상 화물을 받지 않는다. 단, 정류장이 "도착 시 모든 화물 강제 하차"를 쓰면 받으며, 들어가지 않는 것은 파괴된다([상차 및 하차 속도](loading.html) 참조).
- 특화된 모듈을 한 화물 전용으로 두려면 재고 섹션에서 그 화물 종류를 고정한다.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard)는 역마다 닿는 범위의 창고와 그 재고를 보여준다. [Platform Details](https://mod.io/g/transportfever3/m/platform-details)는 하차한 화물이 어디로 갔는지 보여준다.

```check
official: "Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types." Specialised warehouses "freeze the cargo item's delivery timer" and "enable faster loading / unloading speeds". "In specialized warehouses, only one cargo type can be stored at a time for a given module." ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: 범용 모듈은 계수 ×1인 공유 재고 하나를 이룬다. 특화된 모듈은 각각 ×2이고 한 종류의 화물만 담는 500짜리 자체 재고를 가진다. 특화된 모듈은 비용이 두 배(30만, 관리비 5만)이고 오염도 두 배(50)다. 타이머 정지는 스크립트에 없다.
result: refines
```
