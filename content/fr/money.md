---
title: Pourquoi est-ce que je perds de l'argent ?
summary: Ce qui rapporte, ce qui coûte, et une vérification en six étapes pour trouver les lignes qui perdent de l'argent et pourquoi, avec des liens vers les pages qui expliquent chaque point.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-15
game: 40425
fact: 1 | paiement par unité, au consommateur, pour la ligne droite
fact: 0 | payé dans un entrepôt ou en correspondance
fact: 100 % | payé même en retard
fact: ×6 | facteur d'année affiché sur l'entretien des entrepôts, aérodromes, aéroports et ports en 2020
---

Une livraison paie pour **une seule ligne droite**, du lieu où le fret a été produit au lieu où il est utilisé, et seulement quand il y arrive. Tout ce que tu construis et achètes coûte de l'argent chaque année, une partie de plus en plus avec l'année du calendrier. Une ligne perd de l'argent quand sa part des paiements est plus petite que les coûts qu'elle apporte.

```diagram money_flow
```

## Ce qui rapporte

- **La distance à vol d'oiseau** de la source au consommateur, plus 8 × le dénivelé. La longueur de ton trajet ne compte pas (`cargo_income.script.lua:3-7`, `cargo_income.script.lua:5`).
- **Chaque fret paie pareil** par kilomètre : le facteur de revenu est 3,8 pour tous (`cargotype.script.lua:7-13`).
- **Une seule fois, au consommateur.** Décharger dans un entrepôt ou une gare de correspondance ne rapporte rien. Le paiement est ensuite partagé entre les lignes de la chaîne selon la longueur à vol d'oiseau de chaque étape (mesuré en jeu).
- **Le fret en retard est payé en entier** : le temps de trajet n'est pas utilisé (`cargotype.script.lua:7-13`). Le retard fait baisser à la place la note **Livraison** de la ville.
- **Le rang d'entreprise** baisse tous les revenus avec le réglage **Inflation** : au rang 15, ×0,75 en Normale (`company_progression_util.tl:25-40`).
- Un **contrat rempli** double, pendant 5 ans, le revenu des livraisons qu'il couvre : vers son industrie, vers sa ville, ou les passagers entre ses deux villes, sur ses lignes seulement (`subvention_util.tl:286`). Voir [Contrats : offres, délais et récompenses](subsidies.html).

Détails : [Revenus du fret et délai de livraison](income.html).

## Ce qui coûte

- **Véhicules** : les coûts d'exploitation suivent la vitesse moyenne × la capacité, et le prix vaut 6 ans de coûts d'exploitation (`model_metadata_util.lua:499-518`, `model_metadata_util.lua:548-549`).
- **Voies et routes** : environ un sixième du prix de construction par km et par an ; une voie à grande vitesse coûte 9 fois une voie simple (`simple.street_template.lua:33`, `high_speed.street_template.lua:35`).
- **Dépôts, gares, entrepôts, ports, aéroports** : les variantes d'époques plus récentes coûtent ×3 et ×9 (`rail_depot.con.lua:7`, `warehouse.tl:48`), et pour les entrepôts, aérodromes, aéroports et ports la fenêtre du bâtiment affiche un entretien qui suit l'année, de ×1 en 1900 à ×6 en 2020 (`mod.script.tl:92-100`, `entity_window_util.tl:188-192`). Ce qui est facturé est décidé par le moteur.
- **Emprunts** : le taux est compté une seule fois sur le montant, réparti sur la durée (`loan_util.tl:102-111`).
- **L'Inflation n'augmente aucun coût**. Elle baisse seulement les revenus.

Détails : [Coûts, entretien et emprunts](costs.html).

## Six vérifications, dans l'ordre

```diagram money_check
```

1. **Quelles lignes perdent de l'argent ?** Regarde le bilan de chaque ligne, pas le total de l'entreprise. Le mod [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) montre le bilan de chaque ligne sur les 12 derniers mois et sa moyenne sur plusieurs années.
2. **Le fret va-t-il loin ?** Seule la ligne droite de la source au consommateur paie. Une courte ligne d'apport vers un entrepôt ne reçoit que la part de sa propre courte étape ([Revenus du fret et délai de livraison](income.html)).
3. **Roule-t-elle pleine ?** Un véhicule coûte pareil plein ou vide. Regarde les retours à vide, le **niveau de remplissage** et le **chargement complet** de chaque arrêt ([Réglages de départ : chargement complet, niveau de remplissage et temps d'arrêt](departure.html)).
4. **Est-il déchargé là où il paie ?** Ce qui n'est pas dans la liste Charge d'un arrêt est déchargé dans tout stock proche, entrepôt compris, et un entrepôt ne paie rien ([Vitesse de chargement et de déchargement](loading.html), [Entrepôts](warehouses.html)). Le fret qui ne rentre pas dans des stocks de ville pleins reste à bord ([Croissance des villes : XP, notes et taille](towns.html)).
5. **Trop de véhicule ?** La vitesse et la capacité coûtent de l'argent, mais la vitesse ne paie pas : elle n'aide que si elle donne plus de trajets par an. En ville, un vieux bus lent peut être plus rentable qu'un neuf rapide ([Coûts, entretien et emprunts](costs.html)).
6. **Coûts fixes.** Les dépôts, les modules d'entrepôt en plus, les voies rapides et les bâtiments d'une époque plus récente coûtent chaque année, utilisés ou non ([Coûts, entretien et emprunts](costs.html)).

## Bon à savoir

- **Choisis les frets selon le volume et la distance**, pas selon le prix : chaque fret paie pareil par km.
- Une **longue ligne principale** alimentée par des lignes courtes gagne la plus grande partie de l'argent ; les lignes d'apport montrent de petits bilans, mais c'est la chaîne entière qui compte.
- **Plus à transporter** : une industrie boostée produit plus ([Travailleurs et bonus des travailleurs](workers.html), [Industries](industries.html)), et une ville plus grande demande plus de fret.
- Accélérer une ligne n'augmente pas le paiement par unité. Ça n'aide que si les mêmes véhicules font plus de trajets.

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks))
scripts: Pareil : ligne droite plus 8 × dénivelé, le même facteur pour chaque fret, temps de trajet non utilisé ; mesuré en jeu : payé une fois au consommateur et partagé selon la longueur des étapes ; les coûts suivent vitesse × capacité pour les véhicules, 1/6 du prix pour les voies, variantes d'époque ×3 / ×9 et facteur d'année ×1 à ×6 pour les bâtiments ; l'Inflation baisse seulement les revenus.
result: refines
```
