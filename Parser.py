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

        # To view songs between popularity
        elif request == "songs between popularity": #TODO: TEST THIS
            values = [int(s) for s in s.split() if s.isdigit()]
            lowval = values[0]
            highval = values[1]
            Query.song_between_popularity(c,lowval,highval)

        # To view a range of top songs
        elif "songs range" in request: #TODO: TEST THIS
            values = [int(s) for s in s.split() if s.isdigit()]
            lowval = values[0]
            highval = values[1]
            Query.song_between_rank(c,lowval, highval)

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
    pass

"""
one of the commands should be help, which will print out help text about the commands
"""
def help():
    print("Help Section - Note that you must include quotations around input where directed. ")  # Can change message later
    print("-To view the top songs in the database, type 'show all songs'")
    print("-To view a range of top songs, type 'songs range LOWVAL to HIGHVAL'")
    print("-To view all songs of a specific genre, type 'songs genre \"SAMPLEGENRE\"'")
    print("-To view all songs from a particular artist, type 'artist songs \"SAMPLEARTIST\"'")
    print("-To view songs within a particular length, type 'songs between length LOWVAL to HIGHVAL'")
    print("-To view the genre of a particular song, type 'song length \"SONG TITLE\"'")
    print("-To view the rank of a particular song, type 'song popularity \"SONG TITLE\"'")
    print("-To view the length of a particular length, type 'song length \"SONG TITLE\"'")
    print("-To view the artist of a particular song, type 'song artist \"SONG TITLE\"'")
    print("-To view all songs between a certain popularity, type 'songs between popularity LOWVAL to HIGHVAL'")
    print("-To quit to program, type 'quit'")


def quit():
    exit(0)

main()