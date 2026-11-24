---
title: Succès
summary: Ce que le script du jeu vérifie pour chaque succès de la partie libre et quand, lesquels ne comptent que les véhicules, le fret et les animaux du jeu de base, et quelles vérifications sont laissées au moteur.
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-24
game: 40444
fact: 17 | succès débloqués par le script du jeu lui-même
fact: 500 m | hauteur du premier wagon d'un train à un arrêt pour Halte au sommet
fact: < 1 % | de Réputation de la ville pour C’est pas moi
fact: 10 | monuments qui doivent avoir la même ville la plus proche pour Centralisation
---

Le wiki officiel liste 41 succès. Le script du jeu (`achievements.script.tl`) en débloque **17** lui-même et alimente **9 compteurs entre les parties** ; les autres (campagne, météo, taille des villes, entrepôt, intérêts, boosters, voitures, 1900-2000, vapeur dans les années 2000) sont vérifiés ailleurs, par le moteur ou la plateforme. Chaque vérification demande d'abord au moteur si le succès peut encore être débloqué ; c'est là qu'il est décidé si des mods ou des réglages le bloquent (`achievements.script.tl:632`, `achievements.script.tl:510`).

## Succès vérifiés par le script

| Succès | Ce que le script vérifie | Source |
|---|---|---|
| **Colis arrivé** | une unité de fret arrive à destination | `achievements.script.tl:221-225`, `achievements.script.tl:632-636` |
| **Pour le compte de** | un contrat de subvention terminé | `achievements.script.tl:241-244`, `achievements.script.tl:638-642` |
| **Série de contrats** | 10 subventions terminées sans aucun échec entre elles ; une subvention échouée remet le compte à 0 | `achievements.script.tl:243-249`, `achievements.script.tl:644-648` |
| **Intendant** | la note de livraison d'une ville passe à **Excellent** | `achievements.script.tl:270-276`, `towns.script.tl:27-30`, `achievements.script.tl:650-654` |
| **Développement urbain** | une ville monte de niveau | `achievements.script.tl:253-255`, `town_growth.script.tl:92` |
| **Demande accrue** | une ville obtient une demande pour un nouveau type de fret | `achievements.script.tl:257-259`, `achievements.script.tl:668-672` |
| **C’est pas moi** | la Réputation d'une ville **baisse** sous **1 %** | `achievements.script.tl:261-267`, `towns.script.tl:33-36` |
| **Promotion** | l'entreprise gagne un rang | `achievements.script.tl:280-282`, `achievements.script.tl:680-684` |
| **Gravir les échelons** | l'entreprise atteint le rang le plus élevé | `achievements.script.tl:284-290`, `achievements.script.tl:686-690` |
| **Paysagiste** | tu places des arbres, et seulement des arbres, en une construction (rien de retiré, pas par reboisement) | `achievements.script.tl:346-377` |
| **Perfectionniste** | la même station est démolie, reconstruite, démolie et reconstruite, dans cet ordre, sans autre station construite ou retirée entre-temps | `achievements.script.tl:304-341`, `achievements.script.tl:694-710` |
| **Centralisation** | exactement 10 monuments terminés ont la même ville la plus proche | `achievements.script.tl:382-395`, `achievements.script.tl:713-721` |
| **Halte au sommet** | un de tes trains arrive à un arrêt avec son premier wagon à plus de **500 m** | `achievements.script.tl:407-417`, `achievements.script.tl:723-727` |
| **Au large** | un de tes hélicoptères arrive à un arrêt d'une plateforme pétrolière | `achievements.script.tl:420-450`, `achievements.script.tl:729-733` |
| **Flotte patrimoniale** | chaque modèle de navire du jeu de base circule en même temps sur une de tes lignes de navires | `achievements.script.tl:735-776` |
| **Rencontre du 3ᵉ type** | tu cliques sur un OVNI | `achievements.script.tl:793-806` |
| **Montre en main** | tu changes l'heure du jour à la main | `achievements.script.tl:839-844` |

- **Perfectionniste** ne compte qu'une construction qui ajoute ou retire une station entière : ajouter un quai ou un module à une station ne compte pas (`achievements.script.tl:301-302`).
- **Centralisation** compte chaque monument quand il est terminé, pour la ville la plus proche à ce moment-là (`achievements.script.tl:386`).
- **Flotte patrimoniale** n'est vérifié que quand un modèle de navire qui ne s'est jamais arrêté arrive à un arrêt ; il regarde les véhicules de tes lignes de navires, pas les navires au dépôt (`achievements.script.tl:736`, `achievements.script.tl:750-766`).
- **C’est pas moi** demande la Réputation, pas une autre note : voir [Réputation des villes](reputation.html).

```tip scripts
Halte au sommet vérifie la hauteur du premier wagon quand le train s'arrête, pas la hauteur du bâtiment de la gare. Construis la gare sur une montagne au-dessus de 500 m et fais-y rouler un train.
```

## Compteurs entre les parties

Ils continuent d'une partie à l'autre (la plateforme les enregistre). Le script n'envoie que ce qui a changé depuis la dernière vérification.

