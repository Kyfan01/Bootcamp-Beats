# from flask_wtf import FlaskForm
# from wtforms import StringField, IntegerField, SelectField
# from wtforms.validators import DataRequired, URL
# from ..models.album import Album
# from flask_login import current_user

# albums = Album.query.filter(Album.artist_id == current_user.id).order_by(Album.id.desc()).all()
# choices = []

# for album in albums:
#     choices.append((album.id, album.title))

# class NewTrackForm(FlaskForm):
#     title = StringField('title', validators=[DataRequired()])
#     albumId = SelectField('albumId', choices = choices)
#     genre = StringField('genre', validators=[DataRequired()])
#     trackNumber = IntegerField('trackNumber')
#     url = StringField('url', validators=[DataRequired(), URL()])
#     previewImageUrl = StringField('url', validators=[URL()])
