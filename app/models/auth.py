import datetime

from app.db import Base, IdPkMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime
from sqlalchemy.sql import func


class User(IdPkMixin, Base):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False
    )

    is_verified: Mapped[bool] = mapped_column(
        default=False,
        nullable=False
    )

    is_superuser: Mapped[bool] = mapped_column(
        default=False,
        nullable=False
    )

    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        default=datetime.datetime.now
    )

