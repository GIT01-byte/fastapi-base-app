from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000


class DbSettings(BaseModel):
    # db_url: str = ...
    pass

class ApiPrefix(BaseModel):
    api_prefix: str = '/api'


class Settings(BaseSettings):
    run_confix: RunConfig = RunConfig()
    db_settings: DbSettings = DbSettings()
    api_prefix: ApiPrefix = ApiPrefix()


settings = Settings()
