---
title: Navires et ports
summary: Petits et grands navires, quel port accueille lequel, terminaux et coûts des ports, et la liste de tous les navires avec leur fret, leur capacité et leur vitesse.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
game: 40425
fact: 2 | tailles de navire : petit et grand
fact: 1, 2, 4 | terminaux par port
fact: 27 | navires dans le jeu de base
fact: ×9 | prix et entretien de la variante de port de 1990
---

Chaque navire est **petit** ou **grand**. Un grand navire ne peut accoster qu'à un **grand port** ; un petit navire accoste aux deux. Le guide du jeu le dit aussi : « Notez que les grands navires ne peuvent accoster que dans les grands ports. »

```diagram ship_access
```

## Petits et grands ports

- Deux ports dans le menu de construction : **Petit port de passagers/fret** et **Grand port de passagers/fret**. Les deux acceptent les passagers et tout le fret (`harbor_modular.tl:92`, `harbor_modular.tl:122`).
- Le petit port est construit avec de petits quais, qui n'acceptent que les petits navires (`small_pier.module.lua:7`). Le grand port utilise des quais moyens, qui acceptent les deux tailles (`medium_pier.module.lua:6`, `harbor_modular.script.lua:35-39`).
- **Terminaux** : 1, 2 ou 4, au choix à la construction (`harbor_modular.tl:16`, `harbor_modular.script.lua:33`).
- Un terminal de quai accueille 100 passagers en attente sur un petit quai et 50 sur un quai moyen (`modules.script.lua:872`, `modules.script.lua:1004`).
- Les ports se placent le long d'une côte, sur une eau navigable (`harbor_modular.tl:29`).
- Chaque navire définit sa propre taille dans son fichier de véhicule ; le jeu la convertit en mode petit ou grand navire (`model_metadata_util.lua:1411-1412`).

## Coûts

Il y a une variante de port par époque : 1900, 1950 et 1990 (`harbor_modular.tl:71-73`). Prix et entretien sont multipliés par 3 pour une variante à partir de 1940 et par 9 pour une à partir de 1980 (`harbor_modular.tl:76`) :

| Port | Prix (première variante) | Entretien par an (première variante) | Source |
|---|---|---|---|
| Petit port | 144 000 - 444 000 | 24 000 - 74 000 | `harbor_modular.tl:88-89` |
| Grand port | 228 000 - 678 000 | 38 000 - 113 000 | `harbor_modular.tl:118-119` |

- Les deux valeurs correspondent à la plus petite et à la plus grande configuration.
- L'entretien des ports suit aussi l'année du calendrier, ×1 en 1900 jusqu'à ×6 en 2020, comme les entrepôts et les aéroports ([Coûts, entretien et emprunts](costs.html)).
- Les ports sont bruyants et polluants : 180 à 280 pour les deux ([Pollution et bruit](emission.html)).
- Le prix et les coûts d'exploitation d'un navire sont calculés à partir de sa vitesse et de sa capacité, comme pour les véhicules routiers et les avions ([Coûts, entretien et emprunts](costs.html)).

## Tous les navires

Vitesse en km/h, arrondie. « Fret » liste les classes de fret du fichier de véhicule ; « tout fret » signifie tous les types de fret. La capacité est le total affiché par le magasin de véhicules : la somme des compartiments, chacun compté à sa plus grande configuration de chargement (`vehicle_store_util.tl:70-95`).

