from abc import ABC

from injector import inject

from src.dtos.course_dto import CourseDto
from src.repositories.course_repository import CourseRepository
from src.services.base_service import BaseService


class CourseService(BaseService, ABC):
    @inject
    def __init__(self, repository: CourseRepository):
        super().__init__(repository)

    def get_dto(self):
        return CourseDto
