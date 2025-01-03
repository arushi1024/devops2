#!/bin/bash
echo "Running tests..."
python -m unittest discover -s . -p "test_*.py"

