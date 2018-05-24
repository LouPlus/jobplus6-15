'''front.py
首页，企业注册，求职者注册，登录
'''
# TODO 实现front.py 文件
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import User
from jobplus.forms import LoginForm
from flask_login import login_user, logout_user, login_required

front = Blueprint('front', __name__)

@front.route('/')
def index():
    return render_template('index.html')


@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        next = 'user.profile'
	#if user.is_admin:
	#    next = 'admin.index'
	#elif user.is_company:
	#    next = 'company.profile'
        return redirect(url_for(next))
    return render_template('login.html', form=form)
