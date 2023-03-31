from flask import Flask
from flask_cors import CORS, cross_origin
import os
from app.extensions import db, login_manager, migrate
from config import config
from app.models.user import db_get_user


def create_app():
    app = Flask(__name__)

    config_name = os.getenv('FLASK_CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize Flask extensions here
    CORS(app)

    login_manager.session_protection = 'strong'
    login_manager.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here
    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/api/users')

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/api/questions')

    @app.route('/')
    def index():
        return 'Hi'

    @login_manager.user_loader
    def load_user(user_id):
        user = db_get_user(user_id)
        print("LOAD USER", user.get_id())
        return user

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
