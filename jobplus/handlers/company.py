'''company.py
企业列表，企业详情，企业 - 简历管理，企业 - 职位管理
'''
# TODO 实现company.py 文件
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.forms import CompanyProfileForm
from flask_login import login_required, current_user

company = Blueprint('company', __name__, url_prefix='/company')


@company.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = CompanyProfileForm(obj=current_user)
    return render_template('company/profile.html', form=form)

