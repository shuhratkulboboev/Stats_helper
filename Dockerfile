# Base image
FROM python:3.9-slim

# Install system dependencies for matplotlib
RUN apt-get update && apt-get install -y \
    libfreetype6 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application files
COPY . .

# Install package
RUN pip install -e .

# Default command
CMD ["stats-helper", "--help"]