drop database if exists newpokemondatabase;

create database newpokemondatabase;
use newpokemondatabase;

create table Generation(
GenNum int,
genName varchar(255),
yearStart int,
yearEnd int,
primary key(genNum));

insert into Generation(genNum, genName, yearStart, yearEnd) value
	(1, "Kanto", 1996, 2000),
	(2, "Johto", 2000, 2003);

create table pokeType(
TypeName varchar(255) primary key);

insert into pokeType(TypeName) values
	('Darkness'),
    ('Water'),
    ('Fire'),
    ('Fighting'),
    ('Colorless'),
    ('Lightning'),
    ('Metal'),
    ('Grass'),
    ('Psychic');

create table TypeGen(
TAK int,
TypeName varchar(255),
GenNum int,
Weakness varchar(255),
primary key(TAK),
foreign key(TypeName) references pokeType(TypeName),
foreign key(GenNum) references Generation(GenNum));

insert into TypeGen(TAK, TypeName, GenNum, Weakness) values
	(1, 'Water', 1, 'Grass'),
    (2, 'Fire', 1, 'Water'),
    (3, 'Fighting', 1, 'Psychic'),
    (4, 'Colorless', 1, 'Fighting'),
	(5, 'Lightning', 1, 'Fighting'),
    (6, 'Grass', 1, 'Fire'),
    (7, 'Psychic', 1, 'Psychic'),
    (8, 'Darkness', 2, 'Fighting'),
    (9, 'Water', 2, 'Grass'),
    (10, 'Fire', 2, 'Water'),
    (11, 'Fighting', 2, 'Psychic'),
    (12, 'Colorless', 2, 'Fighting'),
    (13, 'Lightning', 2, 'Fighting'),
    (14, 'Metal', 2, 'Fire'),
    (15, 'Grass', 2, 'Fire'),
    (16, 'Psychic', 2, 'Darkness');


create table Pokemon(
pName varchar(255),
preEvol varchar(255),
Evolution varchar(255),
primary key(pName));

insert into Pokemon(pName, preEvol, Evolution) values
	('Alakazam', 'Kadabra', null),
    ('Blastoise', 'Wartortle', null),
    ('Chansey', null, null),
    ('Charizard', 'Charmeleon', null),
    ('Clefairy', null, 'Clefable'),
    ('Gyarados', 'Magikarp', null),
    ('Hitmonchan', null, null),
    ('Machamp', 'Machoke', null),
    ('Magneton', null, null),
    ('Mewtwo', null, null),
    ('Nidoking', 'Nidorino', null),
    ('Ninetales', 'Vulpix', null),
    ('Poliwrath', 'Poliwhirl', null),
    ('Raichu', 'Pikachu', null),
    ('Venasaur', 'Ivysaur', null),
    ('Zapdos', null, null),
    ('Beedrill', 'Kakuna', null),
    ('Dragonair', 'Dratini', null),
    ('Dugtrio', 'Diglett', null),
    ('Electabuzz', null, null),
    ('Electrode', 'Voltorb', null),
    ('Pidgeotto', 'Pidgey', 'Pidgeot'),
    ('Arcanine', 'Growlithe', null),
    ('Charmeleon', 'Charmander', 'Charizard'),
    ('Dewgong', 'Seel', null),
    ('Dratini', null, 'Dragonair'),
    ("Farfetch'd", null, null),
    ('Growlithe', null, 'Arcanine'),
    ('Haunter', 'Gastly', 'Gengar'),
    ('Ivysaur', 'Bulbasaur', 'Venasaur'),
    ('Jynx', null, null),
    ('Kadabra', 'Abra', 'Alakazam'),
    ('Kakuna', 'Weedle', 'Beedrill'),
    ('Machoke', 'Machop', 'Machamp'),
    ('Magikarp', null, 'Gyarados'),
    ('Magmar', null, null),
    ('Nidorino', 'Nidoran male', 'Nidoking'),
    ('Poliwhirl', null, 'Poliwrath'),
    ('Porygon', null, 'Porygon 2'),
    ('Raticate', 'Rattata', null),
    ('Seel', null, 'Dewgong'),
    ('Wartortle', 'Squirtle', 'Blastoise'),
    ('Abra', null, 'Kadabra'),
    ('Bulbasaur', null, 'Ivysaur'),
    ('Caterpie', null, 'Metapod'),
    ('Charmander', null, 'Charmeleon'),
    ('Diglett', null, 'Dugtrio'),
    ('Doduo', null, 'Dodrio'),
    ('Drowzee', null, 'Hypno'),
    ('Gastly', null, 'Haunter'),
    ('Koffing', null, 'Weezing'),
    ('Machop', null, 'Machoke'),
    ('Magnemite', null, 'Magneton'),
    ('Metapod', 'Caterpie', 'Butterfree'),
    ('Nidorina', 'Nidoran female', 'Nidoqueen'),
    ('Onix', null, 'Steelix'),
    ('Pidgey', null, 'Pidgeotto'),
    ('Pikachu', 'Pichu', 'Raichu'),
    ('Poliwag', null, 'Poliwhirl'),
    ('Ponyta', null, 'Rapidash'),
    ('Rattata', null, 'Radicate'),
    ('Sandshrew', null, 'Sandslash'),
    ('Squirtle', null, 'Wartortle'),
    ('Starmie', 'Staryu', null),
    ('Staryu', null, 'Starmie'),
    ('Tangela', null, null),
    ('Voltorb', null, 'Electrode'),
    ('Vulpix', null, 'Ninetales'),
    ('Weedle', null, 'Kakuna'),
    ('Ampharos', 'Flaffy', null),
    ('Azumarill', 'Marill', null),
    ('Bellossom', 'Gloom', null),
    ('Feraligatr', 'Croconaw', null),
    ('Heracross', null, null),
    ('Jumpluff', 'Skiploom', null),
    ('Kingdra', 'Seadra', null),
    ('Lugia', null, null),
    ('Meganium', 'Bayleef', null),
    ('Pichu', null, 'Pikachu'),
    ('Skarmory', null, null),
    ('Slowking', 'Slowpoke', null),
    ('Steelix', 'Onix', null),
    ('Togetic', 'Togepi', null),
    ('Typhlosion', 'Quilava', null),
    ('Cleffa', null, 'Clefairy'),
    ('Donphan', 'Phanpy', null),
    ('Elekid', null, 'Electrobuzz'),
    ('Magby', null, 'Magmar'),
    ('Murkrow', null, null),
    ('Sneasel', null, null),
    ('Aipom', null, null),
    ('Ariados', 'Spinarak', null),
    ('Bayleef', 'Chikorita', 'Meganium'),
    ('Croconaw', 'Tododile', 'Feraligatr'),
    ('Flaaffy', 'Mareep', 'Ampharos'),
    ('Furret', 'Sentret', null),
    ('Gloom', 'Oddish', 'Vileplume'),
    ('Granbull', 'Snubbull', null),
    ('Lanturn', 'Chinchou', null),
    ('Ledian', 'Ledyba', null),
    ('Miltank', null, null),
    ('Noctowl', 'Hoothoot', null),
    ('Phanpy', null, 'Donphan'),
    ('Piloswine', 'Swinub', null),
    ('Quagsire', 'Wooper', null),
    ('Quilava', 'Cyndaquil', 'Typhlosion'),
    ('Seadra', 'Horsea', 'Kingdra'),
    ('Skiploom', 'Hoppip', null),
    ('Sunflora', 'Sunkern', null),
    ('Togepi', null, 'Togetic'),
    ('Xatu', 'Natu', null),
    ('Chikorita', null, 'Bayleef'),
    ('Chinchou', null, 'Lanturn'),
    ('Cyndaquil', null, 'Quilava'),
    ('Girafarig', null, null),
    ('Gligar', null, null),
    ('Hoothoot', null, 'Noctowl'),
    ('Hoppip', null, 'Skiploom'),
    ('Horsea', null, 'Seadra'),
    ('Ledyba', null, 'Ledian'),
    ('Mantine', 'Mantyke', null),
    ('Mareep', null, 'Flaffy'),
    ('Marill', null, 'Azumarill'),
    ('Natu', null, 'Xatu'),
    ('Oddish', null, 'Gloom'),
    ('Sentret', null, 'Furret'),
    ('Shuckle', null, null),
    ('Slowpoke', null, 'Slowking'),
    ('Snubbull', null, 'grannbull'),
    ('Spinarak', null, 'Ariados'),
    ('Stantler', null, null),
    ('Sudowoodo', null, null),
    ('Sunkern', null, 'Sunflora'),
    ('Swinub', null, 'Piloswine'),
    ('Totodile', null, 'Croconaw'),
    ('Wooper', null, 'Quagsire');
    

create table PokeSet(
setNum int,
setName varchar(255),
yearReleased int,
setSize int,
primary key(setNum));

insert into PokeSet(setNum, setName, yearReleased, setSize) values
	(1, 'Baseset', 1996, 102),
    (8, 'Neo Genesis', 2000, 111);

create table Rarity(
rName varchar(255),
primary key(rName));

insert into Rarity(rName) values
	('Common'),
    ('Uncommon'),
    ('Rare');

create table setRarity(
SRAK int,
setNum int,
rName varchar(255),
canBeHolo boolean,
primary key(SRAK),
foreign key(setNum) references pokeSet(setNum),
foreign key(rName) references Rarity(rName));

insert into setRarity(SRAK, setNum, rName, canBeHolo) values
	(1, 1, 'Common', 0),
    (2, 1, 'Uncommon', 0),
    (3, 1, 'Rare', 1),
    (4, 8, 'Common', 0),
    (5, 8, 'Uncommon', 0),
    (6, 8, 'Rare', 1);

create table Card(
CardNum int,
SRAK int,
pName varchar(255),
TAK int not null,
HP int,
retreatCost int,
primary key(CardNum, SRAK),
foreign key(SRAK) references setRarity(SRAK),
foreign key(pName) references Pokemon(pName),
foreign key(TAK) references TypeGen(TAK));

#select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, card.retreatCost, setrarity.rName
#from card, setrarity, typegen
#where card.TAK in (select TAK from typegen where typeName = 'Colorless') and
#card.SRAK = setrarity.SRAK and
#card.TAK = typegen.TAK;

#select card.pName, setrarity.setNum, card.CardNum, typegen.TypeName, card.HP, card.retreatCost, setrarity.rName
#from card, setrarity, typegen
#where card.pName like 'char%' and 
#card.SRAK = setrarity.SRAK and
#card.TAK = typegen.TAK;

#insert into card(CardNum, SRAK, pName, TAK, HP, RetreatCost) values
#	(70, 1, 'Lugia', 1, 60, 0);
    
#delete from card
#where SRAK in(select SRAK from setrarity where setNum = 1) and cardNum = 70;