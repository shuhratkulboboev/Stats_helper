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
- Load data from CSV files
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
1. Full Dataset Analysis:
   ```bash
   python cli.py data/iris.csv
   # Output includes:Summary statistics table,Correlation matrix, and Auto-generated scatter plot of first two numeric columns
   ```
2. Create Visualizations Example:
   Analyze Specific Column (with Auto-Generated Plots)
   ```bash
   python cli.py data.csv --column "column_name"
   # Creates:"plots/histogram_column_name.png" and "plots/boxplot_column_name.png"
   ```
3. Generate Scatter Plot
   ```bash
   python cli.py data.csv --scatter "column_x" "column_y"
   # Creates:plots/scatter_column_x_vs_column_y.png
   ```
## 🧪 Testing
   ```bash
   pytest test/ -s -v
   ```
