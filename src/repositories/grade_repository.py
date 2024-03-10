from sqlalchemy import select

from configs.database import db_session
from src.models import Grade
from src.repositories.base_repository import BaseRepository


class GradeRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Grade)

    def find_by_grade_letter(self, grade_letter):
        return db_session.scalars(select(self.model)
                                  .where(self.model.deleted_at.is_(None))
                                  .where(self.model.grade_letter == grade_letter)).first()