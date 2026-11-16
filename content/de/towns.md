---
title: Stadtwachstum: XP, Wertungen und Größe
summary: Woher die XP einer Stadt kommen, wie die sechs Wertungen ihre Wachstumsrate bestimmen und wie viel größer jede Stufe sie macht.
domain: towns
official: gamemanual:simulation:towns
status: verified
updated: 2026-11-15
game: 40425
fact: 0 % | Wachstum, wenn eine Wertung Sehr schlecht ist
fact: ×1,5 | XP für jede weitere Stufe (1.000 für Stufe 2)
fact: ×40 | Größe nach 17 gewonnenen Stufen
---

Eine Stadt wächst nur durch **deinen** Transport: Passagiere, die mit deinen Linien ankommen, und Fracht, die an ihre Gebäude geliefert wird, geben ihr XP. Ihre Wertungen entscheiden, wie viel davon zählt, und jede gewonnene Stufe macht die Stadt größer.

```diagram town_xp
```

## Woher die XP kommen

| Quelle | Roh-XP | Quelle |
|---|---|---|
| Passagier, der **mit deinen Linien** an einem Stadtgebäude ankommt | 5 · 10 · 20: Wohnung und Arbeit oder Geschäft in derselben Stadt, einer Nachbarstadt, einer weiter entfernten Stadt | `town_growth.script.tl:649-701`, `town_growth_config.res.lua:6` |
| Frachteinheit, an ein Stadtgebäude geliefert | 10 · 20 · 40 für Frachtstufe 0 · 1 · 2 | `town_growth.script.tl:642`, `town_growth_config.res.lua:5` |
| Subventionsbelohnung „Stadterfahrung" | ein Anteil der aktuellen Stufe, ebenfalls × Wachstumsrate | `subvention_util.tl:144-152`, `town_growth.script.tl:608` |

- Die XP gehen an die Stadt des Gebäudes, an dem Passagier oder Fracht **ankommt**. Ein Pendler zwischen zwei Städten gibt beiden XP: der Stadt der Arbeit auf dem Hinweg, der Wohnstadt auf dem Rückweg.
- Fahrten zu oder von einer **Industrie** geben keine XP (`town_growth.script.tl:680-683`). Fahrten zu Fuß oder mit dem Auto auch nicht: nur Fahrten mit deinen Linien zählen (`town_growth.script.tl:656`).
- Zeit allein gibt nichts: die XP pro Tick sind 0 (`town_cargo_util.tl:6`).
- Frachtstufen: **0** Ziegel, Zement, Fisch, Treibstoff, Fleisch, Bretter, Gemüse; **1** Getränke, Bücher, Kleidung, Möbel, Maschinen, Tinned Food, Werkzeuge; **2** Fahrzeuge (`placementparamsutil.lua:506-616`).

Jede Roh-XP wird mit der **Wachstumsrate** der Stadt multipliziert (`town_growth.script.tl:60-63`). Das Stadtfenster zeigt sie als **Wachstumsrate:**.

## Die Wachstumsrate

Die Wachstumsrate kommt aus zwei Wertungen des Stadtfensters (`town_util.tl:607-633`, `town_util.tl:954-962`):

1. **Stadtverwaltung**: die **niedrigste** ihrer sechs Wertungen, nicht der Durchschnitt (`town_util.tl:754-784`).
2. **Versorgung**: die Versorgungsstufen für Passagiere und Fracht gemittelt, aufgerundet (`town_util.tl:555-589`).

```diagram growth_matrix
```

