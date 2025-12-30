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
LOAD DATA LOCAL INFILE './tabelleOrte.csv'
    INTO TABLE ort
    FIELDS TERMINATED BY ';'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (ID_Ort, Name, Adresse, Nordwert, Ostwert, Zoom);

select * from ort
where Name like '%Bahnhof%';

select * from ort;
