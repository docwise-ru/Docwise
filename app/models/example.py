from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Example(Base):
    __tablename__ = "examples"
    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str]

    def __str__(self):
        return f'{self.__tablename__} {self.name}'

    def __repr__(self):
        return f'{self.__tablename__} {self.name}'

