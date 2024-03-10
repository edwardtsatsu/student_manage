import uuid

from sqlalchemy import String, func, Column, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_id = Column(UUID(as_uuid=True), ForeignKey('roles.id'))
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String, nullable=True)
    email = Column(String)
    phone_number = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    role = relationship('Role', back_populates='users')
    student = relationship('Student', back_populates='user', uselist=False)