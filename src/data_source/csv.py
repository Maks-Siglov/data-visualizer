import pandas as pd

from src.data_source.base import DataSource


class CSVDataSource(DataSource):
    """Concrete implementation for CSV file data source."""

    def __init__(self, file_path: str, encoding: str = 'utf-8'):
        """Initialize CSV data source.

        Args:
            file_path: Path to the CSV file
            encoding: File encoding (default: utf-8)
        """
        self.file_path = file_path
        self.encoding = encoding
        self._data = None

    def load_data(self) -> pd.DataFrame:
        """Load data from CSV file.

        Returns:
            pd.DataFrame: The loaded data

        Raises:
            FileNotFoundError: If the CSV file doesn't exist
            pd.errors.ParserError: If the CSV file is malformed
        """
        if self._data is None:
            self._data = pd.read_csv(self.file_path, encoding=self.encoding)
        return self._data
