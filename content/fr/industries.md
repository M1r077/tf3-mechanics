---
title: Industries
summary: Règles de production, stocks, parcelles et extension, pourquoi une industrie ne grandit pas ou n'est pas boostée, quand une industrie inutilisée ferme, et comment de nouvelles industries apparaissent.
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
fact: 5 ans | sans chargement ni consommation font d'une industrie une candidate à la fermeture
fact: 1,1 % | de chance par an à Rarement (le défaut), puis 730 jours de compte à rebours
fact: +50–150 % | de bonus du fret booster, fixe pour chaque industrie
fact: 3 mois | de bonus par lot de fret booster
fact: ×2/3 – ×1,5 | Densité cible des industries : les nouvelles industries ne peuvent pas être désactivées
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
- Avec Moyenne, si 75 % arrondi donne toutes les parcelles, le maximum vaut toutes les parcelles moins une (`industryutil.lua:523-526`). Une nouvelle industrie démarre avec les parcelles que le moteur construit à la pose ; son niveau est fixé d'après elles (`industryutil.lua:602-617`).
- Tous les six mois de **temps de jeu**, le jeu peut ajouter **une parcelle** (`industries_config.res.lua:5`, `industries.script.tl:161-167`). C'est une demi-année standard : la vitesse du calendrier ne change pas la fréquence (voir [Temps de jeu et calendrier](time.html)).
- La chance vaut (note − 25 %) ÷ 50 %, où note = note de production × la part de la production que tu expédies (au plus 1) : 25 % ou moins jamais, 75 % ou plus toujours (`industries.script.tl:168-179`).
- Donc une industrie dont tu n'expédies pas le fret **ne grandit jamais**. Les usines n'ont pas de parcelles et ne grandissent jamais.
- Au maximum la fenêtre affiche **L'industrie a atteint son plein potentiel de développement.** ; quand des bâtiments, voies ou routes gênent, **L'industrie ne peut plus se développer davantage.** (`industry_react_util.tl:588-602`, `industries.script.tl:13-38`). Aucun script ne retire de parcelles ; le wiki officiel dit que des parcelles rasées baissent la production.
- Le script du jeu ignore les industries qui t'appartiennent, celles en développement manuel et celles en compte à rebours de fermeture : elles n'en reçoivent jamais de parcelle (`industries.script.tl:94-99`, `industries.script.tl:147-157`).

Exemple, **Camp de bûcherons** : 20 parcelles, 8 bois par cycle, 30,4 cycles par an (`forest.con.lua:54-66`, `forest.con.lua:75-98`). Par cycle il fait 8 × parcelles ÷ 20, arrondi, au moins 1 (`industryutil.lua:231-241`) :

| Parcelles (niveau) | Bois par cycle | Bois par an (Max., sans bonus, Productivité 100 %) |
|---|---|---|
| 1–3 | 1 | 30 |
| 4–6 | 2 | 61 |
| 7–8 | 3 | 91 |
| 9–11 | 4 | 122 |
| 12–13 | 5 | 152 |
| 14–16 | 6 | 183 |
| 17–18 | 7 | 213 |
| 19–20 | 8 | 243 |

La production monte par paliers : une nouvelle parcelle n'augmente pas toujours la production.

## Pourquoi mon industrie ne grandit pas ?

```diagram ind_growth
```

1. **Fret non expédié** : la note compte la part de la production chargée dans tes véhicules. Avec une note de production de 100 %, expédier 25 % ou moins ne donne aucune chance, 50 % une chance sur deux, 75 % ou plus une parcelle tous les six mois.
2. **Au maximum** : **L'industrie a atteint son plein potentiel de développement.** Le maximum est tiré à la construction (de la moitié à toutes les parcelles) et ne change jamais.
3. **Bloquée** : **L'industrie ne peut plus se développer davantage.** Retire les routes, voies ou bâtiments à l'emplacement de la prochaine parcelle (montré dans la fenêtre).
4. **Pas une industrie primaire** : les usines n'ont pas de parcelles.
5. **Compte à rebours de fermeture**, industrie à toi, ou développement manuel : pas de croissance par le script (ci-dessus).
6. **Aucune production** : une industrie qui ne produit rien dans l'année est ignorée (`industries.script.tl:168-171`).

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

Le moteur ajoute de nouvelles industries pendant la partie. La notification est **Nouvelle industrie fondée** : « Un entrepreneur visionnaire a flairé une opportunité de profit et a fondé {industry}. » (`industry_spawn.script.tl:34-36`, `industry_spawn.res.lua:6`). Aucun script du jeu ne choisit l'endroit, le type ou le moment, et aucun ne filtre ce que le moteur propose.

Ce que les scripts donnent au moteur (`mod.script.tl:128-133`, `mod.script.tl:166-168`, `mod.script.tl:194-195`) :

