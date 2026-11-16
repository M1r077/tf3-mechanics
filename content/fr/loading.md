---
title: Vitesse de chargement et de déchargement
summary: Ce qui fait qu'un véhicule charge vite ou lentement à un arrêt : le véhicule, les sections du quai et le stock qui donne ou reçoit le fret.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-15
fact: ×2 | section de quai spécialisée
fact: ×0,25 | mauvaise section ou train trop long
fact: ×4 | au mieux : quai et entrepôt spécialisés
---

Le temps qu'un véhicule passe à charger ou décharger, c'est sa propre vitesse de chargement multipliée par deux facteurs : un pour le **quai**, un pour le **stock** de l'autre côté (entrepôt, industrie, ville).

```diagram loading_factors
```

## 1. Le véhicule

Chaque véhicule a une vitesse de chargement de base, affichée dans le magasin de véhicules et la fenêtre du véhicule (« 2.0x »). Tout ce qui suit la multiplie.

## 2. Le facteur du quai

Pour le jeu, un quai n'est pas une rangée de modules : c'est une **liste de sections, une par classe de fret**, avec les longueurs de tous les modules de cette classe additionnées.

```diagram loading_sections
```

| Wagons… | Facteur | Source |
|---|---|---|
| sur une section de leur classe (wagons vrac, section vrac) | **×2** | `modular_station.script.lua:1042` |
| sur une section universelle | ×1 | `modular_station.script.lua:1042` |
| sans aucune section de leur classe sur le quai | **×0,25** | `cargo_react_util.tl:60` |
| au-delà de la longueur du quai (train trop long) | **×0,25** | `cargo_react_util.tl:61` |

- Le facteur est un **mélange selon la part du train** : si 3/4 des wagons correspondent et 1/4 non, le facteur vaut ¾ × 2 + ¼ × 0,25 ≈ ×1,56 (`cargo_react_util.tl:63-70`, le même découpage que le jeu affiche comme « Terminal partiellement spécialisé »).
- **L'endroit** où les wagons s'arrêtent sur le quai ne compte pas, seules les longueurs additionnées comptent (mesuré en jeu).
- Route : les terminaux de camions spécialisés donnent ×2 (`modular_terminal.script.lua:2956`) ; les petits arrêts de rue sont toujours à ×1 (`small_stops.script.lua:19`).
- Les quais de passagers sont à ×1.

## 3. Le facteur du stock

Au déchargement, chaque unité va à un destinataire : un module d'entrepôt, une industrie ou un bâtiment de ville. Le stock du destinataire a son propre facteur.

| Destinataire | Facteur | Source |
|---|---|---|
| module d'entrepôt **spécialisé** (liquide, vrac, plateau, marchandises) | **×2** | `modules.script.lua:120`, `warehouse.script.lua:297-314` |
| entrepôt **universel** | ×1 | `warehouse.script.lua:272-285` |
| industrie | ×1 | mesuré en jeu |

- Chaque module d'entrepôt demande ×2, mais les modules universels ne font qu'ajouter de la capacité à **un stock universel commun**, créé à ×1. Seuls les modules spécialisés ont leur propre stock à ×2.
- L'info-bulle du jeu appelle ce facteur « Entrepôt spécialisé : +100 % » (`cargo_react_util.tl:51-54`).
- Pendant un même déchargement, le jeu sert les destinataires **à tour de rôle** : la vitesse change pendant que le train décharge quand une partie du fret va à un entrepôt et une partie à une industrie (mesuré en jeu).

```engine
Le choix du destinataire de chaque unité et la multiplication finale se font dans le moteur. Les facteurs ci-dessus sont les données que les scripts lui donnent ; le résultat a été vérifié avec les valeurs exposées par le moteur (sonde de [Platform Details](https://mod.io/g/transportfever3/m/platform-details), octobre 2026).
```

## Ce que le jeu affiche

- L'indicateur de chargement est dessiné **accéléré** au-dessus de ×1,5 et **ralenti** en dessous de ×0,75 (`cargo_react_util.tl:119-122`).
- Survole-le : l'info-bulle liste « Terminal spécialisé », « Spécialisations incompatibles », « Terminal trop court » et « Entrepôt spécialisé », chacun avec son pourcentage (`cargo_react_util.tl:76-99`).

## Exemple

Un train de 8 wagons vrac, long de 160 m, qui décharge du charbon.

| Gare | Quai | Destinataire | Facteur |
|---|---|---|---|
| quai universel 160 m | ×1 | aciérie | **×1** |
| quai vrac 160 m | ×2 | aciérie | **×2** |
| quai vrac 160 m | ×2 | entrepôt vrac spécialisé | **×4** |
| quai vrac 160 m | ×2 | entrepôt universel | **×2** |
| quai universel 120 m (train trop long de 40 m) | ¾ × 1 + ¼ × 0,25 ≈ ×0,81 | aciérie | **×0,81** |

## Où le fret est déchargé

Chaque arrêt d'une ligne a une liste **Charge**, dans la fenêtre « Filtre de fret » de l'arrêt. À l'arrêt, le véhicule garde à bord le fret de cette liste ; le reste est déchargé dans tout stock de la zone de desserte qui le prend, entrepôt compris (mesuré en jeu).

- C'est ainsi qu'un train se vide dans un entrepôt au milieu de sa ligne. En jeu : à un arrêt à côté d'un entrepôt, avec seulement du plastique dans sa liste, les outils à bord sont partis dans l'entrepôt, alors qu'il était presque plein.
- Un quai voyageurs ne fait pas de transfert de fret : le fret y reste à bord (mesuré en jeu).
- Pour garder le fret à bord, ajoute-le à la liste Charge de cet arrêt.

