from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    login = TextField('Login', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField("Send")
