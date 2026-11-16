---
title: Entrepôts
summary: Modules universels ou spécialisés, ce que contient chaque stock, réserver un type de fret, vitesse de chargement, coûts et pollution, et ce qu'un entrepôt ne fait pas.
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
game: 40425
fact: 500 | unités de fret par module, quel que soit son type
fact: ×2 | vitesse de chargement à un module spécialisé, ×1 à un module universel
fact: 150 000 / 300 000 | prix d'un module universel / spécialisé
fact: 0 | revenu pour le fret déchargé dans un entrepôt
---

Un entrepôt, c'est une entrée et un ensemble de **modules**. Il stocke le fret entre deux lignes : une ligne le décharge, une autre le recharge. Les gares l'atteignent par leur zone de desserte ; les villes et les industries n'y prennent jamais rien (wiki officiel).

## Modules universels ou spécialisés

| Module | Stock | Contient | Facteur de chargement | Source |
|---|---|---|---|---|
| **Entrepôt universel** | tous les modules universels partagent **un seul** stock | tout fret, mélangé | ×1 | `warehouse.script.lua:272-295`, `modules.script.lua:49` |
| **Entrepôt pour liquides**, **Entrepôt pour vrac**, **Entrepôt à plateforme**, **Entrepôt de marchandises** | **un stock par module** | un seul type de fret à la fois, de sa classe | ×2 | `warehouse.script.lua:296-314`, `modules.script.lua:120`, `modules.script.lua:165`, `modules.script.lua:247`, `modules.script.lua:296` |

- Chaque module ajoute **500** unités (`modules.script.lua:49`, `modules.script.lua:120`). Cinq modules universels font un stock de 2 500 ; cinq modules liquides font cinq stocks de 500.
- Les passagers ne sont jamais stockés (`warehouse.script.lua:279`, `warehouse.script.lua:304`).
- Un module spécialisé prend un seul type de fret à la fois : pour stocker du pétrole brut et du carburant, il faut deux modules liquides (wiki officiel).
- Le ×2 d'un module spécialisé se multiplie avec le facteur du quai : un quai vrac et un module vrac donnent ×4. Détails : [Vitesse de chargement et de déchargement](loading.html).

## Universel ou spécialisé ?

1. **Beaucoup de types de fret, petites quantités** : universel. Un seul stock commun, moitié prix et moitié moins de pollution.
2. **Un seul fret en grande quantité** (charbon, pétrole brut, bois) : spécialisé. Les véhicules y déchargent et chargent deux fois plus vite, mais il faut un module par type de fret.
3. **Nourriture et autre fret à délai de livraison court** : spécialisé ; le wiki officiel dit que ces modules gèlent le délai de livraison (voir plus bas).
4. Les deux sortes peuvent être mélangées dans un même entrepôt : les modules universels forment toujours un seul stock, chaque module spécialisé le sien.

## Un entrepôt accélère-t-il le déchargement ?

- **Module spécialisé** : oui, ×2 pour le fret qu'il prend. L'info-bulle de chargement du véhicule affiche « Entrepôt spécialisé : +100 % » (`cargo_react_util.tl:51-54`).
- **Module universel** : non. Son stock est créé à ×1 ; le ×2 demandé par le module est ignoré (`warehouse.script.lua:284`, `warehouse.script.lua:288-289`).
- Quand une partie du fret va à un entrepôt et une partie à une industrie, le véhicule les sert à tour de rôle, donc la vitesse change pendant un même arrêt (mesuré en jeu, voir [Vitesse de chargement et de déchargement](loading.html)).

## La section Stocks

- Une ligne par stock : le fret qu'il prend, la quantité, et le **Délai de livraison moyen restant** au survol (`entity_window_util.tl:408-410`).
- **Réserver un type de fret** : sur un module spécialisé, clique sur une icône de fret. Le jeu reconstruit l'entrepôt avec ce module réservé à ce fret (`entity_window_util.tl:339-367`, `warehouse.script.lua:308`). Retirer ou remplacer le module supprime sa réservation (`warehouse.script.lua:403-405`).
- **Décharger tout le fret** : vide cette ligne d'un coup (`entity_window_util.tl:423-434`). Le fret est perdu.
- Les deux boutons ne manquent que sur un entrepôt qui appartient à un autre joueur ; les tiens et les entrepôts sans propriétaire les ont (`warehouse_eow.script.tl:127-137`, `gui/entity_window/warehouse/warehouse.tl:38`, `entity_util.tl:83-86`).
- Le graphique **Statistiques** montre **Entrant** (déchargé) et **Sortant** (chargé) par an (`warehouse_eow.script.tl:159-160`).

