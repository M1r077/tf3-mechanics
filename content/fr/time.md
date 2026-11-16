---
title: Temps de jeu et calendrier
summary: La vitesse du jeu et la vitesse du calendrier sont deux choses différentes. Combien durent un jour et une année, ce que change un calendrier ralenti ou en pause, et ce qu'il ne change pas.
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
game: 40425
fact: 4 s | un jour du calendrier à la vitesse du calendrier ×1, vitesse du jeu 1x
fact: ≈ 24 min | une année du calendrier aux mêmes vitesses
fact: 0 ×0,25 ×0,5 ×1 ×2 ×4 | paliers de la vitesse du calendrier
fact: 0 1x 2x 4x | paliers de la vitesse du jeu
---

Le jeu a **deux horloges**. La **vitesse du jeu** (pause, 1x, 2x, 4x) fait tout tourner plus vite : véhicules, production, villes. La **Vitesse du calendrier** règle seulement la vitesse à laquelle la date avance. Presque toutes les règles du jeu comptent en temps de jeu, pas en jours du calendrier.

## Les deux réglages

| Réglage | Paliers | Ce qu'il change | Source |
|---|---|---|---|
| **Vitesse du jeu** | Pause, 1x, 2x, 4x | la vitesse de toute la simulation | `game_bar_widgets.tl:199-203` |
| **Vitesse du calendrier** | Jeu en pause, ×0,25, ×0,5, ×1, ×2, ×4 | combien de secondes de jeu dure un jour | `game_bar_widgets.tl:321-335`, `game_bar_widgets.tl:351` |

- À la vitesse du calendrier ×1, un jour dure **4 secondes** de temps de jeu (wiki officiel), donc un mois dure environ 2 minutes et une année environ **24 minutes** à 1x. Mesuré avec [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) : 4,0 s par jour à ×1, 1 s à ×4, 8 s à ×0,5, 16 s à ×0,25.
- ×4 fait avancer la date quatre fois plus vite ; **Jeu en pause** arrête la date, la simulation continue.
- 2x et 4x sont un maximum : le jeu les baisse quand l'ordinateur ne suit pas (`game.tl:636-642`). Mesuré : 2x a donné 1,9x, 4x a donné 3,6x en moyenne.
- L'**Heure de la journée** et la météo sont une troisième horloge, visuelle : par défaut elles changent toutes seules, quel que soit le calendrier (`game_time_config.res.lua:5`, `weather_config.res.lua:5`).

## Ce qui suit le temps de jeu, quel que soit le calendrier

Ces choses sont comptées en temps de jeu, donc un calendrier ralenti ou en pause ne les ralentit pas :

- **Production** : le temps de production d'une industrie est une part fixe d'une année standard (`industry_react_util.tl:51`). La fenêtre de l'industrie l'affiche en jours du calendrier actuel (`industry_react_util.tl:23`) : à ×0,25, le même rythme affiche quatre fois moins de jours.
- **Remboursements d'emprunt** : un par mois standard de temps de jeu, même avec le calendrier en pause (`loan.script.tl:83-88`).
- **Délais des subventions** et la durée du bonus, 5 années standard (`subvention_util.tl:286`, `subvention_util.tl:290-292`).
- **Retour de la réputation des villes** (`towns.script.tl:121-130`), **effets des ouvriers**, comptés sur au plus 2 années standard (`industry_productivity_util.tl:3`), et **fermeture des industries** après des années sans desserte (`industries.script.tl:119-128`).
- **Notes de livraison** des villes, sur le dernier semestre (`town_util.tl:840`).
- **Nouvelles industries** : avec le calendrier en pause, 3 sont apparues en 1809 s de temps de jeu, à 760 s et 728 s d'écart, le même rythme qu'avec le calendrier qui tourne (environ 730 s). Mesuré avec [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) ; voir [Industries](industries.html).

Quand le calendrier tourne, le jeu affiche ces durées en années, mois et jours de la vitesse du calendrier actuelle (`util.tl:40-49`).

## Ce qui suit la date du calendrier

- **Nouveaux véhicules, gares et bâtiments** : ils apparaissent selon l'année (wiki officiel : « Different calendar speeds only affect the availability of vehicles and infrastructure »).
- **Coûts qui montent avec l'année** : l'entretien des bâtiments, les variantes d'époque, l'argent des subventions et les montants des emprunts suivent la date. Voir [Coûts, entretien et emprunts](costs.html).

## Avec le calendrier en pause

1. La date, et donc l'année, restent fixes : pas de nouveaux véhicules, et les coûts liés à l'année ne bougent pas.
2. Les durées sont affichées en **minutes et secondes** au lieu de jours (`util.tl:41-43`, `industry_react_util.tl:16-21`).
3. Un emprunt affiche son remboursement **par min** au lieu de par an (`finances_loan_gui.tl:223-231`), et la carte d'emprunt personnalisé ne peut pas être prise (`finances_loan_gui.tl:393`).
4. La production, les remboursements, les délais et la réputation gardent leur rythme de temps de jeu.

## Bon à savoir

- Tu veux plus de temps pour développer un réseau avant l'arrivée de nouveaux véhicules ? Baisse la vitesse du calendrier : ton revenu par minute de jeu ne change pas.
- La production affichée « par an » dépend de la vitesse du calendrier ; compare les industries à la même vitesse.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) garde des graphiques financiers lisibles avec le calendrier en pause.

```engine
La durée du jour, du mois et de l'année standard (getDefaultDayDuration et les autres) vient du moteur. Le script des villes compte un mois comme 30 × 4 secondes (`towns.script.tl:121`), ce qui correspond au jour mesuré de 4 secondes ; quelques autres constantes supposent encore un jour de 2 secondes (`cargotype.script.lua:3`, `mod.script.tl:172`).
```

```check
official: « By default a day in the game lasts 4 seconds. » « Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent. » ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: Vitesse du calendrier de ×0,25 à ×4 ou en pause, par rapport au jour standard ; la production, les emprunts, les subventions, la réputation et les minuteries des ouvriers tournent en temps de jeu ; un calendrier en pause affiche les durées en minutes, les remboursements par minute et bloque les nouveaux emprunts ; mesuré : 4 s par jour à ×1.
result: refines
```
