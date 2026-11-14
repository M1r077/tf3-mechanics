---
title: Croissance des villes : XP, notes et taille
summary: D'où vient l'XP d'une ville, comment les six notes fixent son taux de croissance, et de combien chaque niveau l'agrandit.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-14
fact: 0 % | de croissance quand une note est Très insuffisant
fact: ×1,5 | d'XP pour chaque niveau suivant (1 000 pour le niveau 2)
fact: ×40 | de taille après 17 niveaux gagnés
---

Une ville ne grandit que grâce à **ton** transport : les passagers qui arrivent par tes lignes et le fret livré à ses bâtiments lui donnent de l'XP. Ses notes décident quelle part de cette XP compte, et chaque niveau gagné agrandit la ville.

```diagram town_xp
```

## D'où vient l'XP

| Source | XP brute | Source |
|---|---|---|
| Passager arrivé **par tes lignes** à un bâtiment de la ville | 5 · 10 · 20 : logement et emploi ou commerce dans la même ville, une ville voisine, une ville plus loin | `town_growth.script.tl:649-701`, `town_growth_config.res.lua:6` |
| Unité de fret livrée à un bâtiment de la ville | 10 · 20 · 40 pour un fret de niveau 0 · 1 · 2 | `town_growth.script.tl:642`, `town_growth_config.res.lua:5` |
| Récompense de contrat « expérience de ville » | une part du niveau en cours, aussi × le taux de croissance | `subvention_util.tl:144-152`, `town_growth.script.tl:608` |

- L'XP va à la ville du bâtiment où le passager ou le fret **arrive**. Un pendulaire entre deux villes donne de l'XP aux deux : à la ville de l'emploi à l'aller, à sa ville au retour.
- Les trajets vers ou depuis une **industrie** ne donnent pas d'XP (`town_growth.script.tl:680-683`). Les trajets à pied ou en voiture non plus : seuls les trajets faits avec tes lignes comptent (`town_growth.script.tl:656`).
- Le temps seul ne donne rien : l'XP par tick vaut 0 (`town_cargo_util.tl:6`).
- Niveaux de fret : **0** briques, ciment, poisson, carburant, viande, planches, légumes ; **1** boissons, livres, vêtements, meubles, machines, Tinned Food, outils ; **2** véhicules (`placementparamsutil.lua:506-616`).

Chaque XP brute est multipliée par le **taux de croissance** de la ville (`town_growth.script.tl:60-63`). La fenêtre de la ville l'affiche comme **Taux de croissance :**.

## Le taux de croissance

Le taux de croissance vient de deux notes de la fenêtre de la ville (`town_util.tl:607-633`, `town_util.tl:954-962`) :

1. **Autorité municipale** : la **plus basse** de ses six notes, pas la moyenne (`town_util.tl:754-784`).
2. **Apports** : les niveaux d'apport en passagers et en fret, en moyenne arrondie vers le haut (`town_util.tl:555-589`).

```diagram growth_matrix
```

- Chaque note a six niveaux : une valeur de 0 à 1 coupée en sixièmes (`town_util.tl:983-985`). **Excellent** demande 5/6 = 83 % ou plus.
- Avec **une seule** note à Très insuffisant, l'autorité est Très insuffisant et le taux vaut **0 %** : la ville s'arrête, quoi que tu livres.
- 100 % demande une autorité Excellent avec des apports Très bon ou mieux, ou une autorité Très bon avec des apports Excellent.
- Ton **siège social** ajoute +5 % à la ville la plus proche, et la plupart de ses extensions +5 % chacune (`headquarter.script.tl:510-515`, `landmark_util.tl:51-70`). Ce bonus multiplie le taux : il ne fait rien à 0 %.

## Les six notes de l'autorité

| Note | Ce qui la fait baisser | Source |
|---|---|---|
| **Réputation** | terrassement, démolition de bâtiments de la ville, arbres retirés ; chaque liaison principale coupée vers une autre ville −1/3 | `town_util.tl:396-404`, `town_util.tl:1608` |
| **Trafic** | rues encombrées dans la ville | `town_util.tl:445-456` |
| **Bonheur** | part des voyageurs mécontents (au moins 15 personnes supposées) | `town_util.tl:479-503` |
| **Livraison** | part des livraisons de fret en retard (voir [Revenus du fret](income.html)) | `town_util.tl:505-519` |
| **Bruit** | bruit de la ville : 65 dB ou moins → note pleine, 80 dB → 0 | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Pollution** | pollution moyenne de la zone de la ville : 60 dB → pleine, 74 dB → 0 | `town_util.tl:413-431`, `emission_config.tl:23-24` |

