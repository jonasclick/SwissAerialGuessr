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
LOAD DATA local INFILE '.\\database\\ort.csv'
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
select * from ort;

# MANUAL DATA IMPORT with insert command (Fallback-Solution)
INSERT INTO ort (ID_Ort, Name, Adresse, Nordwert, Ostwert, Zoom, UpdateFlag) VALUES
                                                                                 (1, 'Bundeshaus', 'Bundesplatz 3, 3003 Bern', NULL, NULL, 400, 0),
                                                                                 (2, 'Prime Tower', 'Hardstrasse 201, 8005 Zürich', NULL, NULL, 400, 0),
                                                                                 (3, 'Verkehrshaus der Schweiz', 'Lidostrasse 5, 6006 Luzern', NULL, NULL, 600, 0),
                                                                                 (4, 'Letzigrund Stadion', 'Badenerstrasse 500, 8048 Zürich', NULL, NULL, 500, 0),
                                                                                 (5, 'Bahnhof Olten', 'Bahnhofstrasse 22, 4600 Olten', 2635441.25, 1244664.125, 600, 1),
                                                                                 (6, 'Rheinfall', 'Rheinfallquai, 8212 Neuhausen am Rheinfall', 2688048.75, 1281511.5, 800, 1),
                                                                                 (7, 'Schloss Chillon', 'Avenue de Chillon 21, 1820 Veytaux', NULL, NULL, 400, 0),
                                                                                 (8, 'Zürich Hauptbahnhof', 'Bahnhofplatz, 8001 Zürich', 2683260.75, 1247919.125, 800, 0),
                                                                                 (9, 'Flughafen Zürich Terminal 1', '8058 Zürich-Flughafen', NULL, NULL, 4000, 0),
                                                                                 (10, 'St. Jakob-Park', 'St. Jakob-Strasse 395, 4052 Basel', 2613584.5, 1265612.875, 600, 0),
                                                                                 (11, 'KKL Luzern', 'Europaplatz 1, 6005 Luzern', 2666356.25, 1211434, 400, 0),
                                                                                 (12, 'Bahnhof Bern', 'Bahnhofplatz 10, 3011 Bern', 2600107.5, 1199722, 700, 0),
                                                                                 (13, 'Palais des Nations', 'Avenue de la Paix 14, 1211 Genève', NULL, NULL, 1000, 0),
                                                                                 (14, 'Stiftsbibliothek St. Gallen', 'Klosterhof 6, 9000 St. Gallen', NULL, NULL, 300, 0),
                                                                                 (15, 'Jet d''Eau', 'Quai Gustave-Ador, 1207 Genève', NULL, NULL, 800, 0),
                                                                                 (16, 'Oerlikon Offene Rennbahn', 'Wallisellenstrasse 4, 8050 Zürich', NULL, NULL, 400, 0),
                                                                                 (18, 'Schloss Thun', 'Schlossberg 1, 3600 Thun', 2614617.5, 1178778.75, 300, 1),
                                                                                 (19, 'Tissot Arena', 'Boulevard des Sports 18, 2504 Biel', NULL, NULL, 600, 0),
                                                                                 (20, 'Maison Cailler', 'Rue Jules Bellet 7, 1636 Broc', 2574717.25, 1161805.5, 400, 0),
                                                                                 (21, 'Technorama', 'Technoramastrasse 1, 8404 Winterthur', 2699833.75, 1263377.625, 500, 0),
                                                                                 (22, 'Bahnhof Frauenfeld', 'Bahnhofplatz, 8500 Frauenfeld', 2709628, 1268393, 500, 1),
                                                                                 (23, 'Kybunpark', 'Zürcher Strasse 464, 9015 St. Gallen', 2740801.25, 1252460, 500, 0),
                                                                                 (24, 'Schloss Lenzburg', 'Schloss, 5600 Lenzburg', 2656372.25, 1248785, 400, 1),
                                                                                 (25, 'Papiliorama', 'Moosmatte 1, 3210 Kerzers', NULL, NULL, 400, 0),
                                                                                 (26, 'Bahnhof Chur', 'Bahnhofplatz 1, 7000 Chur', NULL, NULL, 600, 1),
                                                                                 (27, 'Kirche San Giovanni Battista', '6696 Mogno', NULL, NULL, 200, 0),
                                                                                 (28, 'Landesmuseum Zürich', 'Museumstrasse 2, 8001 Zürich', NULL, NULL, 400, 0),
                                                                                 (30, 'Goetheanum', 'Rüttiweg 45, 4143 Dornach', NULL, NULL, 500, 0),
                                                                                 (31, 'Stadion Wankdorf', 'Papiermühlestrasse 71, 3014 Bern', 2601995.75, 1201234, 600, 0),
                                                                                 (32, 'Kloster Einsiedeln', 'Klosterplatz 2, 8840 Einsiedeln', 2699590.25, 1220453.75, 600, 0),
                                                                                 (34, 'Bern Westside', 'Riedbachstrasse 98, 3027 Bern', NULL, NULL, 800, 0),
                                                                                 (35, 'Zoo Basel', 'Binningerstrasse 40, 4054 Basel', NULL, NULL, 800, 0),
                                                                                 (39, 'Hallenstadion', 'Wallisellenstrasse 45, 8050 Zürich', NULL, NULL, 400, 0),
                                                                                 (40, 'Kloster Königsfelden', 'Zürcherstrasse, 5210 Windisch', NULL, NULL, 400, 0),
                                                                                 (41, 'Messe Basel (Halle 1)', 'Messeplatz 10, 4058 Basel', 2612287, 1268205.375, 600, 0),
                                                                                 (42, 'Bahnhof St. Gallen', 'St. Gallen, Poststr. 28', NULL, NULL, 600, 1),
                                                                                 (43, 'Schloss Rapperswil', 'Eichfeldstrasse, 8640 Rapperswil', 2705572.75, 1231800.75, 300, 1),
                                                                                 (45, 'Glattzentrum', 'Neue Winterthurerstrasse 99, 8304 Wallisellen', NULL, NULL, 800, 0),
                                                                                 (46, 'Shoppi Tivoli', 'Hochstrasse 1, 8957 Spreitenbach', 2670107.5, 1252671.75, 1000, 1),
                                                                                 (48, 'Castelgrande', 'Salita al Castelgrande 18, 6500 Bellinzona', 2722219.5, 1116895.125, 400, 1),
                                                                                 (50, 'KVA Josefstrasse (Turm)', 'Josefstrasse 205, 8005 Zürich', NULL, NULL, 300, 0),
                                                                                 (52, 'FIFA Museum', 'Seestrasse 27, 8002 Zürich', NULL, NULL, 200, 0),
                                                                                 (53, 'CERN Globe', 'Route de Meyrin 385, 1217 Meyrin', 2493089, 1121223.5, 400, 0),
                                                                                 (55, 'Siky Park', 'Chemin de la Forêt 1, 2743 Eschert', 2598694.5, 1234657.375, 400, 1),
                                                                                 (57, 'Münster Bern', 'Münsterplatz 1, 3011 Bern', NULL, NULL, 300, 0),
                                                                                 (59, 'Forum Fribourg', 'Route du Lac 12, 1763 Granges-Paccot', 2578229.5, 1185964.125, 500, 1),
                                                                                 (61, 'Swissminiatur', 'Melide, Via Cantonale 11', 2716867.5, 1090180.125, 300, 1),
                                                                                 (63, 'Fondation Beyeler', 'Baselstrasse 101, 4125 Riehen', NULL, NULL, 400, 0),
                                                                                 (65, 'Knies Kinderzoo', 'Oberseestrasse 36, 8640 Rapperswil', 2704800, 1231265.75, 400, 0),
                                                                                 (67, 'Ballenberg West', 'Museumsstrasse 131, 3858 Hofstetten', NULL, NULL, 1200, 0),
                                                                                 (69, 'Chaplin''s World', 'Route de Saint-Légier 2, 1804 Corsier-sur-Vevey', NULL, NULL, 500, 0),
                                                                                 (71, 'Alpamare', 'Gwattstrasse 12, 8808 Pfäffikon SZ', NULL, NULL, 500, 0),
                                                                                 (73, 'Autobahnraststätte Würenlos', 'A1, 5436 Würenlos', 2668589, 1254630.875, 600, 0),
                                                                                 (75, 'Zentralbibliothek Zürich', 'Zähringerplatz 6, 8001 Zürich', 2683551.5, 1247618.125, 200, 1),
                                                                                 (77, 'Flugplatz Emmen', 'Emmen, Seetalstr. 175.97', 2667257, 1218115, 4000, 1),
                                                                                 (79, 'Hafen Romanshorn', 'Romanshorn, Friedrichshafnerstr. 55', 2745436.25, 1269097.75, 600, 1),
                                                                                 (81, 'Landhaus Solothurn', 'Landhausquai 4, 4500 Solothurn', 2607488.75, 1228403.25, 200, 0),
                                                                                 (83, 'Dreispitzareal', 'Münchensteinerstrasse, 4053 Basel', NULL, NULL, 1200, 0),
                                                                                 (85, 'Schloss Laufen', 'Dachsen, Laufen am Rheinfall 2.1', 2687700.5, 1280421.5, 700, 1),
                                                                                 (87, 'Olympisches Museum, Olympiamuseum', 'Quai d''Ouchy 1, 1006 Lausanne', 2538276.75, 1151058.75, 400, 1),
                                                                                 (89, 'Rolex Learning Center', 'Route Cantonale, 1024 Ecublens', NULL, NULL, 400, 0),
                                                                                 (91, 'Marmorbrücke (Grand Pont)', 'Place de la Riponne, 1005 Lausanne', NULL, NULL, 400, 0),
                                                                                 (93, 'Kaserne Basel', 'Klybeckstrasse 1b, 4057 Basel', NULL, NULL, 400, 0),
                                                                                 (95, 'Vögele Kultur Zentrum', 'Gwattstrasse 14, 8808 Pfäffikon SZ', 2702574.75, 1228481.5, 300, 1),
                                                                                 (97, 'Schokoladenmuseum Lindt', 'Schokoladenplatz 1, 8802 Kilchberg', NULL, NULL, 400, 0),
                                                                                 (99, 'Sauriermuseum Aathal', 'Zürichstrasse 69, 8607 Aathal', NULL, NULL, 400, 0),
                                                                                 (101, 'Tierpark Goldau', 'Parkweg 30, 6410 Goldau', NULL, NULL, 800, 0),
                                                                                 (103, 'Rathaus Basel', 'Marktplatz 9, 4001 Basel', NULL, NULL, 200, 0),
                                                                                 (105, 'Sechseläutenplatz', 'Sechseläutenplatz, 8001 Zürich', NULL, NULL, 400, 0),
                                                                                 (107, 'Conny-Land', 'Connylandstrasse 1, 8564 Lipperswil', NULL, NULL, 500, 0),
                                                                                 (109, 'Sitterviadukt BT', 'Sittertalstrasse, 9014 St. Gallen', NULL, NULL, 600, 0),
                                                                                 (111, 'Kyburg', 'Schloss Kyburg, 8314 Kyburg', 2698404.75, 1257229.625, 300, 0),
                                                                                 (113, 'Abtei Payerne', 'Place du Marché, 1530 Payerne', 2561675, 1185628.75, 300, 0),
                                                                                 (115, 'Schloss Greyerz', 'Rue du Château 8, 1663 Gruyères', 2572781.5, 1159326.125, 300, 0),
                                                                                 (117, 'Lac des Dix Staumauer', 'Hérémence, Rte du Barrage 69', 2604222.75, 1103422.5, 1000, 0),
                                                                                 (119, 'Bahnhof Brig', 'Brig, Bahnhofstr. 2', NULL, NULL, 600, 1),
                                                                                 (120, 'Stockalperschloss', 'Alte Vereina-Strasse, 3900 Brig', NULL, NULL, 400, 0),
                                                                                 (121, 'Bahnhof Locarno', 'Muralto, Via Scazziga Vittore 8', 2704454.5, 1113517, 500, 1),
                                                                                 (122, 'Piazza Grande', 'Piazza Grande 7, 6600 Locarno', NULL, NULL, 400, 0),
                                                                                 (123, 'Bahnhof Biasca', 'Biasca, Via Bellinzona 5', 2718173, 1134584.375, 400, 1),
                                                                                 (124, 'Schloss Sargans', 'Schlossstrasse, 7320 Sargans', NULL, NULL, 300, 0),
                                                                                 (126, 'Tamina Therme', 'Hans-Albrecht-Strasse, 7310 Bad Ragaz', 2757140.25, 1207415.75, 400, 1),
                                                                                 (129, 'Hallenbad City Zürich', 'Sihlstrasse 72, 8001 Zürich', 2682651.75, 1247403.75, 200, 0),
                                                                                 (132, 'Eisstadion Davos (Vaillant Arena)', 'Talstrasse 41, 7270 Davos', NULL, NULL, 400, 0),
                                                                                 (133, 'Bahnhof St. Moritz', 'St. Moritz, Via Grevas 65', NULL, NULL, 500, 1),
                                                                                 (134, 'Schanze Einsiedeln', 'Schnabelsbergstrasse, 8840 Einsiedeln', NULL, NULL, 500, 0),
                                                                                 (135, 'Bahnhof Samedan', 'Samedan, Via Retica 22', 2786751.75, 1156529.875, 500, 1),
                                                                                 (136, 'Flugplatz Samedan', 'Plazza Aviatica 11, 7503 Samedan', 2786897.25, 1156100.375, 1500, 1),
                                                                                 (137, 'Bahnhof Scuol-Tarasp', 'Scuol, Via da la Staziun 40', 2817367.5, 1186444.125, 400, 1),
                                                                                 (138, 'Bärenpark Bern', 'Grosser Muristalden 6, 3006 Bern', 2601603.5, 1199624.875, 400, 1),
                                                                                 (140, 'Zentrum Paul Klee', 'Monument im Fruchtland 3, 3006 Bern', NULL, NULL, 600, 0),
                                                                                 (146, 'Internationales Uhrenmuseum', 'Rue des Musées 29, 2300 La Chaux-de-Fonds', NULL, NULL, 300, 0),
                                                                                 (159, 'Bahnhof Lenzburg', 'Lenzburg, Bahnhofstr. 50', 2655839.75, 1248802.625, 500, 1),
                                                                                 (174, 'Bahnhof Thalwil', 'Gotthardstr. 24, 8800 Thalwil', 2685113.75, 1238918.25, 500, 1),
                                                                                 (176, 'Bahnhof Wädenswil', 'Wädenswil, Bahnhofstr. 9', 2693609, 1231703.75, 500, 1),
                                                                                 (178, 'Bahnhof Küsnacht ZH', 'Küsnacht, Kohlrainstr. 16', NULL, NULL, 400, 1),
                                                                                 (182, 'Bahnhof Hinwil', 'Hinwil, Bahnhofplatz 1.5', 2706085.75, 1239753.875, 500, 1),
                                                                                 (185, 'Bahnhof Bassersdorf', 'Bassersdorf, Bahnhofstr. 40.1', 2689739.5, 1255290.75, 400, 1),
                                                                                 (186, 'Bahnhof Kloten', 'Lindenstrasse 10, 8302 Kloten', 2686265.25, 1256007.625, 400, 1);