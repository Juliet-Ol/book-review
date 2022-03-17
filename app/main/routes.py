from . import main
from flask import render_template
from  .forms import LoginForm

@main.route('/')
@main.route('/index')
def index():
    user = {'username': 'Hey there Get to see and review your top favorite books at the comfort of your couch'}
    users = {'usersname':'Already have an account ?'}
    return render_template('index.html',user =user,users=users)

@main.route('/register')
def register():
    return render_template('register.html')

@main.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login',form=form)        