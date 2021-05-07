# author: Adem YILDIZ
# library.py
import sqlite3
import time

class Music():
    def __init__(self, name, artist, album, label, length):
        self.name = name
        self.artist = artist
        self.album = album
        self.label = label
        self.length = length
    
    def __str__(self):
        return "Title: {}\nArtist: {}\nAlbum: {}\nLabel: {}\nTime: {}\n-------\n".format(self.name, self.artist, self.album, self.label, self.length)
    

class Library():
    def __init__(self):
        self.make_connection()
    
    def make_connection(self):
        self.connection = sqlite3.connect("library.db")
        self.cursor = self.connection.cursor()
        ask = "Create Table If not exists songs (name TEXT,artist TEXT,album TEXT,label TEXT,length INT)"
        self.cursor.execute(ask)
        self.connection.commit()

    def cancel_connection(self):
        self.connection.close()

    def show_songs(self):
        ask = "Select * From songs"
        self.cursor.execute(ask)
        songs = self.cursor.fetchall()

        if( len(songs) == 0 ):
            print("There aren't any songs in library!")
        else:
            for i in songs:
                song = Music(i[0], i[1], i[2], i[3], i[4])
                print(song)
    
    def search_song(self, name):
        ask = "Select * From songs where name = ?"
        self.cursor.execute(ask, (name,))
        songs = self.cursor.fetchall()

        if ( len(songs) == 0 ):
            print("There isn't such a song in library!")
        else:
            song = Music(songs[0][0], songs[0][1], songs[0][2], songs[0][3], songs[0][4])
            print(song)
    
    def add_new_song(self, song):
        ask = "Insert into songs Values(?,?,?,?,?)"
        self.cursor.execute(ask, (song.name, song.artist, song.album, song.label, song.length))
        self.connection.commit()

    def delete_song(self, name):
        ask = "Delete From songs where name = ?"
        self.cursor.execute(ask, (name,))
        self.connection.commit()

    def search_album(self, album):
        ask = "Select * From songs where album = ?"
        self.cursor.execute(ask, (album,))
        songs = self.cursor.fetchall()

        if ( len(songs) == 0 ):
            print("There isn't such an album in library!")
        else:
            for i in range (len(songs)):
                print(songs[i][0])
