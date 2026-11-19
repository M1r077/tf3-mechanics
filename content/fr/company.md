---
title: Rang de l'entreprise, avantages et siège social
summary: Ce qui fait monter le rang de ton entreprise, ce que chaque rang débloque, comment fonctionnent les permis et les prospections, ce que le siège social apporte vraiment et ce qu'un rang plus élevé te coûte.
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40444
fact: 15 | rangs d'entreprise, de Junior à Magnat
fact: ×12,5 | de population mondiale nécessaire pour le rang 15, par rapport au départ
fact: ×0,75 | de revenus au rang 15 avec l'Inflation Normale
fact: 0 | rang perdu quand la population baisse
---

Le rang de ton entreprise ne vient ni de l'argent ni des livraisons : il vient de la **population de toute la carte**. Chaque nouveau rang débloque des avantages (monuments, prospections, campagnes marketing, Verdissement de l’industrie, modules du siège social), et avec le réglage **Inflation** il baisse aussi un peu tous tes revenus.

## Ce qui fait monter le rang

- Le jeu retient la **population mondiale au départ** de la partie : les habitants de toutes les villes (`company.script.tl:392-396`, `company_util.tl:365-371`).
- Il compare ensuite la population mondiale **la plus haute** jamais atteinte avec cette valeur de départ (`company_growth.script.tl:25-27`). La valeur ne fait que monter : des villes qui rétrécissent ne te coûtent jamais un rang.
- Le rang 1 est atteint à la valeur de départ, le rang 15 à environ **12,5 fois** celle-ci (`company_progression_util.tl:6-14`, `company_progression_util.tl:95-120`, `town_growth_function.tl:13-20`).
- Il n'y a pas de rang dans les missions de campagne ni dans l'éditeur de cartes (`company_growth.script.tl:74-79`).

| Rang | Rôle | Population mondiale, par rapport au départ |
|---|---|---|
| 1 | Junior | ×1 |
| 2 | Mécanicien | ×1,02 |
| 3 | Ingénieur | ×1,08 |
| 4 | Coordinateur | ×1,2 |
| 5 | Expert | ×1,4 |
| 6 | Chef d’équipe | ×1,7 |
| 7 | Superviseur | ×2,1 |
| 8 | Manager | ×2,6 |
| 9 | Directeur | ×3,3 |
| 10 | Directeur principal | ×4,2 |
| 11 | PDG | ×5,3 |
| 12 | Président du conseil | ×6,7 |
| 13 | Vice-président | ×8,3 |
| 14 | Président | ×10,2 |
| 15 | Magnat | ×12,5 |

Les rapports sont calculés à partir des scripts pour une population de départ de 50 000 ou plus (`company_progression_util.tl:6-14`, `company_static_util.tl:6-24`). Sur une petite carte, ils sont un peu plus élevés pour les rangs du milieu (le rang 8 demande ×2,85 avec 5 000 habitants) ; les rangs 1 et 15 restent à ×1 et ×12,5.

- Le rang suit donc la **croissance des villes** : les villes grandissent grâce à tes passagers et à ton fret, voir [Croissance des villes](towns.html).
- Les premiers rangs arrivent vite, les derniers demandent des villes plusieurs fois plus grandes.

## Un nouveau rang s'applique dans la fenêtre de l'entreprise

Quand la population passe un seuil, une **notification de rang** apparaît ; un clic dessus ouvre la fenêtre de l'entreprise sur ce rang (`company_growth.script.tl:96-107`, `company_notification_rank_up.script.tl:8-9`).

- Les nouveaux avantages ne sont débloqués que quand ce rang est **sélectionné dans la fenêtre de l'entreprise** : la fenêtre envoie alors le déblocage (`company.tl:420-423`, `company_growth.script.tl:55-62`). Les menus de construction vérifient ce rang appliqué (`company_util.tl:92`, `company_util.tl:171-178`).
- Le multiplicateur de revenus de la section suivante suit le rang **atteint**, appliqué ou non (`company_growth.script.tl:47-48`).

```tip scripts
Après un nouveau rang, clique sur la notification (ou ouvre la fenêtre de l'entreprise et sélectionne le nouveau rang) pour obtenir les avantages. Attendre ne te rapporte rien : les revenus sont déjà baissés.
```

## Ce que coûte un rang plus élevé : le réglage Inflation

Avec l'**Inflation**, tous les revenus du fret et des passagers baissent régulièrement de ×1 au rang 1 jusqu'à un minimum au rang 15 (`company_progression_util.tl:25-40`, `company_growth.script.tl:159-170`).

