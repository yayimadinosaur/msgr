from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
# from flask import render_template
# from wtforms.validators import DataRequired, Length, Email

#TODO   make check for special char, length, num requirement
def is_confirm_password(form, field):
    if form.data["password"] != form.data["confirm"]:
        raise ValidationError('Passwords must match omg')

class SignupForm(FlaskForm):
    #   change all input required to have css changes i.e. text to red to notify required parameters
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
    #   add a show password button to show password
    password = PasswordField(
        'Password',
        [
            #   change to hide password
            Length(min=6,message=('Password is not long enough, minimum 6 chars')),
            InputRequired(),
        ]
    )
    confirm = PasswordField(
        'Repeat Password',
        [
            # #   change to hide password
            # is_confirm_password,
            EqualTo('password', message='Passwords must match')
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
    password = PasswordField(
        'Password',
        validators=[
            # InputRequired(),
            Length(min=1, message="Cannot be blank")
        ]
    )
    login = SubmitField('Login')
    signup = SubmitField('Signup')