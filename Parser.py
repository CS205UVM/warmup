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


# keep program running and reentering the CLI until user types quit
def main():
    print("Welcome to Song/Artist Parser")  # Greeting can be changed later
    print("------------------------------")
    print("Enter commands to find data")
    print("Hint: type help to get a list of commands")

    Query = Queryfunctions
    loadData()

    while True:
        # Get command from user
        request = input(">")

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

        # To view a range of top songs
        elif "songs range " in request:
            # Split search into a list
            request_array = request.split()
            # Initialize - prevent crashing if invalid input
            lowval = 0
            highval = 0
            valid = False  # confirms if input was valid

            # Note: search needs to be typed as 'songs range "LOWVAL" to "HIGHVAL"'
            # so when search is split, size of list needs to be 5, otherwise it is an invalid search
            if len(request_array) != 5 or request_array[0] != "songs" or request_array[1] != "range" or request_array[3] != "to":
                valid = False

            # Otherwise extract low and high values from range
            else:
                # extract index 2 of array (would contain low val)
                lowval = request_array[2]
                # extract index 4 of array (should contain high value)
                highval = request_array[4]

                # get lowval as integer
                lowval_str = ""
                for i in range(len(lowval) - 2):
                    lowval_str += lowval[i+1]
                lowval = lowval_str

                # Get highval as integer
                highval_str = ""
                for i in range(len(highval) - 2):
                    highval_str += highval[i + 1]
                highval = highval_str

                # Check to see both are integers
                if lowval.isdigit() and highval.isdigit():
                    valid = True

            if valid:
                # Test to ensure lower value is smaller than the highervalue
                if highval < lowval:
                    print("The range you entered is invalid.")
                else:
                    pass
                    #Query.song_between_rank(c,lowval, highval) TODO: causes program to crash

            else:
                print("Your search for a range of songs could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


        # To view all songs of a specific genre
        elif "songs genre" in request:
            # Split input up
            request_array = request.split()

            # Variable for valid search
            valid = False

            # Check that array begins with "songs" and "genre" for this search
            if request_array[0] == "songs" and request_array[1] == "genre":
                # Concatenate rest of array into one string - represents genre searched
                genre = ""
                for i in range(len(request_array) - 2):
                    genre += request_array[i + 2]
                    genre += " "
                # Remove trailing space from string
                genre = genre[:-1]

                # Check input is in quotes
                if genre[0] == "\"" and genre[-1] == "\"":
                    # get genre searched
                    genre_str = ""

                    for char in range(len(genre) - 2):
                        # extract genre from string
                        genre_str += genre[char + 1]

                    valid = True

            if valid:
                # Query.songs_by_genre(c,genre_str)
                pass

            else:
                print("Your search for songs of a particular genre could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


        # To view all songs from a particular artist
        elif "artist songs" in request:
            # Split input up
            request_array = request.split()

            # Variable for valid search
            valid = False

            # Check that array begins with "artist" and "songs" for this search
            if request_array[0] == "artist" and request_array[1] == "songs":
                # Concatenate rest of array into one string - represents artist searched
                artist = ""
                for i in range(len(request_array) - 2):
                    artist += request_array[i + 2]
                    artist += " "
                # Remove trailing space from string
                artist = artist[:-1]

                # Check input is in quotes
                if artist[0] == "\"" and artist[-1] == "\"":
                    # get artist searched
                    artist_str = ""

                    for char in range(len(artist) - 2):
                        # extract artist from string
                        artist_str += artist[char + 1]

                    valid = True

            if valid:
                # Query.artist_and_song(c,artist_str)
                pass

            else:
                print("Your search for songs from an artist could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


        # To view songs within a particular length
        elif "songs between length" in request:
            # Split search into a list
            request_array = request.split()
            # Initialize - prevent crashing if invalid input
            lowval = 0
            highval = 0
            valid = False  # confirms if input was valid

            # Note: search needs to be typed as 'songs between length "LOWVAL" to "HIGHVAL"'
            # test all search terms
            if len(request_array) != 6 or request_array[0] != "songs" or request_array[1] != "between" or request_array[
                2] != "length" or request_array[4] != "to":
                valid = False

            # Otherwise extract low and high values from range
            else:
                # extract index 3 of array (would contain low val)
                lowval = request_array[3]
                # extract index 5 of array (should contain high value)
                highval = request_array[5]

                # get lowval as integer
                lowval_str = ""
                for i in range(len(lowval) - 2):
                    lowval_str += lowval[i + 1]
                lowval = lowval_str

                # Get highval as integer
                highval_str = ""
                for i in range(len(highval) - 2):
                    highval_str += highval[i + 1]
                highval = highval_str

                # Check to see both are integers
                if lowval.isdigit() and highval.isdigit():
                    valid = True

            if valid:
                # Test to ensure lower value is smaller than the higher value
                if highval < lowval:
                    print("The range you entered is invalid.")
                else:
                    pass
                    # Query.song_between_length(c,lowval, highval) TODO: causes program to crash

            else:
                print("Your search for songs within a certain length could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")



        # To view the artist of a song
        elif "song artist" in request: #TODO: Test this
            # Split input up
            request_array = request.split()

            # Variable for valid search
            valid = False

            # Check that array begins with "song" and "artist" for this search
            if request_array[0] == "song" and request_array[1] == "artist":
                # Concatenate rest of array into one string - represents genre searched
                song = ""
                for i in range(len(request_array) - 2):
                    song += request_array[i + 2]
                    song += " "
                # Remove trailing space from string
                    song = song[:-1]

                # Check input is in quotes
                if song[0] == "\"" and song[-1] == "\"":
                    # get genre searched
                    song_str = ""

                    for char in range(len(song) - 2):
                        # extract genre from string
                        song_str += song[char + 1]

                    valid = True

            if valid:
                # Query.song_and_artist(c,song_str)
                pass

            else:
                print("Your search for the artist of a song could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


        # To view the genre of a particular song
        elif "song genre" in request:
            # Split input up
            request_array = request.split()

            # Variable for valid search
            valid = False

            # Check that array begins with "genre" and "song" for this search
            if request_array[0] == "genre" and request_array[1] == "song":
                # Concatenate rest of array into one string - represents song searched
                song = ""
                for i in range(len(request_array) - 2):
                    song += request_array[i + 2]
                    song += " "
                # Remove trailing space from string
                song = song[:-1]

                # Check input is in quotes
                if song[0] == "\"" and song[-1] == "\"":
                    # get song searched
                    song_str = ""

                    for char in range(len(song) - 2):
                        # extract song from string
                        song_str += song[char + 1]

                    valid = True

            if valid:
                # Query.song_and_genre(c,song_str)
                pass

            else:
                print("Your search for the genre of a song could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


        # To view the length of a particular song
        elif "song length" in request:
            # Split input up
            request_array = request.split()

            # Variable for valid search
            valid = False

            # Check that array begins with "song" and "length" for this search
            if request_array[0] == "song" and request_array[1] == "length":
                # Concatenate rest of array into one string - represents song searched
                song = ""
                for i in range(len(request_array) - 2):
                    song += request_array[i + 2]
                    song += " "
                # Remove trailing space from string
                song = song[:-1]

                # Check input is in quotes
                if song[0] == "\"" and song[-1] == "\"":
                    # get song searched
                    song_str = ""

                    for char in range(len(song) - 2):
                        # extract song from string
                        song_str += song[char + 1]

                    valid = True

            if valid:
                # Query.song_and_length(c,song_str)
                pass

            else:
                print("Your search for the genre of a song could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


        # To view the rank of a particular song
        elif "song rank" in request:
            # Split input up
            request_array = request.split()

            # Variable for valid search
            valid = False

            # Check that array begins with "song" and "rank" for this search
            if request_array[0] == "song" and request_array[1] == "rank":
                # Concatenate rest of array into one string - represents song searched
                song = ""
                for i in range(len(request_array) - 2):
                    song += request_array[i + 2]
                    song += " "
                # Remove trailing space from string
                song = song[:-1]

                # Check input is in quotes
                if song[0] == "\"" and song[-1] == "\"":
                    # get song searched
                    song_str = ""

                    for char in range(len(song) - 2):
                        # extract song from string
                        song_str += song[char + 1]

                    valid = True

            if valid:
                # Query.song_and_popularity(c,song_str)
                pass

            else:
                print("Your search for the genre of a song could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


        # To view artists between popularity
        elif "artists between popularity" in request:
            # Split search into a list
            request_array = request.split()
            # Initialize - prevent crashing if invalid input
            lowval = 0
            highval = 0
            valid = False  # confirms if input was valid

            # Note: search needs to be typed as 'songs between length "LOWVAL" to "HIGHVAL"'
            # test all search terms
            if len(request_array) != 6 or request_array[0] != "artists" or request_array[1] != "between" or request_array[
                2] != "popularity" or request_array[4] != "to":
                valid = False

            # Otherwise extract low and high values from range
            else:
                # extract index 3 of array (would contain low val)
                lowval = request_array[3]
                # extract index 5 of array (should contain high value)
                highval = request_array[5]

                # get lowval as integer
                lowval_str = ""
                for i in range(len(lowval) - 2):
                    lowval_str += lowval[i + 1]
                lowval = lowval_str

                # Get highval as integer
                highval_str = ""
                for i in range(len(highval) - 2):
                    highval_str += highval[i + 1]
                highval = highval_str

                # Check to see both are integers
                if lowval.isdigit() and highval.isdigit():
                    valid = True

            if valid:
                # Test to ensure lower value is smaller than the higher value
                if highval < lowval:
                    print("The range you entered is invalid.")
                else:
                    pass
                    # Query.song_between_popularity(c, lowval, highval) TODO: causes program to crash

            else:
                print("Your search for songs within a certain length could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


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
    print("-To view the genre of a particular song, type 'genre song \"SONG TITLE\"'")
    print("-To view the rank of a particular song, type 'song rank \"SONG TITLE\"'")
    print("-To view the length of a particular length, type 'song length \"SONG TITLE\"'")
    print("-To view the artist of a particular song, type 'song artist \"SONG TITLE\"'")
    print("-To view all artists between a certain popularity, type 'artists between popularity \"LOWVAL\" to \"HIGHVAL\"'")
    print("-To quit to program, type 'quit'")


def quit():
    exit(0)

main()