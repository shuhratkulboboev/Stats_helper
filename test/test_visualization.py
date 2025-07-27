import os
import matplotlib.pyplot as plt

def test_iris_histogram(iris_loader, iris_numeric_columns, image_output_dir):
    sepal_length = iris_loader.get_column(iris_numeric_columns[0])
    
    output_path = os.path.join(image_output_dir, "iris_sepal_length_histogram.png")
    
    # Debug: Print the actual save path
    print(f"\nSaving histogram to: {output_path}")
    
    plt.figure()
    plt.hist(sepal_length, bins=15)
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    # Enhanced verification
    assert os.path.exists(output_path), f"File not found at {output_path}"
    assert os.path.getsize(output_path) > 1024, "File too small (likely empty)"
    
    # Verify file is actually a PNG
    with open(output_path, 'rb') as f:
        assert f.read(4) == b'\x89PNG', "Not a valid PNG file"

def test_iris_boxplot(iris_loader, iris_numeric_columns, image_output_dir):
    """Test boxplot generation with Iris data and save output."""
    sepal_width = iris_loader.get_column(iris_numeric_columns[1])
    
    # Generate plot
    plt.figure()
    plt.boxplot(sepal_width)
    plt.title("Iris Sepal Width")
    plt.ylabel("Width (cm)")
    plt.grid(True)
    
    # Save plot
    output_path = os.path.join(image_output_dir, "iris_sepal_width_boxplot.png")
    plt.savefig(output_path)
    plt.close()
    
    # Verify file was created
    assert os.path.exists(output_path)
    assert os.path.getsize(output_path) > 0

def test_iris_scatter_plot(iris_loader, iris_numeric_columns, image_output_dir):
    """Test scatter plot generation with Iris data and save output."""
    petal_length = iris_loader.get_column(iris_numeric_columns[2])
    petal_width = iris_loader.get_column(iris_numeric_columns[3])
    
    # Generate plot
    plt.figure()
    plt.scatter(petal_length, petal_width)
    plt.title("Iris Petal Dimensions")
    plt.xlabel("Length (cm)")
    plt.ylabel("Width (cm)")
    plt.grid(True)
    
    # Save plot
    output_path = os.path.join(image_output_dir, "iris_petal_scatter.png")
    plt.savefig(output_path)
    plt.close()
    
    # Verify file was created
    assert os.path.exists(output_path)
    assert os.path.getsize(output_path) > 0