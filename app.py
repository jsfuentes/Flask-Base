from sqlalchemy.orm import DeclarativeBase
from flask import Blueprint, request
from flask import Flask, jsonify, make_response
from flask_login import LoginManager
from sqlalchemy import Column, String, Integer
from flask_cors import CORS, cross_origin
import os

# local config.py
from config import config
from models.user import User
from models.database import db

login_manager = LoginManager()
login_manager.session_protection = 'strong'
# login_manager.login_view = 'main.index'

config_name = os.getenv('FLASK_CONFIG') or 'default'
app = Flask(__name__)
CORS(app)

# app.config is a dictionary object used for flask as well as package config
app.config.from_object(config[config_name])
config[config_name].init_app(app)

login_manager.init_app(app)

db.init_app(app)


# Create all tables
with app.app_context():
    db.create_all()


@app.route('/')
def heartbeat():
    return "Hello World"


user_blueprint = Blueprint(
    "user_blueprint", __name__
)


@user_blueprint.route("/<int:id>")
def user_detail(id):
    user = db.get_or_404(User, id)
    return jsonify(user.as_dict())


@user_blueprint.route("/create", methods=["GET", "POST"])
def user_create():
    user = User(
        username="girl",
        email="jsjfuenetesj@gmail.com",
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.as_dict())


app.register_blueprint(user_blueprint, url_prefix='/users')


if __name__ == '__main__':
    app.run(debug=True)
