---
title: ランドマーク、祝賀、お楽しみ要素
summary: 各ランドマークに必要な貨物、解除されるランク、その町の車両への効果、ランドマークの必要資源 設定による倍率、そして祝賀、花火、飛行船、UFO が実際に何をするか。
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 9 | ランドマーク、会社ランク 2 から 15 までに 1 つずつ
fact: +20 % / -20 % / +25 % | その町の車両の最高速度、汚染、快適性
fact: ×0 から ×4 | ランドマークの必要資源 設定による必要貨物の倍率
fact: 2–4 年 | UFO が現れる間隔
---

ランドマークは工事現場のように建てる：会社ランクで解除し、設置してから**貨物を届ける**。現場に必要な貨物がすべてそろうとランドマークが完成し、**その町**の車両にボーナスを与える。本社は別の建物で、独自のルールがある（[会社ランク、特典、本社](company.html)を参照）。

## ランドマーク一覧

貨物量は **ランドマークの必要資源** ×1（ノーマル）の場合。

| ランドマーク | ランク | 届ける貨物 | その町の車両へのボーナス | ソース |
|---|---|---|---|---|
| **アンフィテアトルム** | 2 | 石 800 | 道路車両：騒音 **-25 %** | `arena.con.lua:10`、`arena.con.lua:20-26`、`arena.con.lua:39` |
| **大灯台** | 5 | 石 1,200、燃料 200 | 船舶：最高速度 **+20 %** | `lighthouse.con.lua:10`、`lighthouse.con.lua:14`、`lighthouse.con.lua:29`、`lighthouse.con.lua:48` |
| **白鷺城** | 7 | 石 1,200、板 400 | 列車：汚染 **-20 %** | `white_heron_castle.con.lua:10`、`white_heron_castle.con.lua:14`、`white_heron_castle.con.lua:28`、`white_heron_castle.con.lua:47` |
| **海事博物館** | 9 | 木材 600、板 600、生地 200 | 船舶：快適性 **+25 %** | `ship_museum.con.lua:10-18`、`ship_museum.con.lua:36`、`ship_museum.con.lua:55` |
| **ノイシュヴァンシュタイン城** | 10 | 石 1,000、板 600、染料 200 | 道路車両：快適性 **+25 %** | `neuschwanstein.con.lua:10-18`、`neuschwanstein.con.lua:36`、`neuschwanstein.con.lua:55` |
| **自由の女神像** | 11 | 石 800、鋼鉄 400、板金 400 | 船舶：汚染 **-20 %** | `statue_of_liberty.con.lua:10-18`、`statue_of_liberty.con.lua:38`、`statue_of_liberty.con.lua:57` |
| **頤和園** | 13 | 石 600、板 300、染料 300、家具 300 | 航空機：汚染 **-20 %** | `summer_palace.con.lua:10-22`、`summer_palace.con.lua:44`、`summer_palace.con.lua:63` |
| **オペラハウス** | 14 | 石 800、ガラス 400、板金 400、生地 400 | 列車：快適性 **+25 %** | `opera_house.con.lua:10-22`、`opera_house.con.lua:44`、`opera_house.con.lua:63` |
| **国会議事堂** | 15 | 石 800、板 400、ガラス 400、家具 400 | 道路車両、列車、船舶、航空機：最高速度 **+20 %** | `westminster.con.lua:10-22`、`westminster.con.lua:45`、`westminster.con.lua:79` |

- 各ランドマークはそのランクで 1 回だけ解除される。ランクの上がり方は[会社ランク、特典、本社](company.html)にある。
- ファイル上、ランドマークの建設費と年間費用は 0 で、必要なのは貨物だけである（`arena.con.lua:59-64`）。
- 現場は各貨物の半分ずつしか保管できないので、各貨物に少なくとも 2 回の配達が必要になる（`arena.con.lua:13-18`）。

## ランドマークの建設

