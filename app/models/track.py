from .db import db, environment, SCHEMA, add_prefix_for_prod
from .like import likes
from flask_login import current_user
from flask import jsonify


class Track(db.Model):
    __tablename__ = 'tracks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('albums.id')))
    title = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    track_number = db.Column(db.Integer)
    url = db.Column(db.String(255), nullable=False)
    preview_image_url = db.Column(db.String(255))

    user = db.relationship("User", back_populates="tracks")
    album = db.relationship("Album", back_populates="tracks")
    track_likes = db.relationship("User", secondary=likes, back_populates="user_likes")



    def to_dict(self):
        print(self.album)
        return {
            'id': self.id,
            'artistId': self.artist_id,
            'albumId': self.album_id,
            'albumTitle': self.album.title if self.album else None,
            'title': self.title,
            'duration': self.duration,
            'genre': self.genre,
            'trackNumber': self.track_number,
            'url': self.url,
            'previewImageUrl': self.preview_image_url,
            'artistName': self.user.to_dict_name_only().get('artistName'),
            'trackLikes': len(self.track_likes),
            'liked': any(user.id == current_user.id for user in self.track_likes) if current_user.is_authenticated else False
        }
