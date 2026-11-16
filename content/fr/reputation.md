---
title: Réputation des villes
summary: Ce qui fait baisser la note Réputation d'une ville, à quelle vitesse elle revient, ce que font vraiment les célébrations et les campagnes marketing, et pourquoi une route coupée entre deux villes coûte si cher.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
game: 40425
fact: −33 % | par connexion principale interrompue vers une autre ville
fact: ≈ 67 % | récupérés par an au calendrier ×1 (≈ 200 % pendant une campagne marketing) ; la fenêtre de la ville affiche 33 % et 100 %
fact: 0,25 % | par arbre adulte supprimé près de la ville
fact: 2 M m³ | de travaux de terrain coûtent toute la réputation
---

La **Réputation** est l'une des six notes de la fenêtre de la ville, et l'Autorité municipale prend la **plus basse** d'entre elles (voir [Croissance des villes](towns.html)). Elle part de 100 % et ne baisse qu'à cause de ce que **tu** construis ou rates : travaux de terrain, arbres et roches supprimés, bâtiments de la ville démolis, contrats échoués et connexions principales coupées. Le temps, les célébrations et les campagnes marketing la font remonter.

```diagram rep_recovery
```

## Ce qui la fait baisser

Chaque construction que tu valides est vérifiée avant d'être appliquée ; le coût est compté à la ville concernée (`towns.script.tl:271-291`, `town_util.tl:1062-1080`). Seules tes propres constructions comptent, et rien ne compte dans l'éditeur de cartes (`town_util.tl:1078-1080`, `towns.script.tl:58`).

| Raison dans la fenêtre de la ville | Ce qui coûte de la réputation | Source |
|---|---|---|
| **Arbres supprimés** | 0,25 % par arbre, × le facteur de distance à la ville la plus proche, × la taille de l'arbre (les petits arbres comptent moins) | `town_util.tl:1144-1150`, `town_util.tl:865`, `model_metadata_util.lua:655-680` |
| **Roches supprimées** | 0,25 % par roche, × le facteur de distance | `town_util.tl:1148-1149`, `town_util.tl:884-885` |
| **Terrassement** | 0,00005 % par m³ de terrain relevé **ou** abaissé : 2 millions de m³ = 100 %. Le terrain modelé par les voies, routes et bâtiments compte aussi (réduit à partir de 10 000 m², de moitié à 50 000 m² ou plus), ainsi que le volume net des nouveaux tunnels | `town_util.tl:873-886`, `town_util.tl:1245-1269`, `town_util.tl:1403-1436` |
| **Bâtiments démolis** | 100 % pour 40,5 % de la capacité d'un quartier supprimée (logements, commerces ou emplois de cette ville) | `town_util.tl:867-869`, `town_util.tl:1165-1184` |
| **Contrat échoué** | Approvisionner la ville : de 10 % jusqu'à 60–90 % (selon le risque) ; Relier des villes : 10–100 % × le facteur de distance, dans les **deux** villes (voir [Contrats](subsidies.html)) | `deliver_cargo_town.script.tl:202-210`, `deliver_passengers.script.tl:113-114`, `towns.script.tl:331-333` |
| **Connexions principales interrompues** | **1/3** par autre ville dont la connexion principale est coupée ou trop longue | `town_util.tl:376-394`, `town_util.tl:1608` |

- Chaque raison est plafonnée à 100 % (`town_util.tl:1611-1620`).
- Pendant la construction, l'infobulle affiche **Réputation : −x %**, avec le nombre de villes touchées quand il y en a plusieurs (`construction_react_util.tl:3818-3864`). Elle compte le coût depuis une note pleine.
- Planter des arbres ou poser des roches annule seulement **Arbres supprimés** ou **Roches supprimées**, au même 0,25 % pièce. Cela ne fait rien pour les autres raisons, ni à réputation pleine (`town_util.tl:1228-1238`, `town_util.tl:1630-1641`).
- Le réglage Réputation d'une nouvelle partie vaut **Désactivé** ou **Activé** (Activé dans tous les préréglages). Désactivé veut dire une note pleine, toujours (`difficulty_util.tl:44`, `difficulty_util.tl:110`, `town_util.tl:396-399`).

```engine
La vitesse à laquelle le facteur de distance baisse entre une ville et un arbre supprimé, le volume de terrain attribué à chaque ville, les arbres supprimés automatiquement par une voie ou une route, et les routes qui comptent comme connexion principale d'une ville (et quand un trajet est « trop long ») sont des valeurs du moteur (getImpactFromDistance, getTerrainBrushVolumeImpact, getTerrainAlignmentImpact, getAutoRemovalEntityImpact, getTownProblems).
```

## Connexions principales coupées

Une connexion principale compte comme coupée quand le jeu affiche **La liaison routière entre les villes a été interrompue** ou **Le temps de trajet entre les villes est trop long** (`town_util.tl:378-380`, `town_warning.script.tl:7-22`). Chaque autre ville concernée coûte 1/3, et la note le montre **tout de suite** (`town_util.tl:401-403`) :

| Connexions coupées | Réputation au plus | Note | Source |
|---|---|---|---|
| 1 | 67 % | Très bon | `town_util.tl:983-985` |
| 2 | 33 % | Médiocre | `town_util.tl:983-985` |
| 3 | 0 % | Très insuffisant : la ville arrête de grandir | `town_util.tl:607-633` |

