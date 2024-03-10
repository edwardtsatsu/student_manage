from abc import ABC

from injector import inject

from src.dtos.program_dto import ProgramDto
from src.repositories.program_repository import ProgramRepository
from src.services.base_service import BaseService


class ProgramService(BaseService, ABC):
    @inject
    def __init__(self, repository: ProgramRepository):
        super().__init__(repository)

    def get_dto(self):
        return ProgramDto
