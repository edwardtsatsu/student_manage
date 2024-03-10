import uuid

from sqlalchemy import UUID, func, Column, ForeignKey, DateTime

from src.models.base import Base


class StudentCourse(Base):
    __tablename__ = 'student_courses'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey('students.id'))
    program_course_id = Column(UUID(as_uuid=True), ForeignKey('program_courses.id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
