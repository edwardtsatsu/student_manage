from sqlalchemy import select

from configs.database import db_session
from src.models import Program
from src.repositories.base_repository import BaseRepository


class ProgramRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Program)

    def find_by_code(self, code):
        return db_session.scalars(select(self.model)
                                  .where(self.model.deleted_at.is_(None))
                                  .where(self.model.code == code)).first()