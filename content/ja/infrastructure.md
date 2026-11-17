---
title: 道路、線路、橋、信号
summary: 線路と道路の種類ごとの速度、価格、維持費、橋、トンネル、踏切、信号のコストとできること、並木と防音壁が実際に何を変えるか、そしてデポの説明がどこにあるか。
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40425
fact: 100 / 160 / 350 km/h | シンプルな線路、標準線路、高速線路
fact: ×9 | シンプルな線路と比べた高速線路の価格と維持費
fact: +30 % | 線路に架線を付けるときの価格
fact: -65 % | 防音壁を付けた道路や線路の騒音
---

道路と線路の種類にはそれぞれ最高速度、1 m あたりの価格、1 m・1 年あたりの維持費があり、すべてファイルに書かれている。橋、踏切、一部の道路の装飾は独自の速度制限を加える。以下のコストは **インフラコスト** と **インフラ維持費** が 100 % のときの値である（[コスト、維持費、融資](costs.html) を参照）。

## 線路

| 線路 | 登場年 | 最高速度 | 1 km あたりの建設費 | 1 km・1 年あたりの維持費 | ソース |
|---|---|---|---|---|---|
| シンプルな線路 | 開始時 | 100 km/h | 6万 | 1万 | `simple.street_template.lua:9`、`simple.street_template.lua:28`、`simple.street_template.lua:33` |
| 標準線路 | 1930 | 160 km/h | 18万 | 3万 | `standard.street_template.lua:4`、`standard.street_template.lua:11`、`standard.street_template.lua:30`、`standard.street_template.lua:35` |
| 高速線路 | 1980 | 350 km/h | 54万 | 9万 | `high_speed.street_template.lua:4`、`high_speed.street_template.lua:11`、`high_speed.street_template.lua:30`、`high_speed.street_template.lua:35` |

- **架線** は線路より **30 %** 高い（`mod.script.tl:24-25`）。シンプルな線路では 1921 年から、より新しい種類では登場時から使える（`simple_catenary.street_template.lua:4`）。ファイル上は年ごとの追加費用はなく、電化版の維持費は同じである（`simple_catenary.street_template.lua:34`）。
- 3 種類とも勾配とカーブの条件は同じ：建設時は **8.5 %**（**勾配** スライダーの上限）、線路の形状としては最大 13 %、カーブ半径は建設時 55 m、最小 40 m（`standard.street_template.lua:36-37`、`standard.street_template.lua:48-49`、`construction_react_util.tl:241-242`、`construction_react_util.tl:1821`）。
- 線路そのものの汚染は種類とともに増える：2、4、6（`simple.street_template.lua:18`、`standard.street_template.lua:20`、`high_speed.street_template.lua:20`）。

```engine
カーブが列車の速度をどれだけ下げるか（各線路の speedCoeffs）と、建設ツールがカーブに表示する速度は、エンジンが計算する。
```

```tip scripts
高速線路は建設も毎年の維持もシンプルな線路の 9 倍かかる。列車が本当に 160 km/h より速く走る区間だけに敷こう。それ以外は標準線路で足り、遅い貨物支線ならシンプルな線路でよい。
```

## 道路

