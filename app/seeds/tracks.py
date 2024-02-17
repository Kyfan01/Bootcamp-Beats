from app.models import db, Track, environment, SCHEMA
from sqlalchemy.sql import text


def seed_tracks():
    # collin
    collin_track1 = Track(
        artist_id = '3', album_id = 1, title = 'Believe', duration = 239, genre = 'Pop', track_number = 1, url = 'ineedaurl.com', preview_image_url = 'ineedanotherurl.com')
    collin_track2 = Track(
        artist_id = '3', album_id = 2, title = 'Holding Out for a Hero', duration = 251, genre = 'Pop', track_number = 1, url = 'ineedaurl.com', preview_image_url = 'ineedanotherurl.com')
    collin_track3 = Track(
        artist_id = '3', album_id = 3, title = 'Data drive', duration = 300, genre = 'EDM', track_number = 1, url = 'ineedaurl.com', preview_image_url = 'ineedanotherurl.com')
    collin_track4 = Track(
        artist_id = '3', album_id = 3, title = 'Digital dreams', duration = 291, genre = 'EDM', track_number = 2, url = 'ineedaurl.com', preview_image_url = 'ineedanotherurl.com')

    # kevin
    kevin_track1 = Track(
        artist_id = '2', album_id = 4, title = 'Genesis', duration = 234, genre = 'EDM', track_number = 1, url = 'ineedaurl.com', preview_image_url = 'ineedanotherurl.com')
    kevin_track2 = Track(
        artist_id = '2', album_id = 4, title = 'Technologic', duration = 284, genre = 'EDM', track_number = 2, url = 'ineedaurl.com', preview_image_url = 'ineedanotherurl.com')

    # hun
    hun_track1 = Track(
        artist_id = '1', album_id = 1, title = "World's smallest violin", duration = 240, genre = 'Pop', track_number = 1, url = 'ineedaurl.com', preview_image_url = 'ineedanotherurl.com')
    hun_track2 = Track(
        artist_id = '1', album_id = 1, title = "Bang!", duration = 171, genre = 'Pop', track_number = 2, url = 'ineedaurl.com', preview_image_url = 'ineedanotherurl.com')


    db.session.add(collin_track1)
    db.session.add(collin_track2)
    db.session.add(collin_track3)
    db.session.add(collin_track4)
    db.session.add(kevin_track1)
    db.session.add(kevin_track2)
    db.session.add(hun_track1)
    db.session.add(hun_track2)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_tracks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.tracks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM tracks"))

    db.session.commit()
