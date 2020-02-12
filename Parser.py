"""
IDEA LIST FOR POSSIBLE COMMANDS
load data
help
quit
select all songs
select all artists
select songs and their genres
select songs and their track lengths
individual artist and their song
song and its popularity
select songs where rank is < some value
select songs where length is < some value
select songs where length is > some value
select songs where popularity is < some value
select songs where popularity is > some value
"""
import Queryfunctions
import re
import sqlite3
from sqlite3 import Error
# keep program running and reentering the CLI, in the future program will run
# until quit command is issued.
def main():

    print("Welcome to Song/Artist Parser")  # Greeting can be changed later
    print("=============================")
    print("Enter commands to find data")
    print("Hint: type help to get a list of commands")

    Query = Queryfunctions
    loadData()

    while True:
        # Get command from user
        print("==>", end =" ")
        request = input("")

        # Conditionals corresponding to words entered
        # To view help options
        if request == "help":
            help()

        # to quit program
        elif request == "quit":
            quit()

        # To view the top songs in the database
        elif request == "show all songs":
            Query.all_songs(c)

        ## To view songs between popularity                                     Not sure what this was Songs don't have popularity rank
        ##elif request == "songs between popularity": #TODO: TEST THIS
        ##    values = [int(s) for s in s.split() if s.isdigit()]
        ##    lowval = values[0]
        ##    highval = values[1]
        ##    Query.song_between_popularity(c,lowval,highval)

        # To view a range of top songs
        elif "songs range " in request: #TODO: TEST THIS
            lowval = 0
            highval = 0
            if request[12] != "\"":
                print("Integers for songs range not recognized, include \"\" around your integers. ")
                pass
            else:                                   #0 1 2 3 4 5 6 7 8 910111213141516171819202122232425262728
                # extract integers - lowval first   #s o n g s   r a n g e   " 1 0 "   t o   " 1 0 "
                if request[13].isdigit():
                    lowval = str(request[13])
                    if request[14].isdigit():
                        lowval += str(request[14])
                        lowval = int(lowval)
                    if request[14] == "\"":
                        lowval = int(lowval)
                    if request [15].isdigit():
                        print("Database does not have that many songs.")
                # extract high val, note either index 14 or 15 need to be quotes or invalid search
                if request[14] == "\"" or request[15] == "\"":
                    if request[14] == "\"":
                        # if lowval is single digit, index 19 is quote for high digit
                        if request[19] == "\"":
                            if request[20].isdigit():
                                highval = str(request[20])
                                if request[21] == "\"":
                                    highval = int(highval)  # convert to int (note high val is single digit)

                                elif request[21].isdigit():
                                    highval += str(request[21])
                        # if lowval is double digit request[20] is "
                        if request[20] == "\"":
                            if request[21].isdigit():
                                highval = str(request[21])
                                # note that if lowval is double digit number, highval needs to be double digit as well
                                if request[22].isdigit():
                                    highval += str(request[22]) #TODO left here

            print(lowval)
            print(highval)



            #values = [int(s) for s in s.split() if s.isdigit()]
            #lowval = values[0]
            #highval = values[1]
            #Query.song_between_rank(c,lowval, highval)

        # To view all songs of a specific genre
        elif "songs genre" in request: #TODO: Test this
            genre = re.findall(r'\"(.+?)\"', request)
            Query.songs_by_genre(c,genre)

        # To view all songs from a particular artist
        elif "artist songs" in request: #TODO: Test this
            artist = re.findall(r'\"(.+?)\"', request)
            Query.artist_and_song(c,artist)

        # To view songs within a particular length
        elif "songs between length" in request: #TODO: TEST THIS
            values = [int(s) for s in s.split() if s.isdigit()]
            lowval = values[0]
            highval = values[1]
            Query.song_between_length(c,lowval, highval)

        # To view the artist of a song
        elif "song artist" in request: #TODO: Test this
            song = re.findall(r'\"(.+?)\"', request)
            Query.song_and_artist(c,song)

        # To view the genre of a particular song
        elif "song genre" in request: #TODO: Retrieve song
            song = re.findall(r'\"(.+?)\"', request)
            Query.song_and_genre(c,song)

        # To view the length of a particular song
        elif "song length" in request: #TODO: Retrieve song
            song = re.findall(r'\"(.+?)\"', request)
            Query.song_and_length(c,song)

        # To view the rank of a particular song
        elif "song popularity" in request: #TODO: Retrieve song
            song = re.findall(r'\"(.+?)\"', request)
            Query.song_and_popularity(c,song)

        # If no command matched -> display error message (error handling) -gives user a message if their command wasn't
        # recognized
        else:
            print("Your command was not recognized, perhaps you misspelled a word. ")
            print("Try typing \"help\" to see exact search commands. ")


"""
one of the commands should be load data, which will create the database 
and the schema and read data from your csv ﬁles into the tables; if the 
database already exists, then the command will overwrite the existing database
"""
def loadData():
    database = "warmup.db"

    sql_create_artist_table = """ CREATE TABLE Artist_DB (
                                        `Artist_Name` VARCHAR(16),
                                        `Genre` VARCHAR(16),
                                        `Popularity` INT,
                                        `Foreign_Key` VARCHAR(21)
                                        ); """

    sql_create_song_table = """CREATE TABLE Song_DB (
                                    `Rank` INT,
                                    `Track_Name` VARCHAR(21),
                                    `Length_sec` INT,
                                    `Foreign_Key` VARCHAR(16)
                                    );"""

    sqlite_insert_song_query = """
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

    sqlite_insert_artist_query = """
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
        ('Jhay Cortez','reggaeton flow',83,'No Me Conoce'),
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
        ('Y2K','canadian hip hop',88,'Lalala');"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create artist table
        create_table(conn, sql_create_artist_table, sqlite_insert_artist_query)

        # create song table
        create_table(conn, sql_create_song_table, sqlite_insert_song_query)

    else:
        print("Error! cannot create the database connection.")

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql, insert_table_data):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        #c.execute(create_table_sql)
        c.execute(insert_table_data)
        conn.commit()


    except Error as e:
        print(e)


"""
one of the commands should be help, which will print out help text about the commands
"""
def help():
    print("Help Section - Note that you must include quotations around input where directed. ")  # Can change message later
    print("-To view the top songs in the database, type 'show all songs'")
    print("-To view a range of top songs, type 'songs range \"LOWVAL\" to \"HIGHVAL\"'")
    print("-To view all songs of a specific genre, type 'songs genre \"SAMPLEGENRE\"'")
    print("-To view all songs from a particular artist, type 'artist songs \"SAMPLEARTIST\"'")
    print("-To view songs within a particular length, type 'songs between length \"LOWVAL\" to \"HIGHVAL\"'")
    print("-To view the genre of a particular song, type 'song length \"SONG TITLE\"'")
    print("-To view the rank of a particular song, type 'song popularity \"SONG TITLE\"'")
    print("-To view the length of a particular length, type 'song length \"SONG TITLE\"'")
    print("-To view the artist of a particular song, type 'song artist \"SONG TITLE\"'")
    print("-To view all songs between a certain popularity, type 'songs between popularity \"LOWVAL\" to \"HIGHVAL\"'")
    print("-To quit to program, type 'quit'")


def quit():
    exit(0)

main()