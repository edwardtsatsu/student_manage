import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.dtos.program_dto import ProgramDto


class StudentDto(BaseModel):
    id: uuid.UUID
    student_code: str
    first_name: str
    last_name: str
    middle_name: Optional[str]
    email: str
    phone_number: str
    gender: str
    program: ProgramDto
    date_of_birth: datetime
    is_active: bool
    current_year: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
