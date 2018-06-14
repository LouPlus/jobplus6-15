# -*- coding: utf-8 -*-
'''app.py
1.App的创建
2.插件初始化
3.蓝图注册
'''

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

    return app