- 現場には **4 段階**がある。貨物が届くにつれて進む：全貨物の 3 分の 1 で段階 2、3 分の 2 で段階 3、100 % で完成。各貨物は自分の量までしか数えないので、余分な石で足りない板を補うことはできない（`landmarks.script.tl:34-46`）。
- ボーナスはランドマークが**完成**したときにだけ働く（`landmark_util_serialized.tl:393-395`）。そのとき「建設完了」のメッセージが出る（`landmarks.script.tl:49-61`）。
- **ランドマークの必要資源** 設定はすべての貨物に倍率をかける：なし ×0、低 ×0.5、ノーマル ×1、高 ×2、極高 ×4。プリセットはイージー ×0.5、ノーマル ×1、ハード ×2、ベリーハード ×4。×0 では設置した時点でランドマークが完成する（`difficulty_util.tl:40`、`difficulty_util.tl:107`、`difficulty_util.tl:135`、`difficulty_util.tl:162`、`difficulty_util.tl:189`、`landmarks.script.tl:38`、`landmarks.script.tl:46`）。

## ボーナスを受けるのは誰か

- ボーナスは**ランドマークに最も近い町**と、最も近い町がその町である、対象の輸送手段の車両に与えられる（`landmark_util.tl:6-47`、`landmarks.script.tl:208-236`）。
- 車両が別の町のエリアに入ると、その町のボーナスを受け、前のボーナスは失う（`landmarks.script.tl:279-299`）。
- 同じ町にある複数のランドマークのボーナスは**加算される**：最高速度 +20 % が 2 つで +40 % になる（`landmark_util.tl:46`、`vehicle_modifier.script.tl:3-16`）。

```engine
ランドマークや走行中の車両の「最も近い町」がどこかはエンジンが決める（getConstructionClosestTown、closestTown）。快適性 +25 % や最高速度 +20 % が移動と収入にどう反映されるかもエンジンの仕事である。
```

```tip scripts
国会議事堂は車両が最も多く走る町に置くとよい：すべての輸送手段で最高速度 +20 %。同じ町の船舶には大灯台からもう +20 % がつく。中央集権化の実績は最も近い町が同じ完成済みランドマーク 10 個を求めるが、ゲームファイルには本社以外のランドマークが 9 個しかない（数えた結果）。このビルドで達成できるかは不明（[実績](achievements.html)を参照）。
```

## 祝賀

祝賀は、何かが初めて起きたときに町の上に表示される小さなお祝いである。町の**評判**も上げるが、評判がすでに満タンでないときだけである。

| イベント | 評判 | ソース |
|---|---|---|
| 町で初めて乗客があなたの路線に乗る | +50 % | `celebrations.script.tl:228-252` |
| 町に初めて貨物を届ける | +50 % | `celebrations.script.tl:187-198` |
| 町のレベルが上がる | +50 % | `celebrations.script.tl:260-272` |
| 産業に初めて貨物を届ける | 最も近い町に +20 % | `celebrations.script.tl:202-219` |

- 町のレベルが上がると、オフにしていない限り**花火**も上がる（`town_growth.script.tl:108-112`）。
- 評判の仕組み：[評判](reputation.html)。

## お楽しみ要素

- 町でマーケティングキャンペーンを始めると、その町の上を**飛行船**が飛ぶ（`fun_elements.script.tl:112-117`）。
- マップ上にいないとき、**UFO** がゲーム時間で **2 から 4 年**ごと（ランダム）に現れる（`fun_elements.script.tl:10`、`fun_elements.script.tl:79-91`）。クリックすると未知との遭遇の実績が得られる。
- どれも経済には影響しない。

## 知っておくと便利なこと

- 建てる前に町を選ぶこと：ボーナスは路線についていかず、その町の近くの車両にだけ効く。
- ベリーハードではランドマークに 4 倍の貨物が必要：国会議事堂なら石 3,200 と、ほかの貨物を各 1,600。

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: ランドマークは 9 個、ランク 2 から 15 までに 1 つずつ。どれも届けた貨物で 4 段階で建ち、ランドマークの必要資源 ×0 から ×4 で倍率がかかる。完成すると、最も近い町の 1 つの輸送手段の車両に 1 つのボーナス（最高速度 +20 %、汚染 -20 %、騒音 -25 %、快適性 +25 %）を与え、ボーナスは加算される。祝賀は評判を 50 % か 20 % 上げる。UFO は 2 から 4 年ごとに来る。
result: adds
```
