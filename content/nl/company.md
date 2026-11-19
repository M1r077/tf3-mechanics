---
title: Bedrijfsrang, voordelen en hoofdkwartier
summary: Wat je bedrijfsrang verhoogt, wat elke rang vrijspeelt, hoe vergunningen en prospecties werken, wat het hoofdkwartier echt geeft, en wat een hogere rang je kost.
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40444
fact: 15 | bedrijfsrangen, van Junior tot Tycoon
fact: ×12,5 | wereldbevolking nodig voor rang 15, vergeleken met de start
fact: ×0,75 | inkomsten op rang 15 met Inflatie Gemiddeld
fact: 0 | rangen verloren wanneer de bevolking daalt
---

Je bedrijfsrang komt niet van geld of leveringen: hij komt van de **bevolking van de hele kaart**. Elke nieuwe rang speelt voordelen vrij (bezienswaardigheden, prospecties, marketingcampagnes, Vergroenen van de industrie, hoofdkwartiermodules), en met de instelling **Inflatie** verlaagt hij ook al je inkomsten een beetje.

## Wat de rang verhoogt

- Het spel onthoudt de **wereldbevolking bij de start** van het spel: de inwoners van alle steden (`company.script.tl:392-396`, `company_util.tl:365-371`).
- Daarna vergelijkt het de **hoogste** ooit bereikte wereldbevolking met die startwaarde (`company_growth.script.tl:25-27`). De waarde gaat alleen omhoog: krimpende steden kosten je nooit een rang.
- Rang 1 wordt bereikt bij de startwaarde, rang 15 bij ongeveer **12,5 keer** die waarde (`company_progression_util.tl:6-14`, `company_progression_util.tl:95-120`, `town_growth_function.tl:13-20`).
- Er is geen rang in campagnemissies en in de kaarteditor (`company_growth.script.tl:74-79`).

| Rang | Rol | Wereldbevolking, vergeleken met de start |
|---|---|---|
| 1 | Junior | ×1 |
| 2 | Mecanicien | ×1,02 |
| 3 | Ingenieur | ×1,08 |
| 4 | Coördinator | ×1,2 |
| 5 | Expert | ×1,4 |
| 6 | Teamleider | ×1,7 |
| 7 | Supervisor | ×2,1 |
| 8 | Manager | ×2,6 |
| 9 | Directeur | ×3,3 |
| 10 | Senior-directeur | ×4,2 |
| 11 | CEO | ×5,3 |
| 12 | Voorzitter | ×6,7 |
| 13 | Vicepresident | ×8,3 |
| 14 | President | ×10,2 |
| 15 | Tycoon | ×12,5 |

De verhoudingen zijn uit de scripts berekend voor een startbevolking van 50.000 of meer (`company_progression_util.tl:6-14`, `company_static_util.tl:6-24`). Op een kleine kaart liggen ze iets hoger voor de middelste rangen (rang 8 vraagt ×2,85 bij 5.000 inwoners); rang 1 en 15 blijven op ×1 en ×12,5.

- De rang volgt dus de **stadsgroei**: steden groeien door je passagiers en vracht, zie [Stadsgroei](towns.html).
- De eerste rangen komen snel, voor de laatste moeten de steden van de kaart vele malen groter zijn.

## Een nieuwe rang wordt toegepast in het bedrijfsvenster

Wanneer de bevolking een drempel passeert, verschijnt een **melding van rangverhoging**; erop klikken opent het bedrijfsvenster op die rang (`company_growth.script.tl:96-107`, `company_notification_rank_up.script.tl:8-9`).

- De nieuwe voordelen worden pas vrijgespeeld wanneer die rang **in het bedrijfsvenster geselecteerd** is: het venster stuurt dan de vrijgave (`company.tl:420-423`, `company_growth.script.tl:55-62`). De bouwmenu's controleren deze toegepaste rang (`company_util.tl:92`, `company_util.tl:171-178`).
- De inkomstenfactor uit de volgende sectie volgt de **bereikte** rang, toegepast of niet (`company_growth.script.tl:47-48`).

```tip scripts
Klik na een rangverhoging op de melding (of open het bedrijfsvenster en selecteer de nieuwe rang) om de voordelen te krijgen. Wachten levert niets op: de inkomsten zijn al verlaagd.
```

## Wat een hogere rang kost: de instelling Inflatie

Met **Inflatie** dalen alle inkomsten uit vracht en passagiers gelijkmatig van ×1 op rang 1 tot een minimum op rang 15 (`company_progression_util.tl:25-40`, `company_growth.script.tl:159-170`).

