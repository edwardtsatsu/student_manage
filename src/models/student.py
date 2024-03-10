import uuid

from sqlalchemy import UUID, Boolean, String, func, Column, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship

from src.models.base import Base


class Student(Base):
    __tablename__ = 'students'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    student_code = Column(String)
    completed_at = Column(DateTime, nullable=True)
    program_id = Column(UUID(as_uuid=True), ForeignKey('programs.id'))
    gender = Column(String)
    date_of_birth = Column(DateTime)
    current_year = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    user = relationship('User', back_populates='student', uselist=False)
    program = relationship('Program', uselist=False)
