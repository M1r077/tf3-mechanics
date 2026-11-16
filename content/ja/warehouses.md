---
title: 倉庫
summary: 汎用モジュールと専門モジュール、各在庫に入るもの、貨物の種類の固定、積載速度、コストと汚染、そして倉庫がしないこと。
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
game: 40425
fact: 500 | 単位：種類に関係なく、モジュール 1 つあたりの貨物
fact: ×2 | 専門モジュールでの積載速度、汎用モジュールでは ×1
fact: 15万 / 30万 | 汎用 / 専門モジュールの価格
fact: 0 | 倉庫で積み下ろした貨物の収入
---

倉庫は入口と一組の**モジュール**でできている。倉庫は 2 つの路線の間で貨物を保管する。1 つの路線が積み下ろし、別の路線がまた積み込む。駅は集客範囲を通じて倉庫に届く。町や産業は倉庫から何も受け取らない（公式wiki）。

## 汎用モジュールと専門モジュール

| モジュール | 在庫 | 入るもの | 係数 | ソース |
|---|---|---|---|---|
| **汎用** | すべての汎用モジュールが**1 つ**の在庫を共有する | どの貨物でも、混在可 | ×1 | `warehouse.script.lua:272-295`、`modules.script.lua:49` |
| **液体**、**ばら積み**、**平型**、**商品** | **モジュールごとに 1 つの在庫** | 一度に 1 種類の貨物、そのクラスのもの | ×2 | `warehouse.script.lua:296-314`、`modules.script.lua:120`、`modules.script.lua:165`、`modules.script.lua:247`、`modules.script.lua:296` |

- どのモジュールも **500** 単位を追加する（`modules.script.lua:49`、`modules.script.lua:120`）。汎用モジュール 5 つで 2500 の在庫が 1 つ、液体モジュール 5 つで 500 の在庫が 5 つになる。
- 乗客は保管されない（`warehouse.script.lua:279`、`warehouse.script.lua:304`）。
- 専門モジュールは一度に 1 種類の貨物しか受け取らない。原油と燃料を保管するには液体モジュールが 2 つ必要である（公式wiki）。
- 専門モジュールの ×2 はプラットフォーム係数と掛け合わされる。ばら積みプラットフォームとばら積みモジュールで ×4 になる。詳細：[積み込みと積み下ろしの速度](loading.html)。

## 汎用か専門か

1. **多くの種類の貨物を少量ずつ**：汎用。共有の在庫が 1 つで、価格も汚染も半分。
2. **1 種類の貨物を大量に**（石炭、原油、丸太）：専門。車両はそこで 2 倍速く積み下ろし・積み込みをするが、貨物の種類ごとに 1 つのモジュールが必要。
3. **食料など配送時間の短い貨物**：専門。公式wikiによると、これらのモジュールは配送タイマーを止める（下記参照）。
4. 1 つの倉庫に両方を混ぜてもよい。汎用モジュールは引き続き 1 つの在庫をつくり、専門モジュールはそれぞれ独自の在庫を持つ。

## 倉庫で積み下ろしは速くなるか

- **専門モジュール**：はい。受け取る貨物について ×2。車両の積載ツールチップに「専門倉庫：+100 %」と表示される（`cargo_react_util.tl:51-54`）。
- **汎用モジュール**：いいえ。その在庫は ×1 で作られ、モジュールが要求する ×2 は無視される（`warehouse.script.lua:284`、`warehouse.script.lua:288-289`）。
- 貨物の一部が倉庫へ、一部が産業へ行くとき、車両はそれらに順番に渡すので、1 回の停車中に速度が変わる（ゲーム内で計測、[積み込みと積み下ろしの速度](loading.html) を参照）。

## 「在庫」セクション

- 在庫ごとに 1 行：受け取る貨物、量、そしてカーソルを合わせると表示される**平均残り配送時間**（`entity_window_util.tl:408-410`）。
- **貨物の種類を固定する**：専門モジュールで貨物アイコンをクリックする。ゲームはそのモジュールをこの貨物専用にして倉庫を作り直す（`entity_window_util.tl:339-367`、`warehouse.script.lua:308`）。モジュールを撤去または置き換えると、固定は解除される（`warehouse.script.lua:403-405`）。
- **すべての貨物を捨てる**：その行をすぐに空にする（`entity_window_util.tl:423-434`）。貨物は失われる。
- どちらのボタンも、ほかのプレイヤーが所有する倉庫にだけない。自分の倉庫と所有者のいない倉庫にはある（`warehouse_eow.script.tl:127-137`、`gui/entity_window/warehouse/warehouse.tl:38`、`entity_util.tl:83-86`）。
- **統計**のグラフは、年ごとの**入庫**（積み下ろした分）と**出庫**（積み込んだ分）を示す（`warehouse_eow.script.tl:159-160`）。

