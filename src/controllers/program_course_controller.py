from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from src.decorators import is_super_admin
from src.requests.assign_program_courses_request import AssignProgramCoursesRequest
from src.services.program_course_service import ProgramCourseService

program_course_bp = Blueprint('program_course_bp', __name__)


@program_course_bp.get('')
@jwt_required()
@is_super_admin
def index(service: ProgramCourseService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@program_course_bp.post('')
@jwt_required()
@is_super_admin
def store(service: ProgramCourseService):
    data = AssignProgramCoursesRequest(**request.get_json()).dict()
    response = service.assign_courses(data)
    return jsonify(response), 201
