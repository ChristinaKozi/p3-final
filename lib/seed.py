from models.__init__ import CONN, CURSOR
from models.playlist import Playlist
from models.song import Song

def seed_database():
    Song.drop_table()
    Playlist.drop_table()
    Playlist.create_table()
    Song.create_table()

    top_hits = Playlist.create("Top Hits", "Bob Johnson")
    workout_tracks = Playlist.create("Workout Tracks", "Jan Johnson")
    Song.create("Let It Be", "The Beatles", 4.03, top_hits.id)
    Song.create("Stand By Me", "Ben E.King", 3, top_hits.id)
    Song.create("I Will Survive", "Gloria Gaynor", 3.19, top_hits.id)
    Song.create("Stronger", "Kelly Clarkson", 3.42, workout_tracks.id)
    Song.create("Eye of the Tiger", "Survivor", 4.06, workout_tracks.id)


seed_database()
print("Seeded database")