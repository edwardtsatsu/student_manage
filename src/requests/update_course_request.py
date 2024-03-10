import uuid
from typing import Optional

from pydantic import BaseModel, constr, conint, field_validator
from pydantic_core.core_schema import FieldValidationInfo

from src.repositories.course_repository import CourseRepository


class UpdateCourseRequest(BaseModel):
    id: Optional[uuid.UUID]
    name: constr(strip_whitespace=True, min_length=1)
    code: constr(strip_whitespace=True, min_length=1)
    credit_hours: conint()

    @field_validator('code')
    def code_unique(cls, v, info: FieldValidationInfo):
        course_repo = CourseRepository()
        course = course_repo.find_by_code(v)
        if course is not None and course.id != info.data['id']:
            raise ValueError('course with this code already exists')
        return v