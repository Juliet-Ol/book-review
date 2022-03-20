from . import main
import urllib.request
import json
from flask import render_template, flash, redirect, url_for
from flask_login import logout_user,login_user,login_required
from app import db
from app.models import User
from .forms import LoginForm, RegistrationForm



@main.route('/')
@main.route('/index')
def index():
    word = {'username': 'Hey there Get to see and review your top favorite books at the comfort of your couch'}
    words = {'usersname': 'Already have an account ?'}
    return render_template('index.html', word=word, words=words)


@main.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_create = User(username=form.username.data,
                           email=form.email.data, password=form.password.data)
        db.session.add(user_create)
        db.session.commit()
        flash(f"Account created successfully for{form.username.data}")
        return redirect('/login')
    return render_template('register.html', title='Create your account', form=form)


@main.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect('/home')
        flash('Login requested for user {},remember_me: {}'.format(
            form.email.data, form.remember_me.data)) 
    return render_template('login.html', title='Login', form=form)


@main.route('/home')
def home():
    url = 'https://www.googleapis.com/books/v1/volumes?q=isbn'
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    wor = {'names': 'Grab yourself some nice cup of coffee as we nit pick'}
    return render_template('home.html', wor=wor,books=dict["items"])


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
