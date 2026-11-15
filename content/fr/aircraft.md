---
title: Avions, aéroports et hélicoptères
summary: Aérodrome ou aéroport, quel avion atterrit où, terminaux, deuxième piste, héliports, et la liste de tous les aéronefs avec leur fret, leur capacité et leur vitesse.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
fact: 2 | tailles d'avion : petit et grand
fact: 1950 | premier aéroport, et premiers hélicoptères
fact: 1980 | deuxième piste
fact: 5 | aéronefs par hangar
---

Chaque avion est **petit** ou **grand**. Un **aérodrome** n'accepte que les petits avions ; un **aéroport** accepte les deux, et les hélicoptères à son bâtiment principal. Les hélicoptères ont aussi leurs propres stations.

```diagram air_access
```

## Aérodrome et aéroport

- **Aérodrome** : « Il peut accueillir des avions de petite taille. » Variantes de 1920, 1950 et 1980 ; 1, 2 ou 3 terminaux et un dépôt optionnel (`airfield.tl:49`, `airfield.tl:76`, `airfield_era_a.metacon.tl:3`).
- **Aéroport** : « Il peut accueillir des avions de petite et de grande taille. » Variantes de 1950 et 1980 ; 2, 3 ou 4 terminaux et une direction d'atterrissage (« Direction d’atterrissage ») (`airport.tl:24`, `airport.tl:80`, `airport1950.metacon.tl:3-4`).
- Les terminaux d'aérodrome n'acceptent que les petits avions ; les terminaux d'aéroport acceptent les deux tailles (`af_terminal.module.lua:715`, `ap_terminal.module.lua:897`).
- Le bâtiment principal de l'aéroport a des aires pour hélicoptères (`ap_main.module.lua:532`), et à partir de 1950 un aéroport peut recevoir un terminal pour hélicoptères (`ap_terminal_heli.module.lua:897`, `ap_terminal_heli.module.lua:971`).
- **Deuxième piste** : un module d'aéroport à partir de 1980 (`airport_2nd_runway.module.lua:5`). Certains modules d'aéroport en ont besoin et affichent « Une deuxième piste est nécessaire. » sans elle (`airport.script.lua:261`).
- Toutes les stations aériennes acceptent les passagers et tout le fret (`airfield.tl:59`, `airport.tl:34`).

| Bâtiment | Passagers en attente | Source |
|---|---|---|
| Terminal d'aérodrome | jusqu'à 250 | `af_terminal.module.lua:773` |
| Bâtiment principal de l'aéroport | jusqu'à 400 | `ap_main.module.lua:667` |
| Terminal d'aéroport | jusqu'à 850 | `ap_terminal.module.lua:951` |
| Terminal pour hélicoptères de l'aéroport | jusqu'à 450 | `ap_terminal_heli.module.lua:990` |

## Hangars et stations pour hélicoptères

- Un **hangar** d'aérodrome ou d'aéroport accueille 5 aéronefs et entretient les aéronefs dans un rayon de 550 m (`af_hangar.module.lua:273-278`, `ap_hangar.module.lua:456-461`).
- **Héliport** (à partir de 1950) : achète et entretient les hélicoptères, dépôt de 5, rayon d'entretien de 800 m (`heliport.script.lua:301-306`).
- **Hélisurface** (à partir de 1950) : une petite aire d'atterrissage pour passagers et fret, sans dépôt (`helipad.con.lua:29-33`).

## Coûts

Prix et entretien de la première variante. Les variantes suivantes coûtent ×3 ou ×9 ([Coûts, entretien et emprunts](costs.html)) ; le premier aérodrome utilise déjà ×3 (`airfield.tl:8`).

| Bâtiment | Prix | Entretien par an | Source |
|---|---|---|---|
| Aérodrome | 1 200 000 - 3 000 000 | 50 000 - 200 000 | `airfield.tl:55-56` |
| Aéroport | 1 800 000 - 4 500 000 | 300 000 - 750 000 | `airport.tl:30-31` |
| Module d'aérodrome (bâtiment principal, terminal, hangar) | 600 000 | 100 000 | `af_main.module.lua:316-317`, `af_hangar.module.lua:326-327` |
| Module d'aéroport (terminal, hangar, deuxième piste) | 900 000 | 150 000 | `ap_main.module.lua:672-673`, `ap_hangar.module.lua:508-509`, `airport_2nd_runway.module.lua:27-28` |

- L'entretien des aéroports et aérodromes suit aussi l'année du calendrier, ×1 en 1900 jusqu'à ×6 en 2020 ([Coûts, entretien et emprunts](costs.html)).
- Le prix et les coûts d'exploitation d'un aéronef sont calculés à partir de sa vitesse et de sa capacité, comme pour les navires et les véhicules routiers ([Coûts, entretien et emprunts](costs.html)).

## Tous les avions

Vitesse en km/h, arrondie. « Tout fret » signifie tous les types de fret.

