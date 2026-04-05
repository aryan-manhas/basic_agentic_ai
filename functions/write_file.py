import os


def write_file(working_directory, file_path, content):
    try:
        # Checks the path of the working directory and creates a absolute path for the target directory
        working_doirectory_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_doirectory_path, file_path))

        # Makes sure target directory is the part of working directory
        valid_target = (
            os.path.commonpath([working_doirectory_path, target_path])
            == working_doirectory_path
        )

        # Makes sure target file is not out of bounds
        if not valid_target:
            print(
                f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            )
            return

        # Makes sure the target file is actually a file and not a directory
        if os.path.isdir(target_path):
            print(f'Error: Cannot write to "{file_path}" as it is a directory')
            return

        # Makes a directory for every part of the target path if they don't exist
        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        # Open the file in the writing mode and writes the content
        with open(target_path, "w") as f:
            f.write(content)
            print(
                f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            )

    except:
        print("Error: Standard Library Function Error.")
