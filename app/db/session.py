from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from app.core.config import settings


class DBHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
            class_=AsyncSession
        )

    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session


db_helper = DBHelper(
    settings.db_url,
    settings.ECHO
)
