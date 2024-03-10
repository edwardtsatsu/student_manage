from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.decorators import is_student
from src.requests.register_student_course_request import RegisterStudentCourseRequest
from src.requests.store_course_request import StoreCourseRequest
from src.services.student_course_service import StudentCourseService

student_course_bp = Blueprint('student_course_bp', __name__)


@student_course_bp.get('')
@jwt_required()
@is_student
def index(service: StudentCourseService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@student_course_bp.post('')
@jwt_required()
@is_student
def store(service: StudentCourseService):
    data = RegisterStudentCourseRequest(**request.get_json()).dict()
    data['user_id'] = get_jwt_identity()
    response = service.store(data)
    return jsonify(response), 201


