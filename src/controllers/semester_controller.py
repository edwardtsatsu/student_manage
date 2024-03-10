from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from src.decorators import is_super_admin
from src.requests.store_semester_request import StoreSemesterRequest
from src.requests.update_semester_request import UpdateSemesterRequest
from src.services.semester_service import SemesterService

semester_bp = Blueprint('semester_bp', __name__)


@semester_bp.get('')
@jwt_required()
@is_super_admin
def index(service: SemesterService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@semester_bp.post('')
@jwt_required()
@is_super_admin
def store(service: SemesterService):
    data = StoreSemesterRequest(**request.get_json()).dict()
    response = service.store(data)
    return jsonify(response), 201


@semester_bp.put('/<string:id>')
@jwt_required()
@is_super_admin
def update(id, service: SemesterService):
    data = UpdateSemesterRequest(**request.get_json()).dict()
    resource = service.update(id, data)
    return jsonify(resource)


@semester_bp.delete('/<string:id>')
@jwt_required()
@is_super_admin
def destroy(id, service: SemesterService):
    service.delete(id)
    return jsonify({}), 204
