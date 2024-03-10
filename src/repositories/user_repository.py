from sqlalchemy import select
from sqlalchemy.orm import joinedload

from configs.database import db_session
from src.models import User, Student
from src.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=User)

    def find_by_email(self, email):
        return db_session.scalars(select(self.model)
                                  .where(self.model.deleted_at.is_(None))
                                  .where(self.model.email == email)).first()

    def find(self, id):
        return db_session.scalars(select(self.model)
                                  .options(joinedload(self.model.role))
                                  .where(self.model.deleted_at.is_(None))
                                  .where(self.model.id == id)).first()

    def find_by_phone_number(self, phone):
        return db_session.scalars(select(self.model)
                                  .where(self.model.deleted_at.is_(None))
                                  .where(self.model.phone_number == phone)).first()

    def find_student_by_student_code(self, student_code):
        return db_session.scalars(select(self.model)
                                  .options(joinedload(self.model.student))
                                  .where(self.model.deleted_at.is_(None))
                                  .where(Student.deleted_at == None)
                                  .where(Student.is_active.is_(True))
                                  .where(Student.student_code == student_code)).first()
