from app.models import db, Track, environment, SCHEMA
from sqlalchemy.sql import text


def seed_tracks(hun, kevin, collin, demo, kevinMacLeod):
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
        # Track(artist_id = 3, album_id = 1, title = 'Data Drive', duration = 300, genre = 'EDM', track_number = 1, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-1.m4a', preview_image_url = album_image_1),
        # Track(artist_id = 3, album_id = 1, title = 'Digital Dreams', duration = 291, genre = 'EDM', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-2.m4a', preview_image_url = album_image_1),
        # Track(artist_id = 3, album_id = 1, title = 'Code Jam', duration = 201, genre = 'Pop', track_number = 3, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-3.m4a', preview_image_url = album_image_1),
        # Track(artist_id = 3, album_id = 1, title = 'Syntax Symphony', duration = 224, genre = 'Pop', track_number = 4, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-4.m4a', preview_image_url = album_image_1),
        # Track(artist_id = 3, album_id = 5, title = 'Binary Boogie', duration = 196, genre = 'Pop', track_number = 5, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-5.m4a', preview_image_url = album_image_2),
        # Track(artist_id = 3, album_id = 5, title = 'Byte-Sized Beats', duration = 213, genre = 'Pop', track_number = 6, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-6.m4a', preview_image_url = album_image_2),
        # Track(artist_id = 3, album_id = 5, title = 'Loop Logic', duration = 198, genre = 'Pop', track_number = 7, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-7.m4a', preview_image_url = album_image_2 ),
        # Track(artist_id = 3, album_id = 6, title = 'Pixel Pulse', duration = 189, genre = 'Pop', track_number = 8, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-8.m4a', preview_image_url = album_image_3),
        # Track(artist_id = 3, album_id = 6, title = 'Bit Bounce', duration = 199, genre = 'Pop', track_number = 9, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-9.m4a', preview_image_url = album_image_3),
        # Track(artist_id = 3, album_id = 6, title = 'Cybernetic Serenade', duration = 214, genre = 'Pop', track_number = 10, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-10.m4a', preview_image_url = album_image_3),
        
        # Track(artist_id = 3, album_id = 7, title = 'ByteBeat Boogie', duration = 214, genre = 'Dance', track_number = 1, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-13.mp3', preview_image_url = album_image_7),
        # Track(artist_id = 3, album_id = 7, title = 'Algorithmic Anthem', duration = 214, genre = 'Dance', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-14.mp3', preview_image_url = album_image_7),
        # Track(artist_id = 3, album_id = 7, title = 'Groove Generator', duration = 214, genre = 'Dance', track_number = 3, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-15.mp3', preview_image_url = album_image_7),
        # Track(artist_id = 3, album_id = 7, title = 'Synthwave Surge', duration = 214, genre = 'Dance', track_number = 4, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-16.mp3', preview_image_url = album_image_7),
        # Track(artist_id = 3, album_id = 7, title = 'Electro Evolution', duration = 214, genre = 'Dance', track_number = 5, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-17.mp3', preview_image_url = album_image_7),
        # Track(artist_id = 3, album_id = 7, title = 'Techno Trance', duration = 214, genre = 'Dance', track_number = 6, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-18.mp3', preview_image_url = album_image_7),
        # Track(artist_id = 3, album_id = 7, title = 'Virtual Vibrations', duration = 214, genre = 'Dance', track_number = 7, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-19.mp3', preview_image_url = album_image_7),
        # Track(artist_id = 3, album_id = 7, title = 'Rhythm Rift', duration = 214, genre = 'Dance', track_number = 8, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-20.mp3', preview_image_url = album_image_7),
        # Track(artist_id = 3, album_id = 7, title = 'Quantum Quake', duration = 214, genre = 'Dance', track_number = 9, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-21.mp3', preview_image_url = album_image_7),
        # Track(artist_id = 3, album_id = 7, title = 'Synthwave Supernova', duration = 214, genre = 'Dance', track_number = 10, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-22.mp3', preview_image_url = album_image_7),

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
        # Track(artist_id = 2, album_id = 3, title = 'Genesis', duration = 234, genre = 'EDM', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/genesis.mp3', preview_image_url = album_image_4),
        # Track(artist_id = 2, album_id = 4, title = 'Technologic', duration = 284, genre = 'EDM', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/technologic.mp3', preview_image_url = album_image_5),

        # Track(artist_id = 2, album_id = 3, title = 'D.A.N.C.E.', duration = 214, genre = 'EDM', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/cross-dance.mp3', preview_image_url = album_image_4),
        # Track(artist_id = 2, album_id = 3, title = 'Waters of Nazareth', duration = 214, genre = 'EDM', track_number = 3, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/cross-waters-of-nazareth.mp3', preview_image_url = album_image_4),
        # Track(artist_id = 2, album_id = 3, title = 'One Minute to Midnight', duration = 214, genre = 'EDM', track_number = 4, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/cross-one-minute-to-midnight.mp3', preview_image_url = album_image_4),

        # Track(artist_id = 2, album_id = 8, title = 'Jasmine', duration = 214, genre = 'EDM', track_number = 1, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/her-jasmine.mp3', preview_image_url = album_image_8),
        # Track(artist_id = 2, album_id = 8, title = 'Martini Blue', duration = 214, genre = 'EDM', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/her-martini-blue.mp3', preview_image_url = album_image_8),
        # Track(artist_id = 2, album_id = 8, title = 'Text Me', duration = 214, genre = 'EDM', track_number = 3, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/her-text-me.mp3', preview_image_url = album_image_8),

        # Track(artist_id = 2, album_id = 9, title = 'Don\'t Go Insane', duration = 214, genre = 'EDM', track_number = 1, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/mito-dont-go-insane.mp3', preview_image_url = album_image_9),
        # Track(artist_id = 2, album_id = 9, title = 'No Blueberries', duration = 214, genre = 'EDM', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/mito-no-blueberries.mp3', preview_image_url = album_image_9),
        # Track(artist_id = 2, album_id = 9, title = 'Nerves', duration = 214, genre = 'EDM', track_number = 3, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/mito-nerves.mp3', preview_image_url = album_image_9),

    # hun
        # Track(artist_id = 1, album_id = 2, title = "World's smallest violin", duration = 240, genre = 'Pop', track_number = 1, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-11.m4a', preview_image_url = album_image_6),
        # Track(artist_id = 1, album_id = 2, title = "Bang!", duration = 171, genre = 'Pop', track_number = 2, url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-track-12.m4a', preview_image_url = album_image_6)
    
    # kevin macleod
        Track(artist_id = 4, album_id = 1, title = "Aurea Carmina", duration = 171, genre = 'Disco', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Aurea+Carmina.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-disco.png'),
        Track(artist_id = 4, album_id = 1, title = "Disco con Tutti", duration = 171, genre = 'Disco', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Disco+con+Tutti.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-disco.png'),
        Track(artist_id = 4, album_id = 1, title = "Disco Lounge", duration = 171, genre = 'Disco', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Disco+Lounge.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-disco.png'),
        Track(artist_id = 4, album_id = 1, title = "Disco Medusae", duration = 171, genre = 'Disco', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Disco+Medusae.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-disco.png'),
        Track(artist_id = 4, album_id = 1, title = "Electro Cabello", duration = 171, genre = 'Disco', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Electro+Cabello.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-disco.png'),
        Track(artist_id = 4, album_id = 1, title = "Ether Disco", duration = 171, genre = 'Disco', track_number = 6, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Ether+Disco.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-disco.png'),
        Track(artist_id = 4, album_id = 1, title = "Overcast", duration = 171, genre = 'Disco', track_number = 7, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Overcast.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-disco.png'),
        Track(artist_id = 4, album_id = 1, title = "Realizer", duration = 171, genre = 'Disco', track_number = 8, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Realizer.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-disco.png'),
        Track(artist_id = 4, album_id = 1, title = "Stringed Disco", duration = 171, genre = 'Disco', track_number = 9, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Stringed+Disco.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-disco.png'),
        Track(artist_id = 4, album_id = 1, title = "Who Likes to Party", duration = 171, genre = 'Disco', track_number = 10, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Who+Likes+to+Party.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-disco.png'),

        Track(artist_id = 4, album_id = 2, title = "Bleeping Demo", duration = 171, genre = 'Electronica', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Bleeping+Demo.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-1.png'),
        Track(artist_id = 4, album_id = 2, title = "Blippy Trance", duration = 171, genre = 'Electronica', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Blippy+Trance.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-1.png'),
        Track(artist_id = 4, album_id = 2, title = "Brain Dance", duration = 171, genre = 'Electronica', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Brain+Dance.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-1.png'),
        Track(artist_id = 4, album_id = 2, title = "Cloud Dancer", duration = 171, genre = 'Electronica', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Cloud+Dancer.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-1.png'),
        Track(artist_id = 4, album_id = 2, title = "Equatorial Complex", duration = 171, genre = 'Electronica', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Equatorial+Complex.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-1.png'),

        Track(artist_id = 4, album_id = 3, title = "Ethernight Club", duration = 171, genre = 'Electronica', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Ethernight+Club.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-2.png'),
        Track(artist_id = 4, album_id = 3, title = "Galactic Rap", duration = 171, genre = 'Electronica', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Galactic+Rap.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-2.png'),
        Track(artist_id = 4, album_id = 3, title = "Mesmerizing Galaxy Loop", duration = 171, genre = 'Electronica', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Mesmerizing+Galaxy+Loop.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-2.png'),
        Track(artist_id = 4, album_id = 3, title = "Newer Wave", duration = 171, genre = 'Electronica', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Newer+Wave.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-2.png'),
        Track(artist_id = 4, album_id = 3, title = "Voxel Revolution", duration = 171, genre = 'Electronica', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Voxel+Revolution.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-2.png'),

        Track(artist_id = 4, album_id = 4, title = "Celebration", duration = 171, genre = 'Funk', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Celebration.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-1.png'),
        Track(artist_id = 4, album_id = 4, title = "Chill Wave", duration = 171, genre = 'Funk', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Chill+Wave.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-1.png'),
        Track(artist_id = 4, album_id = 4, title = "District Four", duration = 171, genre = 'Funk', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/District+Four.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-1.png'),
        Track(artist_id = 4, album_id = 4, title = "Funky Boxstep ", duration = 171, genre = 'Funk', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Funky+Boxstep+.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-1.png'),
        Track(artist_id = 4, album_id = 4, title = "I Got a Stick Arr Bryan Teoh", duration = 171, genre = 'Funk', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/I+Got+a+Stick+Arr+Bryan+Teoh.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-1.png'),

        Track(artist_id = 4, album_id = 5, title = "I Got a Stick Feat James Gavins", duration = 171, genre = 'Funk', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/I+Got+a+Stick+Feat+James+Gavins.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-2.png'),
        Track(artist_id = 4, album_id = 5, title = "Loopster", duration = 171, genre = 'Funk', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Loopster.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-2.png'),
        Track(artist_id = 4, album_id = 5, title = "Miami Viceroy", duration = 171, genre = 'Funk', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Miami+Viceroy.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-2.png'),
        Track(artist_id = 4, album_id = 5, title = "Shaving Mirror", duration = 171, genre = 'Funk', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Shaving+Mirror.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-2.png'),
        Track(artist_id = 4, album_id = 5, title = "ZigZag", duration = 171, genre = 'Funk', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/ZigZag.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-2.png'),

        Track(artist_id = 4, album_id = 6, title = "Deuces", duration = 171, genre = 'Jazz', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Deuces.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-1.png'),
        Track(artist_id = 4, album_id = 6, title = "Fuzzball Parade", duration = 171, genre = 'Jazz', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Fuzzball+Parade.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-1.png'),
        Track(artist_id = 4, album_id = 6, title = "Hard Boiled", duration = 171, genre = 'Jazz', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Hard+Boiled.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-1.png'),
        Track(artist_id = 4, album_id = 6, title = "Night in Venice", duration = 171, genre = 'Jazz', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Night+in+Venice.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-1.png'),
        Track(artist_id = 4, album_id = 6, title = "On Hold for You", duration = 171, genre = 'Jazz', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/On+Hold+for+You.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-1.png'),

        Track(artist_id = 4, album_id = 7, title = "Past Sadness", duration = 171, genre = 'Jazz', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Past+Sadness.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-2.png'),
        Track(artist_id = 4, album_id = 7, title = "Smooth Lovin", duration = 171, genre = 'Jazz', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Smooth+Lovin.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-2.png'),
        Track(artist_id = 4, album_id = 7, title = "Space Jazz", duration = 171, genre = 'Jazz', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Space+Jazz.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-2.png'),
        Track(artist_id = 4, album_id = 7, title = "Study And Relax", duration = 171, genre = 'Jazz', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Study+And+Relax.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-2.png'),
        Track(artist_id = 4, album_id = 7, title = "Vibing Over Venus", duration = 171, genre = 'Jazz', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Vibing+Over+Venus.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-2.png'),

        Track(artist_id = 4, album_id = 8, title = "Colorless Aura", duration = 171, genre = 'Modern', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Colorless+Aura.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-1.png'),
        Track(artist_id = 4, album_id = 8, title = "Decisions", duration = 171, genre = 'Modern', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Decisions.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-1.png'),
        Track(artist_id = 4, album_id = 8, title = "Inexorable", duration = 171, genre = 'Modern', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Inexorable.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-1.png'),
        Track(artist_id = 4, album_id = 8, title = "Junkyard Tribe", duration = 171, genre = 'Modern', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Junkyard+Tribe.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-1.png'),
        Track(artist_id = 4, album_id = 8, title = "Magic Scout - Cottages", duration = 171, genre = 'Modern', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Magic+Scout+-+Cottages.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-1.png'),

        Track(artist_id = 4, album_id = 9, title = "Magic Scout - Farm", duration = 171, genre = 'Modern', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Magic+Scout+-+Farm.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-2.png'),
        Track(artist_id = 4, album_id = 9, title = "Magic Scout - Manor", duration = 171, genre = 'Modern', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Magic+Scout+-+Manor.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-2.png'),
        Track(artist_id = 4, album_id = 9, title = "Magic Scout - Nothern Glade", duration = 171, genre = 'Modern', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Magic+Scout+-+Nothern+Glade.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-2.png'),
        Track(artist_id = 4, album_id = 9, title = "Master Disorder", duration = 171, genre = 'Modern', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Master+Disorder.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-2.png'),
        Track(artist_id = 4, album_id = 9, title = "Vanes", duration = 171, genre = 'Modern', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Vanes.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-2.png'),

        Track(artist_id = 4, album_id = 10, title = "Aerosol of my Love", duration = 171, genre = 'Pop', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Aerosol+of+my+Love.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-1.png'),
        Track(artist_id = 4, album_id = 10, title = "Android Sock Hop", duration = 171, genre = 'Pop', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Android+Sock+Hop.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-1.png'),
        Track(artist_id = 4, album_id = 10, title = "Basic Implosion", duration = 171, genre = 'Pop', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Basic+Implosion.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-1.png'),
        Track(artist_id = 4, album_id = 10, title = "Blown Away", duration = 171, genre = 'Pop', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Blown+Away.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-1.png'),
        Track(artist_id = 4, album_id = 10, title = "Bummin on Tremelo", duration = 171, genre = 'Pop', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Bummin+on+Tremelo.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-1.png'),

        Track(artist_id = 4, album_id = 11, title = "Glitter Blast", duration = 171, genre = 'Pop', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Glitter+Blast.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-2.png'),
        Track(artist_id = 4, album_id = 11, title = "Guts and Bourbon", duration = 171, genre = 'Pop', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Guts+and+Bourbon.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-2.png'),
        Track(artist_id = 4, album_id = 11, title = "Life of Riley", duration = 171, genre = 'Pop', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Life+of+Riley.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-2.png'),
        Track(artist_id = 4, album_id = 11, title = "Pyro Flow", duration = 171, genre = 'Pop', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Pyro+Flow.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-2.png'),
        Track(artist_id = 4, album_id = 11, title = "Werq", duration = 171, genre = 'Pop', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Werq.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-2.png'),

        Track(artist_id = 4, album_id = 12, title = "Boogie Party", duration = 171, genre = 'Rock', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Boogie+Party.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-1.png'),
        Track(artist_id = 4, album_id = 12, title = "Burn The World Waltz", duration = 171, genre = 'Rock', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Burn+The+World+Waltz+.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-1.png'),
        Track(artist_id = 4, album_id = 12, title = "Fantasia Fantasia", duration = 171, genre = 'Rock', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Fantasia+Fantasia.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-1.png'),
        Track(artist_id = 4, album_id = 12, title = "Feral Angel Waltz", duration = 171, genre = 'Rock', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Feral+Angel+Waltz+.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-1.png'),
        Track(artist_id = 4, album_id = 12, title = "Funin and Sunin", duration = 171, genre = 'Rock', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Funin+and+Sunin.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-1.png'),

        Track(artist_id = 4, album_id = 13, title = "Metalmania", duration = 171, genre = 'Rock', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Metalmania.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-2.png'),
        Track(artist_id = 4, album_id = 13, title = "Motherlode", duration = 171, genre = 'Rock', track_number = 2, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Motherlode.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-2.png'),
        Track(artist_id = 4, album_id = 13, title = "Ready Aim Fire", duration = 171, genre = 'Rock', track_number = 3, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Ready+Aim+Fire.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-2.png'),
        Track(artist_id = 4, album_id = 13, title = "Surf Shimmy", duration = 171, genre = 'Rock', track_number = 4, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Surf+Shimmy.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-2.png'),
        Track(artist_id = 4, album_id = 13, title = "Waltz Primordial", duration = 171, genre = 'Rock', track_number = 5, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Waltz+Primordial+.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-2.png'),

        Track(artist_id = 4, album_id = 14, title = "Blobby Samba", duration = 171, genre = 'Misc', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Blobby+Samba.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-single-1.png'),
        Track(artist_id = 4, album_id = 15, title = "Chillin Hard", duration = 171, genre = 'Misc', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Chillin+Hard.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-single-2.png'),
        Track(artist_id = 4, album_id = 16, title = "Grand Dark Waltz Trio Vivace", duration = 171, genre = 'Misc', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Grand+Dark+Waltz+Trio+Vivace.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-single-3.png'),
        Track(artist_id = 4, album_id = 17, title = "Nano Hoedown", duration = 171, genre = 'Misc', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Nano+Hoedown.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-single-4.png'),
        Track(artist_id = 4, album_id = 18, title = "Slow Jam", duration = 171, genre = 'Misc', track_number = 1, url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/Slow+Jam.mp3', preview_image_url ='https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-single-5.png'),

       
       
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
        if track.id % 4 == 0:
            track.track_likes.append(kevinMacLeod)
        
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
