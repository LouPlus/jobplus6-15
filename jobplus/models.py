# -*- coding: utf-8 -*-
'''models.py
实现数据库模型
'''
# TODO 实现 models.py 文件
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.DateTime, default=datetime.utcnow)
    updated_time = db.Column(db.DateTime, default=datetime.utcnow)


user_job = db.Table(
    'user_job',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')),
    db.Column('job_id', db.Integer, db.ForeignKey('job.id', ondelete='CASCADE'))
)


class User(BaseModel, UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 0
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    role = db.Column(db.SmallInteger, default=ROLE_USER)
    name = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(128), unique=True, index=True,nullable=False)
    _password = db.Column('password', db.String(128), nullable=False)

    seeker = db.relationship('Seeker', uselist=False)
    phone = db.Column(db.String(11))

    collect_jobs = db.relationship('Job', secondary=user_job)
    company = db.relationship('Company', uselist=False)

    is_disable = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User:{}>'.format(self.email)

    @property
    def enable_jobs(self):
        if not self.is_company:
            raise AttributeError('User has no attribute enable_jobs')
        return self.jobs.filter(Job.is_disable.is_(False))

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

    @property
    def is_staff(self):
        return self.role == self.ROLE_USER


class Seeker(BaseModel):
    __tablename__ = 'seeker'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', uselist=False)
    name = db.Column(db.String(128))
    work_year = db.Column(db.Integer)
    resume_uri = db.Column(db.String(256))

class Company(BaseModel):
    __tablename__ = 'company'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    user = db.relationship('User', uselist=False, backref=db.backref('companys', uselist=False))
    name = db.Column(db.String(128))
    website = db.Column(db.String(256))
    logo_uri = db.Column(db.String(256))
    introduction = db.Column(db.String(256))
    description = db.Column(db.Text)
    domain = db.Column(db.String(128))
    finance = db.Column(db.String(128))
    city = db.Column(db.String(128))

    def __repr__(self):
        return '<company {}>'.format(self.user_id)

class Job(BaseModel):
    __tablename__ = 'job'
    company_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    company = db.relationship('User', uselist=False, backref=db.backref('jobs', lazy='dynamic'))
    title = db.Column(db.String(128))
    description = db.Column(db.Text)
    address = db.Column(db.String(256))
    salary_max = db.Column(db.Integer)
    salary_min = db.Column(db.Integer)
    location = db.Column(db.String(128))
    experience = db.Column(db.String(128))
    education = db.Column(db.String(128))
    tags = db.Column(db.String(128))
    is_disable = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Job {}>'.format(self.company_id)

    @property
    def tag_list(self):
        return self.tags.split(',')

    @property
    def current_user_is_applied(self):
        d = Delivery.query.filter_by(job_id=self.id, user_id=current_user.id).first()
        return (d is not None)

class Delivery(BaseModel):
    __tablename__ = 'delivery'

    STATUS_WAITING = 1
    STATUS_REJECT = 2
    STATUS_ACCEPT = 3

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id', ondelete='SET NULL'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    company_id = db.Column(db.Integer)
    status = db.Column(db.SmallInteger, default=STATUS_WAITING)
    response = db.Column(db.String(256))

    @property
    def user(self):
        return User.query.get(self.user_id)

    @property
    def job(self):
        return Job.query.get(self.job_id)
