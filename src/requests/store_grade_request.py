from pydantic import BaseModel, constr, field_validator, confloat
from pydantic_core.core_schema import FieldValidationInfo

from src.repositories.grade_repository import GradeRepository


class StoreGradeRequest(BaseModel):
    grade_letter: constr(strip_whitespace=True, max_length=2)
    min_score: confloat()
    max_score: confloat()

    @field_validator('grade_letter')
    def unique_grade_letter(cls, v):
        grade_repo = GradeRepository()
        grade = grade_repo.find_by_grade_letter(v)

        if grade is not None:
            raise ValueError('grade letter already exists')
        return v

    @field_validator('max_score')
    def validate_max_score(cls, v, info: FieldValidationInfo):
        min_score = info.data['min_score']
        if v < min_score:
            raise ValueError('max score cannot be lesser than min score')
        return v
