import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CourseDto(BaseModel):
    id: uuid.UUID
    name: str
    code: str
    credit_hours: int
    created_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)
