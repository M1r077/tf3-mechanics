---
title: 実績
summary: フリーゲームの各実績をゲームスクリプトが何をいつ調べるか、ベースゲームの車両・貨物・動物だけを数える実績はどれか、そしてエンジンに任されている判定。
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-24
game: 40444
fact: 17 | ゲームスクリプト自身が解除する実績
fact: 500 m | 高峰の駅で、停車した列車の先頭車両の高さ
fact: < 1 % | 私のせいじゃないの条件となる町の評判
fact: 10 | 中央集権化で最寄りの町が同じでなければならないランドマーク
---

公式 wiki には 41 の実績が載っている。ゲームスクリプト (`achievements.script.tl`) はそのうち **17** を自分で解除し、**9 つのゲーム間カウンター**に値を送る。残り（キャンペーン、天候、町の規模、倉庫、利子、ブースター、自動車、1900-2000、2000 年代の蒸気）はエンジンやプラットフォームなど別の場所で判定される。どの判定も、まずその実績がまだ解除できるかをエンジンに尋ねる。MOD や設定で解除できなくなるかどうかはそちらで決まる（`achievements.script.tl:632`、`achievements.script.tl:510`）。

## スクリプトが判定する実績

| 実績 | スクリプトが調べること | ソース |
|---|---|---|
| **荷物到着** | 貨物が 1 つ目的地に届く | `achievements.script.tl:221-225`、`achievements.script.tl:632-636` |
| **代表者** | 補助を 1 件達成する | `achievements.script.tl:241-244`、`achievements.script.tl:638-642` |
| **連続補助** | 間に失敗を挟まずに補助を 10 件達成する。失敗するとカウントは 0 に戻る | `achievements.script.tl:243-249`、`achievements.script.tl:644-648` |
| **管理人** | 町の配達評価が「**秀**」に変わる | `achievements.script.tl:270-276`、`towns.script.tl:27-30`、`achievements.script.tl:650-654` |
| **都市開発** | 町のレベルが上がる | `achievements.script.tl:253-255`、`town_growth.script.tl:92` |
| **需要の高まり** | 町に新しい貨物の需要が生まれる | `achievements.script.tl:257-259`、`achievements.script.tl:668-672` |
| **私のせいじゃない** | 町の評判が**下がって** **1 %** 未満になる | `achievements.script.tl:261-267`、`towns.script.tl:33-36` |
| **昇格** | 会社のランクが上がる | `achievements.script.tl:280-282`、`achievements.script.tl:680-684` |
| **出世頭** | 会社が最高ランクに達する | `achievements.script.tl:284-290`、`achievements.script.tl:686-690` |
| **美観管理** | 1 回の建設で木だけを置く（何も撤去せず、植林によるものでもない） | `achievements.script.tl:346-377` |
| **完璧主義者** | 同じ駅を解体、再建、解体、再建の順に行い、その間に他の駅の建設や撤去がない | `achievements.script.tl:304-341`、`achievements.script.tl:694-710` |
| **中央集権化** | 完成したランドマークちょうど 10 個の最寄りの町が同じ | `achievements.script.tl:382-395`、`achievements.script.tl:713-721` |
| **高峰の駅** | あなたの列車が、先頭車両が **500 m** より高い位置で停車駅に着く | `achievements.script.tl:407-417`、`achievements.script.tl:723-727` |
| **海上活動** | あなたのヘリコプターが石油プラットフォームの停車場に着く | `achievements.script.tl:420-450`、`achievements.script.tl:729-733` |
| **遺産艦隊** | ベースゲームのすべての船舶モデルが、同時にあなたの船舶路線で運行している | `achievements.script.tl:735-776` |
| **未知との遭遇** | UFO をクリックする | `achievements.script.tl:793-806` |
| **タイムキーパー** | 時刻を手動で変える | `achievements.script.tl:839-844` |

- **完璧主義者**は駅全体を 1 つ追加または撤去する建設だけを数える。駅にホームやモジュールを追加しても数えない（`achievements.script.tl:301-302`）。
- **中央集権化**は各ランドマークを完成した時点で、その時に最も近い町の分として数える（`achievements.script.tl:386`）。
- **遺産艦隊**は、まだ一度も停車したことのない船舶モデルが停車場に着いたときにだけ判定される。見るのは船舶路線の車両で、車庫にある船は見ない（`achievements.script.tl:736`、`achievements.script.tl:750-766`）。
- **私のせいじゃない**に必要なのは他の評価ではなく評判である。[町の評判](reputation.html)を参照。

```tip scripts
高峰の駅は、駅舎の高さではなく、列車が止まったときの先頭車両の高さを調べる。500 m を超える山の上に駅を建て、列車を 1 本走らせよう。
```

## ゲーム間カウンター

これらはゲームをまたいで続く（プラットフォームが保存する）。スクリプトは前回の判定から変わった分だけを送る。

