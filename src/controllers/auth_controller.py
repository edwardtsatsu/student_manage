from flask import Blueprint, request, jsonify

from src.requests.login_request import LoginRequest
from src.requests.student_login_request import StudentLoginRequest
from src.services.auth_service import AuthService

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.post('/login')
def login(service: AuthService):
    data = LoginRequest(**request.get_json())
    response = service.login(data)
    if response is None:
        return jsonify({'message': 'invalid credentials'}), 401
    return jsonify(response)


@auth_bp.post('/student/login')
def student_login(service: AuthService):
    data = StudentLoginRequest(**request.get_json())
    response = service.student_login(data)
    if response is None:
        return jsonify({'message': 'invalid credentials'}), 401
    return jsonify(response)
