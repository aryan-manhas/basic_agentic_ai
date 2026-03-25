import os


def get_files_info(working_directory, directory="."):

    # Checks the path of the working directory and creates a absolute path for the target directory
    working_directory_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_path, directory))

    # Makes sure target directory is the part of working directory
    valid_target_dir = (
        os.path.commonpath([working_directory_path, target_dir])
        == working_directory_path
    )

    # Function for the output semantics
    if directory == ".":
        print("Result for current directory:")
    else:
        print(f"Result for {directory} directory:")

    # Makes sure target directory is not out of bounds
    if valid_target_dir is False:
        print(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )
        return

    # Makes sure the target directory is actually a directory
    if not os.path.isdir(target_dir):
        print(f'Error: "{directory}" is not a directory')
        return

    # List for storing info from the directory
    info_list = []

    # Finds out the info of directory and files from the target directory
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)

        is_dir = os.path.isdir(item_path)
        file_size = os.path.getsize(item_path)

        line = f"- {item}: file_size={file_size}, is_dir={is_dir}"
        info_list.append(line)

    # Function for output semantics
    if info_list is []:
        print(f"Error: {directory} is empty.")
    else:
        for line in info_list:
            print(line)
