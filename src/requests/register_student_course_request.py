import uuid

from pydantic import BaseModel, constr, field_validator, conlist

from src.repositories.course_repository import CourseRepository


class RegisterStudentCourseRequest(BaseModel):
    semester_id: constr(strip_whitespace=True, min_length=1)
    courses: conlist(min_length=1, item_type=uuid.UUID)

    @field_validator('courses')
    def code_unique(cls, v):
        course_repo = CourseRepository()
        courses = course_repo.find_by_id_in(v)
        for index, course in enumerate(courses):
            if course not in courses:
                raise ValueError(f'course at index {index} is invalid')
        return v
