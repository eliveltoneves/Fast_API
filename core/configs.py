from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:reuza1908@localhost:5432/faculdade'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = '4-oqwhZmrvcwqATC9gBOQGU4E9W-gEPYFosDF4BD2Gg'
    """
    Biblioteca do python geradora de secrets para utilizar na API na geração de TOKEN 

    import secrets

    token: str = secrets.token_urlsafe(32)
    
    """

    ALGORITHM: str = 'HS256'
    # 60 min * 24 hrs * 7 dias => 1 Semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()
