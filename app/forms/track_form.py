from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, URL
from ..models import Album
from flask_login import current_user
from flask_wtf.file import FileField, FileRequired, FileAllowed
from ..api.routes.AWS_helpers import ALLOWED_AUDIO_EXTENSIONS, ALLOWED_IMAGE_EXTENSIONS

# albums = []
# for album in albums:
#     album_choices.append((album.id, album.title))



class NewTrackForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    albumId = SelectField('album_id', choices = [])
    genre = StringField('genre', validators=[DataRequired()])
    trackNumber = IntegerField('track_number')
    # url = StringField('url', validators=[DataRequired()])
    trackFile = FileField('track', validators=[FileRequired(), FileAllowed(list(ALLOWED_AUDIO_EXTENSIONS))]) #replaced url input
    # previewImageUrl = StringField('url')
    previewImage = FileField('preview image', validators=[FileAllowed(list(ALLOWED_IMAGE_EXTENSIONS))])
