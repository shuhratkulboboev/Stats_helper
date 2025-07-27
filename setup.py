from setuptools import setup, find_packages

setup(
    name="stats_helper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "stats_helper=stats_helper.cli:main",
        ],
    },
    author="Kulboboev Shukhrat",
    author_email="pmshav@example.com",
    description="A simple statistical analysis package for CSV files",
    keywords="statistics analysis csv",
)