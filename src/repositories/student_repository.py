from sqlalchemy import select, desc
from sqlalchemy.orm import joinedload

from configs.database import db_session
from src.models import Student
from src.repositories.base_repository import BaseRepository
from utils import get_offset


class StudentRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Student)

    def find_all(self, query=None):
        db_query = select(self.model) \
            .options(joinedload(self.model.program), joinedload(self.model.user)) \
            .where(self.model.deleted_at.is_(None)) \
            .order_by(desc(self.model.id))

        return self.__parse_query(db_query, query)

    def find(self, id):
        return db_session.scalars(select(self.model)
                                  .options(joinedload(self.model.program), joinedload(self.model.user))
                                  .where(self.model.deleted_at.is_(None))
                                  .where(self.model.id == id)).first()

    def __parse_query(self, db_query, query=None):
        if query is None:
            return db_session.scalars(db_query).unique().all()

        if query.get('program_id', '') != '':
            db_query = db_query.where(self.model.program_id == query['program_id'])

        if query.get('paginate') is True and query.get('per_page', 20) != '':
            per_page = int(query.get('per_page', 20))
            offset = get_offset(query.get('page', 1), per_page)
            db_query = db_query.offset(offset).limit(per_page)

        return db_session.scalars(db_query).unique().all()