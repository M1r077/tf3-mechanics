---
title: Pollution et bruit
summary: Ce qui émet du bruit et de la pollution, quand un bâtiment émet plus, comment les villes l'évaluent, et ce que font vraiment le Verdissement de l’industrie et la Station de dépollution.
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
game: 40425
fact: 65–80 dB | bruit en ville : note pleine à 65, nulle à 80
fact: 60–74 | pollution en ville, sur l'échelle logarithmique des scripts (pas un niveau sonore) : note pleine à 60, nulle à 74
fact: −80 % | bruit et pollution d'une industrie verdie
fact: 700 m | portée de la Station de dépollution
---

Les véhicules, voies, rues, gares, dépôts, entrepôts et industries émettent tous du **Bruit** et de la **Pollution**. Deux notes de la ville, **Bruit** et **Pollution**, comparent ce qui atteint la ville à des limites fixes. Une mauvaise note baisse la note **Autorité municipale**, et donc la croissance (voir [Villes](towns.html)).

## Quand un bâtiment émet plus

Un script du jeu règle l'émission de quatre sortes de bâtiments toutes les quelques mises à jour, entre un niveau calme et un niveau chargé (`emissions.script.tl:12-18`) :

| Bâtiment | Émet plus quand | Source |
|---|---|---|
| **Industrie** | elle produit, et encore à chaque boost (fret ou ouvriers) ; quand tous ses stocks de sortie sont pleins à la fois, son niveau est divisé par deux : en production → à l'arrêt, boostée deux fois → en production | `emissions.script.tl:152-194` |
| **Gare** | elle est plus chargée : personnes et fret en attente par rapport à sa capacité | `emissions.script.tl:211-222` |
| **Dépôt**, **station de maintenance** | plus de véhicules utilisent sa maintenance | `emissions.script.tl:223-234` |
| **Entrepôt** | ses stocks sont plus pleins | `emissions.script.tl:237-250` |

- Chaque industrie a ses propres quatre niveaux : à l'arrêt, en production, boostée une fois, boostée deux fois (`industryutil.lua:464-475` ; le défaut 0 / 78 / 84 / 88 ne s'applique qu'à une industrie sans les siens). La plupart émettent un peu même à l'arrêt : une mine de charbon passe de 2 → 10 → 20 → 30 de pollution, ses champs 2 → 30 → 60 → 90 (`coal_mine.con.lua:99-135`, voir [Industries](industries.html)).
- Une industrie dont tous les stocks de sortie sont pleins tombe à la moitié de son niveau (`emissions.script.tl:172-182`) : la desservir augmente sa pollution.
- Les véhicules et les voies émettent aussi ; un véhicule en mauvais état émet plus avec le réglage **Effet de la maintenance des véhicules** (voir [Coûts, entretien et emprunts](costs.html)).

## Ce que montre le menu de construction

| Bâtiment | Bruit | Pollution | Source |
|---|---|---|---|
| Port | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| Aéroport | 8–56 | 80–560 | `airport.tl:28-29` |
| Gare ferroviaire | 25 | 45–350 | `modular_station.con.lua:97-98` |
| Dépôt ferroviaire | 50 | 100 | `rail_depot.con.lua:32-33` |
| Dépôt routier et de tram | 40 | 80 | `road_depot.con.lua:30-31`, `tram_depot.con.lua:32-33` |
| Station souterraine | 40 | 80 | `underground_station.con.lua:75-76` |
| Gare routière (camions et bus) | 1–10 | 12–76 | `modular_terminal.con.lua:67-68`, `modular_terminal.con.lua:121-122` |
| Stations de maintenance | 20 | 40–50 | `road_maint_station.con.lua:30-31`, `rail_maint_station.con.lua:30-31` |
| Entrepôt | 20 | 50 (universel) ou 100 (spécialisé) | `warehouses/warehouse.tl:51`, `warehouses/warehouse.tl:73-74` |

Deux valeurs sont la fourchette affichée par le menu, de la plus basse à la plus haute, comme la fourchette de prix à côté (`construction_desc_react_util.tl:733-746`) ; une seule valeur est un chiffre unique. En fonctionnement, chaque bâtiment émet plus quand il est plus chargé (tableau plus haut). Garde les ports, aéroports et grandes gares de fret loin des maisons.

## Comment une ville l'évalue

| Note | Mesure | Note pleine | Nulle | Source |
|---|---|---|---|---|
| **Bruit** | bruit aux bâtiments de la ville | 65 dB ou moins | 80 dB | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Pollution** | pollution moyenne par case de 16 m de la surface de la ville (surface comptée entre 5 et 10 km²), convertie sur l'échelle logarithmique des scripts (« dB ») | 60 ou moins | 74 | `town_util.tl:413-431`, `emission_config.tl:23-30` |

