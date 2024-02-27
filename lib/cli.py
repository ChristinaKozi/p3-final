# lib/cli.py

from helpers import (
    exit_program,
    list_playlists,
    create_playlist,
    list_songs_by_playlist,
    delete_playlist,
    find_playlist_by_name,
    create_song,
    delete_song,
    list_all_songs,
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
    print("\nHello! Welcome to your interactive Music Playlist Manager!")
    print("\nPlease select from the options below:")
    print("\n-Type 'E' or 'e' to exit the program")
    print("-Type 'P' or 'p' to see playlists menu\n")


def playlist_menu():
    while True:
        print("\n-Type 'L' or 'l' to view or edit all playlists")
        print("-Type 'A' or 'a' to add a new playlist")
        print("-Type 'D' or 'd' to delete a playlist")
        print("-Type 'N' or 'n' to find a playlist by name")
        print("         OR          ")
        print("-Type 'B' or 'b' to go back to the main menu")
        print("-Type 'E' or 'e' to exit the program\n")


        choice = input("> ").lower()
        if choice == "l":
            songs_list()
        elif choice == "a":
            create_playlist()
            list_playlists()
        elif choice == "d":
            delete_playlist()
            list_playlists()
        elif choice == "n":
            find_playlist_by_name()
            list_playlists()
        elif choice == "b":
            break
        elif choice == "e":
            exit_program()
        else:
            print("Invalid choice")


def songs_list():
    while True:
        list_playlists()
        print("\n-Select a playlist number to view the songs within")
        print("-Type 'all' to list all songs")
        print("-Type 'T' or 't' to find a song by title")
        print("         OR          ")
        print("-Type 'B' or 'b' to go back to the playlist menu\n")

        choice = input("> ").lower()
        if choice.isdigit():
            playlist_number = int(choice)
            list_songs_by_playlist(playlist_number)
            song_action_menu(playlist_number)
        elif choice == "all":
            list_all_songs()
        #elif choice == "a":
            #create_song(playlist_number)
        #elif choice == "d":
            #delete_song()
        elif choice == "t": 
            find_song_by_title()
        elif choice == "b":
            break
        else:
            print("Invalid choice")

def song_action_menu(playlist_number):
    while True:
        print("\n-Select an option:")
        print("-Type 'A' or 'a' to add a new song")
        print("-Type 'D' or 'd' to delete a song")
        print("-Type 'B' or 'b' to go back\n")
        inner_choice = input("> ").lower()
        if inner_choice == "a":
            create_song(playlist_number)
            list_songs_by_playlist(playlist_number)
        elif inner_choice == "d":
            delete_song(playlist_number)
            list_songs_by_playlist(playlist_number)
        elif inner_choice == "b":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
