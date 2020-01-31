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
        if request == "":
            Query.allArtists()
            pass  # need QueryFunctions method

        # To view the top artists in the database
        if request == "":
            pass  # need QueryFunctions method

        # To view a range of top songs
        if request == "":
            pass  # need QueryFunctions method

        # To view a range of top artists
        if request == "":
            pass  # need QueryFunctions method

        # To view all songs of a specific genre
        if request == "":
            pass  # need QueryFunctions method

        # To view all songs from a particular artist
        if request == "":
            pass  # need QueryFunctions method

        # To view songs within a particular length
        if request == "":
            pass  # need QueryFunctions method

        # To view the top songs in the database
        if request == "":
            pass  # need QueryFunctions method

        # To view the popularity rank of a particular artist
        if request == "":
            pass  # need QueryFunctions method
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
    print("To view a range of top songs, type 'songs range \"LOWVAL\" to \"HIGHVAL\"'")
    print("To view a range of top artists, type 'artists range \"LOWVAL\" to \"HIGHVAL\"'")
    print("To view all songs of a specific genre, type 'songs genre \"SAMPLEGENRE\"'")
    print("To view all songs from a particular artist, type 'artist songs \"SAMPLEARTIST\"'")
    print("To view songs within a particular length, type 'songs length \"LOWVAL\" to \"HIGHVAL\"'") #TODO: convert to seconds/minutes? (how does user enter this)
    print("To view the popularity rank of a particular artist, type 'artist popularity \"ARTIST NAME\"'")
    #TODO: More commands...?


def quit():
    exit(0)


main()
