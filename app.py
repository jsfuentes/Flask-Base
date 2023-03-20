from flask import Flask, jsonify, make_response
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
from flask_cors import CORS, cross_origin
import os


# local config.py
from config import config

login_manager = LoginManager()
login_manager.session_protection = 'strong'
# login_manager.login_view = 'main.index'

config_name = os.getenv('FLASK_CONFIG') or 'default'
app = Flask(__name__)
# app.config is a dictionary object used for flask as well as package config
app.config.from_object(config[config_name])
config[config_name].init_app(app)

login_manager.init_app(app)

db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def get_user(id):
    user = db.get_or_404(User, id)
    return user


def insert_user():
    user = User(
        username="ssss",
        email="jsjfuenetesj@gmail.com",
    )
    db.session.add(user)
    db.session.commit()
    return user


# Create all tables
with app.app_context():
    db.create_all()


@app.route('/')
def heartbeat():
    return "Hello World"


@app.route("/users/<int:id>")
def user_detail(id):
    user = get_user(id)
    return jsonify(user.as_dict())


@app.route("/users/create", methods=["GET", "POST"])
def user_create():
    user = insert_user()
    return jsonify(user.as_dict())


if __name__ == '__main__':
    app.run(debug=True)
