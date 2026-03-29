import os


def get_file_content(working_directory, file_path):
    working_doirectory_path = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(working_doirectory_path, file_path))

    valid_target = (
        os.path.commonpath([working_doirectory_path, target_path])
        == working_doirectory_path
    )

    if valid_target != False:
        print(
            f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        )
        return

    if not os.path.isfile(valid_target):
        print(f'Error: File not found or is not a regular file: "{file_path}')

    MAX_CHAR = 1000

    with open(file_path, "r") as f:
        file_string = f.read(MAX_CHAR)

        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'
