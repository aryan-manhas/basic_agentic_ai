import os


def get_files_info(working_directory, directory="."):
    working_directory_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_path, directory))

    valid_target_dir = (
        os.path.commonpath([working_directory_path, target_dir])
        == working_directory_path
    )

    if valid_target_dir is False:
        print(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )
