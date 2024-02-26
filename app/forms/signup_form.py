from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')


class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), username_exists, Length(min=3, max=40)])
    artist_name = StringField('artist_name', validators=[DataRequired(), Length(min=1, max=50)])
    name = StringField('name', validators=[DataRequired(), Length(min=1, max=50)])
    email = EmailField('email', validators=[DataRequired(),user_exists, Length(min=5, max=50), Email()])
    password = StringField('password', validators=[DataRequired(), Length(min=5, max=50)])
