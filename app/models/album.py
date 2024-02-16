from .db import db, environment, SCHEMA, add_prefix_for_prod


class Album(db.Model):
    __tablename__ = 'albums'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    album_cover_url = db.Column(db.String(255), nullable=False)
    single = db.Column(db.Boolean, nullable=False)

    user = db.relationship("User", back_populates="albums")
    tracks = db.relationship("Track", back_populates="albums")


    def to_dict(self):
        return {
            'id': self.id,
            'artistId': self.artist_id,
            'title': self.title,
            'releaseDate': self.release_date,
            'genre': self.genre,
            'albumCoverUrl': self.album_cover_url,
            'single': self.single
        }
