from . import main
from flask import render_template,flash,redirect,url_for
from  .forms import LoginForm,RegistrationForm
from app import request
from app.models import User
 
@main.route('/')
@main.route('/index')
def index():
    user = {'username': 'Hey there Get to see and review your top favorite books at the comfort of your couch'}
    users = {'usersname':'Already have an account ?'}
    return render_template('index.html',user =user,users=users)

@main.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User(form.username.data,form.email.data,form.password.data)
        db_session.add(user)
        flash('thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html',title='Create your account',form=form)

@main.route('/login')
def login():
    form = LoginForm()
    
    return render_template('login.html', title='Login',form=form)        