- Jede Wertung hat sechs Stufen: ein Wert von 0–1 wird in Sechstel geteilt (`town_util.tl:983-985`). **Ausgezeichnet** braucht 5/6 = 83 % oder mehr.
- Steht **eine einzige** Wertung auf Sehr schlecht, ist die Verwaltung Sehr schlecht und die Rate **0 %**: die Stadt steht still, egal was du lieferst.
- 100 % braucht Verwaltung Ausgezeichnet mit Versorgung Sehr gut oder besser, oder Verwaltung Sehr gut mit Versorgung Ausgezeichnet.
- Dein **Hauptquartier** gibt der nächstgelegenen Stadt +5 %, mehrere Erweiterungen geben +5 %, manche weniger oder nichts; der Wert steht in der Datei jedes Moduls (`headquarter.script.tl:510-515`, `landmark_util.tl:51-70`). Der Bonus multipliziert die Rate, bei 0 % bringt er nichts.

```tip scripts
**Eine Stadt wächst nicht mehr? Verbessere zuerst ihre schlechteste Wertung.** Die Stadtverwaltung ist die niedrigste der sechs Wertungen: eine einzige Wertung auf Sehr schlecht hält die Stadt bei 0 %, die anderen zu verbessern ändert nichts.
```

## Die sechs Wertungen der Verwaltung

| Wertung | Was sie senkt | Quelle |
|---|---|---|
| **Ruf** | Terraforming, Abriss von Stadtgebäuden, entfernte Bäume oder Felsen, gescheiterte Subventionen; jede getrennte Hauptverbindung zu einer anderen Stadt −1/3 | `town_util.tl:396-404`, `town_util.tl:1608`, `town_react_util.tl:30-43` |
| **Verkehr** | verstopfte Straßen in der Stadt | `town_util.tl:445-456` |
| **Zufriedenheit** | Anteil unzufriedener Reisender (mindestens 15 Personen angenommen) | `town_util.tl:479-503` |
| **Lieferung** | Anteil verspäteter Frachtlieferungen (siehe [Frachteinnahmen](income.html)) | `town_util.tl:505-519` |
| **Lärm** | Lärm der Stadt: 65 dB oder weniger → volle Wertung, 80 dB → 0 | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Verschmutzung** | mittlere Verschmutzung pro 16-m-Zelle des Stadtgebiets, auf der logarithmischen Skala der Skripte („dB“, kein Schallpegel): 60 → voll, 74 → 0 | `town_util.tl:413-431`, `emission_config.tl:23-24` |

Die **Empfindlichkeits**-Einstellungen verschieben diese Grenzen: Ruf ist nur Aus / Ein, die fünf anderen haben sieben Stufen von Aus bis Extrem, Normal ist ×1 (Lärm und Verschmutzung gehen oben weiter: bis ×3,5 und ×5, gegen ×3 bei den anderen); Aus heißt immer volle Wertung (`difficulty_util.tl:44-49`).

## Versorgung

- **Passagiere**: Linienauslastung der Stadt × 2, also **gibt 50 % Auslastung die volle Wertung** (`town_util.tl:546-553`).
- **Fracht**: Angebot ÷ Bedarf jedes Viertels (Wohnen, Gewerbe, Industrie), alle seine Frachten zusammen; es zählt das **beste** Viertel, nicht der Durchschnitt (`town_util.tl:521-543`).
- Eine Stadt ohne etwas zu versorgen zählt als voll versorgt. Eine Stadt, die von dir weder Passagiere noch Fracht bekommt, zählt als „keine Lieferungen": Wachstumsrate 0 % (`town_util.tl:565-588`).

```tip scripts
**Du brauchst nicht alle Einwohner auf deinen Linien: 50 % Linienauslastung gibt schon die volle Passagierwertung.**
```

Neue Frachtbedarfe kommen mit den Stufen (`placementparamsutil.lua:618-660`): je einer für Gewerbe und Industrie am Anfang, ein zweiter Gewerbebedarf ab Stufe 5, ein zweiter Industriebedarf ab Stufe 7, ein dritter Gewerbebedarf ab Stufe 9, ein dritter Industriebedarf ab Stufe 11. Sie kommen erst, nachdem die Stadt mindestens eine Frachtlieferung erhalten hat (`town_growth.script.tl:286-288`). Das Spiel bevorzugt Frachten, die wenige andere Städte schon verlangen (`town_growth.script.tl:258-266`).