| Avion | Années | Taille | Fret | Capacité | Vitesse | Vitesse de chargement |
|---|---|---|---|---|---|---|
| Junkers F 13 Herta | 1920-1950 | petit | passagers | 16 | 135 | - |
| Vickers J6860 Victoria | 1922-1960 | petit | tout fret | 32 | 150 | 2,5 |
| Fokker F VII A | 1925-1960 | petit | passagers | 32 | 175 | 2 |
| Junkers JU-52 Iron Annie | 1933-1982 | petit | passagers, tout fret | 24 | 200 | 3 |
| Douglas DC-3 | 1935-1995 | petit | passagers | 56 | 300 | 2,5 |
| Curtiss C-46 Commando | 1942-1980 | petit | tout fret | 80 | 280 | - |
| Douglas DC-4 | 1944-1998 | petit | passagers | 100 | 365 | 3 |
| Avion-cargo Bristol Type 170 | 1949-2005 | petit | passagers, tout fret | 40 | 350 | 1,5 |
| Lockheed L-1049 Super Connie | 1952-1986 | grand | passagers | 120 | 486 | 3 |
| Lockheed L-1049D/H Super Connie | 1959-2000 | grand | tout fret | 60 | 486 | 2,5 |
| De Havilland DH.106 Comet | 1960-2000 | grand | passagers | 160 | 724 | 3 |
| Avion-cargo Canadair CL-44 | 1962-2005 | grand | tout fret | 48 | 645 | 2 |
| Convair CV 990 Coronado | 1962-2020 | grand | passagers | 200 | 917 | 2 |
| Lockheed L-100 Hercules | 1976-2000 | petit | tout fret | 44 | 400 | 3 |
| McDonnell Douglas DC-10-30 | 1978- | grand | passagers | 400 | 960 | 2,5 |
| McDonnell Douglas DC-10-30CF | 1978- | grand | tout fret | 132 | 960 | 4 |
| Avion-cargo Airbus A310 300F | 1982- | grand | tout fret | 160 | 850 | 3 |
| Short 330 Sherpa | 1984- | petit | passagers, tout fret | 40 | 455 | 2,5 |
| Airbus A320 | 1985- | grand | passagers | 180 | 753 | 3 |
| Br. Aerospace 146 | 1985- | petit | passagers | 112 | 753 | 3 |
| Avion-cargo Br. Aerospace 146 | 1985- | petit | tout fret | 48 | 753 | 2 |
| Fokker 100 | 1988- | grand | passagers | 160 | 845 | 3,5 |
| Tupolev Tu-204 | 1995- | grand | passagers | 280 | 850 | 4 |
| Avion-cargo Tupolev Tu-204C | 1995- | grand | tout fret | 68 | 850 | 2 |
| Boeing 737-700 | 1998- | grand | passagers | 200 | 974 | 2,5 |
| Avion-cargo Boeing 737-700-C | 1998- | grand | tout fret | 80 | 974 | 3 |
| Bombardier DHC-8 | 2000- | petit | passagers | 120 | 648 | 3 |
| Avion-cargo bombardier DHC-8 | 2008- | petit | tout fret | 120 | 648 | 2 |
| Sukhoi Superjet 100 | 2011- | petit | passagers | 160 | 870 | 3 |
| Airbus Canada A220 | 2013- | grand | passagers | 180 | 830 | 5 |

## Tous les hélicoptères

| Hélicoptère | Années | Fret | Capacité | Vitesse | Vitesse de chargement |
|---|---|---|---|---|---|
| Bell 47 | 1950-1990 | passagers, tout fret | 8 | 150 | 2 |
| Piasecki H-21 Workhorse | 1952-1985 | passagers, tout fret | 80 | 210 | 3 |
| Sikorsky S-64 Skycrane | 1962-2017 | tout fret | 40 | 213 | 4 |
| Bell 206 Long Ranger | 1965-2025 | passagers | 32 | 241 | 2,5 |
| Boeing Vertol 234 Chinook | 1980- | passagers, tout fret | 80 | 269 | 2 |
| AgustaWestland AW101 Merlin | 1990- | passagers | 60 | 278 | 3 |
| Mil Mi-26TC | 1993- | tout fret | 120 | 295 | 4 |
| Eurocopter 120B Colibri | 1998- | passagers | 48 | 210 | 3 |
| Kaman K-MAX | 2005- | tout fret | 60 | 190 | 3 |
| Airbus H225 Super Puma | 2013- | passagers | 48 | 288 | 3 |
| NextGen VTOL | 2030- | passagers | 56 | 610 | 4 |

## Bon à savoir

- **Les petits avions restent utiles jusqu'à la fin.** Le DHC-8, sa version cargo et le Sukhoi Superjet 100 sont petits, donc un aérodrome leur suffit.
- **Avant 1952 il n'existe aucun grand avion**, donc un aéroport précoce ne donne pas encore accès à de plus gros appareils.
- Les avions volent en ligne droite, et le paiement ne compte que la distance à vol d'oiseau, donc un détour ne leur coûte rien de plus ([Revenus du fret et délai de livraison](income.html)).
- La longueur de piste minimale, les trajectoires de vol et l'atterrissage sont décidés par le moteur du jeu ; les scripts ne les montrent pas.

```check
official: "It can be used by small airplanes." (Airfield) "It can be used by small and large airplanes." (Airport), build menu descriptions.
scripts: Pareil : les terminaux d'aérodrome n'acceptent que SMALL_AIRCRAFT, ceux d'aéroport AIRCRAFT et SMALL_AIRCRAFT, hélicoptères au bâtiment principal de l'aéroport, héliport et hélisurface dès 1950, deuxième piste dès 1980, hangars de 5 ; 15 petits et 15 grands avions et 11 hélicoptères dans le jeu de base.
result: agrees
```
