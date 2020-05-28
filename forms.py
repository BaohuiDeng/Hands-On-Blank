from flask_wtf import Form
from wtforms import TextField, StringField, PasswordField, SubmitField


#
class RegisterForm(Form):
    
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Register')





