---
title: Revenus du fret et délai de livraison
summary: Ce que rapporte une livraison (distance à vol d'oiseau, montée, rang d'entreprise, contrats) et ce que coûte vraiment un retard.
domain: economy
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: 3,8 | le même facteur de revenu pour tous les frets
fact: +8 × montée | mètres de montée ajoutés à la distance
fact: 100 % | payé même quand la livraison est en retard
---

Une livraison paie la **distance à vol d'oiseau**, rien d'autre du trajet. La vitesse compte pour une autre raison : chaque fret a un **délai**, et les livraisons en retard font baisser la note **Livraison** de la ville, pas ton revenu.

```diagram income_formula
```

## La formule du revenu

Toute la formule tient dans un court script du jeu (`cargo_income.script.lua:10-13`) :

1. **Facteur de revenu** du fret. Tous les frets du jeu de base utilisent la même fonction et les mêmes prix (`initialPrice = 4`, `finalPrice = 3.2`), ce qui donne **3,8 pour les 36 frets** (`cargotype.script.lua:7-13`, `coal.cargo.lua:21-22`). Le charbon rapporte exactement autant que les marchandises sur la même distance.
2. Réglage **Revenu fret** : 50 %, 75 %, 100 %, 125 % ou 150 % (`difficulty_util.tl:38`, `mod.script.tl:211`). Les quatre préréglages de difficulté utilisent 100 % (`difficulty_util.tl:97`).
3. **Distance**, voir plus bas.

La fonction reçoit la durée du trajet mais **ne l'utilise pas** (`cargotype.script.lua:7-13`) : une livraison lente ou en retard rapporte autant.

## Distance : ligne droite plus montée

```diagram income_distance
```

- La distance est la **ligne droite en 3D** entre les deux points, pas la longueur de ton trajet (`cargo_income.script.lua:3-7`).
- Quand la différence de hauteur est positive, **8 × cette hauteur** est ajoutée (`cargo_income.script.lua:5`) : 100 m de montée rapportent comme 800 m de plus. Dans l'autre sens, rien n'est retiré.
- Une ligne sinueuse rapporte donc autant qu'une ligne droite, mais tu paies l'entretien de chaque mètre de voie ou de route construit.

```engine
Les deux points comparés (là où le fret est entré dans ton réseau, là où il a été livré) et le signe de la différence de hauteur sont décidés par le moteur. Le wiki officiel dit : « distances are measured as the crow flies between the source and the final destination ».
```

## Ce qui change encore le montant

| Quoi | Effet | Source |
|---|---|---|
| **Rang d'entreprise** avec le réglage Inflation | rang 1 : ×1, puis baisse régulière jusqu'au rang 15 : ×0,9 (Faible), **×0,75 (Normale)**, ×0,6 (Élevée), ×0,5 (Très élevée) ; Aucune : toujours ×1 | `company_progression_util.tl:25-40`, `difficulty_util.tl:50`, `mod.script.tl:694-697` |
| **Contrat rempli** | ×2 sur les lignes qui ont livré pour le contrat | `deliver_cargo.script.tl:463-469`, `deliver_cargo_town.script.tl:554-565` |
| **Livraison en retard** | aucun effet sur le revenu | `cargotype.script.lua:7-13` |

- Le multiplicateur de rang s'applique à **tous** les paiements de fret et de passagers (`company_growth.script.tl:159-170`). Les préréglages de difficulté utilisent l'Inflation Faible (Easy), Normale (Moyen), Élevée (Hard), Très élevée (Very Hard) (`difficulty_util.tl:108`).
- Le ×2 des contrats ne s'applique qu'aux lignes qui ont livré pendant le contrat, pour une durée limitée (wiki officiel, Subsidies).

## Passagers

