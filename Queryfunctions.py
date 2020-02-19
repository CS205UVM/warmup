import sqlite3


# The all_songs function displays all of the songs and its information
# Parameter c is the database cursor
def all_songs(c):
    print("Rank\tSong\t\t\t\tLength(s)\t\tGenre\t\t\tPopularity\tArtist")
    print("----------------------------------------------------------------------------------")
    for row in c.execute("SELECT songs.rank, songs.song_name, songs.length_sec, artists.genre, artists.popularity,"
                         "artists.artist_name"
                         " FROM songs JOIN artists ON songs.artist_name = artists.artist_name"):
       print("{:7s} {:22s} {:12s} {:15s} {:11s} {:11s}".format(*row))


# The artist_and_song function displays an artist and all the songs by that artist
# Parameter c is the database cursor
# Parameter artist is the artist being search
def artist_and_song(c, artist):
    for row in c.execute("SELECT artists.artist_name, song_name FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE artist_name == ?", (artist,)):
        print(row)


# if the user requests a song and wants the artist
def song_and_artist(c, song):
    for row in c.execute("SELECT song_name, songs.artist_name FROM songs JOIN artists "
                          "ON songs.artist_name = artists.artist_name "
                          "WHERE song_name == ?", (song,)):
        print(row)


# if a user requests a song and wants its popularity
def song_and_popularity(c,song):
    for row in c.execute("SELECT song_name, popularity FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE song_name == ?", (song,)):
        print(row)


# if a user requests a song and wants its genre
def song_and_genre(c, song):
    for row in c.execute("SELECT song_name, genre FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE song_name == ?", (song,)):
        print(row)


# if a user requests a genre and wants its songs
def songs_by_genre(c, genre):
    for row in c.execute("SELECT genre, song_name FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE genre == ?", (genre,)):
        print(row)


# if a user requests a song and its length
def song_and_length(c, song):
    for row in c.execute("SELECT song_name, length_sec FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE song_name == ?", (song,)):
        print(row)


# if a user wants songs in a range of popularity
def song_between_popularity(c, lowval, highval):
    for row in c.execute("SELECT song_name, popularity FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE popularity BETWEEN ? AND ?", (lowval, highval)):
        print(row)


def song_between_rank(c, lowval, highval):
    for row in c.execute("SELECT song_name, rank FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE rank BETWEEN ? AND ?", (lowval, highval)):
        print(row)


# if a user wants songs in a range of length length
def song_between_length(c, lowval, highval):
    for row in c.execute("SELECT song_name, length_sec FROM songs JOIN artists "
                         "ON songs.artist_name = artists.artist_name "
                         "WHERE length_sec BETWEEN ? AND ?", (lowval, highval)):
        print(row)




