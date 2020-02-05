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

    Query = Queryfunctions

    while True:
        # Get command from user
        request = input("")

        # Conditionals corresponding to words entered
        # To view help options
        if request == "help":
            help()

        # to quit program
        if request == "quit":
            quit()

        # To view the top songs in the database
        if request == "show all songs":
            Query.allSongs() #TODO: This is ex of call not call for this request

        # To view the top artists in the database
        if request == "show all artists":
            Query.allArtists()

        # To view a range of top songs
        if "songs range" in request: #TODO: TEST THIS
            values = [int(s) for s in s.split() if s.isdigit()]
            lowval = values[0]
            highval = values[1]
            Query.songBetweenRank(lowval, highval)

        # To view a range of top artists
        if "artists range" in request: #TODO: TEST THIS
            values = [int(s) for s in s.split() if s.isdigit()]
            lowval = values[0]
            highval = values[1]
            Query.songBetweenRank(lowval, highval)
            Query.artistBetweenRank(lowval, highval)

        # To view all songs of a specific genre
        if "songs genre" in request: #TODO: Test this
            genre = re.findall(r'\"(.+?)\"', request)
            Query.genreAndSong(genre)

        # To view all songs from a particular artist
        if "artist songs" in request: #TODO: Test this
            artist = re.findall(r'\"(.+?)\"', request)
            Query.artistAndSong(artist)

        # To view songs within a particular length
        if "songs between length" in request: #TODO: TEST THIS
            values = [int(s) for s in s.split() if s.isdigit()]
            lowval = values[0]
            highval = values[1]
            Query.songBetweenRank(lowval, highval)
            Query.songBetweenLength(lowval, highval)

        # To view the popularity rank of a particular artist
        if "artist popularity" in request: #TODO: Test this
            artist = re.findall(r'\"(.+?)\"', request)
            Query.artistandRank(artist)

        # To view the artist of a song
        if "song artist" in request: #TODO: Test this
            song = re.findall(r'\"(.+?)\"', request)
            Query.songAndArtist(song)

        # To view the genre of a particular song
        if "song genre" in request: #TODO: Retrieve song
            song = re.findall(r'\"(.+?)\"', request)
            Query.songAndGenre(song)

        # To view the length of a particular song
        if "song length" in request: #TODO: Retrieve song
            song = re.findall(r'\"(.+?)\"', request)
            Query.songAndLength(song)

        # To view the rank of a particular song
        if "song popularity" in request: #TODO: Retrieve song
            song = re.findall(r'\"(.+?)\"', request)
            Query.songAndRank(song)

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
    print("To view the top songs in the database, type 'show all songs'")
    print("To view the top artists in the database, type 'show all artists'")
    print("To view a range of top songs, type 'songs range LOWVAL to HIGHVAL'")
    print("To view a range of top artists, type 'artists range LOWVAL to HIGHVAL'")
    print("To view all songs of a specific genre, type 'songs genre \"SAMPLEGENRE\"'")
    print("To view all songs from a particular artist, type 'artist songs \"SAMPLEARTIST\"'")
    print("To view songs within a particular length, type 'songs between length LOWVAL to HIGHVAL'") #TODO: convert to seconds/minutes? (how does user enter this)
    print("To view the popularity rank of a particular artist, type 'artist popularity \"ARTIST NAME\"'")
    print("To view the genre of a particular song, type 'song length \"SONG TITLE\"'")
    print("To view the rank of a particular song, type 'song popularity \"SONG TITLE\"'")
    print("To view the length of a particular length, type 'song length \"SONG TITLE\"'")
    print("To view the artist of a particular song, type 'song artist \"SONG TITLE\"'")
    print("To quit to program, type 'quit'")


def quit():
    exit(0)


main()