- Tant que la coupure dure, la pénalité est aussi inscrite dans le score enregistré, pas à pas, sur 3 mois (`towns.script.tl:137-145`). Une fois la route réparée, cette partie enregistrée ne revient qu'à la vitesse normale : une longue coupure continue de coûter de la réputation pendant un moment.
- 67 % est pile à la limite de Très bon : la moindre autre perte fait passer la ville à Bon.

```tip scripts
**Construis la nouvelle route avant de supprimer l'ancienne.** Chaque connexion principale coupée coûte un tiers de la réputation d'un coup, et plus la coupure dure, plus le retour est long.
```

## Comment elle revient

- **Toute seule** : un niveau (1/6) tous les 3 mois de temps de jeu (360 s), tous les mois (120 s) pendant une campagne marketing (`towns.script.tl:121-135`). Au calendrier ×1, cela fait environ **67 %** par an, **200 %** avec une campagne : de 0 % à plein en 1,5 an environ. La fenêtre de la ville affiche **Récupération annuelle** 33 % et 100 % : des textes fixes, la moitié de la vitesse réelle (`town_react_util.tl:1066`). Mesuré sur une ville de test : un niveau toutes les 358 s, toutes les 120 s avec une campagne.
- La récupération répartit le gain sur toutes les raisons ; elle ne dépasse jamais les connexions coupées encore ouvertes (`town_util.tl:1649-1687`).
- Les **célébrations** ajoutent **+50 %** pour le premier passager qui monte dans une de tes lignes dans une ville, +50 % pour le premier fret livré à une ville, +50 % à chaque niveau gagné par la ville, et +20 % à la ville la plus proche pour le premier fret livré à chaque industrie (`celebrations.script.tl:181-273`). Le message se termine alors par **Réputation de la ville améliorée.** ou **Réputation améliorée à …** (`celebration_react_util.tl:63-75`). Elles ne comptent que si la réputation est sous ce que permettent encore les liaisons principales coupées (pleine moins 1/3 par liaison coupée) et si le réglage Réputation est sur Activé, et pas dans les missions de campagne (`celebrations.script.tl:79-93`, `celebrations.script.tl:140-142`).
- **Approvisionner la ville** peut donner +5 % à +20 % × le facteur de risque à l'acceptation (`deliver_cargo_town.script.tl:195-199`). Comme tout gain, cela retire seulement des pertes existantes (`towns.script.tl:324-330`).

## Campagne marketing

| Quoi | Valeur | Source |
|---|---|---|
| Prix | 10 M × facteur d'année : 4 M en 1900 jusqu'à 25 M en 2020, arrondi à 1 M | `marketing_campaign_tool.script.tl:9-14` |
| Demande | un permis des atouts de l'entreprise | `marketing_campaign_tool.script.tl:83-95`, `company.script.tl:416-423` |
| Durée | un an | `marketing_campaign_tool.script.tl:136` |
| Réputation | récupération ×3 (≈ 200 % par an, la fenêtre affiche 100 %) ; **aucun** gain immédiat | `towns.script.tl:126`, `town_util.tl:915-925` |
| Habitants | tes lignes dans cette ville comptent comme deux fois moins coûteuses quand les habitants choisissent comment se déplacer | `marketing_campaign_tool.script.tl:137`, `towns.script.tl:376-398` |

```engine
Le script compte 360 secondes de temps de jeu par niveau (120 avec une campagne), avec un mois de 30 jours de 4 secondes. La récupération suit le temps de jeu : avec un calendrier plus lent, une année du calendrier dure plus longtemps, donc il revient davantage par année affichée. À quel point le coût de ligne divisé par deux pousse les habitants vers tes lignes dépend du choix d'itinéraire du moteur.
```

## Bon à savoir

- Regarde l'infobulle de construction : si elle affiche **Réputation : −x %**, un tunnel ou un tracé plus doux coûte souvent moins que la réputation.
- Ne laisse jamais coupée une route principale entre deux villes : chacune fait −33 % tout de suite, et trois coupures arrêtent la ville.
- Une campagne marketing à réputation pleine aide seulement tes lignes, pas la note. Lance-la juste après de gros travaux, quand la récupération a quelque chose à rattraper.
- Le bonus **Récupération de réputation** du grand module du siège social (+1 %) s'affiche dans l'onglet Bonus, mais dans les scripts il change seulement une valeur qu'aucune note ne lit (`hq_module_l.module.lua:171`, `towns.script.tl:157`, `town_util.tl:829`, `town_util.tl:857`).
- Le succès **C'est pas moi** demande une ville à 0 % de réputation en partie libre (`achievements.script.tl:261-267`).

```check
official: "Reputation reflects how the town and surrounding nature are treated. Landscaping, removing town buildings and breaking main connections to other towns can lower it, while celebrations and marketing campaigns can improve it. Reputation lost by removing trees can be recovered by planting new ones." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Mêmes causes, plus les roches supprimées, les tunnels, le terrain des voies et routes, et les contrats échoués. Chaque connexion principale coupée ou trop longue coûte 1/3 tout de suite ; trois arrêtent la ville. La récupération est d'environ 67 % par an toute seule et d'environ 200 % avec une campagne marketing, le double de ce qu'affiche la fenêtre de la ville (33 % et 100 %) ; la campagne ne donne rien tout de suite. Planter des arbres annule seulement la perte due aux arbres. Le bonus Récupération de réputation du siège social n'a aucun effet dans les scripts.
result: differs
```
