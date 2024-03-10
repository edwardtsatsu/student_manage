from abc import ABC
from passlib.hash import bcrypt

from flask_jwt_extended import create_access_token
from injector import inject

from src.dtos.auth_dto import AuthDto
from src.dtos.role_dto import RoleDto
from src.models import User, Role
from src.repositories.role_repository import RoleRepository
from src.repositories.user_repository import UserRepository
from src.requests.login_request import LoginRequest

from src.requests.student_login_request import StudentLoginRequest
from src.services.base_service import BaseService


class AuthService(BaseService, ABC):

    @inject
    def __init__(self, repository: UserRepository, role_repository: RoleRepository):
        super().__init__(repository=repository)
        self.role_repository = role_repository

    def login(self, request: LoginRequest):
        user = self.repository.find_by_email(request.email)
        if user is None:
            return None
        if not bcrypt.verify(request.password, user.password):
            return None
        token = create_access_token(identity=user.id, expires_delta=False)
        return self.__get_auth(user, token)

    def student_login(self, request: StudentLoginRequest):
        user = self.repository.find_student_by_student_code(request.student_code)
        if user is None:
            return None
        if not bcrypt.verify(request.password, user.password):
            return None
        token = create_access_token(identity=user.id, expires_delta=False)
        return self.__get_auth(user, token)

    def get_dto(self):
        return AuthDto

    def __get_auth(self, user: User, token: str):
        return AuthDto(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            access_token=token,
            role=RoleDto(id=user.role.id, name=user.role.name).dict()
        ).dict()
