from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired, URL
from ..models import Album
from flask_login import current_user

# albums = []
# for album in albums:
#     album_choices.append((album.id, album.title))



class NewAlbumForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    releaseDate = DateField('releaseDate', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
    albumCoverUrl = StringField('albumCoverUrl', validators=[DataRequired()])
