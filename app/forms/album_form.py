from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired, URL, Length
from ..models import Album
from flask_login import current_user


class NewAlbumForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=1, max=50)])
    releaseDate = DateField('releaseDate', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired(), Length(min=1, max=50)])
    albumCoverUrl = StringField('albumCoverUrl')
