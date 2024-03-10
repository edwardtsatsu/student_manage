import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class StudentCourseDto(BaseModel):
    id: uuid.UUID
    model_config = ConfigDict(from_attributes=True)
