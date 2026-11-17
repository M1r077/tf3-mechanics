---
title: Straßen, Gleise, Brücken und Signale
summary: Geschwindigkeit, Preis und Unterhalt jedes Gleis- und Straßentyps, was Brücken, Tunnel, Bahnübergänge und Signale kosten und erlauben, was Alleen und Lärmschutzwände wirklich ändern und wo Depots erklärt werden.
domain: infrastructure
official: gamemanual:infrastructure:streetstracks
status: verified
updated: 2026-11-17
game: 40425
fact: 100 / 160 / 350 km/h | einfaches, Standard- und Hochgeschwindigkeitsgleis
fact: ×9 | Preis und Unterhalt eines Hochgeschwindigkeitsgleises im Vergleich zum einfachen Gleis
fact: +30 % | Preis der Oberleitung auf einem Gleis
fact: -65 % | Lärm einer Straße oder eines Gleises mit Lärmschutzwand
---

Jeder Straßen- und Gleistyp hat eine Höchstgeschwindigkeit, einen Preis pro Meter und einen Unterhalt pro Meter und Jahr, alles in seiner Datei festgelegt. Brücken, Bahnübergänge und manche Straßendekorationen fügen ihre eigene Geschwindigkeitsgrenze hinzu. Die Kosten unten gelten bei **Infrastrukturkosten** und **Unterhalt der Infrastruktur** 100 % (siehe [Kosten, Unterhalt und Darlehen](costs.html)).

## Gleise

| Gleis | Ab | Höchstgeschwindigkeit | Bau pro km | Unterhalt pro km und Jahr | Quelle |
|---|---|---|---|---|---|
| Einfache Gleise | Start | 100 km/h | 60.000 | 10.000 | `simple.street_template.lua:9`, `simple.street_template.lua:28`, `simple.street_template.lua:33` |
| Standardgleise | 1930 | 160 km/h | 180.000 | 30.000 | `standard.street_template.lua:4`, `standard.street_template.lua:11`, `standard.street_template.lua:30`, `standard.street_template.lua:35` |
| Hochgeschwindigkeitsgleise | 1980 | 350 km/h | 540.000 | 90.000 | `high_speed.street_template.lua:4`, `high_speed.street_template.lua:11`, `high_speed.street_template.lua:30`, `high_speed.street_template.lua:35` |

- Die **Oberleitung** kostet **30 %** mehr als das Gleis (`mod.script.tl:24-25`). Sie ist ab 1921 auf dem einfachen Gleis verfügbar und ab dem Start jedes neueren Typs (`simple_catenary.street_template.lua:4`). Pro Jahr kostet sie laut den Dateien nichts extra: die elektrische Variante hat denselben Unterhalt (`simple_catenary.street_template.lua:34`).
- Alle drei Typen erlauben dieselbe Steigung und dieselben Kurven: **8,5 %** beim Bauen (so weit geht der Regler Steigung), höchstens 13 % für die Form des Gleises, und einen Kurvenradius von 55 m beim Bauen, mindestens 40 m (`standard.street_template.lua:36-37`, `standard.street_template.lua:48-49`, `construction_react_util.tl:241-242`, `construction_react_util.tl:1821`).
- Die Verschmutzung des Gleises selbst steigt mit seinem Typ: 2, 4 und 6 (`simple.street_template.lua:18`, `standard.street_template.lua:20`, `high_speed.street_template.lua:20`).

```engine
Wie stark eine Kurve die Geschwindigkeit eines Zuges senkt (die speedCoeffs jedes Gleistyps) und welche Geschwindigkeit das Bauwerkzeug für eine Kurve anzeigt, berechnet die Engine.
```

```tip scripts
Hochgeschwindigkeitsgleis kostet das 9-Fache des einfachen Gleises, beim Bau und jedes Jahr. Verlege es nur dort, wo Züge wirklich schneller als 160 km/h fahren; anderswo reicht Standardgleis, und einfaches Gleis für langsame Güterstrecken.
```

## Straßen

