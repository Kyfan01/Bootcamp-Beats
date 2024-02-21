from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, URL
from ..models import Album
from flask_login import current_user
from flask_wtf.file import FileField, FileRequired, FileAllowed
from ..api.routes.AWS_helpers import ALLOWED_AUDIO_EXTENSIONS, ALLOWED_IMAGE_EXTENSIONS


class NewTrackForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    albumId = SelectField('album_id', choices = [])
    genre = StringField('genre', validators=[DataRequired()])
    trackNumber = IntegerField('track_number')
    trackFile = FileField('track', validators=[FileRequired(), FileAllowed(list(ALLOWED_AUDIO_EXTENSIONS))]) #replaced url input
    previewImage = FileField('preview image', validators=[FileAllowed(list(ALLOWED_IMAGE_EXTENSIONS))])
