import uuid

from sqlalchemy import String, func, Column, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID

from src.models.base import Base


class Program(Base):
    __tablename__ = 'programs'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    code = Column(String)
    duration_in_years = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)