| Straße | Jahre | Höchstgeschwindigkeit | Bau pro km | Unterhalt pro km und Jahr | Quelle |
|---|---|---|---|---|---|
| Schmale Strasse (alt) | bis 1940 | 20 km/h | 36.000 | 6.000 | `town_old_xsmall.street_template.lua:4-5`, `town_old_xsmall.street_template.lua:8`, `town_old_xsmall.street_template.lua:27`, `town_old_xsmall.street_template.lua:56` |
| Kleine Strasse (alt) | bis 1940 | 40 km/h | 60.000 | 10.000 | `town_old_small.street_template.lua:8`, `town_old_small.street_template.lua:27`, `town_old_small.street_template.lua:56` |
| Grosse Strasse (alt) | bis 1940 | 60 km/h | 180.000 | 30.000 | `town_old_large.street_template.lua:8`, `town_old_large.street_template.lua:27`, `town_old_large.street_template.lua:88` |
| Schmale Strasse (neu) | ab 1940 | 30 km/h | 120.000 | 20.000 | `town_new_xsmall.street_template.lua:4`, `town_new_xsmall.street_template.lua:11`, `town_new_xsmall.street_template.lua:30`, `town_new_xsmall.street_template.lua:59` |
| Kleine Strasse (neu) | ab 1940 | 50 km/h | 180.000 | 30.000 | `town_new_small.street_template.lua:11`, `town_new_small.street_template.lua:30`, `town_new_small.street_template.lua:59` |
| Mittlere Strasse (neu) | ab 1940 | 50 km/h | 360.000 | 60.000 | `town_new_medium.street_template.lua:11`, `town_new_medium.street_template.lua:30`, `town_new_medium.street_template.lua:75` |
| Grosse Strasse (neu) | ab 1940 | 60 km/h | 540.000 | 90.000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:30`, `town_new_large.street_template.lua:91` |
| Kleine Landstrasse (alt) | bis 1940 | 60 km/h | 60.000 | 10.000 | `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:29`, `country_old_small.street_template.lua:58` |
| Kleine Landstrasse (neu) | ab 1940 | 80 km/h | 180.000 | 30.000 | `country_new_small.street_template.lua:10`, `country_new_small.street_template.lua:31`, `country_new_small.street_template.lua:60` |
| Einspurige Autobahn | ab 1940 | 100 km/h | 180.000 | 30.000 | `highway_new_small.street_template.lua:10`, `highway_new_small.street_template.lua:32`, `highway_new_small.street_template.lua:53` |
| Zweispurige Autobahn | ab 1940 | 120 km/h | 360.000 | 60.000 | `highway_new_medium.street_template.lua:10`, `highway_new_medium.street_template.lua:32`, `highway_new_medium.street_template.lua:61` |
| Dreispurige Autobahn | ab 1940 | 120 km/h | 540.000 | 90.000 | `highway_new_large.street_template.lua:10`, `highway_new_large.street_template.lua:32`, `highway_new_large.street_template.lua:69` |
| Tramgleise (alt) | bis 1910 | 40 km/h | 36.000 | 6.000 | `tram_old.street_template.lua:4-5`, `tram_old.street_template.lua:8`, `tram_old.street_template.lua:27`, `tram_old.street_template.lua:40` |
| Tramgleise (neu) | ab 1925 | 100 km/h | 120.000 | 20.000 | `tram_new.street_template.lua:4`, `tram_new.street_template.lua:9`, `tram_new.street_template.lua:29`, `tram_new.street_template.lua:42` |

- Der **Wechsel 1940** macht Stadtstraßen 10 km/h schneller, aber **dreimal** so teuer, beim Bau und jedes Jahr: eine kleine Straße steigt von 60.000 auf 180.000 pro km.
- Die mittlere und große Variante der Landstraßen kosten das 2- und 3-Fache der kleinen, bei gleicher Geschwindigkeit (`country_new_large.street_template.lua:10`, `country_new_large.street_template.lua:31`).
- Zusätze zu einer Straße: eine **Busspur** +10 %, ein **Tramgleis** +20 %, ein **elektrisches Tramgleis** +40 % des Straßenpreises (`mod.script.tl:24-28`).
- Der Spieler besitzt Straßen meist nicht, auch nicht die selbst gebauten; die Straßenwerkzeuge können den Besitzer einer Straße ändern (offizielles Wiki). Wer den Unterhalt einer Straße zahlt, entscheidet die Engine.

## Alleen und Lärmschutzwände

| Werkzeug | Lärm | Verschmutzung | Höchstgeschwindigkeit | Wo | Quelle |
|---|---|---|---|---|---|
| Allee-Werkzeug (Bäume) | -10 % | -50 % | **-25 %** | Straßen mit Gehweg, nicht auf Brücken oder in Tunneln | `alley.edge.lua:39-40`, `alley.edge.lua:53-56` |
| Lärmschutzwand-Werkzeug | -65 % | keine Änderung | keine Änderung | Straßen und Gleise, nicht in Tunneln | `barrier_b.edge.lua:43`, `barrier_b.edge.lua:47`, `barrier_track_b.edge.lua:43` |

- Beide kosten laut ihren Dateien 100 und 10 pro Jahr, wie eine Straße pro Meter (`alley.edge.lua:8`, `alley.edge.lua:12`, `barrier_b.edge.lua:7`, `barrier_b.edge.lua:11`).
- Die Straßentypen „mit Bäumen“ und „mit Lärmschutz“ im Baumenü sind dieselben Straßen, auf denen diese Dekorationen schon angebracht sind (`town_new_medium_trees.street_template.lua:12-14`). Das Baumenü addiert ihre Wirkungen (`construction_react_util.tl:2116-2139`).
- Eine Straße mit Bäumen ist also **ein Viertel langsamer**: eine neue mittlere Straße mit Bäumen erlaubt etwa 38 km/h statt 50.

```tip scripts
Gegen Lärm nimm die Lärmschutzwand: -65 % und kein Geschwindigkeitsverlust. Bäume sind das Werkzeug gegen Verschmutzung (-50 %), aber sie bremsen die Straße um ein Viertel.
```

Wie Städte Lärm und Verschmutzung bewerten: [Verschmutzung und Lärm](emission.html).

## Brücken und Tunnel

| Brücke | Jahre | Höchstgeschwindigkeit | Für | Grundpreis | Quelle |
|---|---|---|---|---|---|
| Steinbrücke | ab Start | 90 km/h | Gleise, Straßen | 200 | `stone.bridge.lua:169-170`, `stone.bridge.lua:181-183`, `stone.bridge.lua:193` |
| Bockbrücke | bis 1970 | 60 km/h | ein Typ für Gleise, einer für Straßen | 100 | `trestle.bridge.lua:200-201`, `trestle.bridge.lua:212-214`, `trestle.bridge.lua:226`, `trestle_s.bridge.lua:212` |
| Stahlbrücke | ab 1940 | 140 km/h | Gleise, Straßen | 200 | `steel.bridge.lua:243`, `steel.bridge.lua:259`, `steel.bridge.lua:269` |
| Hängebrücke | ab 1940 | 180 km/h | Gleise, Straßen | 600 | `suspension.bridge.lua:277`, `suspension.bridge.lua:294`, `suspension.bridge.lua:304` |
| Betonbrücke | ab 1970 | 280 km/h | Gleise, Straßen | 200 | `concrete.bridge.lua:162`, `concrete.bridge.lua:176`, `concrete.bridge.lua:187` |
| Schrägseilbrücke | ab 2000 | 220 km/h | Gleise, Straßen | 750 | `cable.bridge.lua:214`, `cable.bridge.lua:231`, `cable.bridge.lua:240` |
| Stabbogenbrücke | ab 2010 | 350 km/h | Gleise, Straßen | 650 | `tarch.bridge.lua:253`, `tarch.bridge.lua:270`, `tarch.bridge.lua:280` |

- Die Brückengrenze gilt **zusätzlich** zu der des Gleises: eine Hochgeschwindigkeitsstrecke über eine Stahlbrücke fährt dort 140 km/h. Vor 1970 erlaubt keine Brücke mehr als 180 km/h, vor 2010 keine 350 km/h.
- **Tunnel** (Felsentunnel, Betontunnel ab 1970) haben in ihren Dateien **keine Geschwindigkeitsgrenze** und denselben Grundpreis von 600 (`tunnel_a.tunnel.lua:187-188`, `tunnel_a_car.tunnel.lua:185`, `tunnel_b.tunnel.lua:191-194`).
- Brücken- und Tunnelpreise folgen den Infrastrukturkosten (`post_run_util.tl:50-51`).

```engine
Den Grundpreis einer Brücke oder eines Tunnels rechnet die Engine mit der Höhe oder Tiefe (costFactors) in einen Preis pro Meter um; laut offiziellem Wiki hängt er von der Länge und der Höhe über dem Boden oder der Tiefe darunter ab. Derselbe Grundpreis kann also sehr unterschiedliche Rechnungen ergeben. Tunnel kosten Ruf bei der Stadt (siehe [Ruf der Städte](reputation.html)).
```

```tip scripts
Für eine schnelle Strecke über ein Tal vor 1970 ist die Hängebrücke (180 km/h) die einzige Brücke, die schneller als 140 km/h ist; ein Tunnel hat gar keine Grenze.
```

## Bahnübergänge und Signale

| Was | Jahre | Höchstgeschwindigkeit des Gleises | Preis | Quelle |
|---|---|---|---|---|
| Einfacher Bahnübergang | 1850 - 1925 | 120 km/h | 4.000 | `era_a_eu.rcr.lua:14-17`, `era_a_eu.rcr.lua:26` |
| Bahnübergang mit Halbschranken | 1925 - 1975 | 160 km/h | 16.000 | `era_b_eu.rcr.lua:15-18`, `era_b_eu.rcr.lua:27` |
| Moderner Bahnübergang mit Halbschranken | ab 1975 | 160 km/h | 16.000 | `era_c_eu.rcr.lua:15-17`, `era_c_eu.rcr.lua:26` |
| Pfadsignal (Formsignal bis 1950, Lichtsignal ab 1950) | alle | - | 9.000, Unterhalt 1.500 pro Jahr | `signal_path_a.con.lua:4-5`, `signal_path_a.con.lua:10-11`, `signal_path_c.con.lua:4-5` |

- Ein Bahnübergang begrenzt das Gleis auf höchstens 160 km/h: Hochgeschwindigkeitsstrecken brauchen Brücken oder Tunnel, um Straßen zu kreuzen.
- Jedes Signal kann auf **Einbahn** gestellt werden (`signal_path_a.con.lua:51-52`). Wie Signale das Gleis in Blöcke teilen, erklärt die Seite Railway Signals des offiziellen Wikis.

## Depots und Wartungsstationen

Was Depots und Wartungsstationen kosten, wie viele Fahrzeuge sie bedienen und in welchem Radius: [Fahrzeuge](vehicles.html) und [Kosten, Unterhalt und Darlehen](costs.html).

## Gut zu wissen

- Vor 1940 ist das Ausbauen von Stadtstraßen billig; nach 1940 kostet jede neue oder umgebaute Stadtstraße das Dreifache und dreifachen Unterhalt.
- Prüfe auf einer schnellen Strecke jede Brücke und jeden Bahnübergang: der langsamste bestimmt dort die Geschwindigkeit.
- Geschwindigkeit lohnt sich nur, wenn sie mehr Fahrten bringt (siehe [Warum verliere ich Geld?](money.html)).

```check
official: "Streets and tracks have speed limits, depending on the type used. On curved tracks, the speed of trains is also limited by the curve's radius. . Rail bridges have an additional speed limit, which may lower the speed limit of the used tracks." "The Alley tool places trees on the side of the street which reduces the noises and pollutions emitted by vehicles using that street. It also lower the maximum speed of the road." ([Streets and Tracks](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:streetstracks))
scripts: Dieselben Geschwindigkeiten wie in den offiziellen Tabellen für Gleise, Straßen und Brücken. In den Dateien gelten Brückengrenzen auch für Straßen, Tunnel haben keine, Bahnübergänge begrenzen Gleise auf 120 oder 160 km/h, Bäume bremsen eine Straße um 25 % und senken die Verschmutzung um 50 %, den Lärm aber nur um 10 %, während Lärmschutzwände den Lärm um 65 % senken, ohne zu bremsen.
result: refines
```
