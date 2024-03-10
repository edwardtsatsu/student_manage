from abc import ABC

from injector import inject

from src.dtos.semester_dto import SemesterDto
from src.repositories.semester_repository import SemesterRepository
from src.services.base_service import BaseService


class SemesterService(BaseService, ABC):
    @inject
    def __init__(self, repository: SemesterRepository):
        super().__init__(repository)

    def get_dto(self):
        return SemesterDto
