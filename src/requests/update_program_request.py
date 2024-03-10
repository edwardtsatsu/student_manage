import uuid
from typing import Optional

from pydantic import BaseModel, constr, conint, field_validator
from pydantic_core.core_schema import FieldValidationInfo

from src.repositories.program_repository import ProgramRepository


class UpdateProgramRequest(BaseModel):
    id: Optional[uuid.UUID]
    name: constr(strip_whitespace=True, min_length=1)
    code: constr(strip_whitespace=True, min_length=1)
    duration_in_years: conint()

    @field_validator('code')
    def code_unique(cls, v, info: FieldValidationInfo):
        program_repo = ProgramRepository()
        program = program_repo.find_by_code(v)
        if program is not None and program.id != info.data['id']:
            raise ValueError('program with this code already exists')
        return v