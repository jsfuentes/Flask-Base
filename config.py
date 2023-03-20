import os
import ssl
import json


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # Specific name for flask-sqlalchemy
    SQLALCHEMY_DATABASE_URI = json.load(open('zappa_settings.json'))[
        'production']['environment_variables']['DATABASE_URL']

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
