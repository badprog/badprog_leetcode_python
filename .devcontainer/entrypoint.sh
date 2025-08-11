#!/bin/bash

# 
export PYTHONPYCACHEPREFIX=/workspace/pycache
mkdir -p /workspace/pycache


rm -rf /workspace/venv
python -m venv /workspace/venv
. /workspace/venv/bin/activate
pip install --no-cache-dir black isort pylint pytest pytest-cov mypy

# 
export PYTEST_CACHE_DIR=/workspace/.pytest_cache
mkdir -p /workspace/.pytest_cache

# 
export PYTHONPATH=$(/workspace/.devcontainer/identify_projects.sh | tr '\n' ':'):/workspace:/workspace/p_1_two_sum/src

# 
for project_dir in $(/workspace/.devcontainer/identify_projects.sh); do
    if [ -d "${project_dir}/tests" ]; then
        echo "Running pytest for $(basename ${project_dir})..."
        pytest "${project_dir}/tests/" -v
    fi
done

# 
for project_dir in $(/workspace/.devcontainer/identify_projects.sh); do
    if [ -d "${project_dir}/src" ]; then
        echo "Running pylint for $(basename ${project_dir})..."
        pylint --disable=C,R,W --fail-under=8.0 "${project_dir}/src"/*.py "${project_dir}/tests"/*.py
    fi
done
