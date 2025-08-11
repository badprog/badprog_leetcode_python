# Base image
FROM python:3.11

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    tree \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy project files
COPY . .

# Create and activate virtual environment
RUN python -m venv /workspace/venv
ENV PATH="/workspace/venv/bin:$PATH"

# Install Python tools
RUN pip install black isort pylint pytest pytest-cov mypy

# Command
