import sqlite3

#Arist Database:
"""


CREATE TABLE IF NOT EXISTS Artist_DB (
    `Artist_Name` VARCHAR(16) CHARACTER SET utf8,
    `Genre` VARCHAR(16) CHARACTER SET utf8,
    `Popularity` INT,
    `Foreign_Key` VARCHAR(21) CHARACTER SET utf8
);
INSERT INTO Artist_DB VALUES
    ('Ali Gatie','canadian hip hop',89,'It''s You'),
    ('Anuel AA','reggaeton flow',92,'China'),
    ('Ariana Grande','dance pop',89,'7 rings'),
    ('Bad Bunny','reggaeton',93,'Callaita'),
    ('Billie Eilish','electropop',89,'bad guy'),
    ('Chris Brown','dance pop',82,'No Guidance'),
    ('Daddy Yankee','latin',91,'Con Calma'),
    ('DJ Snake','dance pop',86,'Loco Contigo'),
    ('Drake','canadian hip hop',92,'Money In The Grave '),
    ('Ed Sheeran','pop',82,'Cross Me'),
    ('J Balvin','latin',89,'QUE PRETENDES'),
    ('Jhay Cortez','reggaeton flow',83,'No Me Conoce - Remix'),
    ('Jonas Brothers','boy band',80,'Sucker'),
    ('Katy Perry','dance pop',89,'Never Really Over'),
    ('Khalid','pop',84,'Talk'),
    ('Kygo','edm',88,'Higher Love'),
    ('Lady Gaga','dance pop',87,'Shallow'),
    ('Lauv','dance pop',78,'fuck, i''m lonely'),
    ('Lewis Capaldi','pop',88,'Someone You Loved'),
    ('Lil Nas X','country rap',91,'Panini'),
    ('Lil Tecca','trap music',92,'Ransom'),
    ('Lizzo','escape room',91,'Truth Hurts'),
    ('Lunay','latin',91,'Soltera'),
    ('Marshmello','brostep',88,'Happier'),
    ('Martin Garrix','big room',89,'Summer Days'),
    ('MEDUZA','pop house',91,'Piece Of Your Heart'),
    ('Nicky Jam','latin',88,'Te Robaré'),
    ('Post Malone','dfw rap',91,'Sunflower'),
    ('ROSALÍA','r&b en espanol',88,'Con Altura'),
    ('Sam Smith','pop',90,'How Do You Sleep'),
    ('Sech','panamanian pop',91,'Otro Trago'),
    ('Shawn Mendes','canadian pop',70,'If I Can''t Have You'),
    ('Taylor Swift','dance pop',90,'You Need To Calm Down'),
    ('The Chainsmokers','edm',88,'Call You Mine'),
    ('Tones and I','australian pop',83,'Dance Monkey'),
    ('Young Thug','atl hip hop',89,'The London'),
    ('Y2K','canadian hip hop',88,'Lalala');
"""
#Song Database:
"""CREATE TABLE IF NOT EXISTS Song_DB (
    `Rank` INT,
    `Track_Name` VARCHAR(21) CHARACTER SET utf8,
    `Length_sec` INT,
    `Foreign_Key` VARCHAR(16) CHARACTER SET utf8
);
INSERT INTO Song_DB VALUES
    (1,'China',302,'Anuel AA'),
    (2,'boyfriend',186,'Ariana Grande'),
    (3,'Ransom',131,'Lil Tecca'),
    (4,'How Do You Sleep',202,'Sam Smith'),
    (5,'Callaita',251,'Bad Bunny'),
    (6,'Loco Contigo',185,'DJ Snake'),
    (7,'Someone You Loved',182,'Lewis Capaldi'),
    (8,'Money In The Grave',205,'Drake'),
    (9,'No Guidance',261,'Chris Brown'),
    (10,'Sunflower',158,'Post Malone'),
    (11,'Lalala',161,'Y2K'),
    (12,'Truth Hurts',173,'Lizzo'),
    (13,'Piece Of Your Heart',153,'MEDUZA'),
    (14,'Panini',115,'Lil Nas X'),
    (15,'No Me Conoce',309,'Jhay Cortez'),
    (16,'Soltera',266,'Lunay'),
    (17,'bad guy',195,'Billie Eilish'),
    (18,'If I Can''t Have You',191,'Shawn Mendes'),
    (19,'Dance Monkey',210,'Tones and I'),
    (20,'It''s You',213,'Ali Gatie'),
    (21,'Con Calma',193,'Daddy Yankee'),
    (22,'QUE PRETENDES',222,'J Balvin'),
    (23,'The London',200,'Young Thug'),
    (24,'Never Really Over',224,'Katy Perry'),
    (25,'Summer Days',164,'Martin Garrix'),
    (26,'Otro Trago',226,'Sech'),
    (27,'Sucker',181,'Jonas Brothers'),
    (28,'fuck, i''m lonely',199,'Lauv'),
    (29,'Higher Love',228,'Kygo'),
    (30,'You Need To Calm Down',171,'Taylor Swift'),
    (31,'Shallow',216,'Lady Gaga'),
    (32,'Talk',198,'Khalid'),
    (33,'Con Altura',162,'ROSALÍA'),
    (34,'Te Robaré',202,'Nicky Jam'),
    (35,'Happier',214,'Marshmello'),
    (36,'Call You Mine',218,'The Chainsmokers'),
    (37,'Cross Me',206,'Ed Sheeran');
    """


# if the user wants a list of all songs
def allSongs():

    return

# if the user wants a list of all artists
def allArtists():

    return

# if the user requests an artist and wants their song
def artistAndSong(artist):

    return

# if the user requests a song and wants the artist
def songAndArtist(song):

    return

# if a user requests a song and wants the popularity
def songAndRank(song):

    return

# if a user requests a song and wants its genre
def songAndGenre(song):

    return

# if a user requests a genre and wants its songs
def genreAndSong(genre):

    return

#if a user requests a song and its length
def songAndLength(song):

    return

# if a user wants songs in a range of popularity
def songBetweenRank(lowval,highval):

    return


#if a user wants songs in a range of length length
def songBetweenLength(lowval,highval):

    return

def artistandRank(artist):

    return

def artistBetweenRank(lowval,highval):

    return