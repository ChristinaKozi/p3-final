# lib/helpers.py
from models.playlist import Playlist
from models.song import Song

def exit_program():
    print("Happy Listening!")
    exit()

def list_playlists():
    print("\n*** Playlists ***")
    playlists = Playlist.get_all()
    for index, playlist in enumerate(playlists, start=1):
        print(f"{index}: {playlist.name}, {playlist.creator}")

def get_playlist_id_by_displayed_number(displayed_number):
    playlists = Playlist.get_all()
    if 1 <= displayed_number <= len(playlists):
        return playlists[displayed_number - 1].id
    else:
        return None
    
def create_playlist():
    name = input("Enter playlist name: ")
    creator = input("Enter playlist creator: ")
    try:
        playlist = Playlist.create(name, creator)
        print(f'\nPlaylist created: {playlist.name}')
    except Exception as exc:
        print("\nError creating department: ", exc)

def delete_playlist():
    playlist_number = int(input("Enter the playlist's number: "))
    try: 
        playlist_id = get_playlist_id_by_displayed_number(playlist_number)
        if playlist_id is not None:
            playlist = Playlist.find_by_id(playlist_id)

            songs = playlist.songs()
            print(f"Deleting Playlist {playlist_number} with {len(songs)} songs:")
            for song in songs:
                song.delete()
            playlist.delete()
            print(f'\nPlaylist {playlist_number} deleted')
        else:
            print(f'\nPlaylist {playlist_number} not found')
    except ValueError:
        print("Invalid input. Please enter a valid playlist number.")

def find_playlist_by_id():
    id_ = input("Enter the playlist's id: ")
    playlist = Playlist.find_by_id(id_)
    print(playlist) if playlist else print(f'Playlist {id_} not found')

def find_playlist_by_name():
    name = input("Enter the playlist's name: ")
    playlist = Playlist.find_by_name(name)
    print(f"\nPlaylist found: {playlist.name}, {playlist.creator}") if playlist else print(
        f'\nPlaylist {name} not found')

def list_songs_by_playlist(playlist_number):
    playlist_id = get_playlist_id_by_displayed_number(playlist_number)
    playlist = Playlist.find_by_id(playlist_id)
    print(f"\n*** Songs in {playlist.name} ***")
    if playlist:
        songs = playlist.songs()
        for index, song in enumerate(songs, start=1):
            print(f"{index}. {song.title} - {song.artist}, Duration: {song.duration}")
    else:
        print(f'\nPlaylist {playlist_number} not found')

def list_all_songs():
    print("\n*** All Songs ***")
    songs = Song.get_all()
    for index, song in enumerate(songs, start=1):
        print(f"{index}. {song.title} - {song.artist}, Duration: {song.duration}")

def create_song(playlist_number):
    title = input("Enter the songs's title: ")
    artist = input("Enter the song's artist: ")
    duration_input = input("Enter the song's duration: ")
    try:
        playlist_id = get_playlist_id_by_displayed_number(playlist_number)
        playlist = Playlist.find_by_id(playlist_id)
        if not playlist:
            raise ValueError(f'Playlist {playlist_number} not found')
    
        duration = float(duration_input)

        song = Song.create(title, artist, duration, playlist_id)
        print(f'\nSuccess: {song.title} - {song.artist}, Duration: {song.duration} added to {playlist.name}')
    except ValueError as exc:
        print("\nError creating song: ", exc)

def delete_song(playlist_number):
    try:
        playlist_id = get_playlist_id_by_displayed_number(playlist_number)
        playlist = Playlist.find_by_id(playlist_id)

        if not playlist:
            raise ValueError(f'Playlist {playlist_number} not found')

        songs = playlist.songs()

        if not songs:
            raise ValueError(f'No songs found in Playlist {playlist_number}')

        song_number = int(input("Enter the song's number: "))

        if 1 <= song_number <= len(songs):
            song = songs[song_number - 1]
            song.delete()
            print(f'\nSong {song_number} deleted')
        else:
            print(f'\nInvalid song number')
    except ValueError as exc:
        print("\nError deleting song: ", exc)

def find_song_by_id():
    id_ = input("Enter the song's id: ")
    song = Song.find_by_id(id_)
    print(song) if song else print(f'Song {id_} not found')

def find_song_by_title():
    title = input("Enter the song's title: ")
    song = Song.find_by_title(title)
    print(f"\nSong found: {song.title} - {song.artist}, Duration: {song.duration}") if song else print(
        f'\nSong {title} not found')
