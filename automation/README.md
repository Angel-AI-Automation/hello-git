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
### Command-line usage

This script supports command-line arguments, making it reusable in different environments:

```bash
py automation/organize_files.py files_input files_output
This approach allows flexible automation without modifying the source code.

### Safe execution (dry-run)

The script supports a dry-run mode that allows previewing file operations
without making any changes:

```bash
py automation/organize_files.py files_input files_output --dry-run
This feature is useful for preventing accidental file modifications
in production environments.