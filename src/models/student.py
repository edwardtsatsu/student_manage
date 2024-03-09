
import uuid
from sqlalchemy import UUID, Boolean, String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship

from src.models.base import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    student_code = Column(String)
    completed_at = Column(DateTime)
    program_id = Column(UUID(as_uuid=True), ForeignKey('programs.id'))
    gender = Column(String)
    date_of_birth = Column(String)
    active_status = Column(Boolean)
    del_status = Column(Boolean)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())