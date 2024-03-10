from src.models import Semester
from src.repositories.base_repository import BaseRepository


class SemesterRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Semester)

