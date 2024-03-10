from injector import Module, singleton, provider

from src.repositories.program_repository import ProgramRepository
from src.repositories.semester_repository import SemesterRepository
from src.services.program_service import ProgramService
from src.services.semester_service import SemesterService


class SemesterModule(Module):

    @singleton
    @provider
    def provide_semester_repository(self) -> SemesterRepository:
        return SemesterRepository()


    @singleton
    @provider
    def provide_semester_service(self, semester_repo: SemesterRepository) -> SemesterService:
        return SemesterService(repository=semester_repo)
