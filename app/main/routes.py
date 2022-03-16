from . import main
from flask import render_template

@main.route('/')
@main.route('/index')
def index():
    users = {'username': 'Hey there Get to see and review your top favorite books at the comfort of your couch'}
    return render_template('index.html',users =users)