| Inflation | Revenus au rang 15 | Source |
|---|---|---|
| Aucune | ×1 (aucun changement) | `difficulty_util.tl:50`, `mod.script.tl:695-698` |
| Faible | ×0,9 | |
| Normale | ×0,75 | |
| Élevée | ×0,6 | |
| Très élevée | ×0,5 | |

- En Normale, chaque rang coûte environ 1,8 % des revenus : ×0,96 au rang 3, ×0,875 au rang 8, ×0,75 au rang 15.
- L'Inflation n'augmente aucun coût ; les coûts suivent l'année du calendrier (voir [Coûts, entretien et emprunts](costs.html)).
- Un rang plus élevé rend aussi les nouvelles offres de contrats plus rares (voir [Contrats](subsidies.html)).

## Permis

La plupart des avantages sont limités par des **permis**. Un rang donne des permis pour un avantage ; chaque bâtiment ou utilisation en prend un (`company_util.tl:33-80`, `company_util.tl:206`).

- Les permis **s'additionnent** au fil des rangs : un avantage qui en donne 1 au rang 3 et 1 au rang 5 en permet 2 à partir du rang 5 (`company_util.tl:51-56`).
- Un bâtiment rend son permis quand il est démoli : le jeu compte ce qui est debout (`company_util.tl:143-163`, `company_util.tl:203-206`).
- Les prospections, les campagnes marketing et le verdissement consomment un permis au démarrage (`company.script.tl:416-423`, `company.script.tl:459-462`, `company.script.tl:496-500`). Le menu de construction affiche alors **Déjà utilisé** ou **Temps de recharge** (`company_util.tl:207-226`).
- Le permis **Marketing** revient **5 ans** après chaque campagne (`marketing.res.lua:6-7`, `company.script.tl:66-94`).

| Avantage | Permis | Source |
|---|---|---|
| Siège social | 1 au rang 1 | `hq.res.lua:6` |
| Campagne marketing | 1 au rang 4, revient après 5 ans | `marketing.res.lua:6-7` |
| Verdissement de l’industrie | 1 aux rangs 3, 6, 9, 12 et 15 | `industry_greenify_tool.script.tl:101-102` |
| Station de dépollution | 15 au rang 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Monuments | un chacun : Amphithéâtre 2, Grand Phare 5, Château du Héron blanc 7, Bateau musée 9, Château de Neuschwanstein 10, Statue de la Liberté 11, Palais d’Été 13, Opéra 14, Chambres du Parlement 15 | `arena.con.lua:39`, `lighthouse.con.lua:48`, `white_heron_castle.con.lua:47`, `ship_museum.con.lua:55`, `neuschwanstein.con.lua:55`, `statue_of_liberty.con.lua:57`, `summer_palace.con.lua:63`, `opera_house.con.lua:63`, `westminster.con.lua:79` |

Ce que fait chaque avantage : [Réputation](reputation.html) (campagne marketing), [Pollution et bruit](emission.html) (verdissement, Station de dépollution).

## Prospections

Une prospection cherche une ressource près d'une ville et, si elle réussit, y fonde une nouvelle industrie.

| Ressource | Rang | Source |
|---|---|---|
| Poisson | 2 | `exploration_fish.res.lua:9-11` |
| Argile | 3 | `exploration_clay.res.lua:9-11` |
| Pétrole brut | 4 | `exploration_crude_oil.res.lua:9-11` |
| Céréales, légumes | 4, **un seul permis partagé** (Industrie) | `exploration_grain.res.lua:9`, `exploration_vegetables.res.lua:9`, `permit_key_farm.res.lua:6` |
| Bois | 5 | `exploration_logs.res.lua:9-11` |
| Charbon, minerai de fer | 6 | `exploration_coal.res.lua:9-11`, `exploration_iron_ore.res.lua:9-11` |
| Pierre, laine | 8 | `exploration_stone.res.lua:9-11`, `exploration_wool.res.lua:9-11` |
| Sable | 9 | `exploration_sand.res.lua:9-11` |
| Caoutchouc | 12 | `exploration_rubber.res.lua:9-11` |

