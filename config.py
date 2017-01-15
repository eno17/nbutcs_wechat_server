#coding=utf8
import os


class Config:
    SECRET_KEY = 'hard to guess string' # os.environ.get('SECRET_KEY' )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG  = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://waimai:Chihuo2016@127.0.0.1/takeout' # imac 不能填localhost

config = {
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}