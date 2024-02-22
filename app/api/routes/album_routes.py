from flask import Blueprint, jsonify, request
from app.models import Album, db
from app.forms import NewAlbumForm
from flask_login import current_user, login_required
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3

album_routes = Blueprint('albums', __name__)

@album_routes.route('/')
def album_index():
    albums = Album.query.order_by(Album.id.desc()).all()
    # return f"{track.title for track in albums}"
    return {'albums': [album.to_dict() for album in albums]}

@album_routes.route('/<int:albumId>')
def album_details(albumId):
    album = Album.query.get(albumId)
    return album.to_dict()

@album_routes.route('/user/<int:userId>')
def user_album_index(userId):
    albums = Album.query.filter(Album.artist_id == userId).order_by(Album.id.desc()).all()
    return {'albums': [album.to_dict() for album in albums]}

@album_routes.route('/', methods = ['POST'])
@login_required
def create_new_album():
    form = NewAlbumForm()
    print('album form data: ', form.data)
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        preview_image = form.data["albumCoverUrl"]
        preview_image.filename = get_unique_filename(preview_image.filename)
        preview_image_upload = upload_file_to_s3(preview_image)
        if "url" not in preview_image_upload:
            return {"message": "Album image file required"}

        params = {
            'artist_id': current_user.id,
            'title': form.data['title'],
            'genre': form.data['genre'],
            'album_cover_url': preview_image_upload['url'],
            'release_date': form.data['releaseDate']
        }
        new_album = Album(**params)
        db.session.add(new_album)
        db.session.commit()
        return new_album.to_dict()

    return form.errors, 401

@album_routes.route('/<int:albumId>', methods = ['PUT'])
@login_required
def update_album(albumId):
    form = NewAlbumForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        album = Album.query.get(albumId)

        if (form.data["albumCoverUrl"]): 
            remove_file_from_s3(album.album_cover_url) if '/' in album.album_cover_url else None

            updated_album_cover = form.data["albumCoverUrl"]
            updated_album_cover.filename = get_unique_filename(updated_album_cover.filename)
            updated_album_cover_upload = upload_file_to_s3(updated_album_cover)
            print(updated_album_cover_upload)
            album.albumCoverUrl = updated_album_cover_upload['url']

        album.title = form.data['title']
        album.genre = form.data['genre']
        album.release_date = form.data['releaseDate']

        db.session.commit()
        return album.to_dict()

    return form.errors, 401

@album_routes.route('/<int:albumId>', methods = ['DELETE'])
@login_required
def delete_album(albumId):
    album = Album.query.get(albumId)
    db.session.delete(album)
    db.session.commit()

    image_to_delete = remove_file_from_s3(album.album_cover_url) if '/' in album.album_cover_url else None

    return {
       'message': 'Successfully deleted!'
    }
