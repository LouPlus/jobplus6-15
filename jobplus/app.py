# -*- coding: utf-8 -*-
'''app.py
1.App的创建
2.插件初始化
3.蓝图注册
'''

from flask import Flask
from jobplus.models import db
from jobplus.config import configs
from flask_migrate import Migrate


def register_blueprints(app):
    from .handlers import front
    app.register_blueprint(front)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    Migrate(app, db)
    register_blueprints(app)

    return app

