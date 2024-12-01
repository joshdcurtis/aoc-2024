#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide a number as an argument."
    echo "Usage: $0 <number>"
    exit 1
fi

# Store the argument in a variable
n=$1

# Define the script path
script_path="./src/${n}.py"

# Define the input file path
input_path="./inputs/${n}.txt"

# Check if the script exists
if [ ! -f "$script_path" ]; then
    echo "Error: Script $script_path does not exist."
    exit 1
fi

# Check if the input file exists
if [ ! -f "$input_path" ]; then
    echo "Error: Input file $input_path does not exist."
    exit 1
fi

# Run the Python script with the input file path
python3 "$script_path" "$input_path"
