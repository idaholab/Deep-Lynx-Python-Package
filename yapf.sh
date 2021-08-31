#!/bin/bash

STATUS=`yapf --diff --recursive . --style={column_limit:120}`
if [[ ! -z $STATUS ]]; then
    echo "Run 'yapf --in-place --recursive . --style={column_limit:120}' command in the root of the repository."
    exit 1
else
    echo "SUCCESS: Passed Linter Inspection"
    exit 0
fi