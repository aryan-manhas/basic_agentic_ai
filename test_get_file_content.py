from functions.get_files_content import get_file_content


def test():
    get_file_content("calculator", "main.py")
    get_file_content("calculator", "pkg/calculator.py")
    get_file_content("calculator", "/bin/cat")
    get_file_content("calculator", "pkg/does_not_exist.py")


if __name__ == "__main__":
    test()
