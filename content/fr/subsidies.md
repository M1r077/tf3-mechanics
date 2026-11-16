---
title: Contrats : offres, délais et récompenses
summary: Les quatre types de contrats, ce qui les remplit vraiment, ce que tu gagnes et ce que tu risques, et à quel rythme arrivent les offres.
domain: subsidies
official: gamemanual:management:subsidies
status: verified
updated: 2026-11-15
game: 40425
fact: 4 | types de contrats en partie libre
fact: 5 | contrats acceptés au plus en même temps
fact: ×2 | revenus pendant 5 ans sur les lignes qui ont livré
fact: 0 | pénalité pour avoir refusé une offre
---

Un contrat (appelé subvention dans les fichiers du jeu) : une industrie ou une ville propose une tâche, tu reçois quelque chose en acceptant, davantage si tu la remplis à temps, et tu rembourses l'avance plus une pénalité si tu dépasses le délai. Refuser une offre, ou la laisser expirer, ne coûte rien.

```diagram subsidy_life
```

## Les quatre types de contrats

```diagram subsidy_types
```

| Contrat | Cible | Ce qui le remplit | Source |
|---|---|---|---|
| **Approvisionner l'industrie** | une industrie qui n'a jamais rien produit | le nombre demandé de livraisons chez elle, **n'importe lequel de ses intrants** | `deliver_cargo.script.tl:54-61`, `deliver_cargo.script.tl:230-234`, `deliver_cargo.script.tl:470-479` |
| **Approvisionner la ville** | un fret que la ville demande et ne reçoit pas du tout | le nombre demandé d'unités **de ce fret** livrées aux bâtiments de la ville | `deliver_cargo_town.script.tl:566-581` |
| **Relier des villes** | deux villes | **un seul** passager qui commence un trajet entre les deux villes sur une ligne qui s'arrête dans les deux | `deliver_passengers.script.tl:263-280`, `subvention_util.tl:561-592` |
| **Transporter des travailleurs** | une industrie qui expédie ou reçoit déjà du fret, pas encore boostée | son bonus des travailleurs devient actif (la moitié de ses emplois) | `deliver_workers.script.tl:121-131`, `deliver_workers.script.tl:152-156` |

- Chaque nouvelle offre tire un des types qui peuvent apparaître à ce moment, avec les mêmes chances (`subventions.script.tl:147-169`).
- **Approvisionner l'industrie** et **Approvisionner la ville** comptent des livraisons, pas des trajets : chaque unité payée qui arrive à la cible ajoute 1. Les correspondances sont permises (`deliver_cargo.script.tl:470-479`).
- **Relier des villes** ne demande aucun nombre de passagers : le premier passager qui monte dans ta ligne entre les deux villes le remplit. « Sans correspondance » veut dire que ce trajet se fait sur une seule ligne qui dessert les deux villes. Aucune offre n'apparaît si une ligne transporte déjà des passagers entre elles (`deliver_passengers.script.tl:72-78`).
- Les villes proches sont bien plus probables : le poids d'une paire vaut 100 × un facteur de distance à la puissance 7 (1 à 1 km ou moins, 0,01 à 20 km), plus une valeur d'au moins 1 par ville que le moteur lit à la position de la ville dans sa grille d'infrastructure du joueur (`deliver_passengers.script.tl:154-156`, `deliver_passengers.script.tl:175-191`). Au-delà d'environ 10 km, la part de la distance est presque nulle et il ne reste que cette valeur du moteur.
- **Approvisionner la ville** préfère les frets déjà produits quelque part sur la carte : 16 fois plus probables que les autres (`deliver_cargo_town.script.tl:277-280`).
- La quantité à livrer dépend du réglage **Risque des missions** :

| Risque des missions | Approvisionner l'industrie | Approvisionner la ville (au plus la demande de la ville) | Source |
|---|---|---|---|
| Aucun(e) | 10 à 50 | 10 à 30 | `deliver_cargo.script.tl:100-114`, `deliver_cargo_town.script.tl:165-188` |
| Équitable | 50 à 100 | 30 à 100 | |
| Risqué | 75 à 150 | 35 à 125 | |
| Très risqué | 150 à 300 | 45 à 150 | |

## Qu'est-ce qu'une liaison sans correspondance ?

