from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000


class DbSettings(BaseModel):
    # url: str = ...
    pass


class ApiPrefix(BaseModel):
    prefix: str = '/api'


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DbSettings = DbSettings()
    api: ApiPrefix = ApiPrefix()


settings = Settings()
