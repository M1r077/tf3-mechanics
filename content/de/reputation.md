---
title: Ruf der Städte
summary: Was die Wertung Ruf einer Stadt senkt, wie schnell sie zurückkommt, was Feierlichkeiten und Marketingkampagnen wirklich tun und warum eine unterbrochene Straße zwischen zwei Städten so teuer ist.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
fact: −33 % | pro unterbrochener Hauptverbindung zu einer anderen Stadt
fact: 33 % | Erholung pro Jahr (100 % während einer Marketingkampagne)
fact: 0,25 % | pro entferntem ausgewachsenem Baum bei der Stadt
fact: 2 Mio. m³ | Geländearbeiten kosten den ganzen Ruf
---

Der **Ruf** ist eine der sechs Wertungen im Stadtfenster, und die Stadtverwaltung nimmt die **niedrigste** davon (siehe [Stadtwachstum](towns.html)). Er beginnt bei 100 % und sinkt nur durch das, was **du** baust oder verfehlst: Geländearbeiten, entfernte Bäume und Felsen, abgerissene Stadtgebäude, gescheiterte Subventionen und unterbrochene Hauptverbindungen. Zeit, Feierlichkeiten und Marketingkampagnen bringen ihn zurück.

```diagram rep_recovery
```

## Was ihn senkt

Jeder Bau, den du bestätigst, wird vor dem Ausführen geprüft; die Kosten gehen an die betroffene Stadt (`towns.script.tl:271-291`, `town_util.tl:1062-1080`). Nur deine eigenen Bauten zählen, und im Karteneditor zählt nichts (`town_util.tl:1078-1080`, `towns.script.tl:58`).

| Grund im Stadtfenster | Was Ruf kostet | Quelle |
|---|---|---|
| **Entfernte Bäume** | 0,25 % pro Baum, × Entfernungsfaktor zur nächsten Stadt, × Baumgröße (kleine Bäume zählen weniger) | `town_util.tl:1144-1150`, `town_util.tl:865`, `model_metadata_util.lua:655-680` |
| **Entfernte Felsen** | 0,25 % pro Fels, × Entfernungsfaktor | `town_util.tl:1148-1149`, `town_util.tl:884-885` |
| **Landschaftsbau** | 0,00005 % pro m³ angehobenes **oder** abgesenktes Gelände: 2 Millionen m³ = 100 %. Gelände, das Gleise, Straßen und Gebäude formen, zählt auch (bis zur Hälfte weniger bei Bauten über 50.000 m²), ebenso neues Tunnelvolumen | `town_util.tl:873-886`, `town_util.tl:1245-1269`, `town_util.tl:1403-1436` |
| **Abgerissene Gebäude** | 100 % für 40,5 % entfernte Kapazität eines Viertels (Wohnungen, Geschäfte oder Arbeitsplätze dieser Stadt) | `town_util.tl:867-869`, `town_util.tl:1165-1184` |
| **Gescheiterte Subvention** | Stadt versorgen: 10 % bis 60–90 % (je nach Risiko); Städte verbinden: 10–100 % × Entfernungsfaktor, in **beiden** Städten (siehe [Subventionen](subsidies.html)) | `deliver_cargo_town.script.tl:202-210`, `deliver_passengers.script.tl:113-114`, `towns.script.tl:331-333` |
| **Unterbrochene Hauptverbindungen** | **1/3** pro andere Stadt, deren Hauptverbindung unterbrochen oder zu lang ist | `town_util.tl:376-394`, `town_util.tl:1608` |

- Jeder Grund ist auf 100 % begrenzt (`town_util.tl:1611-1620`).
- Beim Bauen zeigt der Tooltip **Ruf: −x %**, mit der Zahl der betroffenen Städte, wenn es mehrere sind (`construction_react_util.tl:3818-3864`). Er rechnet von einer vollen Wertung aus.
- Bäume pflanzen oder Felsen setzen hebt nur **Entfernte Bäume** oder **Entfernte Felsen** auf, mit denselben 0,25 % pro Stück. Für die anderen Gründe tut es nichts, bei vollem Ruf auch nicht (`town_util.tl:1228-1238`, `town_util.tl:1630-1641`).
- Die Einstellung Ruf eines neuen Spiels ist **Aus** oder **Ein** (Ein in jeder Voreinstellung). Aus heißt immer volle Wertung (`difficulty_util.tl:44`, `difficulty_util.tl:110`, `town_util.tl:396-399`).

```engine
Wie schnell der Entfernungsfaktor zwischen einer Stadt und einem entfernten Baum fällt, welches Geländevolumen jede Stadt bekommt, welche Bäume ein Gleis oder eine Straße automatisch entfernt und welche Straßen als Hauptverbindung einer Stadt zählen (und wann eine Fahrt „zu lang“ ist), sind Werte der Engine (getImpactFromDistance, getTerrainBrushVolumeImpact, getTerrainAlignmentImpact, getAutoRemovalEntityImpact, getTownProblems).
```

## Unterbrochene Hauptverbindungen

Eine Hauptverbindung gilt als unterbrochen, wenn das Spiel **Strassenverbindung zwischen Städten wurde unterbrochen** oder **Fahrzeit zwischen Städten ist zu lang** meldet (`town_util.tl:378-380`, `town_warning.script.tl:7-22`). Jede betroffene andere Stadt kostet 1/3, und die Wertung zeigt es **sofort** (`town_util.tl:401-403`):

| Unterbrochene Verbindungen | Ruf höchstens | Wertung | Quelle |
|---|---|---|---|
| 1 | 67 % | Sehr gut | `town_util.tl:983-985` |
| 2 | 33 % | Mittelmässig | `town_util.tl:983-985` |
| 3 | 0 % | Sehr schlecht: die Stadt wächst nicht mehr | `town_util.tl:607-633` |

- Solange die Unterbrechung dauert, wird die Strafe auch Schritt für Schritt über ein halbes Jahr in den gespeicherten Wert geschrieben (`towns.script.tl:137-145`). Nach der Reparatur kommt dieser gespeicherte Teil nur mit der normalen Erholung zurück: eine lange Unterbrechung kostet noch eine Weile Ruf.
- 67 % liegt genau an der Grenze zu Sehr gut: jeder kleine weitere Verlust senkt die Stadt auf Gut.

## Wie er zurückkommt

- **Von selbst**: das Stadtfenster zeigt **Jährliche Aufwertung** 33 %, 100 % mit Marketingkampagne (`town_react_util.tl:1061-1067`). Das ist eine Stufe (1/6) pro halbes Jahr, oder alle 2 Monate während einer Kampagne (`towns.script.tl:121-135`).
- Die Erholung verteilt den Gewinn auf alle Gründe; sie geht nie über die noch offenen Unterbrechungen hinaus (`town_util.tl:1649-1687`).
- **Feierlichkeiten** geben **+50 %** für den ersten Passagier, der in einer Stadt in eine deiner Linien steigt, +50 % für die erste Fracht an eine Stadt, +50 % bei jedem Stufenaufstieg der Stadt und +20 % für die nächste Stadt bei der ersten Fracht an jede Industrie (`celebrations.script.tl:181-273`). Die Meldung endet dann mit **Ruf in Stadt verbessert.** oder **Ruf in … verbessert.** (`celebration_react_util.tl:63-75`). Sie zählen nur, wenn der Ruf nicht voll ist, und nicht in Kampagnenmissionen (`celebrations.script.tl:79-93`, `celebrations.script.tl:140-142`).
- **Stadt versorgen** kann bei Annahme +5 % bis +20 % × Risikofaktor geben (`deliver_cargo_town.script.tl:195-199`). Wie jeder Gewinn entfernt das nur bestehende Verluste (`towns.script.tl:324-330`).

## Marketingkampagne

| Was | Wert | Quelle |
|---|---|---|
| Preis | 10 M × Jahresfaktor: 4 M im Jahr 1900 bis 25 M im Jahr 2020, auf 1 M gerundet | `marketing_campaign_tool.script.tl:9-14` |
| Braucht | eine Genehmigung aus den Firmenboni | `marketing_campaign_tool.script.tl:83-95`, `company.script.tl:416-423` |
| Dauer | ein Jahr | `marketing_campaign_tool.script.tl:136` |
| Ruf | Erholung ×3 (100 % pro Jahr); **kein** sofortiger Gewinn | `towns.script.tl:126`, `town_util.tl:915-925` |
| Einwohner | deine Linien in dieser Stadt zählen als halb so teuer, wenn Einwohner wählen, wie sie reisen | `marketing_campaign_tool.script.tl:137`, `towns.script.tl:376-398` |

```engine
Das Skript rechnet 360 Sekunden Spielzeit pro Stufe (120 mit Kampagne). Der Kalender dahinter ist die Jahresdauer der Engine (getDefaultYearDuration); die 33 % und 100 % im Stadtfenster passen zu einem Jahr von 720 Sekunden (ein Tag von 2 Sekunden, `cargotype.script.lua:3`). Wie stark die halbierten Linienkosten Einwohner zu deinen Linien bringen, entscheidet die Routenwahl der Engine.
```

## Gut zu wissen

- Achte auf den Bau-Tooltip: zeigt er **Ruf: −x %**, ist ein Tunnel oder eine sanftere Trasse oft billiger als der Ruf.
- Lass nie eine Hauptstraße zwischen zwei Städten unterbrochen: jede kostet sofort −33 %, und drei stoppen die Stadt.
- Eine Marketingkampagne bei vollem Ruf hilft nur deinen Linien, nicht der Wertung. Starte sie direkt nach großen Bauarbeiten, wenn die Erholung etwas aufzuholen hat.
- Der Bonus **Rufwiederherstellung** des großen Hauptquartier-Moduls (+1 %) steht im Reiter Boni, ändert in den Skripten aber nur einen Wert, den keine Wertung liest (`hq_module_l.module.lua:171`, `towns.script.tl:157`, `town_util.tl:829`, `town_util.tl:857`).
- Die Errungenschaft **Ich war es nicht** verlangt eine Stadt mit 0 % Ruf im freien Spiel (`achievements.script.tl:261-267`).

```check
official: "Reputation reflects how the town and surrounding nature are treated. Landscaping, removing town buildings and breaking main connections to other towns can lower it, while celebrations and marketing campaigns can improve it. Reputation lost by removing trees can be recovered by planting new ones." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Dieselben Ursachen, dazu entfernte Felsen, Tunnel, das Gelände von Gleisen und Straßen und gescheiterte Subventionen. Jede unterbrochene oder zu lange Hauptverbindung kostet sofort 1/3; drei stoppen die Stadt. Die Erholung beträgt von selbst 33 % pro Jahr; eine Marketingkampagne macht 100 % pro Jahr daraus, gibt aber sofort nichts. Bäume pflanzen hebt nur den Verlust durch Bäume auf. Der Bonus Rufwiederherstellung des Hauptquartiers hat in den Skripten keine Wirkung.
result: refines
```
