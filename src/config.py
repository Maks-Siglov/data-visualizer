from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# Get project root directory
PROJECT_ROOT = Path(__file__).parent.parent


class Config(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application settings
    app_host: str
    app_port: int
    app_debug: bool

    # CSV Data source settings
    csv_file_path: str
    csv_encoding: str

    model_config = SettingsConfigDict(
        env_file=str(PROJECT_ROOT / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
        )

    @field_validator('csv_file_path')
    @classmethod
    def resolve_csv_path(cls, v: str) -> str:
        """Resolve CSV file path to absolute path."""
        csv_path = Path(v)
        if csv_path.is_absolute():
            return str(csv_path)
        return str(PROJECT_ROOT / v)


config = Config()
