import os


def rename_files_in_directory(directory_path):
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"[!] Error: Directory '{directory_path}' does not exist.")
        return

    # Get a list of files in the directory
    files = os.listdir(directory_path)
    files.sort()  # Sort for predictable order
    print(f"Found {len(files)} files.")

    # Rename files
    for index, filename in enumerate(files):
        # Define the full path to the current file
        old_file_path = os.path.join(directory_path, filename)

        # Skip folders, if any exist
        if not os.path.isfile(old_file_path):
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1]

        # Form the new name
        new_filename = f"{index}{file_extension}"
        new_file_path = os.path.join(directory_path, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_filename}")

    print("\n[+] Renaming completed!")


# Specify the path to the directory with files
directory = "/home/path_to_your_folder/"
rename_files_in_directory(directory)
