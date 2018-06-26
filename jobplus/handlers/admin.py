'''admin.py
管理员，管理员 - 用户管理，管理员 - 职位管理
'''
# TODO 实现admin.py 文件
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.decorators import admin_required
from jobplus.models import db, User
from jobplus.forms import RegisterForm, UserEditForm, CompanyEditForm


admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/users')
@admin_required
def users():
    page = request.args.get('page', default=1, type=int)
    pagination = User.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/users.html', pagination=pagination)


@admin.route('/users/create_user', methods=['GET', 'POST'])
@admin_required
def create_user():
    form = RegisterForm()
    if form.is_submitted():
        form.create_user()
        flash('求职者创建成功', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/create_user.html', form=form)


@admin.route('/users/create_company', methods=['GET', 'POST'])
@admin_required
def create_company():
    form = RegisterForm()
    form.name.label = u'企业用户名'
    if form.validate_on_submit():
        company_user = form.create_user()
        company_user.role = User.ROLE_COMPANY
        db.session.add(company_user)
        db.session.commit()
        flash('企业创建成功', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/create_company.html', form=form)


@admin.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.is_company:
        form = CompanyEditForm(obj=user)
        if form.validate_on_submit():
            form.update(user)
            flash('更新成功', 'success')
            return redirect(url_for('admin.users'))
    else:
        form = UserEditForm(obj=user)
        if form.validate_on_submit():
            form.update(user)
            flash('更新成功', 'success')
            return redirect(url_for('admin.users'))
    return render_template('admin/edit_user.html', form=form, user=user)


@admin.route('/users/<int:user_id>/disable', methods=['GET', 'POST'])
@admin_required
def disable_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.is_disable:
        user.is_disable = False
        flash('已经成功启用用户', 'success')
    else:
        user.is_disable = True
        flash('已经成功禁用用户', 'success')
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('admin.users'))


@admin.route('/jobs')
@admin_required
def jobs():
    page = request.args.get('page', default=1, type=int)
    pagination = Job.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/jobs.html', pagination=pagination)
