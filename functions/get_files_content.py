import os


def get_file_content(working_directory, file_path):

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
        print(f'Error: File not found or is not a regular file: "{file_path}')
        return

    # Number of character read from the files
    MAX_CHAR = 1000

    # Opens the file in "reading" format and stores the MAX_CHAR provided
    with open(target_path, "r") as f:
        content = f.read(MAX_CHAR)

        # Reads 1 more character after the MAX_CHAR amount and add the line that the file is truncated
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'
        print(content)