## Stufen und Größe

- Stufe 2 braucht 1.000 XP, jede weitere Stufe 1,5-mal mehr als die vorige (`town_cargo_util.tl:81-97`, `town_growth_config.res.lua:7`): Stufe 5 bei 8.125 XP insgesamt, Stufe 10 bei etwa 75.000, Stufe 18 (Grosse Metropole, die letzte) bei etwa 2 Millionen.
- Städte, die mit mehr Wohnungen platziert werden, beginnen höher: Stufe 2, 3 oder 4 (`town_cargo_util.tl:43-54`).
- Die **Zielgröße** hängt von den seit dem Start gewonnenen Stufen ab, inklusive Fortschritt zur nächsten (`town_cargo_util.tl:100-110`, `town_growth_function.tl:4-11`):

```diagram town_size
```

- Die zusätzliche Größe wird auf Wohn-, Gewerbe- und Industrieviertel verteilt, je nachdem, wie gut sie bedient werden: Passagiernutzung für Wohnungen, Frachtversorgung für die anderen (`town_growth.script.tl:404-421`). Sobald ein Viertel 40 % der Stadt ausmacht, sinkt der größtmögliche Anteil an der zusätzlichen Größe von 100 % auf 50 %, wenn es 50 % der Stadt erreicht (ähnliche Grenzen gelten für die ganze Karte) (`town_growth.script.tl:509-522`). Wird kein Viertel bedient, wächst die Stadt nicht, auch mit XP (`town_growth.script.tl:415`).

```engine
Die Engine berechnet die Linienauslastung, die Verkehrsgeschwindigkeit, die Lärm- und Verschmutzungskarten und die Liste der verspäteten Lieferungen, und baut die neuen Häuser und Straßen. Der Mindestanteil, den ein Viertel immer bekommt (townGrowthMinDistrictFraction), ist ein Engine-Wert.
```

## Frachtbedarf und Gebäudelager

