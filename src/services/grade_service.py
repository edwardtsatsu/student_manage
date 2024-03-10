from abc import ABC

from injector import inject

from src.dtos.grade_dto import GradeDto
from src.repositories.grade_repository import GradeRepository
from src.services.base_service import BaseService


class GradeService(BaseService, ABC):
    @inject
    def __init__(self, repository: GradeRepository):
        super().__init__(repository)

    def get_dto(self):
        return GradeDto
