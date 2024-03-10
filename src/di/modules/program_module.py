from injector import Module, singleton, provider

from src.repositories.program_repository import ProgramRepository
from src.services.program_service import ProgramService


class ProgramModule(Module):

    @singleton
    @provider
    def provide_program_repository(self) -> ProgramRepository:
        return ProgramRepository()


    @singleton
    @provider
    def provide_program_service(self, program_repo: ProgramRepository) -> ProgramService:
        return ProgramService(repository=program_repo)
