import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.dtos.course_dto import CourseDto
from src.dtos.program_dto import ProgramDto


class ProgramCourseDto(BaseModel):
    id: uuid.UUID
    program: ProgramDto
    course: CourseDto
    created_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
