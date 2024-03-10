import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SemesterDto(BaseModel):
    id: uuid.UUID
    name: str
    academic_year: str
    created_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
