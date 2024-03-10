import uuid

from pydantic import BaseModel, constr, field_validator, confloat
from pydantic_core.core_schema import FieldValidationInfo

from src.repositories.grade_repository import GradeRepository


class UpdateGradeRequest(BaseModel):
    grade_letter: constr(strip_whitespace=True, max_length=2)
    min_score: confloat()
    max_score: confloat()
    id: uuid.UUID

    @field_validator('grade_letter')
    def unique_grade_letter(cls, v, info: FieldValidationInfo):
        grade_repo = GradeRepository()
        grade = grade_repo.find_by_grade_letter(v)

        if grade is not None and grade.id != info.data['id']:
            raise ValueError('grade letter already exists')
        return v

    @field_validator('min_score')
    def validate_min_score(cls, v, info: FieldValidationInfo):
        max_score = info.data['max_score']
        if v > max_score:
            raise ValueError('min score cannot be greater than max score')
        return v

    @field_validator('max_score')
    def validate_max_score(cls, v, info: FieldValidationInfo):
        min_score = info.data['min_score']
        if v < min_score:
            raise ValueError('max score cannot be lesser than min score')
        return v
