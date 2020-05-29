from flask import Flask, render_template, request
from flask_mail import Mail, Message
from mongoengine import *
import bcrypt

#uncommet this when finished Task 2.1
# from document import User
from login import LoginForm
# uncomment this when finished Task 1.1 #
#from forms import RegisterForm
import local_setings




app = Flask(__name__,template_folder='template')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] ='your@gmail.com'
app.config['MAIL_PASSWORD'] = local_setings.MAIL_PASSWORD 
app.config['MAIL_DEFAULT_SENDER'] = 'your@gmail.com'
app.config['MAIL_MAX_EMAILS'] =  None
app.config['MAIL_ASCII_ATTACHMENTS'] = False
app.secret_key = 'development key'

mail = Mail (app)

#Task 2.3 start


#Task 2.3 end

@app.route('/')
def index():
    form=LoginForm()
    return render_template('login.html',form=form)




@app.route('/login', methods=['POST'])
def login():
  
    
        if request.method == 'POST':
               login_user = User.objects.filter(username=request.form.get("username")).first()

        if login_user:
                            if bcrypt.hashpw(request.form.get('password').encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                             l = login_user.save()
                             return '<h4>Welcome! You are logged in as </h4>' + l['username'] 
        return 'Invalid username/password combination'
    



@app.route('/signup', methods = ['GET', 'POST'])
def signup():
     # Task 1.2 start

    #Task 1.2 end
    if request.method =='POST':
        existing_user = User.objects.filter(username=request.form.get("username")).first()
        

        if existing_user is None:
            #Task 2.2 start
            
            #password=bcrypt.hashpw(request.form.get("password").encode('utf-8'),bcrypt.gensalt())
            #)
            #Task 2.2 end
            
            user.save()
              
            #Task 3.1 start

            #Task 3.1 end
            
            return 'you have successfully registered, check your email!'
        return 'That username already exists!'
    return render_template('signup.html',form=form)






if __name__ =='__main__':
  app.run(debug=True)