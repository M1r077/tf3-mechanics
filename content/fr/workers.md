---
title: Travailleurs et bonus des travailleurs
summary: Comment les habitants obtiennent un emploi dans une industrie, lesquels comptent pour le bonus, et quelle est sa taille.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-14
fact: 10 / 20 | travailleurs requis pour le bonus
fact: 2 ans | durée pendant laquelle une arrivée compte
fact: ×1,5–2,5 | facteur de bonus, fixe pour chaque industrie
---

Chaque industrie offre des emplois. Quand assez de travailleurs **arrivent par tes lignes de passagers**, l'industrie produit davantage. La fenêtre de l'industrie affiche deux nombres différents, et les confondre est la première source de malentendus.

```diagram workers_flow
```

## Qui peut travailler dans une industrie

- Chaque industrie du jeu de base a **20 emplois** (`industrialCapacity = 20` dans le .con.lua de chaque industrie).
- Les emplois sont réglés pour que les habitants **ne puissent pas y aller à pied ni en voiture** : seules tes lignes peuvent les amener (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Chaque habitant a un logement, un commerce et un emploi. Le jeu choisit l'emploi parmi les lieux que l'habitant peut atteindre ; une industrie a un poids de destination de 2,0 (`industryutil.lua:455`).

```engine
La façon dont un habitant choisit un emploi parmi tous les lieux qu'il peut atteindre (temps de trajet, coût, poids de 2,0) est calculée par le moteur. Les scripts ne donnent que les données d'entrée.
```

## Travailleurs attribués

Les habitants dont l'emploi est cette industrie. C'est la jauge des emplois de la fenêtre de l'industrie et la colonne **Lieux de travail** des statistiques des industries (« 12/20 ») (`entity_window_util.tl:1238`, `statistic_industries.tl:305`). Être attribué ne suffit **pas** pour le bonus : il faut vraiment faire le trajet.

## Travailleurs comptés pour le bonus

Un petit script du jeu, `industry_workers.script.tl`, surveille chaque arrivée :

1. Quand un habitant arrive à une industrie et que son **dernier trajet s'est fait par tes lignes**, l'arrivée est notée avec l'heure du jeu (`industry_workers.script.tl:86-118`).
2. Seules les arrivées des **2 dernières années de jeu** sont gardées (`industry_productivity_util.tl:3` : `2 * getDefaultYearDuration()`).
3. Au plus les **20 dernières** arrivées sont gardées (`industry_workers.script.tl:4`, `KeepHistoryCount = 20`).
4. Quand la même personne arrive à nouveau, la nouvelle arrivée remplace l'ancienne : chaque habitant compte **une seule fois** (`industry_workers.script.tl:56-70`).

```diagram workers_window
```

## Quand le bonus démarre et s'arrête

- L'industrie est boostée quand les travailleurs comptés atteignent **la moitié des emplois** : `comptés ≥ emplois × 0,5` (`industry_productivity_util.tl:35-48`, `RequiredWorkersFractionForBoost = 0.5`). Avec 20 emplois : **10 travailleurs**.
- La section Boosters de la fenêtre de l'industrie affiche exactement cela : « comptés / nécessaires », arrondi au supérieur (`industry_react_util.tl:627`).
- La vérification est refaite à chaque nouvelle arrivée ou quand la plus ancienne dépasse 2 ans (`industry_workers.script.tl:40-43`). Le bonus **s'arrête donc tout seul** environ 2 ans après que les travailleurs ne viennent plus.

## Taille du bonus

- La production est multipliée par le **facteur de bonus** de l'industrie, affiché « +X % » dans la fenêtre (`industry_react_util.tl:716`).
- Ce facteur est tiré une fois à partir de la graine aléatoire de l'industrie : **entre ×1,5 et ×2,5**, et il ne change jamais pour cette industrie (`industry_productivity_util.tl:58-72`). Une industrie sans graine utilise ×2.
- Deux mines identiques peuvent donc avoir des bonus différents : regarde le « +X % » avant de choisir laquelle desservir.

## Exemple

Une mine de charbon avec 20 emplois et « +84 % ».

| Situation | Comptés | Boostée ? | Production |
|---|---|---|---|
| Nouvelle ligne de bus : 14 habitants attribués, aucun n'est encore arrivé | 0 | non | ×1 |
| 12 habitants différents sont arrivés en bus cette année | 12 | oui (≥ 10) | ×1,84 |
| Ligne supprimée ; personne n'arrive pendant 2 ans | tombe à 0 | s'arrête | ×1 |

## Bon à savoir

- La limite de 20 arrivées gardées et la règle des 50 % font qu'une industrie de **plus de 40 emplois** (possible avec des mods) ne pourrait jamais être boostée par les travailleurs.
- La subvention « Transporter des travailleurs » est remplie quand ce bonus s'active (wiki officiel, Subventions).
- Le fret booster (engrais, machines, outils) est un bonus **distinct** des industries de matières premières, non traité ici.

```check
official: « If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again. » ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: « Suffisamment » = la moitié des emplois (10 sur 20) ; « récemment » = les 2 dernières années de jeu, 20 dernières arrivées, une par personne, uniquement par tes lignes ; facteur de bonus ×1,5 à ×2,5 selon l'industrie.
result: refines
```
