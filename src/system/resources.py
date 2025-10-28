"""Dependency injection container configuration."""
from dependency_injector import containers, providers

from src.config import Config
from src.data_source.csv import CSVDataSource
from src.services.visualization import VisualizationService


class IoCContainer(containers.DeclarativeContainer):
    """IoC Container for dependency injection."""

    wiring_config = containers.WiringConfiguration(
        packages=["src.api"]
        )

    # Configuration
    config: Config = providers.Configuration()

    # Data source
    data_source = providers.Singleton(
        CSVDataSource,
        file_path=config.csv_file_path,
        encoding=config.csv_encoding
        )

    # Visualization service
    visualization_service = providers.Factory(
        VisualizationService,
        data_source=data_source
        )
