# -*- coding: utf-8 -*-
'''decorators.py
实现一些常用的装饰器
'''
# TODO 实现decorators.py 文件


from flask import abort
from flask_login import current_user
from functools import wraps
from jobplus.models import User


def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwrargs):
            if not current_user.is_authenticated or current_user.role < role:
                abort(404)
            return func(*args, **kwrargs)
        return wrapper
    return decorator


admin_required = role_required(User.ROLE_ADMIN)
