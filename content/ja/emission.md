---
title: 汚染と騒音
summary: 何が騒音と汚染を出すか、建物がいつ多く出すか、町がそれをどう評価するか、そして産業の緑化と清掃工場が実際に何をするか。
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
game: 40444
fact: 65–80 dB | 町の騒音：65 で満点、80 でゼロ
fact: 60–74 | 町の汚染（スクリプトの対数スケールで、音の大きさではない）：60 で満点、74 でゼロ
fact: −80 % | 緑化した産業の騒音と汚染
fact: 700 m | 清掃工場の届く範囲
---

車両、線路、道路、駅、車庫、倉庫、産業はすべて**騒音**と**公害**を出す。町の 2 つの評価、**騒音**と**公害**は、町に届く量を固定の上限と比べる。悪い評価は町の権限の評価を下げ、成長も下げる（[町](towns.html) を参照）。

## 建物がより多く出すとき

ゲームスクリプトは数回の更新ごとに、4 種類の建物の排出を静かなレベルと忙しいレベルの間で設定する（`emissions.script.tl:12-18`）。

| 建物 | 多く出すとき | ソース |
|---|---|---|
| **産業** | 生産しているとき、そしてブースト（貨物または労働者）ごとにさらに。すべての出力在庫が同時に満杯だとレベルが半分になる（生産中 → 停止中、ブースト 2 回 → 生産中） | `emissions.script.tl:152-194` |
| **駅** | 忙しいほど。待っている人と貨物を容量と比べる | `emissions.script.tl:211-222` |
| **車庫**、**整備所** | その整備を使う車両が多いほど | `emissions.script.tl:223-234` |
| **倉庫** | 在庫が多いほど | `emissions.script.tl:237-250` |

- 産業はそれぞれ独自の 4 段階（停止中、生産中、ブースト 1 回、ブースト 2 回）を持つ（`industryutil.lua:464-475`。既定値 0 / 78 / 84 / 88 は独自の値を持たない産業にだけ使われる）。ほとんどの産業は停止中でも少し出す。炭鉱は汚染 2 → 10 → 20 → 30、その畑は 2 → 30 → 60 → 90（`coal_mine.con.lua:99-135`、[産業](industries.html) を参照）。
- 出力在庫がすべて満杯の産業はレベルが半分になる（`emissions.script.tl:172-182`）。つまり、輸送するとその汚染は増える。
- 車両と線路も排出する。**車両整備エフェクト**の設定では、状態の悪い車両はより多く出す（[コスト、維持費、融資](costs.html) を参照）。

## 建設メニューに表示されるもの

| 建物 | 騒音 | 汚染 | ソース |
|---|---|---|---|
| 港 | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| 空港 | 8–56 | 80–560 | `airport.tl:28-29` |
| 鉄道駅 | 25 | 45–350 | `modular_station.con.lua:97-98` |
| 鉄道車庫 | 50 | 100 | `rail_depot.con.lua:32-33` |
| 道路・路面電車の車庫 | 40 | 80 | `road_depot.con.lua:30-31`、`tram_depot.con.lua:32-33` |
| 地下駅 | 40 | 80 | `underground_station.con.lua:75-76` |
| トラック・バス駅 | 1–10 | 12–76 | `modular_terminal.con.lua:67-68`, `modular_terminal.con.lua:121-122` |
| 整備所 | 20 | 40–50 | `road_maint_station.con.lua:30-31`、`rail_maint_station.con.lua:30-31` |
| 倉庫 | 20 | 50（汎用）または 100（専用） | `warehouses/warehouse.tl:51`, `warehouses/warehouse.tl:73-74` |

2 つの値はメニューが示す範囲で、低い値から高い値まで、隣の価格の範囲と同じである（`construction_desc_react_util.tl:733-746`）。値が 1 つなら単一の数値。稼働中は、どの建物も忙しいほど多く出す（上の表）。港、空港、大きな貨物駅は家から離すこと。

## 町がどう評価するか

| 評価 | 測るもの | 満点 | ゼロ | ソース |
|---|---|---|---|---|
| **騒音** | 町の建物での騒音 | 65 dB 以下 | 80 dB | `town_util.tl:433-443`、`emission_config.tl:10-11` |
| **公害** | 町の面積の 16 m セルあたりの平均汚染（面積は最小 5、最大 10 km² として数える）を、スクリプトの対数スケール（「dB」）に換算 | 60 以下 | 74 | `town_util.tl:413-431`、`emission_config.tl:23-30` |