| 道路 | 年 | 最高速度 | 1 km あたりの建設費 | 1 km・1 年あたりの維持費 | ソース |
|---|---|---|---|---|---|
| 街道（狭）（旧） | 1940 年まで | 20 km/h | 3.6万 | 6,000 | `town_old_xsmall.street_template.lua:4-5`、`town_old_xsmall.street_template.lua:8`、`town_old_xsmall.street_template.lua:27`、`town_old_xsmall.street_template.lua:56` |
| 街道（小）（旧） | 1940 年まで | 40 km/h | 6万 | 1万 | `town_old_small.street_template.lua:8`、`town_old_small.street_template.lua:27`、`town_old_small.street_template.lua:56` |
| 街道（大）（旧） | 1940 年まで | 60 km/h | 18万 | 3万 | `town_old_large.street_template.lua:8`、`town_old_large.street_template.lua:27`、`town_old_large.street_template.lua:88` |
| 街道（狭）（新） | 1940 年から | 30 km/h | 12万 | 2万 | `town_new_xsmall.street_template.lua:4`、`town_new_xsmall.street_template.lua:11`、`town_new_xsmall.street_template.lua:30`、`town_new_xsmall.street_template.lua:59` |
| 街道（小）（新） | 1940 年から | 50 km/h | 18万 | 3万 | `town_new_small.street_template.lua:11`、`town_new_small.street_template.lua:30`、`town_new_small.street_template.lua:59` |
| 街道（中）（新） | 1940 年から | 50 km/h | 36万 | 6万 | `town_new_medium.street_template.lua:11`、`town_new_medium.street_template.lua:30`、`town_new_medium.street_template.lua:75` |
| 街道（大）（新） | 1940 年から | 60 km/h | 54万 | 9万 | `town_new_large.street_template.lua:11`、`town_new_large.street_template.lua:30`、`town_new_large.street_template.lua:91` |
| 田舎道（小）（旧） | 1940 年まで | 60 km/h | 6万 | 1万 | `country_old_small.street_template.lua:8`、`country_old_small.street_template.lua:29`、`country_old_small.street_template.lua:58` |
| 田舎道（小）（新） | 1940 年から | 80 km/h | 18万 | 3万 | `country_new_small.street_template.lua:10`、`country_new_small.street_template.lua:31`、`country_new_small.street_template.lua:60` |
| 1車線高速道路 | 1940 年から | 100 km/h | 18万 | 3万 | `highway_new_small.street_template.lua:10`、`highway_new_small.street_template.lua:32`、`highway_new_small.street_template.lua:53` |
| 2車線高速道路 | 1940 年から | 120 km/h | 36万 | 6万 | `highway_new_medium.street_template.lua:10`、`highway_new_medium.street_template.lua:32`、`highway_new_medium.street_template.lua:61` |
| 3車線高速道路 | 1940 年から | 120 km/h | 54万 | 9万 | `highway_new_large.street_template.lua:10`、`highway_new_large.street_template.lua:32`、`highway_new_large.street_template.lua:69` |
| トラム線路（旧） | 1910 年まで | 40 km/h | 3.6万 | 6,000 | `tram_old.street_template.lua:4-5`、`tram_old.street_template.lua:8`、`tram_old.street_template.lua:27`、`tram_old.street_template.lua:40` |
| トラム線路（新） | 1925 年から | 100 km/h | 12万 | 2万 | `tram_new.street_template.lua:4`、`tram_new.street_template.lua:9`、`tram_new.street_template.lua:29`、`tram_new.street_template.lua:42` |

- **1940 年の切り替え** で町の道路は 10 km/h 速くなるが、建設も毎年の維持も **3 倍** 高くなる。小さな道路は 1 km あたり 6万 から 18万 になる。
- 田舎道の中・大の種類は、同じ速度で小の 2 倍と 3 倍かかる（`country_new_large.street_template.lua:10`、`country_new_large.street_template.lua:31`）。
- 道路への追加：**バスレーン** は道路の価格の +10 %、**トラムの線路** は +20 %、**電化されたトラムの線路** は +40 %（`mod.script.tl:24-28`）。
- プレイヤーは通常、自分で建てた道路であっても道路を所有しない。道路ツールで道路の所有者を変えられる（公式 wiki）。道路の維持費を誰が払うかはエンジンが決める。

## 並木と防音壁

| ツール | 騒音 | 汚染 | 最高速度 | 場所 | ソース |
|---|---|---|---|---|---|
| アレイ工具（木） | -10 % | -50 % | **-25 %** | 歩道のある道路。橋の上やトンネル内は不可 | `alley.edge.lua:39-40`、`alley.edge.lua:53-56` |
| 防音ツール | -65 % | 変化なし | 変化なし | 道路と線路。トンネル内は不可 | `barrier_b.edge.lua:43`、`barrier_b.edge.lua:47`、`barrier_track_b.edge.lua:43` |

- どちらもファイル上は 100 と年 10 で、道路の 1 m あたりと同じ扱いである（`alley.edge.lua:8`、`alley.edge.lua:12`、`barrier_b.edge.lua:7`、`barrier_b.edge.lua:11`）。
- 建設メニューの「並木付き」「防音壁付き」の道路は、これらの装飾が最初から付いた同じ道路である（`town_new_medium_trees.street_template.lua:12-14`）。建設メニューはその効果を合算する（`construction_react_util.tl:2116-2139`）。
- そのため並木付きの道路は **4 分の 1 遅い**。並木付きの新しい街道（中）は 50 km/h ではなく約 38 km/h になる。

```tip scripts
騒音対策には防音壁を使おう：-65 % で速度も落ちない。木は汚染対策の道具（-50 %）だが、道路を 4 分の 1 遅くする。
```

町が騒音と汚染をどう評価するか：[汚染と騒音](emission.html)。

## 橋とトンネル

