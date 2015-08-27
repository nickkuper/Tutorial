from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, SelectField, validators
#from wtforms.validators import Email, DataRequired, EqualTo

class BaseForm(Form):
	email = StringField('E-mail', [validators.Required()])
	password = PasswordField('Password', [validators.Required()])

class LoginForm(BaseForm):
	remember_me = BooleanField('remember_me', default = False)

class RegistrationForm(BaseForm):
	nickname = StringField('Nickname', [validators.Required()])
	confirm = PasswordField('Repeat password', [validators.EqualTo('password')])