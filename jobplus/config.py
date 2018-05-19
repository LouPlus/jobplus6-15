# -*- coding: utf-8 -*-
'''config.py
App配置文件
'''
# TODO 实现 config.py 文件

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'joyccaacca'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15

class DevelopmentConfig(BaseConfig):
    DEBUG = 1
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:123@localhost:3306/jobplus?charset=utf8'


class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass


configs = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestingConfig
}
