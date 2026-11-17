---
title: Monuments, célébrations et éléments amusants
summary: Ce que chaque monument coûte en fret, quand il se débloque et ce qu'il apporte aux véhicules de sa ville, comment le réglage Ressources nécessaires aux monuments le modifie, et ce que font vraiment les célébrations, les feux d'artifice, les dirigeables et les OVNI.
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 9 | monuments, un par rang d'entreprise de 2 à 15
fact: +20 % / -20 % / +25 % | vitesse maximale, pollution ou confort pour les véhicules de sa ville
fact: ×0 à ×4 | de fret nécessaire, avec le réglage Ressources nécessaires aux monuments
fact: 2-4 ans | entre deux OVNI
---

Un monument se construit comme un chantier : tu le débloques avec un rang d'entreprise, tu le places, puis tu **livres du fret**. Quand le chantier a tout son fret, le monument est terminé et donne un bonus aux véhicules de **sa ville**. Le siège social est un bâtiment à part avec ses propres règles (voir [Rang de l'entreprise, avantages et siège social](company.html)).

## Les monuments

Fret avec **Ressources nécessaires aux monuments** ×1 (Normale).

| Monument | Rang | Fret à livrer | Bonus pour les véhicules de sa ville | Source |
|---|---|---|---|---|
| **Amphithéâtre** | 2 | 800 pierre | véhicules routiers : bruit **-25 %** | `arena.con.lua:10`, `arena.con.lua:20-26`, `arena.con.lua:39` |
| **Grand Phare** | 5 | 1 200 pierre, 200 carburant | navires : vitesse maximale **+20 %** | `lighthouse.con.lua:10`, `lighthouse.con.lua:14`, `lighthouse.con.lua:29`, `lighthouse.con.lua:48` |
| **Château du Héron blanc** | 7 | 1 200 pierre, 400 planches | trains : pollution **-20 %** | `white_heron_castle.con.lua:10`, `white_heron_castle.con.lua:14`, `white_heron_castle.con.lua:28`, `white_heron_castle.con.lua:47` |
| **Bateau musée** | 9 | 600 bois, 600 planches, 200 tissu | navires : confort **+25 %** | `ship_museum.con.lua:10-18`, `ship_museum.con.lua:36`, `ship_museum.con.lua:55` |
| **Château de Neuschwanstein** | 10 | 1 000 pierre, 600 planches, 200 colorants | véhicules routiers : confort **+25 %** | `neuschwanstein.con.lua:10-18`, `neuschwanstein.con.lua:36`, `neuschwanstein.con.lua:55` |
| **Statue de la Liberté** | 11 | 800 pierre, 400 acier, 400 tôle | navires : pollution **-20 %** | `statue_of_liberty.con.lua:10-18`, `statue_of_liberty.con.lua:38`, `statue_of_liberty.con.lua:57` |
| **Palais d'été** | 13 | 600 pierre, 300 planches, 300 colorants, 300 meubles | avions : pollution **-20 %** | `summer_palace.con.lua:10-22`, `summer_palace.con.lua:44`, `summer_palace.con.lua:63` |
| **Opéra** | 14 | 800 pierre, 400 verre, 400 tôle, 400 tissu | trains : confort **+25 %** | `opera_house.con.lua:10-22`, `opera_house.con.lua:44`, `opera_house.con.lua:63` |
| **Chambres du Parlement** | 15 | 800 pierre, 400 planches, 400 verre, 400 meubles | véhicules routiers, trains, navires et avions : vitesse maximale **+20 %** | `westminster.con.lua:10-22`, `westminster.con.lua:45`, `westminster.con.lua:79` |

