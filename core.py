import csv
from typing import Dict, List, Union
import numpy as np
import pandas as pd

class DataLoader:
    """Load and manage data from CSV files."""
    
    def __init__(self, file_path: str):
        """
        Initialize DataLoader with CSV file path.
        
        Args:
            file_path (str): Path to the CSV file
        """
        self.file_path = file_path
        self.data = self._load_data()
        
    def _load_data(self) -> Dict[str, List[Union[float, str]]]:
        """
        Load data from CSV file into a dictionary of columns.
        
        Returns:
            Dict[str, List[Union[float, str]]]: Dictionary with column names as keys
        """
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = {field: [] for field in reader.fieldnames}
            for row in reader:
                for field in reader.fieldnames:
                    try:
                        data[field].append(float(row[field]))
                    except ValueError:
                        data[field].append(row[field])
        return data
    
    def get_numeric_columns(self) -> List[str]:
        """Get list of column names with numeric data."""
        return [col for col, values in self.data.items() 
                if all(isinstance(v, (int, float)) for v in values)]
    
    def get_column(self, column_name: str) -> List[Union[float, str]]:
        """Get data from a specific column."""
        return self.data.get(column_name, [])


class Statistics:
    """Core statistical analysis functions."""
    
    @staticmethod
    def mean(data: List[float]) -> float:
        """Calculate mean of a numeric list.
        
        Args:
            data: List of numeric values
            
        Returns:
            float: Mean of the data
            
        Raises:
            ValueError: If input data is empty
        """
        if not data:
            raise ValueError("Cannot calculate mean of empty data")
        return np.mean(data)

    @staticmethod
    def median(data: List[float]) -> float:
        """Calculate median of a numeric list.
        
        Args:
            data: List of numeric values
            
        Returns:
            float: Median of the data
            
        Raises:
            ValueError: If input data is empty
        """
        if not data:
            raise ValueError("Cannot calculate median of empty data")
        return np.median(data)

    @staticmethod
    def mode(data: List[float]) -> List[float]:
        """Calculate mode(s) of a numeric list.
        
        Args:
            data: List of numeric values
            
        Returns:
            List[float]: Mode(s) of the data (may be multiple)
            
        Raises:
            ValueError: If input data is empty
        """
        if not data:
            raise ValueError("Cannot calculate mode of empty data")
        values, counts = np.unique(data, return_counts=True)
        max_count = np.max(counts)
        return list(values[counts == max_count])

    @staticmethod
    def variance(data: List[float], ddof: int = 1) -> float:
        """Calculate variance of a numeric list.
        
        Args:
            data: List of numeric values
            ddof: Delta degrees of freedom (0 for population, 1 for sample)
            
        Returns:
            float: Variance of the data
            
        Raises:
            ValueError: If input data is empty
        """
        if not data:
            raise ValueError("Cannot calculate variance of empty data")
        return np.var(data, ddof=ddof)

    @staticmethod
    def std_dev(data: List[float], ddof: int = 1) -> float:
        """Calculate standard deviation of a numeric list.
        
        Args:
            data: List of numeric values
            ddof: Delta degrees of freedom (0 for population, 1 for sample)
            
        Returns:
            float: Standard deviation of the data
            
        Raises:
            ValueError: If input data is empty
        """
        if not data:
            raise ValueError("Cannot calculate standard deviation of empty data")
        return np.std(data, ddof=ddof)
    
    @staticmethod
    def correlation_matrix(data: Dict[str, List[float]]) -> pd.DataFrame:
        """
        Calculate correlation matrix between numeric columns.
        
        Args:
            data: Dictionary with column names as keys and numeric lists as values
            
        Returns:
            pandas.DataFrame: Correlation matrix
        """
        df = pd.DataFrame(data)
        return df.corr()