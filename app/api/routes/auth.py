from datetime import timedelta
import logging

from fastapi import APIRouter, HTTPException, Depends
from authx import AuthX, AuthXConfig, TokenPayload
from pydantic import BaseModel
from starlette.requests import Request

from app.core.config import settings

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/users",
    tags=["Auth"],
)

config = AuthXConfig(
    JWT_ALGORITHM=settings.auth_settings.JWT_ALGORITHM,
    JWT_SECRET_KEY=settings.auth_settings.JWT_SECRET_KEY,
    JWT_TOKEN_LOCATION=settings.auth_settings.JWT_TOKEN_LOCATION,
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=3)
)

auth = AuthX(config=config)


class LoginForm(BaseModel):
    username: str
    password: str


@router.post('/login')
def login(data: LoginForm):
    if data.username == "test" and data.password == "test":
        access_token = auth.create_access_token(
            data.username,
            fresh=True
        )
        refresh_token = auth.create_refresh_token(data.username)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
    raise HTTPException(401, "Bad username/password")


# Only for registered users
@router.get("/protected", dependencies=[Depends(auth.access_token_required)])
def get_protected():
    return {"message": "Hello World"}


# Get data from access token
@router.get('/profile')
def get_profile(payload: TokenPayload = Depends(auth.access_token_required)):
    print(dict(payload))
    return {
        "id": payload.sub
    }


class RefreshForm(BaseModel):
    refresh_token: str


@router.post('/refresh')
async def refresh(refresh_data: RefreshForm = None):
    refresh_token = refresh_data.refresh_token

    refresh_payload = TokenPayload.decode(
        refresh_token,
        key=settings.auth_settings.JWT_SECRET_KEY
    )

    access_token = auth.create_access_token(refresh_payload.sub)

    return {"access_token": access_token}