## Coûts et pollution

| | Module universel | Module spécialisé | Source |
|---|---|---|---|
| Prix | 150 000 | 300 000 | `wh_universal.module.lua:18`, `wh_liquid.module.lua:22` |
| Entretien par an | 25 000 | 50 000 | `wh_universal.module.lua:19`, `wh_liquid.module.lua:23` |
| Bruit | 20 | 20 | `wh_universal.module.lua:33`, `wh_liquid.module.lua:37` |
| Pollution | 25 | 50 | `wh_universal.module.lua:34`, `wh_liquid.module.lua:38` |

- L'entrepôt ajoute sa propre pollution : **25**, ou **50** dès qu'un module spécialisé est construit (`warehouse.script.lua:327`, `warehouse.script.lua:338-345`).
- Le menu de construction a une entrée par classe et par époque (dès 1900, 1940 et 1980) (`warehouses/warehouse.tl:3-5`) ; les époques suivantes affichent ×3 et ×9 (`warehouses/warehouse.tl:48`, `warehouses/warehouse.tl:75-76`), et l'entretien des entrepôts monte aussi avec l'année. Détails : [Coûts, entretien et emprunts](costs.html).
- Les modules vrac, plateau et marchandises coûtent autant que les modules liquides (`wh_bulk.module.lua:22-23`, `wh_flatbed.module.lua:22-23`, `wh_goods.module.lua:18-19`).

```engine
Les scripts donnent deux niveaux d'émission, le second deux fois le premier (`warehouse.script.lua:342-343`) ; l'entrepôt passe du premier au second à mesure que ses stocks se remplissent, stocks pleins = deux fois (`emissions.script.tl:237-249`). Le prix réellement facturé pour les modules est calculé par le moteur.
```

## Ce qu'un entrepôt ne fait pas

- **Il ne rapporte rien.** Décharger dans un entrepôt ne donne aucun revenu ; l'unité est payée une seule fois, quand elle atteint son client, pour la distance en ligne droite depuis sa source (mesuré en jeu, voir [Revenus du fret et délai de livraison](income.html)).
- **Il n'approvisionne pas les villes ni les industries** proches : elles ne prennent le fret que des véhicules (wiki officiel).
- **Ce n'est pas une destination pour la configuration automatique des lignes**, qui cherche seulement producteurs et clients ; mais un arrêt à côté d'un entrepôt qui stocke un fret laisse ce fret hors de la liste Charge, donc les trains l'y déchargent (voir [Vitesse de chargement et de déchargement](loading.html)).
- **Il n'a pas besoin de route.** L'entrée s'accroche à une rue, mais le fret ne passe que par les zones de desserte des gares (`warehouse.script.lua:386-389`, wiki officiel). La fenêtre de l'entrepôt montre sa zone de desserte (`gui/entity_window/warehouse/warehouse.tl:88-96`).

```engine
Où va le fret déchargé, et si le délai de livraison d'une unité stockée s'arrête, sont décidés par le moteur. Aucun script ne gèle le délai : le wiki officiel dit que les modules spécialisés le font, et qu'un module universel non.
```

## Bon à savoir

- Vérifie la liste Charge de chaque arrêt près d'un entrepôt : ce qui n'y est pas est déchargé dans l'entrepôt, même au milieu de la ligne.
- Un stock plein refuse le fret en plus, sauf si l'arrêt utilise « Forcer le déchargement de tout le fret à l’arrivée » (« Décharger le fret même si les stocks sont pleins ») ; ce que devient le fret qui ne rentre pas est décidé par le moteur (voir [Vitesse de chargement et de déchargement](loading.html)).
- Pour garder un module spécialisé pour un seul fret, réserve son type de fret dans la section Stocks.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) liste, par gare, les entrepôts à portée avec leurs stocks ; [Platform Details](https://mod.io/g/transportfever3/m/platform-details) montre où est parti le fret déchargé.

```check
official: « Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types. » Les entrepôts spécialisés « freeze the cargo item's delivery timer » et « enable faster loading / unloading speeds ». « In specialized warehouses, only one cargo type can be stored at a time for a given module. » ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Les modules universels forment un seul stock commun avec un facteur de chargement ×1, chaque module spécialisé son propre stock de 500 avec ×2 et un seul type de fret. Un module spécialisé coûte deux fois plus (300 000, entretien 50 000) et pollue deux fois plus (50). Le gel du délai n'est pas dans les scripts.
result: refines
```
