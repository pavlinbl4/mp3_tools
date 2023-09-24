from mutagen.mp4 import MP4

from path_and_name import der_path, file_name_and_dir_path


def get_mp4_cover(path_to_media_file):

    file_name, dir_path = file_name_and_dir_path(path_to_media_file)

    video = MP4(path_to_media_file)
    cover_art = video["covr"][0]
    with open(f"{dir_path}/{file_name}_cover.jpg", "wb") as f:
      f.write(cover_art)


if __name__ == '__main__':
    get_mp4_cover('/Volumes/big4photo/Movies/Youtube/Роман "Тайна булавки". Эдгар Уоллес./Эдгар Уоллес. Тайна булавки. Главы 1-3..mp4')