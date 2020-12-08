from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField, PasswordField, StringField, SubmitField, validators, BooleanField, RadioField, SelectField, IntegerField
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


class RadioChoiceForm(FlaskForm):
    radio = RadioField('choice', choices=[('person', 'Person'), ('company', 'Company')], default='person')
    submit = SubmitField('Submit')


class DeleteCoupon(FlaskForm):

    uuid_name = StringField('uuid_name', validators=[DataRequired()])
    submit_delete = SubmitField('Delete')


class AddCoupon(FlaskForm):

    prime_category = SelectField(choices=['Mens', 'Women', 'Children'])
    sub_category = SelectField(choices=['None', ])

    brand = StringField(validators=[DataRequired()])
    color = StringField(validators=[DataRequired()])
    price = StringField(validators=[DataRequired()])
    style = StringField(validators=[DataRequired()])
    min_p = IntegerField(validators=[DataRequired()])
    max_p = IntegerField(validators=[DataRequired()])
    submit_add = SubmitField('Add')

    def __init__(self, primary_cat: list, sub_cat: list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if primary_cat:
            self.prime_category.choices = primary_cat
        if sub_cat:
            self.sub_category.choices = sub_cat


class RegisterPersonForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.DataRequired(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', [validators.DataRequired()])
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField('Submit')


class RegisterCompanyForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    companyname = StringField('Company name', [validators.Length(min=4, max=25)])
    websiteurl = StringField('Website URL', [validators.Length(min=6, max=100)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', [validators.DataRequired()])
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField('Submit')


# class PrefForm(FlaskForm):
#     prime_boolean = BooleanField()
#     sub_boolean = BooleanField()
#
#     def __init__(self, primary_cat: list, sub_cat: list, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if primary_cat:
#             self.prime_category.choices = primary_cat
#         if sub_cat:
#             self.sub_category.choices = sub_cat
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class PreferenceForm(FlaskForm):
    preferences = MultiCheckboxField('Primary', coerce=int, choices=[(1, 'one')], validators=[] )

    submit = SubmitField('submit')
