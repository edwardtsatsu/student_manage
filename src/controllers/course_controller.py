from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from src.decorators import is_super_admin
from src.requests.store_course_request import StoreCourseRequest
from src.requests.update_course_request import UpdateCourseRequest
from src.services.course_service import CourseService

course_bp = Blueprint('course_bp', __name__)


@course_bp.get('')
@jwt_required()
@is_super_admin
def index(service: CourseService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@course_bp.post('')
@jwt_required()
@is_super_admin
def store(service: CourseService):
    data = StoreCourseRequest(**request.get_json()).dict()
    response = service.store(data)
    return jsonify(response), 201


@course_bp.put('/<string:id>')
@jwt_required()
@is_super_admin
def update(id, service: CourseService):
    data = UpdateCourseRequest(id=id, **request.get_json()).dict()
    resource = service.update(id, data)
    return jsonify(resource)


@course_bp.delete('/<string:id>')
@jwt_required()
@is_super_admin
def destroy(id, service: CourseService):
    service.delete(id)
    return jsonify({}), 204
