import re


def select_file_name(file_name):
    pattern = r'.+(?=\.)'
    return re.search(pattern, file_name).group()

def cut_off_extension_from_filename(file_name):
    pattern = r'.\w+$'
    return re.sub(pattern,'', file_name)


def select_file_extension(file_name):
    pattern = r'(?<=\.).+'
    return re.search(pattern, file_name).group()


def list_string_way(file_name):
    return file_name.split('.')


if __name__ == '__main__':
    assert select_file_name(
        'Эдгар Уоллес. Тайна булавки. Главы 1-3..mp4') == 'Эдгар Уоллес. Тайна булавки. Главы 1-3.'

    assert cut_off_extension_from_filename(
        'Эдгар Уоллес. Тайна булавки. Главы 1-3..mp4') == 'Эдгар Уоллес. Тайна булавки. Главы 1-3.'
