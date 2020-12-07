from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):

    username = StringField(
        'Name',
        [DataRequired()]
    )

    password = PasswordField(
        'Password',
        [DataRequired()]
    )

    submit = SubmitField('Submit')


class RegisterPersonForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


class RegisterCompany(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    companyname = StringField('Company name', [validators.Length(min=4, max=25)])
    websiteurl = StringField('Website URL', [validators.Length(min=6, max=100)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
