'''front.py
首页，企业注册，求职者注册，登录
'''
# TODO 实现front.py 文件
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import User, Job
from jobplus.forms import LoginForm
from flask_login import login_user, logout_user, login_required

front = Blueprint('front', __name__)

@front.route('/')
def index():
    newest_jobs = Job.query.order_by(Job.created_time.desc()).limit(12)
    newest_companies = User.query.filter(
        User.role==User.ROLE_COMPANY
    ).order_by(User.created_time.desc()).limit(12)
    return render_template(
        'index.html',
        active='index',
        newest_jobs=newest_jobs,
        newest_companies=newest_companies,
    )

@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.is_disable:
            flash('用户已经被禁用', 'warning')
            return redirect(url_for('front.login'))
        else:
            login_user(user, form.remember_me.data)
            next = 'user.profile'
            if user.is_admin:
                next = 'admin.users'
            elif user.is_company:
                next = 'company.profile'
            return redirect(url_for(next))
    return render_template('login.html', form=form)


@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录', 'success')
    return redirect(url_for('.index'))
