from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, URL, Length
from ..models import Album
from flask_login import current_user
from flask_wtf.file import FileField, FileRequired, FileAllowed
from ..api.routes.AWS_helpers import ALLOWED_AUDIO_EXTENSIONS, ALLOWED_IMAGE_EXTENSIONS


class NewTrackForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=1, max=50)])
    albumId = SelectField('album_id', choices = [])
    genre = StringField('genre', validators=[DataRequired(), Length(min=1, max=50)])
    trackNumber = IntegerField('track_number')
    trackFile = FileField('track', validators=[FileAllowed(list(ALLOWED_AUDIO_EXTENSIONS))])
    previewImage = FileField('preview image', validators=[FileAllowed(list(ALLOWED_IMAGE_EXTENSIONS))])
