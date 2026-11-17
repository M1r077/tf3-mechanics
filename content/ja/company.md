---
title: 会社のランク、特典と本社
summary: 会社のランクを上げるもの、各ランクで解放されるもの、許可と資源調査の仕組み、本社が実際に与えるもの、そしてランクが上がると何を失うのか。
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40425
fact: 15 | 会社のランク、ジュニアからタイクーンまで
fact: ×12.5 | ランク 15 に必要な世界人口（開始時との比較）
fact: ×0.75 | インフレ「普通」でのランク 15 の収入
fact: 0 | 人口が減っても失うランク
---

会社のランクはお金や配達からは決まらない。**マップ全体の人口**から決まる。新しいランクごとに特典（ランドマーク、資源調査、マーケティングキャンペーン、産業の緑化、本社のモジュール）が解放され、設定**インフレ**があると、すべての収入も少しずつ下がる。

## ランクを上げるもの

- ゲームは**開始時の世界人口**、つまりすべての町の住民数を記憶する（`company.script.tl:392-396`、`company_util.tl:365-371`）。
- そして、これまでに達した**最大**の世界人口をその開始値と比べる（`company_growth.script.tl:25-27`）。この値は上がるだけなので、町が縮んでもランクを失うことはない。
- ランク 1 は開始値で、ランク 15 はその約 **12.5 倍**で到達する（`company_progression_util.tl:6-14`、`company_progression_util.tl:95-120`、`town_growth_function.tl:13-20`）。
- キャンペーンのミッションとマップエディターにはランクがない（`company_growth.script.tl:74-79`）。

| ランク | 役職 | 世界人口（開始時との比較） |
|---|---|---|
| 1 | ジュニア | ×1 |
| 2 | メカニック | ×1.02 |
| 3 | エンジニア | ×1.08 |
| 4 | コーディネーター | ×1.2 |
| 5 | エキスパート | ×1.4 |
| 6 | チームリーダー | ×1.7 |
| 7 | スーパーバイザー | ×2.1 |
| 8 | マネージャー | ×2.6 |
| 9 | ディレクター | ×3.3 |
| 10 | シニアディレクター | ×4.2 |
| 11 | CEO | ×5.3 |
| 12 | チェアパーソン | ×6.7 |
| 13 | バイスプレジデント | ×8.3 |
| 14 | プレジデント | ×10.2 |
| 15 | タイクーン | ×12.5 |

比率は開始人口 50,000 以上の場合についてスクリプトから計算した（`company_progression_util.tl:6-14`、`company_static_util.tl:6-24`）。小さなマップでは中間のランクで少し高くなる（住民 5,000 ではランク 8 に ×2.85 が必要）。ランク 1 と 15 は ×1 と ×12.5 のままである。

- つまりランクは**町の成長**に従う。町はあなたの旅客と貨物で成長する。[町の成長](towns.html)を参照。
- 最初のランクはすぐに来るが、最後のランクにはマップの町が何倍も大きくなる必要がある。

## 新しいランクは会社ウィンドウで適用される

人口がしきい値を超えると**ランクアップ通知**が出る。クリックすると、そのランクで会社ウィンドウが開く（`company_growth.script.tl:96-107`、`company_notification_rank_up.script.tl:8-9`）。

- 新しい特典は、そのランクが**会社ウィンドウで選択された**ときにだけ解放される。そのときウィンドウが解放を送る（`company.tl:420-423`、`company_growth.script.tl:55-62`）。建設メニューはこの適用済みのランクを確認する（`company_util.tl:92`、`company_util.tl:171-178`）。
- 次の節の収入係数は、適用されたかどうかに関係なく、**到達した**ランクに従う（`company_growth.script.tl:47-48`）。

```tip scripts
ランクアップしたら通知をクリックする（または会社ウィンドウを開いて新しいランクを選択する）と特典が手に入る。待っても何も得られない。収入はもう下がっている。
```

## ランクが上がると失うもの：設定「インフレ」

**インフレ**があると、貨物と旅客のすべての収入が、ランク 1 の ×1 からランク 15 の最小値まで均等に下がる（`company_progression_util.tl:25-40`、`company_growth.script.tl:159-170`）。

