import pytest
import numpy as np
import pandas as pd
from stats_helper.core import Statistics

def test_data_loader_iris(iris_loader, iris_numeric_columns):
    """Test DataLoader with Iris dataset."""
    # Test column loading
    assert set(iris_loader.data.keys()) == set(iris_numeric_columns + ['species'])
    assert iris_loader.get_numeric_columns() == iris_numeric_columns
    
    # Test column data
    sepal_length = iris_loader.get_column(iris_numeric_columns[0])
    assert len(sepal_length) == 150  # 150 samples
    assert all(isinstance(x, float) for x in sepal_length)

def test_statistics_with_iris(iris_loader, iris_numeric_columns, iris_known_stats):
    """Test Statistics calculations against known Iris dataset values."""
    # Test sepal length statistics
    sepal_length = iris_loader.get_column(iris_numeric_columns[0])
    
    # Test with relative tolerance for floating point comparisons
    assert pytest.approx(Statistics.mean(sepal_length), rel=1e-4) == iris_known_stats['sepal_length']['mean']
    assert pytest.approx(Statistics.median(sepal_length), rel=1e-2) == iris_known_stats['sepal_length']['median']
    assert pytest.approx(Statistics.std_dev(sepal_length), rel=1e-4) == iris_known_stats['sepal_length']['std']
    
    # Test petal width statistics
    petal_width = iris_loader.get_column(iris_numeric_columns[3])
    assert pytest.approx(Statistics.mean(petal_width), rel=1e-4) == iris_known_stats['petal_width']['mean']
    assert pytest.approx(Statistics.median(petal_width), rel=1e-2) == iris_known_stats['petal_width']['median']

def test_correlation_matrix_iris(iris_loader, iris_numeric_columns):
    """Test correlation matrix calculation with Iris data."""
    numeric_data = {col: iris_loader.get_column(col) for col in iris_numeric_columns}
    corr_matrix = Statistics.correlation_matrix(numeric_data)
    
    # Basic checks on correlation matrix
    assert corr_matrix.shape == (4, 4)  # 4 numeric columns
    assert (corr_matrix.values.diagonal() == 1.0).all()  # Diagonal should be 1
    
    # Test known correlations in Iris dataset
    # Sepal length and petal length should be highly correlated
    assert corr_matrix.iloc[0, 2] > 0.8  # sepal length vs petal length
    # Sepal width and petal width should be less correlated
    assert abs(corr_matrix.iloc[1, 3]) < 0.6  # sepal width vs petal width

def test_empty_data_handling():
    """Test statistics with empty data (still needed for coverage)."""
    from stats_helper.core import Statistics
    with pytest.raises(ValueError):
        Statistics.mean([])
    with pytest.raises(ValueError):
        Statistics.median([])