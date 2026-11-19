---
title: Coûts, entretien et emprunts
summary: Ce que changent les réglages de coûts, quels coûts montent avec l'année du calendrier, comment le prix des véhicules est calculé, et ce que coûte vraiment un emprunt.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
game: 40444
fact: ×6 | facteur d'année sur l'entretien des entrepôts, ports et aéroports en 2020
fact: 6 ans | de coûts d'exploitation : le prix d'un véhicule
fact: une fois | le taux d'un emprunt est appliqué au montant, pas chaque année
fact: 4 | emprunts en même temps
---

Le réglage **Inflation** n'augmente aucun coût : il baisse seulement tes revenus quand le rang de l'entreprise monte (voir [Revenus du fret](income.html)). Les coûts montent avec l'**année du calendrier**, et quatre curseurs les règlent dès le départ.

```diagram cost_years
```

## Les réglages de coûts

| Réglage | Valeurs | Préréglages Easy · Moyen · Hard · Very Hard | Source |
|---|---|---|---|
| **Coût des véhicules**, **Entretien des véhicules** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:39`, `difficulty_util.tl:98-101`, `difficulty_util.tl:125-128`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Coût des infrastructures**, **Entretien des infrastructures** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:98-101`, `difficulty_util.tl:125-128`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Effet de la maintenance des véhicules** | Aucun(e) ×0 · Bas ×0,5 · Moyen ×1 · Élevée ×1,5 · Très élevée ×2 | Bas · Moyen · Élevée · Très élevée | `difficulty_util.tl:42`, `difficulty_util.tl:103`, `difficulty_util.tl:185` |
| **Inflation** | revenus seulement, voir [Revenus du fret](income.html) | Faible · Normale · Élevée · Très élevée | `difficulty_util.tl:50`, `mod.script.tl:695-698` |

- **Coût des infrastructures** règle le prix des routes, voies, ponts, tunnels, passages à niveau, bâtiments et modules, ainsi que les travaux de terrain (`post_run_util.tl:23-52`, `post_run_util.tl:83-120`, `construction.script.tl:31-35`, `mod.script.tl:224-227`). Il règle aussi le coût de démolition des bâtiments (`construction.script.tl:39-44`). **Entretien des infrastructures** règle l'entretien des routes, voies, ponts, tunnels, passages à niveau et modules au chargement (`post_run_util.tl:43-45`, `post_run_util.tl:105-112`). Pour les bâtiments, les scripts ne l'appliquent que dans la fenêtre du bâtiment (`entity_window_util.tl:186`) ; ce qui est facturé est décidé par le moteur.
- **Coût des véhicules** et **Entretien des véhicules** règlent le prix d'achat et les coûts d'exploitation de chaque véhicule (`post_run_util.tl:54-81`).
- **Effet de la maintenance des véhicules** règle à quel point un véhicule en mauvais état perd vitesse, puissance et confort et gagne bruit, pollution et coûts d'exploitation (`mod.script.tl:242-246`).

## Ce qui monte avec l'année du calendrier

- **Entretien des bâtiments** : ×1 en 1900, ×1,5 en 1920, ×2,2 en 1940, ×3,2 en 1960, ×4 en 1980, ×5 en 2000, ×6 en 2020 (`mod.script.tl:92-100`). La fenêtre du bâtiment et le menu de construction l'appliquent à chaque bâtiment marqué pour suivre l'année, et le menu de construction marque toutes les méta-constructions (dans le jeu de base : entrepôts, aérodromes, aéroports et ports) (`entity_window_util.tl:186-193`, `construction_react_util.tl:1152`, `warehouse.tl:7`, `harbor_modular.tl:24`).
- Les **modules** ajoutés à un tel bâtiment sont facturés à l'année de construction du bâtiment, leur entretien à l'année en cours (`construction.tl:3741-3748`, `construction.tl:4413-4416`).
- **Variantes par époque** : dépôts, ateliers d'entretien, entrepôts, gares, ports et aéroports ont une variante par époque, et chaque variante suivante coûte **×3** (époque B) ou **×9** (époque C) de la première (`rail_depot.con.lua:7`, `warehouse.tl:48`, `modular_station.con.lua:71`, `harbor_modular.tl:76`, `airport.tl:8`).
- **Argent des contrats** : ×1 en 1900 jusqu'à ×4 dès 2000 (`finances_util.tl:87-90`). **Montant des emprunts** : ×0,4 en 1900 jusqu'à ×2,4 en 2020 (`loan_util.tl:7-10`).
- Les **revenus** n'ont aucun facteur d'année (`cargo_income.script.lua:10-13`).

