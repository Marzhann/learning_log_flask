from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional


class LoginForm(FlaskForm):
    """User login form"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):
    """ A new user registration form """
    username = StringField('Username', validators=[DataRequired(), Length(min=4)])
    first_name = StringField('First Name', validators=[Optional()])
    last_name = StringField('Last Name', validators=[Optional()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Enter a valid email.')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message='Enter a stronger password.')])
    confirm_password = PasswordField('Confirm Your Password', validators=[DataRequired(), EqualTo('password', message='Passwords should match.')])
    submit = SubmitField('Register')