| Valeur de config | Valeur | Sens |
|---|---|---|
| spawnTargetTimeSpan | 50 × 365,25 jours standard | appelé « temps cible » : 50 années standard de temps de jeu |
| spawnProbabilityExponent | 3,0 | exposant de la chance d'apparition (formule dans le moteur) |
| spawnIndustries | désactivé dans l'éditeur de cartes, activé en partie | pas de nouvelles industries dans l'éditeur de cartes |
| industryDensity | 1 × **Densité cible des industries** | le nombre cible d'industries |
| maxNumberPerArea, absoluteMinimum | 0,8 par km² (0,64 sur consoles), 24 | aussi utilisé par le générateur de cartes |

**Densité cible des industries** (« Définissez la densité cible des industries sur la carte. ») : 5 crans, ×2/3, ×5/6, ×1, ×1,2, ×1,5 (`difficulty_util.tl:55`, `difficulty_util.tl:85`).

- Il se trouve dans les réglages avancés, partie économie (`advanced_settings.tl:287-291`), et ne fait pas partie des préréglages Facile … Très difficile (`difficulty_util.tl:90-199`).
- Dans le menu de nouvelle partie, **Densité des industries** (les industries au départ, mêmes 5 facteurs) met **Densité cible des industries** au même cran (`new_game_or_map_settings_page.tl:159-166`, `new_game_react_util.tl:288-296`). Change la cible ensuite dans les réglages avancés si tu veux deux valeurs différentes.
- **Aucun réglage ne le désactive** : le cran le plus bas est ×2/3. Seul l'éditeur de cartes n'a pas de nouvelles industries. Des mods le peuvent.
- Vitesse : le temps cible est en jours standard, comme toutes les règles de temps de jeu, donc la vitesse du calendrier et un calendrier en pause ne devraient pas le ralentir. Mesuré avec le calendrier en pause : en 1809 s de temps de jeu, 3 nouvelles industries sont apparues, à 760 s et 728 s d'écart, donc un calendrier en pause ne les arrête pas. Mesuré avec [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) sur 3 parties (environ 500 apparitions) : les nouvelles industries arrivent à environ **730 s** de temps de jeu d'écart à toutes les vitesses du calendrier (×4, ×1, ×0,5, ×0,25). Cela fait environ 45 jours du calendrier à ×0,25 et 2 ans à ×4.
- Prospection de ressources (ci-dessous) utilise le même appel du moteur avec une ville, donc une apparition « près d'une ville » existe dans le moteur (`company.script.tl:202`). Le tutoriel l'utilise aussi (`tutorial_init.tl:23-24`).

```engine
La formule derrière les 50 ans et l'exposant 3, la façon dont la densité cible est comptée (par surface de carte, par ville ?), le type choisi et l'endroit où l'industrie va (makeIndustrySpawnProposal) relèvent du moteur. Aucun script n'explique pourquoi plusieurs industries d'un même type peuvent apparaître côte à côte (« neuf mines de charbon les unes à côté des autres »), ni pourquoi certaines apparaissent à l'autre bout de la carte.
```

### Prospection de ressources

L'atout d'entreprise **Prospection de ressources** cherche une nouvelle industrie de cette ressource près d'une ville que tu choisis : un essai par mois, avec une chance qui monte de 20 % à 60 %, pendant 6 mois (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`). Si la ressource a plusieurs types d'industrie, ils sont essayés dans un ordre aléatoire (`company.script.tl:185-206`). Si tous les essais échouent, le permis revient (`company.script.tl:106-110`).

## Bon à savoir

- Expédie depuis chaque industrie primaire que tu veux voir grandir : une production non expédiée bloque l'extension, quels que soient les bonus.
- Mets le fret booster sur les plus grandes mines et fermes : le lot coûte pareil, le bonus suit les parcelles.
- Les stocks ne se dégradent pas : tu peux livrer le fret booster d'avance, jusqu'à la limite du stock (100).
- Les bonus augmentent le bruit et la pollution : une Mine de charbon passe de 10 de pollution à 20 avec un bonus et 30 avec deux (`coal_mine.con.lua:99-117`).
- Moins de nouvelles industries : mets **Densité cible des industries** au cran le plus bas dans les réglages avancés ; on ne peut pas la mettre à zéro.
- Au réglage par défaut une industrie inutilisée ferme rarement ; à Très souvent, charge quelque chose de temps en temps.

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 5 ans, pas 10, et la production ne compte pas : seulement le fret chargé dans un véhicule ou consommé. Après ces 5 ans l'industrie n'est qu'une candidate : chaque année elle est marquée avec une chance de 1,1 % (Rarement) à 8,8 % (Très souvent). Le compte à rebours dure bien 730 jours. Le fret booster donne +50 % à +150 % par industrie, par lots qui durent 3 mois. Nouvelles industries : aucun réglage marche/arrêt, seulement Densité cible des industries de ×2/3 à ×1,5 ; aucune dans l'éditeur de cartes.
result: differs
```
