---
title: Rues, voies, ponts et signaux
summary: Vitesse, prix et entretien de chaque type de voie et de rue, ce que coûtent et permettent ponts, tunnels, passages à niveau et signaux, ce que changent vraiment allées d'arbres et écrans antibruit, et où les dépôts sont expliqués.
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40444
fact: 100 / 160 / 350 km/h | voie simple, standard et à grande vitesse
fact: ×9 | prix et entretien d'une voie à grande vitesse par rapport à une voie simple
fact: +30 % | prix de la caténaire sur une voie
fact: -65 % | bruit d'une rue ou d'une voie avec un écran antibruit
---

Chaque type de rue et de voie a une vitesse maximale, un prix par mètre et un entretien par mètre et par an, tous écrits dans son fichier. Les ponts, les passages à niveau et certaines décorations de rue ajoutent leur propre limite de vitesse. Les coûts ci-dessous sont à **Coût des infrastructures** et **Entretien des infrastructures** 100 % (voir [Coûts, entretien et emprunts](costs.html)).

## Voies

| Voie | Dès | Vitesse max | Construction par km | Entretien par km et par an | Source |
|---|---|---|---|---|---|
| Voies simples | début | 100 km/h | 60 000 | 10 000 | `simple.street_template.lua:9`, `simple.street_template.lua:28`, `simple.street_template.lua:33` |
| Voies standards | 1930 | 160 km/h | 180 000 | 30 000 | `standard.street_template.lua:4`, `standard.street_template.lua:11`, `standard.street_template.lua:30`, `standard.street_template.lua:35` |
| Voies à grande vitesse | 1980 | 350 km/h | 540 000 | 90 000 | `high_speed.street_template.lua:4`, `high_speed.street_template.lua:11`, `high_speed.street_template.lua:30`, `high_speed.street_template.lua:35` |

- La **caténaire** coûte **30 %** de plus que la voie (`mod.script.tl:24-25`). Elle est disponible dès 1921 sur la voie simple et dès le début de chaque type plus récent (`simple_catenary.street_template.lua:4`). Elle ne coûte rien de plus par an dans les fichiers : la variante électrique a le même entretien (`simple_catenary.street_template.lua:34`).
- Les trois types permettent la même pente et les mêmes courbes : **8,5 %** à la construction (le curseur Inclinaison va jusque-là), 13 % au plus pour la forme de la voie, et un rayon de courbe de 55 m à la construction, 40 m au minimum (`standard.street_template.lua:36-37`, `standard.street_template.lua:48-49`, `construction_react_util.tl:241-242`, `construction_react_util.tl:1824`).
- La pollution de la voie elle-même augmente avec son type : 2, 4 et 6 (`simple.street_template.lua:18`, `standard.street_template.lua:20`, `high_speed.street_template.lua:20`).

```engine
De combien une courbe réduit la vitesse d'un train (les speedCoeffs de chaque type de voie) et quelle vitesse l'outil de construction affiche pour une courbe sont calculés par le moteur.
```

```tip scripts
La voie à grande vitesse coûte 9 fois la voie simple, à la construction et chaque année. Pose-la seulement là où les trains roulent vraiment à plus de 160 km/h ; la voie standard suffit ailleurs, et la voie simple pour les embranchements de fret lents.
```

## Rues

