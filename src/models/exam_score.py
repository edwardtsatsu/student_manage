import uuid

from sqlalchemy import UUID, Numeric, func, Column, ForeignKey, DateTime

from src.models.base import Base


class ExamScore(Base):
    __tablename__ = 'exam_scores'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey('students.id'))
    course_id = Column(UUID(as_uuid=True), ForeignKey('courses.id'))
    semester_id = Column(UUID(as_uuid=True), ForeignKey('semesters.id'))
    grade_id = Column(UUID(as_uuid=True), ForeignKey('grades.id'))
    score = Column(Numeric)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)