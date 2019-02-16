import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', passwd='Cc20178452#1')

cursor = db.cursor()
cursor.execute("USE songDatabase")


def insert_artist(artist_id: str, artist_name: str):
    sql = "DELETE FROM artist WHERE artistID = %s"
    val = (artist_id,)
    cursor.execute(sql, val)
    db.commit()
    sql = "INSERT INTO artist(artistID, artistName) VALUES (%s, %s)"
    val = (artist_id, artist_name)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record added to ARTIST")


def insert_song(artist_id: str, song_name: str):
    sql = "DELETE FROM song WHERE artistID = %s AND songName = %s"
    val = (artist_id, song_name)
    cursor.execute(sql, val)
    db.commit()
    sql = "INSERT INTO song(artistID, songName) VALUES (%s, %s)"
    val = (artist_id, song_name)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record added to SONG")


def get_artist(artist_id: str):
    sql = "SELECT * FROM artist WHERE artistID = %s"
    val = (artist_id,)
    cursor.execute(sql, val)
    artist = []
    result = cursor.fetchall()
    for a in result:
        artist.append(a)
    return artist


def get_song(artist_id: str, song_name:str):
    sql = "SELECT * FROM song WHERE artistID = %s AND songName = %s"
    val = (artist_id, song_name)
    cursor.execute(sql, val)
    song = []
    result = cursor.fetchall()
    for a in result:
        song.append(a)
    return song


# TESTING#

# Insert artists and songs #
insert_artist("13579", "XXXTENTACION")
insert_artist("2468", "Muse")
insert_song("13579", "SAD!")
insert_song("2468", "Something Human")

# Retrieve songs and artists #
artist1 = get_artist("13579")
print(artist1)
artist2 = get_artist("2468")
print(artist2)

song1 = get_song("13579", "SAD!")
print(song1)
song2 = get_song("2468", "Something Human")
print(song1)

