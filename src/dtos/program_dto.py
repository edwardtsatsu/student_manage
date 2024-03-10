import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProgramDto(BaseModel):
    id: uuid.UUID
    name: str
    code: str
    duration_in_years: Optional[int]
    created_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