| カウンター | 実績 | 数えるもの | ソース |
|---|---|---|---|
| 線路の長さ | **世界一周** | 記録帳の総延長（km）の増加分。撤去しても差し引かれない | `achievements.script.tl:511-523` |
| 人口 | **世界人口** | ゲームを読み込んだときの人口からの、マップ人口の増加分 | `achievements.script.tl:512`、`achievements.script.tl:525-533` |
| 旅客 | **旅客パイオニア** | あなたの路線で移動を終えた旅客 | `achievements.script.tl:236-238`、`achievements.script.tl:535-541` |
| 貨物 | **貨物パイオニア** | 配達した貨物 | `achievements.script.tl:543-549` |
| 気候 | **タイクーン中のタイクーン** | 会社が最高ランクに達したときのマップの気候 | `achievements.script.tl:551-567` |
| 収入 | **汚れた金** | 収入の合計（10 億単位） | `achievements.script.tl:202-204`、`achievements.script.tl:569-590` |
| 貨物の種類 | **営業の達人** | ベースゲームの各貨物の種類を 1 回ずつ配達 | `achievements.script.tl:20-22`、`achievements.script.tl:230-232`、`achievements.script.tl:592-607` |
| 車両 | **鑑定家** | ベースゲームの各車両モデルが 1 回ずつ停車場に着く | `achievements.script.tl:16-18`、`achievements.script.tl:469-481`、`achievements.script.tl:609-625` |
| 動物 | **動物愛好家** | ベースゲームの各動物を 1 回ずつクリック | `achievements.script.tl:24-26`、`achievements.script.tl:809-834` |

- MOD の車両、貨物、動物はこれらのカウンターに決して数えられない。ベースゲームのファイル（`::/vehicle`、`::/cargos`、`::/animal`）だけが対象になる（`achievements.script.tl:16-26`）。
- 鑑定家では、車両が路線の**停車場に着く**必要がある。買うだけでは足りない。

```engine
実績がまだ解除できるか（isAchievementUnlockable）、カウンターが無効になっているか（areStatsDisabled）、各カウンターの目標値、そしてスクリプトにない 24 の実績は、エンジンとプラットフォームが扱う。公式 wiki によると、見た目だけではない MOD を使ったり、ゲームプレイ設定を標準値から変えたりすると、実績は基本的に獲得できない。
```

## MOD と実績

MOD を使うだけで実績が無効になるわけでは**ない**。決め手は 2 つある：有効な各 MOD が **cosmetic**（見た目だけ）として指定されているかどうか、そしてゲームプレイ設定が標準値のままかどうかである。

- すべての MOD は `mod.json` に `cosmetic` フラグを持つ。ゲーム自身の API ドキュメント（フォルダー `api/tealdef`、フィールド `ModDesc.cosmetic`）には "If the mod is purely cosmetic, cosmetic mods still allow achievement from being earned while playing"（MOD が純粋に見た目だけなら、cosmetic MOD でもプレイ中に実績を獲得できる）とある。
- 公式 DLC とキャンペーンのミッションも MOD であり、すべて cosmetic として指定されている（`dlcs/*/mod.json`、`mods/release/urbangames_campaign*/mod.json`）。
- 新規ゲーム画面とロード画面で、ゲームは有効な MOD の一覧でまだ実績を獲得できるかを確認する（`new_game_or_map_settings_page.tl:902-903`、`savegame_react_util.tl:1063-1064`）。できない場合、オレンジ色の帯に **"Achievements cannot be earned."**（実績を獲得できません。）と表示される（`savegame_react_util.tl:1485-1496`）。
- 各セーブデータも独自のフラグ（`achievementsEarnable`）を持つ。これがオフだと、今どの MOD を選んでもロード画面にオレンジ色の帯が表示される（`savegame_react_util.tl:1035-1037`）。再確認されるのは、実績を強制的にオンに戻す MOD だけである（`savegame_react_util.tl:1063`）。
- ゲームプレイ設定（難易度やその他のゲームパラメーター）が 2 つ目の理由である：標準値から外れると難易度が **"Custom"**（カスタム）と表示され（`difficulty_util.tl:201-229`）、公式 wiki によれば実績は獲得できない。

つまり、cosmetic MOD だけで標準設定のゲームなら実績はまだ獲得できる。cosmetic ではない MOD が 1 つでもあるか、設定が標準値から外れていれば、それだけでブロックされる。そして一度ブロックされたセーブデータはブロックされたままになる。

```engine
どの設定が正確に「標準値から外れている」とみなされるか、そしてセーブデータのフラグがいつ設定されるかはエンジンで決まり、読めるファイルには含まれていない。
```

```tip scripts
ゲームを開始またはロードする前に、オレンジ色の帯を確認しよう：帯がなければ実績を獲得できる。おすすめの遊び方：実績は標準設定と cosmetic MOD だけのゲームで獲得し、ゲームプレイを変える MOD や設定は別のフリーゲームやサンドボックスゲームで使う。cosmetic フラグは MOD 作者が決める。MOD の `mod.json` にある `cosmetic` の行を確認するか、作者に聞こう。
```

## 知っておくと便利なこと

- 「初めて」系の実績は前回の判定と比べて調べられる。実績がまだ未解除のゲームで**新しい**出来事が必要で、セーブにある過去の補助やランクは再び数えられない（`achievements.script.tl:633`、`achievements.script.tl:779`）。
- ランク、補助、評判については[会社のランク、特典、本社](company.html)、[補助](subsidies.html)、[町の評判](reputation.html)で説明している。

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: スクリプトには 17 の実績と 9 つのカウンターがある。公式の説明をより詳しくする：管理人は配達評価が「秀」になること、私のせいじゃないは評判が 1 % 未満、高峰の駅は先頭車両が 500 m より上、完璧主義者は同じ駅の解体・再建・解体・再建、遺産艦隊はベースゲームの全船舶モデルが同時に路線で運行すること。カウンターに数えられるのはベースゲームの車両、貨物、動物だけ。
result: refines
```
