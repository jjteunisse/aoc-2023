def read_from_file(file_location: str):
    file_lines = []
    for line in open(file_location).readlines():
        file_lines.append(line.strip())

    return file_lines
