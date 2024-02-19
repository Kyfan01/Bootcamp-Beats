from flask import Blueprint, jsonify
from app.models import Album

album_routes = Blueprint('albums', __name__)

@album_routes.route('/')
def album_index():
    albums = Album.query.order_by(Album.id.desc()).all()
    # return f"{track.title for track in albums}"
    return {'albums': [album.to_dict() for album in albums]}
