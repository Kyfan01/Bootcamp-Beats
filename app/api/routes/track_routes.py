from flask import Blueprint, jsonify, request
from app.models import Track, db, Album, User
from ...forms import NewTrackForm
from flask_login import current_user, login_required
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3

track_routes = Blueprint('tracks', __name__)

@track_routes.route('/')
def track_index():
    tracks = Track.query.order_by(Track.id.desc()).all()
    return {'tracks': [track.to_dict() for track in tracks]}

@track_routes.route('/<int:trackId>')
def track_details(trackId):
    track = Track.query.get(trackId)
    if (not track):
        return {"message": "Track not found"}
    return track.to_dict()

@track_routes.route('/user/<int:userId>')
def user_track_index(userId):
    tracks = Track.query.filter(Track.artist_id == userId).order_by(Track.id.desc()).all()
    if (not tracks):
        return {"message": "User tracks not found"}
    return {'tracks': [track.to_dict() for track in tracks]}

@track_routes.route('/albums/<int:albumId>')
def album_track_index(albumId):
    tracks = Track.query.filter(Track.album_id == albumId).order_by(Track.id.desc()).all()
    if (not tracks):
        return {"message": "Album tracks not found"}
    return {'tracks': [track.to_dict() for track in tracks]}

@track_routes.route('/', methods = ['POST'])
@login_required
def create_new_track():
    form = NewTrackForm()
    form.albumId.choices = [ (album.id, album.title) for album in Album.query.filter(Album.artist_id == current_user.id).all()]
    print('form data: ', form.data)
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        track = form.data["trackFile"]
        track.filename = get_unique_filename(track.filename)
        track_upload = upload_file_to_s3(track)

        preview_image = form.data["previewImage"]
        if (preview_image):
            preview_image.filename = get_unique_filename(preview_image.filename)
            preview_image_upload = upload_file_to_s3(preview_image)

        params = {
            'artist_id': current_user.id,
            'title': form.data['title'],
            'genre': form.data['genre'],
            'url': track_upload['url'],
            'duration': 123,
            'album_id': form.data['albumId'],
            'track_number': form.data['trackNumber'],
            'preview_image_url': preview_image_upload['url'] if preview_image else None
        }
        new_track = Track(**params)
        db.session.add(new_track)
        db.session.commit()
        return new_track.to_dict()

    return form.errors, 401

@track_routes.route('/<int:trackId>', methods = ['PUT'])
@login_required
def update_track(trackId):

    track = Track.query.get(trackId)

    if not track:
        return {"message": "Track not found"}

    if current_user.id != track.artist_id:
        return {"error": "You are not the owner of this track"}, 401


    form = NewTrackForm()
    form.albumId.choices = [ (album.id, album.title) for album in Album.query.filter(Album.artist_id == current_user.id).all()]
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        track = Track.query.get(trackId)

        if (form.data['previewImage']):
            remove_file_from_s3(track.preview_image_url) if '/' in track.preview_image_url else None

            updated_preview_image = form.data['previewImage']
            updated_preview_image.filename = get_unique_filename(updated_preview_image.filename)
            updated_preview_image_upload = upload_file_to_s3(updated_preview_image)
            # print(updated_preview_image_upload)
            track.preview_image_url = updated_preview_image_upload['url']

        if (form.data['trackFile']):
            remove_file_from_s3(track.url) if '/' in track.url else None

            updated_track = form.data['trackFile']
            updated_track.filename = get_unique_filename(updated_track.filename)
            updated_track_upload = upload_file_to_s3(updated_track)
            track.url = updated_track_upload['url']

        track.title = form.data['title']
        track.album_id = form.data['albumId']
        track.genre = form.data['genre']
        track.track_number = form.data['trackNumber']
        track.duration = 123321

        db.session.commit()
        return track.to_dict()

    return form.errors, 401

@track_routes.route('/<int:trackId>', methods = ['DELETE'])
@login_required
def delete_track(trackId):
    track = Track.query.get(trackId)

    if (not track):
        return {"message": "Track not found"}

    if current_user.id != track.artist_id:
        return {"error": "You are not the owner of this track",
                "current_user": current_user.id,
                "track artist": track.artist_id}, 401


    file_to_delete = remove_file_from_s3(track.url) if '/' in track.url else None

    # Needed because preview image is nullable, can't remove null
    if track.preview_image_url:
        image_to_delete = remove_file_from_s3(track.preview_image_url) if '/' in track.preview_image_url else None

    db.session.delete(track)
    db.session.commit()

    return {
       'message': 'Successfully deleted!'
    }

@track_routes.route('/<int:trackId>/like', methods=["PUT"])
@login_required
def like_track(trackId):
    track = Track.query.get(trackId)

    if (not track):
        return {"message": "Track not found"}

    current_user.user_likes.remove(track) if any(user.id == current_user.id for user in track.track_likes) else current_user.user_likes.append(track)

    db.session.commit()
    return track.to_dict()

# @track_routes.route('/<int:trackId>/unlike', methods=["POST"])
# def unlike_track(trackId):
#     track = Track.query.get(trackId)
#     current_user.user_likes.remove(track)
#     db.session.commit()
#     return current_user.to_dict_with_user_likes()