| Inflatie | Inkomsten op rang 15 | Bron |
|---|---|---|
| Geen | ×1 (geen verandering) | `difficulty_util.tl:50`, `mod.script.tl:695-698` |
| Laag | ×0,9 | |
| Gemiddeld | ×0,75 | |
| Hoog | ×0,6 | |
| Zeer hoog | ×0,5 | |

- Op Gemiddeld kost elke rang ongeveer 1,8 % van de inkomsten: ×0,96 op rang 3, ×0,875 op rang 8, ×0,75 op rang 15.
- Inflatie verhoogt geen enkele kost; kosten volgen het kalenderjaar (zie [Kosten, onderhoud en leningen](costs.html)).
- Een hogere rang maakt nieuwe subsidieaanbiedingen ook zeldzamer (zie [Subsidies](subsidies.html)).

## Vergunningen

De meeste voordelen zijn beperkt door **vergunningen**. Een rang geeft vergunningen voor een voordeel; elk gebouw of gebruik neemt er één (`company_util.tl:33-80`, `company_util.tl:206`).

- Vergunningen **tellen op** over de rangen: een voordeel dat 1 geeft op rang 3 en 1 op rang 5, staat er vanaf rang 5 2 toe (`company_util.tl:51-56`).
- Een gebouw geeft zijn vergunning terug wanneer het gesloopt wordt: het spel telt wat er staat (`company_util.tl:143-163`, `company_util.tl:203-206`).
- Prospecties, marketingcampagnes en vergroening verbruiken een vergunning wanneer ze starten (`company.script.tl:416-423`, `company.script.tl:459-462`, `company.script.tl:496-500`). Het bouwmenu toont dan **Al gebruikt** of **Cooldown** (`company_util.tl:207-226`).
- De vergunning voor **Marketing** komt **5 jaar** na elke campagne terug (`marketing.res.lua:6-7`, `company.script.tl:66-94`).

| Voordeel | Vergunningen | Bron |
|---|---|---|
| Hoofdkwartier | 1 op rang 1 | `hq.res.lua:6` |
| Marketingcampagne | 1 op rang 4, terug na 5 jaar | `marketing.res.lua:6-7` |
| Vergroenen van de industrie | 1 op rang 3, 6, 9, 12 en 15 | `industry_greenify_tool.script.tl:101-102` |
| Zuiveringsinstallatie | 15 op rang 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Bezienswaardigheden | elk één: Amfitheater 2, Grote Vuurtoren 5, Wittereigerkasteel 7, Maritiem Museum 9, Slot Neuschwanstein 10, Vrijheidsbeeld 11, Zomerpaleis 13, Opera 14, Houses of Parliament 15 | `arena.con.lua:39`, `lighthouse.con.lua:48`, `white_heron_castle.con.lua:47`, `ship_museum.con.lua:55`, `neuschwanstein.con.lua:55`, `statue_of_liberty.con.lua:57`, `summer_palace.con.lua:63`, `opera_house.con.lua:63`, `westminster.con.lua:79` |

Wat elk voordeel doet: [Reputatie](reputation.html) (Marketingcampagne), [Vervuiling en geluid](emission.html) (Vergroening, Zuiveringsinstallatie).

## Prospecties

Een prospectie zoekt een grondstof bij een stad en sticht er, als ze slaagt, een nieuwe industrie.

| Grondstof | Rang | Bron |
|---|---|---|
| Vis | 2 | `exploration_fish.res.lua:9-11` |
| Klei | 3 | `exploration_clay.res.lua:9-11` |
| Ruwe olie | 4 | `exploration_crude_oil.res.lua:9-11` |
| Graan, groente | 4, **één gedeelde vergunning** (Industrie) | `exploration_grain.res.lua:9`, `exploration_vegetables.res.lua:9`, `permit_key_farm.res.lua:6` |
| Boomstammen | 5 | `exploration_logs.res.lua:9-11` |
| Steenkool, ijzererts | 6 | `exploration_coal.res.lua:9-11`, `exploration_iron_ore.res.lua:9-11` |
| Stenen, wol | 8 | `exploration_stone.res.lua:9-11`, `exploration_wool.res.lua:9-11` |
| Zand | 9 | `exploration_sand.res.lua:9-11` |
| Rubber | 12 | `exploration_rubber.res.lua:9-11` |

