from pydantic import BaseModel, constr, conlist, field_validator

from src.repositories.program_repository import ProgramRepository
from src.repositories.semester_repository import SemesterRepository


class AssignProgramCoursesRequest(BaseModel):
    program_id: constr(strip_whitespace=True, min_length=1)
    semester_id: constr(strip_whitespace=True, min_length=1)
    courses: conlist(item_type=str, min_length=1)

    @field_validator('program_id')
    def program_exists(cls, v):
        program_repo = ProgramRepository()
        program = program_repo.find(v)
        if program is None:
            raise ValueError('program is invalid')
        return v

    @field_validator('semester_id')
    def semester_exists(cls, v):
        semester_repo = SemesterRepository()
        semester = semester_repo.find(v)
        if semester is None:
            raise ValueError('semester is invalid')
        return v