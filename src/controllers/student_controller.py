from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from src.decorators import is_super_admin
from src.requests.register_student_request import RegisterStudentRequest
from src.requests.update_student_request import UpdateStudentRequest
from src.services.student_service import StudentService

student_bp = Blueprint('student_bp', __name__)


@student_bp.get('')
@jwt_required()
@is_super_admin
def index(service: StudentService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@student_bp.post('')
@jwt_required()
@is_super_admin
def store(service: StudentService):
    data = RegisterStudentRequest(**request.get_json()).dict()
    response = service.store(data)
    return jsonify(response), 201


@student_bp.put('/<string:id>')
@jwt_required()
@is_super_admin
def update(id, service: StudentService):
    data = UpdateStudentRequest(**request.get_json()).dict()
    resource = service.update(id, data)
    return jsonify(resource)


@student_bp.delete('/<string:id>')
@jwt_required()
@is_super_admin
def destroy(id, service: StudentService):
    service.delete(id)
    return jsonify({}), 204
