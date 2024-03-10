from pydantic import BaseModel, ConfigDict


class StudentAuthDto(BaseModel):
    id: str
    name: str
    email: str
    access_token: str

    model_config = ConfigDict(from_attributes=True)
