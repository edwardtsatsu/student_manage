from functools import wraps

from flask import jsonify, request
from flask_jwt_extended import decode_token

from src.repositories.user_repository import UserRepository


def is_super_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = get_token()

        if token is None:
            return jsonify({'message': 'unauthorized'}), 401

        payload = decode_token(token)

        user_repo = UserRepository()
        user = user_repo.find(payload.get('sub'))
        if user is None or user.role.name != 'Super Admin':
            return jsonify({'message': 'access denied'}), 403
        return func(*args, **kwargs)

    return decorated_function


def is_student(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = get_token()

        if token is None:
            return jsonify({'message': 'unauthorized'}), 401

        payload = decode_token(token)

        user_repo = UserRepository()
        user = user_repo.find(payload.get('sub'))
        if user is None or user.role.name != 'Student':
            return jsonify({'message': 'access denied'}), 403
        return func(*args, **kwargs)

    return decorated_function


def get_token():
    header = request.headers.get('Authorization')
    token = header.split(' ')[1]
    return token