La carte **Relier des villes** demande : « Créez une liaison sans correspondance entre {fromTownName} et {toTownName} et transportez des passagers entre les deux villes. » (`deliver_passengers.script.tl:14`).

- **Une ligne avec un arrêt dans chaque ville.** Le jeu parcourt les arrêts de la ligne et prend la ville de chacun ; la ligne compte quand au moins un arrêt se trouve dans chacune des deux villes. Les autres arrêts, leur ordre et le type de véhicule (bus, tram, train, bateau, avion) ne comptent pas (`subvention_util.tl:561-592`).
- **Un seul passager le remplit** : le premier passager qui prend cette ligne d'un arrêt d'une ville jusqu'à un arrêt de l'autre, dans un sens ou dans l'autre (`deliver_passengers.script.tl:263-280`, `deliver_passengers.script.tl:210-218`). Le contrôle ne regarde que ce trajet, donc changer de ligne avant ou après ne devrait pas compter.
- **La ville d'un arrêt** est la ville de la première gare de son groupe de gares (`town_util.tl:1844-1873`). La ville à laquelle appartient une gare est décidée par le moteur.
- **Aucune offre** quand une ligne a déjà un arrêt qui charge des passagers dans chaque ville et un véhicule qui prend des passagers (`deliver_passengers.script.tl:72-78`). Une ligne de fret seul entre elles ne bloque pas l'offre.
- Le contrat se termine en **Contrat retiré** quand l'une des deux villes, ou la ligne qui l'a rempli, change d'une manière que le jeu compte comme une nouvelle version (`deliver_passengers.script.tl:232-240`).

```engine
La ville à laquelle appartient une gare (stationSystem.getTown), le moment exact où un passager « commence à utiliser » une ligne (OnStartedLineUsage) et les modifications d'une ligne qui comptent comme une nouvelle version relèvent du moteur. On n'a pas testé si une modification de la ligne après la réalisation met fin à l'effet Revenus 2x.
```

## Récompenses et pénalités

Chaque contrat garde trois listes, affichées sur sa carte comme **À l'acceptation**, **À la réalisation** et **En cas d'échec** (`subvention_util.tl:449-471`). En cas d'échec, tout ce qui a été donné à l'acceptation est repris, plus une pénalité, ou deux pour Relier des villes, une perte de réputation dans chaque ville (`subvention_util.tl:457-463`, `deliver_cargo.script.tl:134-136`, `deliver_passengers.script.tl:111-114`).

| Contrat | À l'acceptation | À la réalisation | En cas d'échec | Source |
|---|---|---|---|---|
| Approvisionner l'industrie | argent | seulement l'effet **Revenus 2x** | avance remboursée + amende | `deliver_cargo.script.tl:120-136` |
| Approvisionner la ville | argent **ou** réputation dans la ville | expérience de la ville **ou** argent, plus Revenus 2x | avance remboursée + perte de réputation **ou** amende | `deliver_cargo_town.script.tl:194-229` |
| Relier des villes | argent, plus pour des villes éloignées | expérience dans **les deux** villes, plus Revenus 2x | avance remboursée + perte de réputation dans **les deux** villes | `deliver_passengers.script.tl:105-119` |
| Transporter des travailleurs | argent | argent | avance remboursée + amende | `deliver_workers.script.tl:92-116` |

