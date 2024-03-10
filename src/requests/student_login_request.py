from pydantic import BaseModel, constr


class StudentLoginRequest(BaseModel):
    student_code: constr(strip_whitespace=True, min_length=1)
    password: constr(strip_whitespace=True, min_length=1)