- 騒音に苦しむのは**住宅**地区だけで、商業と工業の建物は苦しまない（公式wiki）。家のウィンドウはその位置の騒音を表示する（`town_building.tl:165-183`）。
- 汚染は面積全体で平均されるので、中心から遠い 1 つの発生源は、小さな町より大きな町で軽くなる。
- **騒音感度**と**汚染感度**の設定は上限をずらす。感度 2 倍は +3 dB として数える（`town_util.tl:426-428`、`town_util.tl:439-441`）。汚染は騒音と同じ対数スケール（10·log10）を使う。+3「dB」は汚染が 2 倍という意味で、音の大きさではない。

| 段階 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ソース |
|---|---|---|---|---|---|---|---|---|
| 騒音 | オフ（常に満点） | ×¼ | ×½ | ×1 | ×1.4 | ×1.8 | ×3.5 | `difficulty_util.tl:48` |
| 汚染 | オフ（常に満点） | ×¼ | ×½ | ×1 | ×1.7 | ×3 | ×5 | `difficulty_util.tl:49` |

プリセットの「易しい」「普通」「難しい」「とても難しい」は段階 3、4、5、6 を使う（`difficulty_util.tl:114-115`、`difficulty_util.tl:142-143`、`difficulty_util.tl:169-170`、`difficulty_util.tl:196-197`）。

## 産業の緑化

| | | ソース |
|---|---|---|
| 効果 | 産業の騒音と汚染 ×0.2（−80 %）、永続 | `emission_config.tl:32`、`emissions.script.tl:184-192` |
| 回数 | 会社ランク 3、6、9、12、15 で 1 回ずつ | `industry_greenify_tool.script.tl:99-104` |
| 制限 | 産業ごとに 1 回。2 回目は許可を消費しない | `company.script.tl:489-494` |

- 効果はその版の産業に結びつく。産業が建て直されると失われる（`emissions.script.tl:187-190`）。
- 最適な使い方：町のすぐ隣にある最も忙しい産業。ブーストされた産業が最も多く出すからである。

## 清掃工場

周囲の汚染を取り除く会社の特典。

| | | ソース |
|---|---|---|
| 価格 | 1億 | `pollution_cleanup_facility.script.lua:560` |
| 年間の維持費 | 1000万 | `pollution_cleanup_facility.script.lua:561` |
| 利用可能 | 会社ランク 10 で 15 個 | `pollution_cleanup_facility.con.lua:106-108` |
| 必要なもの | **機械**：1 サイクルに 8、年 2 サイクル。労働者 20 人 | `pollution_cleanup_facility.con.lua:43-60` |
| 届く範囲 | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| 状態 | 汚染 | 騒音 | ソース |
|---|---|---|---|
| 停止中（機械なし） | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| 稼働中 | −10,000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| ブースト 1 回 | −20,000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| ブースト 2 回 | −40,000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

最後のレベルにはブースター規則が必要だが、清掃工場にはない。労働者があれば −20,000 に達する（`pollution_cleanup_facility.con.lua:51-58`、`emissions.script.tl:158-166`）。

- 機械がなければほとんど何もしない。産業のように供給する必要がある。
- うるさい。住宅地区の外で、汚染された地域から 700 m 以内に建てること。
- 労働者ブースト係数は ×2 である（`pollution_cleanup_facility.script.lua:549`）。[労働者](workers.html) を参照。

## 知っておくと便利なこと

- 町のウィンドウ、または騒音と汚染のレイヤーを開くと、評価と発生地点が見える。
- 産業の出力在庫がすべて満杯だと排出レベルは半分になるが、その貨物を失う。産業を干上がらせるより町を移すほうがよい。
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) と [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) は最も忙しい駅を見つけるのに役立つ。

```engine
騒音と汚染のマップ、値の広がり方、車両と線路の排出、産業がいつ建て直されるかはエンジンが計算する。スクリプトは各建物のレベルと町の上限を設定するだけである。
```

```check
official: "Noise reflects noise levels in residential areas." "Pollution reflects pollution levels across the town area." 住宅地区は "is sensitive to noise"、商業地区は "is robust against the influence of noise"。([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: 騒音評価は 65 → 80 dB、汚染は 60 → 74 dB で 5〜10 km² で平均。感度は 10·log10 dB を加える。産業、駅、車庫、倉庫は忙しいと多く出す。出力在庫がすべて満杯だと産業の排出レベルは半分になる。緑化は産業ごとに 1 回 −80 %。清掃工場は 700 m 以内で最大 20,000 の汚染を取り除き（40,000 は定義されているがブースター規則が必要）、機械が必要。
result: refines
```
