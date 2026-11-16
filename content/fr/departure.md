---
title: Réglages de départ : chargement complet, niveau de remplissage et temps d'arrêt
summary: Quand un véhicule quitte un arrêt : les trois modes de départ, le niveau de remplissage de chaque fret, et les temps d'arrêt minimum, maximum et supplémentaire.
domain: stations
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-15
game: 40425
fact: 600 s | temps d'arrêt max. par défaut d'un nouvel arrêt
fact: 30 s / 60 s | attente supplémentaire max. par défaut, route / rail
fact: 0–100 % | niveau de remplissage, par fret, de la capacité du véhicule
---

Chaque arrêt d'une ligne a ses propres réglages de départ, dans la fenêtre « Filtre de fret » de l'arrêt (clique sur l'arrêt dans la fenêtre de la ligne). Ils décident **combien** le véhicule charge à cet arrêt et **combien de temps** il peut attendre.

## Les réglages

| Réglage | Valeurs | Nouvel arrêt | Source |
|---|---|---|---|
| « Charger si disponible », « Chargement complet (n’importe lequel) », « Chargement complet (tout) » | un des trois | Charger si disponible (mesuré) | `cargofilter_window.tl:798-821` |
| « Temps d’arrêt min. » | 0–600 s, par pas de 10 | 0 s (mesuré) | `cargofilter_window.tl:841-845` |
| « Temps d’arrêt max. » | 0–600 s, ou « --- » (sans limite, curseur au bout) | **600 s** (mesuré) | `cargofilter_window.tl:855-863` |
| « Attente supplémentaire max. » | 0–600 s, par pas de 10 | 60 s ; 30 s dans une gare routière ou de tram sans rail | `cargofilter_window.tl:827-831`, `line_util.tl:478-490` |
| « Niveau de remplissage », par fret chargé | 0–100 %, par pas de 1 | 100 % | `cargofilter_window.tl:698-704`, `line_util.tl:472` |

- Cliquer sur un temps ouvre une case de saisie : on peut y taper des valeurs au-dessus de 600 s (`cargofilter_window.tl:204-208`).
- Les trois temps restent dans l'ordre : monter le minimum ou l'attente supplémentaire au-dessus du maximum monte aussi le maximum (`cargofilter_window.tl:834-835`, `cargofilter_window.tl:848-849`, `cargofilter_window.tl:865-869`).
- Changer l'un d'eux marque la ligne comme personnalisée : la configuration automatique ne touche plus ses listes Charge (`cargofilter_window.tl:438`, voir [Vitesse de chargement et de déchargement](loading.html)). La configuration automatique elle-même ne change jamais le mode ni les temps (`line_util.tl:495-513`).

## Niveau de remplissage : un plafond par fret

Le niveau de remplissage est le maximum de ce fret que le véhicule prend à cet arrêt, en part de la capacité du véhicule, arrondi à l'unité la plus proche (mesuré en jeu).

| Véhicule | Niveau de remplissage | Part avec |
|---|---|---|
| camion, 15 places, bois | 50 % | **8** (7,5 arrondi au-dessus) |
| camion, 22 places, tissu | 70 % | **15** à chaque fois (15,4) |
| train, 18 places, verre | 48 % | au plus **9** (8,64) |
| tram, 28 places, carburant | 66 % | au plus **18** (18,48) |

- Le fret déjà à bord compte : un tram arrivé avec 14 carburant est reparti avec 18, pas 14 + 18.
- Au-dessus du plafond, rien n'est chargé **et rien n'est déchargé** à cause de lui : un camion arrivé avec 22 engrais (plafond 11) est reparti avec 22.
- **0 %** veut dire : ne pas charger ce fret ici.
- Avec un mode Chargement complet, le plafond compte comme plein : des camions de bois avec un niveau de remplissage de 50 % ont attendu environ 270 s et sont partis avec 8 sur 15, pas 15.
- Il n'y a pas de pourcentage de déchargement. Le déchargement dépend de la liste Charge et de « Forcer le déchargement de tout le fret à l’arrivée » ([Vitesse de chargement et de déchargement](loading.html)).

## Chargement complet et temps d'arrêt

- **Charger si disponible** : le véhicule prend ce qui est là et part.
- **Chargement complet (tout)** : le véhicule attend d'être plein. Des camions de bois ont attendu 460–566 s et sont partis avec 15 sur 15.
- **Chargement complet (n’importe lequel)** : le véhicule part quand un fret est plein. Un train de bois et de planches est parti avec 143 et 144 unités de bois après 369–380 s ; deux autres départs après environ 30 s avec 57 et 118 unités ne sont pas expliqués.
- **Temps d’arrêt max.** met fin à l'attente, même sans rien de chargé. Un train de légumes en Chargement complet (tout) avec un maximum de 120 s s'est soit rempli (64 sur 64) en environ 25 s, soit est parti après 116–120 s avec 26 ou **0**. Avec les 600 s par défaut, il est parti avec 26 sur 64 après 596–600 s.
- **Temps d’arrêt min.** est l'arrêt entier, chargement compris, pas un temps en plus après : avec 60 s, des trains de verre se sont arrêtés 55–61 s à chaque fois, quoi qu'ils aient chargé.
- **Attente supplémentaire max.** : « Maximum wait time after loading to improve vehicle distribution » (`cargofilter_window.tl:828`). La fenêtre du véhicule affiche « Maintien d’une distance de sécurité » pendant qu'il attend (`entity_window_util.tl:2279-2286`).
- **Plusieurs véhicules au même arrêt chargent en même temps**, quel que soit leur moment d'arrivée (vu en jeu). Deux camions de bois arrivés à environ 90 s d'écart sont partis à la même seconde, chacun avec 8. La façon dont le fret est partagé entre eux n'a pas été mesurée.

```engine
Les scripts ne font que stocker les réglages ; le moment où un véhicule part est décidé par le moteur.
```

Les règles ci-dessus ont été mesurées avec la base de données de [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) (relevés toutes les 2 s, donc les temps d'arrêt sont à ±2 s), novembre 2026.

## Bon à savoir

- Une longue attente en Chargement complet à un arrêt où peu de fret arrive bloque le quai : les autres véhicules de la ligne font la queue derrière.
- Un temps d'arrêt max. court avec Chargement complet peut faire partir des véhicules vides s'ils reviennent avant qu'un nouveau fret soit là.
- Une fois, un train en Chargement complet (tout) s'est arrêté 783–992 s avec un maximum de 600 s. La cause n'a pas été trouvée.

```check
official: « Full load (any): The vehicle will stop and wait until one cargo type is fully loaded. Full load (all): The vehicle will stop and wait until it is fully loaded. » « In the vanilla game "all" and "any" only applies to trains and ships […] Any other vehicle type will wait for full load in both cases. » Chaque fret est chargé « to what percentage of a vehicle's total capacity ». ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles#departure_configuration))
scripts: Trois modes de départ, temps d'arrêt min. / max. 0–600 s (ou sans limite), attente supplémentaire max. 0–600 s (60 s, 30 s route), niveau de remplissage 0–100 % par fret ; mesuré : le niveau de remplissage plafonne le fret à bord, arrondi à l'unité la plus proche, et compte comme plein pour le Chargement complet ; le temps d'arrêt max. met fin à un chargement complet, même à vide ; le temps d'arrêt min. inclut le chargement ; les véhicules d'un même arrêt chargent ensemble.
result: refines
```
