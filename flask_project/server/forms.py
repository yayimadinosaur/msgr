from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
# from flask import render_template
# from wtforms.validators import DataRequired, Length, Email

class SignupForm(FlaskForm):
    first_name = StringField(
        'First Name', 
        [InputRequired()]
    )
    last_name = StringField(
        'Last Name', 
        [InputRequired()]
    )
    username = StringField(
        'Username',
        [
            InputRequired(),
            Length(min=3, message=('Minimum of 3 characters for Username'))
        ]
    )
    email = StringField(
        'Email',
        [
            Email(message=('Not a valid email')),
            InputRequired()
        ]
    )
    password = PasswordField(
        'Password',
        [
            Length(min=6,message=('Password is not long enough')),
            InputRequired(),
            EqualTo('confirm', message='Passwords must match')
        ]
    )
    confirm = PasswordField(
        'Repeat Password',
        [
            InputRequired(),
        ])
    submit = SubmitField('Submit')
    goback = SubmitField('Go back')

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            # InputRequired(),
            Length(min=1, message="Cannot be blank")
        ],
    )
    password = StringField(
        'Password',
        validators=[
            # InputRequired(),
            Length(min=1, message="Cannot be blank")
        ]
    )
    login = SubmitField('Login')
    signup = SubmitField('Signup')