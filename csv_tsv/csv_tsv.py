import csv
import os
import argparse

# Default hardcoded paths
DEFAULT_INPUT_PATH = "./input.csv"  # Adjust this to your input CSV
DEFAULT_OUTPUT_FOLDER = "converted_files"  # The folder where the TSV will be saved (relative to the script location)

# Set up argument parser
parser = argparse.ArgumentParser(description="Convert CSV to TSV (UTF-16 encoded).")
parser.add_argument('--input', default=DEFAULT_INPUT_PATH, help=f'Path to input CSV file (default: {DEFAULT_INPUT_PATH})')
parser.add_argument('--output-folder', default=DEFAULT_OUTPUT_FOLDER, help=f'Folder to save TSV (default: {DEFAULT_OUTPUT_FOLDER})')

args = parser.parse_args()

# Get the absolute path of the script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Use the script's directory as the base for the output folder
output_folder_path = os.path.join(script_dir, args.output_folder)

# Extract the filename (without extension) from the input path
input_filename = os.path.basename(args.input)
output_filename = os.path.splitext(input_filename)[0] + ".tsv"  # Change .csv to .tsv

# Build output file path
output_path = os.path.join(output_folder_path, output_filename)

# Ensure the output directory exists (create it if it doesn't)
os.makedirs(output_folder_path, exist_ok=True)

# Convert CSV to TSV with UTF-16 encoding
with open(args.input, 'r', encoding='utf-8') as csvin, open(output_path, 'w', newline='', encoding='utf-16') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')
    
    for row in csvin:
        tsvout.writerow(row)

print(f"✅ CSV converted to UTF-16 TSV and saved at: {output_path}")
