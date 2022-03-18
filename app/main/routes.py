from . import main
from flask import render_template,flash,redirect,url_for
from flask_login import logout_user
from app.models import User
from  .forms import LoginForm,RegistrationForm
from .. requests import get_random_books


@main.route('/')
@main.route('/index')
def index():
    book = get_random_books()
    word = {'username': 'Hey there Get to see and review your top favorite books at the comfort of your couch'}
    words = {'usersname':'Already have an account ?'}
    return render_template('index.html',word =word,words=words)

@main.route('/register',methods=['POST','GET'])
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Create your account',form=form)

@main.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {},remember_me: {}'.format(form.username.data, form.remember_me.data))
        return redirect('/home')
    return render_template('login.html', title='Login',form=form)   

@main.route('/home')    
def home ():
    wor = {'names':'Grab yourself some nice cup of coffee as we nit pick'}
    return render_template('home.html',wor=wor)  

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

     