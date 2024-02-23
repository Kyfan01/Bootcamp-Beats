from .db import db, add_prefix_for_prod


likes = db.Table(
    'likes',
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), primary_key=True),
    db.Column("track_id", db.Integer, db.ForeignKey(add_prefix_for_prod("tracks.id")), primary_key=True)
)
