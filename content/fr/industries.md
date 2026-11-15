---
title: Industries
summary: Règles de production, stocks, parcelles et extension, fret booster, pourquoi une industrie n'est pas boostée, et quand une industrie inutilisée ferme vraiment.
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
fact: 5 ans | sans chargement ni consommation font d'une industrie une candidate à la fermeture
fact: 1,1 % | de chance par an à Rarement (le défaut), puis 730 jours de compte à rebours
fact: +50–150 % | de bonus du fret booster, fixe pour chaque industrie
fact: 3 mois | de bonus par lot de fret booster
---

Chaque industrie fonctionne par **règles** : « prendre ceci dans les stocks entrants, mettre cela dans les stocks sortants », un nombre fixe de fois par an. Les industries primaires (mines, fermes, puits) n'ont besoin d'aucune entrée ; leur taille vient de leurs **parcelles**. Deux bonus peuvent multiplier la production : le **fret booster** (industries primaires seulement) et les **travailleurs**.

## Règles de production

- Une règle donne le fret utilisé et produit par cycle, et combien de cycles par an : un cycle dure un an ÷ ce nombre (`industry_react_util.tl:51-57`). La section Production de la fenêtre de l'industrie l'affiche en petits nombres.
- Le nombre **Max.** de la fenêtre vaut : par cycle × cycles par an × les bonus × le réglage **Productivité des industries** (`industry_util.tl:310-379`).
- **Productivité des industries** : 50 %, 75 %, 100 %, 150 % ou 200 %. Préréglages : Facile 150 %, Normale 100 %, Difficile 75 %, Très difficile 50 % (`difficulty_util.tl:41`, `difficulty_util.tl:93`, `difficulty_util.tl:120`, `difficulty_util.tl:148`, `difficulty_util.tl:175`, `mod.script.tl:196-197`).
- Exemple, Acierie : 6 minerai de fer + 6 charbon → 3 acier + 4 tôle, 121,7 cycles par an : 730 minerai de fer et 730 charbon → 365 acier et 487 tôle (`steel_mill.con.lua:43-71`). Une entrée qui manque arrête la règle.
- La Conserverie a deux règles : poisson + tôle, ou viande + tôle (`food_factory.con.lua:43-74`).

```engine
Le moteur exécute les règles. Il peut rallonger un cycle : l'infobulle du cycle affiche alors « (+ … En raison du délai de livraison) » (`industry_react_util.tl:61-76`). Quand et de combien n'est pas dans les scripts : la production réelle peut donc rester sous le Max.
```

## Stocks

- Chaque fret a son propre stock avec une limite : par ex. une Mine de charbon garde 100 outils et 400 charbon, une Acierie 800 minerai de fer, 800 charbon, 400 acier et 500 tôle (`coal_mine.con.lua:44-67`, `steel_mill.con.lua:43-71`).
- Les stocks ne se dégradent jamais (`industryutil.lua:25-29`) : le fret attend aussi longtemps qu'il faut.
- Un stock sortant plein n'arrête pas la production : le surplus est jeté (wiki officiel). Le graphique **Flux de fret** montre **Consommé**, **Produit** et **Détruit** (`industry_eow.script.tl:804-816`).
- Avec le paramètre de construction **Entrée** sur Désactivé, les règles perdent leurs entrées et l'industrie n'a pas de stocks entrants (`industryutil.lua:280-287`, `industryutil.lua:383-387`, `industryutil.lua:432-441`).

## Parcelles et extension

- Les industries primaires et la Ferme d'élevage ont des **parcelles** (champs, puits de mine, derricks). Leur niveau est leur nombre de parcelles (`industryutil.lua:602-617`).
- La règle grandit avec les parcelles : production par cycle × parcelles ÷ **toutes les parcelles de ce type d'industrie**, arrondi, au moins 1. Les entrées baissent dans la même proportion (`industryutil.lua:225-259`). Une Mine de charbon (8 types de parcelles) avec 4 parcelles fait 8 charbon par cycle au lieu de 16.
- Chaque industrie reçoit un maximum : au hasard entre la moitié des parcelles et toutes, ou Petite / Moyenne / Grande (50 / 75 / 100 %) avec le paramètre **Taille de l'industrie** (`industryutil.lua:519-537`). Une mine dont le maximum est 5 sur 8 n'atteint jamais la règle complète.
- Tous les six mois, le jeu peut ajouter **une parcelle** (`industries_config.res.lua:5`, `industries.script.tl:158-183`). La chance vaut (note − 25 %) ÷ 50 %, où note = note de production × la part de la production que tu expédies (au plus 1) : 25 % ou moins jamais, 75 % ou plus toujours (`industries.script.tl:172-176`).
- Donc une industrie dont tu n'expédies pas le fret **ne grandit jamais**. Les usines n'ont pas de parcelles et ne grandissent jamais.
- Au maximum la fenêtre affiche **L'industrie a atteint son plein potentiel de développement.** ; quand des bâtiments, voies ou routes gênent, **L'industrie ne peut plus se développer davantage.** (`industry_react_util.tl:588-602`, `industries.script.tl:13-38`). Aucun script ne retire de parcelles ; le wiki officiel dit que des parcelles rasées baissent la production.

