---
title: 労働者と労働者ブースト
summary: 住民がどのように産業で職を得るか、どの労働者がブーストに数えられるか、ブーストの大きさはどれほどか。
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-14
fact: 10 / 20 | ブーストに必要な労働者数
fact: 2 年 | 1 回の到着が数えられる期間
fact: ×1.5–2.5 | ブースト係数（産業ごとに固定）
---

どの産業にも職場がある。十分な数の労働者が**あなたの旅客路線で到着する**と、その産業の生産量が増える。産業ウィンドウには 2 つの異なる数字が表示され、この 2 つの混同が最もよくある誤解の原因である。

```diagram workers_flow
```

## 誰が産業で働けるか

- 基本ゲームのすべての産業には **20 の職場**がある（各産業の .con.lua の `industrialCapacity = 20`）。
- 職場は、住民が**徒歩や自動車では行けない**ように設定されている。そこへ住民を運べるのはあなたの路線だけである（`industryutil.lua:451-457`、`disallowedMoveModes = {"WALK", "DRIVE"}`）。
- 住民はそれぞれ住居・買い物先・職場を持つ。ゲームはその住民が到達できる場所の中から職場を選ぶ。産業の目的地としての重みは 2.0 である（`industryutil.lua:455`）。

```engine
住民が到達できるすべての場所の中から 1 つの職場をどう選ぶか（移動時間、費用、2.0 の重み）はエンジンが計算する。スクリプトは入力値を渡すだけである。
```

## 割り当てられた労働者

職場がこの産業である住民のこと。産業ウィンドウの職場バー、および産業統計の **職場** 列（「12/20」）に表示されるのがこの数である（`entity_window_util.tl:1238`、`statistic_industries.tl:305`）。割り当てられただけの労働者は何もブーストし**ない**。実際にそこまで移動する必要がある。

## ブーストに数えられる労働者

小さなゲームスクリプト `industry_workers.script.tl` がすべての到着を監視している。

1. 住民が産業に到着し、その**最後の移動があなたの路線によるもの**だった場合、その到着がゲーム内時刻とともに記録される（`industry_workers.script.tl:86-118`）。
2. 保持されるのは**直近 2 ゲーム年**の到着だけである（`industry_productivity_util.tl:3`：`2 * getDefaultYearDuration()`）。
3. 保持されるのは最大で**最新の 20 件**の到着である（`industry_workers.script.tl:4`、`KeepHistoryCount = 20`）。
4. 同じ人が再び到着すると、新しい到着が古い記録を置き換える。各住民は **1 回**しか数えられない（`industry_workers.script.tl:56-70`）。

```diagram workers_window
```

## ブーストの開始と停止

- 数えられた労働者が**職場数の半分**に達すると、産業はブーストされる：`counted ≥ workplaces × 0.5`（`industry_productivity_util.tl:35-48`、`RequiredWorkersFractionForBoost = 0.5`）。職場が 20 なら **10 人**である。
- 産業ウィンドウのブースター欄が示すのはまさにこれで、「数えられた人数 / 必要人数」と表示され、必要人数は切り上げられる（`industry_react_util.tl:627`）。
- 判定は、新しい到着があったとき、または最も古い到着が 2 年より古くなったときに再実行される（`industry_workers.script.tl:40-43`）。したがって、労働者が来なくなってから約 2 年でブーストは**自動的に止まる**。

## ブーストの大きさ

- 生産量には産業の**ブースト係数**が掛けられる。ウィンドウには「+X %」と表示される（`industry_react_util.tl:716`）。
- この係数は産業の乱数シードから 1 回だけ決められ、**×1.5 から ×2.5 の間**で、その産業では二度と変わらない（`industry_productivity_util.tl:58-72`）。シードのない産業は ×2 を使う。
- そのため、同じ種類の鉱山 2 つでも労働者ブーストが異なることがある。どちらに路線を引くか決める前に「+X %」を確認するとよい。

## 例

職場が 20 で「+84 %」の炭鉱。

| 状況 | 数えられた人数 | ブースト？ | 生産量 |
|---|---|---|---|
| 新しいバス路線：14 人の住民が割り当て済み、まだ誰も到着していない | 0 | なし | ×1 |
| 今年 12 人の異なる住民がバスで到着した | 12 | あり（≥ 10） | ×1.84 |
| バス路線を撤去し、2 年間誰も到着しない | 0 まで減る | 停止 | ×1 |

## 知っておくと便利なこと

- 保持される到着が最大 20 件で、50 % の規則があるため、**職場が 40 を超える**産業（MOD なら可能）は、労働者によるブーストを決して受けられない。
- 助成金「労働者の移送」は、このブーストが有効になった時点で達成となる（公式wiki、助成金）。
- ブースター貨物（肥料、機械、道具）は原料産業の**別の**ブーストであり、このページでは扱わない。
- [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) MOD は、割り当てられた労働者とブーストに数えられた労働者がどの町から来ているかを産業ウィンドウに表示し、地図上に矢印で示す。

```check
official: "If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: 「Sufficient」（十分な数）= 職場数の半分（20 のうち 10）。「recently」（最近）= 直近 2 ゲーム年、最新 20 件の到着、1 人 1 回、あなたの路線によるもののみ。ブースト係数は産業ごとに ×1.5 から ×2.5。
result: refines
```