```engine
L'entretien réellement prélevé, et le fait que routes, voies et véhicules suivent aussi la table des années, sont décidés par le moteur (getCostMultiplierForYear ; la config de base fixe seulement chargeMaintenanceInterval = 60, `mod.script.tl:105`). Les scripts calculent seulement les valeurs affichées dans les fenêtres et le menu de construction, avec la table ci-dessus. Aucun script ne met le drapeau « suivre l'année » des autres bâtiments.
```

## Voies, routes et bâtiments

Les fichiers des routes et des voies donnent le prix et l'entretien annuel par mètre ; le menu de construction les affiche par kilomètre (`construction_react_util.tl:2466`, `construction_react_util.tl:2480-2488`). Pour la plupart des types, l'entretien vaut **un sixième** du prix de construction :

| Type | Disponible dès | Construction par km | Entretien par km et par an | Source |
|---|---|---|---|---|
| Voie simple | début | 60 000 | 10 000 | `simple.street_template.lua:9`, `simple.street_template.lua:33` |
| Voie standard | 1930 | 180 000 | 30 000 | `standard.street_template.lua:11`, `standard.street_template.lua:35` |
| Voie à grande vitesse | 1980 | 540 000 | 90 000 | `high_speed.street_template.lua:11`, `high_speed.street_template.lua:35` |
| Petite route de campagne ancienne | début – 1940 | 60 000 | 10 000 | `country_old_small.street_template.lua:4-5`, `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:58` |
| Grande rue moderne | 1940 | 540 000 | 90 000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:91` |

- La caténaire ajoute **30 %** du prix de la voie ; une voie de bus 10 %, une voie de tram 20 %, une voie de tram électrique 40 % du prix de la rue (`mod.script.tl:24-28`).
- Relever le terrain coûte 4,5 par m³, l'abaisser 5,25 par m³, les deux × Coût des infrastructures ; supprimer un champ 200 000 (`mod.script.tl:20-22`, `mod.script.tl:33`, `mod.script.tl:226-227`).
- Un bâtiment qui ne fixe pas d'entretien paie **un sixième de son prix** par an, calculé sur le prix avant le réglage Coût des infrastructures (`construction.script.tl:25-27`).
- La config de base fixe un facteur de remboursement à la démolition de 0,75 et un délai de 60 (`mod.script.tl:30-31`) : démolir ce que tu viens de construire rend la plus grande partie de l'argent. C'est le moteur qui l'applique.

Entretien annuel écrit dans les fichiers, pour la première variante (avant 1940) et les suivantes ; les entrepôts reçoivent en plus le facteur d'année ci-dessus :

| Bâtiment | Première variante | ×3 (dès 1940) | ×9 (dès 1980) | Source |
|---|---|---|---|---|
| Dépôt de trains, dépôt de bateaux | 100 000 | 300 000 | 900 000 | `rail_depot.con.lua:34`, `water_depot.con.lua:32` |
| Dépôt routier | 30 000 | 90 000 | 270 000 | `road_depot.con.lua:32` |
| Dépôt de trams | 20 000 | 60 000 | 180 000 | `tram_depot.con.lua:34` |
| Atelier d'entretien trains ou bateaux | 40 000 | 120 000 | 360 000 | `rail_maint_station.con.lua:32`, `water_maint_station.con.lua:32` |
| Atelier d'entretien routier | 10 000 | 30 000 | 90 000 | `road_maint_station.con.lua:32` |
| Entrepôt universel | 25 000 | 75 000 | 225 000 | `warehouse.tl:48-52`, `warehouse.tl:75` |
| Entrepôt spécialisé | 50 000 | 150 000 | 450 000 | `warehouse.tl:51`, `warehouse.tl:75` |

Chacun de ces bâtiments coûte **6 ×** son entretien à construire (`rail_depot.con.lua:35`, `warehouse.tl:76`) : 2,7 M pour un entrepôt spécialisé de la dernière époque, avant le facteur d'année.

- Le premier **aérodrome** (jusqu'en 1950) utilise déjà le ×3 de la deuxième époque : son test lit l'année de fin de la variante au lieu de l'année de début (`airfield.tl:8`, `airfield_era_a.metacon.tl:3`).

## Véhicules

Aucun véhicule du jeu de base n'a de prix fixe : le jeu le calcule à partir de la vitesse et de la capacité du véhicule quand il charge le modèle (`model_metadata_util.lua:488-552`) :

1. **Coûts d'exploitation par an** = environ 675 × vitesse moyenne (m/s) × capacité / 4 (`model_metadata_util.lua:499-518`). Le 675 vient du revenu moyen par km, réduit pour laisser de la marge aux retours à vide, à l'achat et à la baisse du prix des billets (`model_metadata_util.lua:500-508`).
2. La **vitesse moyenne** est inférieure à la vitesse maximale (v en km/h) : véhicules routiers et trams v^0,78 + 4, trains v^0,86 + 10, avions −0,0000203 × v² + 0,17 × v + 28,36 (v au plus 4 000), bateaux 65 % de la vitesse max (`model_metadata_util.lua:448-474`).
3. **Trains** : un wagon compte la moitié de sa capacité ; une locomotive compte en plus puissance ÷ vitesse max (km/h) × 12,5 comme capacité, divisée par deux aussi (`model_metadata_util.lua:511-512`, `model_metadata_util.lua:526-540`). Une locomotive puissante et lente coûte cher.
4. **Prix** = **6 ×** les coûts d'exploitation annuels (`model_metadata_util.lua:548-549`).

Exemple à 100 % : un bus à 35 km/h pour 48 passagers coûte environ 45 000 par an à faire rouler et environ 270 000 à l'achat.

- L'état d'un véhicule a cinq niveaux (100–80 %, puis tous les 20 %) (`vehicle_store_util.tl:231-234`) ; à **20 %** le jeu le signale jusqu'à ce qu'il repasse au-dessus de 30 % (`notifications.script.tl:310-318`).

```engine
La vitesse à laquelle l'état d'un véhicule baisse, la hausse des coûts d'exploitation qui en résulte, et une éventuelle évolution du prix des véhicules avec l'année sont des valeurs du moteur (getMaintenanceRunningCostPenalty et les autres pénalités) ; les scripts les règlent seulement avec l'Effet de la maintenance des véhicules.
```

## Emprunts

```diagram loan_interest
```

| Type | Montant vers 1960 (×0,4 en 1900, ×2,4 en 2020) | Durée | Taux | Source |
|---|---|---|---|---|
| Petit | 5–10 M | 1–5 ans | 3–5 % | `loan_util.tl:12-22` |
| Moyen | 15–25 M | 3–8 ans | 5–8 % | `loan_util.tl:24-34` |
| Grand | 30–50 M | 5–12 ans | 8–10 % | `loan_util.tl:36-46` |
| Très grand | 40–60 M | 10–24 ans | 10–12 % | `loan_util.tl:48-58` |

- La carte parle de **Taux d'intérêt annuel**, mais le taux est appliqué **une seule fois** au montant : le total des intérêts vaut montant × taux, quelle que soit la durée. Il est payé en parts égales chaque mois avec le capital (`loan_util.tl:102-111`, `loan_util.tl:126-136`, `loan.script.tl:83-99`). Un emprunt long coûte donc moins par an qu'un emprunt court au même taux.
- **Rembourser** paie seulement le reste du capital : les intérêts restants sont supprimés (`loan.script.tl:171-190`). Le bouton demande ce montant en caisse (`finances_loan_gui.tl:284-286`).
- Les taux ne dépendent **pas** de la difficulté : chaque type a sa propre fourchette fixe (`loan_util.tl:12-58`).
- Au plus **4 emprunts** en même temps (`loan_util.tl:4`, `loan.script.tl:134`). Une offre est remplacée au bout d'un semestre ; l'emplacement d'un emprunt que tu as pris reste vide 4 à 8 mois (`loan.script.tl:61-76`, `loan.script.tl:150`).
- Au début d'une partie, chacun des quatre emplacements reçoit les valeurs d'un type tiré au hasard, donc la première offre « petite » peut être un gros emprunt ; une fois l'offre renouvelée, chaque emplacement propose son propre type (`loan_util.tl:60-74`, `loan.script.tl:63-75`).

```tip scripts
**Prends le prêt le plus long, puis rembourse tôt.** Les intérêts totaux sont les mêmes quelle que soit la durée, les mensualités sont plus faibles, et Rembourser supprime les intérêts restants.
```

## Bon à savoir

- Prends l'emprunt le **plus long** possible : le total des intérêts est le même, réparti sur plus de mois, et tu peux rembourser plus tôt sans payer le reste.
- Les bâtiments à variantes par époque coûtent ×3 et ×9 aux époques suivantes, et leur entretien continue de monter avec l'année : un entrepôt spécialisé de la dernière époque est une grosse charge fixe.
- Un véhicule rapide et de grande capacité coûte plus cher à faire rouler, mais il transporte aussi davantage : prix et coûts d'exploitation suivent vitesse × capacité, comme le revenu qu'il peut rapporter.

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Le taux d'un emprunt dépend seulement de son type (3–12 %), pas de la difficulté, et il est appliqué une fois au montant, réparti sur les mois de la durée ; rembourser plus tôt supprime les intérêts restants. L'Inflation change seulement les revenus ; l'entretien des bâtiments suit l'année (×1 à ×6) ; prix d'un véhicule = 6 × ses coûts d'exploitation annuels, tous deux tirés de la vitesse et de la capacité.
result: differs
```