- Chaque ressource a **un** permis, consommé au démarrage de la prospection (`company.script.tl:451-462`).
- Elle dure jusqu'à **6 mois**. Une fois par mois, elle essaie de placer l'industrie, avec une chance qui monte de 20 % à 60 % sur les 6 mois (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`).
- Un essai échoue aussi quand le jeu ne trouve pas de place pour cette industrie près de la ville (`company.script.tl:199-210`).
- Si le dernier essai échoue, **le permis revient** et une notification le signale (`company.script.tl:106-126`, `company.script.tl:170-181`).
- Une seule prospection par ville et par ressource peut tourner à la fois (`company.script.tl:442-447`).

```engine
L'endroit où la nouvelle industrie peut se placer (makeIndustrySpawnProposal près de la ville) est décidé par le moteur : une prospection de poisson loin de l'eau, ou une ville sans terrain libre autour, échoue simplement et rend le permis.
```

## Le siège social

| Quoi | Valeur | Source |
|---|---|---|
| Prix et entretien | gratuit, sans entretien | `headquarter.script.tl:526-527` |
| Permis | 1, au rang 1 | `headquarter.con.lua:6-7`, `hq.res.lua:6` |
| Croissance des villes | +5 % pour la ville la plus proche | `headquarter.script.tl:510-515`, `landmark_util.tl:51-70` |
| Emplois | 24 | `headquarter.con.lua:16`, `headquarter.script.tl:505-508` |

- Les +5 % sont un bonus sur le taux de croissance de cette ville : ils ne font rien quand ce taux est de 0 % (voir [Croissance des villes](towns.html)).
- Les **modules** coûtent 50 000 chacun et sont limités par des permis qui augmentent avec le rang (`hq_module_m.module.lua:83`, `hq_module_m.module.lua:137`).
- Seuls deux modules ont un bonus dans les fichiers : le **Bâtiment de taille moyenne**, +1 % de croissance de la ville (`hq_module_m.module.lua:139-142`), et le **Grand bâtiment**, +1 % de Récupération de réputation (`hq_module_l.module.lua:169-172`). Le bonus de récupération n'est lu par aucune note de ville (voir [Réputation](reputation.html)). Les autres modules sont décoratifs.
- Chaque fichier de module commence aussi par une table qui donne +5 % de croissance, mais rien dans le fichier ne l'utilise (`hq_corner_l.module.lua:148-159`, `hq_statue.module.lua:46-57`). Seul le bonus dans les `metadata` du module est additionné (`headquarter_addon.script.tl:18-29`).

| Module | Permis gagnés au rang (×2 = deux) | Total au rang 15 |
|---|---|---|
| Drapeau sur mât | 1 ×2, 6, 7, 8, 9, 11, 12, 13, 14 | 10 |
| Bâtiment d’angle | 3, 5, 7 ×2, 9, 11, 13, 15 | 8 |
| Bâtiment de taille moyenne | 2, 4, 10 ×2, 15 ×2 | 6 |
| Grand bâtiment | 5, 6, 10, 12 | 4 |
| Balcon | 8 ×2, 14 ×2 | 4 |
| Grande fontaine | 10 ×2, 14 ×2 | 4 |
| Dôme | 6, 15 ×2 | 3 |
| Drapeau de toit | 7, 10, 13 | 3 |
| Court de tennis | 11, 12, 14 | 3 |
| Arbre ancien | 13, 15 ×2 | 3 |
| Statue | 14 ×2 | 2 |
| Piscine | 15 | 1 |

Sources : la ligne `rankAndPermits` de chaque fichier de module (`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`).

```tip scripts
Place le siège social dans la ville que tu veux faire grandir le plus vite, et ajoute-y des Bâtiments de taille moyenne : ce sont les seuls modules avec un bonus de croissance.
```

## Bon à savoir

- Pour monter en rang, fais grandir les villes : plus de passagers et de fret vers plus de villes, avec de bonnes notes. L'argent en banque ne compte pas.
- Planifie tes monuments et tes prospections : chacun ne vient qu'une fois, à un rang fixe.
- Sur une carte avec Inflation, un nouveau rang est bon pour les avantages et mauvais pour les revenus. En Normale, tout le chemin jusqu'au rang 15 coûte un quart de tous les revenus.

```check
official: "The company rank depends on the population of the map. … Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Même règle : la population mondiale la plus haute atteinte, comparée à la population de départ, ×12,5 pour le rang 15 ; jamais perdu. Un nouveau rang doit être sélectionné dans la fenêtre de l'entreprise pour débloquer ses avantages, alors que l'Inflation baisse les revenus tout de suite. Seuls deux modules ont un bonus (Bâtiment de taille moyenne +1 % de croissance, Grand bâtiment +1 % de Récupération de réputation, qu'aucune note ne lit) ; les autres sont décoratifs.
result: refines
```
