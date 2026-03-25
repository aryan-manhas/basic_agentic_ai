import os


def get_files_info(working_directory, directory="."):
    working_directory_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_path, directory))

    valid_target_dir = (
        os.path.commonpath([working_directory_path, target_dir])
        == working_directory_path
    )

    if directory == ".":
        print("Result for current directory:")
    else:
        print(f"Result for {directory} directory:")

    if valid_target_dir is False:
        print(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )
        return

    if not os.path.isdir(target_dir):
        print(f'Error: "{directory}" is not a directory')
        return

    info_list = []

    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)

        is_dir = os.path.isdir(item_path)
        file_size = os.path.getsize(item_path)

        line = f"- {item}: file_size={file_size}, is_dir={is_dir}"
        info_list.append(line)

    if info_list is []:
        print(f"Error: {directory} is empty.")
    else:
        for line in info_list:
            print(line)