- **Argent**, avant l'effet de l'année : avance de 1,5 M à 3,75 M × le facteur de risque (Aucun ×2, Équitable ×1, Risqué ×0,75, Très risqué ×0,5, ou ×0,625 pour Relier des villes et Transporter des travailleurs), et pour Relier des villes aussi × le facteur de distance (0,3 à 3,0) ; amende de 3 M à 6 M ; paiement à la réalisation de 3,75 M à 11,25 M (`deliver_cargo.script.tl:100-128`, `deliver_passengers.script.tl:82-106`, `deliver_workers.script.tl:64-104`).
- L'argent suit l'**année du calendrier**, pas le réglage Inflation : ×1 en 1900, montée régulière jusqu'à ×4 en 2000 et après, arrondi au-dessus à 10 000 (`finances_util.tl:87-90`). Il est compté en **Contrats** dans les finances (`subvention_util.tl:126-135`).
- **Approvisionner la ville** ne peut avoir un paiement en argent à la réalisation et une amende en argent que si ton compte est sous 100 M au moment où l'offre est créée ; au-dessus, seule 1 offre sur 10 le peut encore, les autres donnent de l'expérience à la ville et retirent de la réputation à la place. L'avance n'est pas concernée (`deliver_cargo_town.script.tl:194-229`).
- L'**expérience de la ville** est une part de son niveau actuel : 20 % à 100 % de l'XP entre son niveau et le suivant (`deliver_cargo_town.script.tl:216`, `town_growth.script.tl:605-608`). Pour **Relier des villes**, elle est multipliée par le facteur de distance, de 0,3 à 1 km jusqu'à 3,0 à 20 km : des villes éloignées peuvent gagner plusieurs niveaux (`deliver_passengers.script.tl:94-96`, `deliver_passengers.script.tl:116-118`).
- La **réputation** perdue après un échec apparaît dans la note Réputation de la ville comme **Contrat échoué** (`towns.script.tl:313-334`). La réputation gagnée à l'acceptation retire seulement des pénalités existantes, elle ne dépasse jamais le maximum (`town_util.tl:1644-1647`).

## L'effet Revenus 2x

- Il dure **60 mois** (5 ans) après la réalisation du contrat (`subvention_util.tl:286`, `subvention_util.tl:292`).
- **Approvisionner l'industrie** : les livraisons à cette industrie, sur les lignes qui l'ont livrée pendant le contrat (`deliver_cargo.script.tl:463-469`).
- **Approvisionner la ville** : les livraisons à n'importe quel bâtiment de la ville, **tout fret**, sur les lignes qui ont livré le fret du contrat (`deliver_cargo_town.script.tl:554-565`).
- **Relier des villes** : les passagers entre les deux villes, sur **une seule** ligne directe : la dernière ligne directe où un passager entre elles est monté. Cela continue de se mettre à jour après le contrat : avec deux lignes directes, le ×2 peut passer de l'une à l'autre (`deliver_passengers.script.tl:263-296`).
- **Transporter des travailleurs** n'a pas d'effet sur les revenus (`deliver_workers.script.tl:90`).
- Pour Approvisionner l'industrie et Approvisionner la ville, une ligne qui ne commence à livrer qu'après la réalisation n'a rien : la liste des lignes n'est remplie que pendant le contrat.
- Deux contrats ne doublent jamais deux fois le même paiement : quand plusieurs correspondent, seule la dernière réponse est utilisée (`subventions.script.tl:570-583`).

```tip scripts
**Tu veux le revenu doublé d'Approvisionner l'industrie ou d'Approvisionner la ville sur plusieurs lignes ? Fais-les toutes livrer avant que le contrat soit réalisé.** Une ligne ajoutée après n'a rien. Relier des villes ne double qu'une seule ligne, la dernière ligne directe où des passagers sont montés : garde une seule ligne directe entre les deux villes.
```

```engine
La façon dont le ×2 d'un contrat se combine avec le multiplicateur du rang de l'entreprise (réglage Inflation) est décidée par le moteur : les deux scripts ne renvoient qu'un multiplicateur pour chaque paiement. Ce qu'est une entrée de paiement (sans doute une unité de fret ou un passager) est aussi décidé par le moteur.
```

## Délais

Le délai commence quand tu acceptes. Il est plus long quand le fret doit venir de loin et plus court avec un risque plus élevé (facteur de risque Aucun ×2, Équitable ×1, Risqué ×0,75, Très risqué ×0,5, ou ×0,625 pour les contrats de passagers et de travailleurs) :

| Contrat | Délai en mois | Distance utilisée | Source |
|---|---|---|---|
| Approvisionner l'industrie, Approvisionner la ville | (6 + 32 × E) × facteur de risque | jusqu'à l'industrie la plus proche qui produit le fret | `deliver_cargo.script.tl:116-117` |
| Relier des villes | (9 + 4 × E) × facteur de risque | entre les deux villes | `deliver_passengers.script.tl:98-99` |
| Transporter des travailleurs | (6 + 15 × E) × facteur de risque × facteur d'époque (×1,75 avant 1940, ×1,25 avant 1980) | jusqu'à la ville la plus proche | `deliver_workers.script.tl:75-87` |

