import uuid
from sqlalchemy import UUID, String, func, Column, DateTime

from src.models.base import Base

class Semester(Base):
    __tablename__ = 'semesters'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    academic_year = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
