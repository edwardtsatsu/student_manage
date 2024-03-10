from src.models import StudentCourse
from src.repositories.base_repository import BaseRepository


class StudentCourseRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=StudentCourse)
