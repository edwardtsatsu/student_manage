from pydantic import BaseModel, constr, conint, field_validator

from src.repositories.course_repository import CourseRepository


class StoreCourseRequest(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    code: constr(strip_whitespace=True, min_length=1)
    credit_hours: conint()

    @field_validator('code')
    def code_unique(cls, v):
        course_repo = CourseRepository()
        course = course_repo.find_by_code(v)
        if course is not None:
            raise ValueError('course with this code already exists')
        return v
