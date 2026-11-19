---
title: Véhicules : état, âge et vitesse de chargement
summary: Ce que signifient les caractéristiques des véhicules, comment fonctionnent l'état et l'âge, ce que font les dépôts et les stations de maintenance, d'où viennent le prix et les coûts d'exploitation, et quand remplacer un véhicule.
domain: vehicles
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-16
game: 40444
fact: 5 | niveaux d'état, de Très mauvais à Très bon, 20 % chacun
fact: 20 % | état qui déclenche l'avertissement État du véhicule
fact: 6 × | le coût d'exploitation annuel de base : le prix d'un véhicule
fact: 4 à 16 | véhicules dans la réserve de maintenance d'un dépôt ou d'une station de maintenance
---

Chaque véhicule a des caractéristiques fixes (vitesse, capacité, vitesse de chargement, prix, coûts d'exploitation, durée de vie) et deux valeurs qui changent : son **état** et son **âge**. L'état baisse pendant qu'il roule et la maintenance le rétablit. L'âge ne fait qu'augmenter.

## Les caractéristiques dans le magasin de véhicules

- Le magasin affiche chaque caractéristique sous forme de barre. La barre utilise une échelle fixe par type de transport, qui change avec l'année (par exemple vitesse de chargement des navires : 10 à 45 à partir de 2003). Elle ne compare pas le véhicule aux autres véhicules (`vehicle_util.tl:210-245`, `vehicle_util.tl:259-268`).
- Pour un train, le magasin affiche la vitesse de chargement **la plus élevée** de toutes ses parties (`vehicle_store_util.tl:333`).
- Un véhicule dont le fichier ne fixe ni vitesse de chargement, ni bruit, ni pollution, ni confort reçoit une valeur calculée à partir de ses autres caractéristiques (année, vitesse, puissance, poids, taille) (`model_metadata_util.lua:395-417`, `vehicle_metadata_util.lua:233-256`). La vitesse de chargement calculée est arrondie à 0,5 et jamais inférieure à 1 (`vehicle_metadata_util.lua:267-269`).

## Quel véhicule charge le plus vite ?

La vitesse de chargement du véhicule n'est que le premier facteur ; le quai et le stock la multiplient (voir [Vitesse de chargement et de déchargement](loading.html)).

| Type de transport | Vitesse de chargement affichée en barre pleine (dernière époque) | Source |
|---|---|---|
| Navires | 10 à 45 (dès 2003) | `vehicle_util.tl:219-223` |
| Véhicules routiers, trams | 0,5 à 10 (dès 1995) | `vehicle_util.tl:232-243` |
| Trains | 0,1 à 10 (dès 1981) | `vehicle_util.tl:226-229` |
| Avions | 1 à 4 (dès 1978) | `vehicle_util.tl:212-216` |

- Les navires ont de loin les vitesses de chargement les plus élevées, les avions l'échelle la plus basse.
- Compare les véhicules d'un même type de transport dans le magasin avec la colonne de vitesse de chargement ; les modèles plus récents sont en général plus haut sur la barre.
- Chaque fret a un facteur de chargement de 0,0625, les passagers 1 (`coal.cargo.lua:29`, `passengers.cargo.lua:23`).

```engine
La façon dont la vitesse de chargement du véhicule, le facteur de chargement du fret et les facteurs du quai et du stock se combinent en temps de chargement réel est calculée par le moteur. Les scripts ne donnent que les entrées.
```

## État

| État | Niveau | Source |
|---|---|---|
| au-dessus de 80 % | **Très bon** | `vehicle_util.tl:159-172` |
| 60–80 % | **Bon** | `vehicle_util.tl:159-172` |
| 40–60 % | **Médiocre** | `vehicle_util.tl:159-172` |
| 20–40 % | **Mauvais** | `vehicle_util.tl:159-172` |
| jusqu'à 20 % | **Très mauvais** | `vehicle_util.tl:159-172` |

- L'état d'un train est la **moyenne** de tous ses wagons et locomotives (`vehicle_util.tl:285-295`).
- Un véhicule usé perd vitesse maximale, puissance et confort, et gagne bruit, pollution et coûts d'exploitation (`vehicle_store_util.tl:236-258`). L'ampleur, et l'état à partir duquel cela commence, sont des valeurs du moteur. La fenêtre du véhicule liste ces pénalités sous **État**.
- La force de ces pénalités est réglée par **Effet de la maintenance des véhicules** (Aucun(e), Bas, Moyen, Élevée, Très élevée) ; avec Aucun(e), l'état n'a aucun effet (`difficulty_util.tl:42`, `mod.script.tl:242-246`, `vehicle_store_util.tl:166-168`, `vehicle_store_util.tl:216-228`). Détails : [Coûts, entretien et emprunts](costs.html).
- À **20 %** ou moins, tu reçois l'avertissement **État du véhicule**. Il reste jusqu'à ce que le véhicule repasse au-dessus de **30 %** (`notifications.script.tl:310-318`).
- Un véhicule cloné est un nouvel achat : état 100 %, nouvelle date d'achat (`manager_window.tl:8744-8748`).

```engine
La vitesse à laquelle l'état baisse, ce que rétablit un passage à une station de maintenance, et l'ampleur de chaque pénalité (getMaintenanceTopSpeedPenalty et les autres) sont des valeurs du moteur. Chaque modèle de véhicule peut aussi fixer sa propre pénalité de vitesse maximale par niveau (`vehicle_store_util.tl:250-253`).
```

## Dépôts et stations de maintenance

Les véhicules sont entretenus par un dépôt ou une station de maintenance proche. Chacun sert un nombre limité de véhicules : sa **Réserve de maintenance**.

| Bâtiment | Réserve de maintenance | Rayon | Véhicules stockés | Source |
|---|---|---|---|---|
| Dépôt ferroviaire | 6 | 800 m | 5 | `rail_depot.script.lua:341-349` |
| Station de maintenance ferroviaire | 12 | 800 m | – | `rail_maint_station.script.lua:151-157` |
| Dépôt routier, dépôt de trams | 12 | 400 m | 10 / 8 | `road_depot.script.lua:189-198`, `tram_depot.script.lua:217-226` |
| Station de maintenance routière | 16 | 600 m | – | `road_maint_station.script.lua:234-240` |
| Dépôt naval | 8 | 1000 m | 5 | `water_depot.script.lua:370-379` |
| Station de maintenance navale | 12 | 1400 m | – | `water_maint_station.script.lua:256-262` |
| Hangar d'aérodrome ou d'aéroport | 16 | 550 m | 5 | `af_hangar.module.lua:272-280`, `ap_hangar.module.lua:455-463` |
| Héliport | 4 | 800 m | 5 | `heliport.script.lua:300-309` |

- La fenêtre du bâtiment affiche « utilisé / réserve » (par exemple 14 / 12) et la liste des véhicules qu'il sert, avec leur état (`entity_window_util.tl:2010-2039`, `maintenance_station_eow.script.tl:188-215`).
- Une réserve plus remplie rend le bâtiment plus bruyant et plus polluant : les émissions augmentent avec la part de la réserve utilisée (`emissions.script.tl:223-234`).
- Une station de maintenance ferroviaire sert deux fois plus de trains qu'un dépôt ferroviaire : 12 contre 6.
- Les stations de maintenance n'achètent ni ne stockent de véhicules, mais leur rayon est souvent plus grand que celui du dépôt : 600 m contre 400 m sur route, 1400 m contre 1000 m pour les navires. Les trams sont entretenus par le dépôt de trams et par la station de maintenance routière ; le dépôt routier n'entretient pas les trams (`tram_depot.script.lua:209`, `tram_depot.script.lua:226`).
- Le wiki officiel conseille des points de passage pour faire passer les véhicules par un bâtiment de maintenance.

```engine
La station à laquelle un véhicule est affecté, ce qui se passe quand plus de véhicules utilisent une station que sa réserve, et le rayon de desserte utilisé sont décidés par le moteur.
```

## Prix et coûts d'exploitation

- Les véhicules du jeu de base n'ont pas de prix fixe : les coûts d'exploitation viennent de la vitesse et de la capacité, et le prix vaut **6 ×** le coût d'exploitation annuel de base, avant les réglages Coût des véhicules et Entretien des véhicules (`model_metadata_util.lua:548-549`). Cela fait exactement 6 ans de coûts d'exploitation seulement si les deux réglages sont égaux. Formule complète : [Coûts, entretien et emprunts](costs.html).
- **Coût des véhicules** fait varier les prix de 50 % à 150 % (`post_run_util.tl:54-81`), et **Entretien des véhicules** fait varier les coûts d'exploitation de la même façon. Mesuré en jeu sur les 921 véhicules d'une sauvegarde, rechargée à 75 %, 100 % et 125 % : les coûts d'exploitation suivent le curseur (médiane ×0,75 et ×1,25 ; les véhicules dont l'état a changé entre deux chargements s'en écartent un peu).
- Un véhicule en mauvais état paie plus de coûts d'exploitation, en plus de la valeur de base (`vehicle_store_util.tl:256-259`).

## Âge et durée de vie

- Chaque modèle a une **durée de vie** (`vehicle_util.tl:31-34`). La colonne **Âge** de la fenêtre de ligne montre l'âge ; son info-bulle montre le temps restant, ou **Durée de vie atteinte** (`line_eow.script.tl:136-150`). La part de la durée de vie dans cette info-bulle affiche **0 %** jusqu'à ce que la durée de vie soit atteinte : le script arrondit la fraction à l'entier inférieur avant de l'afficher (`line_eow.script.tl:142`), alors que la même part est calculée en entier ailleurs (`vehicle_util.tl:311`). Fie-toi plutôt au temps restant.
- Pour un train, c'est la partie **la plus ancienne** qui compte (`vehicle_util.tl:36-52`). Un seul vieux wagon fait apparaître tout le train comme vieux.

```engine
Ce que change le fait d'atteindre la durée de vie (par exemple une perte d'état plus rapide ou une valeur de revente plus basse) n'est pas dans les scripts. Les scripts n'affichent que l'âge et la durée de vie.
```

## Quand remplacer les vieux véhicules ?

1. **L'état reste bas** même avec une station de maintenance proche : le véhicule perd de la vitesse et paie plus de coûts d'exploitation. Vérifie d'abord la réserve de la station : elle est peut-être pleine.
2. **Durée de vie atteinte** dans l'info-bulle Âge : le modèle a dépassé sa durée de vie prévue.
3. **Un meilleur modèle existe** : les véhicules plus rapides ou plus grands coûtent plus cher à exploiter, mais transportent plus (le prix suit vitesse × capacité).
4. Utilise **Remplacer les véhicules** dans le gestionnaire de lignes. Il ouvre le magasin avec une comparaison avec le véhicule actuel (`vehicle_store_window.tl:4997-5032`, `vehicle_store_window.tl:2678`).

```tip scripts
**Des véhicules restent en mauvais état près d'un dépôt ? Ouvre sa fenêtre et regarde « utilisé / pool ».** Un dépôt ferroviaire sert 6 trains, une station de maintenance ferroviaire 12. Ce que fait le moteur des véhicules au-delà du pool n'est pas dans les scripts ; un deuxième bâtiment est la réponse sûre.
```

## Bon à savoir

- Construis assez de capacité de maintenance : un dépôt ferroviaire ne sert que 6 trains.
- Avec **Effet de la maintenance des véhicules** sur Aucun(e), l'état ne compte pas.
- **Envoyer au dépôt** envoie un véhicule au dépôt accessible le plus proche, pas à celui où il a été acheté (wiki officiel).
- [Vehicle Comparison](https://mod.io/g/transportfever3/m/vehicle-comparison) aide à comparer les modèles avant de les remplacer.

```check
official: « This section shows how well the vehicle is maintained and how the maintenance state affects the vehicle properties. » « Loading speed modifies a vehicle's base loading speed which can be seen in the vehicle window or in the vehicle store. » ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles))
scripts: Cinq niveaux d'état de 20 % ; pénalités de vitesse, puissance, confort, émissions et coûts d'exploitation sous 80 %, modulées par Effet de la maintenance des véhicules ; avertissement à 20 %, levé au-dessus de 30 %. Réserve de maintenance de 4 à 16 véhicules par bâtiment. Prix = 6 ans de coûts d'exploitation. Âge d'un train = sa partie la plus ancienne. Les vitesses de chargement manquantes sont calculées à partir des autres caractéristiques, arrondies à 0,5, au moins 1.
result: refines
```
