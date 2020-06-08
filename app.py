from flask import Flask, render_template, request,session
from flask_mail import Mail, Message
from mongoengine import *
import bcrypt
from flask_pymongo import PyMongo 
#uncomment this when finish task 2.1
#from document import User
from login import LoginForm
#uncomment this when finish task 1.1
#from forms import RegisterForm
import local_setings




app = Flask(__name__,template_folder='template')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] ='Your Email@gmail.com'
app.config['MAIL_PASSWORD'] = local_setings.MAIL_PASSWORD 
app.config['MAIL_DEFAULT_SENDER'] = 'Your Email@gmail.com'
app.config['MAIL_MAX_EMAILS'] =  None
app.config['MAIL_ASCII_ATTACHMENTS'] = False
app.secret_key = 'development key'

mail = Mail (app)


# Task 2.3 start

# Task 2.3 end

@app.route('/')
def index():
    form=LoginForm()
    return render_template('login.html',form=form)



@app.route('/login', methods=['POST'])
def login():
        # Task 3.1 start 


        # Task 3.1 end


        if request.method == 'POST':
            # Task 3.2 start

            # Task 3.2 end
            
            if login_user:
                    if bcrypt.checkpw(request.form.get('password').encode('utf-8'), login_user['password'].encode('utf-8')): 
                        session['username'] = request.form['username']
                        return 'You are logged in as ' + session['username']

            return 'Invalid username/password combination'
    



@app.route('/signup', methods = ['GET', 'POST'])
def signup():

    # Task 1.3 start

    # Task 1.3 end

    if request.method =='POST':
        existing_user = User.objects.filter(username=request.form.get("username")).first()
        

        if existing_user is None:
            
            # Task 2.2 start
            
            # Task 2.2 end

            # uncomment this when finish Task 2.2
            #password=bcrypt.hashpw(request.form.get("password").encode('utf-8'),bcrypt.gensalt())
            #)

            user.save()  
            return 'you have successfully registerted, email would not be sent since email and password not provided'

            # Task 3.3 start
            
            # Task 3.3 end
            
            #  uncomment below when you have configured your Email accout and password to do Task 3.3  #
            
            #msg.html = ("<h2>Welcome! you have registered!</h2><b>\
            #</b><br><h4>In this session you will learn more about Flask</h4>"
             #   )
            #mail.send(msg)
            #return 'you have successfully registered, check your email!'
        return 'That username already exists!'
    return render_template('signup.html',form=form)






if __name__ =='__main__':
  app.run(debug=True)
