from abc import ABC, abstractmethod

import pandas as pd


class DataSource(ABC):
    """Abstract interface for data sources."""

    @abstractmethod
    def load_data(self) -> pd.DataFrame:
        """Load and return data as a pandas DataFrame.

        Returns:
            pd.DataFrame: The loaded data
        """
        pass
