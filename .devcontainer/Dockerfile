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

# Copy and make scripts executable
COPY .devcontainer/identify_projects.sh /workspace/.devcontainer/
COPY .devcontainer/entrypoint.sh /workspace/.devcontainer/
RUN chmod +x /workspace/.devcontainer/identify_projects.sh /workspace/.devcontainer/entrypoint.sh