## コストと汚染

| | 汎用モジュール | 専門モジュール | ソース |
|---|---|---|---|
| 価格 | 15万 | 30万 | `wh_universal.module.lua:18`、`wh_liquid.module.lua:22` |
| 年間の維持費 | 2.5万 | 5万 | `wh_universal.module.lua:19`、`wh_liquid.module.lua:23` |
| 騒音 | 20 | 20 | `wh_universal.module.lua:33`、`wh_liquid.module.lua:37` |
| 汚染 | 25 | 50 | `wh_universal.module.lua:34`、`wh_liquid.module.lua:38` |

- 倉庫自体も汚染を加える。**25**、専門モジュールを 1 つでも建てると **50** になる（`warehouse.script.lua:327`、`warehouse.script.lua:338-345`）。
- 建設メニューには、クラスと時代（1900 年、1940 年、1980 年から）ごとに 1 つの項目がある（`warehouses/warehouse.tl:3-5`）。後の時代は ×3 と ×9 を示し、倉庫の維持費も年とともに増える。詳細：[コスト、維持費、融資](costs.html)。
- ばら積み、平型、商品のモジュールは、液体モジュールと同じコストである（`wh_bulk.module.lua:22-23`、`wh_flatbed.module.lua:22-23`、`wh_goods.module.lua:18-19`）。

```engine
スクリプトは 2 つの排出レベルを与え、2 つ目は 1 つ目の 2 倍である（`warehouse.script.lua:342-343`）。倉庫は在庫が埋まるにつれて 1 つ目から 2 つ目へ移り、在庫が満杯なら 2 倍になる（`emissions.script.tl:237-249`）。モジュールに実際に請求される価格はエンジンが計算する。
```

## 倉庫がしないこと

- **何も支払わない。** 倉庫で積み下ろしても収入はない。品物は消費者に届いたときに 1 回だけ、出発地からの直線距離に対して支払われる（ゲーム内で計測、[貨物収入と配送時間](income.html) を参照）。
- **近くの町や産業に供給しない**：それらは車両からしか貨物を受け取らない（公式wiki）。
- **路線の自動設定の目的地にならない**。自動設定は生産者と消費者だけを探す。ただし、ある貨物を保管する倉庫の隣の停車地では、その貨物が積込リストから外れるので、列車はそこで積み下ろす（[積み込みと積み下ろしの速度](loading.html) を参照）。
- **道路は要らない。** 入口は道路にスナップするが、貨物は駅の集客範囲を通じてしか動かない（`warehouse.script.lua:386-389`、公式wiki）。倉庫ウィンドウは集客範囲を表示する（`gui/entity_window/warehouse/warehouse.tl:88-96`）。

```engine
積み下ろした貨物がどこへ行くか、保管された品物の配送タイマーが止まるかどうかは、エンジンが決める。タイマーを止めるスクリプトはない。公式wikiによると、専門モジュールは止め、汎用モジュールは止めない。
```

## 知っておくと便利なこと

- 倉庫の近くにあるすべての停車地の積込リストを確認すること。リストにないものは、路線の途中でも倉庫に積み下ろされる。
- 満杯の在庫はそれ以上の貨物を拒む。ただし停車地が「到着時にすべての貨物を強制的に積み下ろし」を使っていれば別で、入りきらない分は破壊される（[積み込みと積み下ろしの速度](loading.html) を参照）。
- 専門モジュールを 1 つの貨物用に保つには、「在庫」セクションでその貨物の種類を固定する。
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) は駅ごとに、届く範囲の倉庫とその在庫を一覧にする。[Platform Details](https://mod.io/g/transportfever3/m/platform-details) は積み下ろした貨物の行き先を表示する。

```check
official: "Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types." Specialised warehouses "freeze the cargo item's delivery timer" and "enable faster loading / unloading speeds". "In specialized warehouses, only one cargo type can be stored at a time for a given module." ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: 汎用モジュールは係数 ×1 の共有在庫を 1 つつくる。専門モジュールはそれぞれ ×2 で 1 種類の貨物を入れる 500 の独自在庫を持つ。専門モジュールはコストが 2 倍（30万、維持費 5万）で、汚染も 2 倍（50）。タイマーの停止はスクリプトにはない。
result: refines
```
