from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
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