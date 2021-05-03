--Début création Tables

create table Dragons (
    Dragon varchar(30) PRIMARY KEY,
    Sexe char(1) constraint sexe check (Sexe = 'M' or Sexe = 'F'),
    Longueur int constraint longueur_positive check (Longueur > 0),
    Ecailles int constraint nb_ecailles_positifs check (Ecailles >= 0),
    CracheFeu char(1) constraint crachefeuON check (CracheFeu = 'O' or CracheFeu = 'N'),
    EnAmour varchar(30) constraint enamour check (EnAmour in ('macho', 'timide', 'sincere', 'volage'))
);

create table Nourritures (
    Produit varchar(30) PRIMARY KEY,
    Calories int constraint nb_calorie_positif check (Calories >= 0)
);

create table Repas (
    Dragon varchar(30) references Dragons(Dragon),
    Produit varchar(30) references Nourritures(Produit),
    Quantite int constraint Quantité_positive check (Quantite >= 0),
    constraint keys PRIMARY KEY (Dragon, Produit)
);

create table Amours (
    DragonAimant varchar(30) references Dragons(Dragon) PRIMARY KEY,
    DragonAime varchar(30) references Dragons(Dragon),
    force varchar(30) constraint forceon check (force in ('un peu', 'beaucoup', 'passionnement', 'a la folie'))
);

--Fin création Tables

--Début insertion Données
insert into Dragons(Dragon,Sexe,Longueur,Ecailles,CracheFeu,EnAmour) values ('Smeagol','M',152,1857,'O','macho');
insert into Dragons(Dragon,Sexe,Longueur,Ecailles,CracheFeu,EnAmour) values ('Birdurh','M',258,4787,'N','timide');
insert into Dragons(Dragon,Sexe,Longueur,Ecailles,CracheFeu,EnAmour) values ('Negueth','F',128,1582,'O','sincere');
insert into Dragons(Dragon,Sexe,Longueur,Ecailles,CracheFeu,EnAmour) values ('MissToc','F',183,2781,'N','volage');
insert into Dragons(Dragon,Sexe,Longueur,Ecailles,CracheFeu,EnAmour) values ('Bolong', 'M',213,2754,'O','macho');
insert into Dragons(Dragon,Sexe,Longueur,Ecailles,CracheFeu,EnAmour) values ('Miloch', 'M', 83, 718,'O','timide');
insert into Dragons(Dragon,Sexe,Longueur,Ecailles,CracheFeu,EnAmour) values ('Nessie', 'M',168,1721,'N','macho');
insert into Dragons(Dragon,Sexe,Longueur,Ecailles,CracheFeu,EnAmour) values ('Tarak',  'F',123, 851,'O','timide');
insert into Dragons(Dragon,Sexe,Longueur,Ecailles,CracheFeu,EnAmour) values ('Solong', 'M',173,1481,'O','timide');

insert into Amours(DragonAimant,DragonAime,Force) values ('Smeagol', 'Tarak',   'passionnement');
insert into Amours(DragonAimant,DragonAime,Force) values ('Birdurh', 'Negueth', 'beaucoup');
insert into Amours(DragonAimant,DragonAime,Force) values ('Negueth', 'Miloch',  'a la folie');
insert into Amours(DragonAimant,DragonAime,Force) values ('Miloch',  'Negueth', 'a la folie');
insert into Amours(DragonAimant,DragonAime,Force) values ('Tarak',   'Bolong',  'un peu');
insert into Amours(DragonAimant,DragonAime,Force) values ('Bolong',  'Tarak',   'beaucoup');
insert into Amours(DragonAimant,DragonAime,Force) values ('Nessie',  'Tarak',   'un peu');

insert into Nourritures(Produit,Calories) values ('pomme',      7);
insert into Nourritures(Produit,Calories) values ('cacahuete', 10);
insert into Nourritures(Produit,Calories) values ('orange',    25);
insert into Nourritures(Produit,Calories) values ('oeuf',      15);
insert into Nourritures(Produit,Calories) values ('ver',        3);
insert into Nourritures(Produit,Calories) values ('poisson',   35);

insert into Repas(Dragon,Produit,Quantite) values ('Smeagol', 'cacahuete',1000);
insert into Repas(Dragon,Produit,Quantite) values ('Smeagol', 'pomme',      16);
insert into Repas(Dragon,Produit,Quantite) values ('Bolong',  'oeuf',        4);
insert into Repas(Dragon,Produit,Quantite) values ('Negueth', 'orange',      6);
insert into Repas(Dragon,Produit,Quantite) values ('Negueth', 'oeuf',        1);
insert into Repas(Dragon,Produit,Quantite) values ('Miloch',  'cacahuete', 100);
insert into Repas(Dragon,Produit,Quantite) values ('Tarak',   'pomme',      10);
insert into Repas(Dragon,Produit,Quantite) values ('Tarak',   'orange',     10);
insert into Repas(Dragon,Produit,Quantite) values ('Solong',  'oeuf',        6);
insert into Repas(Dragon,Produit,Quantite) values ('Solong',  'orange',      2);
insert into Repas(Dragon,Produit,Quantite) values ('Miloch',  'ver',        53);
insert into Repas(Dragon,Produit,Quantite) values ('Nessie',  'poisson',    20);
insert into Repas(Dragon,Produit,Quantite) values ('Solong',  'poisson',     1);
--Fin insertion Données

