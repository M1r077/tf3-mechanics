---
title: Travailleurs et bonus des travailleurs
summary: Comment les habitants obtiennent un emploi dans une industrie, lesquels comptent pour le bonus, et quelle est sa taille.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-15
game: 40425
fact: 10 / 20 | travailleurs requis pour le bonus
fact: 2 ans | durée pendant laquelle une arrivée compte
fact: ×1,5–2,5 | facteur de bonus, fixe pour chaque industrie
---

Chaque industrie offre des emplois. Quand assez de travailleurs **arrivent par tes lignes de passagers**, l'industrie produit davantage. La fenêtre de l'industrie affiche deux nombres différents, et les confondre est la première source de malentendus.

```diagram workers_flow
```

## Qui peut travailler dans une industrie

- Chaque industrie du jeu de base a **20 emplois** (`industrialCapacity = 20`).
- Les emplois sont réglés pour que les habitants **ne puissent pas y aller à pied ni en voiture** : seules tes lignes peuvent les amener (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Chaque habitant a un logement, un commerce et un emploi. Le jeu choisit l'emploi parmi les lieux que l'habitant peut atteindre ; une industrie a un poids de destination de 2,0 (`industryutil.lua:455`).

```engine
La façon dont un habitant choisit un emploi parmi tous les lieux qu'il peut atteindre (temps de trajet, coût, poids de 2,0) est calculée par le moteur. Les scripts ne donnent que les données d'entrée.
```

## Travailleurs attribués

Les habitants dont l'emploi est cette industrie. C'est la jauge des emplois de la fenêtre de l'industrie et la colonne **Lieux de travail** des statistiques des industries (« 12/20 ») (`entity_window_util.tl:1238`, `statistic_industries.tl:305`). Être attribué ne suffit **pas** pour le bonus : il faut vraiment faire le trajet.

## Travailleurs comptés pour le bonus

Un petit script du jeu surveille chaque arrivée (`industry_workers.script.tl`) :

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
| Ligne de bus supprimée ; personne n'arrive pendant 2 ans | tombe à 0 | s'arrête | ×1 |

## Amener des travailleurs à une industrie

```diagram workers_trip
```

- Un travailleur est compté quand il **arrive à l'industrie** elle-même, que la cible de son trajet (`targetOrAtEntity`) est l'industrie et que son dernier mode de déplacement est **Lignes** (`industry_workers.script.tl:86-94`). Descendre à un arrêt ne suffit pas : la personne doit atteindre l'industrie.
- Chaque habitant a un mode de déplacement par destination (logement, commerce, emploi). La fenêtre de l'industrie liste les travailleurs attribués avec une icône pour ce mode : **À pied**, **Voiture** ou **Lignes** (`entity_window_util.tl:1400-1435`). Pour une industrie, ce doit toujours être Lignes, car À pied et Voiture n'y sont pas autorisés (`industryutil.lua:451-457`).
- « Pas à pied » veut donc dire que tout le trajet ne peut pas être fait à pied ou en voiture. Cela ne veut pas dire « jamais à pied » : un trajet en Lignes commence et finit quand même à pied entre les arrêts et les bâtiments (voir la note moteur ci-dessous).
- **Les correspondances comptent.** Le script regarde seulement le mode du trajet, pas le nombre de lignes utilisées (`industry_workers.script.tl:91`). Un travailleur d'une ville à quatre lignes de là compte autant qu'un voisin, mais peut mettre bien plus longtemps à arriver.
- **N'importe laquelle de tes lignes peut les amener**, même une ligne de fret, tant que ses véhicules prennent des passagers et que l'arrêt charge des passagers. Le script ne vérifie pas le type de véhicule (`industry_workers.script.tl:86-118`). Les joueurs signalent moins de problèmes avec des lignes de passagers séparées.
- Certaines industries (par exemple les plateformes pétrolières) ont leur propre arrêt intégré, qui prend passagers et fret (`industryutil.lua:156-165`).
- La fenêtre de l'industrie indique, pour chaque travailleur attribué, s'il est **Actuellement ici** ou **En route** (`entity_window_util.tl:1371-1384`). La section Boosters liste les travailleurs comptés avec leur **Temps restant** sur les 2 ans (`entity_window_util.tl:1579-1630`, `industry_eow.script.tl:644-649`).
- Une industrie encore sans travailleur affiche : « Connecter cet emplacement aux transports publics pour permettre à des habitants d'y travailler. » (`entity_window_util.tl:1650-1652`).

```engine
Quel arrêt dessert une industrie, quelle distance un travailleur marche d'un arrêt à l'entrée de l'industrie, et les habitants de quelles villes prennent l'emploi sont décidés par le moteur (zones de desserte, recherche de chemin, choix de l'emploi). Les scripts ne fixent aucune limite de distance pour les travailleurs. Des joueurs signalent qu'une gare dont la zone de desserte couvre l'industrie pour le fret n'amenait pas de travailleurs avant qu'un bus aille jusqu'à l'entrée de l'industrie (fil Steam « Problem getting workers to site »).
```

```tip
**Obtenir vite le bonus de travailleurs (et le contrat Transporter des travailleurs) : commencer par une ligne simple.**

1. Créez une **nouvelle ligne de voyageurs** entre un arrêt à l'industrie et **une seule ville**.
2. Placez l'arrêt en ville pour que sa zone de desserte **ne touche aucune de vos autres gares de voyageurs**.
3. Un seul véhicule suffit pour démarrer.

Les emplois sont attribués à l'ouverture de la ligne : lors de deux tests, les **20 emplois sont allés à cette seule ville**, et le bonus a démarré après **346 s et 925 s** de temps de jeu (une fois avec un seul véhicule). Quand l'arrêt en ville touchait la zone de desserte d'une gare du réseau, des emplois sont allés à une ville éloignée et les derniers travailleurs ont mis beaucoup plus longtemps (964 s). Mesuré avec [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) et le [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) ; c'est toujours le moteur qui choisit qui obtient un emploi.
```

## Contrat Transporter des travailleurs

- Il n'est proposé que pour une industrie avec des emplois, dont le bonus des travailleurs n'est pas encore actif et qui a expédié ou reçu du fret sur la dernière année, d'après les chiffres annuels du moteur (`deliver_workers.script.tl:121-131`, `industry_util.tl:541-558`). Savoir si recevoir seulement suffit dépend de la façon dont le moteur remplit les règles de production ; ce n'est pas dans les scripts.
- Il est rempli quand le bonus des travailleurs devient actif : les mêmes 10 arrivées différentes sur 20 par tes lignes (`deliver_workers.script.tl:152-156`). Rien d'autre n'est compté ; il n'y a pas de règle cachée.
- La barre de progression de la carte du contrat vaut « travailleurs comptés ÷ la moitié des emplois » (`deliver_workers.script.tl:267-272`, `industry_util.tl:11-18`).
- Les flèches sur la carte du contrat partent des **5 villes les plus proches**. Ce n'est qu'une indication : le script les trace selon la distance, pas selon qui a l'emploi (`deliver_workers.script.tl:297-317`).
- Voir [Contrats : offres, délais et récompenses](subsidies.html) pour l'argent et le délai.

## Pourquoi mes travailleurs n'arrivent pas ?

| Vérification | Où regarder | Pourquoi |
|---|---|---|
| Quelqu'un a-t-il l'emploi ? | Jauge des emplois (« 12/20 ») | Sans travailleurs attribués, personne ne voyage. Le choix de l'emploi relève du moteur. |
| Icône de mode des travailleurs | Liste des travailleurs : À pied / Voiture / Lignes | Seuls les trajets en Lignes peuvent compter (`industry_workers.script.tl:91`). |
| Se déplacent-ils ? | **En route** / **Actuellement ici** | « En route » longtemps : correspondances lentes ou surchargées, ou pas de chemin depuis le dernier arrêt. |
| Le dernier arrêt atteint-il l'entrée de l'industrie ? | Zone de desserte de l'arrêt, route d'entrée | Signalé par des joueurs ; relève du moteur. Un court bus jusqu'à l'entrée a aidé. |
| L'arrêt charge-t-il des passagers ? | Arrêt de la ligne, Filtre de fret | Les passagers doivent être chargés et déchargés aux deux bouts du trajet. |
| 10 personnes **différentes** en 2 ans ? | Section Boosters, **Temps restant** | La même personne compte une fois ; les arrivées plus anciennes sortent (`industry_workers.script.tl:56-70`). |
| Plus de 40 emplois (mods) ? | Jauge des emplois | Ne peut jamais atteindre la moitié avec 20 arrivées gardées. |

## Bon à savoir

- La limite de 20 arrivées gardées et la règle des 50 % font qu'une industrie de **plus de 40 emplois** (possible avec des mods) ne pourrait jamais être boostée par les travailleurs.
- Le contrat **Transporter des travailleurs** est rempli quand ce bonus s'active (`deliver_workers.script.tl:152-156`).
- Le fret booster (engrais, machines, outils) est un bonus **distinct** des industries de matières premières, non traité ici.
- Le mod [Origine des travailleurs (Worker Origins)](https://mod.io/g/transportfever3/m/worker-origins) montre, dans la fenêtre d'industrie, de quelles villes viennent les travailleurs attribués et ceux du bonus, avec des flèches sur la carte.

```check
official: « If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again. » ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: « Suffisamment » = la moitié des emplois (10 sur 20) ; « récemment » = les 2 dernières années de jeu, 20 dernières arrivées, une par personne, uniquement par tes lignes ; facteur de bonus ×1,5 à ×2,5 selon l'industrie. Les correspondances comptent ; le mode du trajet doit être Lignes, la marche depuis un arrêt fait partie d'un tel trajet.
result: refines
```
