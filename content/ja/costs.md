---
title: コスト、維持費、融資
summary: コスト設定で何が変わるか、どのコストが暦年とともに増えるか、車両の価格がどう計算されるか、そして融資が実際にいくらかかるか。
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: ×6 | 2020 年までに貨物倉庫、港、空港の維持費にかかる年係数
fact: 6 年 | 分のランニングコスト：これが車両の価格
fact: 1 回 | 融資の利率は毎年ではなく、金額に 1 回だけかかる
fact: 4 | 同時に組める融資の数
---

**インフレ** 設定はどのコストも上げない。会社ランクが上がるにつれて収入を下げるだけである（[貨物収入と配送時間](income.html) を参照）。コストはその代わりに**暦年**とともに増え、4 つのスライダーが最初からその倍率を決める。

```diagram cost_years
```

## コスト設定

| 設定 | 値 | プリセット イージー · ノーマル · ハード · ベリーハード | ソース |
|---|---|---|---|
| **車両コスト**、**車両整備** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:39`、`difficulty_util.tl:98-99`、`difficulty_util.tl:125-126` |
| **インフラコスト**、**インフラ維持費** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:100-101`、`difficulty_util.tl:153-156`、`difficulty_util.tl:180-183` |
| **車両整備エフェクト** | なし ×0 · 低い ×0.5 · 普通 ×1 · 高い ×1.5 · とても高い ×2 | 低い · 普通 · 高い · とても高い | `difficulty_util.tl:42`、`difficulty_util.tl:103`、`difficulty_util.tl:185` |
| **インフレ** | 収入のみ。[貨物収入と配送時間](income.html) を参照 | 低い · 普通 · 高い · とても高い | `difficulty_util.tl:50`、`mod.script.tl:694-697` |

- **インフラコスト** は道路、線路、橋、トンネル、踏切、建物、モジュールの価格と、地形の造成にかかる費用を変える（`post_run_util.tl:23-52`、`post_run_util.tl:83-120`、`construction.script.tl:31-35`、`mod.script.tl:223-226`）。**インフラ維持費** はそれらの維持費を変える（`post_run_util.tl:43-45`、`post_run_util.tl:105-112`、`entity_window_util.tl:186`）。
- **車両コスト** と **車両整備** は、すべての車両の購入価格とランニングコストを変える（`post_run_util.tl:54-81`）。
- **車両整備エフェクト** は、状態の悪い車両がどれだけ速度、出力、快適性を失い、騒音、汚染、ランニングコストが増えるかを決める（`mod.script.tl:241-245`）。

## 暦年とともに増えるもの

- **建物の維持費**：1900 年は ×1、1920 年は ×1.5、1940 年は ×2.2、1960 年は ×3.2、1980 年は ×4、2000 年は ×5、2020 年は ×6（`mod.script.tl:92-100`）。建物ウィンドウと建設メニューは、年に従うと指定されたすべての建物にこれを適用する。建設メニューがこの指定をするのは貨物倉庫、飛行場、空港、港である（`entity_window_util.tl:186-193`、`construction_react_util.tl:1149`、`warehouse.tl:7`、`harbor_modular.tl:24`）。
- そうした建物に追加した**モジュール**は、価格は建物を建てた年、維持費は現在の年で決まる（`construction.tl:3720-3727`、`construction.tl:4364-4367`）。
- **時代ごとの種類**：デポ、整備施設、貨物倉庫、駅、港、空港には時代ごとに 1 つの種類があり、後の種類は最初の種類の **×3**（時代 B）または **×9**（時代 C）のコストがかかる（`rail_depot.con.lua:7`、`warehouse.tl:48`、`modular_station.con.lua:71`、`harbor_modular.tl:76`、`airport.tl:8`）。
- **助成金の資金**：1900 年の ×1 から 2000 年以降の ×4 まで（`finances_util.tl:87-90`）。**融資の金額**：1900 年の ×0.4 から 2020 年の ×2.4 まで（`loan_util.tl:7-10`）。
- **収入**には年係数がまったくない（`cargo_income.script.lua:10-13`）。

```engine
実際に請求される維持費と、道路、線路、車両も年の表に従うかどうかはエンジンが決める（getCostMultiplierForYear。基本設定は chargeMaintenanceInterval = 60 を指定するだけ、`mod.script.tl:105`）。スクリプトは上の表を使って、ウィンドウと建設メニューに表示する値を計算するだけである。他の建物に「年に従う」フラグを付けるスクリプトはない。
```

