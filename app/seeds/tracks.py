from app.models import db, Track, environment, SCHEMA
from sqlalchemy.sql import text


def seed_tracks():
    demo = Track(
        artist_id = '1', album_id = 1, title = 'Believe', duration = 239, genre = 'Pop', track_number = 1, url = 'ineedaurl.com', preview_image_url = 'ineedanotherurl.com')
    demo = Track(
        artist_id = '2', album_id = 2, title = 'Holding Out for a Hero', duration = 251, genre = 'Pop', track_number = 1, url = 'ineedaurl.com', preview_image_url = 'ineedanotherurl.com')
    



    db.session.add(demo)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
