from injector import Module, singleton, provider

from src.repositories.program_course_repository import ProgramCourseRepository
from src.services.program_course_service import ProgramCourseService


class ProgramCourseModule(Module):

    @singleton
    @provider
    def provide_program_course_repository(self) -> ProgramCourseRepository:
        return ProgramCourseRepository()


    @singleton
    @provider
    def provide_program_service(self, program_course_repo: ProgramCourseRepository) -> ProgramCourseService:
        return ProgramCourseService(repository=program_course_repo)
