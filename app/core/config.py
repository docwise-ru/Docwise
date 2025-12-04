from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

ENV_DIR = Path(__file__).resolve().parent.parent.parent


class AuthSettings(BaseModel):
    lifetime_seconds: int = 3600
    RESET_PASSWORD_TOKEN_SECRET: str
    VERIFICATION_TOKEN_SECRET: str
    tokenUrl: str = "users/login"


class Settings(BaseSettings):
    ECHO: bool = False

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    auth_settings: AuthSettings

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(
        env_file=ENV_DIR / ".env",
        extra="ignore",
        env_nested_delimiter="__"
    )


settings = Settings()