- Der Bedarf einer Stadt ist die Summe ihrer **Gebäude**. Jedes Gebäude hat ein kleines Eingangslager pro Fracht, die sein Viertel verlangt: Kapazität ÷ 4, aufgerundet, × der Faktor dieser Fracht im Bedarf der Stadt (1, wenn nichts anderes festgelegt ist; woher der Faktor kommt, steht nicht in den Skripten) (`townbuildingutil.lua:226-251`). Jede Fracht legt einen townConsumptionFactor von 1, 0,5 oder 0,25 fest (`placementparamsutil.lua:506-616`); wie er zum Gebäude gelangt, liegt in der Engine. Das Spiel vermerkt, dass diese Lagergröße „is currently nowhere shown in the UI" (derzeit nirgends in der Oberfläche angezeigt wird) (`townbuildingutil.lua:249`).
- Der Bedarf im Stadtfenster ist die Gesamtgrenze dieser Lager; das für die Wertung gezählte Angebot ist auf den Bedarf begrenzt (`town_util.tl:95-99`, `town_util.tl:194-198`). Größere Städte verlangen mehr, weil sie mehr Gebäude haben.
- Das Gebäudefenster zeigt eine **Verbrauchsrate**: wie schnell das Gebäude seine Fracht im Vergleich zu seinem Maximum verbraucht (`town_building.tl:103-132`).
- XP und Bezahlung gibt es, wenn eine Einheit in das Lager eines Gebäudes gelangt (`town_growth.script.tl:620-642`).
- Eine Haltestelle erreicht nur die Gebäude in ihrem Einzugsgebiet. Deren Lager können voll sein, während der Stadt insgesamt noch Fracht fehlt: dann **bleibt** die Fracht, die nicht hineinpasst, **im Fahrzeug**, außer **Entladen aller Güter nach Ankunft erzwingen** ist angehakt („Entladen, auch wenn das Lager voll ist.") (`cargofilter_window.tl:757-763`), was vernichtet, was nicht hineinpasst (siehe [Lade- und Entladegeschwindigkeit](loading.html)).
- An Bord gebliebene Fracht löst die Meldung **Güter-Entladeproblem** aus: „{cargoCount} Güter von {vehicle} wurden auf der Linie nicht entladen." (`cargo_rtc_warning.script.tl:28-41`, `cargo_rtc_warning.script.tl:37`); ihr Typname ist **Güter nicht entladen** (`cargo_rtc_warning.res.lua:6`).
- **Stadtgüterbedarf** („Wähle die maximale Anzahl an Güterbedürfnissen pro Stadt."): 2, 4 oder 6, Standard 2 (`difficulty_util.tl:54`, `difficulty_util.tl:83`, `mod.script.tl:173`, `mod.script.tl:205`). Die Skripte fügen Bedarfe nach Stufe hinzu (siehe oben) und geben diesen Wert an die Engine weiter.

```engine
Wie schnell ein Gebäude sein Lager verbraucht (consumeFrequency), welches Gebäude im Einzugsgebiet jede Einheit bekommt, was mit herumgefahrener Fracht passiert und wie die Engine den Stadtgüterbedarf nutzt, liegt in der Engine.
```

## Kann ich verhindern, dass eine Stadt wächst?

- In einem normalen Spiel gibt es **keine Einstellung** für eine maximale Stadtgröße (`difficulty_util.tl:90-199`).
- Im **Sandbox-Modus** hat das Stadtfenster eine Karte **Angestrebte Gebietskapazitäten** mit **Stadtentwicklung aktivieren** (`town_eow.script.tl:1041-1052`, `town_eow.script.tl:1170-1171`, `town_eow_editor_initial_capacity.res.lua:6`). Nicht angehakt bekommt die Stadt keine XP und wird nicht in der Größe angepasst; das Fenster zeigt **Stadtentwicklung inaktiv** (`town_growth.script.tl:28`, `town_growth.script.tl:345`, `town_eow.script.tl:107`).
- Ohne Sandbox geht es nur indirekt: eine Stadt wächst nur durch deine Passagiere und deine Fracht, und eine einzige Wertung Sehr schlecht stoppt sie (siehe oben).

## Gut zu wissen

- **Zuerst die schlechteste Wertung verbessern**: die Verwaltung ist das Minimum, die anderen zu verbessern bringt nichts.
- Passagiere zwischen **zwei Städten** geben 2-mal (Nachbarn) oder 4-mal (weiter weg) so viele XP wie Fahrten innerhalb einer Stadt, und beiden Städten.
- Gewerbefrachten haben nur Stufe 0–1; nur **Fahrzeuge** (Industrie) geben 40 XP pro Einheit, und eine Stadt verlangt sie normalerweise erst ab ihrem dritten Industriebedarf (Stufe 11).
- Eine Stadt weit weg von deinem HQ bekommt dessen Bonus nicht: nur die nächstgelegene Stadt.

```check
official: „A town needs 1,000 total XP to reach level 2. The XP required for each following level-up is 1.5 times the amount required for the previous level-up." Passagiere 5 / 10 / 20 XP, Fracht 10 / 20 / 40 XP. „The Town Authority rating is determined by the lowest of six ratings." „A line usage of 50% gives the maximum rating." ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Dieselben Zahlen. Wachstumsrate 0–100 % in 20-%-Schritten aus Verwaltung × Versorgung; eine Wertung Sehr schlecht stoppt das Wachstum; keine XP für Fahrten zu Industrien; Frachtbedarfe erst nach einer ersten Lieferung; der dritte Gewerbebedarf kann im Grundspiel nicht Stufe 2 sein (keine Gewerbefracht der Stufe 2); Größe ×40 nach 17 gewonnenen Stufen.
result: refines
```
