"""Application configuration module."""

from typing import Annotated, List

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "GA Python Template"
    PROJECT_DESCRIPTION: str = (
        "Simple python template / project for testing github actions"
    )
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    # CORS settings - use string type to avoid JSON parsing issues
    BACKEND_CORS_ORIGINS: str = "*"

    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False

    @property
    def cors_origins_list(self) -> List[str]:
        """Get CORS origins as a list."""
        if self.BACKEND_CORS_ORIGINS == "*":
            return ["*"]
        return [origin.strip() for origin in self.BACKEND_CORS_ORIGINS.split(",")]

    class Config:
        """Pydantic config."""

        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings()
