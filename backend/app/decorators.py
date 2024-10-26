from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify

def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            identity = get_jwt_identity()
            if identity['role'] != role:
                return jsonify({'msg': 'Access forbidden: Role does not match'}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper
