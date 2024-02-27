from models.__init__ import CURSOR, CONN

class Playlist:

    all = {}

    def __init__(self, name, creator, id = None):
        self.id = id
        self.name = name
        self.creator = creator
    '''
    def __repr__(self):
        return f"Playlist {self.id}: {self.name}, {self.creator}"
    '''
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
    @property
    def creator(self):
        return self._creator
    
    @creator.setter
    def creator(self, creator):
        if isinstance(creator, str) and len(creator):
            self._creator = creator

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Playlist instances """
        sql = """
            CREATE TABLE IF NOT EXISTS playlists (
            id INTEGER PRIMARY KEY,
            name TEXT,
            creator TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Playlist instances """
        sql = """
            DROP TABLE IF EXISTS playlists;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and creator values of the current Playlist instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO playlists (name, creator)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.creator))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, creator):
        """ Initialize a new Playlist instance and save the object to the database """
        playlist = cls(name, creator)
        playlist.save()
        return playlist
    
    def delete(self):
        """Delete the table row corresponding to the current Playlist instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM playlists
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Playlist object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        playlist = cls.all.get(row[0])
        if playlist:
            # ensure attributes match row values in case local instance was modified
            playlist.name = row[1]
            playlist.creator = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            playlist = cls(row[1], row[2])
            playlist.id = row[0]
            cls.all[playlist.id] = playlist
        return playlist
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Playlist object per table row"""
        sql = """
            SELECT *
            FROM playlists
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return a Playlist object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM playlists
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Playlist object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM playlists
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def songs(self):
        """Return list of songs associated with current playlist"""
        from models.song import Song
        sql = """
            SELECT * FROM songs
            WHERE playlist_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Song.instance_from_db(row) for row in rows
        ]
