import argparse
from core import DataLoader, Statistics
from visualization import Plotter

def main():
    parser = argparse.ArgumentParser(
        description="Stats Helper - CSV Analysis with 3 Plot Types",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("file_path", help="Path to the CSV file")
    parser.add_argument("--column", help="Analyze a specific column (generates histogram and boxplot)")
    parser.add_argument("--scatter", nargs=2, metavar=("X", "Y"),
                  help='Generate scatter plot (use quotes for columns with spaces: "sepal length (cm)")')
    parser.add_argument("--output-dir", default="plots",
                      help="Directory to save generated plots")
    
    args = parser.parse_args()
    
    # Load data
    loader = DataLoader(args.file_path)
    numeric_cols = loader.get_numeric_columns()
    
    # Create output directory
    import os
    os.makedirs(args.output_dir, exist_ok=True)

    # Column-specific analysis
    if args.column:
        column_data = loader.get_column(args.column)
        if all(isinstance(v, (int, float)) for v in column_data):
            print(f"\nStatistics for column '{args.column}':")
            print(f"Mean: {Statistics.mean(column_data):.2f}")
            print(f"Median: {Statistics.median(column_data):.2f}")
            print(f"Mode: {Statistics.mode(column_data)}")
            print(f"Variance: {Statistics.variance(column_data):.2f}")
            print(f"Standard Deviation: {Statistics.std_dev(column_data):.2f}")
            
            # Generate and save plots
            output_dir = "plots"
            os.makedirs(output_dir, exist_ok=True)
            
            Plotter.histogram(
                column_data,
                title=f"Histogram of {args.column}",
                xlabel=args.column,
                save_path=os.path.join(output_dir, f"histogram_{args.column.replace(' ', '_')}.png"),
                show=False
            )
            
            Plotter.boxplot(
                column_data,
                title=f"Boxplot of {args.column}",
                ylabel=args.column,
                save_path=os.path.join(output_dir, f"boxplot_{args.column.replace(' ', '_')}.png"),
                show=False
            )
            
            print(f"\nPlots saved to '{output_dir}' directory")
    # Full dataset analysis
    else:
        print("\nAvailable numeric columns:", ", ".join(numeric_cols))
        
        if numeric_cols:
            # Calculate statistics for all columns
            print("\nSummary Statistics:")
            stats = []
            for col in numeric_cols:
                col_data = loader.get_column(col)
                stats.append({
                    "Column": col,
                    "Mean": Statistics.mean(col_data),
                    "Median": Statistics.median(col_data),
                    "Std Dev": Statistics.std_dev(col_data)
                })
            
            # Print formatted statistics
            import pandas as pd
            print(pd.DataFrame(stats).to_string(index=False))
            
            # Correlation matrix
            numeric_data = {col: loader.get_column(col) for col in numeric_cols}
            corr_matrix = Statistics.correlation_matrix(numeric_data)
            print("\nCorrelation Matrix:")
            print(corr_matrix)
            
            # Generate default scatter plot if no columns specified
            scatter_cols = args.scatter if args.scatter else numeric_cols[:2]
            if len(scatter_cols) == 2:
                x, y = scatter_cols
                if x not in numeric_cols or y not in numeric_cols:
                    print(f"\nScatter plot skipped: Columns must be numeric. Choose from: {', '.join(numeric_cols)}")
                else:
                    Plotter.scatter(
                        loader.get_column(x),
                        loader.get_column(y),
                        save_path=os.path.join(args.output_dir, f"scatter_{x}_vs_{y}.png"),
                        title=f"{x} vs {y}",
                        xlabel=x,
                        ylabel=y,
                        show=False
                    )
                    print(f"\nSaved scatter plot: {x} vs {y}")

if __name__ == "__main__":
    main()