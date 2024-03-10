from injector import Module, singleton, provider

from src.repositories.program_course_repository import ProgramCourseRepository
from src.repositories.student_course_repository import StudentCourseRepository
from src.repositories.user_repository import UserRepository
from src.services.student_course_service import StudentCourseService


class StudentCourseModule(Module):

    @singleton
    @provider
    def provide_student_course_repository(self) -> StudentCourseRepository:
        return StudentCourseRepository()

    @singleton
    @provider
    def provide_student_course_service(self, repo: StudentCourseRepository,
                                       user_repo: UserRepository,
                                       program_course_repo: ProgramCourseRepository) -> StudentCourseService:
        return StudentCourseService(repository=repo, user_repo=user_repo, program_course_repo=program_course_repo)
