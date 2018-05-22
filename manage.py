# -*- coding: utf-8 -*-
'''manage.py
用于APP的启动
'''
# TODO 实现 manage.py 模块
from jobplus.app import create_app
from flask import render_template

app = create_app()

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()
