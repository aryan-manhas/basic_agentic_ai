import os


def run_python_file(working_directory, file_path, args=None):

    # Checks the path of the working directory and creates a absolute path for the target directory
    working_doirectory_path = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(working_doirectory_path, file_path))

    # Makes sure target directory is the part of working directory
    valid_target = (
        os.path.commonpath([working_doirectory_path, target_path])
        == working_doirectory_path
    )

    # Makes sure target directory is not out of bounds
    if not valid_target:
        print(
            f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        )
        return

    # Makes sure the target directory is actually a directory
    if not os.path.isfile(target_path):
        print(f'Error: "{file_path}" does not exist or is not a regular file')
        return

    if not target_path.endswith(".py"):
        print(f'Error: "{file_path}" is not a Python file')
        return
