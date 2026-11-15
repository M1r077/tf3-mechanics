---
title: Industrie
summary: Productieregels, voorraden, percelen en uitbreiding, boostervracht, waarom een industriebedrijf geen boost heeft, en wanneer een ongebruikt bedrijf echt sluit.
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
fact: 5 jaar | zonder laden of verbruik maken een bedrijf kandidaat voor sluiting
fact: 1,1 % | kans per jaar bij Zelden (standaard), daarna 730 dagen aftellen
fact: +50–150 % | bonus van boostervracht, vast per bedrijf
fact: 3 maanden | bonus per partij boostervracht
---

Elk industriebedrijf werkt met **regels**: „neem dit uit de invoervoorraad, leg dat in de uitvoervoorraad”, een vast aantal keer per jaar. Grondstofbedrijven (mijnen, boerderijen, bronnen) hebben geen invoer nodig; hun grootte komt van hun **percelen**. Twee boosts kunnen de productie vermenigvuldigen: **boostervracht** (alleen grondstofbedrijven) en **arbeiders**.

## Productieregels

- Een regel geeft de gebruikte en gemaakte vracht per ronde, en hoeveel rondes per jaar: een ronde duurt een jaar ÷ dat getal (`industry_react_util.tl:51-57`). Het onderdeel Productie van het bedrijfsvenster toont dit met kleine getallen.
- Het getal **Max.** in het venster is: per ronde × rondes per jaar × de boosts × de instelling **Productiviteit industrie** (`industry_util.tl:310-379`).
- **Productiviteit industrie**: 50 %, 75 %, 100 %, 150 % of 200 %. Voorinstellingen: Makkelijk 150 %, Gemiddeld 100 %, Moeilijk 75 %, Heel moeilijk 50 % (`difficulty_util.tl:41`, `difficulty_util.tl:93`, `difficulty_util.tl:120`, `difficulty_util.tl:148`, `difficulty_util.tl:175`, `mod.script.tl:196-197`).
- Voorbeeld, Staalbedrijf: 6 ijzererts + 6 steenkool → 3 staal + 4 plaatmetaal, 121,7 rondes per jaar: 730 ijzererts en 730 steenkool → 365 staal en 487 plaatmetaal (`steel_mill.con.lua:43-71`). Ontbreekt één invoer, dan staat de regel stil.
- De Conservenfabriek heeft twee regels: vis + plaatmetaal, of vlees + plaatmetaal (`food_factory.con.lua:43-74`).

```engine
De engine voert de regels uit. Hij kan een ronde langer maken: de tooltip toont dan „(+ … vanwege bezorgtijd)” (`industry_react_util.tl:61-76`). Wanneer en hoeveel staat niet in de scripts, dus de echte productie kan onder Max. blijven.
```

## Voorraden

- Elke vracht heeft een eigen voorraad met een grens: bijv. een Steenkolenmijn houdt 100 gereedschap en 400 steenkool, een Staalbedrijf 800 ijzererts, 800 steenkool, 400 staal en 500 plaatmetaal (`coal_mine.con.lua:44-67`, `steel_mill.con.lua:43-71`).
- Voorraden bederven nooit (`industryutil.lua:25-29`): vracht wacht zo lang als nodig.
- Een volle uitvoervoorraad stopt de productie niet: het overschot wordt weggegooid (officiële wiki). De grafiek **Vrachtstroom** toont **Verbruikt**, **Gemaakt** en **Vernietigd** (`industry_eow.script.tl:804-816`).
- Met de bouwparameter **Invoer** op Uit verliezen de regels hun invoer en heeft het bedrijf geen invoervoorraad (`industryutil.lua:280-287`, `industryutil.lua:383-387`, `industryutil.lua:432-441`).

## Percelen en uitbreiding

- Grondstofbedrijven en het Veeteeltbedrijf hebben **percelen** (velden, mijnschachten, boortorens). Hun niveau is hun aantal percelen (`industryutil.lua:602-617`).
- De regel groeit met de percelen: productie per ronde × percelen ÷ **alle percelen van dat bedrijfstype**, afgerond, minstens 1. De invoer daalt in dezelfde verhouding (`industryutil.lua:225-259`). Een Steenkolenmijn (8 perceeltypes) met 4 percelen maakt 8 steenkool per ronde in plaats van 16.
- Elk bedrijf krijgt een maximum: willekeurig tussen de helft van de percelen en allemaal, of Klein / Middel / Groot (50 / 75 / 100 %) met de parameter **Grootte industriebedrijf** (`industryutil.lua:519-537`). Een mijn met maximum 5 van 8 haalt nooit de volle regel.
- Elk half jaar kan het spel **één perceel** toevoegen (`industries_config.res.lua:5`, `industries.script.tl:158-183`). De kans is (score − 25 %) ÷ 50 %, met score = productiescore × het deel van de productie dat je vervoert (hoogstens 1): 25 % of minder nooit, 75 % of meer altijd (`industries.script.tl:172-176`).
- Een bedrijf waarvan je de vracht niet vervoert, **groeit dus nooit**. Fabrieken hebben geen percelen en groeien nooit.
- Op het maximum zegt het venster **Industriebedrijf is uitgebreid naar zijn maximale potentieel.**; staan gebouwen, sporen of wegen in de weg, dan **Industriebedrijf kan niet verder worden uitgebreid.** (`industry_react_util.tl:588-602`, `industries.script.tl:13-38`). Geen script haalt percelen weg; volgens de officiële wiki verlagen gesloopte percelen de productie.

