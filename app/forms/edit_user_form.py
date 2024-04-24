from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import User
from flask_login import current_user


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

def same_username(form, field):
    # Checks if form user is the current user
    username = field.data
    user = User.query.filter(User.username == username).first()
    if (user and user.username != current_user.username):
        raise ValidationError('Username is already in use.')

def same_email(form, field):
    # Checks if form user is the current user
    email = field.data
    user = User.query.filter(User.email == email).first()
    if (user and user.email != current_user.email):
        raise ValidationError('Email is already in use.')


def same_artist_name(form, field):
    # Checks if form user is the current user
    artist_name = field.data
    user = User.query.filter(User.artist_name == artist_name).first()
    if (user and user.artist_name != current_user.artist_name):
        raise ValidationError('Artist name is already in use.')



class EditUserForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), same_username, Length(min=3, max=40)])
    artist_name = StringField('artist_name', validators=[DataRequired(), same_artist_name,Length(min=1, max=50)])
    name = StringField('name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('email', validators=[DataRequired(), same_email, Length(min=5, max=50)])
