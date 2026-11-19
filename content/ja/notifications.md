---
title: 通知と警告
summary: 各警告がいつ出ていつ消えるか：立ち往生した車両、使えない駅や混雑した駅、路線と停車駅の問題、町の評価、車両状態、閉鎖する産業、そして初期設定でログに残らない警告。
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40444
fact: 5 分 | 車両が立ち往生と報告されるまでに止まっているゲーム時間
fact: 20 % | 警告が出る車両状態。30 % を超えるまで続く
fact: 11 | 新しいゲームでオフになっている通知の種類
fact: 75 日 | 道路に接続されていない駅を調べる間隔
---

ほとんどの警告は**持続型**である。ゲームスクリプトが状況を繰り返し調べ、問題がある間は警告が残り、解決すると自然に消える。調査は 4 回の更新に順番に分けて行われるため、警告が出たり消えたりするまで少し時間がかかることがある（`notifications.script.tl:13`、`notifications.script.tl:49`）。

## 各警告が出る条件

| 警告 | 出る条件 | 消える条件 | ソース |
|---|---|---|---|
| **車両が立ち往生しています** | あなたの車両が運行中で、あなたが止めたのではなく、ゲーム時間で **5 分**間速度 0 のまま | 再び動く | `notifications.script.tl:557-580` |
| **駅が機能していません** | 駅のどのターミナルでも旅客の乗降がなく、集客範囲に**何も**ない（倉庫、産業、町の建物がない）状態で、あなたの路線が停車している | 集客範囲に何かが入る | `notifications.script.tl:602-617`、`notifications.script.tl:630-647`、`station_useless.script.tl:39` |
| **駅が混雑しています** | 駅で待つ旅客や貨物が収容量を超え（あふれ）、あなたの路線が停車している。旅客は去っていく | あふれが解消する | `notifications.script.tl:599`、`notifications.script.tl:649-661`、`overcrowding.script.tl:23` |
| **車両状態** | あなたの車両の状態が **20 %** 以下 | **30 %** を超えるまで戻る | `notifications.script.tl:310-318` |
| **町の評価が極めて低い** | 町の評価のどれかが「劣」（1/6 未満）に落ちる | 評価が「可」以上に戻る | `notifications.script.tl:230-238`、`town_util.tl:763-769`、`town_util.tl:983-985` |
| **町の評価が低下中** | 評価が「不可」または「可」（50 % 未満）で、「劣」の警告には入っていない | 評価が「良」以上になる | `notifications.script.tl:240-248` |
| **産業の閉鎖** | 産業が閉鎖のカウントダウンを始める | 閉鎖する、または間に合ううちに再び利用される | `notifications.script.tl:439-451`、`industry_close.script.tl:53-59` |
| **道路の接続なし** | 駅が道路に接続されていない。**75 日**ごとに調べられる | 次の調査で道路が見つかる | `notifications.script.tl:16`、`notifications.script.tl:423-436` |
| **貨物積み下ろしの問題** | 車両の貨物がその路線のどこでも積み下ろされない | 積み下ろされる | `notifications.script.tl:277-290`、`cargo_rtc_warning.script.tl:28-37` |

- **車両基地にいる**車両は立ち往生とみなされない。その判定はスクリプトで無効にされている（`notifications.script.tl:563-564`）。あなたが止めた車両もみなされない。
- 「駅が機能していません」の判定は集客範囲だけを見る。ターミナルですでに旅客の乗降がある駅は報告されない（`notifications.script.tl:606-610`）。
- 町の評価を上げる方法は[町の成長](towns.html)と[評判](reputation.html)、閉鎖のカウントダウンの仕組みと止め方は[産業](industries.html)、車両状態が車両に与える影響は[コスト、維持費、借入](costs.html)を参照。

```engine
駅があふれているか、車両に経路があるか、路線が駅に到達できるか、2 つの町の間の移動にどれだけかかってよいかは、エンジンが判定する（calculateStationGroupCargo、getVehicleProblems、getLineProblems、getTownProblems）。スクリプトはその結果を警告に変えるだけである。
```

```tip scripts
「車両が立ち往生しています」「車両の問題」「車両状態」「駅が混雑しています」「駅が使用できません」は、新しいゲームではログでオフになっている。通知の設定でオンにしよう。渋滞、経路の欠如、老朽化した車両群を知らせてくれる警告である。
```

