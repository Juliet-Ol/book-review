from . import main
from flask import render_template

@main.route('/')
@main.route('/index')
def index():
    user = {'username': 'Hey there Get to see and review your top favorite books at the comfort of your couch'}