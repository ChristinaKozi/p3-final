# lib/helpers.py
from models.playlist import Playlist
from models.song import Song

def exit_program():
    print("Happy Listening!")
    exit()

def list_playlists():
    print("*** Playlists ***")
    playlists = Playlist.get_all()
    for playlist in playlists:
        print(playlist)

def create_playlist():
    name = input("Enter playlist name: ")
    creator = input("Enter playlist creator: ")
    try:
        playlist = Playlist.create(name, creator)
        print(f'Playlist created: {playlist}')
    except Exception as exc:
        print("Error creating department: ", exc)

def delete_playlist():
    id_ = input("Enter the playlist's id: ")
    if playlist := Playlist.find_by_id(id_):
        playlist.delete()
        print(f'Playlist {id_} deleted')
    else:
        print(f'Playlist {id_} not found')

def find_playlist_by_id():
    id_ = input("Enter the playlist's id: ")
    playlist = Playlist.find_by_id(id_)
    print(playlist) if playlist else print(f'Playlist {id_} not found')

def find_playlist_by_name():
    name = input("Enter the playlist's name: ")
    playlist = Playlist.find_by_name(name)
    print(playlist) if playlist else print(
        f'Playlist {name} not found')

def list_songs_by_playlist(id_):
    playlist = Playlist.find_by_id(id_)
    if playlist:
        songs = playlist.songs()
        for song in songs:
            print(song)
    else:
        print(f'Playlist {id_} not found')

def list_all_songs():
    songs = Song.get_all()
    for song in songs:
        print(song)

def create_song():
    title = input("Enter the songs's title: ")
    artist = input("Enter the song's artist: ")
    duration_input = input("Enter the song's duration: ")
    playlist_id_input = input("Enter the song's playlist id: ")

    try:
        playlist_id = int(playlist_id_input)
        playlist = Playlist.find_by_id(playlist_id)
        if not playlist:
            raise ValueError(f'Playlist {playlist_id} not found')
        
        duration = float(duration_input)

        song = Song.create(title, artist, duration, playlist_id)
        print(f'Success: {song}')
    except ValueError as exc:
        print("Error creating song: ", exc)

def delete_song():
    id_ = input("Enter the song's id: ")
    if song := Song.find_by_id(id_):
        song.delete()
        print(f'Song {id_} deleted')
    else:
        print(f'Song {id_} not found')

def find_song_by_id():
    id_ = input("Enter the song's id: ")
    song = Song.find_by_id(id_)
    print(song) if song else print(f'Song {id_} not found')

def find_song_by_title():
    title = input("Enter the song's title: ")
    song = Song.find_by_title(title)
    print(song) if song else print(
        f'Song {title} not found')
