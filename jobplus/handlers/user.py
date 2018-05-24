'''user.py
求职者，求职者 - 个人信息，求职者 - 简历管理，求职者 - 投递管理
'''
# TODO 实现user.py 文件
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.forms import UserProfileForm
from flask_login import login_required, current_user

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UserProfileForm(obj=current_user)
    return render_template('user/profile.html', form=form)

