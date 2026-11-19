---
title: Notifications et avertissements
summary: Quand chaque avertissement apparaît et quand il disparaît : véhicules bloqués, stations inutilisables ou surchargées, problèmes de lignes et d'arrêts, notes des villes, état des véhicules, industries qui ferment, et quels avertissements sont masqués du journal par défaut.
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40444
fact: 5 min | de temps de jeu à l'arrêt avant qu'un véhicule soit signalé bloqué
fact: 20 % | d'état qui déclenche l'avertissement, jusqu'à ce que le véhicule repasse au-dessus de 30 %
fact: 11 | types de notifications désactivés dans une nouvelle partie
fact: 75 jours | entre deux vérifications des stations sans connexion routière
---

La plupart des avertissements sont **persistants** : un script du jeu vérifie la situation encore et encore, l'avertissement reste tant que le problème est là et disparaît tout seul quand il est réglé. Les vérifications sont réparties à tour de rôle sur 4 mises à jour, donc un avertissement peut mettre un moment à apparaître ou à disparaître (`notifications.script.tl:13`, `notifications.script.tl:49`).

## Quand chaque avertissement apparaît

| Avertissement | Apparaît quand | Disparaît quand | Source |
|---|---|---|---|
| **Véhicule bloqué** | un de tes véhicules est en route, pas arrêté par toi, et a une vitesse de 0 depuis **5 minutes** de temps de jeu | il roule de nouveau | `notifications.script.tl:557-580` |
| **Station non opérationnelle** | aucun terminal de la station ne charge ni ne décharge de passagers et **rien** n'est dans sa zone de chalandise (ni entrepôt, ni industrie, ni bâtiment de ville), alors qu'une de tes lignes s'y arrête | quelque chose entre dans la zone de chalandise | `notifications.script.tl:602-617`, `notifications.script.tl:630-647`, `station_useless.script.tl:39` |
| **Station surchargée** | la station contient plus de passagers ou de fret en attente qu'elle ne peut (débordement), alors qu'une de tes lignes s'y arrête ; des passagers partent | le débordement cesse | `notifications.script.tl:599`, `notifications.script.tl:649-661`, `overcrowding.script.tl:23` |
| **État du véhicule** | un de tes véhicules est à **20 %** d'état ou moins | il repasse au-dessus de **30 %** | `notifications.script.tl:310-318` |
| **Évaluation de la ville très faible** | une des notes de la ville tombe à Très insuffisant (moins de 1/6) | la note revient à Médiocre ou mieux | `notifications.script.tl:230-238`, `town_util.tl:763-769`, `town_util.tl:983-985` |
| **Évaluation de la ville en baisse** | une note est Insuffisant ou Médiocre (moins de 50 %) sans être dans l'avertissement Très insuffisant | la note est Bon ou mieux | `notifications.script.tl:240-248` |
| **Fermeture de l’industrie** | une industrie commence son compte à rebours de fermeture | elle ferme, ou elle est de nouveau utilisée à temps | `notifications.script.tl:439-451`, `industry_close.script.tl:53-59` |
| **Aucune connexion routière** | une station n'est pas reliée à une route ; vérifié tous les **75 jours** | la vérification suivante trouve une route | `notifications.script.tl:16`, `notifications.script.tl:423-436` |
| **Problème de déchargement du fret** | le fret d'un véhicule n'est jamais déchargé sur sa ligne | il est déchargé | `notifications.script.tl:277-290`, `cargo_rtc_warning.script.tl:28-37` |

- Un véhicule **au dépôt** ne compte jamais comme bloqué : cette vérification est désactivée dans le script (`notifications.script.tl:563-564`). Un véhicule que tu as arrêté ne compte pas non plus.
- La vérification Station non opérationnelle ne regarde que la zone de chalandise. Une station qui a déjà des passagers qui montent ou descendent à un terminal n'est jamais signalée (`notifications.script.tl:606-610`).
- Comment remonter une note de ville : [Croissance des villes](towns.html) et [Réputation](reputation.html). Comment fonctionne le compte à rebours de fermeture et comment l'arrêter : [Industries](industries.html). Ce que l'état fait à un véhicule : [Coûts, entretien et emprunts](costs.html).

```engine
Le débordement d'une station, l'existence d'un parcours pour un véhicule, la capacité d'une ligne à atteindre ses stations et la durée permise du trajet entre deux villes sont déterminés par le moteur (calculateStationGroupCargo, getVehicleProblems, getLineProblems, getTownProblems). Les scripts ne font que transformer ses réponses en avertissements.
```

```tip scripts
Véhicule bloqué, Problème de véhicule, État du véhicule, Station surchargée et Station inutilisable sont désactivés dans le journal d'une nouvelle partie. Active-les dans les réglages des notifications : ce sont eux qui te signalent un embouteillage, un parcours manquant ou une flotte usée.
```

