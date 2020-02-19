import Queryfunctions
import sqlite3, csv, os
from sqlite3 import Error


# keep program running and reentering the CLI until user types quit
def main():
    print("Welcome to Song/Artist Parser")  # Greeting can be changed later
    print("------------------------------")
    print("Enter commands to find data")
    print("Hint: type help to get a list of commands")

    Query = Queryfunctions
    load()
    c = False

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
            if c:
                Query.all_songs(c)
            else:
                conn = create_connection("warmup.db")
                c = conn.cursor()
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
            if len(request_array) != 5 or request_array[0] != "songs" or request_array[1] != "range" or request_array[
                3] != "to":
                valid = False

            # Otherwise extract low and high values from range
            else:
                # extract index 2 of array (would contain low val)
                lowval = request_array[2]
                # extract index 4 of array (should contain high value)
                highval = request_array[4]

                # Make sure values entered in quotations
                if lowval[0] == "\"" and lowval[-1] == "\"" and highval[0] == "\"" and highval[-1] == "\"":
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
                highval = int(highval)
                lowval = int(lowval)
                # Test to ensure lower value is smaller than the highervalue
                if highval < lowval:
                    print("The range you entered is invalid.")
                else:
                    pass
                    if c:
                        Query.song_between_rank(c, lowval, highval)
                    else:
                        conn = create_connection("warmup.db")
                        c = conn.cursor()
                        Query.song_between_rank(c, lowval, highval)

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
                if (c):
                     Query.songs_by_genre(c, genre_str)
                else:
                    conn = create_connection("warmup.db")
                    c = conn.cursor()
                    Query.songs_by_genre(c, genre_str)
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
                if c:
                    Query.artist_and_song(c, artist_str)
                else:
                    conn = create_connection("warmup.db")
                    c = conn.cursor()
                    Query.artist_and_song(c, artist_str)
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

                # Make sure values entered in quotations
                if lowval[0] == "\"" and lowval[-1] == "\"" and highval[0] == "\"" and highval[-1] == "\"":
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
                highval = int(highval)
                lowval = int(lowval)
                # Test to ensure lower value is smaller than the higher value
                if highval < lowval:
                    print("The range you entered is invalid.")
                else:
                    pass
                    if c:
                        Query.song_between_length(c, lowval, highval)
                    else:
                        conn = create_connection("warmup.db")
                        c = conn.cursor()
                        Query.song_between_length(c, lowval, highval)


            else:
                print("Your search for songs within a certain length could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


        # To view the artist of a song
        elif "song artist" in request:
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
                if c:
                    Query.song_and_artist(c, song_str)
                else:
                    conn = create_connection("warmup.db")
                    c = conn.cursor()
                    Query.song_and_artist(c, song_str)
                pass

            else:
                print("Your search for the artist of a song could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


        # To view the genre of a particular song
        elif "genre song " in request:
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
                if c:
                    Query.song_and_genre(c, song_str)
                else:
                    conn = create_connection("warmup.db")
                    c = conn.cursor()
                    Query.song_and_genre(c, song_str)
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
                if c:
                  Query.song_and_length(c, song_str)
                else:
                    conn = create_connection("warmup.db")
                    c = conn.cursor()
                    Query.song_and_length(c, song_str)
                pass

            else:
                print("Your search for the genre of a song could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


        # To view the rank of a particular song
        elif "song popularity" in request:
            # Split input up
            request_array = request.split()

            # Variable for valid search
            valid = False

            # Check that array begins with "song" and "rank" for this search
            if request_array[0] == "song" and request_array[1] == "popularity":
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
                if c:
                    Query.song_and_popularity(c, song_str)
                else:
                    conn = create_connection("warmup.db")
                    c = conn.cursor()
                    Query.song_and_popularity(c, song_str)
                pass

            else:
                print("Your search for the genre of a song could not be understood. ")
                print("Ensure you are entering data as directed in the help menu. ")


        # To view songs between popularity
        elif "songs between popularity" in request:
            # Split search into a list
            request_array = request.split()
            # Initialize - prevent crashing if invalid input
            lowval = 0
            highval = 0
            valid = False  # confirms if input was valid

            # Note: search needs to be typed as 'songs between length "LOWVAL" to "HIGHVAL"'
            # test all search terms
            if len(request_array) != 6 or request_array[0] != "songs" or request_array[1] != "between" or request_array[
                2] != "popularity" or request_array[4] != "to":
                valid = False

            # Otherwise extract low and high values from range
            else:
                # extract index 3 of array (would contain low val)
                lowval = request_array[3]
                # extract index 5 of array (should contain high value)
                highval = request_array[5]

                # Make sure values entered in quotations
                if lowval[0] == "\"" and lowval[-1] == "\"" and highval[0] == "\"" and highval[-1] == "\"":
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
                highval = int(highval)
                lowval = int(lowval)

                # Test to ensure lower value is smaller than the higher value
                if highval < lowval:
                    print("The range you entered is invalid.")
                else:
                    pass
                    if c:
                        Query.song_between_popularity(c, lowval, highval)
                    else:
                        conn = create_connection("warmup.db")
                        c = conn.cursor()
                        Query.song_between_popularity(c, lowval, highval)

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


def load():
    # referenced https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python

    if os.path.exists("warmup.db"):
        os.remove("warmup.db")

    con = sqlite3.connect("warmup.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE artists (artist_name, genre, popularity, song_name);")  # use your column names here
    with open('Artist-Table.csv', 'rt', encoding="UTF-8") as fin:  # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i['artist_name'], i['genre'], int(i['popularity']), i['song_name']) for i in dr]
    cur.executemany("INSERT INTO artists (artist_name, genre, popularity, song_name) VALUES (?, ?, ?, ?);", to_db)

    cur.execute("CREATE TABLE songs (rank, song_name, length_sec, artist_name);")  # use your column names here
    with open('Song-Table.csv', 'rt', encoding="UTF-8") as fin:  # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(int(i['rank']), i['track_name'], int(i['length']), i['artist_name']) for i in dr]
    cur.executemany("INSERT INTO songs (rank, song_name, length_sec, artist_name) VALUES (?, ?, ?, ?);", to_db)
    con.commit()
    con.close()


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


"""
one of the commands should be help, which will print out help text about the commands
"""


def help():
    print(
        "Help Section - Note that you must include quotations around input where directed. ")  # Can change message later
    print("-To view all of the songs in the database, type 'show all songs'")
    print("-To view a range of top songs, type 'songs range \"LOWVAL\" to \"HIGHVAL\"'")
    print("-To view all songs of a specific genre, type 'songs genre \"SAMPLEGENRE\"'")
    print("-To view all songs from a particular artist, type 'artist songs \"SAMPLEARTIST\"'")
    print("-To view songs within a particular length, type 'songs between length \"LOWVAL\" to \"HIGHVAL\"'")
    print("-To view the genre of a particular song, type 'genre song \"SONG TITLE\"'")
    print("-To view the popularity of a particular song, type 'song popularity \"SONG TITLE\"'")
    print("-To view the length of a particular length, type 'song length \"SONG TITLE\"'")
    print("-To view the artist of a particular song, type 'song artist \"SONG TITLE\"'")
    print("-To view songs between a certain popularity, type 'songs between popularity \"LOWVAL\" to \"HIGHVAL\"'")
    print("-To quit to program, type 'quit'")


def quit():
    exit(0)


main()
