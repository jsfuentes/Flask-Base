from flask import Flask
from flask_cors import CORS, cross_origin
from flask_login import LoginManager
import os
from app.extensions import db
from config import config


def create_app():
    app = Flask(__name__)

    config_name = os.getenv('FLASK_CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize Flask extensions here
    CORS(app)

    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.init_app(app)

    db.init_app(app)

    # Register blueprints here
    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    @app.route('/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