| インフレ | ランク 15 の収入 | ソース |
|---|---|---|
| なし | ×1（変化なし） | `difficulty_util.tl:50`、`mod.script.tl:694-697` |
| 低い | ×0.9 | |
| 普通 | ×0.75 | |
| 高い | ×0.6 | |
| とても高い | ×0.5 | |

- 「普通」では、ランクごとに収入の約 1.8 % を失う。ランク 3 で ×0.96、ランク 8 で ×0.875、ランク 15 で ×0.75。
- インフレはどのコストも上げない。コストは暦の年に従う（[コスト、維持費とローン](costs.html)を参照）。
- ランクが高いと、新しい助成金の提案も少なくなる（[助成金](subsidies.html)を参照）。

## 許可

ほとんどの特典は**許可**で制限される。ランクが特典の許可を与え、建物 1 つまたは使用 1 回ごとに 1 つ使う（`company_util.tl:33-80`、`company_util.tl:206`）。

- 許可はランクを通じて**加算される**。ランク 3 で 1、ランク 5 で 1 を与える特典は、ランク 5 から 2 つ使える（`company_util.tl:51-56`）。
- 建物は解体すると許可を返す。ゲームは立っているものを数える（`company_util.tl:143-163`、`company_util.tl:203-206`）。
- 資源調査、マーケティングキャンペーン、緑化は開始時に許可を使い切る（`company.script.tl:416-423`、`company.script.tl:459-462`、`company.script.tl:496-500`）。そのあと建設メニューには**使用済**または**クールダウン**が表示される（`company_util.tl:207-226`）。
- **マーケティング**の許可は、各キャンペーンの **5 年**後に戻る（`marketing.res.lua:6-7`、`company.script.tl:66-94`）。

| 特典 | 許可 | ソース |
|---|---|---|
| 本社 | ランク 1 で 1 | `hq.res.lua:6` |
| マーケティングキャンペーン | ランク 4 で 1、5 年後に戻る | `marketing.res.lua:6-7` |
| 産業の緑化 | ランク 3、6、9、12、15 で 1 | `industry_greenify_tool.script.tl:101-102` |
| 清掃工場 | ランク 10 で 15 | `pollution_cleanup_facility.con.lua:106-108` |
| ランドマーク | 各 1 つ：アンフィテアトルム 2、大灯台 5、白鷺城 7、海事博物館 9、ノイシュヴァンシュタイン城 10、自由の女神像 11、頤和園 13、オペラハウス 14、国会議事堂 15 | `arena.con.lua:39`、`lighthouse.con.lua:48`、`white_heron_castle.con.lua:47`、`ship_museum.con.lua:55`、`neuschwanstein.con.lua:55`、`statue_of_liberty.con.lua:57`、`summer_palace.con.lua:63`、`opera_house.con.lua:63`、`westminster.con.lua:79` |

各特典の効果：[町の評判](reputation.html)（マーケティングキャンペーン）、[汚染と騒音](emission.html)（緑化、清掃工場）。

## 資源調査

資源調査は町の近くで資源を探し、成功するとそこに新しい産業を設立する。

| 資源 | ランク | ソース |
|---|---|---|
| 魚 | 2 | `exploration_fish.res.lua:9-11` |
| 粘土 | 3 | `exploration_clay.res.lua:9-11` |
| 原油 | 4 | `exploration_crude_oil.res.lua:9-11` |
| 穀物、野菜 | 4、**共通の許可 1 つ**（産業） | `exploration_grain.res.lua:9`、`exploration_vegetables.res.lua:9`、`permit_key_farm.res.lua:6` |
| 木材 | 5 | `exploration_logs.res.lua:9-11` |
| 石炭、鉄鉱石 | 6 | `exploration_coal.res.lua:9-11`、`exploration_iron_ore.res.lua:9-11` |
| 石、綿 | 8 | `exploration_stone.res.lua:9-11`、`exploration_wool.res.lua:9-11` |
| 砂 | 9 | `exploration_sand.res.lua:9-11` |
| ゴム | 12 | `exploration_rubber.res.lua:9-11` |

