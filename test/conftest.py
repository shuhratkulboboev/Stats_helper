import pytest
import os
import pandas as pd
import warnings
from sklearn.datasets import load_iris
import matplotlib
matplotlib.use('Agg')  # Set non-interactive backend

# Suppress matplotlib warning about non-interactive backend
warnings.filterwarnings("ignore", message="FigureCanvasAgg is non-interactive")
@pytest.fixture(scope="session")
def image_output_dir():
    """Persistent output directory for visual inspection"""
    import os
    output_dir = os.path.join(os.path.dirname(__file__), "test_output")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir
    
@pytest.fixture(scope="module")
def iris_data_path(tmp_path_factory):
    """Create iris dataset fixture."""
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target_names[iris.target]
    
    path = tmp_path_factory.mktemp("data") / "iris.csv"
    df.to_csv(path, index=False)
    return str(path)

@pytest.fixture
def iris_loader(iris_data_path):
    """Fixture providing loaded Iris data."""
    from stats_helper.core import DataLoader
    return DataLoader(iris_data_path)

@pytest.fixture
def iris_numeric_columns():
    """Known numeric columns in Iris dataset."""
    return ['sepal length (cm)', 'sepal width (cm)', 
            'petal length (cm)', 'petal width (cm)']

@pytest.fixture
def iris_known_stats():
    """Known statistical values for Iris dataset."""
    return {
        'sepal_length': {
            'mean': 5.843333,
            'median': 5.80,
            'std': 0.828066,
            'min': 4.3,
            'max': 7.9
        },
        'petal_width': {
            'mean': 1.199333,
            'median': 1.30,
            'std': 0.762238,
            'min': 0.1,
            'max': 2.5
        }
    }