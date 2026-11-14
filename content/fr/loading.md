---
title: Vitesse de chargement et de déchargement
summary: Ce qui fait qu'un véhicule charge vite ou lentement à un arrêt : le véhicule, les sections du quai et le stock qui donne ou reçoit le fret.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-14
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
Le choix du destinataire de chaque unité et la multiplication finale se font dans le moteur. Les facteurs ci-dessus sont les données que les scripts lui donnent ; le résultat a été vérifié avec les valeurs exposées par le moteur (sonde de Platform Details, octobre 2026).
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

## Bon à savoir

- Les gares à l'intérieur d'une industrie sont toujours spécialisées pour le fret dont l'industrie a besoin (wiki officiel).
- Les modules d'entrepôt spécialisés gèlent aussi le délai de livraison du fret stocké (wiki officiel) ; un entrepôt universel non.
- Platform Details affiche les deux facteurs de chaque véhicule à quai, et où est parti le fret déchargé.

```check
official: « Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization. » Les entrepôts spécialisés « enable faster loading / unloading speeds ». ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Section spécialisée ×2, universelle ×1, aucune section adaptée ×0,25, au-delà du quai ×0,25, mélangés selon la part du train ; module d'entrepôt spécialisé ×2, entrepôt universel ×1.
result: refines
```
