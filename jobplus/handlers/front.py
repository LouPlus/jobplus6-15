'''front.py
首页，企业注册，求职者注册，登录
'''
# TODO 实现front.py 文件
from flask import Blueprint, render_template
from jobplus.forms import LoginForm

front = Blueprint('front', __name__)

@front.route('/')
def index():
    return render_template('index.html')


@front.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
