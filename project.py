# from library import Music
# from library import Library
# from library import sqlite3
# from library import time

from library import *
print("""***********************************
Welcome to your Music Library!

1. Show my songs!
2. I want to search a song by name.
3. Add a new song
4. Delete a song
5. Edit a song
6. Show me album

Press 'q' to exit!
***********************************""")

library = Library()

while True:
    op = input("What would you like to do?\n")

    if(op == "q"):
        print("Bye bye!")
        break

    elif(op == "1"):
        library.show_songs()

    elif(op == "2"):
        name = input("Enter the song's name: ")
        print("Searching...")
        time.sleep(2)
        library.search_song(name)

    elif(op == "3"):
        name = input("Name: ")
        artist = input("Artist: ")
        album = input("Album: ")
        label = input("Label: ")
        length = input("Length: ")

        new_song = Music(name, artist, album, label, length)
        print("New song is being added...")
        time.sleep(2)

        library.add_new_song(new_song)
        print("New song is added to your library!!")

    elif(op == "4"):
        name = input("Which song do you want to delete?")
        library.delete_song(name)
        print("And, it's gone!")
    
    elif(op == "5"):
        name2 = input("Which song do you want to edit?")
        library.delete_song(name2)

        name = input("Name: ")
        artist = input("Artist: ")
        album = input("Album: ")
        label = input("Label: ")
        length = input("Length: ")

        edited_song = Music(name, artist, album, label, length)
        library.add_new_song(edited_song)
        
        print("Song is edited succesfully!")

    elif(op == "6"):
        album_name = input("Enter the album name: ")
        library.search_album(album_name)

    else:
        print("There isn't such an option.")