## 路線、停車駅、車両の問題

これらはエンジンによる路線と車両の判定をそのまま使い、スクリプトがそれぞれに見出しを付ける。

| 警告 | ケース | ソース |
|---|---|---|
| **路線の問題** | 駅が少なすぎる、同じ駅が 2 回続く、駅同士に互換性がない、駅を接続できなかった、代替ターミナルを接続できなかった | `line_warning.script.tl:46-128` |
| **路線の設定が正しくありません** | どこでも積み込めない、またはどこでも積み下ろせない貨物の種類がある、積み込む設定の貨物を運べる車両がない、設定したどの貨物も運ばない車両や、旅客路線の貨物専用車両がある、貨物がまったく設定されていない | `line_warning.script.tl:15-36`、`line_warning.script.tl:133` |
| **駅の問題** | 現在の車両が使えない停車駅、旅客用の停車駅を貨物車両が使っている（一部またはすべて）、貨物用の停車駅を旅客車両が使っている、設定した貨物の種類をその停車駅で積み込めない、または積み下ろせない | `line_station_warning.script.tl:6-87` |
| **車両の問題** | 電化された経路がない、大型航空機用の経路がない、大型船舶用の経路がない、経路がまったくない、2 本の列車が互いにふさいでいる | `vehicle_warning.script.tl:6-58` |
| **街が接続されていません** | 2 つの町の間の道路が途切れている、2 つの町の間の移動に時間がかかりすぎる | `town_warning.script.tl:7-19` |

- 「大型航空機用の経路がありません」と「大型船舶用の経路がありません」は、車両がその路線の滑走路、ドック、水路に対して大きすぎることを意味する。[航空機](aircraft.html)と[船舶](ships.html)を参照。

## ログ、ポップアップ、設定

- 警告の種類はそれぞれ通知の設定（「通知ログを設定」）でオフにできる。オフにした種類はポップアップが出ず、ログにも残らない（`notification_util.tl:145-146`、`notification_log.tl:480`）。
- **新しいゲーム**では、11 種類が最初からオフになっている：**車両が立ち往生しています**、**車両の問題**、**車両状態**、**駅が混雑しています**、**駅が使用できません**、**駅が接続されていません**、**街が接続されていません**、**積み下ろされていない貨物**、そして会社の資源調査、マーケティングキャンペーン、産業の緑化の進行メッセージ（`stuck_vehicle.res.lua:7`、`vehicle_warning.res.lua:8`、`noroadconnection.res.lua:8`、`vehiclecondition.res.lua:8`、`overcrowding.res.lua:8`、`station_useless.res.lua:7`、`town_warning.res.lua:8`、`cargo_rtc_warning.res.lua:8`、`notification_util.tl:32-39`）。
- 1 回限りのメッセージ（新しい車両、新しい建設、昇格、助成金）は、ゲーム時間で **60 秒**後にポップアップが消える。履歴には残る（`notification_util.tl:10`、`notifications.script.tl:85-94`）。
- 通知が指しているものがすべて撤去または再建されたときも、その通知は終わる（`notifications.script.tl:95-107`）。
- ミッションでは通知は一時停止の状態で始まり、ミッションがオンにするまで続く（`notifications.script.tl:700-704`）。

## 知っておくと便利なこと

- 5 分後の立ち往生の警告は理由を教えてくれない。車両を見てみよう：赤信号、逆向きの一方通行信号、または同じ車両の「車両の問題」警告。
- 「駅が機能していません」は「集客範囲にまだ何もない」という意味でしかない。駅を家、産業、倉庫に近づけるか、駅を大きくしよう。
- 混雑した駅は旅客を失う。車両を増やすか、運行間隔を短くしよう（[発車と待機](departure.html)を参照）。

```check
official: The official wiki's User Interface page describes the notification button, the log and its filters, without the conditions of each warning. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: 上記の条件：運行中に速度 0 で 5 分たつと立ち往生、車両状態は 20 % から 30 % まで、町の評価「劣」は 1/6 未満、道路接続は 75 日ごとに確認、初期設定で 11 種類がオフ。
result: adds
```
