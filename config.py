import os
import json


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # Specific name for flask-sqlalchemy
    SQLALCHEMY_DATABASE_URI = json.load(open('./zappa_settings.json'))[
        'production']['environment_variables']['DATABASE_URL']
    JWT_SECRET_KEY = 'your-secret-key'
    # Needed to validate tokens
    GOOGLE_CLIENT_ID = '1092564513780-rdhenfi8go2oeoesarnirb0l9aaimkri.apps.googleusercontent.com'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # Should still set --debug flag when running flask run
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
