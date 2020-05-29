from flask_wtf import Form
from wtforms import TextField, StringField, PasswordField, SubmitField


<<<<<<< HEAD
# Task 1.1 start 

# Task 1.1 end
=======
#
class RegisterForm(Form):
    
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Register')
>>>>>>> d215739b43a819c5863e31460a4f182d27dda5e8





