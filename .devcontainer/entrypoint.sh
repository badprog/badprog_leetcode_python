#!/bin/bash

# 
export PYTHONPYCACHEPREFIX=/workspace/pycache
mkdir -p /workspace/pycache

# Force remove and create virtual env
rm -rf /workspace/venv
python -m venv /workspace/venv
. /workspace/venv/bin/activate
pip install --no-cache-dir black isort pylint pytest pytest-cov mypy

# Configure pytest cache
export PYTEST_CACHE_DIR=/workspace/.pytest_cache
mkdir -p /workspace/.pytest_cache

# Copy dynamically the sub-projects (p_[0-9]*_*)
for project_dir in /workspace/p_[0-9]*_*; do
    if [ -d "$project_dir" ]; then
        project_name=$(basename "$project_dir")
        echo "Copying project $project_name to /workspace/$project_name..."
        cp -r "$project_dir" "/workspace/$project_name"
    else
        echo "No project directories found in /workspace/p_[0-9]*_*"
    fi
done

# Generate PYTHONPATH dynamically
export PYTHONPATH=$(/workspace/.devcontainer/identify_projects.sh | tr '\n' ':'):/workspace:/workspace/p_1_two_sum/src

# Run tests
for project_dir in $(/workspace/.devcontainer/identify_projects.sh); do
    if [ -d "${project_dir}/tests" ]; then
        echo "Running tests for $(basename ${project_dir})..."
        pytest "${project_dir}/tests/" -v
    else
        echo "No tests directory found in $project_dir"
    fi
done