E est le temps qu'un train à la vitesse maximale de l'époque (120 km/h dès 1900 jusqu'à 300 km/h dès 1981) met pour cette distance, arrondi au-dessus, au moins 1 (`subvention_util.tl:486-489`, `vehicle_util.tl:225-230`).

- Une offre non acceptée disparaît après environ **6 mois** (150 à 210 jours), sans pénalité (`subvention_util.tl:284`, `subvention_util.tl:290`).
- Tant qu'un contrat **Approvisionner l'industrie** ou **Transporter des travailleurs** court, l'industrie ciblée ne peut pas fermer : une fermeture prévue est annulée (`subvention_util.tl:473-484`).
- Si la cible disparaît ou est reconstruite pendant le contrat, le jeu affiche **Contrat retiré**, mais les pénalités d'échec s'appliquent comme pour un délai dépassé (`subventions.script.tl:172-190`, `subvention_util.tl:406-412`).
- Il n'y a pas de bouton pour annuler un contrat accepté.

```engine
La durée d'un mois de jeu, et donc la vraie longueur des délais, est fixée par le moteur (getDefaultMonthDuration). Les formules ci-dessus sont en mois du calendrier du jeu.
```

## À quel rythme arrivent les offres

- **Missions disponibles** : Rarement, Parfois (par défaut), Souvent, Très souvent donnent une nouvelle offre tous les 12, 6, 3 ou 1 mois ; **Jamais** désactive les contrats (`subvention_util.tl:13-38`, `mod.script.tl:247-248`).
- L'intervalle grandit avec le **rang de l'entreprise** : ×1 au rang 1 jusqu'à ×2 au rang 15 (`subvention_util.tl:19-22`).
- **Refuser** une offre divise l'intervalle suivant par deux ; accepter ou une nouvelle offre le remet à la normale (`subventions.script.tl:429`, `subventions.script.tl:395`, `subventions.script.tl:118`).
- Plus aucune offre tant que **5 contrats** acceptés sont en cours (`subventions.script.tl:23`, `subventions.script.tl:256-262`). La première offre arrive après un demi-mois.
- La même cible (industrie, ville et fret, paire de villes) n'est proposée **qu'une fois par partie**, même après un contrat manqué ou échoué (`subventions.script.tl:107-113`, `subventions.script.tl:186`).
- Préréglages de difficulté, disponibilité / risque (`difficulty_util.tl:104-105`, `difficulty_util.tl:132-133`, `difficulty_util.tl:159-160`, `difficulty_util.tl:186-187`) : Facile Souvent / Aucun(e), Normale Parfois / Équitable, Difficile Rarement / Risqué, **Très difficile Jamais** : aucun contrat.
- La vérification qui n'autoriserait les contrats que dans les villes notées Très bon existe, mais elle est désactivée (`town_util.tl:1574-1580`, `deliver_cargo_town.script.tl:272-275`).

## Bon à savoir

- Accepte sans crainte quand la cible est facile : refuser ou ignorer ne coûte rien, mais **échouer** coûte l'avance plus une amende qui peut dépasser l'avance.
- Pour **Approvisionner la ville** et **Approvisionner l'industrie**, livre avec toutes les lignes qui doivent en profiter : seules les lignes qui ont livré pendant le contrat ont les Revenus 2x pendant 5 ans.
- **Relier des villes** avec des villes éloignées donne le plus d'expérience, et ne demande qu'un seul passager.
- **Approvisionner l'industrie** ne paie rien de plus à la réalisation : sa récompense, ce sont les Revenus 2x seuls.

```check
official: "Accept an offer to begin the contract; declining it has no penalty." "Possible rewards include town experience, an additional payment, or a limited-time 2x income effect on eligible transport lines." "The upfront reward is reversed, and an additional fine or loss of town reputation may apply." ([Subsidies](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:subsidies))
scripts: Quatre types ; un seul passager remplit Relier des villes ; le ×2 dure 60 mois sur les lignes qui ont livré pendant le contrat ; Approvisionner l'industrie ne donne que le ×2 ; argent selon l'année (×1 à ×4) ; une nouvelle offre tous les 1 à 12 mois, plus rare à haut rang ; au plus 5 acceptés ; chaque cible proposée une fois par partie.
result: refines
```
