from converter.filename_or_extension import select_file_name
from converter.files_work import find_files

from converter.mp3_converter import convert_mp4_to_mp3
from tkinter import filedialog


def select_folder():
    return filedialog.askdirectory()


def work_with_file(folders_paths, extension, final_extension):
    files_list = find_files(folders_paths[1], extension)  # files list
    for file in files_list:
        convert_mp4_to_mp3(f'{folders_paths[1]}/{file}',
                           f'{folders_paths[2]}/{select_file_name(file)}.{final_extension}')