Les passagers utilisent la même distance et un facteur de revenu fixe d'environ 3,61 (`cargotype.script.lua:50-53`), multiplié par **0,5 + le facteur de prix du billet du véhicule** (`cargo_income.script.lua:14-17`). Quand un modèle de véhicule ne définit pas son facteur de confort, le jeu met le facteur de prix à 0,3 pour les bus et trams, 0,9 pour les avions, 0,1 pour les bateaux et 0,5 pour les trains (`base_mod.lua:46-61`) ; pour les autres modèles, c'est une valeur du moteur, non visible dans les scripts. Un contrat de passagers double aussi le revenu sur sa ligne (`deliver_passengers.script.tl:284-298`).

## Délais de livraison

Chaque fret a son propre délai (`timeToDeliverInSeconds` dans chaque .cargo.lua, par exemple `meat.cargo.lua:30`, `coal.cargo.lua:30`). Les produits frais ont le plus court, les matières premières lourdes cinq fois plus long :

```diagram delivery_times
```

- **Finances › Délai de livraison** affiche le délai de chaque fret sur ta carte ; le calque de satisfaction du fret colore les trajets du vert au rouge.
- Une livraison est **retardée** quand elle arrive après son délai (`towns.script.tl:425`).
- Les modules d'entrepôt spécialisés **gèlent** le délai du fret qu'ils stockent (wiki officiel, Warehouses).

```engine
Le moteur transforme le temps de base en délai affiché dans Finances (les scripts le lisent avec getAdjustedDeliveryTime) et décide quand une unité est en retard. Seules les valeurs relatives ci-dessus viennent des fichiers de fret.
```

## Ce que coûte un retard : la note Livraison

Le fret en retard est payé en entier, mais chaque ville garde une note **Livraison** (`town_util.tl:505-519`) :

1. Le jeu compte les livraisons vers la ville sur le **dernier semestre**, et combien étaient en retard (au moins 10 sont supposées, pour que les premières livraisons ne la fassent pas basculer).
2. Part à l'heure → note : sous une limite basse la note vaut 0, au-dessus d'une limite haute elle vaut 1, linéaire entre les deux. Avec la sensibilité par défaut (**Normale**) : **30 % à l'heure → 0, 100 % → 1**, donc 90 % à l'heure donnent 0,86.
3. Le réglage **Sensibilité aux livraisons** déplace les limites (`difficulty_util.tl:47`). Désactivé : toujours 1. Préréglages : Easy Faible, Moyen Normale, Hard Élevée, Very Hard Très élevée (`difficulty_util.tl:113`).

```diagram delivery_rating
```

Livraison est l'une des six notes dont la plus basse fixe le taux de croissance de la ville : une seule note Très insuffisant arrête la ville (voir [Croissance des villes](towns.html)).

## Exemple

La même livraison de charbon, à 5 km à vol d'oiseau.

| Situation | Payé |
|---|---|
| à plat, quelle que soit la longueur du trajet | **100 %** |
| à 10 km | **200 %** |
| destination 100 m plus haut | **116 %** |
| livrée en retard | **100 %** (la note Livraison baisse) |
| rang d'entreprise 15, Inflation Normale | **75 %** |
| ligne d'un contrat rempli | **200 %** |

## Bon à savoir

- Comme tous les frets paient pareil au kilomètre, **choisis tes frets selon le volume, la distance et le délai**, pas selon le prix.
- Les délais comptent surtout pour la viande, le poisson, les légumes et les boissons : lignes courtes, ou entrepôts qui gèlent le délai.
- Chaque unité livrée à un bâtiment de ville donne aussi de l'expérience à cette ville (`town_growth.script.tl:642`, `town_growth_config.res.lua:5`).

```check
official: « The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'. » « While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth. » ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks), [Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Même facteur 3,8 pour tous les frets ; distance en 3D plus 8 × la montée ; le rang d'entreprise baisse le revenu jusqu'à ×0,75 au rang 15 (Inflation Normale) ; ×2 après un contrat ; la durée n'est pas utilisée pour le revenu ; note Livraison selon la part à l'heure du dernier semestre (Normale : 30 % → 0, 100 % → 1).
result: refines
```