- Seul le quartier **Résidentiel** souffre du bruit ; les bâtiments commerciaux et industriels non (wiki officiel). La fenêtre d'une maison montre le bruit à son emplacement (`town_building.tl:165-183`).
- La pollution est moyennée sur toute la surface : une source loin du centre pèse moins dans une grande ville que dans une petite.
- Les réglages **Sensibilité au bruit** et **Sensibilité à la pollution** décalent les limites : une sensibilité doublée compte pour +3 dB (`town_util.tl:426-428`, `town_util.tl:439-441`). La pollution utilise la même échelle logarithmique que le bruit (10·log10) : +3 « dB » veut dire deux fois plus de pollution. Ce n'est pas un niveau sonore.

| Niveau | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Source |
|---|---|---|---|---|---|---|---|---|
| Bruit | Désactivé (toujours pleine) | ×¼ | ×½ | ×1 | ×1,4 | ×1,8 | ×3,5 | `difficulty_util.tl:48` |
| Pollution | Désactivé (toujours pleine) | ×¼ | ×½ | ×1 | ×1,7 | ×3 | ×5 | `difficulty_util.tl:49` |

Les préréglages Facile, Moyen, Difficile et Très difficile utilisent les niveaux 3, 4, 5 et 6 (`difficulty_util.tl:114-115`, `difficulty_util.tl:142-143`, `difficulty_util.tl:169-170`, `difficulty_util.tl:196-197`).

## Verdissement de l’industrie

| | | Source |
|---|---|---|
| Effet | bruit et pollution de l'industrie ×0,2 (−80 %), pour toujours | `emission_config.tl:32`, `emissions.script.tl:184-192` |
| Utilisations | une au rang d'entreprise 3, 6, 9, 12 et 15 | `industry_greenify_tool.script.tl:99-104` |
| Limite | une fois par industrie ; un second essai ne consomme pas de permis | `company.script.tl:489-494` |

- L'effet est lié à cette version de l'industrie : quand l'industrie est reconstruite, il est perdu (`emissions.script.tl:187-190`).
- Meilleur usage : l'industrie la plus active juste à côté d'une ville, car une industrie boostée émet le plus.

## La Station de dépollution

Un avantage d'entreprise qui retire la pollution autour de lui.

| | | Source |
|---|---|---|
| Prix | 100 000 000 | `pollution_cleanup_facility.script.lua:560` |
| Entretien par an | 10 000 000 | `pollution_cleanup_facility.script.lua:561` |
| Disponible | 15 au rang d'entreprise 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Besoins | **Machines** : 8 par cycle, deux cycles par an ; 20 ouvriers | `pollution_cleanup_facility.con.lua:43-60` |
| Portée | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| État | Pollution | Bruit | Source |
|---|---|---|---|
| à l'arrêt (sans machines) | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| en marche | −10 000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| boostée une fois | −20 000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| boostée deux fois | −40 000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

Le dernier niveau demande une règle de boost, que la Station de dépollution n'a pas : avec les ouvriers, elle atteint −20 000 (`pollution_cleanup_facility.con.lua:51-58`, `emissions.script.tl:158-166`).

- Sans machines, elle ne fait presque rien : il faut l'approvisionner comme une industrie.
- Elle est bruyante : construis-la hors du quartier résidentiel, à moins de 700 m de la zone polluée.
- Son facteur de boost par les ouvriers est ×2 (`pollution_cleanup_facility.script.lua:549`). Voir [Ouvriers](workers.html).

## Bon à savoir

- Ouvre la fenêtre de la ville ou les calques bruit et pollution pour voir la note et les points chauds.
- Quand tous les stocks de sortie d'une industrie sont pleins, son niveau d'émission est divisé par deux, mais tu perds son fret : mieux vaut éloigner la ville qu'affamer l'industrie.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) et [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) aident à trouver les gares les plus chargées.

```engine
Le moteur calcule les cartes de bruit et de pollution, la diffusion des valeurs, les émissions des véhicules et des voies, et le moment où une industrie est reconstruite. Le script règle seulement le niveau de chaque bâtiment et les limites des villes.
```

```check
official: « Noise reflects noise levels in residential areas. » « Pollution reflects pollution levels across the town area. » Le quartier résidentiel « is sensitive to noise » ; le quartier commercial « is robust against the influence of noise ». ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Note de bruit 65 → 80 dB, pollution 60 → 74 dB moyennée sur 5–10 km² ; la sensibilité ajoute 10·log10 dB ; industries, gares, dépôts et entrepôts émettent plus quand ils sont chargés ; quand tous les stocks de sortie sont pleins, le niveau d'émission d'une industrie est divisé par deux ; verdissement −80 % une fois par industrie ; la Station de dépollution retire jusqu'à 20 000 de pollution (40 000 est défini mais demande une règle de boost) dans un rayon de 700 m et a besoin de machines.
result: refines
```