| Rue | Années | Vitesse max | Construction par km | Entretien par km et par an | Source |
|---|---|---|---|---|---|
| Rue étroite (ancienne) | jusqu'en 1940 | 20 km/h | 36 000 | 6 000 | `town_old_xsmall.street_template.lua:4-5`, `town_old_xsmall.street_template.lua:8`, `town_old_xsmall.street_template.lua:27`, `town_old_xsmall.street_template.lua:56` |
| Petite rue (ancienne) | jusqu'en 1940 | 40 km/h | 60 000 | 10 000 | `town_old_small.street_template.lua:8`, `town_old_small.street_template.lua:27`, `town_old_small.street_template.lua:56` |
| Grande rue (ancienne) | jusqu'en 1940 | 60 km/h | 180 000 | 30 000 | `town_old_large.street_template.lua:8`, `town_old_large.street_template.lua:27`, `town_old_large.street_template.lua:88` |
| Rue étroite (moderne) | dès 1940 | 30 km/h | 120 000 | 20 000 | `town_new_xsmall.street_template.lua:4`, `town_new_xsmall.street_template.lua:11`, `town_new_xsmall.street_template.lua:30`, `town_new_xsmall.street_template.lua:59` |
| Petite rue (moderne) | dès 1940 | 50 km/h | 180 000 | 30 000 | `town_new_small.street_template.lua:11`, `town_new_small.street_template.lua:30`, `town_new_small.street_template.lua:59` |
| Rue moyennes (moderne) | dès 1940 | 50 km/h | 360 000 | 60 000 | `town_new_medium.street_template.lua:11`, `town_new_medium.street_template.lua:30`, `town_new_medium.street_template.lua:75` |
| Grande rue (moderne) | dès 1940 | 60 km/h | 540 000 | 90 000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:30`, `town_new_large.street_template.lua:91` |
| Petite route de campagne (ancienne) | jusqu'en 1940 | 60 km/h | 60 000 | 10 000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:29`, `country_old_small.street_template.lua:58` |
| Petite route de campagne (moderne) | dès 1940 | 80 km/h | 180 000 | 30 000 | `country_new_small.street_template.lua:10`, `country_new_small.street_template.lua:31`, `country_new_small.street_template.lua:60` |
| Autoroute à une voie | dès 1940 | 100 km/h | 180 000 | 30 000 | `highway_new_small.street_template.lua:10`, `highway_new_small.street_template.lua:32`, `highway_new_small.street_template.lua:53` |
| Autoroute à deux voies | dès 1940 | 120 km/h | 360 000 | 60 000 | `highway_new_medium.street_template.lua:10`, `highway_new_medium.street_template.lua:32`, `highway_new_medium.street_template.lua:61` |
| Autoroute à trois voies | dès 1940 | 120 km/h | 540 000 | 90 000 | `highway_new_large.street_template.lua:10`, `highway_new_large.street_template.lua:32`, `highway_new_large.street_template.lua:69` |
| Voies de tramway (anciennes) | jusqu'en 1910 | 40 km/h | 36 000 | 6 000 | `tram_old.street_template.lua:4-5`, `tram_old.street_template.lua:8`, `tram_old.street_template.lua:27`, `tram_old.street_template.lua:40` |
| Voies de tramway (modernes) | dès 1925 | 100 km/h | 120 000 | 20 000 | `tram_new.street_template.lua:4`, `tram_new.street_template.lua:9`, `tram_new.street_template.lua:29`, `tram_new.street_template.lua:42` |

- Le **changement de 1940** rend les rues de ville 10 km/h plus rapides mais **trois fois** plus chères, à la construction et chaque année : une petite rue passe de 60 000 à 180 000 par km.
- Les variantes moyenne et grande des routes de campagne coûtent 2 et 3 fois la petite, à la même vitesse (`country_new_large.street_template.lua:10`, `country_new_large.street_template.lua:31`).
- Ajouts à une rue : une **voie de bus** +10 %, une **voie de tram** +20 %, une **voie de tram électrique** +40 % du prix de la rue (`mod.script.tl:24-28`).
- En général le joueur ne possède pas les rues, même celles qu'il a construites ; les outils de rue peuvent changer le propriétaire d'une rue (wiki officiel). Qui paie l'entretien d'une rue est décidé par le moteur.

## Allées d'arbres et écrans antibruit

| Outil | Bruit | Pollution | Vitesse max | Où | Source |
|---|---|---|---|---|---|
| Outil pour allée d’arbres (arbres) | -10 % | -50 % | **-25 %** | rues avec trottoir, pas sur les ponts ni dans les tunnels | `alley.edge.lua:39-40`, `alley.edge.lua:53-56` |
| Outil d'écran antibruit | -65 % | aucun changement | aucun changement | rues et voies, pas dans les tunnels | `barrier_b.edge.lua:43`, `barrier_b.edge.lua:47`, `barrier_track_b.edge.lua:43` |

- Les deux coûtent 100 et 10 par an dans leurs fichiers, comme une rue par mètre (`alley.edge.lua:8`, `alley.edge.lua:12`, `barrier_b.edge.lua:7`, `barrier_b.edge.lua:11`).
- Les types de rue « avec arbres » et « avec écrans » du menu de construction sont les mêmes rues avec ces décorations déjà posées (`town_new_medium_trees.street_template.lua:12-14`). Le menu de construction additionne leurs effets (`construction_react_util.tl:2119-2142`).
- Une rue avec arbres est donc **un quart plus lente** : une rue moyenne moderne avec arbres permet environ 38 km/h au lieu de 50.

```tip scripts
Contre le bruit, utilise l'écran antibruit : -65 % et aucune perte de vitesse. Les arbres sont l'outil contre la pollution (-50 %), mais ils ralentissent la rue d'un quart.
```

Comment les villes jugent le bruit et la pollution : [Pollution et bruit](emission.html).

## Ponts et tunnels

