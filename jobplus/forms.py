# -*- coding: utf-8 -*-
'''form.py
实现表单模型
'''
# TODO 实现 forms.py 文件
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db, User, Company
from flask import flash

class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            flash('登录失败', 'danger')
            raise ValidationError('该邮箱未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')


class RegisterForm(FlaskForm):
    name = StringField('用户名', validators=[Required(), Length(3, 24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('用户名已存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在')

    def create_user(self):
        user = User(name=self.name.data,
                    email=self.email.data,
                    password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user


class UserProfileForm(FlaskForm):
    name = StringField('姓名')
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码（不填写保持不变）', validators=[Required(), Length(6, 24)])
    phone = StringField('手机号')
    work_year = IntegerField('工作年限')
    resume_uri = StringField('简历地址')
    submit = SubmitField('提交')


class CompanyProfileForm(FlaskForm):
    name = StringField('企业名称')
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码（不填写保持不变）', validators=[Required(), Length(6, 24)])
    phone = StringField('手机号')
    city = IntegerField('地址')
    website = StringField('公司网站')
    logo_uri = StringField('Logo')
    introduction = StringField('一句话描述')
    description = TextAreaField('公司详情')
    submit = SubmitField('提交')


class UserEditForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码')
    name = StringField('姓名')
    phone = StringField('手机号')
    submit = SubmitField('提交')

    def update(self, user):
        self.populate_obj(user)
        user.email = self.email.data
        user.name = self.name.data
        user.phone = self.phone.data
        if self.password.data:
            user.password = self.password.data
        db.session.add(user)
        db.session.commit()


class CompanyEditForm(FlaskForm):
    name = StringField('企业名称')
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码')
    phone = StringField('手机号')
    website = StringField('公司网站', validators=[Length(0, 64)])
    description = StringField('一句话简介', validators=[Length(0, 100)])
    submit = SubmitField('提交')

    def update(self, company):
        company.name = self.name.data
        company.email = self.email.data
        company.phone = self.phone.data
        if self.password.data:
            company.password = self.password.data
        if company.company:
            companydetail = company.company
        else:
            companydetail = Company()
            companydetail.user_id = company.id
        companydetail.website = self.website.data
        companydetail.description = self.description.data
        self.populate_obj(companydetail)
        db.session.add(company)
        db.session.add(companydetail)
        db.session.commit()
