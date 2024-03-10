from pydantic import BaseModel, constr


class UpdateSemesterRequest(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    academic_year: constr(strip_whitespace=True, min_length=1)
