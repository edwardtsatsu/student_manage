from injector import Module, singleton, provider

from src.repositories.course_repository import CourseRepository
from src.services.course_service import CourseService


class CourseModule(Module):

    @singleton
    @provider
    def provide_course_repository(self) -> CourseRepository:
        return CourseRepository()


    @singleton
    @provider
    def provide_program_service(self, course_repo: CourseRepository) -> CourseService:
        return CourseService(repository=course_repo)
