from app.models import db, Album, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date

def seed_albums():
    albums = [
        Album(artist_id = '3', title = 'Binary Grooves: The Dj Bytebeat Collection', release_date= date(1997, 12, 4), genre = 'Pop', album_cover_url = 'ineedaurl.com', single = False),
        Album(artist_id = '1', title = 'Metronome', release_date= date(1997, 12, 4), genre = 'Pop', album_cover_url = 'ineedaurl.com', single = False),
        Album(artist_id = '2', title = 'Cross', release_date= date(1997, 12, 4), genre = 'EDM', album_cover_url = 'ineedaurl.com', single = False),
        Album(artist_id = '2', title = 'Human After All', release_date= date(2005, 12, 4), genre = 'Electronica', album_cover_url = 'ineedaurl.com', single = False)
    ]

    db.session.add_all(albums)
    db.session.commit()

def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))

    db.session.commit()
