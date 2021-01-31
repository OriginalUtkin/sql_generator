def get_file_content(filename: str):
    content = None

    with open(filename, "r") as file:
        content = file.read()

    return content