Les réglages de **sensibilité** de chaque note (sept crans, le premier est Désactivé) déplacent ces limites ; Désactivé donne toujours la note pleine (`difficulty_util.tl:44-49`).

## Apports

- **Passagers** : utilisation des lignes de la ville × 2, donc **50 % d'utilisation donnent la note pleine** (`town_util.tl:546-553`).
- **Fret** : apport ÷ demande de chaque quartier (commercial, industriel) ; c'est le **meilleur** quartier qui compte, pas la moyenne (`town_util.tl:521-529`).
- Une ville sans rien à approvisionner compte comme apports pleins. Une ville qui ne reçoit de toi ni passagers ni fret compte comme « aucune livraison » : taux de croissance 0 % (`town_util.tl:565-588`).

Les nouvelles demandes de fret viennent avec les niveaux (`placementparamsutil.lua:618-660`) : une commerciale et une industrielle au départ, une deuxième commerciale au niveau 5, une deuxième industrielle au niveau 7, une troisième commerciale au niveau 9, une troisième industrielle au niveau 11. Elles ne s'ajoutent qu'après au moins une livraison de fret à la ville (`town_growth.script.tl:286-288`). Le jeu préfère les frets que peu d'autres villes demandent déjà (`town_growth.script.tl:258-266`).

## Niveaux et taille

- Le niveau 2 demande 1 000 XP, chaque niveau suivant 1,5 fois plus que le précédent (`town_cargo_util.tl:81-97`, `town_growth_config.res.lua:7`) : niveau 5 à 8 125 XP au total, niveau 10 à environ 75 000, niveau 18 (Grande métropole, le dernier) à environ 2 millions.
- Les villes placées avec plus de logements commencent plus haut : niveau 2, 3 ou 4 (`town_cargo_util.tl:43-54`).
- La **taille visée** dépend des niveaux gagnés depuis le départ, progression vers le suivant comprise (`town_cargo_util.tl:100-110`, `town_growth_function.tl:4-11`) :

```diagram town_size
```

- La taille en plus est partagée entre les quartiers résidentiel, commercial et industriel selon leur desserte : usage des passagers pour les logements, apport de fret pour les autres (`town_growth.script.tl:404-421`). Dès qu'un quartier fait 40 % de la ville, la part maximale de taille en plus qu'il peut prendre passe de 100 % à 50 % quand il atteint 50 % de la ville (des limites semblables valent pour toute la carte) (`town_growth.script.tl:509-522`). Si aucun quartier n'est desservi, la ville ne grandit pas, même avec de l'XP (`town_growth.script.tl:415`).

```engine
Le moteur calcule l'utilisation des lignes, la vitesse du trafic, les cartes de bruit et de pollution et la liste des livraisons en retard, et construit les nouvelles maisons et rues. La part minimale qu'un quartier reçoit toujours (townGrowthMinDistrictFraction) est une valeur du moteur.
```

## Bon à savoir

- **Corrige d'abord la pire note** : l'autorité est le minimum, améliorer les autres ne sert à rien.
- Les passagers entre **deux villes** donnent 2 fois (voisines) ou 4 fois (plus loin) l'XP d'un trajet dans une seule ville, et aux deux villes.
- Les frets commerciaux sont seulement de niveau 0–1 ; seuls les **véhicules** (industriels) donnent 40 XP par unité, et une ville ne les demande normalement qu'à partir de sa troisième demande industrielle (niveau 11).
- Une ville loin de ton siège n'a pas son bonus : seule la ville la plus proche l'a.

```check
official: « A town needs 1,000 total XP to reach level 2. The XP required for each following level-up is 1.5 times the amount required for the previous level-up. » Passagers 5 / 10 / 20 XP, fret 10 / 20 / 40 XP. « The Town Authority rating is determined by the lowest of six ratings. » « A line usage of 50% gives the maximum rating. » ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Mêmes chiffres. Taux de croissance de 0 à 100 % par paliers de 20 % selon autorité × apports ; une note Très insuffisant arrête la croissance ; pas d'XP pour les trajets vers les industries ; demandes de fret ajoutées seulement après une première livraison ; la troisième demande commerciale ne peut pas être de niveau 2 dans le jeu de base (aucun fret commercial de niveau 2) ; taille ×40 après 17 niveaux gagnés.
result: refines
```
