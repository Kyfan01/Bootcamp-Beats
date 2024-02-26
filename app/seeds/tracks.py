from app.models import db, Track, environment, SCHEMA
from sqlalchemy.sql import text


def seed_tracks(hun, kevin, collin, demo):
        # collin
    # collin_track1 = Track(
    #     artist_id = '3', album_id = 1, title = 'Believe', duration = 239, genre = 'Pop', track_number = 1, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # collin_track2 = Track(
    #     artist_id = '3', album_id = 2, title = 'Holding Out for a Hero', duration = 251, genre = 'Pop', track_number = 1, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # collin_track3 = Track(
    #     artist_id = '3', album_id = 3, title = 'Data drive', duration = 300, genre = 'EDM', track_number = 1, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # collin_track4 = Track(
    #     artist_id = '3', album_id = 3, title = 'Digital dreams', duration = 291, genre = 'EDM', track_number = 2, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # collin_track5 = Track(
    #     artist_id = '3', album_id = 3, title = 'Code Jam', duration = 201, genre = 'Pop', track_number = 3, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # collin_track6 = Track(
    #     artist_id = '3', album_id = 3, title = 'Syntax Symphony', duration = 224, genre = 'Pop', track_number = 4, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # collin_track7 = Track(
    #     artist_id = '3', album_id = 3, title = 'Binary Boogie', duration = 196, genre = 'Pop', track_number = 5, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # collin_track8 = Track(
    #     artist_id = '3', album_id = 3, title = 'Byte-sized Beats', duration = 213, genre = 'Pop', track_number = 6, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # collin_track9 = Track(
    #     artist_id = '3', album_id = 3, title = 'Loop Logic', duration = 198, genre = 'Pop', track_number = 7, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # collin_track10 = Track(
    #     artist_id = '3', album_id = 3, title = 'Pixel Pulse', duration = 189, genre = 'Pop', track_number = 8, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # collin_track11 = Track(
    #     artist_id = '3', album_id = 3, title = 'Bit Bounce', duration = 199, genre = 'Pop', track_number = 9, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # collin_track12 = Track(
    #     artist_id = '3', album_id = 3, title = 'Cybernetic Serenade', duration = 214, genre = 'Pop', track_number = 10, url = 'ineedaurl.com', preview_image_url = test_image_url)

    # # kevin
    # kevin_track1 = Track(
    #     artist_id = '2', album_id = 4, title = 'Genesis', duration = 234, genre = 'EDM', track_number = 1, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # kevin_track2 = Track(
    #     artist_id = '2', album_id = 4, title = 'Technologic', duration = 284, genre = 'EDM', track_number = 2, url = 'ineedaurl.com', preview_image_url = test_image_url)

    # # hun
    # hun_track1 = Track(
    #     artist_id = '1', album_id = 1, title = "World's smallest violin", duration = 240, genre = 'Pop', track_number = 1, url = 'ineedaurl.com', preview_image_url = test_image_url)
    # hun_track2 = Track(
    #     artist_id = '1', album_id = 1, title = "Bang!", duration = 171, genre = 'Pop', track_number = 2, url = 'ineedaurl.com', preview_image_url = test_image_url)
    test_image_url_1 = 'https://bootcampbeats-tracks.s3.amazonaws.com/4ddbd8fa75ef47b8814d594183c0bffd.jpg'
    test_image_url_2 = 'https://bootcampbeats-tracks.s3.amazonaws.com/4ddbd8fa75ef47b8814d594183c0bffd.jpg'

    test_track_url_1 = 'https://bootcampbeats-tracks.s3.amazonaws.com/9f1923edbd0c4b969f64938dd22bb36a.wav'
    test_track_url_2 = 'https://bootcampbeats-tracks.s3.amazonaws.com/9f1923edbd0c4b969f64938dd22bb36a.wav'

    album_image_1 = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-1.jpg'
    album_image_2 = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-2.jpg'
    album_image_3 = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-3.jpg'
    album_image_4 = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-4.jpg'
    album_image_5 = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-5.jpg'
    album_image_6 = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-6.jpg'
    album_image_7 = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-7.jpg'
    album_image_8 = 'https://bootcampbeats-tracks.s3.amazonaws.com/her-album-cover.jpg'
    album_image_9 = 'https://bootcampbeats-tracks.s3.amazonaws.com/mito-album-cover.jpg'






    tracks = [
    # collin
        Track(artist_id = 3, album_id = 1, title = 'Data Drive', duration = 300, genre = 'EDM', track_number = 1, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-1.m4a', preview_image_url = album_image_1),
        Track(artist_id = 3, album_id = 1, title = 'Digital Dreams', duration = 291, genre = 'EDM', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-2.m4a', preview_image_url = album_image_1),
        Track(artist_id = 3, album_id = 1, title = 'Code Jam', duration = 201, genre = 'Pop', track_number = 3, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-3.m4a', preview_image_url = album_image_1),
        Track(artist_id = 3, album_id = 1, title = 'Syntax Symphony', duration = 224, genre = 'Pop', track_number = 4, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-4.m4a', preview_image_url = album_image_1),
        Track(artist_id = 3, album_id = 5, title = 'Binary Boogie', duration = 196, genre = 'Pop', track_number = 5, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-5.m4a', preview_image_url = album_image_2),
        Track(artist_id = 3, album_id = 5, title = 'Byte-Sized Beats', duration = 213, genre = 'Pop', track_number = 6, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-6.m4a', preview_image_url = album_image_2),
        Track(artist_id = 3, album_id = 5, title = 'Loop Logic', duration = 198, genre = 'Pop', track_number = 7, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-7.m4a', preview_image_url = album_image_2 ),
        Track(artist_id = 3, album_id = 6, title = 'Pixel Pulse', duration = 189, genre = 'Pop', track_number = 8, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-8.m4a', preview_image_url = album_image_3),
        Track(artist_id = 3, album_id = 6, title = 'Bit Bounce', duration = 199, genre = 'Pop', track_number = 9, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-9.m4a', preview_image_url = album_image_3),
        Track(artist_id = 3, album_id = 6, title = 'Cybernetic Serenade', duration = 214, genre = 'Pop', track_number = 10, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-10.m4a', preview_image_url = album_image_3),
        
        Track(artist_id = 3, album_id = 7, title = 'ByteBeat Boogie', duration = 214, genre = 'Dance', track_number = 1, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-13.mp3', preview_image_url = album_image_7),
        Track(artist_id = 3, album_id = 7, title = 'Algorithmic Anthem', duration = 214, genre = 'Dance', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-14.mp3', preview_image_url = album_image_7),
        Track(artist_id = 3, album_id = 7, title = 'Groove Generator', duration = 214, genre = 'Dance', track_number = 3, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-15.mp3', preview_image_url = album_image_7),
        Track(artist_id = 3, album_id = 7, title = 'Synthwave Surge', duration = 214, genre = 'Dance', track_number = 4, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-16.mp3', preview_image_url = album_image_7),
        Track(artist_id = 3, album_id = 7, title = 'Electro Evolution', duration = 214, genre = 'Dance', track_number = 5, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-17.mp3', preview_image_url = album_image_7),
        Track(artist_id = 3, album_id = 7, title = 'Techno Trance', duration = 214, genre = 'Dance', track_number = 6, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-18.mp3', preview_image_url = album_image_7),
        Track(artist_id = 3, album_id = 7, title = 'Virtual Vibrations', duration = 214, genre = 'Dance', track_number = 7, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-19.mp3', preview_image_url = album_image_7),
        Track(artist_id = 3, album_id = 7, title = 'Rhythm Rift', duration = 214, genre = 'Dance', track_number = 8, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-20.mp3', preview_image_url = album_image_7),
        Track(artist_id = 3, album_id = 7, title = 'Quantum Quake', duration = 214, genre = 'Dance', track_number = 9, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-21.mp3', preview_image_url = album_image_7),
        Track(artist_id = 3, album_id = 7, title = 'Synthwave Supernova', duration = 214, genre = 'Dance', track_number = 10, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-22.mp3', preview_image_url = album_image_7),

        # Track(artist_id='2', album_id=3, title="Code'n'Country", duration=180, genre='Country', track_number=1, url='ineedaurl.com', preview_image_url=test_image_url, track_likes=[collin, kevin]),
        # Track(artist_id='2', album_id=3, title='Digital Dusty Roads', duration=220, genre='Country', track_number=2, url='ineedaurl.com', preview_image_url=test_image_url, track_likes=[hun, collin]),
        # Track(artist_id='2', album_id=3, title='ByteBeat Hoedown', duration=195, genre='Country', track_number=3, url='ineedaurl.com', preview_image_url=test_image_url, track_likes=[kevin, hun]),
        # Track(artist_id='2', album_id=3, title='Algorithmic Cowboy', duration=210, genre='Country', track_number=4, url='ineedaurl.com', preview_image_url=test_image_url, track_likes=[collin, hun]),
        # Track(artist_id='2', album_id=3, title='Syntax Saddle', duration=190, genre='Country', track_number=5, url='ineedaurl.com', preview_image_url=test_image_url, track_likes=[kevin, hun]),
        # Track(artist_id='2', album_id=3, title='Binary Sunset', duration=205, genre='Country', track_number=6, url='ineedaurl.com', preview_image_url=test_image_url, track_likes=[kevin, collin]),
        # Track(artist_id='2', album_id=3, title='Loopin\' Lasso', duration=240, genre='Country', track_number=7, url='ineedaurl.com', preview_image_url=test_image_url, track_likes=[hun, collin]),
        # Track(artist_id='2', album_id=3, title='Cybernetic Swing', duration=195, genre='Country', track_number=8, url='ineedaurl.com', preview_image_url=test_image_url, track_likes=[hun, collin]),
        # Track(artist_id='2', album_id=3, title='Recursive Roundup', duration=220, genre='Country', track_number=9, url='ineedaurl.com', preview_image_url=test_image_url, track_likes=[kevin, hun]),
        # Track(artist_id='2', album_id=3, title='Tech Tumbleweed', duration=320, genre='Country', track_number=10, url='ineedaurl.com', preview_image_url=test_image_url, track_likes=[kevin, collin]),


    # kevin
        Track(artist_id = 2, album_id = 3, title = 'Genesis', duration = 234, genre = 'EDM', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/genesis.mp3', preview_image_url = album_image_4),
        Track(artist_id = 2, album_id = 4, title = 'Technologic', duration = 284, genre = 'EDM', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/technologic.mp3', preview_image_url = album_image_5),

        Track(artist_id = 2, album_id = 3, title = 'D.A.N.C.E.', duration = 214, genre = 'EDM', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/cross-dance.mp3', preview_image_url = album_image_4),
        Track(artist_id = 2, album_id = 3, title = 'Waters of Nazareth', duration = 214, genre = 'EDM', track_number = 3, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/cross-waters-of-nazareth.mp3', preview_image_url = album_image_4),
        Track(artist_id = 2, album_id = 3, title = 'One Minute to Midnight', duration = 214, genre = 'EDM', track_number = 4, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/cross-one-minute-to-midnight.mp3', preview_image_url = album_image_4),

        Track(artist_id = 2, album_id = 8, title = 'Jasmine', duration = 214, genre = 'EDM', track_number = 1, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/her-jasmine.mp3', preview_image_url = album_image_8),
        Track(artist_id = 2, album_id = 8, title = 'Martini Blue', duration = 214, genre = 'EDM', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/her-martini-blue.mp3', preview_image_url = album_image_8),
        Track(artist_id = 2, album_id = 8, title = 'Text Me', duration = 214, genre = 'EDM', track_number = 3, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/her-text-me.mp3', preview_image_url = album_image_8),

        Track(artist_id = 2, album_id = 9, title = 'Don\'t Go Insane', duration = 214, genre = 'EDM', track_number = 1, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/mito-dont-go-insane.mp3', preview_image_url = album_image_9),
        Track(artist_id = 2, album_id = 9, title = 'No Blueberries', duration = 214, genre = 'EDM', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/mito-no-blueberries.mp3', preview_image_url = album_image_9),
        Track(artist_id = 2, album_id = 9, title = 'Nerves', duration = 214, genre = 'EDM', track_number = 3, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/mito-nerves.mp3', preview_image_url = album_image_9),

    # hun
        Track(artist_id = 1, album_id = 2, title = "World's smallest violin", duration = 240, genre = 'Pop', track_number = 1, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-11.m4a', preview_image_url = album_image_6),
        Track(artist_id = 1, album_id = 2, title = "Bang!", duration = 171, genre = 'Pop', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-12.m4a', preview_image_url = album_image_6)
        ]
    


    for track in tracks:
        db.session.add(track)


    # db.session.add_all(tracks)

    db.session.commit()

    for track in tracks:
        track.track_likes.append(hun)
        if track.id % 2 == 0:
            track.track_likes.append(kevin)
        if track.id % 3 == 0:
            track.track_likes.append(collin)
        
    db.session.commit()



    # print([track.to_dict() for track in tracks])

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

def undo_likes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.likes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM likes"))

    db.session.commit()