## 線路、道路、建物

道路と線路のファイルには、1 m あたりの価格と年間の維持費が書かれている。建設メニューは 1 km あたりで表示する（`construction_react_util.tl:2463`、`construction_react_util.tl:2477-2485`）。ほとんどの種類で、維持費は建設価格の **6 分の 1** である。

| 種類 | 登場年 | 1 km あたりの建設費 | 1 km・1 年あたりの維持費 | ソース |
|---|---|---|---|---|
| 簡易線路 | 開始時 | 6万 | 1万 | `simple.street_template.lua:9`、`simple.street_template.lua:33` |
| 標準線路 | 1930 | 18万 | 3万 | `standard.street_template.lua:11`、`standard.street_template.lua:35` |
| 高速線路 | 1980 | 54万 | 9万 | `high_speed.street_template.lua:11`、`high_speed.street_template.lua:35` |
| 古い小さな田舎道 | 開始時 | 6万 | 1万 | `country_old_small.street_template.lua:8`、`country_old_small.street_template.lua:58` |
| 新しい大きな町の通り | 1940 | 54万 | 9万 | `town_new_large.street_template.lua:11`、`town_new_large.street_template.lua:91` |

- 懸垂線は線路の価格の **30 %** を加える。バスレーンは道路の価格の 10 %、路面電車の線路は 20 %、電化された路面電車の線路は 40 % を加える（`mod.script.tl:24-28`）。
- 地形を盛るのは 1 m³ あたり 4.5、削るのは 1 m³ あたり 5.25、畑を取り除くのは 20万 かかる（`mod.script.tl:20-22`、`mod.script.tl:33`）。
- 維持費を指定していない建物は、毎年**価格の 6 分の 1** を払う（`construction.script.tl:25-27`）。
- 基本設定は撤去の払い戻し係数を 0.75、払い戻し時間を 60 にしている（`mod.script.tl:30-31`）。建てたばかりのものを取り壊すと、ほとんどのお金が戻る。これを適用するのはエンジンである。

ファイルに書かれた年間の維持費。最初の種類（1940 年より前）と後の種類。貨物倉庫にはさらに上の年係数がかかる。

| 建物 | 最初の種類 | ×3（1940 年から） | ×9（1980 年から） | ソース |
|---|---|---|---|---|
| 鉄道デポ、船舶デポ | 10万 | 30万 | 90万 | `rail_depot.con.lua:34`、`water_depot.con.lua:32` |
| 道路デポ | 3万 | 9万 | 27万 | `road_depot.con.lua:32` |
| 路面電車デポ | 2万 | 6万 | 18万 | `tram_depot.con.lua:34` |
| 鉄道または船舶の整備施設 | 4万 | 12万 | 36万 | `rail_maint_station.con.lua:32`、`water_maint_station.con.lua:32` |
| 道路の整備施設 | 1万 | 3万 | 9万 | `road_maint_station.con.lua:32` |
| 汎用の貨物倉庫 | 2.5万 | 7.5万 | 22.5万 | `warehouse.tl:48-52`、`warehouse.tl:75` |
| 専門の貨物倉庫 | 5万 | 15万 | 45万 | `warehouse.tl:51`、`warehouse.tl:75` |

これらの建物の建設費は、どれも維持費の **6 倍** である（`rail_depot.con.lua:35`、`warehouse.tl:76`）。最後の時代の専門の貨物倉庫なら、年係数の前で 270万 になる。

- 最初の**飛行場**（1950 年まで）は、すでに 2 番目の時代の ×3 を使う。判定が種類の開始年ではなく終了年を読んでいるためである（`airfield.tl:8`、`airfield_era_a.metacon.tl:3`）。

## 車両

基本ゲームの車両には固定の価格がない。ゲームはモデルを読み込むときに、車両の速度と容量から価格を計算する（`model_metadata_util.lua:488-552`）。

