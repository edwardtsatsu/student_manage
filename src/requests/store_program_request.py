from pydantic import BaseModel, constr, conint, field_validator

from src.repositories.program_repository import ProgramRepository


class StoreProgramRequest(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    code: constr(strip_whitespace=True, min_length=1)
    duration_in_years: conint()

    @field_validator('code')
    def code_unique(cls, v):
        program_repo = ProgramRepository()
        program = program_repo.find_by_code(v)
        if program is not None:
            raise ValueError('program with this code already exists')
        return v