| Pont | Années | Vitesse max | Pour | Prix de base | Source |
|---|---|---|---|---|---|
| Pont en pierre | dès le début | 90 km/h | voies, rues | 200 | `stone.bridge.lua:169-170`, `stone.bridge.lua:181-183`, `stone.bridge.lua:193` |
| Pont à chevalets | jusqu'en 1970 | 60 km/h | un type pour les voies, un pour les rues | 100 | `trestle.bridge.lua:200-201`, `trestle.bridge.lua:212-214`, `trestle.bridge.lua:226`, `trestle_s.bridge.lua:212` |
| Pont en acier | dès 1940 | 140 km/h | voies, rues | 200 | `steel.bridge.lua:243`, `steel.bridge.lua:259`, `steel.bridge.lua:269` |
| Pont suspendu | dès 1940 | 180 km/h | voies, rues | 600 | `suspension.bridge.lua:277`, `suspension.bridge.lua:294`, `suspension.bridge.lua:304` |
| Pont en béton | dès 1970 | 280 km/h | voies, rues | 200 | `concrete.bridge.lua:162`, `concrete.bridge.lua:176`, `concrete.bridge.lua:187` |
| Pont à haubans | dès 2000 | 220 km/h | voies, rues | 750 | `cable.bridge.lua:214`, `cable.bridge.lua:231`, `cable.bridge.lua:240` |
| Pont bow-string | dès 2010 | 350 km/h | voies, rues | 650 | `tarch.bridge.lua:253`, `tarch.bridge.lua:270`, `tarch.bridge.lua:280` |

- La limite du pont s'applique **en plus** de celle de la voie : une ligne à grande vitesse sur un pont en acier y roule à 140 km/h. Avant 1970 aucun pont ne permet plus de 180 km/h, avant 2010 aucun ne permet 350 km/h.
- Les **tunnels** (Tunnel rocheux, Tunnel en béton dès 1970) n'ont **aucune limite de vitesse** dans leurs fichiers, et le même prix de base de 600 (`tunnel_a.tunnel.lua:187-188`, `tunnel_a_car.tunnel.lua:185`, `tunnel_b.tunnel.lua:191-194`).
- Les prix des ponts et tunnels suivent Coût des infrastructures (`post_run_util.tl:50-51`).

```engine
Le prix de base d'un pont ou d'un tunnel est converti en prix par mètre par le moteur, avec la hauteur ou la profondeur (costFactors) ; le wiki officiel dit qu'il dépend de la longueur et de la hauteur au-dessus du sol ou de la profondeur. Le même prix de base peut donc donner des factures très différentes. Les tunnels coûtent de la Réputation auprès de la ville (voir [Réputation des villes](reputation.html)).
```

```tip scripts
Pour une ligne rapide qui traverse une vallée avant 1970, le pont suspendu (180 km/h) est le seul pont plus rapide que 140 km/h ; un tunnel n'a aucune limite.
```

## Passages à niveau et signaux

| Quoi | Années | Vitesse max de la voie | Prix | Source |
|---|---|---|---|---|
| Passage à niveau simple | 1850 - 1925 | 120 km/h | 4 000 | `era_a_eu.rcr.lua:14-17`, `era_a_eu.rcr.lua:26` |
| Passage à niveau à demi-barrières | 1925 - 1975 | 160 km/h | 16 000 | `era_b_eu.rcr.lua:15-18`, `era_b_eu.rcr.lua:27` |
| Passage à niveau à demi-barrières moderne | dès 1975 | 160 km/h | 16 000 | `era_c_eu.rcr.lua:15-17`, `era_c_eu.rcr.lua:26` |
| Signal d’itinéraire (sémaphore jusqu'en 1950, lumineux dès 1950) | toutes | - | 9 000, entretien 1 500 par an | `signal_path_a.con.lua:4-5`, `signal_path_a.con.lua:10-11`, `signal_path_c.con.lua:4-5` |

- Un passage à niveau limite la voie à 160 km/h au plus : les lignes à grande vitesse ont besoin de ponts ou de tunnels pour franchir les rues.
- Chaque signal peut être réglé en **Sens unique** (`signal_path_a.con.lua:51-52`). La façon dont les signaux divisent la voie en cantons est expliquée dans la page Railway Signals du wiki officiel.

## Dépôts et ateliers d'entretien

Ce que coûtent les dépôts et les ateliers d'entretien, combien de véhicules ils servent et dans quel rayon : [Véhicules](vehicles.html) et [Coûts, entretien et emprunts](costs.html).

## Bon à savoir

- Avant 1940, améliorer les rues de ville coûte peu ; après 1940 chaque rue de ville neuve ou reconstruite coûte trois fois plus et trois fois plus d'entretien.
- Sur une ligne rapide, vérifie chaque pont et chaque passage à niveau : le plus lent fixe la vitesse à cet endroit.
- La vitesse ne rapporte que si elle donne plus de trajets (voir [Pourquoi est-ce que je perds de l'argent ?](money.html)).

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: Mêmes vitesses que les tableaux officiels pour les voies, les rues et les ponts. Dans les fichiers, les limites des ponts s'appliquent aussi aux rues, les tunnels n'en ont aucune, les passages à niveau limitent les voies à 120 ou 160 km/h, les arbres ralentissent une rue de 25 % et réduisent la pollution de 50 % mais le bruit de seulement 10 %, tandis que les écrans antibruit réduisent le bruit de 65 % sans ralentir.
result: refines
```
