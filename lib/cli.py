# lib/cli.py

from helpers import (
    exit_program,
    list_playlists,
    create_playlist,
    list_songs_by_playlist,
    delete_playlist,
    find_playlist_by_id,
    find_playlist_by_name,
    create_song,
    delete_song,
    list_all_songs,
    find_song_by_id,
    find_song_by_title
)


def main():
    while True:
        menu()
        choice = input("> ").lower()
        if choice == "e":
            exit_program()
        elif choice == "p":
            playlist_menu()
        else:
            print("Invalid choice")


def menu():
    print("\nPlease select an option:")
    print("-Type 'E' or 'e' to exit the program")
    print("-Type 'P' or 'p' to see playlists menu\n")


def playlist_menu():
    while True:
        print("\n-Type 'L' or 'l' to see playlists")
        print("-Type 'A' or 'a' to add a new playlist")
        print("-Type 'D' or 'd' to delete a playlist")
        print("-Type 'F' or 'f' to find a playlist by ID")
        print("-Type 'N' or 'n' to find a playlist by name")
        print("         OR          ")
        print("-Type 'B' or 'b' to go back to the main menu")
        print("-Type 'E' or 'e' to exit the program\n")


        choice = input("> ").lower()
        if choice == "l":
            list_playlists()
            songs_list()
        elif choice == "a":
            create_playlist()
        elif choice == "d":
            delete_playlist()
        elif choice == "f":
            find_playlist_by_id()
        elif choice == "n":
            find_playlist_by_name()
        elif choice == "b":
            break
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice")


def songs_list():
    while True:
        print("\n-Select a playlist number to view the songs in playlist")
        print("-Type 'all' to list all songs")
        print("-Type 'A' or 'a' to add a new song")
        print("-Type 'D' or 'd' to delete a song")
        print("-Type 'F' or 'f' to find a song by ID")
        print("-Type 'T' or 't' to find a song by title")
        print("         OR          ")
        print("-Type 'B' or 'b' to go back to the playlist menu\n")

        choice = input("> ").lower()
        if choice.isdigit():
            playlist_number = int(choice)
            list_songs_by_playlist(playlist_number)
        elif choice == "all":
            list_all_songs()
        elif choice == "a":
            create_song()
        elif choice == "d":
            delete_song()
        elif choice == "f":
            find_song_by_id()
        elif choice == "t": 
            find_song_by_title()
        elif choice == "b":
            break
        else:
            print("Invalid choice")
            

if __name__ == "__main__":
    main()