```engine
De productiescore (getProductionRating), de jaarproductie en de vervoerde hoeveelheid (getCargoOutputPerYear, getCargoShippedPerYear), en waar een nieuw perceel komt (makeIndustryExtendProposal) zijn waarden van de engine.
```

## Boostervracht

De 13 grondstofbedrijven hebben een tweede regel, de **booster**: hij neemt 4 keer per jaar een partij boostervracht uit de invoervoorraad en geeft een bonus zolang hij loopt.

| Bedrijf | Percelen | Op volle grootte, per jaar | Boosterpartij (4 per jaar) | Bron |
|---|---|---|---|---|
| Kleigroeve | 8 | 365 klei | 12 gereedschap | `clay_pit.con.lua:42-82` |
| Steenkolenmijn | 8 | 320 steenkool | 13 gereedschap | `coal_mine.con.lua:44-85` |
| Katoenplantage | 21 | 274 wol | 17 kunstmest | `cotton_farm.con.lua:42-98` |
| Landbouwbedrijf | 20 | 274 graan + 183 groente | 17 kunstmest | `farm.con.lua:44-106` |
| Visgrond | 18 | 263 vis | 12 gereedschap | `fishing_grounds.con.lua:44-101` |
| Houthakkerskamp | 20 | 243 boomstammen | 15 machines | `forest.con.lua:44-99` |
| IJzerertsmijn | 8 | 365 ijzererts | 15 machines | `iron_ore_mine.con.lua:44-84` |
| Olieplatform | 9 | 365 ruwe olie | 12 machines | `oil_platform.con.lua:45-96` |
| Oliebron | 14 | 548 ruwe olie | 15 machines | `oil_well.con.lua:44-94` |
| Steengroeve | 7 | 365 stenen | 12 gereedschap | `quarry.con.lua:44-83` |
| Rubberplantage | 23 | 365 rubber | 17 kunstmest | `rubber_farm.con.lua:41-102` |
| Baggeraar | 9 | 365 zand | 15 machines | `sand_excavator.con.lua:44-92` |
| Zandgroeve | 8 | 365 zand | 12 gereedschap | `sand_pit.con.lua:44-84` |

- De bonus wordt één keer per bedrijf geloot: **+50 % tot +150 %**, afgerond op 1 % (`industryutil.lua:394-405`). Het onderdeel Booster toont hem als „+X %” (`industry_util.tl:428-434`). Met de parameter **Boostfactor** is hij in plaats daarvan +50 %, +75 %, +100 %, +125 % of +150 % (`industryutil.lua:289-299`).
- Het venster toont de booster actief zolang zijn laatste partij duurt (3 maanden), of zodra de voorraad een volle partij bevat (`industry_util.tl:55-91`).
- De partij krimpt **niet** met de percelen: een kleine mijn vraagt evenveel gereedschap als een grote (`industryutil.lua:227-229`).
- Beide boosts vermenigvuldigen: productie × arbeidersfactor × (1 + boosterbonus) (`industry_util.tl:42-104`).

## De werknemersboost

De helft van de arbeidsplaatsen (10 van 20) moet bezet zijn door inwoners die in de laatste 2 jaar **met jouw passagierslijnen zijn aangekomen**; de factor is ×1,5 tot ×2,5, vast per bedrijf (`industry_productivity_util.tl:35-72`). Alleen toegewezen werknemers tellen niet. Details: [Werknemers en de werknemersboost](workers.html).

## Waarom heeft mijn industrie geen boost?

1. **Geen grondstofbedrijf**: fabrieken hebben geen boosterregel, alleen de werknemersboost (`steel_mill.con.lua:61-70`).
2. **Partij onvolledig**: de voorraad moet een volle partij bevatten, bijv. 13 gereedschap voor een Steenkolenmijn. Onder 4 partijen per jaar (52 gereedschap) stopt de boost tussen leveringen.
3. **Verkeerde vracht**: gereedschap, machines of kunstmest naargelang het bedrijf (tabel hierboven).
4. **Werknemers**: toegewezen is niet genoeg; het onderdeel Booster telt aankomsten („12/10”) (`industry_react_util.tl:617-654`). Zie [Werknemers en de werknemersboost](workers.html).

## Wanneer sluit een ongebruikt industriebedrijf?

```diagram ind_closure
```

