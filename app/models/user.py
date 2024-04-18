from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .like import likes


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    artist_name = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date)

    tracks = db.relationship("Track", back_populates="user", cascade="all, delete-orphan")
    album = db.relationship("Album", back_populates="user", cascade="all, delete-orphan")
    user_likes = db.relationship("Track", secondary=likes, back_populates="track_likes")
    playlists = db.relationship("Playlist", back_populates="user")


    @property
    def password(self):
        return self.hashed_password

    # @password.setter
    # def password(self, password):
    #     self.hashed_password = generate_password_hash(password)
    @password.setter
    def password(self, password):
	# New code starts here #################
        if password == 'OAUTH':
            self.hashed_password = 'OAUTH' # If we look at the password_checker() method, we see that it hashes the user input and compares it
                        ## during login. With this adjustment, even a data breach would NOT expose our Oauth users to
                        ### having their accounts accessed with our default password for Oauth logins, 'OAUTH', as it would never
                        #### hash to that value.
            return
        # New code ends here ####################
        else:
            self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'artistName': self.artist_name,
            'name': self.name
        }

    def to_dict_name_only(self):
        return {
            'artistName': self.artist_name
        }

    def to_dict_with_user_likes(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'artistName': self.artist_name,
            'name': self.name,
            'userLikes': [track.to_dict() for track in self.user_likes]
        }
