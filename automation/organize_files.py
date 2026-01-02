import os
import sys

def organize_files(source_folder, output_folder):
    if not os.path.exists(source_folder):
        print(f"Source folder not found: {source_folder}")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path):
            new_name = filename.lower().replace(" ", "_")
            destination_path = os.path.join(output_folder, new_name)
            os.rename(source_path, destination_path)

    print("Files organized successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: py organize_files.py <source_folder> <output_folder>")
    else:
        organize_files(sys.argv[1], sys.argv[2])