- 各資源の許可は **1 つ**で、資源調査の開始時に使う（`company.script.tl:451-462`）。
- 期間は最長 **6 か月**。月に 1 回産業の配置を試み、確率は 6 か月で 20 % から 60 % に上がる（`company_util.tl:14-17`、`company.script.tl:299-307`、`company.script.tl:130-142`）。
- ゲームが町の近くにその産業の場所を見つけられないときも、試行は失敗する（`company.script.tl:199-210`）。
- 最後の試行が失敗すると、**許可が戻り**、通知でそう知らされる（`company.script.tl:106-126`、`company.script.tl:170-181`）。
- 町と資源の組み合わせごとに、同時に実行できる資源調査は 1 つだけ（`company.script.tl:442-447`）。

```engine
新しい産業が立てる場所（町の近くの makeIndustrySpawnProposal）はエンジンが決める。水から遠い魚の資源調査や、周りに空き地がない町では、単に失敗して許可が戻る。
```

## 本社

| 項目 | 値 | ソース |
|---|---|---|
| 価格と維持費 | 無料、維持費なし | `headquarter.script.tl:526-527` |
| 許可 | 1、ランク 1 で | `headquarter.con.lua:6-7`、`hq.res.lua:6` |
| 町の成長 | 最も近い町に +5 % | `headquarter.script.tl:510-515`、`landmark_util.tl:51-70` |
| 職場 | 24 | `headquarter.con.lua:16`、`headquarter.script.tl:505-508` |

- +5 % はその町の成長率へのボーナスなので、町の成長率が 0 % のときは何もしない（[町の成長](towns.html)を参照）。
- **モジュール**は 1 つ 50,000 で、ランクとともに増える許可で制限される（`hq_module_m.module.lua:83`、`hq_module_m.module.lua:137`）。
- ファイルでボーナスを持つモジュールは 2 つだけ：**中型建造物**の町の成長 +1 %（`hq_module_m.module.lua:139-142`）と**大型建造物**の**評判回復** +1 %（`hq_module_l.module.lua:169-172`）。回復ボーナスはどの町の評価も読まない（[町の評判](reputation.html)を参照）。他のモジュールは装飾である。
- 各モジュールのファイルは、町の成長 +5 % を与える表で始まるが、ファイル内でそれを使うものはない（`hq_corner_l.module.lua:148-159`、`hq_statue.module.lua:46-57`）。加算されるのはモジュールの `metadata` 内のボーナスだけである（`headquarter_addon.script.tl:18-29`）。

| モジュール | 許可が増えるランク（×2 = 2 つ） | ランク 15 での合計 |
|---|---|---|
| 旗（地面） | 1 ×2、6、7、8、9、11、12、13、14 | 10 |
| コーナー建造物 | 3、5、7 ×2、9、11、13、15 | 8 |
| 中型建造物 | 2、4、10 ×2、15 ×2 | 6 |
| 大型建造物 | 5、6、10、12 | 4 |
| バルコニー | 8 ×2、14 ×2 | 4 |
| 大型噴水 | 10 ×2、14 ×2 | 4 |
| ドーム | 6、15 ×2 | 3 |
| 旗（屋根） | 7、10、13 | 3 |
| テニスコート | 11、12、14 | 3 |
| 古木 | 13、15 ×2 | 3 |
| 像 | 14 ×2 | 2 |
| プール | 15 | 1 |

ソース：各モジュールファイルの `rankAndPermits` の行（`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`）。

```tip scripts
本社は最も速く成長させたい町に置き、そこに中型建造物を追加しよう。成長ボーナスを持つモジュールはこれだけである。
```

## 知っておくと便利なこと

- ランクを上げるには町を成長させよう。より多くの町へより多くの旅客と貨物を、良い評価で。銀行のお金は数えられない。
- ランドマークと資源調査を計画しよう。それぞれ決まったランクで 1 回だけである。
- インフレのあるマップでは、ランクアップは特典には良く、収入には悪い。「普通」では、ランク 15 までの道のりで全収入の 4 分の 1 を失う。

```check
official: "The company rank depends on the population of the map. . Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: ルールは同じ：これまでに達した最大の世界人口を開始時の人口と比べ、ランク 15 は ×12.5。失われることはない。新しいランクは会社ウィンドウで選択しないと特典が解放されないが、インフレはすぐに収入を下げる。ボーナスを持つモジュールは 2 つだけ（中型建造物の成長 +1 %、大型建造物の評判回復 +1 % で、これはどの評価も読まない）。他は装飾である。
result: refines
```