```engine
La note de production (getProductionRating), la production annuelle et la quantité expédiée (getCargoOutputPerYear, getCargoShippedPerYear), et l'endroit où va une nouvelle parcelle (makeIndustryExtendProposal) sont des valeurs du moteur.
```

## Fret booster

Les 13 industries primaires ont une deuxième règle, le **booster** : il prend un lot de fret booster dans le stock entrant 4 fois par an et donne un bonus tant qu'il tourne.

| Industrie | Parcelles | À taille pleine, par an | Lot booster (4 par an) | Source |
|---|---|---|---|---|
| Carrière d'argile | 8 | 365 argile | 12 outils | `clay_pit.con.lua:42-82` |
| Mine de charbon | 8 | 320 charbon | 13 outils | `coal_mine.con.lua:44-85` |
| Ferme de coton | 21 | 274 laine | 17 engrais | `cotton_farm.con.lua:42-98` |
| Exploitation agricole | 20 | 274 céréales + 183 légumes | 17 engrais | `farm.con.lua:44-106` |
| Zone de pêche | 18 | 263 poisson | 12 outils | `fishing_grounds.con.lua:44-101` |
| Camp de bûcherons | 20 | 243 bois | 15 machines | `forest.con.lua:44-99` |
| Mine de fer | 8 | 365 minerai de fer | 15 machines | `iron_ore_mine.con.lua:44-84` |
| Plateforme pétrolière | 9 | 365 pétrole brut | 12 machines | `oil_platform.con.lua:45-96` |
| Site pétrolier | 14 | 548 pétrole brut | 15 machines | `oil_well.con.lua:44-94` |
| Carrière | 7 | 365 pierre | 12 outils | `quarry.con.lua:44-83` |
| Plantation d'hévéas | 23 | 365 caoutchouc | 17 engrais | `rubber_farm.con.lua:41-102` |
| Drague à sable | 9 | 365 sable | 15 machines | `sand_excavator.con.lua:44-92` |
| Carrière de sable | 8 | 365 sable | 12 outils | `sand_pit.con.lua:44-84` |

- Le bonus est tiré une fois par industrie : **+50 % à +150 %**, arrondi à 1 % (`industryutil.lua:394-405`). La section Booster l'affiche en « +X % » (`industry_util.tl:428-434`). Avec le paramètre **Facteur d'amplification**, il vaut à la place +50 %, +75 %, +100 %, +125 % ou +150 % (`industryutil.lua:289-299`).
- La fenêtre montre le booster actif tant que son dernier lot dure (3 mois), ou dès que le stock contient un lot complet (`industry_util.tl:55-91`).
- Le lot ne diminue **pas** avec les parcelles : une petite mine demande autant d'outils qu'une grande (`industryutil.lua:227-229`).
- Les deux bonus se multiplient : production × facteur travailleurs × (1 + bonus booster) (`industry_util.tl:42-104`).

## Le bonus des travailleurs

La moitié des emplois (10 sur 20) doit être occupée par des habitants **arrivés par tes lignes de passagers** au cours des 2 dernières années ; le facteur vaut ×1,5 à ×2,5, fixe pour chaque industrie (`industry_productivity_util.tl:35-72`). Les travailleurs seulement attribués ne comptent pas. Détails : [Travailleurs et bonus des travailleurs](workers.html).

## Pourquoi mon industrie n'est pas boostée ?

1. **Pas une industrie primaire** : les usines n'ont pas de règle booster, seulement le bonus des travailleurs (`steel_mill.con.lua:61-70`).
2. **Lot incomplet** : le stock doit contenir un lot complet, par ex. 13 outils pour une Mine de charbon. Sous 4 lots par an (52 outils), le bonus s'arrête entre deux livraisons.
3. **Mauvais fret** : outils, machines ou engrais selon l'industrie (tableau ci-dessus).
4. **Travailleurs** : attribués ne suffit pas ; la section Booster compte les arrivées (« 12/10 ») (`industry_react_util.tl:617-654`). Voir [Travailleurs et bonus des travailleurs](workers.html).

## Quand une industrie inutilisée ferme-t-elle ?