De controle loopt elke 100 updates voor elk bedrijf (`industries.script.tl:84-85`):

1. **Kandidaat**: geen vracht in een voertuig **geladen** en niets **verbruikt** gedurende **5 jaar** (vanaf de bouw als nooit) (`industries.script.tl:104-119`, `industries_config.res.lua:6`). Alleen produceren telt niet.
2. **Toeval**: elk jaar wordt een kandidaat gemarkeerd met de kans van de instelling **Frequentie van industriesluitingen** (tabel hieronder) (`industries.script.tl:120-131`).
3. **Aftellen**: de melding **Sluiting van industrie** verschijnt, met 2 jaar (730 dagen) te gaan (`industries_config.res.lua:7`, `industry_close.script.tl:53-67`). Daarna wordt het bedrijf verwijderd met zijn eigen wegstukken (`industries.script.tl:147-155`, `industry_util.tl:560-601`).
4. **Gered**: één keer laden of verbruik tijdens het aftellen breekt het af (`industries.script.tl:134-137`). Een aangenomen subsidie **Bevoorraad industriebedrijf** of **Werknemers vervoeren** ervoor breekt het ook af (`subvention_util.tl:473-484`).

| Frequentie van industriesluitingen | Kans per jaar als kandidaat | Helft van de kandidaten gemarkeerd na | Voorinstelling | Bron |
|---|---|---|---|---|
| Nooit | 0 | nooit | Makkelijk | `difficulty_util.tl:94` |
| Zelden (standaard) | 1,1 % | ongeveer 63 jaar | Gemiddeld | `difficulty_util.tl:121` |
| Soms | 2,2 % | ongeveer 32 jaar | Moeilijk | `difficulty_util.tl:149` |
| Vaak | 4,4 % | ongeveer 16 jaar | – | `difficulty_util.tl:37` |
| Zeer vaak | 8,8 % | ongeveer 8 jaar | Heel moeilijk | `difficulty_util.tl:176` |

De kans is 0,011 per jaar × 0, 1, 2, 4 of 8 (`mod.script.tl:171`, `mod.script.tl:202-203`, `difficulty_util.tl:37`). Bedrijven die van jou zijn sluiten nooit, net als bedrijven met handmatige ontwikkeling en geen enkel bedrijf tijdens de tutorial (`industries.script.tl:94-102`).

```engine
Wat telt als „geladen” en „verbruikt” (de logs itemsLoaded en itemsConsumed, bijv. of boostervracht telt), de vlag manualDevelopment, en waarom bedrijven met een depot overgeslagen worden (`industries.script.tl:140-146`) liggen bij de engine. Net als wat de engine doet met een boosterregel zonder invoer (Invoer uit).
```

## Nieuwe industriebedrijven

- De engine voegt na verloop van tijd bedrijven toe; de scripts geven hem alleen een doeltijd van 50 jaar, een exponent van 3, en geen nieuwe bedrijven in de kaarteditor (`mod.script.tl:166-168`). De instelling **Doeldichtheid industriebedrijven** schaalt dit (`mod.script.tl:194-195`). De melding is **Industriebedrijf opgericht** (`industry_spawn.res.lua:6`).
- Het bedrijfsvoordeel **Prospectie voor grondstoffen** zoekt een nieuw bedrijf voor die grondstof bij een stad: één poging per maand met een kans van 20 % tot 60 %, 6 maanden lang; mislukt het, dan komt de vergunning terug (`company_util.tl:14-17`, `company.script.tl:96-142`, `company.script.tl:299-307`).

```engine
Waar en wanneer een nieuw bedrijf verschijnt, en welk type, beslist de engine (makeIndustrySpawnProposal).
```

## Goed om te weten

- Vervoer vanuit elk grondstofbedrijf dat je wilt laten groeien: niet vervoerde productie blokkeert de uitbreiding, wat de boosts ook zijn.
- Breng boostervracht naar de grootste mijnen en boerderijen: de partij kost hetzelfde, de bonus groeit met de percelen.
- Voorraden bederven niet: je kunt boostervracht vooruit leveren, tot de voorraadgrens (100).
- Boosts verhogen geluid en vervuiling: een Steenkolenmijn gaat van 10 vervuiling naar 20 met één boost en 30 met twee (`coal_mine.con.lua:99-117`).
- Bij de standaardinstelling sluit een ongebruikt bedrijf zelden; bij Zeer vaak laad je af en toe iets.

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 5 jaar, niet 10, en productie telt niet: alleen vracht die in een voertuig geladen of verbruikt is. Na de 5 jaar is het bedrijf alleen kandidaat: elk jaar wordt het gemarkeerd met een kans van 1,1 % (Zelden) tot 8,8 % (Zeer vaak). Het aftellen duurt 730 dagen, zoals gezegd. Boostervracht geeft +50 % tot +150 % per bedrijf, in partijen die 3 maanden duren.
result: differs
```