| Navire | Années | Taille | Fret | Capacité | Vitesse | Vitesse de chargement |
|---|---|---|---|---|---|---|
| Dunara Castle | 1875-1930 | grand | passagers, tout fret | **160** (2 × 80) | 20 | 20 |
| Chalutier canadien | 1884-1948 | petit | tout fret | 40 | 35 | 10 |
| Waimarie | 1889-1940 | petit | passagers | 80 | 30 | 15 |
| Sydfart | 1900-1930 | petit | liquide, plateau, marchandises, vrac | 80 | 30 | 20 |
| PS Trillium | 1910-1955 | grand | passagers | 200 | 35 | 15 |
| Bateau à roue arrière | 1915-1960 | petit | passagers, tout fret | **120** (2 × 60) | 40 | 10 |
| Terra Nova | 1925-1975 | grand | vrac, plateau, marchandises | **200** (2 × 100) | 45 | 30 |
| Remorqueur-citerne Votrans | 1935-1990 | petit | liquide | 120 | 33 | 20 |
| Remorqueur-cargo Votrans | 1935-1990 | petit | vrac, plateau, marchandises | 120 | 33 | 20 |
| MS Stadt Kiel | 1943-1990 | petit | passagers | 80 | 30 | 20 |
| Borealis | 1948-1994 | petit | tout fret | 60 | 38 | 20 |
| Wopper | 1950-2005 | petit | liquide, plateau, marchandises, vrac | 160 | 30 | 25 |
| Meridian Ferry | 1956-2011 | petit | passagers | 240 | 30 | 15 |
| Cap Arkona | 1965-2010 | grand | passagers | 200 | 40 | 20 |
| Tora Coaster Ship | 1970-2020 | grand | liquide, plateau, marchandises, vrac | 320 | 40 | 25 |
| Aéroglisseur AP1-8 | 1980- | petit | passagers | 240 | 90 | 15 |
| Hercules XI Towboat | 1990- | grand | plateau, marchandises, vrac | **240** (2 × 120) | 32 | 20 |
| Baltica | 1994- | petit | tout fret | 80 | 40 | 20 |
| HADAG Type 2000 | 1995- | petit | passagers | 100 | 35 | 25 |
| Damen Tanker 800 | 1996- | petit | liquide | **320** (2 × 160) | 28 | 30 |
| Damen Fast Ferry | 2003- | grand | passagers | 220 | 75 | 20 |
| Luise Deymann | 2013- | grand | liquide | **480** (2 × 240) | 30 | 35 |
| MS Diamant | 2013- | grand | passagers | 280 | 45 | 35 |
| Virgo Towboat | 2015- | grand | plateau, marchandises, vrac | **320** (2 × 160) | 40 | 15 |
| Aéroglisseur GHL Oita | 2023- | petit | passagers | 320 | 100 | 20 |
| Yara Birkeland | 2030- | grand | plateau, marchandises, vrac | 480 | 42 | 10 |
| Solar Shuttle | 2035- | petit | passagers | 80 | 30 | 30 |

## Bon à savoir

- **Vérifie la taille avant de construire un petit port.** Plusieurs des plus gros cargos (Tora, Virgo, Yara Birkeland) sont grands, et ils n'y accosteront pas.
- **« Aucun parcours pour les grands navires »** est un avertissement à part pour les grands navires : le jeu n'a trouvé aucun trajet sur l'eau utilisable par un grand navire. Quelle eau est ouverte à quelle taille est décidé par le moteur du jeu, pas par les scripts, qui ne font qu'afficher l'avertissement (`vehicle_warning.script.tl:28-36`).
- **Les points de passage des navires** doivent être placés sur l'eau (« Les points de passage maritimes doivent être sur l’eau. »).
- Le dépôt naval et l'atelier d'entretien naval sont des bâtiments distincts ; l'entretien agit dans un rayon autour d'eux ([Véhicules : état, âge et vitesse de chargement](vehicles.html)).

```check
official: "Passenger and cargo ships are available in two sizes: small and large. Large ships can only dock at large harbors, so make sure the harbor matches the size of the ships assigned to the line." (in-game guide "Water Infrastructure")
scripts: Pareil : les petits quais n'acceptent que SMALL_SHIP, les quais moyens SHIP et SMALL_SHIP ; les deux ports acceptent passagers et tout le fret ; 1, 2 ou 4 terminaux ; trois variantes d'époque à ×1 / ×3 / ×9 ; 16 petits et 11 grands navires dans le jeu de base.
result: refines
```
