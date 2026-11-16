---
title: ゲーム時間とカレンダー
summary: ゲーム速度とカレンダー速度は別のもの。1 日と 1 年の長さ、カレンダーを遅くしたり止めたりすると何が変わり、何が変わらないか。
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
game: 40425
fact: 4 s | カレンダー速度 ×1、ゲーム速度 1x でのカレンダーの 1 日
fact: ≈ 24 min | 同じ速度でのカレンダーの 1 年
fact: 0 ×0.25 ×0.5 ×1 ×2 ×4 | カレンダー速度の段階
fact: 0 1x 2x 4x | ゲーム速度の段階
---

ゲームには**2 つの時計**がある。**ゲーム速度**（一時停止、1x、2x、4x）はすべてを速く動かす。車両、生産、町もそうである。**カレンダー速度**は日付の進む速さだけを決める。ゲームのほぼすべてのルールは、カレンダーの日数ではなくゲーム時間で数える。

## 2 つの設定

| 設定 | 段階 | 変わるもの | ソース |
|---|---|---|---|
| **ゲーム速度** | 一時停止、1x、2x、4x | シミュレーション全体の速さ | `game_bar_widgets.tl:199-203` |
| **カレンダー速度** | 一時停止、×0.25、×0.5、×1、×2、×4 | 1 日が何秒のゲーム時間か | `game_bar_widgets.tl:321-335`、`game_bar_widgets.tl:351` |

- カレンダー速度 ×1 では、1 日はゲーム時間で **4 秒**である（公式wiki）。1x では 1 か月は約 2 分、1 年は約 **24 分**になる。[Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) で計測：×1 で 1 日 4.0 秒、×4 で 1 秒、×0.5 で 8 秒、×0.25 で 16 秒。
- ×4 では日付が 4 倍速く進む。**一時停止**では日付が止まるが、シミュレーションは続く。
- 2x と 4x は上限である。コンピューターが追いつかないと、ゲームはこれを下げる（`game.tl:636-642`）。計測では、2x は平均 1.9x、4x は平均 3.6x だった。
- **時刻**と天気は 3 つ目の、見た目だけの時計である。初期設定では、カレンダーに関係なく自動で変わる（`game_time_config.res.lua:5`、`weather_config.res.lua:5`）。

## カレンダーに関係なくゲーム時間に従うもの

これらはゲーム時間で数える。そのため、カレンダーを遅くしても止めても遅くならない。

- **生産**：産業の生産時間は標準の 1 年の決まった割合である（`industry_react_util.tl:51`）。産業ウィンドウは、それを現在のカレンダーの日数で表示する（`industry_react_util.tl:23`）。×0.25 では、同じ速さでも日数は 4 分の 1 と表示される。
- **融資の支払い**：ゲーム時間の標準の 1 か月ごとに 1 回。カレンダーが止まっていても同じである（`loan.script.tl:83-88`）。
- **補助金の期限**と ×2 の収入ボーナス（`subvention_util.tl:290-292`）。
- **町の評判の回復**（`towns.script.tl:121-130`）、**労働者ブースト**（`industry_productivity_util.tl:3`）、何年も輸送がないときの**産業の閉鎖**（`industries.script.tl:119-128`）。
- 直近半年の町の**配送評価**（`town_util.tl:840`）。
- **新しい産業**：カレンダー停止中もゲーム時間 1809 秒で 3 つ、760 秒と 728 秒の間隔で現れた。カレンダーが動いているとき（約 730 秒）と同じリズム。[Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) で計測。[産業](industries.html) を参照。

カレンダーが動いているとき、ゲームはこれらの期間を現在のカレンダー速度での年、月、日で表示する（`util.tl:40-49`）。

## カレンダーの日付に従うもの

- **新しい車両、駅、建物**は年に応じて登場する（公式wiki："Different calendar speeds only affect the availability of vehicles and infrastructure"）。
- **年とともに増えるコスト**：建物の維持費、時代ごとの種類、補助金の額、融資の額は日付に従う。詳細：[コスト、維持費、融資](costs.html)。

## カレンダーが一時停止のとき

1. 日付、つまり年は変わらない。新しい車両は出ず、年に応じたコストもそのまま。
2. 期間は日数ではなく**分と秒**で表示される（`util.tl:41-43`、`industry_react_util.tl:16-21`）。
3. 融資は支払いを年ごとではなく**分ごと**で表示する（`finances_loan_gui.tl:223-231`）。カスタム融資のカードは借りられない（`finances_loan_gui.tl:393`）。
4. 生産、支払い、期限、評判はゲーム時間のペースのまま進む。

## 知っておくと便利なこと

- 新しい車両が出る前に、路線網を育てる時間がもっとほしい？ カレンダー速度を下げよう。ゲーム時間 1 分あたりの収入は変わらない。
- 「年ごと」と表示される生産はカレンダー速度で変わる。産業は同じ速度で比べること。
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) は、カレンダーが止まっていても読みやすい財務グラフを表示する。

```engine
標準の 1 日、1 か月、1 年の長さ（getDefaultDayDuration など）はエンジンから来る。町のスクリプトは 1 か月を 30 × 4 秒と数える（`towns.script.tl:121`）。これは計測した 1 日 4 秒と合う。ほかのいくつかの定数は、まだ 1 日を 2 秒としている（`cargotype.script.lua:3`、`mod.script.tl:172`）。
```

```check
official: "By default a day in the game lasts 4 seconds." "Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent." ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: カレンダー速度は標準の 1 日に対して ×0.25 から ×4、または一時停止。生産、融資、補助金、評判、労働者のタイマーはゲーム時間で進む。カレンダーが止まると、期間は分で、支払いは分ごとで表示され、新しい融資はできない。計測：×1 で 1 日 4 秒。
result: refines
```
