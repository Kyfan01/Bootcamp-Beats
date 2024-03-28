from app.models import db, Album, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date

def seed_albums():
    test_image_url = 'https://bootcampbeats-tracks.s3.amazonaws.com/4ddbd8fa75ef47b8814d594183c0bffd.jpg'
    albums = [

        # Album(artist_id = 3, title = 'Binary Grooves: The DJ ByteBeat Collection', release_date= date(1997, 12, 4), genre = 'Pop', album_cover_url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-1.jpg'),
        # Album(artist_id = 1, title = 'Metronome', release_date= date(1997, 12, 4), genre = 'Pop', album_cover_url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-6.jpg'),
        # Album(artist_id = 2, title = 'Cross', release_date= date(1997, 12, 4), genre = 'EDM', album_cover_url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-4.jpg'),
        # Album(artist_id = 2, title = 'Human After All', release_date= date(2005, 12, 4), genre = 'Electronica', album_cover_url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-5.jpg'),
        # Album(artist_id = 3, title = 'Binary Grooves: The DJ ByteBeat Collection 2', release_date= date(1998, 12, 4), genre = 'Pop', album_cover_url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-2.jpg'),
        # Album(artist_id = 3, title = 'Binary Grooves: The DJ ByteBeat Collection 3', release_date= date(1999, 12, 4), genre = 'Pop', album_cover_url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-3.jpg'),
        # Album(artist_id = 3, title = 'Binary Grooves: The DJ ByteBeat Collection 4', release_date= date(2000, 12, 4), genre = 'Dance', album_cover_url = 'https://bootcampbeats-tracks.s3.amazonaws.com/seeder-album-7.jpg'),
        # Album(artist_id = 2, title = 'Her', release_date= date(2017, 12, 7), genre = 'EDM', album_cover_url = 'https://bootcampbeats-tracks.s3.amazonaws.com/her-album-cover.jpg'),
        # Album(artist_id = 2, title = 'Moodswings in to Order', release_date= date(2022, 7, 29), genre = 'EDM', album_cover_url = 'https://bootcampbeats-tracks.s3.amazonaws.com/mito-album-cover.jpg')


        Album(artist_id = 5, title = 'Kevin MacLeod Disco', release_date= date(2022, 7, 29), genre = 'Disco', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-disco.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Electronica - Part One', release_date= date(2022, 7, 29), genre = 'Electronica', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-1.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Electronica - Part Two', release_date= date(2022, 7, 29), genre = 'Electronica', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-electronica-2.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Funk - Part One', release_date= date(2022, 7, 29), genre = 'Funk', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-1.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Funk - Part Two', release_date= date(2022, 7, 29), genre = 'Funk', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-funk-2.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Jazz - Part One', release_date= date(2022, 7, 29), genre = 'Jazz', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-1.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Jazz - Part Two', release_date= date(2022, 7, 29), genre = 'Jazz', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-jazz-2.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Modern - Part One', release_date= date(2022, 7, 29), genre = 'Modern', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-1.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Modern - Part Two', release_date= date(2022, 7, 29), genre = 'Modern', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-modern-2.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Pop - Part One', release_date= date(2022, 7, 29), genre = 'Pop', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-1.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Pop - Part Two', release_date= date(2022, 7, 29), genre = 'Pop', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-pop-2.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Rock - Part One', release_date= date(2022, 7, 29), genre = 'Rock', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-1.png'),
        Album(artist_id = 5, title = 'Kevin MacLeod Rock - Part Two', release_date= date(2022, 7, 29), genre = 'Rock', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-rock-2.png'),
        Album(artist_id = 5, title = 'Blobby Samba - Single', release_date= date(2022, 7, 29), genre = 'Misc', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-single-1.png'),
        Album(artist_id = 5, title = 'Chillin Hard - Single', release_date= date(2022, 7, 29), genre = 'Misc', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-single-2.png'),
        Album(artist_id = 5, title = 'Grand Dark Waltz Trio Vivace - Single', release_date= date(2022, 7, 29), genre = 'Misc', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-single-3.png'),
        Album(artist_id = 5, title = 'Nano Hoedown - Single', release_date= date(2022, 7, 29), genre = 'Misc', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-single-4.png'),
        Album(artist_id = 5, title = 'Slow Jam - Single', release_date= date(2022, 7, 29), genre = 'Misc', album_cover_url = 'https://bootcampbeats-tracks.s3.us-east-2.amazonaws.com/album-cover-single-5.png'),







    ]

    db.session.add_all(albums)
    db.session.commit()

def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))

    db.session.commit()
