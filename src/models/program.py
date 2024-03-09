import datetime
import uuid
from sqlalchemy import Boolean, String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


from src.models.base import Base

class Program(Base):
    __tablename__ = 'programs'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    code = Column(String)
    duration = Column(String)
    active_status = Column(Boolean)
    del_status = Column(Boolean)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())