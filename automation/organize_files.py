import os
import sys

def organize_files(source_folder, output_folder, dry_run=False):
    if not os.path.exists(source_folder):
        print(f"Source folder not found: {source_folder}")
        return

    if not os.path.exists(output_folder):
        if dry_run:
            print(f"[DRY-RUN] Would create folder: {output_folder}")
        else:
            os.makedirs(output_folder)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path):
            new_name = filename.lower().replace(" ", "_")
            destination_path = os.path.join(output_folder, new_name)

            if dry_run:
                print(f"[DRY-RUN] Would move: {filename} → {destination_path}")
            else:
                os.rename(source_path, destination_path)

    if dry_run:
        print("Dry-run completed. No files were modified.")
    else:
        print("Files organized successfully!")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: py organize_files.py <source_folder> <output_folder> [--dry-run]")
    else:
        source = sys.argv[1]
        output = sys.argv[2]
        dry_run_flag = "--dry-run" in sys.argv

        organize_files(source, output, dry_run=dry_run_flag)

