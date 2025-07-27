import matplotlib.pyplot as plt
from typing import List, Optional
import os

class Plotter:
    @staticmethod
    def histogram(data: List[float], title: str = "Histogram", 
                 xlabel: str = "Value", ylabel: str = "Frequency", 
                 bins: int = 10, save_path: Optional[str] = None, 
                 show: bool = True) -> None:
        """Generate histogram with save capability."""
        plt.figure()
        plt.hist(data, bins=bins, edgecolor='black')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)
        if show:
            plt.show()
        plt.close()

    @staticmethod
    def boxplot(data: List[float], title: str = "Boxplot", 
               ylabel: str = "Value", save_path: Optional[str] = None,
               show: bool = True) -> None:
        """Generate boxplot with save capability."""
        plt.figure()
        plt.boxplot(data)
        plt.title(title)
        plt.ylabel(ylabel)
        plt.grid(True)
        
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)
        if show:
            plt.show()
        plt.close()

    @staticmethod
    def scatter(x: List[float], y: List[float], title: str = "Scatter Plot",
               xlabel: str = "X", ylabel: str = "Y", 
               save_path: Optional[str] = None, show: bool = True) -> None:
        """Generate scatter plot with save capability."""
        plt.figure()
        plt.scatter(x, y)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)
        if show:
            plt.show()
        plt.close()