```tip
**Du fret disparaît à un arrêt près d'un entrepôt ? Ajoute-le à la liste Charge de cet arrêt.** Tout ce qui n'est pas dans la liste est déchargé dans un stock à portée, et l'entrepôt ne paie rien.
```

| Option de « Filtre de fret » | Effet | Source |
|---|---|---|
| « Forcer le déchargement de tout le fret à l’arrivée » | décharge dans les stocks compatibles même pleins ; ce qui ne rentre pas est détruit. Désactivée pour un nouvel arrêt. | `cargofilter_window.tl:757`, `line_util.tl:476` |
| « Détruire le fret à l’arrivée lorsque la configuration change » | détruit le fret à bord quand un autre fret attend d'être chargé à cet arrêt | `cargofilter_window.tl:767` |
| « Remplacer par un fret plus récent si disponible » | détruit le fret revenu à l'arrêt où il a été chargé, quand du fret plus récent du même type attend | `cargofilter_window.tl:778` |

- Quand la première option est désactivée, l'icône du fret affiche « ≤ » et l'info-bulle « Décharger uniquement si les stocks ont de la capacité » (`cargofilter_window.tl:124`, `cargofilter_window.tl:158`).

## Plusieurs frets sur une ligne

- La liste **Charge** d'un arrêt est un oui/non par type de fret, **sans ordre** : le joueur ne peut pas choisir quel fret est chargé en premier. Les icônes sont simplement dessinées dans l'ordre des frets du jeu (`line_util.tl:471-475`, `line_util.tl:510`, `cargofilter_window.tl:533-535`).
- Un wagon ou un camion qui prend plusieurs frets a, par compartiment, plusieurs **configurations de chargement** ; la capacité du compartiment est la plus grande d'entre elles, pas leur somme (`model_metadata_util.lua:682-733`, `vehicle_metadata_util.lua:27-37`). Il en transporte donc une seule à la fois.
- Les nouveaux véhicules ont le choix automatique de la configuration activé pour chaque compartiment (`vehicle_react_util.tl:339`), et le jeu n'a aucune fenêtre pour choisir à la main le fret d'un véhicule.
- Passagers et fret peuvent partager une ligne : les scripts ne refusent jamais du fret à un arrêt parce qu'il prend aussi des passagers (`line_util.tl:1381-1386`). Le fret n'est retiré que d'un arrêt dont le terminal ne peut ni charger ni décharger de fret (`line_util.tl:554-559`).
- Avec plusieurs frets, **Chargement complet (n’importe lequel)** et **Chargement complet (tout)** se comportent différemment : voir [Réglages de départ : chargement complet, niveau de remplissage et temps d'arrêt](departure.html).
- Quand la configuration ne convient pas, la ligne affiche **Certaines configurations de types de fret de cette ligne sont en conflit**, par exemple « Aucun véhicule de la ligne ne peut transporter certains des types de fret configurés pour le chargement. » (`line_warning.script.tl:10-36`).

```engine
L'ordre dans lequel plusieurs frets sont chargés, la façon dont un stock partagé est réparti entre les véhicules qui attendent, et la façon dont un véhicule choisit sa configuration de chargement sont décidés par le moteur.
```

## La configuration automatique

Tant que personne n'a enregistré de modification dans la fenêtre « Filtre de fret » d'un arrêt, ce qui la désactive pour de bon sur cette ligne (`line_util.tl:495-498`, `cargofilter_window.tl:438`), le jeu remplit lui-même les listes Charge à chaque création de la ligne, à chaque arrêt ajouté ou retiré, à chaque changement d'ordre des arrêts et à chaque point de passage ajouté (`manager_window.tl:6712`, `:6786`, `:6845`, `:6879`, `:6963`). Déplacer un arrêt vers une autre gare ou un autre quai, et retirer ou déplacer un point de passage, ne la relancent pas (`manager_window.tl:6851-6868`, `manager_window.tl:6968-6987`).

- Elle repart de listes vides, avec les passagers aux gares voyageurs (`line_util.tl:542-588`).
- Elle cherche producteurs et clients parmi les industries et les bâtiments de ville seulement : les entrepôts ne comptent pas (`cargo_util.tl:518-526`).
- Elle met un fret dans la liste Charge d'un arrêt quand ce fret sert plus loin et que rien ne le prend à cet arrêt. Un entrepôt compte comme prenant tout ce qu'il stocke (`line_util.tl:676-693`) : à un arrêt à côté d'un entrepôt qui stocke ce fret, le fret reste hors de la liste, et le train l'y décharge.
- Dès qu'un filtre a été modifié à la main, la ligne est marquée comme personnalisée (`cargofilter_window.tl:438`) et la configuration automatique ne la touche plus, même quand on ajoute des arrêts ensuite (`line_util.tl:496`).

```engine
Les scripts ne font qu'écrire les listes Charge ; le déchargement lui-même est fait par le moteur. La règle ci-dessus (ce qui n'est pas dans la liste est déchargé dans tout stock qui le prend) a été observée en jeu avec [Platform Details](https://mod.io/g/transportfever3/m/platform-details), novembre 2026.
```

## Bon à savoir

- Les gares à l'intérieur d'une industrie sont toujours spécialisées pour le fret dont l'industrie a besoin (wiki officiel).
- Les modules d'entrepôt spécialisés gèlent aussi le délai de livraison du fret stocké (wiki officiel) ; un entrepôt universel non.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) affiche les deux facteurs de chaque véhicule à quai, et où est parti le fret déchargé.

```check
official: « Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization. » Les entrepôts spécialisés « enable faster loading / unloading speeds ». ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Section spécialisée ×2, universelle ×1, aucune section adaptée ×0,25, au-delà du quai ×0,25, mélangés selon la part du train ; module d'entrepôt spécialisé ×2, entrepôt universel ×1.
result: refines
```
