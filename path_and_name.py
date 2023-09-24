from pathlib import Path

from converter.filename_or_extension import cut_off_extension_from_filename


def der_path(path_to_image):
    # Using pathlib.Path.parent
    file_name = Path(path_to_image).name
    dir_path = Path(path_to_image).parent
    return file_name, dir_path


def file_name_and_dir_path(full_path):
    # Splitting the string on slash and joining back
    dir_path = '/'.join(full_path.split('/')[:-1])
    file_name_no_extension = cut_off_extension_from_filename(full_path.split('/')[-1])
    return file_name_no_extension, dir_path

if __name__ == '__main__':
    print(file_name_and_dir_path(
        '/Volumes/big4photo/Movies/Youtube/Роман "Тайна булавки". Эдгар Уоллес./Эдгар Уоллес. Тайна булавки. Главы 1-3..mp4'))
