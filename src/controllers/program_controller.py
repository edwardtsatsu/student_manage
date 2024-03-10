from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from src.decorators import is_super_admin
from src.requests.assign_program_courses_request import AssignProgramCoursesRequest
from src.requests.store_program_request import StoreProgramRequest
from src.requests.update_program_request import UpdateProgramRequest
from src.services.program_course_service import ProgramCourseService
from src.services.program_service import ProgramService

program_bp = Blueprint('program_bp', __name__)


@program_bp.get('')
@jwt_required()
@is_super_admin
def index(service: ProgramService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@program_bp.post('')
@jwt_required()
@is_super_admin
def store(service: ProgramService):
    data = StoreProgramRequest(**request.get_json()).dict()
    response = service.store(data)
    return jsonify(response), 201


@program_bp.put('/<string:id>')
@jwt_required()
@is_super_admin
def update(id, service: ProgramService):
    data = UpdateProgramRequest(id=id, **request.get_json()).dict()
    resource = service.update(id, data)
    return jsonify(resource)


@program_bp.delete('/<string:id>')
@jwt_required()
@is_super_admin
def destroy(id, service: ProgramService):
    service.delete(id)
    return jsonify({}), 204
