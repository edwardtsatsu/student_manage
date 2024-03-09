import uuid
from sqlalchemy import UUID, Numeric, String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship

from src.models.base import Base

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    min_score = Column(Numeric)
    max_score = Column(Numeric)
    grade_letter = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
