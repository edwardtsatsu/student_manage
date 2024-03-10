from injector import Module, singleton, provider

from src.repositories.student_repository import StudentRepository
from src.repositories.user_repository import UserRepository
from src.services.student_service import StudentService


class UserModule(Module):

    @singleton
    @provider
    def provide_user_repository(self) -> UserRepository:
        return UserRepository()

    @singleton
    @provider
    def provide_student_repository(self) -> StudentRepository:
        return StudentRepository()

    @singleton
    @provider
    def provide_student_service(self, student_repo: StudentRepository) -> StudentService:
        return StudentService(repository=student_repo)