## Problèmes de lignes, d'arrêts et de véhicules

Ils viennent directement des vérifications du moteur sur tes lignes et tes véhicules ; le script donne un titre à chacun.

| Avertissement | Cas | Source |
|---|---|---|
| **Problème de ligne** | trop peu de stations ; une station deux fois de suite ; des stations incompatibles entre elles ; des stations n'ont pas pu être reliées ; des terminaux alternatifs n'ont pas pu être reliés | `line_warning.script.tl:46-128` |
| **La ligne est mal configurée** | un type de fret qui ne peut être chargé nulle part, ou déchargé nulle part ; aucun véhicule ne peut transporter un fret réglé pour être chargé ; des véhicules qui ne transportent aucun des frets configurés, ou des véhicules de fret seul sur une ligne de passagers ; aucun fret configuré du tout | `line_warning.script.tl:15-36`, `line_warning.script.tl:133` |
| **Problème de gare** | un arrêt que les véhicules actuels ne peuvent pas utiliser ; un arrêt de passagers utilisé par des véhicules de fret (un ou tous) ; un arrêt de fret utilisé par des véhicules de passagers ; un type de fret configuré qui ne peut pas être chargé ou déchargé à cet arrêt | `line_station_warning.script.tl:6-87` |
| **Problème de véhicule** | aucun parcours électrifié ; aucun parcours pour les grands aéronefs ; aucun parcours pour les grands navires ; aucun parcours du tout ; deux trains qui se bloquent mutuellement | `vehicle_warning.script.tl:6-58` |
| **Ville non connectée** | la route entre deux villes est interrompue ; le trajet entre deux villes est trop long | `town_warning.script.tl:7-19` |

- « Aucun parcours pour les grands aéronefs » et « Aucun parcours pour les grands navires » signifient que le véhicule est trop grand pour une piste, un quai ou une voie navigable de sa ligne : voir [Aéronefs](aircraft.html) et [Navires](ships.html).

## Journal, fenêtres et réglages

- Chaque type d'avertissement peut être désactivé dans les réglages des notifications (« Configurer la journalisation des notifications »). Un type désactivé n'a pas de fenêtre et n'est pas gardé dans le journal (`notification_util.tl:145-146`, `notification_log.tl:480`).
- Dans une **nouvelle partie**, 11 types sont désactivés dès le départ : **Véhicule bloqué**, **Problème de véhicule**, **État du véhicule**, **Station surchargée**, **Station inutilisable**, **Station non connectée**, **Ville non connectée**, **Fret non déchargé**, et les messages d'avancement Prospection, Campagne marketing et Verdissement de l’industrie de l'entreprise (`stuck_vehicle.res.lua:7`, `vehicle_warning.res.lua:8`, `noroadconnection.res.lua:8`, `vehiclecondition.res.lua:8`, `overcrowding.res.lua:8`, `station_useless.res.lua:7`, `town_warning.res.lua:8`, `cargo_rtc_warning.res.lua:8`, `notification_util.tl:32-39`).
- Les messages ponctuels (nouveau véhicule, nouvelle construction, nouveau rang, contrats) cachent leur fenêtre après **60 secondes** de temps de jeu ; ils restent dans l'historique (`notification_util.tl:10`, `notifications.script.tl:85-94`).
- Une notification prend aussi fin quand tout ce qu'elle désigne a été supprimé ou reconstruit (`notifications.script.tl:95-107`).
- Dans une mission, les notifications démarrent en pause, jusqu'à ce que la mission les active (`notifications.script.tl:700-704`).

## Bon à savoir

- Un avertissement de blocage après 5 minutes ne dit pas pourquoi. Regarde le véhicule : un signal rouge, un signal à sens unique dans le mauvais sens, ou un avertissement Problème de véhicule pour le même véhicule.
- « Station non opérationnelle » veut seulement dire « rien dans la zone de chalandise pour l'instant ». Rapproche la station des maisons, d'une industrie ou d'un entrepôt, ou agrandis-la.
- Une station surchargée perd des passagers : ajoute des véhicules, ou raccourcis l'intervalle (voir [Départ et attente](departure.html)).

```check
official: La page User Interface du wiki officiel décrit le bouton des notifications, le journal et ses filtres, sans les conditions de chaque avertissement. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: Les conditions ci-dessus : bloqué après 5 minutes à vitesse 0 en route, état du véhicule à 20 % jusqu'à 30 %, note de ville Très insuffisant sous 1/6, connexion routière vérifiée tous les 75 jours, 11 types désactivés par défaut.
result: adds
```
