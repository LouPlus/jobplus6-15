# -*- coding: utf-8 -*-
'''app.py
1.App的创建
2.插件初始化
3.蓝图注册
'''

from flask import Flask

def create_app():
    app = Flask(__name__)
    return app



