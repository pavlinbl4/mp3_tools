import os


def find_files(dir_path, extension):  # find all files with extension in directory
    return [f for f in os.listdir(dir_path) if f.endswith(extension)]
