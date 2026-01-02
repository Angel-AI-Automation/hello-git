# Automation Scripts

This directory contains Python automation scripts designed to solve practical file management problems.
These scripts are written with clean structure, readability, and real-world usage in mind.

## Script: organize_files.py

### Description
This script automatically organizes files from an input directory into an output directory.
Files are renamed using a standardized format and moved according to simple automation rules.

### How it works
1. Reads all files from the `files_input` directory
2. Normalizes file names (lowercase, underscores instead of spaces)
3. Moves processed files into the `files_output` directory
4. Prevents crashes by validating folder existence

### Usage
From the project root, run:

```bash
py automation/organize_files.py
