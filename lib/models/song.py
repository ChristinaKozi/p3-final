from models.__init__ import CURSOR, CONN
from models.playlist import Playlist

class Song:

    all = {}

    def __init__(self, title, artist, duration, playlist_id, id=None):
        self.id = id
        self.title = title
        self.artist = artist
        self.duration = duration
        self.playlist_id = playlist_id

    def __repr__(self):
        return (
            f"Song {self.id}: {self.title} - {self.artist}, Duration: {self.duration}, " +
            f"Playlist {self.playlist_id}"
        )
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError(
                "Title must be a non-empty string"
            )

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, artist):
        if isinstance(artist, str) and len(artist):
            self._artist = artist
        else:
            raise ValueError(
                "Artist must be a non-empty string"
            )
        
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if isinstance(duration, (int, float)) and duration >= 0:
            self._duration = duration
        else:
            raise ValueError("Duration must be a non-negative number")

    @property
    def playlist_id(self):
        return self._playlist_id

    @playlist_id.setter
    def playlist_id(self, playlist_id):
        if type(playlist_id) == int and Playlist.find_by_id(playlist_id):
            self._playlist_id = playlist_id
        else:
            raise ValueError(
                "playlist_id must reference a department in the database")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Song instances """
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            artist TEXT,
            title TEXT,
            duration INTEGER,
            playlist_id INTEGER,
            FOREIGN KEY (playlist_id) REFERENCES playlists(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Songs instances """
        sql = """
            DROP TABLE IF EXISTS songs;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the title, artist, duration and playlist id values of the current Song object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO songs (title, artist, duration, playlist_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.artist, self.duration, self.playlist_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):
        """Delete the table row corresponding to the current Song instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM songs
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, title, artist, duration, playlist_id):
        """ Initialize a new Song instance and save the object to the database """
        song = cls(title, artist, duration, playlist_id)
        song.save()
        return song
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Song object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        song = cls.all.get(row[0])
        if song:
            song.title = row[1]
            song.artist = row[2]
            song.duration = row[3]
            song.department_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            song = cls(row[1], row[2], row[3], row[4])
            song.id = row[0]
            cls.all[song.id] = song
        return song
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Song object per table row"""
        sql = """
            SELECT *
            FROM songs
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Song object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM songs
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """Return Song object corresponding to first table row matching specified title"""
        sql = """
            SELECT *
            FROM songs
            WHERE title is ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def list_playlist_songs():
        id_ = input("Enter the song's playlist id: ")
        playlist = Playlist.find_by_id(id_)
        if playlist:
            songs = playlist.songs()
            for songs in songs:
                print(songs)
        else:
            print(f'Playlist {id_} not found')