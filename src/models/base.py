from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...
#     pass
   
#  # def to_json(self):
#     #     return {col.name: getattr(self, col.name) for col in self.__table__.columns}