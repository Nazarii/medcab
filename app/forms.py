from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    login = TextField('Login', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    # remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField("Send")
