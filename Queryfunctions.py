import sqlite3


# The all_songs function displays all of the songs and their information
# Parameter c is the database cursor
def all_songs(c):
    print("Rank\tSong\t\t\t\tLength(s)\t\tGenre\t\t\tPopularity\t\tArtist")
    print("-------------------------------------------------------------------------------------")
    for row in c.execute("SELECT songs.rank, songs.song_name, songs.length_sec, artists.genre, artists.popularity,"
                         "artists.artist_name"
                         " FROM songs JOIN artists ON songs.artist_name = artists.artist_name"):
       print("{:<7d} {:22s} {:<12d} {:17s} {:<13d} {:11s}".format(*row))


# The artist_and_song function displays an artist and all the songs by that artist
# Parameter c is the database cursor
# Parameter artist is the artist being searched
def artist_and_song(c, artist):
    for row in c.execute("SELECT artists.artist_name, songs.song_name FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE artists.artist_name == ?", (artist,)):
        print("{}".format(row[1]))


# This song displays the artist for a user input song
# Parameter c is the database cursor
# Parameter song is the song being searched
def song_and_artist(c, song):
    for row in c.execute("SELECT songs.song_name, artists.artist_name FROM songs JOIN artists "
                          "ON songs.artist_name = artists.artist_name "
                          "WHERE songs.song_name == ?", (song,)):
        print("{}".format(row[1]))


# This function displays the popularity of a user input song
# Parameter c is the cursor to the database
# Parameter song is the input song
def song_and_popularity(c, song):
    for row in c.execute("SELECT songs.song_name, popularity FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE songs.song_name == ?", (song,)):
        print("{}".format(row[1]))


# This function displays the genre of a user input song
# Parameter c is the cursor to the database
# Parameter song is the input song
def song_and_genre(c, song):
    for row in c.execute("SELECT songs.song_name, genre FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE songs.song_name == ?", (song,)):
        print("{}".format(row[1]))


# This function displays a list of songs of a particular genre
# The parameter c is the cursor to the database
# The parameter genre is the genre to be searched
def songs_by_genre(c, genre):
    for row in c.execute("SELECT genre, songs.song_name FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE genre == ?", (genre,)):
        print("{}".format(row[1]))


# This function displays the length of a user input song
# The parameter c is the cursor to the database
# Song is the song to be searched
def song_and_length(c, song):
    for row in c.execute("SELECT songs.song_name, length_sec FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE songs.song_name == ?", (song,)):
        print("{}".format(row[1]))


# This function returns a list of songs between a user input popularity range
# The parameter c is the cursor to the database
# The parameter lowval is the lower bound of popularity
# The parameter highval is the upper bound of popularity
def song_between_popularity(c, lowval, highval):
    for row in c.execute("SELECT songs.song_name, popularity FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE popularity BETWEEN ? AND ?", (lowval, highval)):
        print("Song: {:23s} Popularity: {}".format(*row))

# This function returns a list of songs between a user input rank range
# The parameter c is the cursor to the database
# The parameter lowval is the lower bound of rank
# The parameter highval is the upper bound of rank
def song_between_rank(c, lowval, highval):
    for row in c.execute("SELECT songs.song_name, rank FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE rank BETWEEN ? AND ?", (lowval, highval)):
        print("Song: {:23s} Rank: {}".format(*row))


# This function returns a list of songs between a user input length range
# The parameter c is the cursor to the database
# The parameter lowval is the lower bound of length
# The parameter highval is the upper bound of length
def song_between_length(c, lowval, highval):
    for row in c.execute("SELECT songs.song_name, length_sec FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE length_sec BETWEEN ? AND ?", (lowval, highval)):
        print("Song: {:23s} Length: {}".format(*row))