| Compteur | Succès | Ce qui compte | Source |
|---|---|---|---|
| Longueur de voies | **Tour du monde** | la hausse de la longueur totale du registre (en km) ; rien n'est retiré quand tu démolis | `achievements.script.tl:511-523` |
| Population | **Population mondiale** | la hausse de la population de la carte, depuis la population au chargement de la partie | `achievements.script.tl:512`, `achievements.script.tl:525-533` |
| Passagers | **Pionnier du transport** | les passagers qui ont terminé un trajet sur une de tes lignes | `achievements.script.tl:236-238`, `achievements.script.tl:535-541` |
| Fret | **Pionnier du fret** | les unités de fret livrées | `achievements.script.tl:543-549` |
| Climats | **Magnat des magnats** | le climat de la carte, quand l'entreprise y atteint le rang le plus élevé | `achievements.script.tl:551-567` |
| Revenus | **Magot à gogo** | tes revenus cumulés, en milliards | `achievements.script.tl:202-204`, `achievements.script.tl:569-590` |
| Types de fret | **Maître vendeur** | chaque type de fret du jeu de base livré une fois | `achievements.script.tl:20-22`, `achievements.script.tl:230-232`, `achievements.script.tl:592-607` |
| Véhicules | **Connaisseur** | chaque modèle de véhicule du jeu de base qui arrive une fois à un arrêt | `achievements.script.tl:16-18`, `achievements.script.tl:469-481`, `achievements.script.tl:609-625` |
| Animaux | **Ami des animaux** | chaque animal du jeu de base sur lequel tu cliques une fois | `achievements.script.tl:24-26`, `achievements.script.tl:809-834` |

- Les véhicules, le fret et les animaux des mods ne comptent jamais pour ces compteurs : seuls les fichiers du jeu de base (`::/vehicle`, `::/cargos`, `::/animal`) sont pris (`achievements.script.tl:16-26`).
- Pour Connaisseur, un véhicule doit **arriver à un arrêt** d'une ligne ; l'acheter ne suffit pas.

```engine
Si un succès peut encore être débloqué (isAchievementUnlockable), si les compteurs sont désactivés (areStatsDisabled), les objectifs de chaque compteur et les 24 succès absents du script sont gérés par le moteur et la plateforme. Le wiki officiel dit que les succès sont en général indisponibles avec des mods non cosmétiques ou avec des réglages de jeu différents des valeurs standard.
```

## Mods et succès

Utiliser des mods ne désactive **pas** les succès à lui seul. Deux choses décident : si chaque mod actif est marqué **cosmétique**, et si les réglages de jeu restent aux valeurs standard.

- Chaque mod a un indicateur `cosmetic` dans son `mod.json`. La documentation de l'API du jeu (dossier `api/tealdef`, champ `ModDesc.cosmetic`) indique : "If the mod is purely cosmetic, cosmetic mods still allow achievement from being earned while playing" (si le mod est purement cosmétique, il permet toujours d'obtenir des succès).
- Les DLC officiels et les missions de campagne sont aussi des mods, et tous sont marqués cosmétiques (`dlcs/*/mod.json`, `mods/release/urbangames_campaign*/mod.json`).
- Dans la page de nouvelle partie et dans la page de chargement, le jeu demande si la liste des mods actifs permet encore les succès (`new_game_or_map_settings_page.tl:902-903`, `savegame_react_util.tl:1063-1064`). Sinon, une bande orange indique **"Achievements cannot be earned."** (les succès ne peuvent pas être obtenus) (`savegame_react_util.tl:1485-1496`).
- Chaque sauvegarde garde aussi son propre indicateur (`achievementsEarnable`). S'il est désactivé, la page de chargement affiche aussi la bande orange, quels que soient les mods choisis maintenant (`savegame_react_util.tl:1035-1037`). Seul un mod qui force le retour des succès est vérifié à nouveau (`savegame_react_util.tl:1063`).
- Les réglages de jeu (difficulté et autres paramètres de partie) sont une deuxième raison : avec des valeurs différentes des valeurs standard, la difficulté s'affiche comme **Custom** (personnalisée) (`difficulty_util.tl:201-229`) et, selon le wiki officiel, les succès ne sont pas disponibles.

Une partie avec uniquement des mods cosmétiques et des réglages standard peut donc toujours obtenir des succès. Un seul mod non cosmétique, ou des réglages différents des valeurs standard, suffit à les bloquer, et une sauvegarde bloquée une fois le reste.

```engine
Quels réglages comptent exactement comme « différents des valeurs standard », et quand l'indicateur de la sauvegarde est fixé, est décidé par le moteur : pas dans les fichiers lisibles.
```

```tip scripts
Cherche la bande orange avant de lancer ou de charger une partie : pas de bande, les succès peuvent être obtenus. Une bonne façon de jouer : obtiens les succès dans une partie avec les réglages standard et uniquement des mods cosmétiques, et utilise des parties libres ou bac à sable séparées pour les mods et réglages qui changent le gameplay. C'est l'auteur du mod qui choisit l'indicateur cosmétique ; vérifie la ligne `cosmetic` dans le `mod.json` du mod, ou demande à l'auteur.
```

## Bon à savoir

- Chaque succès de « première fois » est vérifié par rapport à la vérification précédente : il faut un **nouvel** événement dans une partie où le succès est encore ouvert ; une ancienne subvention ou un ancien rang d'une sauvegarde ne compte pas de nouveau (`achievements.script.tl:633`, `achievements.script.tl:779`).
- Ton rang, les subventions et la Réputation sont expliqués dans [Rang de l'entreprise, avantages et siège social](company.html), [Subventions](subsidies.html) et [Réputation des villes](reputation.html).

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: 17 succès et 9 compteurs sont dans le script. Il précise les textes officiels : Intendant veut dire la note de livraison qui atteint Excellent, C’est pas moi une Réputation sous 1 %, Halte au sommet le premier wagon au-dessus de 500 m, Perfectionniste démolir-reconstruire-démolir-reconstruire la même station, et Flotte patrimoniale tous les modèles de navires du jeu de base sur des lignes en même temps. Seuls les véhicules, le fret et les animaux du jeu de base comptent pour les compteurs.
result: refines
```
