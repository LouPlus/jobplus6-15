# -*- coding: utf-8 -*-
'''app.py
1.App的创建
2.插件初始化
3.蓝图注册
'''

from flask import Flask
from jobplus.models import db
from jobplus.config import configs


def create_app():
    app = Flask(__name__)
    app.config.from_object(configs.get('development'))
    db.init_app(app)
    return app



