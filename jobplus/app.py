# -*- coding: utf-8 -*-
'''app.py
1.App的创建
2.插件初始化
3.蓝图注册
'''
import datetime
from flask import Flask
from jobplus.models import db, User
from jobplus.config import configs
from flask_migrate import Migrate
from flask_login import LoginManager
#from flask_moment import Moment

def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)
#    moment = Moment(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)

    login_manager.login_view = 'front.login'

def register_filters(app):

    @app.template_filter()
    def timesince(value):
        now = datetime.datetime.utcnow()
        delta = now - value
        if delta.days > 365:
            return '{}年前'.format(delta.days // 365)
        if delta.days > 30:
            return '{}月前'.format(delta.days // 30)
        if delta.days > 0:
            return '{}天前'.format(delta.days)
        if delta.seconds > 3600:
            return '{}小时前'.format(delta.seconds // 3600)
        if delta.seconds > 60:
            return '{}分钟前'.format(delta.seconds // 60)
        return '刚刚'

def register_blueprints(app):
    from .handlers import front, user,company, admin, job
    app.register_blueprint(front)
    app.register_blueprint(user)
    app.register_blueprint(company)
    app.register_blueprint(admin)
    app.register_blueprint(job)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extensions(app) 
    register_blueprints(app)
    register_filters(app)

    return app