```diagram ind_closure
```

La vérification passe toutes les 100 mises à jour pour chaque industrie (`industries.script.tl:84-85`) :

1. **Candidate** : aucun fret **chargé** dans un véhicule et aucun **consommé** pendant **5 ans** (comptés depuis sa construction si jamais) (`industries.script.tl:104-119`, `industries_config.res.lua:6`). Produire seul ne compte pas.
2. **Hasard** : chaque année, une candidate est marquée avec la chance du réglage **Fréquence de fermeture des industries** (tableau ci-dessous) (`industries.script.tl:120-131`).
3. **Compte à rebours** : la notification **Fermeture de l'industrie** apparaît, avec 2 ans (730 jours) à attendre (`industries_config.res.lua:7`, `industry_close.script.tl:53-67`). Ensuite l'industrie est supprimée avec ses propres morceaux de route (`industries.script.tl:147-155`, `industry_util.tl:560-601`).
4. **Sauvée** : un seul chargement ou une consommation pendant le compte à rebours l'annule (`industries.script.tl:134-137`). Accepter un contrat **Approvisionner l'industrie** ou **Transporter des travailleurs** pour elle l'annule aussi (`subvention_util.tl:473-484`).

| Fréquence de fermeture des industries | Chance par an en tant que candidate | La moitié des candidates marquées après | Préréglage | Source |
|---|---|---|---|---|
| Jamais | 0 | jamais | Facile | `difficulty_util.tl:94` |
| Rarement (défaut) | 1,1 % | environ 63 ans | Normale | `difficulty_util.tl:121` |
| Parfois | 2,2 % | environ 32 ans | Difficile | `difficulty_util.tl:149` |
| Souvent | 4,4 % | environ 16 ans | – | `difficulty_util.tl:37` |
| Très souvent | 8,8 % | environ 8 ans | Très difficile | `difficulty_util.tl:176` |

La chance vaut 0,011 par an × 0, 1, 2, 4 ou 8 (`mod.script.tl:171`, `mod.script.tl:202-203`, `difficulty_util.tl:37`). Les industries qui t'appartiennent ne ferment jamais, ni celles en développement manuel, ni aucune pendant le tutoriel (`industries.script.tl:94-102`).

```engine
Ce qui compte comme « chargé » et « consommé » (les journaux itemsLoaded et itemsConsumed, par ex. si le fret booster compte), l'indicateur manualDevelopment, et pourquoi les industries avec un dépôt sont laissées de côté (`industries.script.tl:140-146`) relèvent du moteur. De même que ce que fait le moteur d'une règle booster qui a perdu son entrée (Entrée désactivée).
```

## Nouvelles industries

- Le moteur ajoute des industries avec le temps ; les scripts lui donnent seulement un temps cible de 50 ans, un exposant de 3, et aucune nouvelle industrie dans l'éditeur de cartes (`mod.script.tl:166-168`). Le réglage **Densité cible des industries** le fait varier (`mod.script.tl:194-195`). La notification est **Industrie fondée** (`industry_spawn.res.lua:6`).
- L'atout d'entreprise **Prospection de ressources** cherche une nouvelle industrie de cette ressource près d'une ville : un essai par mois avec une chance de 20 % à 60 %, pendant 6 mois ; en cas d'échec, le permis revient (`company_util.tl:14-17`, `company.script.tl:96-142`, `company.script.tl:299-307`).

```engine
Où et quand une nouvelle industrie apparaît, et de quel type, est décidé par le moteur (makeIndustrySpawnProposal).
```

## Bon à savoir

- Expédie depuis chaque industrie primaire que tu veux voir grandir : une production non expédiée bloque l'extension, quels que soient les bonus.
- Mets le fret booster sur les plus grandes mines et fermes : le lot coûte pareil, le bonus suit les parcelles.
- Les stocks ne se dégradent pas : tu peux livrer le fret booster d'avance, jusqu'à la limite du stock (100).
- Les bonus augmentent le bruit et la pollution : une Mine de charbon passe de 10 de pollution à 20 avec un bonus et 30 avec deux (`coal_mine.con.lua:99-117`).
- Au réglage par défaut une industrie inutilisée ferme rarement ; à Très souvent, charge quelque chose de temps en temps.

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 5 ans, pas 10, et la production ne compte pas : seulement le fret chargé dans un véhicule ou consommé. Après ces 5 ans l'industrie n'est qu'une candidate : chaque année elle est marquée avec une chance de 1,1 % (Rarement) à 8,8 % (Très souvent). Le compte à rebours dure bien 730 jours. Le fret booster donne +50 % à +150 % par industrie, par lots qui durent 3 mois.
result: differs
```
