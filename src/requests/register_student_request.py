from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, constr, field_validator

from src.repositories.program_repository import ProgramRepository
from src.repositories.user_repository import UserRepository


class RegisterStudentRequest(BaseModel):
    first_name: constr(strip_whitespace=True, min_length=1)
    last_name: constr(strip_whitespace=True, min_length=1)
    middle_name: Optional[str]
    email: EmailStr
    phone_number: constr(strip_whitespace=True, min_length=10)
    program_id: constr(strip_whitespace=True, min_length=1)
    gender: constr(strip_whitespace=True, min_length=1)
    date_of_birth: datetime

    @field_validator('email')
    def email_unique(cls, v):
        user_repo = UserRepository()
        user = user_repo.find_by_email(v)
        if user is not None:
            raise ValueError('email already taken')
        return v

    @field_validator('gender')
    def gender_valid(cls, v):
        accepted = ['male', 'female', 'other']
        if v not in accepted:
            raise ValueError('gender is invalid')
        return v

    @field_validator('phone_number')
    def phone_number_unique(cls, v):
        user_repo = UserRepository()
        user = user_repo.find_by_phone_number(v)
        if user is not None:
            raise ValueError('phone number already taken')
        return v

    @field_validator('program_id')
    def program_exists(cls, v):
        program_repo = ProgramRepository()
        user = program_repo.find(v)
        if user is None:
            raise ValueError('program does not exists')
        return v

