import uuid

from pydantic import BaseModel, ConfigDict


class RoleDto(BaseModel):
    id: uuid.UUID
    name: str

    model_config = ConfigDict(from_attributes=True)