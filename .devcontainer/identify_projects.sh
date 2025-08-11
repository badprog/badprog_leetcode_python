#!/bin/bash

# List every folder as p_[0-9]*_*
for project_dir in p_[0-9]*_*; do
    if [ -d "$project_dir" ]; then
        echo "$PWD/$project_dir"
    fi
done