- Chaque monument se débloque une seule fois, par son rang ; la façon dont le rang monte est dans [Rang de l'entreprise, avantages et siège social](company.html).
- Dans leurs fichiers, les monuments ne coûtent rien à construire ni par an : seulement le fret (`arena.con.lua:59-64`).
- Le chantier stocke la moitié de chaque fret à la fois, il faut donc au moins deux livraisons de chacun (`arena.con.lua:13-18`).

## Construire un monument

- Le chantier a **4 étapes**. Il avance à mesure que le fret arrive : étape 2 à un tiers de tout le fret, étape 3 aux deux tiers, terminé à 100 %. Chaque fret ne compte que jusqu'à sa propre quantité : de la pierre en trop ne remplace pas des planches manquantes (`landmarks.script.tl:34-46`).
- Le bonus ne marche que quand le monument est **terminé** (`landmark_util_serialized.tl:393-395`). Le message « Construction terminée » apparaît alors (`landmarks.script.tl:49-61`).
- Le réglage **Ressources nécessaires aux monuments** multiplie tout le fret : Aucun(e) ×0, Bas ×0,5, Normale ×1, Élevée ×2 ou Très élevée ×4. Les préréglages sont Easy ×0,5, Moyen ×1, Hard ×2, Very Hard ×4. À ×0, un monument est terminé dès qu'il est placé (`difficulty_util.tl:40`, `difficulty_util.tl:107`, `difficulty_util.tl:135`, `difficulty_util.tl:162`, `difficulty_util.tl:189`, `landmarks.script.tl:38`, `landmarks.script.tl:46`).

## Qui reçoit le bonus

- Le bonus va à la ville **la plus proche du monument**, et aux véhicules dont la ville la plus proche est cette ville, du mode de transport indiqué (`landmark_util.tl:6-47`, `landmarks.script.tl:208-236`).
- Quand un véhicule entre dans la zone d'une autre ville, il prend les bonus de cette ville et perd les anciens (`landmarks.script.tl:279-299`).
- Les bonus de plusieurs monuments dans la même ville **s'additionnent** : deux +20 % de vitesse maximale donnent +40 % (`landmark_util.tl:46`, `vehicle_modifier.script.tl:3-16`).

```engine
La « ville la plus proche » d'un monument ou d'un véhicule en mouvement est décidée par le moteur (getConstructionClosestTown, closestTown). La façon dont le moteur transforme +25 % de confort ou +20 % de vitesse maximale en trajets et en revenus relève aussi du moteur.
```

```tip scripts
Place les Chambres du Parlement dans la ville où roulent la plupart de tes véhicules : +20 % de vitesse maximale pour tous les modes. Un second +20 % vient du Grand Phare pour les navires de la même ville. Le succès Centralisation demande 10 monuments terminés avec la même ville la plus proche, alors que les fichiers du jeu contiennent 9 monuments en plus du siège social (comptés) ; on ne sait pas s'il peut être obtenu dans cette version (voir [Succès](achievements.html)).
```

## Célébrations

Une célébration est la petite fête affichée au-dessus d'une ville quand quelque chose arrive pour la première fois. Elle augmente aussi la **Réputation** de la ville, mais seulement quand la Réputation n'est pas déjà pleine.

| Événement | Réputation | Source |
|---|---|---|
| premier passager à monter dans une de tes lignes dans la ville | +50 % | `celebrations.script.tl:228-252` |
| premier fret livré à la ville | +50 % | `celebrations.script.tl:187-198` |
| la ville monte de niveau | +50 % | `celebrations.script.tl:260-272` |
| premier fret livré à une industrie | +20 % pour la ville la plus proche | `celebrations.script.tl:202-219` |

- Une ville qui monte de niveau a aussi des **feux d'artifice**, sauf s'ils sont désactivés (`town_growth.script.tl:108-112`).
- Le fonctionnement de la Réputation : [Réputation](reputation.html).

## Éléments amusants

- Un **dirigeable** survole une ville quand tu y lances une Campagne marketing (`fun_elements.script.tl:112-117`).
- Un **OVNI** apparaît tous les **2 à 4 ans** de temps de jeu, au hasard, quand il n'y en a aucun sur la carte (`fun_elements.script.tl:10`, `fun_elements.script.tl:79-91`). Clique dessus pour le succès Rencontre du 3ᵉ type.
- Aucun d'eux ne change l'économie.

## Bon à savoir

- Choisis la ville avant de construire : le bonus ne suit pas tes lignes, seulement les véhicules près de cette ville.
- En Very Hard, un monument demande quatre fois plus de fret : les Chambres du Parlement demandent alors 3 200 pierre et 1 600 de chacun des autres frets.

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: Neuf monuments, un par rang de 2 à 15, chacun construit avec du fret livré en 4 étapes, modifié par Ressources nécessaires aux monuments ×0 à ×4. Une fois terminé, chacun donne un bonus (+20 % de vitesse maximale, -20 % de pollution, -25 % de bruit ou +25 % de confort) aux véhicules d'un mode de transport dans sa ville la plus proche ; les bonus s'additionnent. Les célébrations ajoutent 50 % ou 20 % de Réputation ; un OVNI vient tous les 2 à 4 ans.
result: adds
```
