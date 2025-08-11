#!/bin/bash

# List every folder as p_[0-9]*_* in /workspace
for project_dir in /workspace/p_[0-9]*_*; do
    if [ -d "$project_dir" ]; then
        echo "$project_dir"
    fi
done