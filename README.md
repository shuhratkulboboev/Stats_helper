# Stats_helper
# Stats Helper - Statistical Analysis Package

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Tests](https://github.com/yourusername/stats_helper/actions/workflows/tests.yml/badge.svg)
![Coverage](https://codecov.io/gh/yourusername/stats_helper/branch/main/graph/badge.svg)

A Python package for statistical analysis of CSV datasets with built-in visualization.

## ✨ Features

### Core Statistics
- Descriptive statistics (mean, median, mode)
- Dispersion metrics (variance, standard deviation)
- Correlation matrix generation

### Visualization
- Publication-ready plots:
  - Histograms
  - Boxplots
  - Scatter plots
- Customizable styling and output formats

### CLI Interface
- Load data from CSV files and used iris.csv dataset for checking and testing packages
- Generate summary statistics
- Export visualizations to files

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stats_helper.git
   cd stats_helper
   ```
2. Create and activate virtual environment (Windows):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # For development, also install:
   pip install -e
   ```
## 🛠 Usage
Here , the column name can be changed based on users desire , if another dataset is used for testing, it is enough to change path of dataset and respective column name.
1. Full Dataset Analysis:
   ```bash
   python cli.py data/iris.csv
   # Output includes:Summary statistics table,Correlation matrix, and Auto-generated scatter plot of first two numeric columns
   ```
2. Create Visualizations Example:
   Analyze Specific Column (with Auto-Generated Plots)
   ```bash
   python cli.py data.csv --column "sepal length (cm)"
   # Creates:"plots/histogram_sepal_length.png" and "plots/boxplot_sepal_length.png"
   ```
3. Generate Scatter Plot
   ```bash
   python cli.py data.csv --scatter "sepal length (cm)" "sepal width (cm)"
   # Creates:plots/scatter_sepal_length_vs_sepal_width.png
   ```
## 🧪 Testing
   ```bash
   pytest test/ -s -v
   ```
