create database swissaerialguessr;
use swissaerialguessr;

create table ort (
    ID_Ort int primary key auto_increment,
    Name varchar(250) not null,
    Adresse varchar(250) not null,
    Nordwert double,
    Ostwert double,
    Zoom int DEFAULT 500,
    UpdateFlag int not null DEFAULT 0
);

CREATE TABLE spiel (
    ID_Spiel int primary key auto_increment,
    Punktzahl int,
    Zeitstempel timestamp DEFAULT CURRENT_TIMESTAMP
);

# Import Game Data:
LOAD DATA local INFILE '.\\database\\tabelleOrte.csv'
    INTO TABLE ort
    FIELDS TERMINATED BY ';'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (ID_Ort, Name, Adresse, Nordwert, Ostwert, Zoom, UpdateFlag);

# If Error "[42000][3948] Loading local data is disabled;
# this must be enabled on both the client and server sides"
# then try the following:
SET GLOBAL local_infile = 1;
# Then: Retry the command "LOAD DATA" above

# Else try to import with the MANUAL DATA IMPORT below.


# Test your Import
select * from ort
where Name like '%Bern%';

select * from ort;

delete from ort;



# MANUAL DATA IMPORT (Fallback-Solution)
INSERT INTO ort (ID_Ort, Name, Adresse, Nordwert, Ostwert, Zoom, UpdateFlag) VALUES
                                                                                 (1, 'Bundeshaus', 'Bundesplatz 3, 3003 Bern', NULL, NULL, 400, 0),
                                                                                 (2, 'Prime Tower', 'Hardstrasse 201, 8005 Zürich', NULL, NULL, 400, 0),
                                                                                 (3, 'Verkehrshaus der Schweiz', 'Lidostrasse 5, 6006 Luzern', NULL, NULL, 600, 0),
                                                                                 (4, 'Letzigrund Stadion', 'Badenerstrasse 500, 8048 Zürich', NULL, NULL, 500, 0),
                                                                                 (5, 'Bahnhof Olten', 'Bahnhofstrasse 22, 4600 Olten', 2635441.25, 1244664.125, 600, 1),
                                                                                 (6, 'Rheinfall', 'Rheinfallquai, 8212 Neuhausen am Rheinfall', 2688048.75, 1281511.5, 800, 1),
                                                                                 (7, 'Schloss Chillon', 'Avenue de Chillon 21, 1820 Veytaux', NULL, NULL, 400, 0),
                                                                                 (8, 'Zürich Hauptbahnhof', 'Bahnhofplatz, 8001 Zürich', NULL, NULL, 800, 0),
                                                                                 (9, 'Flughafen Zürich Terminal 1', '8058 Zürich-Flughafen', NULL, NULL, 2500, 0),
                                                                                 (10, 'St. Jakob-Park', 'St. Jakob-Strasse 395, 4052 Basel', NULL, NULL, 600, 0),
                                                                                 (11, 'Kultur- und Kongresszentrum KKL', 'Europaplatz 1, 6005 Luzern', 2666356.25, 1211434, 400, 1),
                                                                                 (12, 'Bahnhof Bern', 'Bahnhofplatz 10, 3011 Bern', 2600107.5, 1199722, 700, 1),
                                                                                 (13, 'Palais des Nations', 'Avenue de la Paix 14, 1211 Genève', NULL, NULL, 1000, 0),
                                                                                 (14, 'Stiftsbibliothek St. Gallen', 'Klosterhof 6, 9000 St. Gallen', NULL, NULL, 300, 0),
                                                                                 (15, 'Jet d\'Eau', 'Quai Gustave-Ador, 1207 Genève', NULL, NULL, 800, 0),
                                                                                 (16, 'Oerlikon Offene Rennbahn', 'Wallisellenstrasse 4, 8050 Zürich', NULL, NULL, 400, 0),
                                                                                 (17, 'Bahnhof Lausanne', 'Place de la Gare 5, 1003 Lausanne', NULL, NULL, 600, 0),
                                                                                 (18, 'Schloss Thun', 'Schlossberg 1, 3600 Thun', 2614617.5, 1178778.75, 300, 1),
                                                                                 (19, 'Tissot Arena', 'Boulevard des Sports 18, 2504 Biel', NULL, NULL, 600, 0),
                                                                                 (20, 'Maison Cailler', 'Rue Jules Bellet 7, 1636 Broc', 2574717.25, 1161805.5, 400, 1),
                                                                                 (21, 'Technorama', 'Technoramastrasse 1, 8404 Winterthur', 2699833.75, 1263377.625, 500, 1),
                                                                                 (22, 'Bahnhof Frauenfeld', 'Bahnhofplatz, 8500 Frauenfeld', 2709628, 1268393, 500, 1),
                                                                                 (23, 'Kybunpark', 'Zürcher Strasse 464, 9015 St. Gallen', 2740801.25, 1252460, 500, 1),
                                                                                 (24, 'Schloss Lenzburg', 'Schloss, 5600 Lenzburg', 2656372.25, 1248785, 400, 1),
                                                                                 (25, 'Papiliorama', 'Moosmatte 1, 3210 Kerzers', NULL, NULL, 400, 0),
                                                                                 (26, 'Bahnhof Chur', 'Bahnhofplatz, 7000 Chur', NULL, NULL, 600, 0),
                                                                                 (27, 'Kirche San Giovanni Battista', '6696 Mogno', NULL, NULL, 200, 0),
                                                                                 (28, 'Landesmuseum Zürich', 'Museumstrasse 2, 8001 Zürich', NULL, NULL, 400, 0),
                                                                                 (29, 'Bahnhof Ziegelbrücke', '8866 Ziegelbrücke', NULL, NULL, 600, 0),
                                                                                 (30, 'Goetheanum', 'Rüttiweg 45, 4143 Dornach', NULL, NULL, 500, 0),
                                                                                 (31, 'Stadion Wankdorf', 'Papiermühlestrasse 71, 3014 Bern', 2601995.75, 1201234, 600, 1),
                                                                                 (32, 'Kloster Einsiedeln', 'Klosterplatz 2, 8840 Einsiedeln', NULL, NULL, 600, 0),
                                                                                 (33, 'Bahnhof Bellinzona', 'Viale Stazione, 6500 Bellinzona', 2722498.75, 1116934.375, 500, 1),
                                                                                 (34, 'Bern Westside', 'Riedbachstrasse 98, 3027 Bern', NULL, NULL, 800, 0),
                                                                                 (35, 'Zoo Basel', 'Binningerstrasse 40, 4054 Basel', NULL, NULL, 800, 0),
                                                                                 (36, 'Bahnhof Lugano', 'Piazzale della Stazione, 6900 Lugano', NULL, NULL, 500, 0),
                                                                                 (37, 'Ozeanium (geplant/Bauplatz)', 'Heuwaage, 4051 Basel', NULL, NULL, 300, 0),
                                                                                 (39, 'Hallenstadion', 'Wallisellenstrasse 45, 8050 Zürich', NULL, NULL, 400, 0),
                                                                                 (40, 'Kloster Königsfelden', 'Zürcherstrasse, 5210 Windisch', NULL, NULL, 400, 0),
                                                                                 (41, 'Messe Basel (Halle 1)', 'Messeplatz 10, 4058 Basel', 2612287, 1268205.375, 600, 1),
                                                                                 (42, 'Bahnhof St. Gallen', 'Bahnhofplatz, 9000 St. Gallen', NULL, NULL, 600, 0),
                                                                                 (43, 'Schloss Rapperswil', 'Eichfeldstrasse, 8640 Rapperswil', 2705572.75, 1231800.75, 300, 1),
                                                                                 (44, 'Bahnhof Winterthur', 'Bahnhofplatz 7, 8400 Winterthur', NULL, NULL, 600, 0),
                                                                                 (45, 'Glattzentrum', 'Neue Winterthurerstrasse 99, 8304 Wallisellen', NULL, NULL, 800, 0),
                                                                                 (46, 'Shoppi Tivoli', 'Hochstrasse 1, 8957 Spreitenbach', 2670107.5, 1252671.75, 1000, 1),
                                                                                 (48, 'Castelgrande', 'Salita al Castelgrande 18, 6500 Bellinzona', 2722219.5, 1116895.125, 400, 1),
                                                                                 (49, 'Bahnhof Neuchâtel', 'Place de la Gare, 2000 Neuchâtel', NULL, NULL, 500, 0),
                                                                                 (50, 'KVA Josefstrasse (Turm)', 'Josefstrasse 205, 8005 Zürich', NULL, NULL, 300, 0),
                                                                                 (52, 'FIFA Museum', 'Seestrasse 27, 8002 Zürich', NULL, NULL, 200, 0),
                                                                                 (53, 'CERN Globe', 'Route de Meyrin 385, 1217 Meyrin', NULL, NULL, 400, 0),
                                                                                 (54, 'Bahnhof Zug', 'Bahnhofplatz, 6300 Zug', NULL, NULL, 500, 0),
                                                                                 (55, 'Siky Park', 'Chemin de la Forêt 1, 2743 Eschert', 2598694.5, 1234657.375, 400, 1),
                                                                                 (56, 'Bahnhof Aarau', 'Bahnhofstrasse 50, 5000 Aarau', NULL, NULL, 500, 0),
                                                                                 (57, 'Münster Bern', 'Münsterplatz 1, 3011 Bern', NULL, NULL, 300, 0),
                                                                                 (58, 'Bahnhof Schaffhausen', 'Bahnhofstrasse, 8200 Schaffhausen', NULL, NULL, 500, 0),
                                                                                 (59, 'Forum Fribourg', 'Route du Lac 12, 1763 Granges-Paccot', 2578229.5, 1185964.125, 500, 1),
                                                                                 (60, 'Bahnhof Fribourg', 'Place de la Gare, 1700 Fribourg', NULL, NULL, 600, 0),
                                                                                 (61, 'Swissminiatur', 'Via Rompada 16, 6815 Melide', NULL, NULL, 300, 0),
                                                                                 (62, 'Bahnhof Visp', 'Bahnhofplatz, 3930 Visp', 2634112.75, 1127022.75, 500, 1),
                                                                                 (63, 'Fondation Beyeler', 'Baselstrasse 101, 4125 Riehen', NULL, NULL, 400, 0),
                                                                                 (64, 'Bahnhof Spiez', 'Bahnhofstrasse 12, 3700 Spiez', 2618467.75, 1170633.375, 500, 1),
                                                                                 (65, 'Knies Kinderzoo', 'Oberseestrasse 36, 8640 Rapperswil', 2704800, 1231265.75, 400, 1),
                                                                                 (66, 'Bahnhof Thun', 'Bahnhofstrasse, 3600 Thun', 2614628.75, 1178364.25, 600, 1),
                                                                                 (67, 'Ballenberg West', 'Museumsstrasse 131, 3858 Hofstetten', NULL, NULL, 1200, 0),
                                                                                 (68, 'Bahnhof Montreux', 'Avenue des Alpes 74, 1820 Montreux', NULL, NULL, 500, 0),
                                                                                 (69, 'Chaplin\'s World', 'Route de Saint-Légier 2, 1804 Corsier-sur-Vevey', NULL, NULL, 500, 0),
                                                                                 (71, 'Alpamare', 'Gwattstrasse 12, 8808 Pfäffikon SZ', NULL, NULL, 500, 0),
                                                                                 (73, 'Autobahnraststätte Würenlos', 'A1, 5436 Würenlos', NULL, NULL, 600, 0),
                                                                                 (75, 'Zentralbibliothek Zürich', 'Zähringerplatz 6, 8001 Zürich', 2683551.5, 1247618.125, 200, 1),
                                                                                 (76, 'Bahnhof Uster', 'Bahnhofstrasse, 8610 Uster', NULL, NULL, 500, 0),
                                                                                 (77, 'Flugplatz Emmen', 'Emmen, Seetalstr. 175.97', 2667257, 1218115, 4000, 1),
                                                                                 (78, 'Bahnhof Wetzikon', 'Bahnhofstrasse, 8620 Wetzikon', NULL, NULL, 500, 0),
                                                                                 (79, 'Hafen Romanshorn', 'Friedrichshafnerstrasse, 8590 Romanshorn', 2745436.25, 1269097.75, 600, 1),
                                                                                 (80, 'Bahnhof Baden', 'Bahnhofstrasse 25, 5400 Baden', NULL, NULL, 400, 0),
                                                                                 (81, 'Landhaus Solothurn', 'Landhausquai 4, 4500 Solothurn', 2607488.75, 1228403.25, 200, 1),
                                                                                 (82, 'Bahnhof Liestal', 'Bahnhofplatz, 4410 Liestal', NULL, NULL, 400, 0),
                                                                                 (83, 'Dreispitzareal', 'Münchensteinerstrasse, 4053 Basel', NULL, NULL, 1200, 0),
                                                                                 (85, 'Schloss Laufen', 'Dachsen, Laufen am Rheinfall 2.1', 2687700.5, 1280421.5, 700, 1),
                                                                                 (87, 'Olympisches Museum, Olympiamuseum', 'Quai d\'Ouchy 1, 1006 Lausanne', 2538276.75, 1151058.75, 400, 1),
                                                                                 (89, 'Rolex Learning Center', 'Route Cantonale, 1024 Ecublens', NULL, NULL, 400, 0),
                                                                                 (91, 'Marmorbrücke (Grand Pont)', 'Place de la Riponne, 1005 Lausanne', NULL, NULL, 400, 0),
                                                                                 (92, 'Bahnhof Effretikon', 'Bahnhofsplatz, 8307 Illnau-Effretikon', NULL, NULL, 500, 0),
                                                                                 (93, 'Kaserne Basel', 'Klybeckstrasse 1b, 4057 Basel', NULL, NULL, 400, 0),
                                                                                 (94, 'Bahnhof Rapperswil', 'Bahnhofplatz, 8640 Rapperswil', 2704388, 1231372.375, 500, 1),
                                                                                 (95, 'Vögele Kultur Zentrum', 'Gwattstrasse 14, 8808 Pfäffikon SZ', 2702574.75, 1228481.5, 300, 1),
                                                                                 (96, 'Bahnhof Pfäffikon SZ', 'Bahnhofstrasse, 8808 Pfäffikon SZ', NULL, NULL, 500, 0),
                                                                                 (97, 'Schokoladenmuseum Lindt', 'Schokoladenplatz 1, 8802 Kilchberg', NULL, NULL, 400, 0),
                                                                                 (98, 'Bahnhof Meilen', 'Bahnhofstrasse, 8706 Meilen', NULL, NULL, 400, 0),
                                                                                 (99, 'Sauriermuseum Aathal', 'Zürichstrasse 69, 8607 Aathal', NULL, NULL, 400, 0),
                                                                                 (101, 'Tierpark Goldau', 'Parkweg 30, 6410 Goldau', NULL, NULL, 800, 0),
                                                                                 (102, 'Bahnhof Romanshorn', 'Bahnhofplatz, 8590 Romanshorn', NULL, NULL, 500, 0),
                                                                                 (103, 'Rathaus Basel', 'Marktplatz 9, 4001 Basel', NULL, NULL, 200, 0),
                                                                                 (104, 'Bahnhof Amriswil', 'Bahnhofstrasse, 8580 Amriswil', NULL, NULL, 400, 0),
                                                                                 (105, 'Sechseläutenplatz', 'Sechseläutenplatz, 8001 Zürich', NULL, NULL, 400, 0),
                                                                                 (106, 'Bahnhof Kreuzlingen', 'Bahnhofstrasse, 8280 Kreuzlingen', 2730188, 1279365, 500, 1),
                                                                                 (107, 'Conny-Land', 'Connylandstrasse 1, 8564 Lipperswil', NULL, NULL, 500, 0),
                                                                                 (109, 'Sitterviadukt BT', 'Sittertalstrasse, 9014 St. Gallen', NULL, NULL, 600, 0),
                                                                                 (110, 'Bahnhof Gossau', 'Gossau, Sportstr. 13', 2736792.25, 1253284.625, 500, 1),
                                                                                 (111, 'Kyburg', 'Schloss Kyburg, 8314 Kyburg', NULL, NULL, 300, 0),
                                                                                 (113, 'Abtei Payerne', 'Place du Marché, 1530 Payerne', NULL, NULL, 300, 0),
                                                                                 (115, 'Schloss Greyerz', 'Rue du Château 8, 1663 Gruyères', NULL, NULL, 300, 0),
                                                                                 (117, 'Grande Dixence (Basis)', 'Val d\'Hérens, 1987 Hérémence', NULL, NULL, 1000, 0),
                                                                                 (119, 'Bahnhof Brig', 'Bahnhofplatz, 3902 Brig', NULL, NULL, 600, 0),
                                                                                 (120, 'Stockalperschloss', 'Alte Vereina-Strasse, 3900 Brig', NULL, NULL, 400, 0),
                                                                                 (121, 'Bahnhof Locarno', 'Muralto, Via Scazziga Vittore 8', 2704454.5, 1113517, 500, 1),
                                                                                 (122, 'Piazza Grande', '6600 Locarno', NULL, NULL, 400, 0),
                                                                                 (123, 'Bahnhof Biasca', 'Via alla Stazione, 6710 Biasca', 2718031.75, 1135761.5, 400, 1),
                                                                                 (124, 'Schloss Sargans', 'Schlossstrasse, 7320 Sargans', NULL, NULL, 300, 0),
                                                                                 (125, 'Bahnhof Sargans', 'Bahnhofstrasse, 7320 Sargans', NULL, NULL, 500, 0),
                                                                                 (126, 'Tamina Therme', 'Hans-Albrecht-Strasse, 7310 Bad Ragaz', 2757140.25, 1207415.75, 400, 1),
                                                                                 (129, 'Hallenbad City', 'Sihlstrasse 71, 8001 Zürich', NULL, NULL, 200, 0),
                                                                                 (130, 'Bahnhof Landquart', 'Bahnhofplatz, 7302 Landquart', NULL, NULL, 600, 0),
                                                                                 (131, 'Bahnhof Davos Platz', 'Talstrasse, 7270 Davos', NULL, NULL, 500, 0),
                                                                                 (132, 'Eisstadion Davos (Vaillant Arena)', 'Talstrasse 41, 7270 Davos', NULL, NULL, 400, 0),
                                                                                 (133, 'Bahnhof St. Moritz', 'Via Veglia, 7500 St. Moritz', NULL, NULL, 500, 0),
                                                                                 (134, 'Schanze Einsiedeln', 'Schnabelsbergstrasse, 8840 Einsiedeln', NULL, NULL, 500, 0),
                                                                                 (135, 'Bahnhof Samedan', 'Bahnhofplatz, 7503 Samedan', NULL, NULL, 500, 0),
                                                                                 (136, 'Flugplatz Samedan', 'Plazza Aviatica 2, 7503 Samedan', NULL, NULL, 1500, 0),
                                                                                 (137, 'Bahnhof Scuol-Tarasp', '7550 Scuol', NULL, NULL, 400, 0),
                                                                                 (138, 'Bärenpark Bern', 'Grosser Muristalden 6, 3006 Bern', 2601603.5, 1199624.875, 400, 1),
                                                                                 (139, 'Bahnhof Langenthal', 'Eisenbahnstr. 7, 4900 Langenthal', 2626537.75, 1229142.125, 500, 1),
                                                                                 (140, 'Zentrum Paul Klee', 'Monument im Fruchtland 3, 3006 Bern', NULL, NULL, 600, 0),
                                                                                 (146, 'Internationales Uhrenmuseum', 'Rue des Musées 29, 2300 La Chaux-de-Fonds', NULL, NULL, 300, 0),
                                                                                 (149, 'Bahnhof Payerne', 'Place de la Gare, 1530 Payerne', NULL, NULL, 400, 0),
                                                                                 (153, 'Bahnhof Lyss', 'Bahnhofstrasse, 3250 Lyss', 2589948, 1213762.875, 500, 1),
                                                                                 (159, 'Bahnhof Lenzburg', 'Lenzburg, Bahnhofstr. 50', 2655839.75, 1248802.625, 500, 1),
                                                                                 (162, 'Bahnhof Rheinfelden', 'Bahnhofstrasse, 4310 Rheinfelden', 2626599, 1267165, 400, 1),
                                                                                 (164, 'Bahnhof Muttenz', 'Bahnhofstrasse 62, 4132 Muttenz', 2615795.5, 1264185, 600, 1),
                                                                                 (171, 'Bahnhof Rotkreuz', 'Bahnhofplatz, 6343 Holzhäusern', NULL, NULL, 600, 0),
                                                                                 (174, 'Bahnhof Thalwil', 'Gotthardstr. 24, 8800 Thalwil', 2685311, 1238817.375, 500, 1),
                                                                                 (175, 'Bahnhof Horgen', 'Bahnhofstrasse, 8810 Horgen', 2687539, 1235168.75, 400, 1),
                                                                                 (176, 'Bahnhof Wädenswil', 'Bahnhofstrasse, 8820 Wädenswil', 2693700.25, 1231533.25, 500, 1),
                                                                                 (178, 'Bahnhof Küsnacht ZH', 'Bahnhofstrasse, 8700 Küsnacht', NULL, NULL, 400, 0),
                                                                                 (179, 'Bahnhof Zollikon', 'Bahnhofstrasse, 8702 Zollikon', 2685356.25, 1243765.25, 300, 1),
                                                                                 (182, 'Bahnhof Hinwil', 'Hinwil, Bahnhofplatz 1.5', 2706085.75, 1239753.875, 500, 1),
                                                                                 (184, 'Bahnhof Dübendorf', 'Bahnhofstrasse, 8600 Dübendorf', NULL, NULL, 500, 0),
                                                                                 (185, 'Bahnhof Bassersdorf', 'Bahnhofstrasse, 8303 Bassersdorf', NULL, NULL, 400, 0),
                                                                                 (186, 'Bahnhof Kloten', 'Bahnhofstrasse, 8302 Kloten', NULL, NULL, 400, 0),
                                                                                 (187, 'Bahnhof Bülach', 'Bahnhofstrasse, 8180 Bülach', NULL, NULL, 500, 0),
                                                                                 (192, 'Bahnhof Baden', 'Bahnhofstrasse, 5400 Baden', 2665507.5, 1258468, 500, 1);