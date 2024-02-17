from flask import Blueprint, jsonify
from app.models import Track

track_routes = Blueprint('tracks', __name__)

@track_routes.route('/')
def track_index():
    tracks = Track.query.order_by(Track.id.desc()).all()
    # return f"{track.title for track in tracks}"
    return {'tracks': [track.to_dict() for track in tracks]}
