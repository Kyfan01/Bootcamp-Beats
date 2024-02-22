from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired, URL
from ..models import Album
from flask_login import current_user


class NewAlbumForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    releaseDate = DateField('releaseDate', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
    albumCoverUrl = StringField('albumCoverUrl')
