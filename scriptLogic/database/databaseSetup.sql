create database swissaerialguessr;
use swissaerialguessr;

drop table ort;
create table ort (
    ID_Ort int primary key auto_increment,
    Name VARCHAR(250) not null,
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


INSERT INTO ort (Name, Adresse, Zoom) VALUES
      ('Bundeshaus', 'Bundesplatz 3, 3003 Bern', 400),
      ('Prime Tower', 'Hardstrasse 201, 8005 Zürich', 500),
      ('Jet d''Eau', 'Quai Gustave-Ador, 1207 Genève', 800),
      ('Schloss Chillon', 'Avenue de Chillon 21, 1820 Veytaux', 600);