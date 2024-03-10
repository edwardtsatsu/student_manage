import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class GradeDto(BaseModel):
    id: uuid.UUID
    grade_letter: str
    min_score: float
    max_score: float
    created_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)
