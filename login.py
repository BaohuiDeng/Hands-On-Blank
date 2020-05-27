from flask_wtf import Form
from wtforms import TextField, StringField, PasswordField, SubmitField



class LoginForm(Form):
    
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Log In')