- Elke grondstof heeft **één** vergunning, verbruikt wanneer de prospectie start (`company.script.tl:451-462`).
- Ze loopt tot **6 maanden**. Eén keer per maand probeert ze de industrie te plaatsen, met een kans die over de 6 maanden stijgt van 20 % tot 60 % (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`).
- Een poging mislukt ook wanneer het spel geen plaats voor die industrie bij de stad vindt (`company.script.tl:199-210`).
- Als de laatste poging mislukt, **komt de vergunning terug** en een melding zegt dat (`company.script.tl:106-126`, `company.script.tl:170-181`).
- Per stad en grondstof kan er maar één prospectie tegelijk lopen (`company.script.tl:442-447`).

```engine
Waar de nieuwe industrie mag staan (makeIndustrySpawnProposal bij de stad) beslist de engine: een visprospectie ver van water, of een stad zonder vrij land eromheen, mislukt gewoon en geeft de vergunning terug.
```

## Het hoofdkwartier

| Wat | Waarde | Bron |
|---|---|---|
| Prijs en onderhoud | gratis, geen onderhoud | `headquarter.script.tl:526-527` |
| Vergunning | 1, op rang 1 | `headquarter.con.lua:6-7`, `hq.res.lua:6` |
| Stadsgroei | +5 % voor de stad die er het dichtst bij ligt | `headquarter.script.tl:510-515`, `landmark_util.tl:51-70` |
| Arbeidsplaatsen | 24 | `headquarter.con.lua:16`, `headquarter.script.tl:505-508` |

- De +5 % is een bonus op de groeisnelheid van die stad, dus doet hij niets wanneer die snelheid 0 % is (zie [Stadsgroei](towns.html)).
- **Modules** kosten elk 50.000 en zijn beperkt door vergunningen die met de rang groeien (`hq_module_m.module.lua:83`, `hq_module_m.module.lua:137`).
- Maar twee modules hebben een bonus in de bestanden: **Middelgroot gebouw** +1 % stadsgroei (`hq_module_m.module.lua:139-142`) en **Groot gebouw** +1 % Reputatieherstel (`hq_module_l.module.lua:169-172`). De herstelbonus wordt door geen enkele stadsbeoordeling gelezen (zie [Reputatie](reputation.html)). De andere modules zijn decoratief.
- Elk modulebestand begint ook met een tabel die +5 % stadsgroei geeft, maar niets in het bestand gebruikt die (`hq_corner_l.module.lua:148-159`, `hq_statue.module.lua:46-57`). Alleen de bonus in de `metadata` van de module wordt opgeteld (`headquarter_addon.script.tl:18-29`).

| Module | Vergunningen erbij op rang (×2 = twee) | Totaal op rang 15 |
|---|---|---|
| Grondvlag | 1 ×2, 6, 7, 8, 9, 11, 12, 13, 14 | 10 |
| Hoekgebouw | 3, 5, 7 ×2, 9, 11, 13, 15 | 8 |
| Middelgroot gebouw | 2, 4, 10 ×2, 15 ×2 | 6 |
| Groot gebouw | 5, 6, 10, 12 | 4 |
| Balkon | 8 ×2, 14 ×2 | 4 |
| Grote fontein | 10 ×2, 14 ×2 | 4 |
| Koepel | 6, 15 ×2 | 3 |
| Dakvlag | 7, 10, 13 | 3 |
| Tennisbaan | 11, 12, 14 | 3 |
| Oude boom | 13, 15 ×2 | 3 |
| Standbeeld | 14 ×2 | 2 |
| Zwembad | 15 | 1 |

Bronnen: de regel `rankAndPermits` van elk modulebestand (`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`).

```tip scripts
Zet het hoofdkwartier in de stad die je het snelst wilt laten groeien, en voeg daar middelgrote gebouwen toe: dat zijn de enige modules met een groeibonus.
```

## Goed om te weten

- Om in rang te stijgen, laat je de steden groeien: meer passagiers en vracht naar meer steden, met goede beoordelingen. Geld op de bank telt niet.
- Plan je bezienswaardigheden en prospecties: elk komt één keer, op een vaste rang.
- Op een kaart met Inflatie is een rangverhoging goed voor de voordelen en slecht voor de inkomsten. Op Gemiddeld kost de hele weg naar rang 15 een kwart van alle inkomsten.

```check
official: "The company rank depends on the population of the map. … Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Dezelfde regel: de hoogste bereikte wereldbevolking, vergeleken met de bevolking bij de start, ×12,5 voor rang 15; nooit verloren. Een nieuwe rang moet in het bedrijfsvenster geselecteerd worden om zijn voordelen vrij te spelen, terwijl Inflatie de inkomsten meteen verlaagt. Maar twee modules hebben een bonus (Middelgroot gebouw +1 % groei, Groot gebouw +1 % Reputatieherstel, dat geen beoordeling leest); de andere zijn decoratief.
result: refines
```
