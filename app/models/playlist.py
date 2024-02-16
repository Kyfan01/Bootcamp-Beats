from .db import db, environment, SCHEMA, add_prefix_for_prod
from .like import likes


class Playlist(db.Model):
    __tablename__ = 'playlists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    createdAt = db.Column(db.String(255), nullable=False)
    updatedAt = db.Column(db.String(255), nullable=False)

    user = db.relationship("User", back_poplates="playlists")
    


    def to_dict(self):
        return {
            'id': self.id,
            'artistId': self.artist_id,
            'albumId': self.album_id,
            'title': self.title,
            'duration': self.duration,
            'genre': self.genre,
            'trackNumber': self.track_number,
            'url': self.url,
            'previewImageUrl': self.preview_image_url,
            'artistName': self.user.to_dict_name_only().get('artistName')
        }
