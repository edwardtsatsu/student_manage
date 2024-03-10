import uuid

from sqlalchemy import UUID, func, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.models.base import Base


class ProgramCourse(Base):
    __tablename__ = 'program_courses'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    program_id = Column(UUID(as_uuid=True), ForeignKey('programs.id'))
    course_id = Column(UUID(as_uuid=True), ForeignKey('courses.id'))
    semester_id = Column(UUID(as_uuid=True), ForeignKey('semesters.id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    program = relationship('Program', uselist=False)
    semester = relationship('Semester', uselist=False)
    course = relationship('Course', uselist=False)
