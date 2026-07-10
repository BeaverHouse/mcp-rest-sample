from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_", extra="ignore")

    name: str = "MCP REST Sample"
    version: str = "0.2.0"
    host: str = "0.0.0.0"
    port: int = 8001


settings = Settings()
