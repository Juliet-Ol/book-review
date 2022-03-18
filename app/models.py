from . import login_manager
from app import db
from flask_login import UserMixin


class Book:
    def __init__(self, id, title, author, publisher, description):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.description = description


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
