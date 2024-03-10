from injector import Module, singleton, provider

from src.repositories.course_repository import CourseRepository
from src.repositories.grade_repository import GradeRepository
from src.services.course_service import CourseService
from src.services.grade_service import GradeService


class GradeModule(Module):

    @singleton
    @provider
    def provide_grade_repository(self) -> GradeRepository:
        return GradeRepository()

    @singleton
    @provider
    def provide_grade_service(self, grade_repo: GradeRepository) -> GradeService:
        return GradeService(repository=grade_repo)
