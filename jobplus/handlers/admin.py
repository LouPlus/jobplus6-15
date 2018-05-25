'''admin.py
管理员，管理员 - 用户管理，管理员 - 职位管理
'''
# TODO 实现admin.py 文件
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():
    return render_template('admin/index.html')
