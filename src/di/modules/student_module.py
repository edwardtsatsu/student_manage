from injector import Module, singleton, provider

from src.repositories.program_repository import ProgramRepository
from src.repositories.role_repository import RoleRepository
from src.repositories.student_repository import StudentRepository
from src.services.program_service import ProgramService
from src.services.student_service import StudentService


class StudentModule(Module):

    @singleton
    @provider
    def provide_student_repository(self) -> StudentRepository:
        return StudentRepository()


    @singleton
    @provider
    def provide_student_service(self, student_repo: StudentRepository, role_repo: RoleRepository) -> StudentService:
        return StudentService(repository=student_repo, role_repo=role_repo)
