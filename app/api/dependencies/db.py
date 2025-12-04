from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import session_dependency

SessionDep = Annotated[AsyncSession, Depends(session_dependency)]
