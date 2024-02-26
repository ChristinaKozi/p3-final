# Phase 3 Final

## Introduction
Here we have a one-to-many relationship being represented by a Playlist model and a Song model. Using ORM methods and CLI commands we are able to navigate the different functions available to both classes.

This Command Line Interface (CLI) allows users to manage playlists and songs. It provides a simple and interactive way to perform actions such as creating playlists, adding and deleting songs, and finding playlists or songs by ID or name.

## Getting Started
Be sure to run `pipenv install` to install the dependencies and
`pipenv shell` to enter your virtual environment before running your code.**

```bash
pipenv install
pipenv shell
```
The file `lib/seed.py` contains code to initialize the database with sample
playlists and songs. Run the following command to seed the database:

```bash
python lib/seed.py
```
The file `lib/cli.py` contains a command line interface for our music streaming database
application.

Run the CLI by executing the command:
```bash
python lib/cli.py
```

## Navigate through the CLI Menus:

Use the following options to navigate through the menus:

Type 'E' or 'e' to exit the program.

Type 'P' or 'p' to see the playlists menu.

Inside the playlists menu:

Type 'L' or 'l' to see existing playlists.
Type 'A' or 'a' to add a new playlist.
Type 'D' or 'd' to delete a playlist.
Type 'F' or 'f' to find a playlist by ID.
Type 'N' or 'n' to find a playlist by name.
Type 'B' or 'b' to go back to the main menu.
Type 'E' or 'e' to exit the program.

Inside the songs menu (activated when viewing playlists):

Select a playlist number to view songs in the playlist.
Type 'all' to list all songs.
Type 'A' or 'a' to add a new song.
Type 'D' or 'd' to delete a song.
Type 'F' or 'f' to find a song by ID.
Type 'T' or 't' to find a song by title.
Type 'B' or 'b' to go back to the playlist menu.

Follow the prompts above to perform various actions such as creating playlists, adding or deleting songs, and finding playlists or songs.

Type 'E' or 'e' at any time to exit the program.

## Available Actions
* Create Playlist:
Add a new playlist with a specified name and creator.

* Delete Playlist:
Delete an existing playlist by providing its ID.

* Find Playlist by ID or Find Playlist by Name:
Find a playlist by either its numerical ID or name.

* List All Playlists:
Display a list of all existing playlists.

* Add Song to Playlist:
Add a new song to a specified playlist.

* Delete Song:
Delete an existing song by providing its ID.

* Find Song by ID or Find Song by Title:
Find a song by either its numerical ID or title.

* List All Songs:
Display a list of all existing songs.

## Helper Functions
The helper functions are housed in lib/helpers.py which is imported into the cli.py file to clearly state and facilitate the management of playlists and songs within the music playlist manager. Below is a brief description of each function.

1. exit_program():
Exits the program and prints the farewell message, "Happy Listening!".

2. list_playlists():
Lists all playlists by fetching and displaying information from the Playlist model.

3. create_playlist():
Creates a new playlist by taking user input for the playlist name and creator. Handles exceptions and prints a success message upon playlist creation.

4. delete_playlist():
Deletes a playlist by accepting the playlist's ID as input. Checks if the playlist exists, deletes it, and prints a confirmation message.

5. find_playlist_by_id():
Finds and displays a playlist by accepting the playlist's ID as input.

6. find_playlist_by_name():
Finds and displays a playlist by accepting the playlist's name as input.

7. list_songs_by_playlist(id_):
Lists all songs in a playlist by accepting the playlist's ID as input. Retrieves the playlist, fetches its songs, and prints song information.

8. list_all_songs():
Lists all songs by fetching and displaying information from the Song model.

9. create_song():
Creates a new song by taking user input for the song's title, artist, duration, and playlist ID. Handles exceptions and prints a success message upon song creation.

10. delete_song():
Deletes a song by accepting the song's ID as input. Checks if the song exists, deletes it, and prints a confirmation message.

11. find_song_by_id():
Finds and displays a song by accepting the song's ID as input.

12. find_song_by_title():
Finds and displays a song by accepting the song's title as input.

## Playlist Model:

The Playlist class has the following attributes:

* id: Playlist ID.
* name: Playlist name.
* creator: Playlist creator.

The property methods are:
name
* Getter: Returns the playlist name.
* Setter: Validates and sets the playlist name.

creator
* Getter: Returns the playlist creator.
* Setter: Validates and sets the playlist creator.

Below are a list of class methods that are utilized by the helper functions:
1. create_table()
* Creates a new table in the database to persist Playlist instances.

2. drop_table()
* Drops the table that persists Playlist instances.

3. save()
* Inserts a new row with the name and creator values, updates object id, and saves in a local dictionary.

4. create(name, creator)
* Initializes a new Playlist instance and saves it to the database.

5. delete()
* Deletes the table row, dictionary entry, and reassigns id to None.

6. instance_from_db(row)
* Returns a Playlist object with attribute values from the table row.

7. get_all()
* Returns a list with one Playlist object per table row.

8. find_by_id(id)
* Returns a Playlist object for the table row matching the specified primary key.

9. find_by_name(name)
* Returns a Playlist object for the first table row matching the specified name.

10. songs()
* Returns a list of songs associated with the current playlist.

## Song Model
The Song class has the following attributes:

* id: Song ID.
* title: Song title.
* artist: Song artist.
* duration: Song duration.
* playlist_id: Playlist ID associated with the song.

The property methods are similar to those of the playlist model with the only difference being the class attributes aligning with the song class for methods like create, find_by_id, find_by_title. The Song class is designed to be used within the larger music playlist manager application, interacting with a database to manage all songs associated with playlists.

## Conclusion
The collaboration between the Song and Playlist classes allows for seamless interaction between songs and playlists, enhancing the functionality of the overall music management system.