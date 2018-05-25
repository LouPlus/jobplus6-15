# -*- coding: utf-8 -*-
'''models.py
实现数据库模型
'''
# TODO 实现 models.py 文件
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    updated_time = db.Column(db.DateTime, default=datetime.utcnow)


class User(BaseModel, UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 0
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    role = db.Column(db.SmallInteger, default=ROLE_USER)
    email = db.Column(db.String(128), unique=True, index=True,nullable=False)
    _password = db.Column('password', db.String(128), nullable=False)

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY


class Seeker(BaseModel):
    __tablename__ = 'seeker'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('seeker', uselist=False), uselist=False )
    name = db.Column(db.String(128))
    phone = db.Column(db.Integer)
    work_year = db.Column(db.Integer)
    resume_uri = db.Column(db.String(256))

class Company(BaseModel):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('company',uselist=False), uselist=False)
    name = db.Column(db.String(128))
    website = db.Column(db.String(256))
    logo_uri = db.Column(db.String(256))
    introduction = db.Column(db.String(256))
    description = db.Column(db.Text)
    domain = db.Column(db.String(128))
    finance = db.Column(db.Integer)
    city = db.Column(db.String(128))

class Job(BaseModel):
    __tablename__ = 'job'
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = db.relationship('Company', backref=db.backref('jobs'), uselist=False)
    title = db.Column(db.String(128))
    description = db.Column(db.Text)
    address = db.Column(db.String(256))
    salary_max = db.Column(db.Integer)
    salary_min = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    education = db.Column(db.String(128))
    tags = db.relationship('Tag', backref='job')

class Tag(BaseModel):
    __tablename__ = 'tag'
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    name = db.Column(db.String(128))

class Delivery(BaseModel):
    __tablename__ = 'delivery'
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    job = db.relationship('Job', backref='deliverys', uselist=False)
    seeker_id = db.Column(db.Integer, db.ForeignKey('seeker.id'))
    seeker = db.relationship('Seeker', backref='deliverys', uselist=False)
    status = db.Column(db.Integer)
