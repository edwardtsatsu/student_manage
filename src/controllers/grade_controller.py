from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from src.decorators import is_super_admin
from src.requests.store_grade_request import StoreGradeRequest
from src.requests.update_grade_request import UpdateGradeRequest
from src.services.grade_service import GradeService

grade_bp = Blueprint('grade_bp', __name__)


@grade_bp.get('')
@jwt_required()
@is_super_admin
def index(service: GradeService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@grade_bp.post('')
@jwt_required()
@is_super_admin
def store(service: GradeService):
    data = StoreGradeRequest(**request.get_json()).dict()
    response = service.store(data)
    return jsonify(response), 201


@grade_bp.put('/<string:id>')
@jwt_required()
@is_super_admin
def update(id, service: GradeService):
    data = UpdateGradeRequest(id=id, **request.get_json()).dict()
    resource = service.update(id, data)
    return jsonify(resource)


@grade_bp.delete('/<string:id>')
@jwt_required()
@is_super_admin
def destroy(id, service: GradeService):
    service.delete(id)
    return jsonify({}), 204
