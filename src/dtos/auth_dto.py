import uuid

from pydantic import BaseModel, ConfigDict

from src.dtos.role_dto import RoleDto


class AuthDto(BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    email: str
    role: RoleDto
    access_token: str

    model_config = ConfigDict(from_attributes=True)
