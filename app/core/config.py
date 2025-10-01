"""Application configuration module."""

from typing import List, Optional

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

    # API documentation settings
    CONTACT_NAME: Optional[str] = None
    CONTACT_EMAIL: Optional[str] = None
    CONTACT_URL: Optional[str] = None
    LICENSE_NAME: Optional[str] = None
    LICENSE_URL: Optional[str] = None
    TERMS_OF_SERVICE: Optional[str] = None

    # Environment
    ENVIRONMENT: str = "development"

    @property
    def cors_origins_list(self) -> List[str]:
        """Get CORS origins as a list."""
        if self.BACKEND_CORS_ORIGINS == "*":
            return ["*"]
        origins = self.BACKEND_CORS_ORIGINS.split(",")
        return [origin.strip() for origin in origins]

    @property
    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.ENVIRONMENT.lower() in ("production", "prod")

    class Config:
        """Pydantic config."""

        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings()