1. **年間のランニングコスト** = 約 675 × 平均速度（m/s）× 容量 ÷ 4（`model_metadata_util.lua:499-518`）。675 は 1 km あたりの平均収入から来ていて、空の帰り便、購入費、運賃の下落の分を残すために減らしてある（`model_metadata_util.lua:500-508`）。
2. **平均速度**は最高速度より低い。道路車両は（最高速度 km/h）^0.78 + 4、列車は ^0.86 + 10、船舶は最高速度の 65 % である（`model_metadata_util.lua:448-474`）。
3. **列車**：貨車は容量の半分で数える。機関車は出力 ÷ 最高速度（km/h）× 12.5 も容量として数え、これも半分にする（`model_metadata_util.lua:511-512`、`model_metadata_util.lua:526-540`）。強力で遅い機関車は高い。
4. **価格** = 年間のランニングコストの **6 倍**（`model_metadata_util.lua:548-549`）。

100 % での例：48 人乗りで 35 km/h のバスは、ランニングコストが年に約 4.5万、価格が約 27万 になる。

- 車両の状態は 5 段階で表される（100–80 %、その後は 20 % ごと）（`vehicle_store_util.tl:231-234`）。**20 %** になるとゲームが警告し、30 % を超えるまで続く（`notifications.script.tl:310-318`）。

```engine
車両の状態がどれだけ速く下がるか、それによってランニングコストがどれだけ上がるか、車両の価格が年で変わるかどうかはエンジンの値である（getMaintenanceRunningCostPenalty とその他のペナルティ）。スクリプトはそれらに車両整備エフェクトの倍率を掛けるだけである。
```

## 融資

```diagram loan_interest
```

| 種類 | 1960 年ごろの金額（1900 年は ×0.4、2020 年は ×2.4） | 期間 | 利率 | ソース |
|---|---|---|---|---|
| 小さい | 500万–1000万 | 1–5 年 | 3–5 % | `loan_util.tl:12-22` |
| 普通 | 1500万–2500万 | 3–8 年 | 5–8 % | `loan_util.tl:24-34` |
| 大きい | 3000万–5000万 | 5–12 年 | 8–10 % | `loan_util.tl:36-46` |
| 特大 | 4000万–6000万 | 10–24 年 | 10–12 % | `loan_util.tl:48-58` |

- カードには **年利率** と書かれているが、利率は金額に **1 回だけ** かかる。利息の合計は期間に関係なく金額 × 利率である。元金と一緒に毎月均等に支払う（`loan_util.tl:102-111`、`loan_util.tl:126-136`、`loan.script.tl:83-99`）。そのため、同じ利率なら長い融資のほうが 1 年あたりは安い。
- **返済** で払うのは元金の残りだけで、残りの利息はなくなる（`loan.script.tl:171-190`）。ボタンを押すにはその額の現金が必要である（`finances_loan_gui.tl:284-286`）。
- 利率は難易度に**よらない**。種類ごとに固定の範囲がある（`loan_util.tl:12-58`）。
- 同時に組める融資は最大 **4 件**（`loan_util.tl:4`、`loan.script.tl:134`）。提案は半年後に入れ替わる。組んだ融資の枠は 4～8 か月空いたままになる（`loan.script.tl:61-76`、`loan.script.tl:150`）。
- ゲーム開始時は 4 つの枠それぞれにランダムな種類の値が入るので、最初の「小さい」提案が大きな融資のこともある。提案が一度更新されると、各枠は自分の種類を提案する（`loan_util.tl:60-74`、`loan.script.tl:63-75`）。

## 知っておくと便利なこと

- 組める中で**いちばん長い**融資を選ぶとよい。利息の合計は同じで、より多くの月に分けられ、早めに返済すれば残りは払わなくてよい。
- 時代ごとの種類がある建物は後の時代に ×3、×9 のコストがかかり、維持費も年とともに増え続ける。最後の時代の専門の貨物倉庫は大きな固定費になる。
- 速くて容量の大きい車両はランニングコストが高いが、運ぶ量も多い。価格とランニングコストは、稼げる収入と同じく速度 × 容量に従う。

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: 融資の利率は種類だけで決まり（3–12 %）、難易度にはよらない。金額に 1 回だけかかり、期間の各月に分けて払う。早めに返済すると残りの利息はなくなる。インフレは収入だけを変える。建物の維持費は年に従う（×1～×6）。車両の価格 = 年間のランニングコストの 6 倍で、どちらも速度と容量から決まる。
result: differs
```
