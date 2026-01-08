# File Organizer Automation Script (Python)

## Overview
This project is a Python automation script designed to organize files automatically by type, helping reduce manual work, human errors, and time wasted managing unstructured folders.

## Why This Project Matters
Manual file organization is a common but inefficient task in many workplaces.
This script demonstrates how automation can reduce human error, save time, and improve daily productivity using Python tools.

## Problem Statement
In many real-world environments, files are often stored in a single directory without proper organization. This leads to disorganization, repetitive manual tasks, increased errors, and reduced productivity.

## Solution
The script scans a source folder, identifies files based on their extensions, and moves them into categorized folders inside an output directory. This automation minimizes repetitive work and improves file management efficiency.

## Features
- Automatic file organization by file extension
- Command-line interface support
- Clear and reusable automation logic
- Simple folder-based workflow
- Easily extendable for future improvements

## How to Run
```bash
py automation/organize_files.py files_input files_output
```
Make sure both folders exist before running the script.

## Use Cases
- Office and administrative environments
- Universities and academic institutions
- Freelancers managing multiple document types
- Small businesses and personal productivity workflows

## Technologies Used
- Python
- Standard libraries (os, sys)
- Command-line execution
- Git & GitHub

## Future Improvements
- Logging system for file operations
- Support for additional file formats
- Improved CLI arguments
- Optional user interface

## Code Design Notes

- The script uses clear function separation to improve readability.
- Early exits are applied to avoid unnecessary processing.
- The project is intentionally kept simple to ensure maintainability.