| 橋 | 年 | 最高速度 | 対象 | 基本価格 | ソース |
|---|---|---|---|---|---|
| 石橋 | 開始時から | 90 km/h | 線路、道路 | 200 | `stone.bridge.lua:169-170`、`stone.bridge.lua:181-183`、`stone.bridge.lua:193` |
| トレッスル橋 | 1970 年まで | 60 km/h | 線路用と道路用で別の種類 | 100 | `trestle.bridge.lua:200-201`、`trestle.bridge.lua:212-214`、`trestle.bridge.lua:226`、`trestle_s.bridge.lua:212` |
| 鉄橋 | 1940 年から | 140 km/h | 線路、道路 | 200 | `steel.bridge.lua:243`、`steel.bridge.lua:259`、`steel.bridge.lua:269` |
| つり橋 | 1940 年から | 180 km/h | 線路、道路 | 600 | `suspension.bridge.lua:277`、`suspension.bridge.lua:294`、`suspension.bridge.lua:304` |
| コンクリート橋 | 1970 年から | 280 km/h | 線路、道路 | 200 | `concrete.bridge.lua:162`、`concrete.bridge.lua:176`、`concrete.bridge.lua:187` |
| 斜張橋 | 2000 年から | 220 km/h | 線路、道路 | 750 | `cable.bridge.lua:214`、`cable.bridge.lua:231`、`cable.bridge.lua:240` |
| 結合アーチ橋 | 2010 年から | 350 km/h | 線路、道路 | 650 | `tarch.bridge.lua:253`、`tarch.bridge.lua:270`、`tarch.bridge.lua:280` |

- 橋の制限は線路の制限に **重ねて** かかる。鉄橋を渡る高速線はそこでは 140 km/h で走る。1970 年より前は 180 km/h を超える橋がなく、2010 年より前は 350 km/h を出せる橋がない。
- **トンネル**（岩のトンネル、1970 年からはコンクリートのトンネル）にはファイル上 **速度制限がなく**、基本価格はどちらも 600 である（`tunnel_a.tunnel.lua:187-188`、`tunnel_a_car.tunnel.lua:185`、`tunnel_b.tunnel.lua:191-194`）。
- 橋とトンネルの価格はインフラコストに従う（`post_run_util.tl:50-51`）。

```engine
橋やトンネルの基本価格は、高さや深さ（costFactors）を使ってエンジンが 1 m あたりの価格に変える。公式 wiki によると、価格は長さと地面からの高さ、または地下の深さで決まる。そのため同じ基本価格でも請求額は大きく変わりうる。トンネルは町の評判を下げる（[評判](reputation.html) を参照）。
```

```tip scripts
1970 年より前に谷を越える高速線を通すなら、140 km/h より速い橋はつり橋（180 km/h）だけである。トンネルには制限がまったくない。
```

## 踏切と信号

| 種類 | 年 | 線路の最高速度 | 価格 | ソース |
|---|---|---|---|---|
| シンプルな踏切 | 1850 - 1925 | 120 km/h | 4,000 | `era_a_eu.rcr.lua:14-17`、`era_a_eu.rcr.lua:26` |
| 半防壁付き踏切 | 1925 - 1975 | 160 km/h | 1.6万 | `era_b_eu.rcr.lua:15-18`、`era_b_eu.rcr.lua:27` |
| 近代化半防壁付き踏切 | 1975 年から | 160 km/h | 1.6万 | `era_c_eu.rcr.lua:15-17`、`era_c_eu.rcr.lua:26` |
| 経路信号（1950 年まで腕木式、1950 年から灯火式） | すべて | - | 9,000、維持費 年 1,500 | `signal_path_a.con.lua:4-5`、`signal_path_a.con.lua:10-11`、`signal_path_c.con.lua:4-5` |

- 踏切は線路を最大 160 km/h に制限する。高速線は道路を橋かトンネルで越える必要がある。
- どの信号も **一方通行** に設定できる（`signal_path_a.con.lua:51-52`）。信号が線路をどうブロックに分けるかは、公式 wiki の鉄道信号のページで説明されている。

## デポと整備施設

デポと整備施設のコスト、扱える車両の数と範囲：[路線と車両](vehicles.html) と [コスト、維持費、融資](costs.html)。

## 知っておくと良いこと

- 1940 年より前は町の道路の改良が安い。1940 年以降は新設や建て直しの町の道路が 3 倍の価格、3 倍の維持費になる。
- 高速線では橋と踏切をすべて確認しよう：最も遅いものがそこでの速度を決める。
- 速度は運行回数が増えるときだけ元が取れる（[なぜお金が減るのか？](money.html) を参照）。

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: 線路、道路、橋の速度は公式の表と同じ。ファイルでは橋の制限は道路にもかかり、トンネルには制限がなく、踏切は線路を 120 または 160 km/h に制限し、木は道路を 25 % 遅くして汚染を 50 % 減らすが騒音は 10 % しか減らさない。一方、防音壁は速度を落とさずに騒音を 65 % 減らす。
result: refines
```
